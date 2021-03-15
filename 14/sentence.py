import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    """
    Sentence是可迭代的对象，但不是迭代器
    迭代器需要实现__iter__方法 return self
    """
    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence()'.format(reprlib.repr(self.text))

    def __iter__(self):
        # 每次实例化都会创建一个信的迭代器
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self,words):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word

    def __iter__(self):
        return 







if __name__ == '__main__':

    s1 = Sentence("word to word")
    for item in s1:
        print(item)