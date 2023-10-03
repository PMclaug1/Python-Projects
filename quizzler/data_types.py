# age: int
# name: str
# height: float
# is_human: bool

# can specify data type in or outside function, will display error in IDE if it is not the correct type.
# -> shows that return is typed as a bool
# these are called Type Hints

def police_check(age: int) -> bool:
    if age > 16:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(15):
    print("You may pass.")
else:
    print("Go directly to jail.")
