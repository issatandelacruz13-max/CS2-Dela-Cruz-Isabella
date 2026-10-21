# Travel Fare Calculator

## Description
This program calculates the total travel fare based on the passenger's name, travel distance in kilometers, and number of passengers. The fare rate is PHP 14 per kilometer per passenger.

## Version 1 - Original Code Without Input Validation

- Input: Accepts the passenger's name, distance in kilometers, and number of passengers.
- Process: Multiplies the distance by the fare rate and the number of passengers.
- Output: Displays the passenger's name and total fare in Philippine pesos.
- Limitation: Does not validate user input. Invalid numeric input may cause an error, and zero or negative values may be accepted.

## Version 2 - Code With Input Validation

- Input: Accepts the passenger's name, travel distance, and number of passengers.
- Process: Checks that the passenger's name is not empty, the distance is a number greater than zero, and the number of passengers is a positive whole number. Invalid entries produce error messages and prompt the user to try again.
- Output: Displays the passenger's name and the calculated total fare in Philippine pesos.
