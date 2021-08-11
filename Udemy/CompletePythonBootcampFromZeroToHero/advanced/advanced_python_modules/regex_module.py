# (control + '/' for comments)

# regex e.g  search for (555)-555-5555 -> regex pattern: r"(\d{3})-\d{3}-\d{4}"

import re

text = "The agent's phone number is 408-555-1234. Call soon! Call fast!"

match = re.search('phone',text)
print(match) #type:ignore

match = re.search('not in text',text)
print(match) #type:ignore

matches = re.findall('Call',text)
print(matches) 

for match in re.finditer('Call',text):
    print(match)

'''
Character identifiers: (note below has two double slashes to ignore errors, should only have 1 slash)
    \\d     a digit         
    \\w     Alphanumeric
    \\s     White space
    \\D     a non digit
    \\W     non alphanumeric
    \\S     non whitespace
    \\b     Matches if the specified characters are at the beginning or end of a word

Quantifiers:
    +       occurs 1 or more times
    {3}     occurs exactly 3 times
    {2,4}   occurs 2 to 4 times
    {3,}    occurs 3 or more times
    *       occurs 0 or more times
    ?       occurs 0 or 1 time

Additional Syntax:
    .       Wildcard        ".at" will find "cat" "hat" "bat" or whatever in the string
    |       OR operator     "x" | "y" will search string for either "x" or "y"
    ^       Starts with     "^hi" will return a match for "hi dear" and NOT "oh hi dear"
    $       Ends with       "hi$" will return a match for "oh hi" and NOT "oh hi dear"
    [^...]  Excludes        "[^n]" excludes all "n" - findall "hen" will return a list ["h","e"]
    (?=...) +ve lookahead   
    (?!...) -ve lookahead   succeeds if the expression doesnt match at the current position
                            ^question: why do we need (?!...) when we can use [^...]
                            ^answer: [^cat] excludes 'c', or 'a', or 't' and NOT the entire string 'cat'
                            ^i.e [^cat] excludes cat, BUT it also excludes 'ca' from cake, 'a' from apple, and 't' from time
                            ^thus: in order to exclude the entire string 'cat' a lookahead is required
'''


text = "The agent's phone number is 408-555-1234. Call soon! Call fast!"
phone = re.search(r'\d{3}-\d{3}-\d{4}',text)
print("TEST")
print(phone)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
phone = re.search(phone_pattern,text)
print(phone.group(1))  #type:ignore

search_result = re.search(r'cat|dog', "The dog is here!")
print(search_result)

search_results = re.findall(r'.at', "The cat in the hat sat on the bat")
print(search_results)

search_results = re.findall(r'...at', "The cat in the hat sat on the bat")
print(search_results)

search_results = re.findall(r'[^cat]+', "The cat in the hat sat on the bat")
print(search_results)

search_results = re.findall(r'\b(?!.at\b)\w+', "The cat in the hat sat on the bat")
print(search_results)

search_results = re.findall(r'[^!.?]+', "This is a string! With punctuation. How do we remove them?")
print(search_results)
print(" ".join(search_results))

text = "find only hypen-words but you don't know how long-ish they are"
pattern = r"[\w]+-[\w]+"
search_results = re.findall(pattern,text)
print(search_results)

