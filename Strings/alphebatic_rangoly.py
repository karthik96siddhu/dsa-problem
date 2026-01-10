import string

def print_rangoli(size):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3
    lines = []

    # Build from center to top
    for i in range(size):
        left = alphabet[size-1:i:-1]
        middle = alphabet[i]
        right = alphabet[i+1:size]
        row = "-".join(left + middle + right)
        lines.append(row.center(width, "-"))

    # Reverse to get top half, then mirror for bottom
    top = lines[::-1]
    bottom = lines[1:]

    print("\n".join(top + bottom))

print_rangoli(5)

# Sample Output:
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

