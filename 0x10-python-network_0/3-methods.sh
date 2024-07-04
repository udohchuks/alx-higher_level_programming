#!/bin/bash
# Displays all HTTP methods the server will accept for the given URL
curl -sI "$1" | grep "Allow:" | cut -d ' ' -f2-
