wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1Zly3p3i7sc-ikg5CPg-GqTv19gzp29fo' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1Zly3p3i7sc-ikg5CPg-GqTv19gzp29fo" -O models.zip && rm -rf /tmp/cookies.txt
unzip models.zip -d models/
rm models.zip
