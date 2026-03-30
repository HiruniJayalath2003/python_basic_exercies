# Problem 18_Simple discount calculator

purchase_amount= float(input("Enter your purchase amount $"))

#calculate discount
discount1= purchase_amount*(20/100)
discount2= purchase_amount*(10/100)
discount3= 0

#check conditions
if (purchase_amount>=100):
   discount=discount1
   discount_="20%"

elif (50<=purchase_amount<=100):
   discount=discount2
   discount_="10%"

else:
   discount=discount3   
   discount_="0"

print(f"\nYour original price is ${purchase_amount}")
print(f"You are getting {discount_} discount and your discount amount is ${discount} ")  
print(f"Your final price is ${purchase_amount-discount}")