import random
import time


OPERATORS = ["+", "-", "*","/"]
MIN_OPERAND = 0
MAX_OPERAND = 20
TOTAL_PROBLEMS = 10
def generate_problem():
    left=random.randint(MIN_OPERAND, MAX_OPERAND)
    right=random.randint(MIN_OPERAND, MAX_OPERAND)
    operator=random.choice(OPERATORS)

    expr= str(left)+operator+str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("--------------------------------")

start_time = time.time()
for i in range (TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    guess = input("Problem # "+str(i+1)+": "+expr + "=")
    if guess!= str(answer):
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

correct= TOTAL_PROBLEMS-wrong
print("--------------------------------")
print("Nice work! You finished in ", total_time, " seconds. You have got ", correct, "answers correct!")
if wrong == 0:
    print ("Nice job! You did all correct!")