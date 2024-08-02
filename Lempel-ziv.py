#II LZ
input_str = 'AAAABBCDEABCDABCAAABCDEEEEEECBBBBBBDDAAE' keys_dict = {}
ind = 0
inc = 1
while True:
if not (len(input_str) >= ind+inc):
break
sub_str = input_str[ind:ind + inc]
print (sub_str,ind,inc)
if sub_str in keys_dict:
inc += 1
else:
keys_dict[sub_str] = 0
ind += inc
inc = 1
# print 'Adding %s' %sub_str
print (list(keys_dict))

Output:
A 0 1
A 1 1
AA 1 2
A 3 1
AB 3 2
B 5 1
C 6 1
D 7 1
E 8 1
A 9 1
AB 9 2
ABC 9 3
D 12 1
DA 12 2
B 14 1
BC 14 2
A 16 1
AA 16 2
AAA 16 3
B 19 1
BC 19 2
BCD 19 3
E 22 1
EE 22 2
E 24 1
EE 24 2
EEE 24 3
E 27 1
EC 27 2
B 29 1
BB 29 2
B 31 1
BB 31 2
BBB 31 3
B 34 1
BD 34 2
D 36 1
DA 36 2
DAA 36 3
E 39 ['A', 'AA', 'AB', 'B', 'C', 'D', 'E', 'ABC', 'DA', 'BC', 'AAA', 'BCD', 'EE', 'EEE', 'EC', 'BB', 'BBB', 'BD', 'DAA']