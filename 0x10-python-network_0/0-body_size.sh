#!/bin/bash
# Bash script that sends a request to that URL and displays the size
curl -o /dev/null -sw "%{size_download}\n" "$1"