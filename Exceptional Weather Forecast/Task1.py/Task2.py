# Write a function that converts the Fahrenheit temperature to Celsius. 
# Remember that the formula is (Fahrenheit - 32) * 5/9.


def temperature_inputs():
    while True:
        try:
            temperature_input = float(input("What is the temperature in Fahrenheit? "))
            return temperature_input
        except ValueError:
            print('Please enter temperature in numeric form.')  

      
def celicius_conversion(fahrenheit):
    return ((fahrenheit - 32) * (5/9))

temperature_input = temperature_inputs()
provided_temperatures_F = []   
provided_temperatures_F.append(temperature_input)
provided_temperatures_C = []
converted_temperatures = celicius_conversion(temperature_input)
provided_temperatures_C.append(converted_temperatures)

print(f'That converts to {converted_temperatures: .2f}°C')