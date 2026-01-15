scores = [
    [85, 90, 88],  
    [78, 82, 80],  
    [92, 95, 94],  
    [70, 75, 72],  
    [88, 86, 90]   
]

for i in range(len(scores)):
    total = sum(scores[i])
    average = total / len(scores[i])
    minimum = min(scores[i])
    maximum = max(scores[i])

    print(
        f"Student {i+1} - Total Score: {total} | "
        f"Average: {average:.1f} | "
        f"Min: {minimum} | "
        f"Max: {maximum}"
    )
