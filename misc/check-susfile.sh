#!/bin/sh

archive='files'

function check {
    input_file=$1
    output_dir=$2

    if [ ! -d $output_dir ]; then mkdir $output_dir; fi 

    count=0
    det_cnt=0
    total=`wc -l $input_file | awk '{print $1}'`

    while read line
    do
        count=$((count+1))
        stamp=`printf "%d/%d" $count $total`
        url=`echo $line | awk '{sub(/hxxp/, "http", $2); print $2}'`
        wget -T 10 -t 1 -q -O output "$url"
        if [ $? -eq 0 ]; then
            name=`sha1sum output | awk '{print $1}'`
            mv output $name
            if [ -e "$archive/$name" ]; then
                rm $name 
                if [ -e "$archive/$name.url" ]; then
                    det_cnt=$((det_cnt+1))
                    echo $stamp detected before
                else
                    echo $stamp skip
                fi 
            else
                mv $name $archive
                file $archive/$name
                avgscan $archive/$name > report
                ra=$?
                clamscan $archive/$name >> report
                rc=$?
                if [ $ra -eq 0 ] && [ $rc -eq 0 ]; then
                    echo $stamp no detect
                else
                    det_cnt=$((det_cnt+1))
                    echo $name $url > $archive/$name.url
                    cat report >> $archive/$name.url
                    cd $output_dir
                    ln -s ../$archive/$name .
                    ln -s ../$archive/$name.url .
                    cd ..
                    echo $stamp virus on $url
                fi
                rm report
            fi
        else
            echo $stamp not found 
            rm output
        fi
    done < $input_file 
    return $det_cnt
}


if [ "$#" -lt 1 ]; then
    echo $0 input_file 
    exit 1
fi

file=$1

if [ ! -d $archive ]; then mkdir $archive; fi

dir=`echo $file | cut -c 15-18`
check $file $dir
echo $? found!

