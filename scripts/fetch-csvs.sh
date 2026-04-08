git pull origin main
wget 'https://github.com/joachimvandekerckhove/cogs205b-s26/raw/refs/heads/main/modules/02-version-control/files/data.zip'
unzip data.zip  -d /workspace/COGS205-complabskills/temp
current_date=$(date +%F)
mkdir -p /workspace/COGS205-complabskills/data/$current_date/
cp /workspace/COGS205-complabskills/temp/*.csv /workspace/COGS205-complabskills/data/$current_date/
git add data/
git add scripts/
git commit -m "HW2: commit data csv files & script"
git push origin main
