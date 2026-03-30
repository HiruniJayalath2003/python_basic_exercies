name=input("Enter Your Name :")
print("\nEnter Your Marks.")
Mark1=int(input("Science :"))
Mark2=int(input("Maths :"))
Mark3=int(input("English :"))

average= ((Mark1+Mark2+Mark3)/3)
if (75<=average<=100):
    grade= "A" 
    status="Pass"
elif (60<=average<=74):
    grade= "B" 
    status="Pass"
elif (50<=average<=59):
    grade= "C" 
    status="Fail"
elif (30<=average<=49):
    grade= "D" 
    status="Fail" 
else:
    grade="F"
    status="Fail"

print("\n-----STUDENT REPORT CARD-----")
print(f"\nStudent Name : {name}")
print("\nTest Marks")
print(f"Science : {Mark1}")
print(f"Maths : {Mark2}")
print(f"English : {Mark3}")
print(f"\nAverageMarks: {average}")
print(f"\nGrade :{grade}")
print(f"\nPASS/FAIL : {status}")
print("----------------------------------")
