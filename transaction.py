a=int(input('enter the withdrawl amount'))
b=int(input('enter the balance amount'))
if a>b:
    print('insufficient balance')
else:
  if a<b and a%5==0:
      print("transaction is successfull")
  else:
      print("incorrect withdrawl amount(not multiple of 5)")
