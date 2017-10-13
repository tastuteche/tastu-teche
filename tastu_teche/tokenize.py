import string
from nltk import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words.update(list(string.punctuation))
# stop_words.update(["gt", "lt"])

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")

# translator = str.maketrans('', '', string.punctuation)
replace_punctuation = str.maketrans(
    string.punctuation + '0123456789', ' ' * (len(string.punctuation) + 10))

from collections import Counter, defaultdict
dict_stem_word = defaultdict(Counter)


def _stem(word):
    stem = stemmer.stem(word)
    dict_stem_word[stem].update([word])
    return stem


def tokenize(text):
    return [_stem(word) for word in word_tokenize(text.lower().translate(replace_punctuation)) if word not in stop_words]


def stem2word(stem):
    return dict_stem_word[stem].most_common(1)[0][0]


def word_trigram_count(trigram_count):
    return [("%s_%s_%s" % (stem2word(stem1), stem2word(stem2), stem2word(stem3)), count)
            for (stem1, stem2, stem3), count in trigram_count]


def word_bigram_count(bigram_count):
    return [("%s_%s" % (stem2word(stem1), stem2word(stem2)), count)
            for (stem1, stem2), count in bigram_count]


def word_unigram_count(unigram_count):
    return [(stem2word(stem), count) for stem, count in unigram_count]
