with open('_1_input.txt', 'r') as file:
    input = file.read().strip()

lines = input.split("\n")

numbers = []
for line in lines:
    numbers_in_line = []
    
    for char in line:
        if char.isdigit():
            numbers_in_line.append(char)
            
    numbers.append(numbers_in_line)
    
two_digit_numbers = []
for line in numbers:
    first_element = line[0]
    last_element = line[-1]
    
    two_digit_numbers.append(first_element + last_element)
   
    
sum = 0
for number in two_digit_numbers:
    sum += int(number)
    
print(sum)