#!/bin/bash
python3 generate.py
git add .
git commit -m "sync auto"
git push origin master
