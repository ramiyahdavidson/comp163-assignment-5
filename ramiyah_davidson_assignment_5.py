#variables for each 
current_number = int(input("Pick a number 1 - 100"))
step_count = 0
#first loop
while current_number != 1:
    print(current_number, end=" ")
    if current_number % 2 == 0:
        current_number = current_number // 2
    else: 
        current_number = current_number * 3 + 1
    step_count += 1
#prints 1 everytime    
print(1)
print("Total Steps:", step_count)

# Challenge 2
num_to_check = int(input("Enter a number:"))
is_prime = True
#testing if number is a prime number
print(f"Testing divisors from 2 to {num_to_check - 1}")
for divisor in range(2, num_to_check):
    if num_to_check % divisor == 0:
        is_prime = False  # if is not a prime number it is a false
        break
#final output
if is_prime:
    print(f"{num_to_check} is prime")
else:
    print(f"{num_to_check} is not prime (divisible by {divisor})")
