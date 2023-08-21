#!/usr/bin/env bash

git log --grep 'ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}' | grep -o 'ctf{[a-zA-Z0-9_!?#.:*\-]\{8,32\}}'