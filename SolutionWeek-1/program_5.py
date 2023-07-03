#Write a python scrit to enter any string and count vowel
def vow():
    a=input("Enter String :")
    b=['a','A','e','E','i','I','o','O','u','U']
    v=0
    for i in a:
        if i in b:
            v+=1
    print(f"Vowels in {a} is {v}")
vow()
