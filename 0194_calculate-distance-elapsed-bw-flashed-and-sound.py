# write a program that determines the distance to a lightening strike based on the time elapsed between flash and sound of thunder.The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft

speed_of_sound = 1100
feet_per_mile = 5280

time = float(input("Enter the time elapsed between the flash and the sound of thunder : "))

distance_feet = speed_of_sound * time
distance_mile = distance_feet/feet_per_mile

print(f"Distance to lightening strike is {distance_feet:.2f} feet or {distance_mile:.2f} miles")

