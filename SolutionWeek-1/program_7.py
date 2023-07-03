#write a python script to enter any string,replace vowel with its position number.
#for example : input:Amit
#              output:0m2t

def vow():
    a=input("Enter String :")
    b=''
    c=['a','A','e','E','i','I','o','O','u','U']
    for index,j in enumerate(a):
        if (j in c):
            b+=str(index)
        else:
            b+=j
    print(f"String is {b}")
vow()
