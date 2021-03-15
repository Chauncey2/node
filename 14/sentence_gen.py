"""
使用生成器函数实现sentence类
"""
import re
import reprlib

RE_WORD = re.compile("\w+")


class Sentence:
    
    def __init__(self, words):
        self.text = words
        self.words = RE_WORD.findall(self.words)

    def __repr__(self):
        return 'Sentence()'.format(reprlib.repr(self.text))

    def __iter__(self):
        """
            使用yield语句生成的生成器函数
         """
        for item in self.words:
            yield item
        return
