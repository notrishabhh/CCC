a = int(input())
if((a>99)&(a<1000)):
    print((a+((a//10)%10))**(a%10))
