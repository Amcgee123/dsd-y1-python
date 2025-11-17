
notifications = [34, 28, 55, 40, 60, 22, 18]


print("Notifications each day:")
for i in range(len(notifications)):
    print(f"Day {i+1}: {notifications[i]}")


highest = max(notifications)
print("\nHighest notifications in a day:", highest)


lowest = min(notifications)
print("Lowest notifications in a day:", lowest)


total = sum(notifications)
print("Total notifications:", total)


average = total / len(notifications)
print("Average per day:", round(average, 2))


new_value = int(input("\nEnter a new notification value to add: "))
notifications.append(new_value)

d
print("\nUpdated notifications list:")
print(notifications)


user1 = notifications
user2 = [20, 45, 33, 50, 70, 15, 25]  

print("\nComparison of two users:")
print("User 1:", user1)
print("User 2:", user2)
