#Write a python script to enter any number and check its prime or not.
def prime():
    a=int(input("Enter Number :"))
    ans=0
    for i in range(2,a) :
        if(a%i==0):
           ans+=1
    if(ans==0):
            print("Number is Prime")
    else:
          print("Number is not Prime")
prime()
