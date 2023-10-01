#!/bin/bash

# Default IP and port
IPS="127.0.0.1"
PORT="14550"

while getopts "i:p:" opt; do
  case $opt in
    i) IPS="$OPTARG"
    ;;
    p) PORT="$OPTARG"
    ;;
    \?) echo "Invalid option -$OPTARG" >&2
    ;;
  esac
done

# Connect to the USBtty* or ACM* (you may need to adjust this logic)
DEVICE=$(ls /dev | grep -E 'ttyUSB|ACM' | head -n 1)
if [ -z "$DEVICE" ]; then
    echo "No device found"
    exit 1
fi

# Start mavproxy
mavproxy.py --master=/dev/$DEVICE --out=$IPS:$PORT

