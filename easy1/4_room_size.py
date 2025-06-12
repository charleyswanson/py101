# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

room_length = float(input("What's the room's length in meters? "))
room_width = float(input("What's the room's width in meters? "))

print(f"The room's area in square meters is {room_length * room_width}")
print(f"The room's area in square feet is {room_length * room_width * 10.7639}")