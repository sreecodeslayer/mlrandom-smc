import random

# DEFAULT_WORDS = [
#     'അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'ൠ', 'ഌ',
#     'ൡ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ', 'ക', 'ഖ',
#     'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ', 'ട', 'ഠ',
#     'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 'ദ', 'ധ', 'ന', 'പ', 'ഫ', 'ബ',
#     'ഭ', 'മ', 'യ', 'ര', 'ല', 'വ', 'ശ', 'ഷ', 'സ', 'ഹ', 'ള',
#     'ഴ', 'റ', 'ഀ', 'ഁ', 'ം', 'ഃ', 'ാ', 'ി', 'ീ', 'ു', 'ൂ',
#     'ൃ', 'ൄ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ', '്', 'ൎ'
# ]
DEFAULT_WORDS = dict(
    vowels=['അ', 'ആ', 'ഇ', 'ഈ', 'ഉ', 'ഊ', 'ഋ', 'ൠ', 'ഌ',
            'ൡ', 'എ', 'ഏ', 'ഐ', 'ഒ', 'ഓ', 'ഔ'],
    consonants=['ക', 'ഖ', 'ഗ', 'ഘ', 'ങ', 'ച', 'ഛ', 'ജ', 'ഝ', 'ഞ', 'ട', 'ഠ',
                'ഡ', 'ഢ', 'ണ', 'ത', 'ഥ', 'ദ', 'ധ', 'ന', 'പ', 'ഫ', 'ബ',
                'ഭ', 'മ', 'യ', 'ര', 'ല', 'വ', 'ശ', 'ഷ', 'സ', 'ഹ', 'ള',
                'ഴ', 'റ'],
    diacs=['ഀ', 'ഁ', 'ം', 'ഃ', 'ാ', 'ി', 'ീ', 'ു', 'ൂ',
           'ൃ', 'ൄ', 'െ', 'േ', 'ൈ', 'ൊ', 'ോ', 'ൌ', '്', 'ൎ'])


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

    def _gen_word(self, count=1):
        atleast = random.randint(2, 4)
        atmost = random.randint(5, 8)
        wordlen = random.randint(atleast, atmost)
        word = ''
        while(len(word) < wordlen):
            con_dia = '%s%s%s' % (
                random.choice(self.charset['consonants']),
                random.choice(self.charset['diacs']),
                random.choice(self.charset['consonants']),
            )
            word += con_dia
        return word
