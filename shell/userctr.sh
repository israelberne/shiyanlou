#!/bin/bash

if [ $# -ne 4 ] 
then
    echo "parameter error"
    exit 0 
fi

expr $4 + 0 &> /dev/null
if [ $? -ne 0 ] || [ $4 -gt 10 ] || [ $4 -lt 1 ]
then
    echo "paramater error"
    exit 0 
fi

if [[ ! $3 =~ ^[a-z]+$ ]]
then
    echo "parameter error"
    exit 0 
fi

function add_user(){
    if `id $1 &> /dev/null`
    then
        echo "$1:******"
    else
        useradd -s /usr/bin/zsh $1 &> /dev/null
        password=`cat /dev/urandom | tr -dc '0-9' | head -c 6`
        echo $password | passwd $1 --stdin
        echo "$1:$password"
    fi
}

function del_user(){
    if `id $1 &> /dev/null`
    then
        userdel $1
    fi
}

if [ $1 == 'add' ]
then
    add_user $2
    for i in `seq $4`
    do
        add_user $3$4
    done

elif [ $1 == 'del' ]
then
    del_user $2
    for i in `seq $4`
    do 
        del_user $3$4
    done
fi
