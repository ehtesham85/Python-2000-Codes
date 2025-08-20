# Convert a date in form "mm/dd/yyyy" to "month day, year"

dateStr = input("Enter date (mm/dd/yyyy) : ")
monthSrt, dayStr, yearStr = dateStr.split("/")

months=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

monthStr = months[int(monthSrt)-1]

print("The Converted date is : ", monthStr, dayStr + ",", yearStr)

