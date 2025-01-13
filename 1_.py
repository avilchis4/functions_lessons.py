# Methods, Help & Documentation Practice #1
# Remove the characters to the left of our main text:
# functions are ways to wrap your code
# into reusuable units


# how you define a function
# only define a function ONCE
# whatever i pass inside the parentheses is called a paramater (place holder for future information)
# def sayHello(name, age, number):
#     print (f"say hello {name}")
#     print ("say hello")
#     print ("Hello Governor")
#     print (f"welcome back {name}")
#     print (f"your age is {age}")
#     print (f"your phone number is {number}")

# # once you define a function, you must call or invoke the function
# # when i pass info into the called function, its called an argument
# sayHello("ariana", 16, "708-347-1958")
# sayHello("tyler", 34, "773-027-9486")
# sayHello("hayden", 19, "708-190-0271")

# def determainEligibility(age):
#     # if your age is over the age of 18, you can vote
#     # otherwise you cannot vote
#     if age >= 18:
#         print ("you can vote")
#     else:
#         print("you can't vote")

# determainEligibility(12)
# determainEligibility(19)
# determainEligibility(15)

# def willYouGraducate(gpa, credits, SAT):
#     # gpa is float variable
#     # credits is number variable
#     # passed SAT is boolen (true or false)
#     if (gpa >= 3.0) and (credits >= 28) and (SAT == True):
#         print ("you passed!")
#     elif (gpa < 3.0) or (credits < 28) or (SAT != True):
#         print ("back to the drawing board")
#     else:
#         print ("talk to your counselor")
    
# willYouGraducate(2.8, 15, True)
# willYouGraducate(3.7, 30, True)
# willYouGraducate(2.8, 15, False)

# return = staement used to end a function and send a result back to caller 

# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# functions wont work unless you call them

# print(add(1,2))
# print(subtract(1,2))
# print(multiply(1,2))
# print(divide(1,2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("spongebob", "squarepants")
print(full_name)

# ,

# :

# %

# _

# #

# Use the lstrip() method. Print the result to the screen:

# ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

# Search the documentation for the requested method to learn how it works. You can use intermediate variables if you need them.


# Methods, Help & Documentation Practice #2
# Add the element "orange" as the fourth element of the following list fruits, using the insert() method:

# fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

# Search the documentation for the requested method to know how it works.

# Methods, Help & Documentation Practice #3
# Check if the sets below are isolated (that is, they have no elements in common), using the isdisjoint() method. Store this result in the isolated_sets variable:

# phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
# tv_brands = {"Sony", "Philips", "Samsung", "LG"}
# Search the documentation for the requested method to know how it works.

