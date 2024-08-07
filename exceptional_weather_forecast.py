# Objective: The aim of this assignment is to enhance your understanding 
#            of exception handling by creating a weather forecast 
#            application that gracefully handles unexpected user input 
#            and provides user-friendly error messages.

# Task 1: Start 

# - Begin by asking the user to enter the temperature in Fahrenheit.

''' 
putting the input variable assignment in the below line into the function of task 2

user_temp = input("Please enter the temperature in fahrenheit: ") 

'''

# Task 2: Temperature Conversion 

# - Write a function that converts the Fahrenheit temperature to Celsius. 
#   Remember that the formula is (Fahrenheit - 32) * 5/9.

# - Use a try block to catch any potential errors during the conversion process. 
#   What happens if they type out "thirty" instead of doing 30?

def convert_f_to_c():
    while True:
        # made a bool that later triggers the finally print
        conversion_successful = False
        try:
            f_temp = float(input("Please enter the temperature in fahrenheit: "))
        except ValueError:
            print("Value Error: please enter temperature as number (e.g. '78' NOT 'seventy-eight').")
            continue
        except Exception as e:
            print(f"Unexpected Error: {e}")
            continue
# Task 3: User Experience 
# - Implement an else block that prints the converted temperature in a user-friendly format. 
# Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."
        else:
            celcius = round(((f_temp - 32) * 5/9), 2)
            print(f"Fahrenheit {f_temp}˚ = Celcius {celcius}˚")
            conversion_successful = True
# Task 4: Finally 

# - Add a finally block that thanks the user for using the weather forecast application, 
#   ensuring that this message is displayed regardless of whether an exception was caught or not.  
        finally:
            if conversion_successful:
                print("thanks for using this weather forecast application")
                break   

convert_f_to_c()


