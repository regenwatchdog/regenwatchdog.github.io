#!/bin/bash


urlnumber=300
counter=0


until [ $counter -gt 9 ]
do
url=http://moderngov.southwark.gov.uk/documents/s88$urlnumber


if [[ `wget -S --spider $url  2>&1 | grep 'not'` ]]; then
        
	    echo $url
	    echo "no pdf exits"
	    ((counter=counter+1))

    else

            echo "exists"
	    wget --no-directories --content-disposition -e robots=off -A.pdf -r $url
	    if pdfgrep -i council *.pdf 
	    then
	       echo "Contains keywords"
	       echo $url >> filename.md
	    fi
	    counter=0
    fi
    ((urlnumber++))
done
