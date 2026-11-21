
FIXTURES = {}

def fixture(fn):
    FIXTURES[fn.__name__] = fn
    return fn

@fixture
def config(request):
    return {"env": "test"}

@fixture
def db(request):
    cfg = request.getfixturevalue("config")
    return f"connected to {cfg['env']}"

class FakeRequest:
    def __init__(self):
        self._cache = {}

    def getfixturevalue(self, name):
        if name not in self._cache:
            self._cache[name] = FIXTURES[name](self)
        return self._cache[name]

if __name__ == "__main__":
    # pytest 里:db = request.getfixturevalue("db") 按需解析
    req = FakeRequest()
    print(req.getfixturevalue("db"))
    print("scope 缓存生效:", req.getfixturevalue("db") is req.getfixturevalue("db"))
