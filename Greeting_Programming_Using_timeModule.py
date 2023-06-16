import time

hour = int(time.strftime('%H'))

time = time.strftime('%H:%M:%S')
print(time)

if hour >= 6 | hour < 12:
    print("Good Morning!")
elif hour >= 12:
    print("Good Afternoon!")
elif hour >= 18 | hour < 24:
    print("Good Evening!")
