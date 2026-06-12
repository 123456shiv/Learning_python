cp=int(input("Enter the cost price: "))
sp=int(input("Enter the selling price: "))
if sp>cp:
    print("Profit:",sp-cp)
elif cp>sp:
    print("Loss:",cp-sp)
else:
    print("No profit, no loss.")

# percentage profit and loss

if sp>cp:
    profit=sp-cp
    profit_percent=(profit/cp)*100
    print("Profit percentage:",profit_percent,"%")  
elif cp>sp:
    loss=cp-sp
    loss_percent=(loss/cp)*100
    print("Loss percentage:",loss_percent,"%")
else:
    print("No profit, no loss.")
