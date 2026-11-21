import functools

@functools.total_ordering
class SemVer:
    def __init__(self, major, minor):
        self.major, self.minor = major, minor

    def __eq__(self, other):
        if not isinstance(other, SemVer):
            return NotImplemented
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        if not isinstance(other, SemVer):
            return NotImplemented
        return (self.major, self.minor) < (other.major, other.minor)

    def __repr__(self):
        return f"{self.major}.{self.minor}"

if __name__ == "__main__":
    a, b, c = SemVer(1, 0), SemVer(1, 2), SemVer(2, 0)
    print(a < b, b <= c, c > a, a != b)   # <= 与 > 由 total_ordering 推导
    print(sorted([c, a, b]))
    print(max(a, c))
