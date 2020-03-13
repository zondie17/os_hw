#! /usr/bin/env python

import sys
from optparse import OptionParser
import math

def hfunc(index):
    if index == -1:
        return 'MISS'
    else:
        return 'HIT '

def vfunc(victim):
    if victim == -1:
        return '-'
    else:
        return str(victim)

#
# main program
#
parser = OptionParser(usage='%prog', version='%prog 1.0', description='this is a program about PFF Page-Fault-Frequency')
parser.add_option('-a', '--addresses', default='-1',   		help='a set of comma-separated pages to access; -1 means randomly generate',  		action='store', type='string', dest='addresses')
parser.add_option('-i', '--inital memory', default='-1', 	help='a set of comma-separated inital memory pages; -1 means randomly generate', 	action='store', type='string', dest='initMem')
parser.add_option('-w', '--window', default='0', 			help='size of T time window', 														action='store', type='string', dest='window')
parser.add_option('-N', '--notrace', default=False,    		help='do not print out a detailed trace',                                     		action='store_true', dest='notrace')
parser.add_option('-c', '--compute', default=False,    		help='compute answers for me',                                                		action='store_true', dest='solve')

(options, args) = parser.parse_args()
print 'ARG policy', 'PFF'
print 'ARG addresses', options.addresses
print 'ARG inital memory', options.initMem
print 'ARG window', options.window
print 'ARG notrace', options.notrace
print ''

addresses 		= str(options.addresses)
initMem			= str(options.initMem)
window			= int(options.window)
notrace			= options.notrace

addrList = []
addrList = addresses.split(',')
initMemList = []
initMemList = initMem.split(',')
initMemList = list(map(int, initMemList))
# print 'addrList', addrList
# print 'initMemList', initMemList

if options.solve == False:
	print 'Assuming a replacement policy of PFF, and a window T of size %d,' % window
	print 'figure out whether each of the following page references hit or miss'

	for n in addrList:
		print 'Access: %d  Hit/Miss?  State of Memory?' % int(n)
	print ''
else:
	if notrace == False:
		print 'Solving...\n'

	# init memory structure
	count = 0
	memory = []
	memory = initMemList
	temp_memory = []
	hits = 0
	miss = 0
	lst_time = 0
	cur_time = 0

	# need to generate addresses
	for nStr in addrList:
		# first, lookip
		n = int(nStr)
		cur_time += 1
		try:
			# hits
			idx = memory.index(n)
			if n not in temp_memory:
				temp_memory.append(n)
			hits += 1
		except:
			# miss
			idx = -1
			miss += 1

		victim = -1
		if idx == -1:
			diff_time = cur_time - lst_time
			if diff_time > window:
				memory = temp_memory
				temp_memory = []
			else:
				memory.append(n)
			memory.sort()
			lst_time = cur_time

			if victim != -1:
				assert(victim not in memory)

		if notrace == False:
			print 'Access: %d  %s PFF -> %12s <- Replaced: %s [Hits: %d Misses: %d]' % (n, hfunc(idx), memory, vfunc(victim), hits, miss)

	print ''
	print 'FINALSTATS hits %d   misses %d   hitrate %.2f' % (hits, miss, (100.0*float(hits))/(float(hits)+float(miss)))
	print ''














