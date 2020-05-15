import os
"""
Renames the multiple file within the same directory with appending number
"""
path = './text'
files = os.listdir(path)
i = 1

for file in files:
    	filename, file_extension = os.path.splitext(file)
    #os.rename(os.path.join(path, file), os.path.join(path, filename + str(i) + file_extension))
    	i = i+1
	text1=filename.replace('KM001_BTEC1_','kh_atr_m001_a')
	tt=text1.replace('_T01','')
	text2=tt.replace('.w','')
	
	#text2=filename.replace('.txt','')
	#text3=text2.replace('.w.wlist.pho','')
	#text4=text3.replace('.pho','')
	#text5=text4.replace('._T01','')
	file_extension = '.txt'
	os.rename(os.path.join(path, file), os.path.join(path, text2+file_extension))
	print text2,filename
