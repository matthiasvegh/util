#!/usr/bin/env bash

getParentPid() {
  ps -o ppid= $1
}

getDistanceFromInit() {
  ShellPid=`getParentPid $$`

  Pid=$ShellPid
  Counter=0
  while [ "$Pid" -ne "1" ]
  do
    Pid=`getParentPid $Pid`
    Counter=$((Counter+1))
  done
  echo $Counter
}

getDistanceFromInit
