# Telephone Case Study
# Celajes, Jyra Mae C. & Luardo Crestalyn
# BSCS 302A

# Cost calculation
def american_region(time_code, day_code, duration_call):
    if time_code == 'A':
        if day_code == 'X':
            return ((duration_call + 2) // 3) * 50.00  # Daytime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 2) // 3) * 40.00  # Daytime, Weekends
    elif time_code == 'B':
        if day_code == 'X':
            return ((duration_call + 2) // 3) * 45.00  # Nighttime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 2) // 3) * 38.00  # Nighttime, Weekends
    return None


def asian_region(time_code, day_code, duration_call):
    if time_code == 'A':
        if day_code == 'X':
            return ((duration_call + 1) // 2) * 30.00  # Daytime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 1) // 2) * 25.00  # Daytime, Weekends
    elif time_code == 'B':
        if day_code == 'X':
            return ((duration_call + 1) // 2) * 27.00  # Nighttime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 1) // 2) * 15.00  # Nighttime, Weekends
    return None


def african_region(time_code, day_code, duration_call):
    if time_code == 'A':
        if day_code == 'X':
            return ((duration_call + 2) // 3) * 40.00  # Daytime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 2) // 3) * 35.00  # Daytime, Weekends
    elif time_code == 'B':
        if day_code == 'X':
            return ((duration_call + 2) // 3) * 36.00  # Nighttime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 2) // 3) * 22.00  # Nighttime, Weekends
    return None


def european_region(time_code, day_code, duration_call):
    if time_code == 'A':
        if day_code == 'X':
            return ((duration_call + 1) // 2) * 35.00  # Daytime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 1) // 2) * 20.00  # Daytime, Weekends
    elif time_code == 'B':
        if day_code == 'X':
            return ((duration_call + 1) // 2) * 30.00  # Nighttime, Weekdays
        elif day_code == 'Y':
            return ((duration_call + 1) // 2) * 19.00  # Nighttime, Weekends
    return None


# Function to calculate cost based on destination, time, day, and duration
def calculate_cost(destination_code, time_code, day_code, duration_call):
    if destination_code == 1:
        total_cost = american_region(time_code, day_code, duration_call)
    elif destination_code == 2:
        total_cost = asian_region(time_code, day_code, duration_call)
    elif destination_code == 3:
        total_cost = african_region(time_code, day_code, duration_call)
    elif destination_code == 4:
        total_cost = european_region(time_code, day_code, duration_call)
    else:
        return None  # Return None if destination code is invalid

    return total_cost


# Function to display menu
def menu():
    print("Call amount is considered flat rate.")
    print("WEEKDAYS")
    print("\t Daytime Calls")
    print("\t\t 1. American Region -- P50 EVERY 3 Minutes ")
    print("\t\t 2. Asian Region --    P30 EVERY 2 Minutes ")
    print("\t\t 3. African Region --  P40 EVERY 3 Minutes ")
    print("\t\t 4. European Region -- P35 EVERY 2 Minutes ")
    print("\t Nighttime Calls")
    print("\t\t 1. American Region -- P45 EVERY 3 Minutes ")
    print("\t\t 2. Asian Region --    P27 EVERY 2 Minutes ")
    print("\t\t 3. African Region --  P36 EVERY 3 Minutes ")
    print("\t\t 4. European Region -- P30 EVERY 2 Minutes ")
    print()
    print("WEEKENDS")
    print("\t Daytime Calls")
    print("\t\t 1. American Region -- P40 EVERY 3 Minutes ")
    print("\t\t 2. Asian Region --    P25 EVERY 2 Minutes ")
    print("\t\t 3. African Region --  P35 EVERY 3 Minutes ")
    print("\t\t 4. European Region -- P20 EVERY 2 Minutes ")
    print("\t Nighttime Calls")
    print("\t\t 1. American Region -- P38 EVERY 3 Minutes ")
    print("\t\t 2. Asian Region --    P15 EVERY 2 Minutes ")
    print("\t\t 3. African Region --  P22 EVERY 3 Minutes ")
    print("\t\t 4. European Region -- P19 EVERY 2 Minutes ")
    print()


# Function to display title and manage continuation
def display_title():
    print("Telephone Cost Calculator")

    print()
    choice = input("Do you want to continue? [Y/N] ").upper()
    if choice != 'Y':
        print("Thank you for using the Telephone Cost Calculator. Goodbye!")
        return


# Main program execution starts here
if __name__ == "__main__":
    display_title()
    menu()

    while True:
        try:
            destination_code = int(input("Enter destination code [1-4]: "))
            if destination_code < 1 or destination_code > 4:
                raise ValueError
            break
        except ValueError:
            print("Please enter an integer between 1 and 4.")

    while True:
        time_code = input("Enter Time Code [A for Day, B for Night]: ").upper()
        if time_code not in ['A', 'B']:
            print("Please enter A or B only.")
        else:
            break

    while True:
        day_code = input("Enter Day Code [X for Weekdays, Y for Weekends]: ").upper()
        if day_code not in ['X', 'Y']:
            print("Please enter X and Y only.")
        else:
            break

    while True:
        try:
            duration_call = int(input("Enter duration call in minutes: "))
            if duration_call <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter duration in minutes only.")

    # Calculate total cost
    total_cost = calculate_cost(destination_code, time_code, day_code, duration_call)

    print()
    # Display call details
    print("Call Details:")
    if destination_code == 1:
        region = "American Region"
    elif destination_code == 2:
        region = "Asian Region"
    elif destination_code == 3:
        region = "African Region"
    elif destination_code == 4:
        region = "European Region"
    else:
        region = "Unknown Region"
    print(f"Region: {region}")
    print(f"Time: {'Daytime' if time_code == 'A' else 'Nighttime'}")
    print(f"Day: {'Weekdays' if day_code == 'X' else 'Weekends'}")
    print(f"Duration of Call: {duration_call} minutes")
    print(f"Total Cost: PHP {total_cost:.2f}")
