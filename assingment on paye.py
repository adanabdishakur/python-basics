
level = [
[10000,0.1],
[20000,0.2],
[10000,0.1],
[None, 0.4]
]

def calculate_tax(level, income):
if income level[0]:
income = income - level[0]
return (income, level[0] * level[1])
else:
taxable_income = income
income = 0
return (income, taxable_income * level[1])


def calculate(level, income):

total_tax = 0.0
for l in level:
income, tax = calculate_tax(l, income)
total_tax += tax
return total_tax

print(calculate(level, 71000))    