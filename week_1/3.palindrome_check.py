def check_palindrome(n):
    # Negative numbers are not considered as palindromes
    if n < 0:
        return False
    
    original_number = n
    reversed_number = 0

    while n > 0:
        digit = n % 10
        reversed_number = reversed_number * 10 + digit
        n //= 10

    return original_number == reversed_number

if __name__ == "__main__":

    n = int(input("Enter the number: "))
    
    if check_palindrome(n):
        print(f"The given number {n} is a palindrome")
    else:
        print(f"The given number {n} is not a palindrome")
