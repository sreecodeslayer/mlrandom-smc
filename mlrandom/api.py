import random

DEFAULT_WORDS = [
    'അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'ൠ', 'ഌ',
    'ൡ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ', 'ക', 'ഖ',
    'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ', 'ട', 'ഠ',
    'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 'ദ', 'ധ', 'ന', 'പ', 'ഫ', 'ബ',
    'ഭ', 'മ', 'യ', 'ര', 'ല', 'വ', 'ശ', 'ഷ', 'സ', 'ഹ', 'ള',
    'ഴ', 'റ', 'ഀ', 'ഁ', 'ം', 'ഃ', 'ാ', 'ി', 'ീ', 'ു', 'ൂ',
    'ൃ', 'ൄ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ', '്', 'ൎ'
]

PUNCTUATIONS = [' ', ', ', '. ']
# DEFAULT_WORDS = dict(
#     vowels=['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'ൠ', 'ഌ',
#             'ൡ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ'],
#     consonants=['ക', 'ഖ', 'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ', 'ട', 'ഠ',
#                 'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 'ദ', 'ധ', 'ന', 'പ', 'ഫ', 'ബ',
#                 'ഭ', 'മ', 'യ', 'ര', 'ല', 'വ', 'ശ', 'ഷ', 'സ', 'ഹ', 'ള',
#                 'ഴ', 'റ'],
#     diacs=['ഀ', 'ഁ', 'ം', 'ഃ', 'ാ', 'ി', 'ീ', 'ു', 'ൂ',
#            'ൃ', 'ൄ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ', '്', 'ൎ'])


class DummyText(object):
    """
    The main entry point for DummyText api which lets you produce random text in Malayalam, with customizable options.
    """

    def __init__(self, charset=set(), limit=0, hasnum=False, punctuate=True):
        super(DummyText, self).__init__()
        self._charset = charset or DEFAULT_WORDS
        self._limit = limit
        self._text = ''
        self._hasnum = hasnum
        self._punctuate = punctuate

    @property
    def text(self):
        return self._text

    @property
    def charset(self):
        return self._charset

    @property
    def limit(self):
        return self._limit

    @property
    def hasnum(self):
        return self._hasnum

    def _gen_word(self, minlen=2, maxlen=8, charset=[], *args, **kwargs):
        if minlen > maxlen:
            raise ValueError('minlen cannot be larger than maxlen')

        if isinstance(charset, str):
            charset = set([ch for ch in charset])

        atleast = random.randint(minlen, minlen+2)
        atmost = random.randint(minlen+3, maxlen)
        size = random.randint(atleast, atmost)
        word = ''
        while(len(word) < size):
            word += random.choice(charset or self.charset)
        return word

    def gen_word(self, minlen=2, maxlen=8, charset=[], *args, **kwargs):
        '''
        This function returns a random sized word that may or may not be meaningful
        minlen(default: 2) and maxlen(default: 8) can be used to vary the word's total length.
        Additionally, you can also pass a character set as a list or a string(default: []).
        '''
        return self._gen_word(minlen=2, maxlen=8, charset=[], *args, **kwargs)

    def _gen_sentence(self, word_count=8, *args, **kwargs):
        sentence = [self._gen_word(*args, **kwargs) +
                    ' ' for _ in range(word_count)]
        return ''.join(sentence).strip()

    def gen_sentence(self, word_count=8, *args, **kwargs):
        '''
        This function returns a random sized sentence that may or may not be meaningful
        The function takes an optional word_count for the sentence to have (default: 8), and all other arguments suported by the method: gen_word
        Params minlen and maxlen can be used to vary each word's length.
        Additionally, you can also pass a character set as a list or a string to be used while generating the sentence.
        '''
        return self._gen_sentence(word_count=8, *args, **kwargs)

        
