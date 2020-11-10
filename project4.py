import re
import PorterStemmer as Porter
import numpy as np
import pandas as pd


def readandprocess():
    pars = list(filter(None, open("paragraphs.txt", "r").read().lower().split('\n')))
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
            stemmed_par.append(p.stem(word, 0, len(word) - 1))
        stemmed_t_pars.append(stemmed_par)
    return stemmed_t_pars


def featureVector(s_pars):
    f_vector = []
    seen = set()
    for par in s_pars:
        words = [x for x in par if not (x in seen or seen.add(x))]
        for w in words:
            f_vector.append(w)
    return f_vector


def createTDM(f_v, pars):
    tdm = [["Keyword set"]]
    # create column headers
    for f in f_v:
        tdm[0].append(f)
    # create rows of TDM
    itr = 0
    for par in pars:
        itr += 1
        par_cnt = []
        for kw in tdm[0]:
            if kw == "Keyword set":
                par_cnt.append("Paragraph " + str(itr))
            else:
                par_cnt.append(par.count(kw))
        tdm.append(par_cnt)
    # return tdm
    return np.array(tdm)


def csvTDM(tdm):
    # np.savetxt("TDM.csv", tdm, delimiter=",")
    df = pd.DataFrame(tdm)
    df.to_csv('TDM.csv', index=False)



if __name__ == '__main__':
    p = Porter.PorterStemmer()
    processed_pars = readandprocess()
    print(processed_pars)
    stemmed_pars = doStemming(p, processed_pars)
    print(stemmed_pars)
    feature_vector = featureVector(stemmed_pars) #need show feature vector in report
    print(feature_vector)
    TDM = createTDM(feature_vector, stemmed_pars)
    csvTDM(TDM)
