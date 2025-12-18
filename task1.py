slices = party_pizza_mini + large + medium + people
print(f"Total number of slices: {slices}")

people = +1
share = slices % people
leftover = (int(input(share)))
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")

people = +2 #Eric and Brandon are coming too.
share = slices % people
leftover = (int(input(share)))
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")

#Mom says "Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”

party_pizza_mini = +1
share = slices % people
leftover = (int(input(share)))
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")


