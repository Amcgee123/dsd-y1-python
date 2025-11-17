total_minutes = int(input("Enter the total number of minutes: "))


hours = total_minutes // 60       
minutes = total_minutes % 60      


print(f"{total_minutes} minutes is {hours} hours and {minutes} minutes.")
