def is_palindrome(s):
    s = s.lower().replace(" ", "").replace(".", "").replace(",","").replace("'","")
    if s == s[::-1]:
        print("Palindrome")
    else:
        print("None-palindrome")

str = "Madam, in Eden, I'm Adam"
is_palindrome(str)
stt = "KBTU"
is_palindrome(stt)
'''Palindrome
None-palindrome'''