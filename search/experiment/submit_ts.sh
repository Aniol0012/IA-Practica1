#!/bin/bash

cmd=$1
name=$2
slots=$3
output=$4
err=$5
shift 5

EXECUTING_COMMAND="${cmd} ${@} > ${output} 2> ${err}"
ts -L $name -n -N ${slots} sh -c "$EXECUTING_COMMAND"
