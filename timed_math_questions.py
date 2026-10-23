import random
import time

operations=['+', '-', '*', '/']

def generate():
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    op=random.choice(operations)
    print(f"{num1} {op} {num2}" )
    answer=eval(f"{num1} {op} {num2}")
    return answer

st=input("press enter to start")
print("\n-----------------------\n")

start_time = time.time()
correct=0
wrong=0
for i in range(10):
    answer = generate()
    while True:
        guess=int(input("Your answer: "))
        if guess==answer:
            print("Correct!\n")
            correct += 1
            break
        else:
            print("Incorrect!! \n")
            wrong += 1
            break

end_time = time.time()
total_time = end_time - start_time
print(f"You took {total_time:.2f} seconds to complete the quiz.")
print(f"Correct answers: {correct}")
print(f"Wrong answers: {wrong}")