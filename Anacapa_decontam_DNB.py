#!/usr/bin/env python3

#March2020
#removing contamination reads from a metabarcode sequencing "taxonomy table". This taxonomy table is the output of the program Anacapa and contains trimmed and filtered sequences assigned to taxon.
#to run:
	# import Anacapa_decontam_DNB.py
	# Anacapa_decontam_DNB.remove_homo("taxonomy_table_infile", "decontam_taxonomy_table_outfile.txt")

#module 1 - remove human reads
print("removing human reads from taxonomy table")

def remove_homo(infile, outfile):	
	output = []
	counter=0
	f = open (infile, "r")
	for line in f.readlines(): #writing all lines that don't contain genus: Homo to new file"
		if not "Homo" in line:
			output.append(line)		
	f.close()
	f2 = open (outfile, "w")
	f2.writelines(output)
	f2.close	
	f = open (infile, "r") 
	for line in f.readlines(): #counting number of homo seqs in file"
		if "Homo" in line:
			counter+=1
	f.close()	
	print("{} updated with {} homo sequences removed". format(outfile, counter))
