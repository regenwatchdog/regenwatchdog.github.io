#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

page = requests.get('http://democracy.brent.gov.uk/ieSearchResults2.aspx?SS=regeneration%20OR%20estate%20OR%20demoliton%20OR%20renewal%20OR%20housing%20OR%20demolition&SD=20%2f03%2f2020&ED=27%2f03%2f2020&DT=3&ADV=1&CA=false&SB=true&CX=31572955&PG=1&')

soup = BeautifulSoup(page.content, 'html.parser')

var = list(soup.p)[1]

if var: print('http://democracy.brent.gov.uk/ieSearchResults2.aspx?SS=regeneration%20OR%20estate%20OR%20demoliton%20OR%20renewal%20OR%20housing%20OR%20demolition&SD=20%2f03%2f2020&ED=27%2f03%2f2020&DT=3&ADV=1&CA=false&SB=true&CX=31572955&PG=1&')
