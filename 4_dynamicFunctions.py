#*agrs =  allows you to pass multiple non-key arguments
#**kwargs = allows you to pass multiple keyword-arguments
#               *unpacking operator
#               1.positional 2.default 3.keyword 4.ARBITRARY

# #before
# def add(a + b):
#     return a + b

# print(add(1,2,3))

# #arguments will now pack into a tuple and not just a + b
# #after
# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total

# print(add(1,2,3,4,5))


# def display_name (*args):
#     for arg in args:
#         print(arg, end = " ")


# display_name("Dr. ","Spongebob", "Harold", "Squarepants")

#**kwargs**

# def print_address(**kwargs):
#     for value in kwargs.values():
#         print(value)

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")


print_address(street="123 Fake St",
               city="Detriot", 
               state="MI",
                 zip="54321")


# Dynamic Functions Practice #1
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

# Don't call the function, you just need to define it.






# Dynamic Functions Practice #2
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.

# def sum_less(list1):
#     three_digit_list = []
#     for n in list1:
#         if n in range (1, 999):
#             three_digit_list.append(n)
#     else:
#         pass
#     return three_digit_list

# result = sum_less([378,100,200])
# print(result)
    



# Dynamic Functions Practice #3
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.


# def check_3_digets(number):
#     return number in range(100,100)

# result = check_3_digets (68)
# print(result)


# def check_3_digets(list1):
#     for n in list1:
#         if n in range(100,1000):
#             return True
#         else:
#             pass


# result = check_3_digets([693, 903, 600])
# print(result)

# def check_3_digets(list1):
    
#     three_diget_list = []
    
#     for n in list1:
#         if n in range (100,1000):
#             three_diget_list.append(n)
#         else:
#             pass

#     return three_diget_list

# result = check_3_digets([55,99,600])
# print(result)







# coffee_prices = [('cappuccino', 1.5),
#                  ('espresso', 1.2),
#                  ('mocha', 1.9)]

# def most_expensive_coffee(list_of_prices):
#     highest_price = 0
#     my_most_expensive_coffee = ''