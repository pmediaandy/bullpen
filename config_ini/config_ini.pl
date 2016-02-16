#!/usr/bin/perl

use Config::IniFiles;
use Getopt::Long;

my $section;
my $key;
my $value;
my $read;
my $write;
my $exist;

sub usage {
    print "usage: $0 [options] file\n";
    print "       -r, --read\n";
    print "       -w, --write\n";
    print "       -s SECTION, --section=SECTION\n";
    print "       -k KEY, --key=KEY\n";
    print "       -v VALUE, --value=VALUE\n";
    exit 1;
}

$result = GetOptions("section=s" => \$section, 
                     "key=s" => \$key, 
                     "value=s" => \$value, 
                     "exist" => \$exist,
                     "read" => \$read, 
                     "write" => \$write);

usage unless $section;

if(!defined($exist)) {
    usage unless $key && ($read || ($write && $value));
}

usage if $#ARGV < 0;

$cfg_file = $ARGV[0];
$cfg = new Config::IniFiles(-file => $cfg_file);

if($read) {
    if($cfg->exists($section, $key)) {
        print $cfg->val($section, $key), "\n";
    }
    else {
        print "[$section] $key not found", "\n";
        exit 1;
    }
}
elsif($write) {
    $cfg->setval($section, $key, $value);
    $cfg->RewriteConfig();
}
elsif($exist) {
    if(defined($key)) {
        exit !$cfg->exists($section, $key);
    }
    else {
        exit !$cfg->SectionExists($section);
    }
}
