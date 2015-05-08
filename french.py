#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import division
from collections import defaultdict
import random

if __name__ == "__main__":
	print 'Welcome to the French Verb Conjugations Reviewer 1.0!'

	verb = defaultdict()
	subjects = ['je', 'tu', 'il/elle', 'nous', 'vous', 'ils/elles']
	correct = 0
	tries = 0
	rounds = 1

	try:
		f = open('verbs.txt', 'r')
	except IOError:
		print 'ERROR: Sorry, please review your french and write the verbs.txt file'
		exit(1)

	for line in f:
		w = line.strip().split()
		if (len(w) > 1 and w[0][0] != '#'):
			verb[w[0]] = w[1:]

	f.close()

	print "You will be tested on the following verbs today: "
	for v in sorted(verb.keys()):
		print v,

	while(True):
		print
		print '--- Round ' + str(rounds) + '---'
		v = random.randint(0, len(verb.keys())-1)
		s = random.randint(0, len(subjects)-1)
		while(raw_input(verb.keys()[v] + ': ' + subjects[s] + ' ') != verb[verb.keys()[v]][s]):
			tries += 1
			print "Try again"

		correct += 1
		tries += 1
		rounds += 1
		score = correct/tries

		if(raw_input('Score: ' + '{:.0%}'.format(score) + ' Continue? [y/n]: ') == 'n'):
			print '\nYou played ' + str(rounds-1) + ' rounds, and your final score is ' + '{:.0%}'.format(score)
			if (score > 0.9):
				print 'Great Job! :D'
			elif (score > 0.8):
				print "You did alright, I guess."
			elif (score > 0.6):
				print "At least you won't fail."
			else:
				print "You're going to FAIL!!! Keep studying!"
			break