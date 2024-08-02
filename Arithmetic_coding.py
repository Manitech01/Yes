def get_unique_char(message): # O(n^2)
unique_char = []
for character in message: # O(n)
unique = True
# check if the character has already been added to unique_char list
for e in unique_char: # O(n)
if e == character:
# change unique to False if the character already exist in unique_char list
unique = False
break
if unique:
unique_char.append(character) # O(1) amortized
return unique_char
def get_frequency(message, unique_char): # O(n^2)
# use a dictionary where
# the key is the unique character
# the value is the frequency
frequency = {}
for character in unique_char: # O(n)
char_freq = 0
# count the number of occurrences of the current character
for e in message: # O(n)
if character == e:
# increase char_freq by 1 every time a character in message
# is the same as a character in the unique_char list
char_freq += 1
frequency[character] = char_freq # Average case O(1) or Amortized worst case O(n)
return frequency
def get_occurring_probability(message, frequency): # O(n)
# use a dictionary where
# the key is the unique character
# the value is the probability of occurrence
probability = {}
message_length = len(message)
for key, value in frequency.items(): # O(n)
# probability of occurrence of a unique character = frequency/message_length
probability[key] = value / message_length
return probability
def get_cumulative_sum(lower_bound, upper_bound, probability_ls): # O(n) (where appendtoalist takes O(1) amortized)
cumulative_sum = [lower_bound]
diff_btw_two_bounds = upper_bound - lower_bound
char_lower_bound = lower_bound
for probability in probability_ls: # O(n)
char_upper_bound = char_lower_bound + (diff_btw_two_bounds * probability)
cumulative_sum.append(char_upper_bound) # O(1) amortized
char_lower_bound = char_upper_bound
return cumulative_sum
def associate_key_with_interval(cumulative_sum, unique_char):
interval = {}
i = 0
j = 0
while i < len(cumulative_sum) - 1: # O(n)
key = unique_char[j]
lower_bound = cumulative_sum[i]
upper_bound = cumulative_sum[i + 1]
interval[key] = [lower_bound, upper_bound] # Average case O(1) or Amortized worst caseO(n)
i += 1
j += 1
return interval
# get_tag() takes O(n^2) (if get_cumulative_sum() and associate_key_with_interval() take O(n))
def get_tag(probability, unique_char, message):
# put all values from probability dictionary into a probability list
probability_ls = []
for key, value in probability.items(): # O(n)
probability_ls.append(value) # O(1) amortized
# then use the probability list to calculate cumulative sum of probability_ls
# initially, the lower bound is 0.0 and the upper bound is 1.0
cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls) # O(n) (where appendtoalisttakes O(1) amortized)
print('Cumulative sum for interval [0, 1): ', cumulative_sum)
# associate each key with its interval
interval_dict = associate_key_with_interval(cumulative_sum, unique_char) # O(n) (where adding to a dictionary O(1) averagecase)
# get the tag
tag = 0.0
for character in message: # O(n)
# get the interval of the current character (narrow down the interval)
char_interval = interval_dict.get(character) # Average case O(1) or Amortized worst caseO(n)
char_lower_bound = char_interval[0]
char_upper_bound = char_interval[1]
# calculate the tag: tag = average of lower and upper bound
# the tag is recalculated until the last element in the message is reached
tag = (char_lower_bound + char_upper_bound) / 2.0
# every time the interval is narrowed down:
# - get the new cumulative sum for the new interval
# - each key will have a new lower and upper bound in the new interval
cumulative_sum = get_cumulative_sum(char_lower_bound, char_upper_bound, probability_ls) # O(n) (where append to a list takes O(1)
interval_dict = associate_key_with_interval(cumulative_sum, unique_char) # O(n) (where adding to a dictionary O(1) averagecase)
return tag
def concatenate_char(ls): # O(n)
string = '' for e in ls: # O(n)
string += e
return string
def arithmetic_encoding(message): # O(n^2)
# generate a list that contains unique characters in the message
unique_char = get_unique_char(message) # O(n^2)
print('Unique char in the message: ', unique_char)
# get frequency of occurrences of all unique characters in the message
frequency = get_frequency(message, unique_char) # O(n^2)
print('Frequency of each unique character: ', frequency)
# get probability of occurrence of all unique characters in the message
probability = get_occurring_probability(message, frequency) # O(n)
print('Occurring probability of each unique character: ', probability)
# get the tag: get_tag() takes O(n^2) (if get_cumulative_sum() and associate_key_with_interval()
take O(n))
tag = get_tag(probability, unique_char, message) # O(n^2)
return tag, probability
def arithmetic_decoding(probability, message_length, tag): 
# put all values from probability dictionary into a probability list
# put all keys from probability dictionary into a unique_char list
probability_ls = []
unique_char = []
for key, value in probability.items(): # O(n)
probability_ls.append(value) # O(1) amortized
unique_char.append(key) # O(1) amortized
# then use the probability list to calculate cumulative sum of probability_ls
# initially, the lower bound is 0.0 and the upper bound is 1.0
cumulative_sum = get_cumulative_sum(0.0, 1.0, probability_ls) # O(n) (where appendtoalisttakes O(1) amortized)
# associate each key with its interval
interval_dict = associate_key_with_interval(cumulative_sum, unique_char) # O(n) (where adding to a dictionary O(1) averagecase)
i = 0
message_char_ls = []
current_lower_bound = 0.0
current_upper_bound = 1.0
while i < message_length: # O(n)
for key, value in interval_dict.items(): # O(n)
# get the interval of the current character (key)
lower_bound = value[0]
upper_bound = value[1]
# check if tag is within the interval of the current character (key)
if (tag > lower_bound) and (tag < upper_bound):
# narrow down the interval
current_lower_bound = lower_bound
current_upper_bound = upper_bound
# add the character to message_char_ls if tag is within the interval of thecurrentcharacter (key)
message_char_ls.append(key) # O(1) amortized
break
# every time the interval is narrowed down:
# - get the new cumulative sum for the new interval
# - each key will have a new lower and upper bound in the new interval
cumulative_sum = get_cumulative_sum(current_lower_bound, current_upper_bound, probability_ls) # O(n) (where append to a list takes O(1) amortized)
interval_dict = associate_key_with_interval(cumulative_sum, unique_char) # O(n) (where adding to a dictionary O(1) averagecase)
i += 1
return concatenate_char(message_char_ls)
def run_arithmetic_coding():
message = 'OpenGenus' message_len = len(message)
print('The message is ', message)
print('The length of the message is', message_len)
tag, probability = arithmetic_encoding(message)
print('The tag for ', message, ' is ', tag)
decoded_msg = arithmetic_decoding(probability, message_len, tag)
print('Decode the message using probability (coding model), message length, andthegenerated tag: ', decoded_msg)
if __name__ == '__main__':
run_arithmetic_coding()
Output(A):
The message is OpenGenus
The length of the message is 9
Unique char in the message: ['O', 'p', 'e', 'n', 'G', 'u', 's']
Frequency of each unique character: {'O': 1, 'p': 1, 'e': 2, 'n': 2, 'G': 1, 'u': 1, 's': 1}
Occurring probability of each unique character: {'O': 0.1111111111111111, 'p':
0.1111111111111111, 'e': 0.2222222222222222, 'n': 0.2222222222222222, 'G':
0.1111111111111111, 'u': 0.1111111111111111, 's': 0.1111111111111111}
Cumulative sum for interval [0, 1): [0.0, 0.1111111111111111, 0.2222222222222222, 0.4444444444444444, 0.6666666666666666, 0.7777777777777777, 0.8888888888888888, 1.0]
The tag for OpenGenus is 0.016739628347327812
Decode the message using probability (coding model), message length, and the generatedtag:
OpenGenus
Program(B):
import string
import random
from collections import Counter
import time
# Arithmetic Encoding
def ac_encode(txt):
res = Counter(txt)
# characters
chars = list(res.keys())
# frequency of characters
freq = list(res.values())
probability = []
for i in freq:
probability.append(i / len(txt))
print(chars)
print(probability)
high = 1.0
low = 0.0
for c in txt:
diff = high - low
index = chars.index(c)
for i in range(index):
high = low + diff * probability[i]
low = high
high = low + diff * probability[index]
print(f'char {c} -> Low: {low} Higgh: {high}')
tag = (low+high)/2.0
print('Input: ' + txt)
print(str(low) + '< codeword <' + str(high))
print('codeword = ' + str(tag))
with open('encode.ac', 'w') as fw:
for i in chars:
fw.write(i + ' ')
fw.write('\n')
for i in probability:
fw.write(str(i) + ' ')
fw.write('\n')
fw.write(str(tag))
return chars, probability, tag
# Arithmetic Decoding
def ac_decode(chars, probability, tag):
high = 1.0
low = 0.0
output = '' c = '' while (c != '$'):
diff = high - low
for i in range(len(chars)):
high = low + diff * probability[i]
if low < tag < high:
break
else:
low = high
c = chars[i]
output t += c
return output
def arithmetic_coding(input):
if '$' in input:
input = input[0:input.index('$')]
if input[-1] != '$':
input += '$' print('Input: ' + input)
start = time.time()
(chars, probability, tag) = ac_encode(input)
output = ac_decode(chars, probability, tag)
end = time.time()
print('Decode: ' + output)
print('does match : ' + str(input == output))
print(f"Total Time: {end - start} sec\n\n")
return input == output
############# INPUT ######################
# Random String , 100 test case
count = 0
testcase = 10
for i in range(testcase):
# generating string
letters = string.ascii_uppercase
random_txt = ''.join(random.choice(letters) for i in range(13)) + '$'
flag = arithmetic_coding(random_txt)
if flag:
count += 1
print(f"Total Test: {testcase}")
print(f"Succecss: {count}")
#---------------------------------------- # User given specific data
# Please use small string (less than 13 characters)
txt = "BANGLADESH$" arithmetic_coding(txt)
Output(B):
Input: DZJHDDDTCRWLP$
['D', 'Z', 'J', 'H', 'T', 'C', 'R', 'W', 'L', 'P', '$']
[0.2857142857142857, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142, 0.07142857142857142]
char D -> Low: 0.0 High: 0.2857142857142857
char Z -> Low: 0.08163265306122448 High: 0.1020408163265306
char J -> Low: 0.08892128279883381 High: 0.09037900874635567
char H -> Low: 0.0895460224906289 High: 0.08965014577259475
char D -> Low: 0.0895460224906289 High: 0.08957577199976201
char D -> Low: 0.0895460224906289 High: 0.08955452235038122
char D -> Low: 0.0895460224906289 High: 0.0895484510219867
char T -> Low: 0.08954723675630781 High: 0.08954741022283337
char C -> Low: 0.0895473358800367 High: 0.08954734827050281
char R -> Low: 0.08954734384533636 High: 0.08954734473036965
char W -> Low: 0.08954734447750302 High: 0.08954734454071969
char L -> Low: 0.08954734452717322 High: 0.0895473445316887
char P -> Low: 0.08954734453104363 High: 0.08954734453136616
char $ -> Low: 0.08954734453134311 High: 0.08954734453136615
Input: DZJHDDDTCRWLP$
0.08954734453134311< codeword <0.08954734453136615
codeword = 0.08954734453135463
Decode: DZJHDDDTCRWLP$
does match : True
Total Time: 0.005059957504272461 sec
