n = int(input("enter"))
if n <=0:
    fib_sequence = []
fibonacci_sequence = [0,1]

for i in range(2,n):
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)
if n==1:
    fib_sequence = [0]
print(fibonacci_sequence)