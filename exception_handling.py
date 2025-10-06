import copy

# try:
#     num1 = int(input("Enter the 1 number: "))
#     num2 = int(input("Enter the 2 number: "))
#     result = num1/num2
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# except ValueError:
#     print("Error: Number invalid, please enter a valid input")
# finally:
#     print(result)



# list = [[1,2], [3,4]]
# shallow = copy.copy(list)
# deepcopy = copy.deepcopy(list)
# print(shallow)
# print(deepcopy)



import time

def decorator(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result  = func(*args,**kwargs)
        end = time.time()
        print(f"{start - end} seconds")
        return result
    return wrapper


@decorator
def slow_function():
    # time.sleep(2)
    print("finished !")



slow_function()