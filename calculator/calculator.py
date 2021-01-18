from addition import Addition

class Calculator:

    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)
    
    @classmethod
    def subtract(cls, num1, num2):
        return abs(Addition.add(num1, -num2))

    @classmethod
    def multiply(cls, num1, num2):
        result = 0
        odd = num2 % 2

        while num2 > 0:
            # Store value in new variable
            new_result = Addition.add(num1, num1)

            # Add to the main result
            result = Addition.add(result, new_result)

            # Go back two numbers
            num2 = Addition.add(num2, -2)

        # If it's odd the times we multiply, remove one time the number
        if odd != 0:
            result = Addition.add(result, -num1)

        return result

    @classmethod
    def divide(cls, num1, num2):
        result = 0

        if num1 == num2:
            return 1

        while num1 > 0:
            # Add one to each time we loop
            result = Addition.add(result, 1)

            # Subtract one time
            num1 = Addition.add(num1,-num2)

        # If result is 1, then it means its 0
        if result == 1:
                return 0

        # If num1 is 0 we need to get the rest
        if num1 < 0:
            result = Addition.add(result, -1)
            num1 = Addition.add(num1, 1)

        return result



x = Calculator.add(2, 2)
y = Calculator.subtract(4, 8)
n = Calculator.multiply(12, 9)
n = Calculator.divide(4, 4)

print(x)
print(y)
print(n)

 
## Another way

# class Calculator:
#     @classmethod
#     def add(cls, num1, num2):
#         return Addition.add(num1, num2)  # make use of add() from Addition module
 
#     @classmethod
#     def subtract(cls, num1, num2):
#         return cls.add(num1, -num2)     # turn subtraction to adding a negative num2
 
#     @classmethod
#     def multiply(cls, num1, num2):
#         res = 0
#         for x in range(0, num2):
#             res = cls.add(res, num1)    # add num1 for num2 times
#         return res
 
#     @classmethod
#     def divide(cls, num1, num2):
#         res = 0
#         while num1 >= num2:
#             num1 = cls.subtract(num1, num2)  # subtract num2 from num1 until its remainder is smaller than num2
#             res = cls.add(res, 1)   # count the times of subtraction as the result
#         return res