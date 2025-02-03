# Remove first and last character
def array(_s):
    arr = _s.split(',')
    if len(arr) == 0:
        return None
    else:
        del(arr[0])
    if len(arr) == 0:
        return None
    else:
        del(arr[-1])
    s = ' '.join(arr)
    return None if s == '' else s
# Template Strings
def temple_strings(obj, feature): 
    return((obj) + " are " + str(feature))
# Contamination #1
def contamination(text, char):
  return char*len(text)
# Is it a palindrome?
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]