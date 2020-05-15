import os

def find_prev_next(elements,wordList,pos,subpos):
	#print 'POS::::',pos,'SUB::::',subpos
    	bf_pre='X'	
    	pre='X'
    	after_next='X'
    	next='X'
	countData = len(wordList[pos-2])
	if pos == 1:
		if subpos == 0:
			bf_pre='X'
			pre='X'
		elif subpos == 1:
			bf_pre='X'
			pre=elements[subpos-1]
		else:
			bf_pre=elements[subpos-2]
			pre=elements[subpos-1]
	else:

		if subpos == 0:
			if countData > 1:
				bf_pre=wordList[pos-2][countData-2]
				pre=wordList[pos-2][countData-1]
			else:
				cn = len(wordList[pos-3])
				pre=wordList[pos-2][countData-1]
				bf_pre=wordList[pos-3][cn-1]
				#if elements[subpos-1] == 'sil':
				if pre == 'sil':
					bf_pre = 'X'
		elif subpos == 1:
			bf_pre=wordList[pos-2][countData-1]
			#bf_pre='SAM70'
			pre=elements[subpos-1]	
		else:
			bf_pre=elements[subpos-2]
			pre=elements[subpos-1]

	
	#---- find next
	word = len(wordList)
 	if word > pos:	
		cnum = wordList[pos]
		countNext = len(elements)-1
		if countNext > subpos+1:
			next = elements[subpos+1]
			after_next = elements[subpos+2]
		else:
			if len(elements) > subpos+1:
				next = elements[subpos+1]
				after_next = wordList[pos][0]
			else:
				next = wordList[pos][0]
				if len(wordList[pos])>1:
					after_next = wordList[pos][1]
				elif len(wordList[pos])==1 and pos < len(wordList)-1:
					after_next = wordList[pos+1][0]
					#after_next = 'YYYY'
					#print wordList[pos][0]
					#wordList[pos+1][0]
				else:
					after_next = 'X'
					#print wordList[pos][0],wordList
		
	
	return bf_pre, pre, next,after_next
def find_prev_index(index,all_elements):
	pre='X'
	db_pre='X'
	allpos=all_elements[index-1]
	sub=len(allpos)
	
	pre=allpos[sub-1]
	db_pre=allpos[sub-2]
	#db_pre=all_elements[index-2]
	return db_pre,pre

def find_prev_next_con_pos_word(elem, elements,i):
    	#pre,con,next = None,None,None
    	pre='X'
    	con='X'
    	next='X'
    	index = elements.index(elem)
	conWord = len(elements)
    	con = len(elem)
    	if index > 0:
       		pre = len(elements[index-1])
    	if index < (len(elements)-1):
        	next = len(elements[index+1])
		#if (i+2)==conWord and elements[conWord-1][0]=='PAU':
		if (i+2)==conWord and elements[conWord-1][0]=='sil':
			next = 'X'
		#print conWord,i+2,elements[conWord-1]
	#print con,elem,next,elements[i]
	if i < conWord-1:
		print elements[i+1]
	 	if elements[i+1][0] == 'pm':
			next = 'X'
			print con,next,elements[i+1][0]
		elif elements[i-1][0] == 'pm' or elements[i-1][0] == 'sil':
			pre = 'X'
	if elements[i-1][0] == 'pm' or elements[i-1][0] == 'sil':
                        pre = 'X'		
    	return pre,con,next

indir = './phos/'   
#-----------------------------Work for convert pho to kh-context lables.
def apply_context_lable_kh(file_pho):
	allList = []
	list = []
	subList = []
	countWord = 0
	countTotalWord = 0
	path = indir+file_pho
	with open(path,'r') as f:
        	read_data = f.read()
        	countWord = read_data.count('#')
        	if(read_data.split()!=''):
                	for line in read_data.split():
                        	list.append(line)
				if(line == '#'):
					allList.append(subList)
                                	subList = []
					countTotalWord+=1
				else:
					subList.append(line)
		
				if (line == 'pm'):
					countTotalWord-=1
				elif (line == 'qm'):
					countTotalWord-=1
				elif (line == 'sil'):
					countTotalWord-=1
	print '---------------------- START ----------------------',file_pho,countTotalWord
	countFirstWord = -1
	str_result = ''
	i = 0
	pnum = len(allList)
	for alldata in allList:
    		countFirstPos = 0
   		countFirstWord+=1
		if(allList[i][0]=='pm'):
			countFirstWord -= 1
		countEndWord = (countTotalWord+1)-countFirstWord
    		getCountPre,getCon,getCountNext=find_prev_next_con_pos_word(alldata,allList,i)
		i += 1
    	#print '===== get Cound of pos in word  ========',getCountPre,getCon,getCountNext
		j = 0
    		for data in alldata:
        		foo = data
        		countFirstPos+=1
			status = 'S0'
        		countEndPos = (len(alldata)+1)-countFirstPos
        		bf_previous, previous, next, after_next = find_prev_next(alldata,allList,i,j)
			j += 1
			if foo == 'pm':
				str_result=str_result+str(bf_previous)+'^'+str(previous)+'-'+str(foo)+'+'+str(next)+'='+str(after_next)+'/PHN2:'+'X'+'_'+'X'+'/WRD1:'+'#X'+'-'+'#X'+'+'+'#'+str(getCountNext)+'/WRD2:'+'X'+'_'+'X'+'/UTTF:'+'X'+'_'+'X'
                                str_result +='\n'
			elif foo == 'sil': 
				#and i == pnum:
				countFirstPos='X'
				countEndPos='X'
				getCountPre='X'
				getCon='X'
			
				getCountNext='X'
				strFirstWord='X'
				strEndWord='X'
				strTotalWord='X'
				status='X'
				str_result=str_result+str(bf_previous)+'^'+str(previous)+'-'+str(foo)+'+'+str(next)+'='+str(after_next)+'/PHN2:'+'X'+'_'+'X'+'/WRD1:'+'@X'+'-'+'&X'+'+'+'#X'+'/WRD2:'+'X'+'_'+'X'+'/UTTF:'+'X'+'_'+'X'				
                        	str_result +='\n'
			else:	
        			str_result=str_result+str(bf_previous)+'^'+str(previous)+'-'+str(foo)+'+'+str(next)+'='+str(after_next)+'/PHN2:'+str(countFirstPos)+'_'+str(countEndPos)+'/WRD1:'+'@'+str(getCountPre)+'-'+'&'+str(getCon)+'+'+'#'+str(getCountNext)+'/WRD2:'+str(countFirstWord)+'_'+str(countEndWord)+'/UTTF:'+str(countTotalWord)+'_'+status
				str_result +='\n'
				#print str_result
			#print str_result
			#print str_result
	saveToLab(str_result,file_pho)
       	str_result = ''
	

def saveToLab(result,fName):
	with open('./lab/'+fName+'.lab','w') as wf:
		wf.write(result)

		wf.close()
for root, dirs, filenames in os.walk(indir):
    for f in filenames:
        apply_context_lable_kh(f)



