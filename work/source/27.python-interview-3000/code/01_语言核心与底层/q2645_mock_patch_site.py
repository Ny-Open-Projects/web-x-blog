"""mock.patch 的打桩位置:from-import 复制名字 vs 模块属性访问。"""
import sys
import types
from unittest import mock

# 构造两个演示模块:a 定义,b 用 from-import 引入
mod_a = types.ModuleType("fake_a")
mod_a.get_data = lambda: "real"
sys.modules["fake_a"] = mod_a

mod_b = types.ModuleType("fake_b")
exec("from fake_a import get_data\ndef use():\n    return get_data()",
     mod_b.__dict__)
sys.modules["fake_b"] = mod_b

if __name__ == "__main__":
    print("未打桩:", mod_b.use())

    # 打在定义处:使用方手里的旧引用不受影响
    with mock.patch("fake_a.get_data", return_value="stubbed-a"):
        print("patch 定义处:", mod_b.use(), "(仍是 real)")

    # 打在使用处:生效
    with mock.patch("fake_b.get_data", return_value="stubbed-b"):
        print("patch 使用处:", mod_b.use())

    # 属性访问风格:定义处打桩有效
    mod_c = types.ModuleType("fake_c")
    exec("import fake_a\ndef use():\n    return fake_a.get_data()",
         mod_c.__dict__)
    sys.modules["fake_c"] = mod_c
    with mock.patch("fake_a.get_data", return_value="stubbed-c"):
        print("属性访问风格:", mod_c.use())
