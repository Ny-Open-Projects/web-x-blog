"""配置驱动的动态导入:后端选择器与导入白名单。"""
import importlib

REGISTRY = {                       # 配置名 -> 模块.属性,白名单防任意导入
    "json": "json.dumps",
    "csv": "csv.writer",
}


class BackendError(Exception):
    pass


def load_backend(name):
    if name not in REGISTRY:
        raise BackendError("不在白名单: " + name)
    mod_name, _, attr = REGISTRY[name].rpartition(".")
    module = importlib.import_module(mod_name)   # 运行时按配置导入
    return getattr(module, attr)


if __name__ == "__main__":
    dumps = load_backend("json")
    print("json 后端:", dumps({"k": "中文"}, ensure_ascii=False))
    writer_cls = load_backend("csv")
    print("csv 后端:", writer_cls.__name__)
    for bad in ("os", "builtins"):
        try:
            load_backend(bad)
        except BackendError as e:
            print("白名单拦截:", e)
