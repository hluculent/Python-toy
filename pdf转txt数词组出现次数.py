#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import re

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO

#convert pdf to text， extract from PDFminer, ignoring everything but english words
def pdf_to_text(root):
    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Extract text
    fp = file(root, 'rb')
    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
    fp.close()
    # Get text from StringIO
    text = sio.getvalue()
    # Cleanup
    device.close()
    sio.close()

    return text

#count M&A and [Mm]ergers and [Aa]cquisitions
def words_count(text, root):
    count = 0
    count = len(re.findall(r'[M|m]ergers and [A|a]cquisitions', text)) + len(re.findall(r'M&A', text))
    #there are many way to use regular expression, re.search and re.match will returen a value as soon as it finds one
    if count == 0:
        os.remove(root) 
    return count

#if count=0 remove this file from the directory
    

#create a new text to store pdfname and words_count, then convert it to excel
def write_into_txt(pdfname, count):
    database = open('database.txt', 'a')
    database.write(pdfname + "\t" + str(count) + '\n')
    database.close()

#create a pdf path and read one by one, maybe there are more than one folder
def main():
    path = u'E:\\最近任务\\实习资料\\姚老师\\2.7_R_to_Python'
    
    for rt, dirs, files in os.walk(path):
        for f in files:
            if not f.endswith('.pdf'):
                continue
            else:
                pdfname = os.path.join(f)
                root = os.path.join(rt,f)
                text = pdf_to_text(root)
                count = words_count(text,root)
                write_into_txt(pdfname, count)
        for f in dirs:
            if not f.endswith('.pdf'):
                continue
            else:
                pdfname = os.path.join(f)
                root = os.path.join(rt,f)
                text = pdf_to_text(root)
                count = words_count(text,root)
                write_into_txt(pdfname, count)

if __name__ == '__main__':
  main()
