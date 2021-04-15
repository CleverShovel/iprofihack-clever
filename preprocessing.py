# import pymorphy2
import enchant, re, nltk, pymorphy2
from nltk.corpus import stopwords

dictionary = enchant.Dict("ru_RU")
nltk.download('stopwords')
morph = pymorphy2.MorphAnalyzer(lang='ru')

# print(morph.parse('стали'))
# print(morph.parse('стали')[0].normal_form)

# import pandas as pd
# df = pd.read_csv('data.csv', sep=r'((?:(^\d+));)|(^(?:(ID));)', skiprows=0, index_col=0)
# print(df)

# print(df)s
# print(df.to_string())

# from numpy import genfromtxt
# my_data = genfromtxt('data.csv', delimiter=';')
stopwords_ru = stopwords.words("russian")
data = ['ID\tQuestion\n']
missplells_log = []
words_errors = []

for idx,line in enumerate(open('onlyquestions').readlines()[:10]):
# for idx,line in enumerate(open('onlyquestions').rseadlines()):
    t = line.strip()
    split_pattern=r'[«]?[а-яА-Я]+[»]?'
    splitted = re.findall(split_pattern, t)
    # splitted = t.split()
    words = []
    char_exceptions = ['«','»']
    exceptions_pattern = r'«|»'
    for word in splitted:
        if word not in stopwords_ru:
            print(morph.normal_forms(token)[0])
        # if not re.search(exceptions_pattern, word):
            # if not dictionary.check(word):
            #     # re.findall(pattern, string)
            #     try:
            #         correct_word = dictionary.suggest(word)[0]
            #         words.append(correct_word)
            #         missplells_log.append(f'"{word}" -> "{correct_word}"\n')
            #     except:
            #         words_errors.append(f'{word}\n')
            #         # pass
            #         # sprint(f'err w/ {word}')
                
            # else:
            #     words.append(word)
        else:
            words.append(word)
    # print(words)
    joined_word = ' '.join(words)
    # print(joined_word)s
    # data.append(f'{idx+1}\t{t}\n')
    # da
    # print(idx,t)

# open('fixedmisspelled.csv','w').writelines(data)
# open('missplells_log.txt','w').writelines(missplells_log)
# open('words_errors.txt','w').writelines(words_errors)

# for line in :
#     t = line.strip()
    # splitted_line = t.split()
    # if len(t) < 6: print(t)
    # if len(splitted_line)<2: print(t)
    


