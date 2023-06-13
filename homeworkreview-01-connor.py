#Answers from Class
#6/7/2023

#How old is the user options
##One line is shorter, but can be harder to read and harder to debug
birth_year = int(input("What year were you born?"))
##Multiple lines can be easier to read and easier to debug
birth_year = input("What year were you born?")
birth_year = int(birth_year)
age = 2023 - birth_year
print(age)

#Return how many times their heart has beaten in their lifetime
##Put spaces between math symbols
##Can use a constant instead of a number, put constants in all caps
HUMAN_HEARTBEATS_PER_YEAR = 35000000
##My code edited - remove extra parantheses and keep math out of print statements
hb_in_millions = round(age * 35,2)
print("Your heart has beaten", hb_in_millions, "million times in your lifetime.")
##Format large numbers to have commas using an F string
heartbeats = 100000 * 365 * age
print(f"Your heart has beaten about {heartbeats:,} in your lifetime.")
##Keep your math clear and explained
bpm = 80
heartbeats_math = age * 365 * 24 * 60 * bpm
print(f'Your heart has beaten roughly {heartbeats/1000000000:,.2} billion times.')
##Include citation URLs in your comments and the URLs for libraries that you used for code packages, etc.
