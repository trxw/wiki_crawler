#!/usr/bin/python
# -*- coding: utf_8 
#Note: In order to use urllib2 python 2.6+ is required.
import urllib
import urllib2
from collections import Counter

#######################System Setup:########################
# Installing mongodb for python:
# http://api.mongodb.org/python/current/installation.html
# How to use pymongo in python:  
# http://api.mongodb.org/python/current/tutorial.html

######################Uresolved:############################

#How python will count the number of charactes in a link if 
#they are in URL encoding format? I have to count in a couple of 
#the methods in this crawler.


##################For further development####################:
# How to detect a location page like http://en.wikipedia.org/wiki/Princeton,_New_Jersey
# How to detect publishers and news agencies such as http://en.wikipedia.org/wiki/Scientific_American
# and http://en.wikipedia.org/wiki/BBC
# http://en.wikipedia.org/wiki/Wikipedia:Biographies_of_living_persons
# http://en.wikipedia.org/w/index.php?title=Category:1960_births&from=K
# http://en.wikipedia.org/wiki/Wikipedia:Who_is_a_low_profile_individual
# http://en.wikipedia.org/wiki/Category:Living_people
# All wikipedia categories: http://en.wikipedia.org/wiki/Category:Commons_category_with_page_title_same_as_on_Wikidata
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# requests: an alternative to urllib2 which is used by everyone nowedays according to themselves:
# http://docs.python-requests.org/en/latest/
# For requests also see:
# http://stackoverflow.com/questions/10342694/sending-requests-to-webpages-using-pythons-urllib2
# How to log into a website using python:
# http://stackoverflow.com/questions/189555/how-to-use-python-to-login-to-a-webpage-and-retrieve-cookies-for-later-usage
# How to avoid non html content in http request:
# http://stackoverflow.com/questions/8479736/using-python-urllib-how-to-avoid-non-html-content

# Link emotions for A.I.. Look at the pages under the category emotions. This is what I was
# looking for:
# http://en.wikipedia.org/wiki/Category:Emotions
# Now if we extract the graph of emotions from wikipedia, would we find some fundamental
# emotions that all other emotions are connected to most frequently? 
########################### To study#########################:
#http://docs.python.org/2/library/urllib2.html
#http://www.cs.tut.fi/~jkorpela/http.html
#http://json.org/
# Comparison of different html parsers in python: 
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
# Every website now has RESTful API - related to semantic web:
# http://stackoverflow.com/questions/671118/what-exactly-is-restful-programming
# Git good intro: http://git-scm.com/docs/gittutorial



#Set the parent link where crawling begins:
url = "http://en.wikipedia.org/wiki/Mathematics"
# Undesirable links:
UNDESIRABLE_LINKS = [ 
	'digital_object_identifier',
	'/w/index.php?title=event_(', # These two are to exclude possible  
	################################ direct self-referral since it creates
	################################ an infinite loop while crawling the
	################################ links referred in the html data.
	'pubmed_identifier',
	'//creativecommons.org/licenses/by-sa/3.0/',
	'/wiki/category:wikipedia_articles_needing',
	'/wiki/category:pages_containing_cite_templates',
	'/wiki/category:featured_articles',
	'/wiki/category:wikipedia_semi-protected_pages',
	'//wikimediafoundation.org/wiki/privacy_policy',
	'/wiki/main_page',
	'//en.wikipedia.org/wiki/wikipedia:contact_us',
	'/wiki/wikipedia:about',
	'/wiki/help:',
	'/wiki/help:',
	'//shop.wikimedia.org',
	'/wiki/special:recentchangeslinked',
	'/wiki/special:booksources/',
	'/wiki/wikipedia:community_portal',
	'/wiki/wikipedia:community_portal',
	'/wiki/category:all_articles_needing_additional_references',
	'//meta.wikimedia.org',
	'/wiki/category:all_articles_lacking_sources',
	'//be-x-old.wikipedia.org/wiki/',
	'//wikimediafoundation.org/wiki/terms_of_use',
	'https://www.mediawiki.org/wiki/special:mylanguage/how_to_contribute',
	'/wiki/Scientific_American',
	'/wiki/Portal:',
	'/wiki/Scientific_American',
	'/wiki/portal:featured_content',
	'/wiki/portal:current_events',
	'/wiki/help:category',
	'/wiki/file:question_book-new.svg',
	'/wiki/wikipedia:file_upload_wizard',
	'/w/index.php?title=special:recentchanges&amp;feed=atom',
	'#p-search',
	'#see_also',
	'/wiki/special:random',
	'/wiki/wikipedia:citing_sources',
	'/wiki/special:recentchanges',
	'//bits.wikimedia.org/apple-touch/wikipedia.png',
	'/wiki/help:introduction_to_referencing/1',
	'/wiki/category:articles_lacking_sources_from_july_2007',
	'//en.wikipedia.org/w/api.php?action=rsd',
	'//www.mediawiki.org/',
	'/wiki/category:wikipedia_indefinitely_move-protected_pages',
	'//en.wikipedia.org/wiki/wikipedia:',
	'https://donate.wikimedia.org/wiki/special:',
	'http://en.wikipedia.org/wiki/template_talk:',
	'/wiki/template_talk:',
	'/wiki/category:articles_with_open_directory_project_links',
	'//en.wikipedia.org/w/index.php?title=template:',
	'http://www.wikidata.org/wiki/',## Note that a link that begins with 
	################################### this refers to the corresponding
	################################### page in which the equivalent of 
	################################### the title of the current page in 
	################################### other languages are listed.
	'//www.wikidata.org/wiki/',
	'/wiki/special:specialpages',
	'/wiki/talk:',
	'//bits.wikimedia.org/en.wikipedia.org/load',
	'/wiki/portal:contents',
	'/w/opensearch_desc.php',
	'//bits.wikimedia.org/favicon/wikipedia.ico',
	'//bits.wikimedia.org',
	'/w/index.php?title=special:book&',
	'/wiki/special:whatlinkshere',
	'/w/index.php?title=special:userlogin',
	'/wiki/oxford_university_press',
	'/wiki/wikipedia:',
	'/wiki/especial:',
	'/wiki/especial%',
	'/wiki/spezial:',
	'/wiki/spezial%',
	'/wiki/special:',
	'/wiki/special%',
	'/wiki/wikipedia_diskussion:',
	'/wiki/spesial:',
	'/wiki/spesial%',
	'/wiki/specjalna:',
	'/wiki/specjalna%',
	'/wiki/speciaal:',
	'/wiki/speciaal%',
	'/wiki/speciel:',
	'/wiki/speciel%',
	'/wiki/category:cs1_errors:_dates',
	'/wiki/category:hidden_templates_using_styles',
	'/wiki/category:wikipedia_indefinitely_semi-protected_pages',
	'/wiki/category:all_articles_with_unsourced_statements',
	'/wiki/category:articles_with_unsourced_statements',
	'/wiki/book:',
	'/w/index.php?title=',
	'#mw-navigation',
	'/wiki/category:articles_containing',
	'/wiki/category:use_dmy_dates_from',
	'/wiki/Digital_object_identifier',
	'/wiki/Bibcode',
	'_needing_style_editing', #/wiki/Category:All_articles_needing_style_editing 
	]

# Note that before checking this list, it must be ensured that the link
# is not a bad link, that is it is not in either UNDESIRABLE_LINKS, FILES
# or in BAD_EXTENTIONS.


## IMPORTANT NOTE: This can in fact help a lot in determining important
	##################### subcatagories of each field. For example, /wiki/Category:Mathematics
	##################### has a subcaragory /wiki/Category:Fields_of_Mathematics 
TEMPLATE_OR_CATEGORY = [
	'/wiki/template:',
	'/wiki/category:', 
	'/template:', 
	]

FILES = [
	'/wiki/file:',
	'.jpg',
#	'.JPG', 
	'.png',
#	'.PNG', 
	'.pdf',
#	'.PDF',
	'.svg',
	]	

BAD_EXTENTIONS = [
	'edit',
	'printable=yes',
	'#sitelinks-wikipedia',
	'#mw-navigation',
	'wikipedia:general_disclaimer',
	'&amp;action=info',
	'skin=vector&amp;*',
	'&amp;writer=rl',
	'#external_links',
	'#p-search',
	'#a_note_on_notation',
	'#external_links',
	'#notes',
	'#see_also',
	'/wiki/inverse_image',
	'/w/index.',
	'wikipedia.',
	'wikipedia.',
	'wikipedia',
	'/ka.wikipedia.',
	'pedia.',
	'wikimediafoundation.org/',
	'wikimediafoundation.org',
	'/wiki/springer_science%2bbusiness_media',
	'http://en.wikipedia.org/wiki/OCLC',
	'//en.wikipedia.org/wiki/OCLC',
	#'mwl',  	
	#'vec',
	#'csb'
	#'zea'
	#'bat-smg'
	'/wiki/international_standard_book_number',
	'education.aspx',
	'/w/',
	'/trap/',
	]

BOOK_SITE_LIST = [
	"books.google.com/",
	"www.amazon.",
	]



def extract_link(data, start_link, end_link):
	"""Extract the links from string data starting at start_link and
	 ending at end_link

	 """    
	return data[start_link : end_link + 1]


"""get_links gets html_data file as an argument and returns a dictionary 
 (or a list if adjusted) containing the links. The keys in dictionary are
 the links and the values are the number of
 times the link appeared in the html file.  
"""

def get_start_link(data, end_link):

	temp = data.find('"', data.find('href', end_link)) + 1
	if temp > 0:
		return temp
	else:
		return -1

def get_end_link(data, start_link):

	temp = data.find('"', start_link) - 1
	if temp > 0:
		return temp
	else:
		return -1

def store_link_count(dictionary, link):
	"""Store link in the dictionary in the (k, v) form with 
	k = link.get_actual_link() and v += 1 for each new referral to that link in
	the html file. At the end of html file v will be the total number of referrals 
	to that link in the page.
	
	"""

#	dictionary[link.get_actual_link()] = {}

	if link.get_actual_link() not in dictionary:
#		dictionary[link.get_actual_link()]["Title"] = link.get 
		dictionary[link.get_actual_link()] = 1
	else:
		dictionary[link.get_actual_link()] += 1


def sort_dic(dic):
	"""Return a sorted disctionary based on integer values from largest 
	to smallest.

	This must be reconsidered if memory is limited

	"""
	return Counter(dic).most_common()


class Link(object):  #='NOPARENTLINK'  default parent?
 	"""

	"""
	def __init__(self, link, parent_link='NOPARENTLINK'):
		"""link and parent_link can be either strings or other Link objects. """
		self.link = str(link).lower()
		self.parent_link = str(parent_link).lower()
		# Note that wikipedia links are case-sensitive, so, e. g., 
		# D%27Alembert%27s_principle and D%27alembert%27s_principle
		# are different; the second one actually doesn't exist!
		self.actual_link = link  
		self.actual_parent_link = parent_link
		self.html_data = ""
		self.page_title = ""
		self.page_topic = ""

	def get_link(self):
		return self.link 

	def set_link(self, modified_link):
		self.link = modified_link	
		
	def is_good_link(self):
		"""Return True if string argument link is an acceptable link; return 
		False otherwise.

		"""
		if len(self.get_link()) <= 3 or self.is_parent_link(): 
			return False 

		# If it is not an internal link, that is if it doesn't start with #, and
		# if it doesn't contain '/' in the first 7 characters then it is neither an
		# external link nor an internal link.
		if self.get_link()[:3].find("#") == -1 and self.get_link()[:7].find("/") == -1:
				return False 

		for i in BAD_EXTENTIONS: 
			if self.get_link().find(i, len(self.get_link()) - len(str(i))) != -1: 
				return False

		for k in FILES:
			if self.get_link().find(k) != -1:
				return False

		for j in UNDESIRABLE_LINKS:
			if self.get_link().find(j) != -1:
				return False

		return True 


	def is_wikipedia_template_or_category_link(self):
		"""Return True if the link contains an item in TEMPLATE_OR_CATEGORY,
		and return False otherwise. Note that there are nonuseful template and 
		category links that must have been excluded using is_good_link() method 
		before using this method.  

		"""

		for item in TEMPLATE_OR_CATEGORY:
			if self.get_link().find(item) != -1:
				return True
		
		return False


	def is_parent_link(self):
		"""Return True if link contains parent_link or if parent_link is 'NOPARENTLINK', and False otherwise."""
		if self.get_parent_link() != 'NOPARENTLINK':
			return self.get_link().find(self.get_parent_link()[self.get_parent_link().find('.org/') + 5 : -1]) != -1

		return False

	def get_parent_link(self):
		"""Return the lowercased parent link. 

		"""
		return self.parent_link

	def get_actual_parent_link(self):
		"""Return the actual parent link, as entered as an argument once the Link object
		was created. This is in contrast to get_link() which returns lowercased parent link. 

		"""
		return self.actual_parent_link


	def is_cite_number(self):
		if len(self.get_link()) > 4:
			return self.get_link()[0:4].find('#cit') != -1
		else:
			return False

	def is_anchor_tag(self):
		if self.get_link()[0:2].find('#') != -1:	
			return True
		
		return False


	def is_wikipedia_non_en_link(self):
		"""Check if it is a wikipedia page and is non-English."""
		temp = self.get_link().find('.wikipedia.org')
		if temp != -1:
			return self.get_link()[0:7].find('en') == -1 and self.get_link()[0:7].find('en.m') == -1 
		return False    

	def is_book_link(self):
		
		for item in BOOK_SITE_LIST:
			index = self.get_link().find(item)
			# Check if there is anything after books.google.com/. That means it
			# is most likely a book and not an explanation about google books service.
			if index != -1 and len(self.get_link()) > index + len(item) + 10:
				return True

		return False


	def is_wikipedia_en_link(self):
		"""Return True if the link is a Wikipedia link. 

		Note: is_good_link() must be checked BEFORE passing self.get_link() to 
		is_wikipedia_en_link(), to ensure that it is not a robot.txt forbidden link in 
		wikipedia. There are numerous links forbidden to crawl on wikipedia that 
		start with '/wiki/'. 

		"""

		if self.get_link()[:6] == "/wiki/":
			return True

		return False


	def is_wikipedia_person(self):
		"""Check if the argument refers to a page with persondata-label css file,
		which means it is a person page. The argument to is_wikipedia_person() must
		have been checked to return True with is_wikipedia_en_link(), that is it must 
		be a wikipedia link, which starts with /wiki/.

		"""
		self.complete_http_link()

		if self.get_html().find("persondata-label") != -1:
			return True
		return False

	def get_html(self):
		"""Return a string containing the HTML code the page at completed 
		version of url self.get_actual_link(), that is the completed version
		of the link given as argument for creating the Link object. 

		"""
		self.complete_http_link()
		try:
			result = urllib2.urlopen(self.get_actual_link())
			return result.read()
		except:
			print "There is a problem with this link:\n" + self.get_actual_link()

	def set_html_data(self):
		"""Set instance variable html_data equal to the string of the html content at
		web page self.actual_link"""
		self.html_data = self.get_html() 		
		
	def complete_http_link(self):
		""" Set the actual_link equal to a comleted link with http://. """

		temp = self.get_actual_link()
		if temp.find("/wiki") == 0:
			self.set_actual_link("http://en.wikipedia.org" + temp)
		
		elif self.get_link().find("//") == 0:
			self.set_actual_link("http:" + temp)
	

	def get_actual_link(self):
		return self.actual_link

	def set_actual_link(self, actual_link):
		self.actual_link = actual_link
	

	def get_page_title(self):
		"""Get the title of a the URL pointed at actual_link by parsing the html file and 
		reading what comes between first pair of <title> tags on the page.
		Warning: The method must be used only for a parent (root) link, that is for a link
		which was not extracted from the parsed html file of a parent link. In that case 
		method extract_link_title() must be used.  

		"""
		self.set_html_data()  # Note here that html_data might have been parsed once before. 
							  # Think of a way to avoid second time parsing the same page.

		i1 = self.html_data.find('<title>') 
		if i1 != -1:
			i2 = self.html_data.find('</title>')
			return self.html_data[i1 + 7 : i2]
		
		return 'NoTitle'
	
	def set_page_title(self):
		self.page_title = self.get_page_title()

	def get_wikipedia_page_topic(self):
		"""Remove ' - Wikipedia, the free encyclopedia' from page title if it is in 
		page title, then return the result.
		Warning: The method must be used only for a parent (root) link, that is for a link
		which was not extracted from the parsed html file of a parent link. In that case 
		method extract_link_title() must be used.  

		"""
		self.set_page_title()
		if self.page_title != 'NoTitle':
			temp = self.page_title.find(' - Wikipedia')
			if temp != -1:
				return self.page_title[ 0: temp]
			else:
				return "NoWikipediaTitle"

		return 'NoTitle'
			
	def set_wikipedia_page_topic(self):
		self.page_topic = self.get_wikipedia_page_topic()		


	@staticmethod
	def extract_link_title(data, end_link):
		"""Look for 'title="' keyword after the index of the last character of 
		the link (end_link), and return the string starting from index after '"'
		in 'title="' up to the next '"'.  

		Note 1: This method gives wrong title (possibly title of the next tag) for 
		a given href if the link is not checked to give True with is_good_link()
		method first. 
		Note 2: In contrast with get_page_title() and get_wikipedia_page_topic() methods, 
		wherein the html of the URL is parsed, this method reads the title of a link
		from string data.  
	
		"""
		title_start_index = data.find('title="', end_link) + 7
		if title_start_index != -1 + 7:
			title_last_index = data.find('"',title_start_index) - 1
			return data[title_start_index : title_last_index + 1]


	def __repr__(self):
		return self.get_link()


def get_links(data, given_url):
	url = str(given_url)
	end_link = 0
	#li=[]
	dic_section_anchor_links = {}
	dic_external_links = {}
	dic_cite_numbers = {}
	dic_wikipedia_non_en_links = {}
	dic_book_links = {}
	dic_wikipedia_en_links = {}
	dic_wikipedia_person_links = {}
	dic_wikipedia_template_or_category_links = {}
	link_count = 0
	start_link = 0

	#test_link = Link('/wiki/template:')

	while start_link != -1:
		
		# Note that getStart_link() and getEnd_link will both return -1 
		# if there are no more hrefs:
		start_link = get_start_link(data, end_link) 
		end_link = get_end_link(data, start_link)
	
		if start_link != -1:
			link_count += 1
			## Extract the link as string:      
			if end_link != -1:
				current_link = Link(extract_link(data, start_link, end_link), url)
				current_link_title = Link.extract_link_title(data, end_link)
			## and Store the extracted link inside list li:     
			#   li.append(current_link)

			## and Store the extracted link inside dictionary dic, and add 1 to the number of 
			## occurrence of the link:
			if current_link.is_good_link(): #len(current_link.get_actual_link()) > 2:
				if current_link.is_wikipedia_en_link():     
					if current_link.is_wikipedia_template_or_category_link():
						store_link_count(dic_wikipedia_template_or_category_links, current_link)
   					#
   					#elif current_link.is_wikipedia_person():
					#	store_link_count(dic_wikipedia_person_links, current_link)
					#
					else:
   						store_link_count(dic_wikipedia_en_links, current_link)
					
					#else:	
				elif current_link.is_wikipedia_non_en_link():
					store_link_count(dic_wikipedia_non_en_links, current_link)

				elif current_link.is_anchor_tag():
					if current_link.is_cite_number():
						store_link_count(dic_cite_numbers, current_link)
					else: 
						store_link_count(dic_section_anchor_links, current_link)
  
	
				elif current_link.is_book_link():
					store_link_count(dic_book_links, current_link)
				
				
				else:                           
					store_link_count(dic_external_links, current_link)
	

	return [dic_section_anchor_links, dic_external_links, dic_wikipedia_non_en_links, dic_cite_numbers, dic_book_links, dic_wikipedia_en_links, dic_wikipedia_person_links, dic_wikipedia_template_or_category_links]    

url = Link("http://en.wikipedia.org/wiki/Sadness")

html_data = url.get_html()
dics_list = get_links(html_data, url)

print url.get_wikipedia_page_topic() + "\n"

for i in range(len(dics_list)):
	print "There are " + str(len(dics_list[i])) + " links.\n"


print "There are "+str(len(dics_list[1])) + " unique external links on the page."


t = sort_dic(dics_list[5])

f = open(url.get_actual_link()[url.get_actual_link().find('wiki/')+5 : ]+".txt", "w")

wikipedia_links_sorted = sort_dic(dics_list[5])
number_of_wikipedia_links = len(wikipedia_links_sorted)
f.write("There are " + str(number_of_wikipedia_links) + " links in dic_wikipedia_en_links: \n") 

for i in range(len(wikipedia_links_sorted)):
	f.write(str(wikipedia_links_sorted[i][0]) + " : " + str(wikipedia_links_sorted[i][1]) + "\n")   

#for k in dics_list[5]:
#   f.write(str(k) + " : " + str(dics_list[5][k]) + "\n")    

q = sort_dic(dics_list[6])
f.write("\n\n\n\n\n\n")
f.write("Ranked dic_wikipedia_person_links are: \n")  
for j in range(len(q)):
	f.write(str(q[j][0]) + " : " + str(q[j][1]) + "\n")    



f.write("\n\n\n\n\n\n")

## Write the dic_external_links:
f.write("Ranked dic_wikipedia_en_links are: \n") 
for i in range(len(t)):
	f.write(str(t[i][0]) + " : " + str(t[i][1]) + "\n")

f.write("\n\n\n\n\n\n")

f.write("dic_section_anchor_links are: \n") 
for j in dics_list[0]:
	f.write(str(j) + " : " + str(dics_list[0][j]) + "\n")    

f.write("\n\n\n\n\n\n")

f.write("dic_wikipedia_non_en_links are: \n")    
for k in dics_list[2]:
	f.write(str(k) + " : " + str(dics_list[2][k]) + "\n")    

f.write("\n\n\n\n\n\n")

f.write("dic_cite_numbers are: \n")   
for k in dics_list[3]:
	f.write(str(k) + " : " + str(dics_list[3][k]) + "\n")    

f.write("\n\n\n\n\n\n")

f.write("dic_book_links are: \n") 
for k in dics_list[4]:
	f.write(str(k) + " : " + str(dics_list[4][k]) + "\n")    

f.write("\n\n\n\n\n\n")

f.write("dic_wikipedia_template_or_category_links are: \n") 
for k in dics_list[7]:
	f.write(str(k) + " : " + str(dics_list[7][k]) + "\n")    


f.close() 

print "\n"
print len(dics_list[7])

