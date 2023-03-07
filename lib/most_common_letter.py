import string
def get_most_common_letter(text):
    counter = {}
    alphabet = list(string.ascii_letters)
    print(alphabet)
    for char in text:
        if char in alphabet:
            counter[char] = counter.get(char, 0) + 1
    
    print(sorted(counter.items(), key=lambda item: item[1]))
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")