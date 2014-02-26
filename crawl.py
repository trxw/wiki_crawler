#!/usr/bin/python
#Note: In order to use urllib2 python 2.6+ is required.
import urllib2
from collections import Counter

#Set the parent link where crawling begins:
url = "http://en.wikipedia.org/wiki/Mathematics"
url = "http://en.wikipedia.org/wiki/Physics"
# Undesirable links:
undesirableLinks = [
	url[url.find('.org/') + 5:], '/w/index.php?title=Event_(',  # These two are to exclude possible direct 
	################################ self-referral since it creates an infinite
	################################ loop while crawling the links referred in the html data.
	'//creativecommons.org/licenses/by-sa/3.0/', 
	'//wikimediafoundation.org/wiki/Privacy_policy',
	'/wiki/Main_Page',
	'//en.wikipedia.org/wiki/Wikipedia:Contact_us',
	'/wiki/Wikipedia:About',
	'/wiki/Help:Contents',
	'/wiki/Help:Introduction_to_referencing',
	'//shop.wikimedia.org',
    '/wiki/Special:RecentChangesLinked',
    '/wiki/Special:BookSources/',  ## Note that this is the book source ISBNs and can be useful in 
    ################################ a graphical representation of wikipedia
    '/wiki/Wikipedia:Community_portal',
    '/wiki/Wikipedia:Community_portal',
    '/wiki/Category:All_articles_needing_additional_references',
    '//meta.wikimedia.org',
    '/wiki/Category:All_articles_lacking_sources',
    '//be-x-old.wikipedia.org/wiki/',
    '//wikimediafoundation.org/wiki/Terms_of_Use',
    'https://www.mediawiki.org/wiki/Special:MyLanguage/How_to_contribute',
    '/wiki/Portal:Featured_content',
    '/wiki/Portal:Current_events',
    '/wiki/Help:Category',
    '/wiki/File:Question_book-new.svg',
    '/wiki/Wikipedia:File_Upload_Wizard',
	'/w/index.php?title=Special:RecentChanges&amp;feed=atom',
	'#p-search',
	'#See_also',
	'/wiki/Special:Random',
	'/wiki/Wikipedia:Citing_sources',
	'/wiki/Special:RecentChanges',
	'//bits.wikimedia.org/apple-touch/wikipedia.png',
	'/wiki/Help:Introduction_to_referencing/1',
	'/wiki/Category:Articles_lacking_sources_from_July_2007',
	'//en.wikipedia.org/w/api.php?action=rsd',
	'//www.mediawiki.org/',
	'0_Unported_License',
	'//en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-ShareAlike_3',
	'https://donate.wikimedia.org/wiki/Special:FundraiserRedirector?utm_source=donate&amp;utm_medium=sidebar&amp;utm_campaign=C13_en.wikipedia.org&amp;uselang=en',
	'http://en.wikipedia.org/wiki/Template_talk:',
	'/wiki/Template_talk:',
	'//en.wikipedia.org/w/index.php?title=Template:',
	'http://www.wikidata.org/wiki/', ## Note that a link that begins with this refers to 
	################################### the corresponding page in which the equivalent of 
	################################### the title of the current page in other languages are listed.
	'//www.wikidata.org/wiki/',
	'/wiki/Special:SpecialPages',
	'/wiki/Talk:',
	'php?debug=false&amp;',
	'//bits.wikimedia.org/en.wikipedia.org/load',
	'/wiki/Portal:Contents',
	'Wikipedia:Verifiability',
	'&amp;oldid=',
	'be-x-old',
	'/w/opensearch_desc.php',
	'//bits.wikimedia.org/favicon/wikipedia.ico',
	'//bits.wikimedia.org',
	'Special:Cite',
	'/w/index.php?title=Special:Book&',
	'/wiki/Special:WhatLinksHere',
	'/w/index.php?title=Special:UserLogin',
	#'/wiki/BBC_Radio', ## wtf? Why using this public tool to advertise your company?
	'/wiki/Oxford_University_Press',  
	':Citation_needed',
	'/wiki/Wikipedia:',
	'/wiki/Especial:',
	'/wiki/Especial%',
	'/wiki/Spezial:',
	'/wiki/Spezial%',
	'/wiki/Special:',
	'/wiki/Special%',
	'/wiki/Wikipedia_Diskussion:',
	'/wiki/Spesial:',
	'/wiki/Spesial%',
	'/wiki/Specjalna:',
	'/wiki/Specjalna%',
	'/wiki/Speciaal:',
	'/wiki/Speciaal%',
	'/wiki/Speciel:',
	'/wiki/Speciel%',
	
	]

badExtentions = ['.jpg', 
	'.png',
	'.pdf',
	'edit', 
	'printable=yes',
	'#sitelinks-wikipedia', ## Note that a link that ends with this refers to 
	################################### the corresponding page in which the equivalent of 
	################################### the title of the current page in other languages are listed.
	'#mw-navigation',
	'Wikipedia:General_disclaimer',
	'&amp;action=info',
	'skin=vector&amp;*',
	'&amp;writer=rl',
	'#External_links',
	'#p-search',
	'#A_note_on_notation',
	'#External_links',
	'#Notes',
	'#See_also',
	'/wiki/Inverse_image',
	'/w/index.',
	'wikipedia.',
	'.svg',
	'wikipedia.',
	'wikipedia',
	'/ka.wikipedia.',
	'pedia.',
	'wikimediafoundation.org/',
	'wikimediafoundation.org',
	"/wiki/Springer_Science%2BBusiness_Media",	
'''	"mwl",  Not required if isGoodInternalLink returns False for len(currentLink) <= 3 
	"dsb",
	"vec",
	"csb",
	"zea",
'''
	"bat-smg",
	'/wiki/International_Standard_Book_Number',
	"Education.aspx",
	'/w/',
	'/trap/',

	]

bookSiteList = ["books.google.com/",
"www.amazon.",

]

## getHTML gets a URL as argument and returns a string containing the HTML code:
def getHTML(url):
	result = urllib2.urlopen(url)
	return result.read()

## extracLink gets the links 	
def extractLink(data, start_link, end_link):
	return data[start_link : end_link + 1]

# getLinks gets htmlData file as an argument and returns a dictionary (or a list if adjusted) 
# containing the links. The keys in dictionary are the links and the values are the number of
# times the link appeared in the html file.  

def getStart_link(data, end_link):

	temp = data.find('"', data.find('href', end_link)) + 1
	if temp > 0:
		return temp
	else:
		return -1

def getEnd_link(data, start_link):

	temp = data.find('"', start_link) - 1
	if temp > 0:
		return temp
	else:
		return -1

## Sort and store dic based on key, that is based on the number of referrals to 
## each link stored in dic:
def storeLink(dictionary, link):
	
	if link not in dictionary:
		dictionary[link] = 1
	else:
		dictionary[link] += 1

## This must be reconsidered if memory is limited:
def sortDic(dic):
	return Counter(dic).most_common()
		
def isGoodLink(link, url):
	
	## Length less than or equal to 2 links are '#' and references to the end like "ga":
	if len(link) <= 3:  ## Note that length >2 was ensured in advance outside this function.
		return False 

	for i in badExtentions: 
		if link.find(i, len(link) - len(str(i))) != -1: 
			return False
	if link[:6].find("/") == -1:
		return False 

	for j in undesirableLinks:
		if link.find(j) != -1:
			return False

	return True 

def isGoodCiteNumber(currentLink):
	if len(currentLink) > 4:
		return currentLink[0:4].find('#cit') != -1
	else:
		return False

def isGoodInternalLink(currentLink):
	
	if len(currentLink) < 2:
		return False

	for i in badExtentions:
		if currentLink.find(i) != -1:
			return False
	
	return True

def isNotEnglish(currentLink):
	temp1 = currentLink.find('//')
	temp2 = currentLink.find('.wikipedia.org')
	if temp2 != -1:
		return currentLink[0:7].find('en') == -1 and currentLink[0:7].find('en.m') == -1 
	return False	

def isBookLink(currentLink):
	
	for item in bookSiteList:
		index = currentLink.find(item)
		# Check if there is anything after books.google.com/. That means it is most likely a book and not an explanation about google books service.
		if index != -1 and len(currentLink) > index + len(item) + 10:
			return True

	return False


## Note that isGoodLink() must be checked BEFORE passing currentLink to isWikipediaLink(),
## because there are numerous links forbidden to crawl on wikipedia that start with '/wiki/'.
def isWikipediaLink(currentLink):
	if currentLink[:6] == "/wiki/":
		return True
	return False


## isWikipediaPerson() checks if the argument refers to a page with persondata-label css file, which means it is a person page.
## The argument to isWikipediaPerson() must have been checked to return True with isWikipediaLink(), that
## is it must be a wikipedia link, which starts with /wiki/.
def isWikipediaPerson(currentLink):
	if isWikipediaLink(currentLink) and getHTML("http://en.wikipedia.org" + currentLink).find("persondata-label") != -1:
		return True
	return False


def getLinks(data, url):
	end_link = 0
	li=[]
	dicInternalLinks = {}
	dicExternalLinks = {}
	dicCiteNumbers = {}
	dicExternalLinksNonEN = {}
	dicBookLinks = {}
	dicWikipediaLinks = {}
	dicWikipediaPersonLinks = {}
	linkCount = 0
	start_link = 0
	
	while start_link != -1:
		
		# Note that getStart_link() and getEnd_link will both return -1 if there are no more hrefs:
		start_link = getStart_link(data, end_link) 
		end_link = getEnd_link(data, start_link)
	
		if start_link != -1:
			linkCount += 1
			## Extract the link as string:   	
			currentLink = extractLink(data, start_link, end_link)
			
			## and Store the extracted link inside list li:		
			#	li.append(currentLink)

			## and Store the extracted link inside dictionary dic, and add 1 to the number of 
			## occurrence of the link:
			if len(currentLink) > 2:
				if currentLink[0:2].find('#') != -1:
					if isGoodCiteNumber(currentLink):
						storeLink(dicCiteNumbers, currentLink)
					elif isGoodInternalLink(currentLink):
						storeLink(dicInternalLinks, currentLink)

				elif isGoodLink(currentLink, url):	
					if isWikipediaLink(currentLink):		
						storeLink(dicWikipediaLinks, currentLink)
						##if isWikipediaPerson(currentLink):
						##	storeLink(dicWikipediaPersonLinks, currentLink)

						
					elif isNotEnglish(currentLink):
						storeLink(dicExternalLinksNonEN, currentLink)
		
					elif isBookLink(currentLink):
						storeLink(dicBookLinks, currentLink)
		
					else:							
						storeLink(dicExternalLinks, currentLink)

	return [dicInternalLinks, dicExternalLinks, dicExternalLinksNonEN, dicCiteNumbers, dicBookLinks, dicWikipediaLinks, dicWikipediaPersonLinks]	

htmlData = getHTML(url)
dicsList = getLinks(htmlData, url)


print "There are "+str(len(dicsList[1])) + " unique external links on the page."


t = sortDic(dicsList[1])
f = open("linkList.txt", "w")

wikipediaLinksSorted = sortDic(dicsList[5])
numberOfWikipediaLinks = len(wikipediaLinksSorted)
f.write("There are " + str(numberOfWikipediaLinks) + " links in dicWikipediaLinks: \n")	

for i in range(len(wikipediaLinksSorted)):
	f.write(str(wikipediaLinksSorted[i][0]) + " : " + str(wikipediaLinksSorted[i][1]) + "\n")	

#for k in dicsList[5]:
#	f.write(str(k) + " : " + str(dicsList[5][k]) + "\n")	

'''
f.write("\n\n\n\n\n\n")
f.write("dicWikipediaPersonLinks are: \n")	
for j in dicsList[6]:
	f.write(str(j) + " : " + str(dicsList[6][j]) + "\n")	
'''


f.write("\n\n\n\n\n\n")

## Write the dicExternalLinks:
f.write("dicExternalLinks are: \n")	
for i in range(len(t)):
	f.write(str(t[i][0]) + " : " + str(t[i][1]) + "\n")

f.write("\n\n\n\n\n\n")

f.write("dicInternalLinks are: \n")	
for j in dicsList[0]:
	f.write(str(j) + " : " + str(dicsList[0][j]) + "\n")	

f.write("\n\n\n\n\n\n")

f.write("dicExternalLinksNonEN are: \n")	
for k in dicsList[2]:
	f.write(str(k) + " : " + str(dicsList[2][k]) + "\n")	

f.write("\n\n\n\n\n\n")

f.write("dicCiteNumbers are: \n")	
for k in dicsList[3]:
	f.write(str(k) + " : " + str(dicsList[3][k]) + "\n")	

f.write("\n\n\n\n\n\n")

f.write("dicBookLinks are: \n")	
for k in dicsList[4]:
	f.write(str(k) + " : " + str(dicsList[4][k]) + "\n")	

f.close() 
