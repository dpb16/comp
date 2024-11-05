def fractional_knap(Object, profit, weight, capacity):
    # Calculate profit-to-weight ratios
    pw = [p/w for p, w in zip(profit, weight)]
    
    n = len(profit)
    sorted_indx = list(range(n))
    
    # Simple bubble sort to sort indices based on profit-to-weight ratio
    for i in range(n):
        for j in range(0, n-i-1):
            if pw[sorted_indx[j]] < pw[sorted_indx[j+1]]:
                sorted_indx[j], sorted_indx[j+1] = sorted_indx[j+1], sorted_indx[j]

    max_profit = 0
    obj = []
    fractionals = [0] * n

    for i in sorted_indx:
        if capacity >= weight[i]:
            capacity -= weight[i]
            fractionals[i] = 1
            max_profit += profit[i]
            obj.append(Object[i])
        else:
            # If the item can't fully fit, take the fraction that fits
            fractionals[i] = capacity / weight[i]
            max_profit += profit[i] * fractionals[i]
            obj.append(f"{Object[i]} * {fractionals[i]:.2f}")
            break

    print(f"Maximum Profit: {max_profit:.2f}")
    print("Items Taken:", obj)

# Example usage:
Object = ["A", "B", "C", "D", "E", "F", "G"]
profit = [10, 5, 15, 7, 6, 18, 3]
weight = [2, 3, 5, 7, 1, 4, 1]
capacity = 15

fractional_knap(Object, profit, weight, capacity)
