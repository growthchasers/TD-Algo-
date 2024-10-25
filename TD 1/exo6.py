# exo 6 
print('----------exo6 started---------')

vat_rate = 0.20
price_ht = float(input("Enter the price HT of the article: "))
quantity = int(input("Enter the number of articles: "))
total_price_ht = price_ht * quantity
total_vat = total_price_ht * vat_rate
total_price_ttc = total_price_ht + total_vat
print(f"The total price TTC is: {total_price_ttc:.2f} €")

print('----------exo6 finished---------')