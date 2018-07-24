import argparse
import sys
from .api import DummyText


def create_parser():
    parser = argparse.ArgumentParser(
        prog='mlrandom',
        add_help=False,
        description='Malayalam Random Text Generator'
        ' [Word | Sentence | Paragraphs]',
        epilog='''Run '%(prog)s --help'for more information.''')

    subparsers = parser.add_subparsers(
        dest='command',
        title='Commands',
        description='These are common commands used in various situations')
    parser_group = parser.add_argument_group(title='Options')
    add_help_arg(parser_group)
    add_punctuate_arg(parser_group)

    wrdparser = subparsers.add_parser(
        'word',
        add_help=False,
        help='Generate a random word',
        description='Generate a random word from a charset')
    wrdparser_group = wrdparser.add_argument_group(title='Options')
    add_word_args(wrdparser)
    add_help_arg(wrdparser_group)
    add_punctuate_arg(wrdparser_group)
    add_charset_arg(wrdparser_group)

    senparser = subparsers.add_parser(
        'sentence',
        add_help=False,
        help='Generate a random sentence',
        description='Generate a random sentence from a charset')
    senparser_group = senparser.add_argument_group(title='Options')
    add_word_args(senparser)
    add_help_arg(senparser_group)
    add_punctuate_arg(senparser_group)
    add_charset_arg(senparser_group)
    add_sentence_args(senparser_group)

    return parser


def add_word_args(group):
    group.add_argument(
        '--minlen',
        type=int,
        default=2,
        dest='minlen',
        help='The minimum number of characeters to be required in a word.')
    group.add_argument(
        '--maxlen',
        type=int,
        default=8,
        dest='maxlen',
        help='The maximum number of characeters to be required in a word.')


def add_sentence_args(group):
    group.add_argument(
        '--wordcount', '-wc',
        type=int,
        default=8,
        dest='wordcount',
        help='The maximum number of words to be required in a sentence.')


def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def add_punctuate_arg(group):
    group.add_argument(
        '--punctuate', '-p',
        type=str2bool,
        default=True,
        dest='punctuate',
        help='Disable punctuations in the paragraphs and sentences')


def add_charset_arg(group):
    group.add_argument(
        '--charset', '-C',
        type=str,
        default='',
        dest='charset',
        help='The characeter set that needs to be used.')


def add_help_arg(group):
    group.add_argument(
        '--help', '-h',
        action='help',
        help='Show this help message and exit')


def cli(args=sys.argv[1:]):

    parser = create_parser()
    ns = parser.parse_args(args)

    dummy = DummyText(punctuate=ns.punctuate)
    if not ns.command:
        parser.print_help()
        return
    elif ns.command == 'word':
        args = [ns.minlen, ns.maxlen, ns.charset]
        print(dummy.gen_word(*args))
        return
    elif ns.command == 'sentence':
        args = [ns.minlen, ns.maxlen, ns.charset]
        print(dummy.gen_sentence(ns.wordcount, *args))
        return
