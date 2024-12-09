def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
dict_cal={"+":add,"-":sub,"*":mul,"/":div}
def cal():
    should_accumulate=True
num1=float(input("what is first numebr"))
while should_accumulate:
    for i in dict_cal:
        print(i)
    op=input("enter op")
    num2=float(input("what is sec numebr"))
    answer=dict_cal[op](num1,num2)
    print(f"{num1} {op}{num2}={answer}")
    choice=input("type y to conytinue with {answer},or type n to start a new calculation")
    if choice=="y":
        num1=answer
    else:
        should_accumulate=False
        print("\n")
        cal()
        

