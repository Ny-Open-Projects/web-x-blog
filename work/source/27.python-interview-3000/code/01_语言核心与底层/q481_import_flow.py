import importlib.util
import sys

def explain(name):
    spec = importlib.util.find_spec(name)
    print(f"module {name}:")
    print("  origin :", spec.origin)
    print("  loader :", type(spec.loader).__name__)
    print("  cached :", spec.cached)

if __name__ == "__main__":
    print("meta_path finders:")
    for f in sys.meta_path:
        print("  -", f.__name__ if isinstance(f, type) else type(f).__name__)
    explain("json")
    m = __import__("json")
    print("registered in sys.modules:", sys.modules["json"] is m)
