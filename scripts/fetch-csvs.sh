wget 'https://github.com/joachimvandekerckhove/cogs205b-s26/raw/refs/heads/main/modules/02-version-control/files/data.zip'
unzip data.zip  -d /workspace/COGS205-complabskills/temp
current_date=$(date +%F)
cp "*.csv" /workspace/COGS205-complabskills/data/$current_date
