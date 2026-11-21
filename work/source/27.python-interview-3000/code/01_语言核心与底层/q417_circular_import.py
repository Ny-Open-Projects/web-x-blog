import sys
import types

# 用合成模块在单文件里复现循环导入现场
a = types.ModuleType("a"); b = types.ModuleType("b")
sys.modules["a"] = a; sys.modules["b"] = b   # 步骤 1:先注册,模拟开始导入

a_code = "import b\nVALUE = 'a-done'\n"
b_code = "from a import VALUE\n"             # b 在 a 执行完前就要取 a.VALUE

try:
    exec(compile(a_code, "a.py", "exec"), a.__dict__)   # a 执行中转去导入 b
except ImportError as e:
    print("reproduced:", e)
# a 的执行被打断:VALUE 尚未赋值
print("a has VALUE:", hasattr(a, "VALUE"))

# 修复:把 from-import 改为模块级引用,属性访问延迟到使用时
b_code_fixed = "import a\ndef get(): return a.VALUE\n"
exec(compile(b_code_fixed, "b.py", "exec"), b.__dict__)
exec(compile("VALUE = 'a-done'", "a.py", "exec"), a.__dict__)   # 补完 a
print("fixed:", b.get())
