import re

# f = open("paragraphs.txt", "r").readline().lower().split()
# f = open("test_paragraphs.txt", "r").read().split('\n')#.lower().split()
# f = list(filter(None, f))
f = list(filter(None, open("test_paragraphs.txt", "r").read().lower().split('\n')))#.split() #THIS GET ALL PARAGRAPHS INTO A LIST OF INDV STRINGS AS LOWERCASE
stop_words = open("stop_words.txt", "r").read().split()
print(stop_words)
# f= open("test_paragraphs.txt", "r").read().lower()
print(f)
new_f = []
for par in f:
    # tmp = re.sub(r'[^a-zA-Z\d\s:]', '', par)
    new_par = re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par))
    new_f.append(new_par)
    # print(new_par)
    #par_lst = []
    # # par_lst.append(par_lst.split())
    # for par in new_par:
    #     par_lst.append(par.split())
    # # print(par_lst)
    # new_f.append(par_lst)
print(new_f)

#remove stop words:
# no_sw_paragraph = [word for word in new_f if word not in stop_words]
# result = ' '.join(no_sw_paragraph)
# print(no_sw_paragraph)

newest_f = []
for par in new_f:
    wrds = par.strip().split()
    newest_f.append(wrds)
print(newest_f)

final_f = []
for par in newest_f:
    no_sw_paragraph = [word for word in par if word not in stop_words]
    # result = ' '.join(no_sw_paragraph)
    final_f.append(no_sw_paragraph)

print(final_f)

# f = re.sub(r'\W+', '', f)
