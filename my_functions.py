def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name

name_1 = "Rowan"
time_of_day_1 = "morning"
greeting = greet(name_1, time_of_day_1)
print(greeting)
# => "Good morning, Rowan"

name_2 = "Frank"
time_of_day_2 = "night"
greeting = greet(name_2, time_of_day_2)
print(greeting)
# => "Good night, Frank"