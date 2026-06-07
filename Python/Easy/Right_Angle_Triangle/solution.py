def pattern(n):
    # Loop through each row from 1 up to n (inclusive)
    for i in range(1, n + 1):
        
        # Loop to print numbers from 1 up to the current row number (i)
        for j in range(1, i + 1):
            # Print the current number followed by a space instead of a newline
            print(j, end=" ")
            
        # Move to the next line after finishing the current row
        print()