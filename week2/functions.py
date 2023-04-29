

def greet():
    print("Hello")
    print("two")
    print("three")

greet()

# Function w/ input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")
    print(f"Isn't the weather nice today?")

greet_with_name("Sean")

# Function w/ two inputs positional arguments
def greet_with_name_loc(name, location):
    print(f"Hello {name}")
    print(f"What time is it in {location}?")

greet_with_name_loc("Chad", "Hawaii")

# Function w/ two inputs keyword args
def greet_with(location="Tuvalu", name="Rick"):
    print(f"Hello {name}")
    print(f"What time is it in {location}?")

greet_with()