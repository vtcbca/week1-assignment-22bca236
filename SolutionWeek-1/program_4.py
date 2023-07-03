#4.Write a python script to enter any number, if it is integer number, then check its armstrong or not. Print appropriate message if it is not palindrom.
def armstong(n):
    n=int(n)
    rem=0
    sum=0
    a=n
    while(n!=0):
        r=n%10
        sum=sum+(r**3)
        n//=10
    if(a==sum):
        print("The number is an armstrong number!")
    else:
        print("The number is  not an armstrong number!")


num=input("Enter a number!!:")
if(num.isdigit()):
    armstong(num)
else:
    print("The given input is not valid number!!")
