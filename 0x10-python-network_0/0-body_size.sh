#!/bin/bash
# Bash script that sends a request to that URL and displays the size
curl -o /dev/null -s -w "%{size_download}\n" "$1"