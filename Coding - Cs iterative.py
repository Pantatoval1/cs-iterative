def calc():
    print('Calculator menu :')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exit')

    count = 0
    choice = int(input("Enter Choice :"))
    while choice != 5:
        num1 = int(input("Please enter first number:"))
        num2 = int(input("Please enter second number:"))
        if choice == 1 :
            print(num1 + num2)
            count += 1
        elif choice == 2 :
            print(num1 - num2)
            count += 1
        elif choice == 3 :
            print(num1 * num2)
            count += 1
        elif choice == 4 :
            print(num1 / num2)
            count += 1
            if num2 == 0 :
                print('Error : Cannot divide by zero')
        else:
            print('Invalid choice')
        choice = int(input("Enter Choice :"))
    print('\nThank you for using the calculator!')
    print('Total calculations performed: ' + str(count))


def check_password_strength(password):
    length = len(password)
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0
    special_count = 0

    special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    for char in password:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1
        elif char in special_chars:
            special_count += 1


    score = 0

    print("\nPassword Strength Analysis:")

    if length >= 12:
        print(f"✓ Length ({length} chars): +3 points")
        score += 3
    elif length >= 8:
        print(f"✓ Length ({length} chars): +2 points")
        score += 2
    else:
        print(f"✗ Length ({length} chars): +0 points (too short)")

    if uppercase_count > 0:
        print(f"✓ Uppercase letters ({uppercase_count}): +2 points")
        score += 2
    else:
        print("✗ Uppercase letters (0): +0 points")

    if lowercase_count > 0:
        print(f"✓ Lowercase letters ({lowercase_count}): +2 points")
        score += 2
    else:
        print("✗ Lowercase letters (0): +0 points")

    if number_count > 0:
        print(f"✓ Numbers ({number_count}): +2 points")
        score += 2
    else:
        print("✗ Numbers (0): +0 points")

    if special_count > 0:
        print(f"✓ Special characters ({special_count}): +2 points")
        score += 2
    else:
        print("✗ Special characters (0): +0 points")

    print(f"\nTotal Score: {score}/11")

    if score >= 10:
        strength = "VERY STRONG"
    elif score >= 8:
        strength = "STRONG"
    elif score >= 6:
        strength = "MODERATE"
    elif score >= 4:
        strength = "WEAK"
    else:
        strength = "VERY WEAK"

    print(f"Strength: {strength}")

def password():
    password = input("Enter password to check: ")
    check_password_strength(password)


def compound_interest_calculator():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    years = int(input("Enter number of years: "))

    print("\nCompound Interest Calculation:\n")

    current_amount = principal

    for year in range(1, years + 1):
        interest = current_amount * (rate / 100)
        new_amount = current_amount + interest

        print(f"Year {year}: ${current_amount:.2f} + ${interest:.2f} = ${new_amount:.2f}")

        current_amount = new_amount


    total_interest = current_amount - principal

    print(f"\nFinal Amount: ${current_amount:.2f}")
    print(f"Total Interest Earned: ${total_interest:.2f}")

print('1. Calculator')
print('2. Password Strength Checker')
print('3. Compound Interest Calculator')
choice = int(input('\nPlease choose between 1,2,3 (stop = 0):'))
while choice != 0 :
    if choice == 1:
        calc()
    elif choice == 2:
        password()
    elif choice == 3:
        compound_interest_calculator()
    else:
        print('Invalid choice')
    print('1. Calculator')
    print('2. Password Strength Checker')
    print('3. Compound Interest Calculator')
    choice = int(input('Please choose between 1,2,3 (stop = 0):'))
print("\nThank you")