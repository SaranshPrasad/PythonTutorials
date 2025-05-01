# Strings 

a = "saransh"

# Multiline Strings 

s = """I am saransh prasad bari
 student of ysm
 preparing for software engg..
"""
name = "Saransh"
# slicing 
n = name[:5] +  "a" +name[5:]
print(name[1:4])
# reverse a string using slicing 
name = name[::-1]
# print(name)
# print(n)
# print(s)

# replace
s = s.replace("ysm", "Yogoda Satasanga Mahavidyalaya")
print(s)
# length of string 
length = len(s)
print(length)

# Common methods 
up = name.upper()
lo = name.lower()

demo = "    s    "
demo = demo.strip()

demo = demo * 3

demo = demo + " "+ demo

demo = f"{demo} new demo"

name = "saransh prasad bari"
age = 20
msg = "My name is {0} i am {1} years old".format(name,age)
print("I got {:.2f} cgpa in my first semester".format(98.299345))

spb = name.split()
print(spb)
spb = "-".join(spb)
print(spb)
