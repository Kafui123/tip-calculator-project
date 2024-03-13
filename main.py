
l = int(input("What was the total bill? $: "))

j = int(input("How many people are splitting the bill?: "))

k = int(input("How much tip would you like to give? 10, 12, or 15?: "))
w = int(((100 + k )/ 100) * l)
r = (round(w / j, 2))

print(f"Each person should pay:  {r}")