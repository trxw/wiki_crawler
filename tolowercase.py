UNDESIRABLE_LINKS = [ 
	'/w/index.php?title=Event_(',  # These two are to exclude possible  
	################################ direct self-referral since it creates
	################################ an infinite loop while crawling the
	################################ links referred in the html data.
	'//creativecommons.org/licenses/by-sa/3.0/', 
	'//wikimediafoundation.org/wiki/Privacy_policy',
	'/wiki/Main_Page',
	'//en.wikipedia.org/wiki/Wikipedia:Contact_us',
	'/wiki/Wikipedia:About',
	'/wiki/Help:',
	'/wiki/Help:',
	'//shop.wikimedia.org',
	'/wiki/Special:RecentChangesLinked',
	'/wiki/Special:BookSources/',  ## Note that this is the book source 
	################################# ISBNs and can be useful in a graphical
    ################################# representation of wikipedia
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
#	'0_Unported_License',
	'//en.wikipedia.org/wiki/Wikipedia:',
	'https://donate.wikimedia.org/wiki/Special:',
	'http://en.wikipedia.org/wiki/Template_talk:',
	'/wiki/Template_talk:',
	'//en.wikipedia.org/w/index.php?title=Template:',
	'http://www.wikidata.org/wiki/', ## Note that a link that begins with 
	################################### this refers to the corresponding
	################################### page in which the equivalent of 
	################################### the title of the current page in 
	################################### other languages are listed.
	'//www.wikidata.org/wiki/',
	'/wiki/Special:SpecialPages',
	'/wiki/Talk:',
#	'php?debug=false&amp;',
	'//bits.wikimedia.org/en.wikipedia.org/load',
	'/wiki/Portal:Contents',
#	'Wikipedia:Verifiability',
#	'&amp;oldid=',
#	'be-x-old',
	'/w/opensearch_desc.php',
	'//bits.wikimedia.org/favicon/wikipedia.ico',
	'//bits.wikimedia.org',
#	'Special:Cite',
	'/w/index.php?title=Special:Book&',
	'/wiki/Special:WhatLinksHere',
	'/w/index.php?title=Special:UserLogin',
	#'/wiki/BBC_Radio', ## wtf? Why using this public tool to advertise your
	# company?
	'/wiki/Oxford_University_Press',  
#	':Citation_needed',
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
	'/wiki/Category:CS1_errors:_dates',
	'/wiki/Category:Hidden_templates_using_styles',
	'/wiki/Category:Wikipedia_indefinitely_semi-protected_pages',
	'/wiki/Category:All_articles_with_unsourced_statements',
	'/wiki/category:articles_with_unsourced_statements',
	'/wiki/book:',
	'/w/index.php?title=',
	'#mw-navigation',
	'/wiki/category:Articles_containing',
	'/wiki/category:Use_dmy_dates_from',
	]

# Note that before checking this list, it must be ensured that the link
# is not a bad link, that is it is not in either UNDESIRABLE_LINKS, FILES
# or in BAD_EXTENTIONS.

BAD_EXTENTIONS = [
	'edit', 
	'printable=yes', 
	'#sitelinks-wikipedia', 
	#Note that a link that ends with this refers to 
	#the corresponding page in which the equivalent of 
	#the title of the current page in other languages are listed.

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
	""" 'mwl',  Not required if isGoodInternalLink returns False 
	for len(current_link.get_link()) <= 3""" 
	"dsb",
	"vec",
	"csb",
	"zea",
	"bat-smg",
	'/wiki/International_Standard_Book_Number',
	"Education.aspx",
	'/w/',
	'/trap/',
	]

f = open("tolower","w")

f.write("UNDESIRABLE_LINKS:\n")
for i in range(len(UNDESIRABLE_LINKS)):
	f.write("\t" + "'" + UNDESIRABLE_LINKS[i].lower()+"'" + "\n")

f.write("\n\n\n\n\n\n\n")
for i in range(len(BAD_EXTENTIONS)):
	f.write("\t" + "'" + BAD_EXTENTIONS[i].lower()+"'" + "\n")

f.close()
