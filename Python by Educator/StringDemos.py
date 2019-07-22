#Creating a string
pancard_number="AABGT6715H"

#Length of the string
print("Length of the PAN card number:", len(pancard_number))

#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)

print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])
    
print("Iterating the string using keyword in")
for value in pancard_number:
    print(value)

print("Searching for a character in string")
if "Z" in pancard_number:
    print("Character present")
else:
    print("Character is not present")

#Slicing a string
print("The numbers in the PAN card number:", pancard_number[5:9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])

# pancard_number[2]="A" #This line will result in an error, i.e., string is immutable
# print(pancard_number)
str1="abc"
print(str1+"def")
string1="The quick brown fox jumps over the lazy dog."

print("Character at position 5:")
print(string1[4])
print("--------------------------------")

print("Substring.To get the characters from position 2 to position 7 (not included)")
print(string1[2:7])
print("--------------------------------")

print("To remove preceding or trailing white spaces:")
print(string1.strip())
print("--------------------------------")

str1="AbCDe"
print(str1.lower())
str2="AbCDe"
print(str1.upper())
print("--------------------------------")

print("Count of \' o \' : "+str(string1.count("o")))
print("--------------------------------")

print("Splitting a string:")
words=string1.split(" ")
print(words)

print(string1.replace(" ","*"))
print(string1.find("o"))
print(string1.startswith("The"))

