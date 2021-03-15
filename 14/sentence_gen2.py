import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self,word):
        self.text = word

    def __repr__(self):
        return 'Sentence()'.format(reprlib.repr(self.text))

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()


if __name__ == '__main__':
    s1 = Sentence("world peace !")
    for item in s1:
        print(item )