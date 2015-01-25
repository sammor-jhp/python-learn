#!/bin/sh python
import re
import os

print "For Find UnusedSymbol."

def praseDataSection(line):
	#print line
	match = re.match(r'(.*)\.data\.(\w*?)\'(.*)',line)
	if match:
		aUnusedDataSymbol[match.group(2)] = match.group(3)
		return True
	return False

def praseTextSection(line):
	match = re.match(r'(.*)\.text\.(\w*?)\'(.*)',line)
	if match:
		#print match.group(2)
		aUnusedTextSymbol[match.group(2)] = match.group(3)
		return True
	return False

def praseExecFileDataDefSym(line):
	match = re.match(r'(\S*)\s{1}[d|D]\s{1}(\w*?)\s{1}',line)
	if match:
                #aExecFileDataSymbol.append(match.group(2))
		aExecFileDataSymbol[match.group(2)] = match.group()
		return True
	return False
		#print match.group(2)

def praseExecFileTextDefSym(line):
	match = re.match(r'(\S*)\s{1}[t|T]\s{1}(\w*?)\s{1}',line)
        if match:
                #aExecFileTextSymbol.append(match.group(2))
                #print match.group(2)
		aExecFileTextSymbol[match.group(2)] = match.group()
		return True
	return False

strGccOutPutPath="output.txt"
strExecFileDefSybFilePath="symbol.txt"
aExecFileDataSymbol = {}
aExecFileTextSymbol = {}
aUnusedDataSymbol = {}
aUnusedTextSymbol = {}
aCheckTrueUnusedDataSymbol = {}
aCheckTrueUnusedTextSymbol = {}

#load the symbol to mem
def LoadSymbolFile(strPath):
	SymbolFile = open(strPath, "r")
	while 1:
        	line = SymbolFile.readline()
        	if not line:
                	break
        	#print line
        	result = praseExecFileDataDefSym(line)
		if result == False: #if not match data, find Fun Text Next.
	        	praseExecFileTextDefSym(line)

	#global aExecFileDataSymbol
	#global aExecFileTextSymbol
	#aExecFileDataSymbol = list(set(aExecFileDataSymbol)) #remove double str
	#aExecFileTextSymbol = list(set(aExecFileTextSymbol)) #remove double str
        SymbolFile.close()


def LoadGccUnusedSymbol(strPath):
	UnusedSymbolFile = open(strPath, "r")
        while 1:
                line = UnusedSymbolFile.readline()
                if not line:
                        break
                #print line
                result = praseDataSection(line)
                if result == False: #if not match data, find Fun Text Next.
                        praseTextSection(line)
	#global aUnusedDataSymbol
	#global aUnusedTextSymbol
        #aUnusedDataSymbol = list(set(aUnusedDataSymbol)) #remove double str
        #aUnusedTextSymbol = list(set(aUnusedTextSymbol)) #remove double str
        UnusedSymbolFile.close()

def CheckSymbolAndOutput():
	print "-------------"
	for strSymbol in aUnusedDataSymbol.keys():
		#print strSymbol
		#print aExecFileDataSymbol
		#ulCount =  aExecFileDataSymbol.count(strSymbol)
		#if ulCount == 0:
		#	print strSymbol 
		if aExecFileDataSymbol.has_key(strSymbol) == False:
			print "VarName:\t" + strSymbol + "\t" + aUnusedDataSymbol[strSymbol]

	print "-------------"
	for strSymbol in aUnusedTextSymbol.keys():
		if aExecFileTextSymbol.has_key(strSymbol) == False:
			print "Function:\t" + strSymbol + "\t" + aUnusedTextSymbol[strSymbol]
		#ulCount = aExecFileTextSymbol.count(strSymbol)
		#if ulCount == 0:
		#	print strSymbol

LoadSymbolFile("symbol.txt")
LoadGccUnusedSymbol("output.txt")
CheckSymbolAndOutput()

#print aUnusedDataSymbol
#print aUnusedTextSymbol
#print aExecFileDataSymbol
#print aExecFileTextSymbol
print "End"


