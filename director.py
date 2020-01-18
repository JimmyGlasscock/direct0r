#Direct0r
#Written by Jimmy Glasscock - 1/17/20

from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import tensorflow as tf
from tensorflow import keras

dictionary = []

#This function will parse the scripts using regex,
#add them to array, along with 0 or 1 depending on franchise it is from

#takes in two arrays of filepaths
def makeTrainingAndTestingArrays(targetFiles, controlFiles):

	data = []
	labels = []

	#adds the data that should pass the tests to the dataset
	for filepath in targetFiles:
		with open(filepath) as file:
			#change to one block of text that starts with a charecter's name, rather than lines
			for line in file.readlines():
				#splits the line up into an array of words
				line = line.split()
				numericLine = convertLineToNumbers(line)

				data.append(numericLine)
				labels.append(1)

	#adds the data that should fail the tests to the dataset
	for filepath in controlFiles:
		with open(filepath) as file:
			#change to one block of text that starts with a charecter's name, rather than lines
			for line in file.readlines():
				#splits the line up into an array of words
				line = line.split()
				numericLine = convertLineToNumbers(line)

				data.append(numericLine)
				labels.append(0)


def convertLineToNumbers(line):
	for i in range(0, len(line)):
		num = addToDictionary(line[i])
		line[i] = num

	#returns line that is only composed of numbers
	return line

def addToDictionary(word):
	if(word not in dictionary):
		dictionary.append(word)

	#returns index of that word in dictionary
	return dictionary.index(word)

def getTrainingAndTestingData(percentTestingEntries):
	if(percentTestingEntries > 1 or percentTestingEntries < 0):
		print("The Percentage of Testing Entries must be between 0 and 1!")
		exit()

	numTestingEntries = int(percentTestingEntries*len(data))

	#shuffle arrays here
	#
	#

	training_data = data[:numTestingEntries]
	training_labels = labels[:numTestingEntries]

	testing_data = data[numTestingEntries:]
	testing_labels = data[numTestingEntries:]

	return (training_data, training_labels, testing_data, testing_labels)
