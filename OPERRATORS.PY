num = 100,
name='jane'
print(10>=11 and num % 6 !=0 or len(name)<=10 )


name=['jane','john','yussuf','nasteha']
print('john' not in name)

greetings='mambo kenya'
if 'kenya' in greetings:
     print('yes')
else:
     print('no')     

age =int(input('what is your age?\n'))
gender =input('what is your gender?\n')
if gender =='male' and age >=21:
    print('you are a male,welcome to our club')
elif gender== 'female' and age >= 21:
    print('you are a female, welcome to our club')
else:
    print('incorrect input')        