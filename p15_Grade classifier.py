test_score=int(input("Enter your test score :"))

#compare grades
if (90<=test_score<=100):
    grade= 'A'
elif (80<=test_score<=89):    
    grade= 'B'
elif (70<=test_score<=79):    
    grade= 'C'
elif (60<=test_score<=69):    
    grade='D'
else:
    grade='F'       

print(f"Your grade : {grade}")    