#!/bin/bash
# Sends a request to the given URL and displays only the status code of the response
awk 'NR==1{printf "%s", $2}' test7 $(curl -sI "$1" -o test7)
