def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        right -= 1
        left += 1

    return True
input_string = input("Введите строку: ")
if is_palindrome(input_string):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")