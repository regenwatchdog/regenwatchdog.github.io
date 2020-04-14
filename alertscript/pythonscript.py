#!/usr/bin/env python
import requests
import PyPDF2
import re
import sys


urlsuffix = 62730 
blankcount = 0

while blankcount <= 110:
      #url = (f'http://moderngov.southwark.gov.uk/documents/s88407/')
      #url = (f'http://moderngov.southwark.gov.uk/documents/s8{urlsuffix}/')
      #url = (f'https://committees.westminster.gov.uk/documents/s{urlsuffix}/')
      #url = (f'http://democracy.cityoflondon.gov.uk/documents/s131659/')
      #url = (f'http://moderngov.redbridge.gov.uk/documents/s{urlsuffix}/')
      #url = (f'http://democracy.towerhamlets.gov.uk/documents/s166125/')
      #url = (f'https://moderngov.sutton.gov.uk/documents/s63277/')
      https://democracy.islington.gov.uk/documents/s21033/
      https://modgov.hillingdon.gov.uk/documents/s47790/
      urlsuffix += 1
      r = requests.get(url)

      print(url)

      if r.headers['content-type'] != "application/pdf": blankcount += 1

      else:
        blankcount = 0
        with open('/tmp/metadata.pdf', 'wb') as f:
                f.write(r.content)
        print("pdf found")
        # Open the pdf file
        object = PyPDF2.PdfFileReader("/tmp/metadata.pdf", strict=False)

        # get number of pages
        NumPages = object.getNumPages()
        print(NumPages)
        
        f = open('filename.md', 'w')
        # extract text and do the search
        for i in range(0, NumPages):
            PageObj = object.getPage(i)
            print("this is page " + str(i)) 
            Text = PageObj.extractText() 
            # print(Text)
            EstateSearch = re.search(('estate'), Text, re.IGNORECASE)
            SecondarySearch = re.search(('redevelopment|renewal|demolition|regeneration'), Text, re.IGNORECASE)
            if EstateSearch and SecondarySearch:
                print("yes word combination found")
                f.write(url)
        f.close()
