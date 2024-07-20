def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return round(a/b,2)
while True:
  x=float(input("\nEnter first number: "))
  ean=False
  while not ean:
    operation=input("""+
-
*
/
What operation do you wish to perform? """)
    y=float(input("Enter second number: "))
    result=0
    if operation=="+":
      result=add(x,y)
    elif operation=="-":
      result=sub(x,y)
    elif operation=="*":
      result=mul(x,y)
    elif operation=="/":
      result=div(x,y)
    print(f"\n{x}{operation}{y} is {result}")
    x=result
    choice=input("\nDo you wish to continue with this answer? ").lower()
    if choice=="no":
      print("-------------------------------------------------------------------------------------------")
      ean=True
    



                  
