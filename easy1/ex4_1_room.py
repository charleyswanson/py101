# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

room_length = float(input('Room length in meters? '))
room_width = float(input('Room width in meters? '))

room_area_meters = room_length * room_width
room_area_feet = room_area_meters * 10.7639

print()
print("The room's area is:\n"
     f"{room_area_meters:.2f} square meters\n"
     f"{room_area_feet:.2f} square feet")