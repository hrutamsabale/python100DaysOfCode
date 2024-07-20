def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return round(a/b,2)
operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div
}

to_continue=True
while to_continue:
  x=float(input("\nEnter first number: "))
  for operation in operations:
    print(operation)
  ean=False#ean=Enter Another Number
  while not ean:    
    operation=input("What operation do you wish to perform? ")
    y=float(input("Enter second number: "))
    result=0
    operation_function=operations[operation]
    result=operation_function(x,y)
    print(f"\n{x}{operation}{y} is {result}")
    x=result
    choice1=input(f"Do you wish to continue calculations with {result}? ").lower()
    if choice1=="no":
      ean=True
      choice2=input(f"Do you wish to exit the program? ").lower()
      if choice2=="yes":
        print("\nTHANK YOU")
        to_continue=False
      else:
        print("""---------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------""")
    



                  
