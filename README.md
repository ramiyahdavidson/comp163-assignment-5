# comp163-assignment-5

> Why you chose each loop type for each challenge?
- I chose the while loop for Challenge 1 because the problem was asking for user input, and I didn't know how many steps it would take to meet the condition. I just knew that certain conditions (the Collatz rules) needed to be met repeatedly until the number reached 1.
- The for loops were used for Challenges 2 and 3 because I knew the exact range of numbers I needed to iterate through. For the Prime Checker, the range was known (from 2 up to n−1). For the Multiplication Table, the rows and columns were a fixed range (1 to 10).
> How your solutions work
- For the first solution, the program asks a person to input an integer. A while loop then shows the steps it takes to get that specific integer down to 1 by applying the Collatz rules (divide by 2 if even, multiply by 3 and add 1 if odd).
- The second challenge determines if the user's number is a prime number, meaning it is only divisible by 1 and itself. To find this out, I use a for loop to check if the user's number is evenly divisible by any number in the range from 2 up to the input number minus one. If the modulus operation (%) equals 0, a factor is found, and the number is declared non-prime.
- The final challenge creates a multiplication table. I used nested for loops—an outer loop to handle the rows and an inner loop to handle the columns—to calculate and print the product for every combination from 1×1 up to 10×10.
> Any AI assistance used
- I used AI to clarify the assignment and walk me step-by-step through the structure of each problem.
- I used AI to help identify errors, explain what I was missing (such as misplaced newlines or break statements), and clarify why the correct placement was necessary.
- I used AI to help with writing lines when I didn't know the exact syntax (like f-string formatting) and asked it to explain and clarify the functionality.
