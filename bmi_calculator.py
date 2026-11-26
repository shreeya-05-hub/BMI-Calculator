# BMI Calculator in Python

def calculate_bmi(weight, height):
    # BMI formula: weight (kg) / [height (m)]^2
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("=== Welcome to BMI Calculator ===")
    try:
        weight = float(input("Enter your weight in kg (e.g., 60): "))
        height = float(input("Enter your height in meters (e.g., 1.75): "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers!")
            return
            
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        print(f"\nYour BMI is: {bmi}")
        print(f"Category: {category}")
        
    except ValueError:
        print("Invalid input! Please enter valid numbers for weight and height.")

if __name__ == "__main__":
    main()
