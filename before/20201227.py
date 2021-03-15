# -*- encoding:utf-8 -*-

def this_is_memaryview():
    """所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问。


    """
    # what is memaryview
    # memoryview() 函数返回给定参数的内存查看对象(memory view)。
    a = 'this is test'
    a = a.encode()
    v = memoryview(a)
    print(v.tobytes()) # b'this is test'
    print(v[1])

def listcomps():
    la = ["a","b"]
    lb = [1,2,3,4]
    result = [[c,n] for c in la for n in lb]
    print(result)

def genexps():
    ta ="abcde"
    t = (ord(i) for i in ta) 
    # <generator object genexps.<locals>.<genexpr> at 0x00000225304E2548>   
    print(t)
    for i in t:
        print(i)

def printx(a,b,c):

    print(a,b,c)

def make_nametuple():
    from collections import namedtuple 
    Card = namedtuple("Card",["rank","suit"])
    cad = Card('A','黑桃') 
    print(cad) # Card(rank='A', suit='黑桃'

def user_bisect():
    from bisect import bisect,insect
    a = [1,2,3,4,5,6]


def dictcomp():
    source =[("pert",18),
             ("Nicy",16),
             ("Bob",20)
            ]
    people_info_dict = {name:age for name,age in source}
    print(people_info_dict) # {'pert': 18, 'Nicy': 16, 'Bob': 20}

def deal_non_key_from_dict():
    import collections
    # 1. list被传递进defaultdict‘作为default_factory 
    #   当调用的key值不存在的时候，则会调用default_factory创建一个空的序列
    #   不会报keyError
    default_dict = collections.defaultdict(list)  # befor:defaultdict(<class 'list'>, {})
    print("befor:{}".format(default_dict)) 
    # 2. default_factory 只会在 __getitem__ 里被调用，在其他方法里是无效的，例如get[key]就会报keyError
    print(default_dict["a"]) # []
    default_dict["b"] = 1
    print(default_dict["c"]) # []
    print("after:{}".format(default_dict)) # after:defaultdict(<class 'list'>, {'a': [], 'b': 1, 'c': []})
    print("after:{}".format(dict(default_dict))) # after:{'a': [], 'b': 1, 'c': []}

def test_dict_keys():
    d = dict()
    keys_iter = d.keys()
    print(type(keys_iter)) # <class 'dict_keys'>
    print(isinstance(keys_iter,memoryview)) # False


def test_chain_map():
    
    pass

def test_counter():
    import collections 
    counter = collections.Counter()
    print(counter) # Counter()
    counter.update("aaa")  # update方法属于原地操作
    print(counter) # Counter({'a': 3})

    l1 = ["蓝色","红","红","黑色","红","红","红",]
    counter2 = collections.Counter(l1) # Counter({'红': 5, '蓝色': 1, '黑色': 1})
    print(counter2)


from collections import UserDict

class strkeydict(UserDict):
    def __missing__(self,key):
        # 这个判断是用来避免陷入无限递归(边界条件)
        if isinstance(key,str):
            raise keyError(key)
        # return self.data[str(key)]
        return self[str(key)]

    def __contains__(self,key):
        return str(key) in self.data

    def __setitem__(self,key,item):
        self.data[str(key)] = item


def test_mappingproxytype():
    from types import MappingProxyType as mpt
    d = {"a":1}
    d_proxy = mpt(d)
    print(d)




def main():
   # dictcomp()
   # this_is_memaryview()
   # listcomps()
   # genexps()
   # a = (1,2,3)
   # printx(*a)
   # a,b,*rest = range(5)
   # print(a,b,rest) # 0 1 [2, 3, 4]
   # make_nametuple()
   # d = {"a":"11","b":"22"}
   # print(d.get("c",default))

   # deal_non_key_from_dict()
   # test_dict_keys()
   test_mappingproxytype()


if __name__ == '__main__':
    main()