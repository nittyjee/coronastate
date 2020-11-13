#!/bin/bash
#convert geojson to newline json
cat /home/nittyjee/code/coronastate/data/layers/adm0.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/adm0_nl
#Delete first
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm0-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

#Create
curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm0-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/adm0_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm0-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_adm0.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm0-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"
sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/adm1_bunch1.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/adm1_bunch1_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm1_bunch1-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm1_bunch1-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/adm1_bunch1_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm1_bunch1-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_adm1_bunch1.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm1_bunch1-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"
sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/adm1_bunch2.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/adm1_bunch2_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm1_bunch2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm1_bunch2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/adm1_bunch2_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm1_bunch2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_adm1_bunch2.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm1_bunch2-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"
sleep 2m
#adm2 is a big file, and jq didn't work.
geojson2ndjson /home/nittyjee/code/coronastate/data/layers/adm2.geojson > /home/nittyjee/code/coronastate/data/layers/adm2_nl
#cat /home/nittyjee/code/coronastate/data/layers/adm2.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/adm2_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/adm2_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_adm2.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm2-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"
sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/adm3.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/adm3_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm3-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm3-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/adm3_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm3-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_adm3.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm3-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/adm3_healthmap.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/adm3_healthmap_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm3_healthmap-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/adm3_healthmap-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/adm3_healthmap_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm3_healthmap-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_adm3_healthmap.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.adm3_healthmap-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"


sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/static_adm1.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/static_adm1_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm1-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm1-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/static_adm1_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm1-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_static_adm1.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm1-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/static_adm2.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/static_adm2_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/static_adm2_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm2-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_static_adm2.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm2-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/static_adm3.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/static_adm3_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm3-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm3-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/static_adm3_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm3-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_static_adm3.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm3-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"


sleep 2m
cat /home/nittyjee/code/coronastate/data/layers/static_adm3_healthmap.geojson | jq -c ".features[]" > /home/nittyjee/code/coronastate/data/layers/static_adm3_healthmap_nl
curl -X DELETE "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm3_healthmap-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"

curl -X POST "https://api.mapbox.com/tilesets/v1/sources/coronastate/static_adm3_healthmap-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"    -F file=@/home/nittyjee/code/coronastate/data/layers/static_adm3_healthmap_nl    --header "Content-Type: multipart/form-data"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm3_healthmap-test?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"  -d @/home/nittyjee/code/coronastate/data/layers/recipe_static_adm3_healthmap.json  --header "Content-Type:application/json"
curl -X POST "https://api.mapbox.com/tilesets/v1/coronastate.static_adm3_healthmap-test/publish?access_token=sk.eyJ1IjoiY29yb25hc3RhdGUiLCJhIjoiY2s5amVwNnJzMDJqODNuc2MxdDBwZGV0NyJ9.e8ftqhU0EuCVz5T4EYMShw"
