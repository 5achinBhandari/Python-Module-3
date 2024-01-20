
cabin_class = input("Enter the cabin class (LUX, A, B, or C): ")


if cabin_class == "LUX":
    description = "You have an upper-deck cabin with a balcony."
elif cabin_class == "A":
    description = "You have a cabin above the car deck, equipped with a window."
elif cabin_class == "B":
    description = "You have a windowless cabin above the car deck."
elif cabin_class == "C":
    description = "You have a windowless cabin below the car deck."
else:
    description = "Invalid cabin class. Please enter LUX, A, B, or C."

print(description)
