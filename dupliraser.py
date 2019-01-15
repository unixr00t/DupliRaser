#!/usr/bin/python3

import hashlib

resultPath = "specify-path"
inputFilePath = "specify-path"

completedLineHash = set()

result = open(result_path, "w")

for line in open(inputFilePath, "r"):
	
	hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
	
	if hashValue not in completed_lines_hash:
		output_file.write(line)
		completedLinesHash.add(hashValue)

result.close()
