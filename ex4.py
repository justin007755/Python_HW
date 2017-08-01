cars = 100 # number of cars
space_in_a_car = 4 # how many people can be driven per car
drivers = 30 # number of drivers
passengers = 90 # number of passengers
cars_not_driven = cars - drivers # number of cars which have no driver assgined
cars_driven = drivers # number of cars which have driver assgined
carpool_capacity = cars_driven * space_in_a_car # total number of people we can transport
average_passengers_per_car = passengers / cars_driven # the actual number of passengers driven per car


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."

# Study Drills

# I used 4.0 for space_in_a_car, but is that necessary? What happens if it's just 4?
# A: It's not necessary because the number of people will be a integer instead of floating.
# A: If it's just 4 then the number of people will be 120 instead of 120.0

# Remember that 4.0 is a floating point number. It's just a number with a decimal point, and
# you need 4.0 instead of just 4 so that it is floating point.
# A: Ok.

# Write comments above each of the variable assignments.
# A: See above

# Make sure you know what = is called (equals) and that it's making names for things.
# A: Yes

# Remember that _ is an underscore character.
# A: Yes

# Try running python from the Terminal as a calculator like you did before and use variable names to
# do your calculations. Popular variable names are also i, x, and j.
# A: Done
