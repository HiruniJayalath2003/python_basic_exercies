# Problem 19_password strength checker

password=input("Enter password :")
password_=len(password)
print(password_)

#check the conditions
if(password_<6):
   password1="Weak password"
elif(6<=password_<=10):
   password1="Medium password"
else:
   password1="Strong password"

print(f"Your password has {password_} characters , It is {password1} . ")