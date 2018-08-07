n=12
rest = balance
prest = 10

while rest >= 0:
  rest = rest - prest
  for i in range(n-2):
    rest = (rest - prest + rest*annualInterestRate/n)
  if rest > prest:
    prest += 10
    rest = balance
print('Lowest Payment: ',prest)
