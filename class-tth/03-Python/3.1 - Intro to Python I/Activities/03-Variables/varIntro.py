# string datatype
name = "George Washington"
# integer datatype
age = 30
# boolean datatype
employed_status = True

# float datatype
hourly_wage = 7.25
daily_wage = hourly_wage * 8

#George Washington is 30 years old.
print(name + " is " + str(age) + " years old.")

#Is George Washington employed? True"
print("Is " + name + " employed? " + str(employed_status))

# George Washington makes 58.0 dollars per day
# f-strings
print(f"{name} makes {daily_wage} dollars per day.")