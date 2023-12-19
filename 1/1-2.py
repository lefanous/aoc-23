with open('_1_input.txt', 'r') as file:
    input = file.read().strip()

lines = input.split("\n")

spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def replace(line):
    substrings = [line[i:j+1] for i in range(len(line)) for j in range(i,len(line))]
    substrings = [s for s in substrings if s in spelled_numbers]
    if len(substrings) != 0:
        line = line.replace(substrings[-1],f'{spelled_numbers.index(substrings[-1]) + 1}')
        line = line.replace(substrings[0],f'{spelled_numbers.index(substrings[0]) + 1}')
    return line

lines = [replace(line) for line in lines]

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