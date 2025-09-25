for row in range(1):          # row = 0..5  (6 rows)
    for col in range(5):      # col = 0..6  (7 columns per row)
        if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


    print("Hello World")
    print("Hello World")