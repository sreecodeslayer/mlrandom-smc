
DEFAULT_WORDS = []


class DummyText(object):
    """
    The main entry point for DummyText api which lets you produce random text in Malayalam, with customizable options.
    """

    def __init__(self, charset=set(), limit=0):
        super(DummyText, self).__init__()
        self._charset = charset or frozenset(DEFAULT_WORDS)
        self._limit = limit
        self._text = ''

    @property
    def text(self):
        return self._text

    @property
    def charset(self):
        return self._charset

    @property
    def limit(self):
        return self._limit
