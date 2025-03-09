def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
        return None
    except TypeError:
        print("Error: Both inputs must be numbers!")
        return None
    else:
        return result
    finally:
        print("Division operation attempted.")

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 'a'))
 