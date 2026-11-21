import importlib

class LazyModule:
    """属性首次访问时才真正 import"""
    def __init__(self, modname):
        self._modname = modname
        self._module = None

    def _load(self):
        if self._module is None:
            print(f"[lazy] importing {self._modname} now")
            self._module = importlib.import_module(self._modname)
        return self._module

    def __getattr__(self, name):
        return getattr(self._load(), name)

    def __dir__(self):
        return dir(self._load())

class Config:
    json = LazyModule("json")
    zlib = LazyModule("zlib")

if __name__ == "__main__":
    c = Config()
    print("created without importing json or zlib")
    print(c.json.dumps({"a": 1}))         # 此刻才 import json
    print(c.zlib.crc32(b"hello"))         # zlib 同样按需加载
