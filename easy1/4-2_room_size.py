# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

def room_calculator(length, width):
    print(f"The room's area is:\n"
          f"{(length * width):.2f} square meters\n"
          f"{(length * width * 10.7639):.2f} square feet")

room_length = float(input("What's the room's length in meters? "))
room_width = float(input("What's the room's width in meters? "))

room_calculator(room_length, room_width)