def largestAltitude(gain) -> int:
    altitudes = [0]*(len(gain)+1)
    for i in range(len(gain)):
        altitudes[i+1] = altitudes[i] + gain[i]
    return max(altitudes)
    
print(largestAltitude([-5,1,5,0,-7]))