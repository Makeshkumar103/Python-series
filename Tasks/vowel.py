# ...existing code...
s = 'software developer'

vowels = set('aeiou')
vowel_count = 0
consonant_count = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
# ...existing code...