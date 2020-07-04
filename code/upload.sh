#!/bin/bash
cd /home/nittyjee/code/coronastate/
git pull
git add .
git add \*.csv
git commit -a -m 'upload data'
git push
echo 'done'
