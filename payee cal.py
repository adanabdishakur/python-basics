salary=int(input('enter your salary'))
NETPAY=0
PAYE=0
if salary<=24000:
   tax=0
elif salary <=40000:
    tax=12500+(salary-40000)*0.15
else:
    tax=12500 +(salary -57000)*0.20
PAYE =tax*0.30 
NETPAY=tax+PAYE
print('incometax=', tax)
print('pay as you earn=', PAYE)
print('net per pay=',NETPAY)