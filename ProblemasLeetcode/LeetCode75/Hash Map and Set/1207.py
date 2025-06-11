def uniqueOccurrences(arr) -> bool:
    occurrences = {}
    for n in arr:
        if n in occurrences:
            occurrences[n] +=1
        else:
            occurrences[n] = 1
    seen = set()
    for numO in occurrences.values():
        if numO in seen:
            return False
        else:
            seen.add(numO)
    return True

print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences([1,2]))
print(uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))