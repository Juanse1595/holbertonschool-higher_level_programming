#!/bin/bash
#  Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -o /dev/null -sw "%{size_download}\n" "$1" # curl -s 0.0.0.0:5000 | wc -c;; curl -sI "$1" | grep "Content-Length" | cut -d " " -f2