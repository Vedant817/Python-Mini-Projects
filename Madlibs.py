#  String Concatenation-> how to put the strings together
youtuber = input(print("Enter the Name of the Person"))
print(f"Subscribe to {youtuber}")
print("Subscribe to {}".format(youtuber))

# Actual Example:
adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")
madlib = f"Computer Programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}."
print(madlib)
