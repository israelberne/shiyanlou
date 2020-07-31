#!/bin/bash

if [ $# -ne 4 ] #The number of the argument must be equal to 4  
then
    echo "parameter error"
    exit 0 
fi

expr $4 + 0 &> /dev/null
if [ $? -ne 0 ] || [ $4 -gt 10 ] || [ $4 -lt 1 ] #The fourth argument must be integer and between 1-10
then
    echo "paramater error"
    exit 0 
fi

if [[ ! $3 =~ ^[a-z]+$ ]] #The third argument can be any lowercase letter.
then
    echo "parameter error"
    exit 0 
fi

function add_user(){ #Define a function-create user
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

function del_user(){ #Define a function-delete user
    if `id $1 &> /dev/null`
    then
        userdel $1
    fi
}

if [ $1 == 'add' ] #Specify how to use the function by the first argument.
then
    add_user $2
    for i in `seq $4`
    do
        add_user $3$i
    done

elif [ $1 == 'del' ]
then
    del_user $2
    for i in `seq $4`
    do 
        del_user $3$i
    done
fi
