---
title: [Q2378] import 遮蔽的排查
date: 2026-11-17
categories: [Python语言核心]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q2378 · import 遮蔽的排查

> 难度:★★★★☆ | 标签:import 遮蔽, sys.path, debug

**问**:import json 导进了本地同名文件,怎么发现、怎么定位、怎么根治?

**答**:同名文件遮蔽标准库是最高频的 import 事故(目录里有 json.py、email.py,或脚本名叫 random.py)。定位三件套:`模块.__file__` 看 json 到底从哪加载,出现项目路径即中招;`sys.modules["json"]` 查当前会话已缓存的模块对象;`python -v` 启动会打印每个模块的加载来源,遮蔽现场一目了然。复现方法:在同目录起子进程 import,实测 demo 里本地 json.py 成功顶掉标准库——因为 sys.path[0](脚本目录)排在标准库之前。排查口诀:「报错的属性方法不存在」+「该模块标准库明明有」→ 先怀疑遮蔽。根治:本地文件绝不与标准库/关键第三方库同名(命名习惯加业务前缀);把脚本移出同名目录;用绝对导入与规范包结构让查找路径可控。CI 里加一步 `python -c "import 关键模块; 校验 __file__ 路径"` 可以自动把关。

```python
# file: code/01_语言核心与底层/q2378_import_shadowing.py
"""import 遮蔽排查:同名文件盖掉标准库的定位方法。"""
import os
import subprocess
import sys
import tempfile

if __name__ == "__main__":
    import json
    print("正常环境 json 来源:", json.__file__)

    shadow_dir = tempfile.mkdtemp(prefix="shadow_")
    with open(os.path.join(shadow_dir, "json.py"), "w") as f:
        f.write("value = '我是本地假 json'\n")

    probe = "import json; print(json.__file__); print(getattr(json, 'value', '真模块'))"
    proc = subprocess.run(
        [sys.executable, "-c", probe],
        cwd=shadow_dir,
        capture_output=True, text=True,
        env={**os.environ, "PYTHONPATH": shadow_dir},
    )
    print("被遮蔽时的加载来源与结果:")
    for line in proc.stdout.strip().splitlines():
        print("   ", line)

    print("排查1 sys.path 首位:", repr(sys.path[0]))
    print("排查2 sys.modules 指向:", sys.modules["json"].__file__)
    print("排查3 python -v 会打印每个模块的加载来源")
```

**追问**:1) 为什么 -c 或交互式环境下更容显中招?——此时 sys.path[0] 是空串即当前工作目录,本地同名文件天然排第一;脚本模式 sys.path[0] 是脚本所在目录,同理。2) 排查手法?——`import x; print(x.__file__)` 看实际来源;sys.path 快照;python -X importtime 看导入耗时异常;改名验证「是不是遮蔽」。3) 常见肇事者?——脚本名撞标准库(random.py/email.py)、测试目录同名模块、打包把本地脚本带进部署(Q485)。4) 生产陷阱?——遮蔽标准库让依赖它的模块连锁崩;目录里的旧同名文件复活;容器镜像残留调试脚本;修复靠「删文件」而不是「改 sys.path」。
