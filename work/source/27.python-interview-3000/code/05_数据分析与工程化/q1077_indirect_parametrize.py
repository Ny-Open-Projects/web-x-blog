
FIXTURES = {}

def fixture(name):
    def deco(fn):
        FIXTURES[name] = fn
        return fn
    return deco

@fixture("db")
def db_fixture(request):
    # indirect=True 时,参数化值通过 request.param 进入 fixture
    env = request.param
    return {"engine": "sqlite", "env": env}

def parametrize(argname, values, indirect=False):
    cases = []
    for v in values:
        if indirect:
            fake_request = type("R", (), {"param": v})()
            cases.append((argname, FIXTURES[argname](fake_request)))
        else:
            cases.append((argname, v))
    return cases

if __name__ == "__main__":
    # pytest 中:@pytest.mark.parametrize("db", ["prod", "staging"], indirect=True)
    for name, value in parametrize("db", ["prod", "staging"], indirect=True):
        print(name, value)
