def rabin_karp_search(text, pattern, d=256, q=101):
    """
    d: Number of characters in the input alphabet (e.g., 256 for ASCII)
    q: A prime number for modulo to reduce hash value size
    """
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []  # Empty pattern matches at every position
    if m > n:
        return []  # Pattern longer than text, no match possible
    
    # Calculate h = pow(d, m-1) % q
    h = 1
    for _ in range(m - 1):
        h = (h * d) % q
    
    # Calculate hash value for pattern and first window of text
    pattern_hash = 0
    window_hash = 0
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % q
        window_hash = (d * window_hash + ord(text[i])) % q
    
    positions = []  # Store starting positions of matches
    
    # Slide pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == window_hash:
            # Verify character by character to handle hash collisions
            match = True
            for j in range(m):
                if pattern[j] != text[i + j]:
                    match = False
                    break
            if match:
                positions.append(i)
        
        # Calculate hash value for next window by removing leading digit
        # and adding trailing digit
        if i < n - m:
            window_hash = (d * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % q
            # Ensure window_hash is non-negative
            if window_hash < 0:
                window_hash += q
    
    return positions

# Function to get user input
def get_user_input():
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search for: ")
    return text, pattern

# Main execution
if __name__ == "__main__":
    text, pattern = get_user_input()
    
    print(f"\nText: {text}")
    print(f"Pattern: {pattern}")
    
    positions = rabin_karp_search(text, pattern)
    
    if positions:
        print(f"Pattern found at position(s): {positions}")
        for pos in positions:
            print(f"Match: {text[pos:pos + len(pattern)]} at index {pos}")
    else:
        print("Pattern not found in the text.")