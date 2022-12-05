#!/bin/bash
filename=$1
python3 custom_ssl.py $filename
python3 ssl_checker.py -f output.csv | tee output
echo "curl" > desire.csv
grep "Connection refused" output | awk '{ print $2}'  >> desire.csv
python write_to_file.py 
