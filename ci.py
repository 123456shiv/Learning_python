p=int(input("Enter the principal amount:"))
r=float(input("Enter the rate of interest:"))
t=float(input("Enter the time:"))
ci=p*((1+r/100)**t)-p
print("The compound interest of", p, "at", r, "% interest rate for", t, "years is", ci)