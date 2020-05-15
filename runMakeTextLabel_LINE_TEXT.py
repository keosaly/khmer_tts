#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import os
rootdir='/home/dotaplus/Documents/kh_new_seg/text/'
with open("./fullTextLabel.txt", "w") as w:
	for subdir, dirs, files in os.walk(rootdir):
    		for file in files:
        		filepath = subdir + os.sep + file
			with open(filepath, "r") as r:
				fr=r.read()
				re=fr.replace("\u200b","")
				print file
				fname = file.replace('.txt','')
				w.write('( "'+fname+' "')
				te = re.replace('_','')
				te1 = te.replace('។ ','។ " )')
				w.write(te1)
			
				w.write('\n')
        		#if filepath.endswith(".wav"):
            			#print (file)
				#re = file.replace('.wav','.mfcc')
				#w.write('./wav/'+file+' '+'./mfcc/'+re)
				#w.write('\n')

