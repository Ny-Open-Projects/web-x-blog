import sys
import types

# 用 sys.modules + exec 模拟循环导入:A 启动时导入 B,B 又回头导入 A
mod_a = types.ModuleType("demo_a")
mod_b = types.ModuleType("demo_b")
sys.modules["demo_a"] = mod_a   # A 已登记进 sys.modules 但尚未执行完
sys.modules["demo_b"] = mod_b

if __name__ == "__main__":
    # 现场 1:A 要 B 的 helper,此刻 B 还没定义它 -> ImportError
    try:
        exec("from demo_b import helper", mod_a.__dict__)
    except ImportError as e:
        print("cycle hit (A->B):", e)

    # 现场 2:B 补上 helper 后回头要 A 的类,而 A 早已中断 -> ImportError
    exec("def helper():\n    return 'helper'", mod_b.__dict__)
    try:
        exec("from demo_a import ServiceA", mod_b.__dict__)
    except ImportError as e:
        print("cycle hit (B->A):", e)

    # 解法 1:重构——把公共依赖收敛到先完成定义的一方
    exec("""
def helper():
    return "helper"
class ServiceA:
    def use(self):
        return helper() + "-a"
""", mod_a.__dict__)
    print(mod_a.ServiceA().use())

    # 解法 2:延迟导入——函数体内 import,调用时双方模块都已就绪
    src = "def late():\n    import json\n    return json.dumps([1, 2])"
    mod = types.ModuleType("late_mod")
    exec(src, mod.__dict__)
    print(mod.late())

    print("demo_a" in sys.modules, "demo_b" in sys.modules)
