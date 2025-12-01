from datetime import datetime

current = datetime.strptime(input("Current time (H:M:S): "), "%H:%M:%S")
future = datetime.strptime(input("Future time (H:M:S): "), "%H:%M:%S")

print(current.hour)    # 12
print(current.minute)  # 34
print(current.second)




print("Time difference:", difference)

print(difference.hour)    # 12
print(difference.minute)  # 34
print(difference.second)