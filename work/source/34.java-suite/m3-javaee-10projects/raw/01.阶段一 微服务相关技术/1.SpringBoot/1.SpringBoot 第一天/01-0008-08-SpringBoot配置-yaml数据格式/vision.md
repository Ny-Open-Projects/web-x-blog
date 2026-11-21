# 画面线理解：08-SpringBoot配置-yaml数据格式

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\08-SpringBoot配置-yaml数据格式_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 01:29, 03:16, 04:31, 04:33, 05:20, 05:37, 05:41, 09:13, 09:14, 09:42, 09:58, 09:59, 10:12, 10:15
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 02:15:06

1) 这一组画面整体在讲 SpringBoot 中 YAML 配置文件的语法、数据格式、参数引用及小结。

2) 按时间顺序列出每张画面的要点：
画面 1: PPT 页面，标题为“SpringBoot 配置”，子标题“YAML：数据格式”，内容包括对象（map）和数组（array）的 YAML 语法示例。
画面 2: IDEA 编辑器，显示项目结构，选中 `application.yml` 文件，内容为 `server: port: 8082`，光标在 `hehe` 后。
画面 3: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082`，`name: abc`，`person: name: zhangsan`。
画面 4: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082`，`name: abc`，`person: name: zhangsan age: 20`。
画面 5: IDEA 编辑器，切换到 `application.properties` 文件，内容为 `server.port=8082 name=abc`。
画面 6: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: zhangsan age: 20`。
画面 7: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: zhangsan age: 20`，光标在文件末尾。
画面 8: PPT 页面，标题为“SpringBoot 配置”，子标题“YAML：数据格式”，内容包括对象（map）、数组（array）和纯量（scalar）的 YAML 语法示例。
画面 9: PPT 页面，标题为“SpringBoot 配置”，子标题“YAML：参数引用”，内容为 `name: lisi person: name: ${name} # 引用上边定义的name值`。
画面 10: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: zhangsan age: 20 address: - beijing - shanghai msg1: 'hello \n world' # 不会识别转义字符，会原样输出 msg2: "hello \n world" # 双引号转义字符`。
画面 11: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: ${name} age: 20 address: - beijing - shanghai msg1: 'hello \n world' # 不会识别转义字符，会原样输出 msg2: "hello \n world" # 双引号转义字符`，光标在 `name: ${name}` 后，弹出系统属性提示框。
画面 12: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: ${name} age: 20 address: - beijing - shanghai msg1: 'hello \n world' # 不会识别转义字符，会原样输出 msg2: "hello \n world" # 双引号转义字符`，光标在 `name: ${name}` 后。
画面 13: PPT 页面，标题为“SpringBoot 配置”，子标题“YAML：参数引用”，内容为 `name: lisi person: name: ${name} # 引用上边定义的name值`。
画面 14: PPT 页面，标题为“SpringBoot 配置”，子标题“YAML：小结”，内容为“1) 配置文件类型：properties: 和以前一样 yaml/yaml: 注意空格 2) yaml: 简洁，以数据为核心 基本语法：大小写敏感 数据值前边必须有空格，作为分隔符 使用空格缩进表示层级关系，相同缩进表示同一级 数据格式：对象 数组：使用 “-” 表示数组每个元素 纯量 参数引用：${key}`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```
对象(map): 键值对的集合.
person:
  name: zhangsan
# 行内写法
person: {name: zhangsan}

数组: 一组按次序排列的值
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]
```

画面 2:
```
server:
  port: 8082
```

画面 3:
```
server:
  port: 8082
name: abc
# 对象
person:
  name: zhangsan
```

画面 4:
```
server:
  port: 8082
name: abc
# 对象
person:
  name: zhangsan
  age: 20
```

画面 5:
```
server.port=8082
name=abc
```

画面 6:
```
server:
  port: 8082
name: abc
person:
  name: zhangsan
  age: 20
```

画面 7:
```
server:
  port: 8082
name: abc
person:
  name: zhangsan
  age: 20
```

画面 8:
```
对象(map): 键值对的集合.
person:
  name: zhangsan
# 行内写法
person: {name: zhangsan}

数组: 一组按次序排列的值
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

纯量: 单个的、不可再分的值
msg1: 'hello \n world' # 单引号转义字符
msg2: "hello \n world" # 双引号转义字符
```

画面 9:
```
name: lisi
person:
  name: ${name} # 引用上边定义的name值
```

画面 10:
```
server:
  port: 8082
name: abc
person:
  name: zhangsan
  age: 20
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

# 纯量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 双引号转义字符
```

画面 11:
```
server:
  port: 8082
name: abc
person:
  name: ${name}
  age: 20
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

# 纯量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 双引号转义字符
```

画面 12:
```
server:
  port: 8082
name: abc
person:
  name: ${name}
  age: 20
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

# 纯量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 双引号转义字符
```

画面 13:
```
name: lisi
person:
  name: ${name} # 引用上边定义的name值
```

画面 14:
```
1) 配置文件类型
  • properties: 和以前一样
  • yaml/yaml: 注意空格
2) yaml: 简洁，以数据为核心
  • 基本语法
    • 大小写敏感
    • 数据值前边必须有空格，作为分隔符
    • 使用空格缩进表示层级关系，相同缩进表示同一级
  • 数据格式
    • 对象
    • 数组: 使用 “-” 表示数组每个元素
    • 纯量
  • 参数引用
    • ${key}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: 标题“SpringBoot 配置”，子标题“YAML：数据格式”，内容为 YAML 对象和数组的示例。
画面 8: 标题“SpringBoot 配置”，子标题“YAML：数据格式”，内容为 YAML 对象、数组和纯量的示例。
画面 9: 标题“SpringBoot 配置”，子标题“YAML：参数引用”，内容为 YAML 参数引用示
