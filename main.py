print("Welcome to the Trip Cost Calculator!")
days = int(input("How many days will you stay? "))
hotel_cost = float(input("How much does hotel cost per night? $"))
flight_cost = float(input("How much does flight cost? $"))
rental_car_price = float(input("If you need rental car please enter the price otherwise enter zero. $"))
other_expenses = float(input("Enter other possible expenses $"))
total_expenses = round((days*hotel_cost)+flight_cost+(days*rental_car_price)+other_expenses, 2)
print(f"Total Cost: ${total_expenses}")