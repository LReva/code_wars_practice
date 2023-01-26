def unique_in_order(sequence):
    if len(sequence) <= 1:
        return list(sequence)
    list_unique_in_order = []
    list_unique_in_order.append(sequence[0])
    for n in range (1, len(sequence)):
        if sequence[n-1] != sequence[n]:
            list_unique_in_order.append(sequence[n])
    return list_unique_in_order

print(unique_in_order([1,3,3,4,6,2,3,3]))