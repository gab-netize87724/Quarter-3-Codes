names = ["Me", "Yno", "Kara"]

steps = [
    [4500, 5200, 4800, 5000, 5300],
    [4000, 4100, 3900, 4200, 4600],
    [6000, 5800, 5900, 6100, 6200]
]

totals = []

for i in range(len(steps)):
    total = sum(steps[i])
    totals.append(total)
    print(f"{names[i]} - Total Steps: {total}")

highest = max(totals)
lowest = min(totals)

top_index = totals.index(highest)
top_name = names[top_index]

difference = highest - lowest

print("\nTop Performer:", top_name)
print("Difference between highest and lowest total steps:", difference)
