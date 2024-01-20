
zander_length = float(input("Enter the length of the zander in centimeters: "))


size_limit = 42
if zander_length >= size_limit:
    print("You can keep the zander.")
else:

    below = size_limit - zander_length
    print(f"The zander is {below} centimeters below the size limit.")
    print("Please release the zander back into the lake.")
