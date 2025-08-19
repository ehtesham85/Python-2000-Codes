# Print Abbrevation of months

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

n = int(input("Enter the month number (1-12): "))

pos=(n-1)*3

monthAbbrev = months[pos:pos+3]

print("The abbreviation of the month is:", monthAbbrev)

