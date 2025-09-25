"""
sample2.py
Author: Jacob Catayoc
Date: 9/11/2025
"""

print("""
Sample code using divmod

You may run this application anytime.
""")
dividend = int(input("Dividend: "))
divisor = input("Divisor: ")
divisor = int(divisor)
print(dividend / divisor)

answer = divmod(dividend, divisor)
print(answer)

print("The quotient is " + str(answer[0]))
print("The remainder is " + str(answer[1]))