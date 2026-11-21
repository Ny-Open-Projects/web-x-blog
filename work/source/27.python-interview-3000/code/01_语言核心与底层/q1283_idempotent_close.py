

class ManagedResource:
    def __init__(self, name):
        self.name = name
        self._closed = False

    def close(self):
        if self._closed:
            return                      # 幂等:重复 close 无害
        self._closed = True
        print("closing", self.name)

    def write(self, data):
        if self._closed:
            raise ValueError("I/O on closed resource: %s" % self.name)
        print("write", data)

    def __enter__(self):
        if self._closed:
            raise ValueError("cannot reuse closed resource")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()
        return False


if __name__ == "__main__":
    r = ManagedResource("conn-1")
    with r:
        r.write("hello")
    r.close()                           # with 之后再来一次:静默幂等
    r.close()
    try:
        r.write("again")
    except ValueError as e:
        print("after close ->", e)
