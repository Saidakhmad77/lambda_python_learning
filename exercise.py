
# 1. Write a function that will find the sum of a series of repeating digits equal in number to n 
	# e.g. 3 + 33 + 333 + 3333 + 33333 ... n times
	# The function should take in two arguments, n and the digit to repeat OR you can write 2 seperate functions


from ast import pattern


repeating_digit_sum = lambda n, digit: sum(int(str(digit) * i) for i in range(1, n + 1))


""" def repeating_digit_sum(n, digit):
    total_sum = 0
    current_number = 0
    
    for i in range(1, n + 1):
        current_number = current_number * 10 + digit
        total_sum += current_number
    return total_sum """
    
n = 5
digit = 3
result = repeating_digit_sum(n, digit)
print(f"The sum of the series for digit {digit} repeted {n} times is: {result}")


# 2. Print out the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

pattern = lambda n: '\n'.join(['*' * i for i in range(1, n + 1)] + ['*' * i for i in range(n - 1, 0, -1)])

n = 5
print(pattern(n))


# 3. Write a SINGLE function that accepts 2 numbers, return the sum, difference, product and quotient of the two numbers at 4 seperate variables.

calculate_operations = lambda a, b: (a + b, a - b, a * b, a / b if  b != 0 else None)

num1 = 10
num2 = 5

sum_result, difference_result, product_result, quotient_result = calculate_operations(num1, num2)

print("Sum:", sum_result)
print("Difference", difference_result)
print("Product", product_result)
print("Quotient", quotient_result)


# 4. Write a function that takes 2 integer arguments and returns a list of every even number between them
	# e.g. arguments = 3 and 17, return [4, 6, 8, 10, 12, 14, 16]
 
even_numbers_between = lambda x, y: list(filter(lambda n: n % 2 == 0, range(x + 1, y)))

result = even_numbers_between(3, 17)
print(result)


# 5. Write a function that iterates through a list and returns the largest number in that list. DON'T USE THE MAX() FUNCTION for practice
 
def find_largest(lst):
    if not lst: 
        return None

    largest = lst[0] 

    for num in lst:
        if num > largest:
            largest = num 

    return largest 

numbers = [3, 7, 2, 9, 4, 5, 12, 1]
largest_number = find_largest(numbers)

print(largest_number)
