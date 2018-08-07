#!/bin/sh

dir=`dirname $0`
echo $dir
cd $dir
for count in {1..50}; do
    echo "$dir run #$count `date`"
    /builds/scriptworker/bin/python /builds/scriptworker/bin/signingscript script_config.json 2>&1 > log.$count
    status=$?
    echo "Exited $status" >> log.$count
    echo "$dir run $count exited $status `date`"
done
