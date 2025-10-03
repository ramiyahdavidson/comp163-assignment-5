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
  
     
print(1)
print("Total Steps:", step_count)