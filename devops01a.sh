#!/bin/sh -e

echo "list number of volumes, size of each volume, free space on each volume"
df -h

echo "number of cpus/cores"
sysctl -n hw.ncpu

echo "info about the cpus/cores"
sysctl -n machdep.cpu.brand_string

echo "amound of RAM"
sysctl hw.memsize

echo "mac address"
ifconfig en1 | awk '/ether/{print $2}'

echo "IP address"
ipconfig getifaddr en1