def palindrome_triangle(N):
    for i in range(1, N + 1):
        print(int('1' * i)**2)

palindrome_triangle(int(input()))