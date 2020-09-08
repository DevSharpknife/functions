# def greet(name): # MODIFIED
#     return "Hey " + name

# greeting = greet("Rowan") # ADDED
# print(greeting) # ADDED

# # => Hey Rowan

def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name

greeting = greet("Rowan", "morning")
print(greeting)

# => "Good morning, Rowan"