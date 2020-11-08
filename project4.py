import re


f = list(filter(None, open("test_paragraphs.txt", "r").read().lower().split('\n')))
stop_words = open("stop_words.txt", "r").read().split()

new_f = []
newest_f = []
final_f = []
for par in f:
    # new_f.append(re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par)).strip().split())
    # newest_f.append(re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par)).strip().split())
    # t_par = re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par)).strip().split()
    final_f.append([word for word in re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par)).strip().split() if word not in stop_words])

# newest_f = []
# for par in new_f:
#     newest_f.append(par.strip().split())

# final_f = []
# for par in newest_f:
#     final_f.append([word for word in par if word not in stop_words])

print(final_f)
