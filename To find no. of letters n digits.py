print(" ")
print('                "Python program that accepts a string and calculate the number of digits and letters" ')
print(" ")

stri = input("Enter String: ")
print(" ")

num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

alph = []

let = []

f = []

for letter in range(97, 123):
    alph.append(chr(letter))

for x in stri:
    for a in alph:
        if x is a:
            let.append(a)

Letter = len(let)
print("No. Of Letters Is " + str(Letter))
print(" ")

for y in stri:
    for z in num:
        if y is z:
            f.append(z)

digits = len(f)
print("No. Of Digits Is: " + str(digits))
print(" ")