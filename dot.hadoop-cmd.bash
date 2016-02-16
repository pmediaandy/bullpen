
huser=chris_huang

hkey() {
    u=$1
    if [ -z "$u" ]; then
        u=$USER
    fi
    kinit -kt ~/$u.keytab $u
}

hrm() {
    hcmd "hadoop fs -rm -r -skipTrash $@"
}

hls() {
    hcmd "hadoop fs -ls $@"
}

hput() {
    hcmd "hadoop fs -put $@"
}

hget() {
    hcmd "hadoop fs -get $@"
}

hgetm() {
    folder=$1
    tmpn="/tmp/hgetm-$RANDOM.$$.tmp"
    hadoop fs -getmerge $folder $tmpn && mv $tmpn $folder.txt
    rm -rf .??*.crc
}

hcmd() {
    cmd=$1
    echo $cmd
    $cmd
}

hpig() {
    script=$1
    output=$2
    param=$3
    if [ -f "$script" ]; then
        if [ -z "$output" ]; then 
            echo "warning: no output folder is specified"
        else
            hcmd "hadoop fs -rm -r -skipTrash $output"
            po="-p output=$output"
        fi
        ps=$(echo "$param" | awk -F';' '{for(i=1;i<=NF;i++) printf "-p %s ", $i}END{printf"\n"}')
        hcmd "pig -f $script $ps $po"
        if [ ! -z "$output" ]; then 
            hgetm "$output"
        fi
    else
        echo pig script \'$script\' not exist
    fi
}

hkey $huser
