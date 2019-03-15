# UniProt_API
In this work I use API to retrieve information of a customized list of proteins from the famous protein database UniProt.

I found two different methods:

Method 1: Slower but direct: This method loops through the list of proteins we want to extract the information for and directly outputs the result in the output file.

Method 2: Much faster and resistant to connection losses in the middle of the process: This one retreives from the database the WHOLE subset of proteins belonging to Human specie and rewieved. Then it loops through the resulting output and prints to the new output only  the lines that belong to one of the proteins in our custom list.
