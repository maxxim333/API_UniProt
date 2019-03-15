import urllib,urllib2

url = "https://www.uniprot.org/uploadlists/"

outputdump = open("outputdump.txt", "w+") #Define output file

def download_url(url):
	downloaded = False
	while not downloaded:
		try:
			response = urllib2.urlopen(request)
			downloaded = True
		except urllib2.HTTPError: pass
	return response

#Read the file containingt the list of genes for which we want to retreive information from database
entries=[line.rstrip('\n') for line in open("trusight_expanded_text.txt")]

for entri in entries: #Keep this line if want to loop the entire file
#for j, entri in enumerate(entries): #Keep this if reading from specific line
	#if j>3253: #Keep this if reading from specific line
		params = {
		"from":"GENENAME",
		"to":"ACC",
		"format":"tab",
		"query": entri,
		}
		
		data = urllib.urlencode(params)
		request = urllib2.Request(url, data)
		contact = "" # Please set a contact email address here to help us debug in case of problems (see https://www.uniprot.org/help/privacy).
		request.add_header("User-Agent", "Python %s" % contact)
		response = download_url(request)
		
		page = response.read(200000)
		outputdump.write(page)
		i=+1
		print("Working on " + entri)

