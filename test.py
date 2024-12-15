from main import salary,hello_who

print("Error" if salary(2,10)!=40 else "good")
print("Failed" if hello_who("Max")!="Hello,Max" else "Good")
print("Failed" if hello_who("Leo")!="Hello,Leo" else "Amazing")

print("\nError" if salary(5,52)!=520 else "\nGood")
print("Failed" if hello_who("Vadim")!="Hello,Vadim" else "Good")