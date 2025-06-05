def maxVowels(s: str, k: int) -> int:
    vowels = {"a", "e", "i", "o", "u"}
    current = 0
    for i in range(k):
        if s[i] in vowels:
            current += 1
    max_vowels = current
    for right in range(k, len(s)):
        current += (1 if s[right] in vowels else 0) + (-1 if s[right-k] in vowels else 0)
        if current > max_vowels:
            max_vowels = current
    return max_vowels