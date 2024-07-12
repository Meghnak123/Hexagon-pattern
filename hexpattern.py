def print_hexagon_pattern(rows, cols):
    for row in range(rows):
        for part in range(2): 
            for col in range(cols):
                if part == 0:
                    if col % 2 == 0:
                        print(" --- ", end="")
                    else:
                        print("     ", end="")
                else:
                    if col % 2 == 0:
                        print("/   \\", end="")
                        
                       
                    else:
                        print(" ___ ", end="")
            print()
        if row < rows :
            for col in range(cols):
                if col % 2 == 0:
                    print("\\   /", end="")
                else:
                    print("     ", end="")
            print()
    for col in range(cols):
        if col % 2 == 0:
            print(" --- ", end="")
        else:
            print("     ", end="")
    print() 
print("inputs :- 4 7")
print_hexagon_pattern(4, 7)
print()
print("inputs :- 3 5")
print_hexagon_pattern(3, 5)