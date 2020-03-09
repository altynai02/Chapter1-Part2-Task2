# 2. N students take K apples and distribute them among each other evenly. The
# remaining (the undivisible) part 
# remains in the basket. How many apples will
# each single student get? How many apples will remain in the basket?
# The program reads the numbers N and K. It should print the two answers for
# the questions above. (Each N student will take K apples, and remains X)




num_student = int(input("Enter the number of students: "))
num_apple = int(input("Enter the number of apples: "))
get_apple = num_apple // num_student
remainder = num_apple % num_student 
print(get_apple, 'students get apple and', remainder, 'apple will remain in the basket')



