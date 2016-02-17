#!/bin/bash

cmd='ssh -NfR 1314:10.1.145.4:22 chris@tor'
psr=$(ps aux | grep -v grep | grep 'ssh -NfR 1314:10.1.145.4:22 chris@tor')
if [ $? -eq 0 ]; then
    echo tunnel \"$cmd\" already exist
else
    $cmd
    echo tunnel \"$cmd\" established
fi
