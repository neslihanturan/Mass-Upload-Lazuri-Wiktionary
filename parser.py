#! /usr/bin/python
# -*- coding: utf-8 -*-

import json

json_file = 'Desktop/lazuri/lazuri.json'

with open(json_file, 'r') as content_file:
    content = content_file.read()

records = json.loads(content)
turkceList = []

for record in records:
    turkceler = record["turkish_meaning"].split("|")
    wikitext = "{{-start-}}\n"+"'''{}'''\n".format(record["form"])+"==Lazca==\n===İsim===\n{{başlık başı|lzz|ad}}"
    for i,turkce in enumerate(turkceler):
         wikitext = wikitext + "\n:[{0}] {1}".format(i+1, turkce)
    wikitext = wikitext +"\n[[Kategori:Lazca sözcükler]]"+"\n{{-stop-}}\n\n"
    print (wikitext)
    with open('Desktop/lazuri/lazuriTargetTr.json', 'a') as targetFile:
        targetFile.write(wikitext)
    
    turkcelist = []
    wikitext = []
   

    lazcalar = record["form"].split("|")
    ingilizceler = record["english_meaning"].split("|")






