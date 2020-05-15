#-*- coding: utf-8 -*-
#import syl_seg
import os
LEXICON = "itc_kh_lex.out"

def load_dict(filename):
    res = {}
    for line in open(filename):
    	try:
            res[line.split('"')[1].decode("utf-8").strip()] = 1
        except:
            pass
    return res

def get_min_len(p):
    res = len(p[0])
    for each_sent in p:
        if res > len(each_sent):
            res = len(each_sent)
    return res

def get_sent_with_minimum_len(p):
    min_len = get_min_len(p)
    res = [sent for sent in p if len(sent) == min_len]
    return res

def post_process(sent):
    res = []
    i = 0
    while i < len(sent):
        # go to the first word with 1 char
        while i < len(sent) and len(sent[i]) != 1: 
            res.append(sent[i])
            i += 1
        if i >= len(sent): break
        syls = []
        i0 = i
        # go to the first word with more than 1 char
        while i < len(sent) and len(sent[i]) == 1: 
            syls.append(sent[i])
            i += 1
        if sent[i0] >= u"ា" and sent[i0] <= u"្":
            syls.insert(0, res[-1])
            del res[-1]
        if sent[i-1] in u"្័៌":
            syls.append(sent[i])
            i += 1
        res.append("".join(syls))
        #print res[-1]
    i = 0
    while i < len(res):
        if len(res[i]) == 2 and res[i][1] in u"់៍":
            res[i-1] += res[i]
            del res[i]
        i += 1
    return " ".join(res)

def word_segmentation(sentence, kh_dict):
    if sentence == "": return sentence
    sent_len = len(sentence)
    p = [0] * sent_len
    p[-1] = [(sentence[-1],)]
    for i in reversed(range(sent_len-1)):
        p[i] = []
        for j in range(i, sent_len):
            first_word = sentence[i:j+1]
            if i == j or first_word in kh_dict:
                if j != sent_len - 1:
                    for each_sent in p[j+1]:
                        p[i].append((first_word,)+each_sent)
                else:
                    p[i].append((first_word,))
#            else:
#                break
        p[i] = get_sent_with_minimum_len(p[i])
    res = post_process(p[0][0])
    return res

def read_input_sentence(filename):
    return open(filename).read().decode("utf-8")

def write_output_sentence(filename, sentence):
    f = open(filename, "w")
    f.write(sentence.encode("utf-8"))
    f.close()
indir='/home/dotaplus/Documents/kh_new_seg/word_seg/test/'
outdir='/home/dotaplus/Documents/kh_new_seg/word_seg/data/'
def main():
    for root, dirs, filenames in os.walk(indir):
    	for f in filenames:
		print f
    		text = read_input_sentence(indir+f)
    		res  = segment_text(text)
    		tt=res.replace(' ','\n').replace('\n\n\n','')
    		write_output_sentence(outdir+f, tt)
    		print "finish"

def segment_text(text):
    kh_dict = load_dict(LEXICON)
    text = text.replace(u"​", "").replace(" ","")
    res = ""
    i = 0
    while i < len(text):
        i0 = i
        # go to the first khmer char (char used to write khmer word)
        while i < len(text) and (text[i] < u"ក" or text[i] > u"្") : i += 1
        if i != i0: res += text[i0:i] + " "
        start_sent = i
        # go to the first non khmer char (char used to write khmer word)
        while i < len(text) and (text[i] >= u"ក" and text[i] <= u"្")  : i += 1
        res += word_segmentation(text[start_sent:i], kh_dict) + " "
    res = res.replace(" ,", ", ")
    return res

if __name__ == '__main__':
    main()
