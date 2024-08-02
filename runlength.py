def printRLE(st):
    n = len(st)
    i = 0

    while i < n:
        # Count occurrences of current character
        count = 1
        while i + 1 < n and st[i] == st[i + 1]:
            i += 1
            count += 1
        
        # Print character and its count
        print(st[i] + str(count), end="")
        i += 1

# Example usage
test_string = "aaabbcddd"
printRLE(test_string)  # Output should be "a3b2c1d3"