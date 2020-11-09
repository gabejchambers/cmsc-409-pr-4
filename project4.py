import re
import PorterStemmer as Porter


def readandprocess():
    pars = list(filter(None, open("test_paragraphs.txt", "r").read().lower().split('\n')))
    sw = open("stop_words.txt", "r").read().split()
    processed_pars = []
    for par in pars:
        processed_pars.append(
            [word for word in re.sub(r'\s+', ' ', re.sub(r'[^a-zA-Z\s]', '', par)).strip().split() if word not in sw])
    return processed_pars

def doStemming(p, p_pars):
    stemmed_t_pars = []
    for par in p_pars:
        stemmed_par = []
        for word in par:
            stemmed_par.append(p.stem(word, 0,len(word)-1))
        stemmed_t_pars.append(stemmed_par)
    return stemmed_t_pars



if __name__ == '__main__':
    p = Porter.PorterStemmer()
    processed_pars = readandprocess()
    print(processed_pars)
    stemmed_pars = doStemming(p, processed_pars)
    print(stemmed_pars)

