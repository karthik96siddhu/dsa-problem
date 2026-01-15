def minion_game(string):
    vowels = "AEIOU"
    n = len(string)

    kevin = 0
    stuart = 0

    for i in range(n):
        points = n - i
        if string[i] in vowels:
            kevin += points # 5+3+1
        else:
            stuart += points # 6 + 4 + 2
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

minion_game("BANANA")
# Sample Output:
# Stuart 12   