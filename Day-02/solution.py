n = int(input())

sum_digits = 0  # sum store krne ke liye

#sum of digits
while(n > 0):
  digit = n % 10   #last digit
  sum_digits = sum_digits + digit
  n = n // 10      #last digit remove

print("sum of digits: ", sum_digits)
