#!/bin/bash

cmd=$1
name=$2
cpu_seconds=$3
output=$6
err=$7
shift 7

EXECUTING_COMMAND="${cmd} ${@} > ${output} 2> ${err}"
sh -c "timeout ${cpu_seconds} $EXECUTING_COMMAND &"
