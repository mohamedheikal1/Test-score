Test1 =eval(input("Enter your score in test 1:"))#Gets score test 1 from user
Test2 =eval(input("Enter your score in test 2:"))#Gets score test 2 from user
Test3 =eval(input("Enter your score in test 3:"))#Gets score test 3 from user

sum = Test1 + Test2 + Test3 #Calc. sum of total grades for student in tests for calculating average
average_score = sum / 3 # calc. average score of all tests

if average_score >= 90 :#to checks average score for all tests more than or equal 90
    grade = "A" #if average score is more than or equal his grade will be A

elif average_score >=80 :#to checks average score for all tests more than or equal 80
    grade = "B" #if average score is more than or equal his grade will be B

elif average_score >=70 :#to checks average score for all tests more than or equal 70
    grade = "C" #if average score is more than or equal his grade will be C

elif average_score >=60 :#to checks average score for all tests more than or equal 60
    grade = "D" #if average score is more than or equal his grade will be D
    
else:#to checks average score for all tests less than 60
    grade = "F" #if average score is more than or equal his grade will be F

print("The Grade Is :", grade)#output the grade