def rabin_karp_search(text, pattern, d=256, q=101):
    n, m = len(text), len(pattern)
    if m == 0 or m > n:
        return []
    
    h, pattern_hash, window_hash = pow(d, m-1, q), 0, 0
    positions = []
    
    for i in range(m):  # Compute initial hash values
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q

    for i in range(n - m + 1):
        if pattern_hash == window_hash and text[i:i + m] == pattern:
            positions.append(i)
        
        if i < n - m:  # Compute next window hash
            window_hash = (d * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            if window_hash < 0:
                window_hash += q

    return positions

if __name__ == "__main__":
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")

    positions = rabin_karp_search(text, pattern)
    if positions:
        print(f"Pattern found at positions: {positions}")
    else:
        print("Pattern not found.")