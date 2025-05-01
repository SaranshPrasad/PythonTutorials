#Conditional Statements 
a = True
if a:
    print("Ok")

if not a:
    print("Not Ok")
else:
    print("Double Ok")

if a == 0:
    print("3 Ok")
elif a == 1:
    print("4 Ok")
else:
    print("Not Ok")

age = 1
s = "Adult" if age >= 18 else "Minor"
print(s)

# Match Case Statement

match age:
    case 18:
        print("Adult")
    case 1 | 17:
        print("One or 17")