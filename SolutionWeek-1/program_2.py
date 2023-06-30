#Write a python script to enter any number and print the sum of its digit.
def digit():
    a=int(input("Enter Number :"))
    sum=0
    temp=a
    while(a>0):
        b=a%10
        sum=sum+b
        a=a//10
    print(f"Sum of Digit of Number {temp} is {sum} ")
digit()
