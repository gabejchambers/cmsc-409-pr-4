import re


def readandprocess():
    pars = list(filter(None, open("test_paragraphs.txt", "r").read().lower().split('\n')))
    sw = open("stop_words.txt", "r").read().split()
    processed_pars = []
    for par in pars:
        processed_pars.append(
            [word for word in re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par)).strip().split() if word not in sw])
    return processed_pars


if __name__ == '__main__':
    processed_pars = readandprocess()
    print(processed_pars)
