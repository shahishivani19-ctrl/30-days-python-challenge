n = int(input("Enter number: "))

original = n
sum_of_cubes = 0

while n > 0:
    digit = n % 10
    sum_of_cubes += digit ** 3
    n = n // 10

if original == sum_of_cubes:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
