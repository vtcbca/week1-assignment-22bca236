#Write a python script to enter any number, if it is integer number, then check its palindrom or not. Print appropriate message if it is not palindrom.
def pel():
    a=int(input("Enter Number :"))
    if isinstance(a,int):
        a=str(a)
        b=a[::-1]
        if a==b:
            print("It is Pelindron")
        else:
            print("It is not pelindron")
    else:
        print("The number is not integer")
pel()
