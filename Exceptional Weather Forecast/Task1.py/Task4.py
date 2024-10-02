# Add a finally block that thanks the user for using the weather forecast application, 
# ensuring that this message is displayed regardless of whether an exception was caught or not.

def celicius_conversion(fahrenheit):
                return ((fahrenheit - 32) * (5/9))

def temperature_inputs():
    while True:
        try:
            temperature_input = float(input("What is the temperature in Fahrenheit? "))
        except ValueError:
            print('Please enter temperature in numeric form.')
        else:  
            temperature_C = celicius_conversion(temperature_input)
            return temperature_input, temperature_C
        finally:
              print('Thanks for using the weather forecasting application!')
        

temperature_F, temperature_C = temperature_inputs()

print(f'{temperature_F: .2f}°F converts to {temperature_C: .2f}°C.')