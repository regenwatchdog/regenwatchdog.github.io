#!/usr/bin/env python

import PyPDF2
pdfFileObj = open('/tmp/metadata.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
search_word = "council"
search_word_count = 0
    for pageNum in range(1, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText().encode('utf-8')
        search_text = text.lower().split()
        for word in search_text:
            if search_word in word.decode("utf-8"):
                search_word_count += 1
            
print("The word {} was found {} times".format(search_word, search_word_count))



