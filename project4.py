import re

# f = open("paragraphs.txt", "r").readline().lower().split()
# f = open("test_paragraphs.txt", "r").read().split('\n')#.lower().split()
# f = list(filter(None, f))
f = list(filter(None, open("test_paragraphs.txt", "r").read().lower().split('\n')))#.split() #THIS GET ALL PARAGRAPHS INTO A LIST OF INDV STRINGS AS LOWERCASE
# f= open("test_paragraphs.txt", "r").read().lower()
print(f)
new_f = []
for par in f:
    # tmp = re.sub(r'[^a-zA-Z\d\s:]', '', par)
    new_par = re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par))
    new_f.append(new_par)

# f = re.sub(r'\W+', '', f)
print(new_f)