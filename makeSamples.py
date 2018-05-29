''' 

author nick
21 May 2018 17:57:31

'''

import numpy as np
import random as rand

def generateSamples(setName, prototypes, n_samples, max_noise):
	letters = ['A','B','C','D','E','F','G','H','I','J']
	fileName = setName + "/lab5_" + setName + ".arff"
	
	# for each letter
	for i in range(len(letters)):
		# for the number of samples to create
		for j in range(n_samples):
			# temp copy of prototype for modifications
			current = list(prototypes[i])
			
			# create noise randomly
			for k in range(max_noise):
				index = rand.randint(0,len(current)-1)
				if current[index] == 0:
					current[index] = 1
				else:
					current[index] = 0
			# write current sample to appropriate file
			writeSample(current, fileName, letters[i])
			

def writeSample(x, fileName, letter):
	file = open(fileName, "a")
	for i in range(len(x)):
		file.write(str(x[i]))
		if (i+1) < len(x):
			file.write(",")
		else:
			file.write(",")
			file.write(letter)
			file.write("\n")
	file.close()

def writeSettings(samples, noise, fileName):
	file = open(fileName, "a")
	file.write("Number of Samples: ")
	file.write(str(samples))
	file.write("\nMax Noise %: ")
	file.write(str(noise * 2))
	file.write("\n")
	file.close()
	
def main():
	rand.seed()
	# n_samples:  2   5   10
	n_samples = [20, 50, 100]
	# noise:     4% 10% 20%
	max_noise = [2,  5, 10]
	sets = ["set1","set2","set3"]
	
	#shuffle the arrays to get a random combination of the 3
	rand.shuffle(n_samples)
	rand.shuffle(max_noise)
	
	# get the prototypes 
	prototypes = np.genfromtxt("prototypes.csv", dtype='intc', delimiter=",")
	
	for i in range(len(sets)):
		generateSamples(sets[i], prototypes, n_samples[i], max_noise[i])
		writeSettings(n_samples[i], max_noise[i], (sets[i] + "/settings_" + sets[i] + ".txt"))
		

main()