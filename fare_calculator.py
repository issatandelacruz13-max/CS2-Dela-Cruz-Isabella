FARE_RATE = 14

name = input("Enter passenger name: ")
while name.strip() == "":
    print("Name cannot be empty!")
    name = input("Enter passenger name: ")

while True:
    try:
        distance = float(input("Enter distance (km): "))
        if distance > 0:
            break
        print("Distance must be greater than 0!")
    except ValueError:
        print("Please enter a valid number!")

while True:
    try:
        passengers = int(input("Enter number of passengers: "))
        if passengers > 0:
            break
        print("Passengers must be greater than 0!")
    except ValueError:
        print("Please enter a whole number!")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name.strip())
print("Total Fare: PHP", round(total_fare, 2))
