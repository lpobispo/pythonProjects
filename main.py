from operator import index

# print("Hi universe!")
# print("Hello world!")

# Function to generate Fibonacci sequence
# def fibonacci(n):
#     sequence = [0, 1]
#     while len(sequence) < n:
#         next_value = sequence[-1] + sequence[-2]
#         sequence.append(next_value)
#     return sequence[:n]
# 
# # Define the number of terms
# n_terms = int(input("Enter the number of terms: "))
# 
# # Get the Fibonacci sequence
# fib_sequence = fibonacci(n_terms)
# 
# # Print the result
# print("Fibonacci Sequence:", fib_sequence)


#
# AI: Certainly!
# You can create a function that takes in a number and returns its reverse.
# Here’s how you can do it:
#
#
def reverse_number(num):
  # convert num into string data type
  num = str(num)
  # Reverse the number
  reverse = num[::-1]
  # Return the number
  return int(reverse)

## Example usage:
print(reverse_number(1223)) # Output: 3221
print(reverse_number(987654321)) # Output: 123456789


# #
# # AI: Sure!
# # You can create a function that takes in a number and returns its opposite.
# # Here's how you can do it:
# #
#
# def oppositeNumber(num):
#     return -num
#
# # Example usage:
# print(oppositeNumber(54321)) # Output: -5
# print(oppositeNumber(-7)) # Output: 7