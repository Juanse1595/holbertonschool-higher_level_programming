#!/bin/bash
# Bash script that sends a request to that URL and displays the size
curl -sI "$1" | grep Content-Length | cut -d " " -f 2