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
				fname = file.replace('.txt','.lab')
				w.write('"*/'+fname+'"')
				w.write('\n')
				te = re.replace('_','')
				w.write(te)
				w.write('\n')
				w.write('.')
				w.write('\n')
        		#if filepath.endswith(".wav"):
            			#print (file)
				#re = file.replace('.wav','.mfcc')
				#w.write('./wav/'+file+' '+'./mfcc/'+re)
				#w.write('\n')

