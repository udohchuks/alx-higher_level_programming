#!/bin/bash
# Sends a GET request to the given URL with a custom header and displays the body of the response
curl -s -H "X-School-User-Id:98" "$1"
