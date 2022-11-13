"""Package for simplifying writing VapourSynth "plugins" in python."""

__version__ = '1.1.1'

__author__ = 'Setsugen no ao <setsugen@setsugen.dev>'
__maintainer__ = __author__

__author_name__, __author_email__ = [x[:-1] for x in __author__.split('<')]
__maintainer_name__, __maintainer_email__ = [x[:-1] for x in __maintainer__.split('<')]

if __name__ == '__github__':
    print(__version__)
