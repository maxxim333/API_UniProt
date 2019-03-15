import urllib,urllib2
import re

output = open("query_reviewed.txt", "w+") #Define output file. In this file, ALL the information of ALL rewieved genes of UniProt Database will be stored



###############


url = "https://www.uniprot.org/uniprot/?query=reviewed:yes+AND+organism:9606&format=tab"

request = urllib2.Request(url)
response = urllib2.urlopen(request)
page = response.read()

print(page)
output.write(page)
	

inputlines = [line.rstrip('\n') for line in open("query_reviewed.txt", "r")] #This input file is the former output file

trusightlines = [line.rstrip('\n') for line in open("trusight_expanded_text.txt")] #Open the file containing the list of genes for which we want to retreive information from UniProt database



#Define new output file. Here, only the information of the custom genes will be stored
outputfile= open("query_reviewed_filtered_txt","w+")


for protein in trusightlines:
	prot = protein
	for line in inputlines:
		if re.search(r'\b' + prot + r'\b', line): #Using re, I can get exact matches 
		
			print >> outputfile, protein, line
