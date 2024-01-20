gender = input("Enter biological gender (male/female): ").lower()
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

normal_ranges = {
    "female": (117, 155),
    "male": (134, 167)
}

if gender not in normal_ranges:
    print("Invalid gender entered.")
else:

    min_normal, max_normal = normal_ranges[gender]


    if hemoglobin < min_normal:
        print("Hemoglobin is low.")
    elif min_normal <= hemoglobin <= max_normal:
        print("Hemoglobin is normal.")
    else:
        print("Hemoglobin is high.")
