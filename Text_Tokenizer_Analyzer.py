import re, time, string
from collections import Counter
from itertools import islice, tee
from mpi4py import MPI #import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
#running on Python 3.6.2
#used for getting runtime
start_time = time.time()

##Getting number of each word and unique words from text file
with open('C:\\Users\\chi10\\OneDrive\\Documents\\test.txt', 'r') as f:
    words = [word for line in f for word in line.split()]
    print ("Frequency of words is")

    c = Counter(words)
    unique_count = 0
    for word, count in c.most_common(): #loop through file and count the nunber of each word
        print (word, count)
        if count == 1: #for counting "unique" words
            unique_count = unique_count + 1
    print("")

    ##Prints out top 1000 most frequent words
    print ("Top 1000 most frequent words")
    print ("============================")
    print ("============================")
    for i, count in c.most_common(1000):
        print (i, count)
    ##
        
    print("")
    
    print ("Number of unique words is: ", unique_count) #print number of unique words
    
##  

##getting the frequency of characters from text file
files = open('C:\\Users\\chi10\\OneDrive\\Documents\\test.txt', 'r') #open file
File = open('C:\\Users\\chi10\\OneDrive\\Documents\\test.txt')
data = File.read()
words = str.split(data) #split words into array
characters = 0 #hold number of characters
for i in words:
    characters += len(i)
print ("Number of characters in file: ", characters)
##

#Printing number of total words in file
print ("Total number of words is: ", sum(len(line.split()) for line in open('C:\\Users\\chi10\\OneDrive\\Documents\\test.txt', 'r')))
#Printing number of sentences in file
print ("Total number of sentences is: ", open('C:\\Users\\chi10\\OneDrive\\Documents\\test.txt', 'r').read().count("."))
print ("")

def ngrams(arr, n): #function for get n-grams
    teearr = arr
    while True:
        a, b = tee(teearr)
        x = tuple(islice(a, n))
        if len(x) == n:
            yield x
            next(b)
            teearr = b
        else:
            break

#Filter out the punctuation in text file to get just words
justwords = [w.lower() for w in words if (w.isalnum()) and (w.find("'"))]

##Top 1000 most frequent 2-word bigrams

print ("Top 1000 most frequent 2-word bigrams")
print ("=====================================")
ngramprint = Counter(ngrams(justwords, 2)) #without punctuation
for i, value in ngramprint.most_common(1000):
    print (i, value)
##
print ("")
##Top 1000 most frequent 3-word 3-grams
print ("Top 1000 most frequent 3-word trigrams")
print ("=====================================")
ngramprint = Counter(ngrams(justwords, 3)) #without punctuation
for i, value in ngramprint.most_common(1000):
    print (i, value)
##

print ("")
##Top 1000 most frequent n-word n-grams
print ("Top 1000 most frequent n-word n-grams")
print ("=====================================")
ngramprint = Counter(ngrams(justwords, 4))
for i, value in ngramprint.most_common(1000):
    print (i, value)
##
print ("")

#Printing runtime
print ("Time to run program: ", (time.time() - start_time))
