balance = 320000
annualInterestRate = 0.2
n=12
mrate = (annualInterestRate) / n
rest = balance
paylower = balance / n
payupper = balance * (1 + mrate)**n / n


def fun(balance,paylower,payupper):
    
    prest = (payupper + paylower)/2
    balance = rest
    
    for i in range(n):
        
        balance -= prest
        balance += balance*mrate
            
    if round(balance) > 0:
        
        paylower = prest
        fun(balance,paylower,payupper)
        
    elif round(balance) < 0:
        
        payupper = prest
        fun(balance,paylower,payupper)
    else:
        
        print('Lowest Payment: ',round(prest,2))
    

fun(balance,paylower,payupper)
