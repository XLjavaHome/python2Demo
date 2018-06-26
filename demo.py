d = dict()
d["a"] = 1
d["b"] = 2
print d
del d["a"]
print d
class TestDict(object):
    def __getitem__(self, key):
        return self.__dict__.get(key)
    def __setitem__(self, key, value):
        self.__dict__[key] = value
    def __delitem__(self, key):
        self.__dict__.pop(key)
td = TestDict()
td["a"] = 1
td["b"] = 2
print td["a"]
print td.__dict__
del td["a"]
print td.__dict__
