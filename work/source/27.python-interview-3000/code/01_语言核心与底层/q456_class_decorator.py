def comparable(cls):
    """基于 _key 方法注入 == < 和 hash"""
    if hasattr(cls, "_key") is False:
        raise TypeError(f"{cls.__name__} must define _key")

    def __eq__(self, other):
        if not isinstance(other, cls):
            return NotImplemented
        return self._key() == other._key()

    def __lt__(self, other):
        if not isinstance(other, cls):
            return NotImplemented
        return self._key() < other._key()

    cls.__eq__ = __eq__
    cls.__lt__ = __lt__
    cls.__hash__ = lambda self: hash(self._key())
    return cls

@comparable
class Version:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def _key(self):
        return (self.major, self.minor)

    def __repr__(self):
        return f"{self.major}.{self.minor}"

if __name__ == "__main__":
    a, b, c = Version(1, 0), Version(1, 0), Version(2, 0)
    print(a == b, a < c)
    print(sorted([c, b, a]))
    print({a: "v1.0"}[b])                 # hash 注入后可做 dict key
