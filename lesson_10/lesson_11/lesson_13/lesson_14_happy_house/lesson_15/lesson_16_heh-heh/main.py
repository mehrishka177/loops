def total_cacl(bill_amount,tip_perc):
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print("Please pay ${total}")
    
    total_cacl(150,20)