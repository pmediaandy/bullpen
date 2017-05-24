#!/usr/bin/python3.5

import elasticsearch
import elasticsearch.helpers
import ujson
import pymysql
import http.client
import os
import hashlib
import datetime
import argparse

es = None

def setup_es(args):
    es = elasticsearch.Elasticsearch([{'host': args.es_host, 'port': args.es_port}])
    return es

def delete_index(args):
    ans = input('Are you sure to delete index `%s\'? [yes/NO] ' % args.index)
    if ans == 'yes':
        res = es.indices.delete(index = args.index)
        print(res)
    else:
        print('abort')

def create_index(args):
    if args.schema is None:
        print('Missing schema file')
        return
    with open(args.schema, 'r') as f:
        mapping = ujson.loads(f.read())
    res = es.indices.create(index = args.index, body = mapping)
    print(res)

def update_index(args):
    print('update')

def list_index(args):
    res = es.indices.get_alias()
    for idx in sorted(res.keys()):
        print('%s\t\t%s %s' % (idx, '<=' if len(res[idx]['aliases']) else '', ','.join(res[idx]['aliases'].keys())))

def reindex(args):
    if args.dest_index is None:
        print('Missing dest index')
        return
    ans = input('Are you sure to reindex from `%s\' to `%s\'? [yes/NO] ' % (args.index, args.dest_index))
    if ans == 'yes':
        res = elasticsearch.helpers.reindex(client = es, source_index = args.index, target_index = args.dest_index, target_client = es)
        print(res)
    else:
        print('abort')

def remapping(args):
    if args.dest_index is None:
        print('Missing dest index')
        return
    if args.remapping is None:
        print('Missing remapping file')
        return
    else:
        with open(args.remapping, 'r') as f:
            remap = ujson.loads(f.read())
    ans = input('Are you sure to remap from `%s\' to `%s\' with mapping file `%s\'? [yes/NO] ' % (args.index, args.dest_index, args.remapping))
    if ans == 'yes':
        es2 = elasticsearch.Elasticsearch([{'host': args.es_host, 'port': args.es_port}])
        page = es.search(index = args.index, body = {"query" : {"match_all" : {}}}, scroll = '2m', size = 1000)
        cnt = 0
        while True:
            sid = page['_scroll_id']
            scroll_size = page['hits']['total']
            rows = page['hits']['hits']
            cnt += len(rows)
            print('scrolling - %.2f%%' % (cnt * 100.0 / scroll_size))
            
            actions = []
            for row in rows:
                source = row['_source']
                for field in remap:
                    if remap[field] is None:
                        source.pop(field, None)
                    else:
                        source[remap[field]] = source.pop(field, None)
                actions.append({'_index': args.dest_index, '_type': row['_type'], '_id': row['_id'], '_source': source})
            res = elasticsearch.helpers.bulk(es2, actions)
            print(res)

            page = es.scroll(scroll_id = sid, scroll = '2m')
            if cnt == scroll_size:
                break
    else:
        print('abort')

def add_alias(args):
    if args.dest_index is None:
        print('Missing dest index')
        return
    res = es.indices.put_alias(index = args.index, name = args.dest_index)
    print(res)

def remove_alias(args):
    if args.dest_index is None:
        print('Missing dest index')
        return
    res = es.indices.delete_alias(index = args.index, name = args.dest_index)
    print(res)

def get_schema(args):
    res = es.indices.get(index = args.index)
    mapping = res[args.index]['mappings']
    print(ujson.dumps({ 'mappings': mapping }, indent = 2, sort_keys = True))

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description = 'command-line tool for elasticsearch')
    parser.add_argument('--src-index', '-i', dest = 'index', nargs = '?', action = 'store', default = None, help = 'source index')
    parser.add_argument('--dest-index', '-j', dest = 'dest_index', nargs = '?', action = 'store', default = None, help = 'dest index to reindex, or alias name')
    parser.add_argument('--es-host', '-H', dest = 'es_host', nargs = '?', action = 'store', default = None, help = 'elasticsearch host, default read from environment variable ES_HOST')
    parser.add_argument('--es-port', '-P', dest = 'es_port', nargs = '?', action = 'store', default = None, type = int, help = 'elasticsearch port, default read from environment variable ES_PORT')
    parser.add_argument('--schema', '-s', dest = 'schema', nargs = '?', action = 'store', default = None, help = 'schema file')
    parser.add_argument('--remapping', '-M', dest = 'remapping', nargs = '?', action = 'store', default = None, help = 'remapping file')
    parser.add_argument('--create', '-c', dest = 'dispatch', action = 'store_const', const = create_index, default = None, help = 'create index')
    parser.add_argument('--list', '-l', dest = 'dispatch', action = 'store_const', const = list_index, default = None, help = 'list all indices & aliases')
    parser.add_argument('--delete', '-d', dest = 'dispatch', action = 'store_const', const = delete_index, default = None, help = 'delete index')
    parser.add_argument('--update', '-u', dest = 'dispatch', action = 'store_const', const = update_index, default = None, help = 'update index')
    parser.add_argument('--mapping', '-m', dest = 'dispatch', action = 'store_const', const = get_schema, default = None, help = 'get index mapping')
    parser.add_argument('--alias-add', '-A', dest = 'dispatch', action = 'store_const', const = add_alias, default = None, help = 'add alias')
    parser.add_argument('--alias-remove', '-D', dest = 'dispatch', action = 'store_const', const = remove_alias, default = None, help = 'remove alias')
    parser.add_argument('--reindex', '-r', dest = 'dispatch', action = 'store_const', const = reindex, default = None, help = 'reindex')
    parser.add_argument('--reindex-fields', '-R', dest = 'dispatch', action = 'store_const', const = remapping, default = None, help = 'reindex & rename fields')

    args = parser.parse_args()
    if args.es_host is None:
        try:
            args.es_host = os.environ['ES_HOST']
        except KeyError:
            print('--es-host not specified or ES_HOST is not set')
            exit(1)
    if args.es_port is None:
        try:
            args.es_port = int(os.environ['ES_PORT'])
        except KeyError:
            print('--es-port not specified or ES_PORT is not set')
            exit(1)

    if args.dispatch is None:
        parser.print_help()
    else:
        if args.index is None and args.dispatch != list_index:
            print('Missing index name')
            exit(1)
        else:
            es = setup_es(args)
            args.dispatch(args)
