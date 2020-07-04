#!/bin/bash
cd /home/nittyjee/code/coronastate/code/
./node_modules/.bin/babel-node index.js

python /home/nittyjee/code/coronastate/code/update_geocoding_from_jhu.py > /home/nittyjee/code/coronastate/code/Process5.log
/usr/local/bin/python3.8 /home/nittyjee/code/coronastate/code/process_healthmap.py 2>&1> /home/nittyjee/code/coronastate/code/process_healthmap.log
python /home/nittyjee/code/coronastate/code/preprocess_India_Districts.py 2>&1> /home/nittyjee/code/coronastate/code/preprocess_India_Districts.log
python /home/nittyjee/code/coronastate/code/Process1.py > /home/nittyjee/code/coronastate/code/Process1.log
sleep 5
python /home/nittyjee/code/coronastate/code/Process2.py > /home/nittyjee/code/coronastate/code/Process2.log
python /home/nittyjee/code/coronastate/code/Process4.py > /home/nittyjee/code/coronastate/code/Process4.log
python /home/nittyjee/code/coronastate/code/Process6.py > /home/nittyjee/code/coronastate/code/Process6.log
sleep 5
#/usr/local/bin/python3.8 /home/nittyjee/code/coronastate/code/copy_from_source_to_rawdata.py > /home/nittyjee/code/coronastate/code/copy_from_source_to_rawdata.log
./update_map_tileset.sh 

./upload.sh
