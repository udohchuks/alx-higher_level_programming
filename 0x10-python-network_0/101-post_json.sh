#!/bin/bash
# Sends a JSON POST request to the URL passed as the first argument, using the JSON contents from a file passed as the second argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
