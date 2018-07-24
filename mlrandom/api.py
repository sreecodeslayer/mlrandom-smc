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

    def _gen_word(self, minlen=2, maxlen=8, charset=[]):
        atleast = random.randint(minlen, 4)
        atmost = random.randint(5, maxlen)
        size = random.randint(atleast, atmost)
        word = ''
        while(len(word) < size):
            word += random.choice(charset or self.charset)
        return word

    def gen_word(self,minlen=2,maxlen=8,charset=[]):
        '''
        This function returns a random sized word that may or may not be meaningful
        minlen and maxlen can be used to vary the word's total length.
        Additionally, you can also pass a character set as a list.
        '''
        return self._gen_word(minlen=2,maxlen=8,charset=[])
