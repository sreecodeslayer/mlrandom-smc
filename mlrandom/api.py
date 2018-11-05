import random
from mlrandom.morphology import Mlmorph
from mlrandom.constants import *


class DummyText(object):
    """
    The main entry point for DummyText api which lets you produce random text in Malayalam, with customizable options.
    """

    def __init__(self, charset=set(), limit=0, hasnum=False,
                 punctuate=True, logical=True, apply_rules=True):
        super(DummyText, self).__init__()
        self._charset = charset or DEFAULT_WORDS
        self._limit = limit
        self._text = ''
        self._hasnum = hasnum  # Todo:
        self._punctuate = punctuate
        self._islogical = logical
        self._applyrules = logical or apply_rules
        self.morph = Mlmorph()

    @property
    def text(self):
        return self._text

    @property
    def islogical(self):
        return self._islogical

    @property
    def charset(self):
        return self._charset

    @property
    def limit(self):
        return self._limit

    @property
    def hasnum(self):
        return self._hasnum

    # Rules

    def _startswith_consonant_vowel(self, word):
        try:
            tok = str(word)[0]
            rule = tok in (
                self.charset['constants'] | tok in self.charset['vowels'])
            return rule
        except IndexError:
            return False

    def _no_following_vowel(self, word):
        try:
            tok = str(word)
            for char in tok:
                if char in self.charset['vowels']:
                    pos = tok.index(char)
                    if tok[pos+1] in self.charset['vowels']:
                        return False
            return True
        except IndexError:
            return True

    def _vowel_at_begining_only(self, word, size):
        cutoff = int(size/2)
        rule = set(list(word[cutoff:size])).issubset(
            self.charset['vowels'])
        return not rule

    def _gen_word(self, minlen=2, maxlen=8, charset=[], *args, **kwargs):
        if minlen > maxlen:
            raise ValueError('minlen cannot be larger than maxlen')

        charset = charset or self.charset
        if isinstance(charset, str):
            charset = list(set([ch for ch in charset]))

        atleast = random.randint(minlen, minlen+2)
        atmost = random.randint(minlen+3, maxlen)
        size = random.randint(atleast, atmost)
        word = ''
        while(len(word) < size):
            word += random.choice(charset)
        return word

    def gen_word(self, minlen=2, maxlen=8, charset=[], *args, **kwargs):
        '''
        This function returns a random sized word that may or may not be meaningful
        minlen(default: 2) and maxlen(default: 8) can be used to vary the word's total length.
        Additionally, you can also pass a character set as a list or a string(default: []).
        '''

        meaningful = False
        charset = charset or self.charset
        word = self._gen_word(minlen, maxlen, charset, *args, **kwargs)
        if self.islogical:
            while not meaningful:
                word = self._gen_word(minlen, maxlen, charset, *args, **kwargs)
                if self.morph.analyse(word):
                    meaningful = True
                    self._text += word
                    return word
        return word

    def _gen_sentence(self, word_count=8, *args, **kwargs):
        sentence = [self._gen_word(*args, **kwargs) +
                    ' ' for _ in range(word_count)]
        sentence = ''.join(sentence).strip()
        if self._punctuate:
            sentence += random.choice(PUNCTUATIONS)
        self._text += sentence
        return sentence

    def gen_sentence(self, word_count=8, *args, **kwargs):
        '''
        This function returns a random sized sentence that may or may not be meaningful
        The function takes an optional word_count for the sentence to have (default: 8), and all other arguments suported by the method: gen_word
        Params minlen and maxlen can be used to vary each word's length.
        Additionally, you can also pass a character set as a list or a string to be used while generating the sentence.
        '''
        return self._gen_sentence(word_count, *args, **kwargs)

    def _gen_paragraph(
            self, paras=5, *args, **kwargs):
        para = ''
        text = []
        atleast = random.randint(5, 8)
        atmost = random.randint(8, 10)

        size = random.randint(atleast, atmost)
        for _ in range(paras):
            scount = 0
            para = ''
            while(scount < size):
                para += self._gen_sentence(*args, **kwargs)
                if self._punctuate:
                    para + random.choice(PUNCTUATIONS).strip()

                scount += 1
            text.append(para.strip())
        text = '\n'.join(text)
        self._text += text
        return text

    def gen_paragraph(self, paras=5, *args, **kwargs):
        '''
        This function returns a random sized paragraph that may or may not be meaningful
        It also supports specifying a paragraph count (default: 5), which will be separated by a full stop and a new line character if punctuations are enabled.
        All other params of `gen_sentence` and `gen_word` are supported.
        '''
        return self._gen_paragraph(paras, *args, **kwargs)
