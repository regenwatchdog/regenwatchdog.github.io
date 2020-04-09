#!/bin/bash

urlnumber=300
counter=0

until [ $counter -gt 4 ]
do

url=http://moderngov.southwark.gov.uk/documents/s88$urlnumber/

wget --no-directories --content-disposition -e robots=off -A.pdf -r $url 

if pdfgrep -i splosh *.pdf 
then
      echo "Contains keywords"
      echo $url >> filename.md
else
      echo "Does not contain keywords"
      echo counter: $counter
        ((counter=counter+1))
fi
((urlnumber++))
done
