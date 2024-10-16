name = str(input("Enter your Name: "))
sec = str(input("Enter your Section: "))
prelims = float(input("Enter your Preliminary Grade: "))
midterms = float(input("Enter your Midterm Grade: "))
finals = float(input("Enter your Final Grade: "))

if prelims < 40.0 or prelims > 100.0:
    print("Error: your grade must stay between 40 and 100.")
elif midterms < 40.0 or midterms > 100.0:
    print("Error: your grade must stay between 40 and 100.")
elif finals < 40.0 or midterms > 100.0:
    print("Error: your grade must stay between 40 and 100.")
else:
    final_grade = (prelims * 0.3333) + (midterms * 0.3333) + (finals * 0.3333)
    
    if final_grade>= 99.0 and final_grade<=100.0:
        grades = 1.00
        status = "Excellent"
    elif final_grade>= 96.0 and final_grade<=99.0:
        grades = 1.25
        status = "Outstanding"
    elif final_grade>=93.0 and final_grade<=96.0:
        grades = 1.50 
        status = "Superior"   
    elif final_grade>=90.0 and final_grade<=93.0:
        grades = 1.75
        status = "Very Good"
    elif final_grade>=87.0 and final_grade<=90.0:
        grades = 2.00
        status = "Good"
    elif final_grade>=84.0 and final_grade<=87.0:
        grades = 2.25
        status = "Satisfactory"
    elif final_grade>=81.0 and final_grade<=84.0:
        grades = 2.50
        status = "Fairly Satisfactory"
    elif final_grade>=78.0 and final_grade<=81.0:
        grades = 2.75
        status = "Fair"
    elif final_grade>=75.0 and final_grade<=78.0:
        grades = 3.00
        status = "Passed"
    else:
        grades = 5.00
        status = "Failed"
    
print(f"Final Grade: {final_grade:.2f}")
print(f"Your Grade: {grades:}")
print(f"Status: {status}")
