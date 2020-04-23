#!/bin/bash

usage(){
  echo "Usage: -volumes -cpu -ram -network -all"}
  exit 1
}

[[ $# -eq 0 ]] && usage

while [[ ! -z "$1" ]]; do
  case "$1" in
    -volumes)
      shift
      echo "list number of volumes, size of each volume, free space on each volume"
      df -h
      ;;
    -cpu)
      shift
      echo "cpus/cores info"
      sysctl -n hw.ncpu
      sysctl -n machdep.cpu.brand_string
      ;;
    -ram)
      echo "amound of RAM"
      sysctl hw.memsize
      shift
      ;;
    -network)
      echo "mac address"
      ifconfig en1 | awk '/ether/{print $2}'
      echo "IP address"
      ipconfig getifaddr en1
      shift
      ;;
    -all)
      ./devops01a.sh
      shift
      ;;
    *)
      usage
      ;;
  esac
  shift
done

exit 0

#if [[ "$*" == "-volumes" ]]; then
#  echo "list number of volumes, size of each volume, free space on each volume"
#  df -h
#elif [[ "$*" == "-cpu" ]]; then
#  echo "cpus/cores info"
#  sysctl -n hw.ncpu
#  sysctl -n machdep.cpu.brand_string
#elif [[ $* == "-ram" ]]; then
#  echo "amound of RAM"
#  sysctl hw.memsize
#elif [[ $* == "-network" ]]; then
#  echo "mac address"
#  ifconfig en1 | awk '/ether/{print $2}'
#  echo "IP address"
#  ipconfig getifaddr en1
#elif [[ $* == "-all" ]]; then
#  ./devops01a.sh
#else
#  usage
#fi