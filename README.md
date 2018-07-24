# mlrandom

## Installation

### via clone
1. Clone the repository
2. Run `python setup.py install`

### via pip and git url
1. `pip install git+https://gitlab.com/sreecodeslayer/mlrandom.git`

## Usage
Once the package is installed, command `mlrandom` will be available to you.
It has three subcommands:
1. `mlrandom word`
2. `mlrandom sentence`
3. `mlrandom paragraphs`

#### Help:
```bash
$ mlrandom -h         
usage: mlrandom [--help] [--punctuate PUNCTUATE]
                {word,sentence,paragraphs} ...

Malayalam Random Text Generator [Word | Sentence | Paragraphs]

Commands:
  These are common commands used in various situations

  {word,sentence,paragraphs}
    word                Generate a random word
    sentence            Generate a random sentence
    paragraphs          Generate multiple random paragraphs

Options:
  --help, -h            Show this help message and exit
  --punctuate PUNCTUATE, -p PUNCTUATE
                        Disable punctuations in the paragraphs and sentences

Run 'mlrandom --help'for more information.

```

```bash
$ mlrandom word -h
usage: mlrandom word [--minlen MINLEN] [--maxlen MAXLEN] [--help]
                     [--punctuate PUNCTUATE] [--charset CHARSET]

Generate a random word from a charset

optional arguments:
  --minlen MINLEN       The minimum number of characeters to be required in a
                        word.
  --maxlen MAXLEN       The maximum number of characeters to be required in a
                        word.

Options:
  --help, -h            Show this help message and exit
  --punctuate PUNCTUATE, -p PUNCTUATE
                        Disable punctuations in the paragraphs and sentences
  --charset CHARSET, -C CHARSET
                        The characeter set that needs to be used.

```

```bash
$ mlrandom sentence -h
usage: mlrandom sentence [--minlen MINLEN] [--maxlen MAXLEN] [--help]
                         [--punctuate PUNCTUATE] [--charset CHARSET]
                         [--wordcount WORDCOUNT]

Generate a random sentence from a charset

optional arguments:
  --minlen MINLEN       The minimum number of characeters to be required in a
                        word.
  --maxlen MAXLEN       The maximum number of characeters to be required in a
                        word.

Options:
  --help, -h            Show this help message and exit
  --punctuate PUNCTUATE, -p PUNCTUATE
                        Disable punctuations in the paragraphs and sentences
  --charset CHARSET, -C CHARSET
                        The characeter set that needs to be used.
  --wordcount WORDCOUNT, -wc WORDCOUNT
                        The maximum number of words to be required in a
                        sentence.

```

```bash
$ mlrandom paragraphs -h
usage: mlrandom paragraphs [--minlen MINLEN] [--maxlen MAXLEN] [--help]
                           [--punctuate PUNCTUATE] [--charset CHARSET]
                           [--wordcount WORDCOUNT] [--paracount PARACOUNT]

Generate a random paragraphs from a charset

optional arguments:
  --minlen MINLEN       The minimum number of characeters to be required in a
                        word.
  --maxlen MAXLEN       The maximum number of characeters to be required in a
                        word.

Options:
  --help, -h            Show this help message and exit
  --punctuate PUNCTUATE, -p PUNCTUATE
                        Disable punctuations in the paragraphs and sentences
  --charset CHARSET, -C CHARSET
                        The characeter set that needs to be used.
  --wordcount WORDCOUNT, -wc WORDCOUNT
                        The maximum number of words to be required in a
                        sentence.
  --paracount PARACOUNT, -pc PARACOUNT
                        The maximum number of paragraphs to be required in the
                        text.

```