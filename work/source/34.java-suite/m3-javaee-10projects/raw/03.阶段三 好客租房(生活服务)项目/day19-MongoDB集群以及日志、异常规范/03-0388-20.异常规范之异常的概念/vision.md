# 画面线理解：20.异常规范之异常的概念

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day19-MongoDB集群以及日志、异常规范
- 源文件：03.阶段三 好客租房(生活服务)项目\day19-MongoDB集群以及日志、异常规范\20.异常规范之异常的概念【海量资源尽在 ubkz.com】.mp4
- 抽帧：9 帧 @ 00:11, 01:26, 01:36, 01:37, 02:45, 02:55, 03:55, 03:58, 03:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:14:22

1) 这一组画面整体在讲Java异常规范，包括异常概念、分类（Throwable、Error、Exception）及抛出与捕获机制。

2) 按时间顺序列出每张画面的要点：
画面1：
- 标题：4.1、异常概念
- 内容：异常是发生在程序执行过程中阻碍程序正常执行的错误事件，当一个程序出现错误时，可能的情况有如下3种：
  - 语法错误：代码的格式错了，某个字母输错了
  - 运行时错误：空指针异常，数组越界，除数为零等
  - 逻辑错误：运行结果与预期的结果不一样，这是一种很难调试的错误
- 图表：异常分类图（Throwable → Error → VirtualMachineError, AWTError；Throwable → Exception → IOException, RuntimeException）
画面2：
- 内容同画面1，无新增要点。
画面3：
- 图表更新：在“Exception”下新增“RuntimeException”节点，并标注“运行异常”。
画面4：
- 图表更新：在“RuntimeException”下新增多个异常类节点，包括“NullPointerException”、“IllegalArgumentException”、“ArrayIndexOutOfBoundsException”、“UnknownTypeException”等。
画面5：
- 内容同画面4，无新增要点。
画面6：
- 标题：4.2、异常规范
- 内容：1.【限制】Java 类库中定义的一类 RuntimeException 可以通过预检查进行规避，而不应该通过 catch 来处理，比如：IndexOutOfBoundsException，NullPointerException 等等。
  说明：无法通过预检查的异常除外，如在解析一个外部传来的字符形式数字时，通过 catch NumberFormatException 来实现。
画面7：
- 图表更新：鼠标悬停在“RuntimeException”下的“NullPointerException”节点上。
画面8：
- 标题：4.1、异常概念
- 内容：异常是发生在程序执行过程中阻碍程序正常执行的错误事件，当一个程序出现错误时，可能的情况有如下3种：
  - 语法错误：代码的格式错了，某个字母输错了
  - 运行时错误：空指针异常，数组越界，除数为零等
  - 逻辑错误：运行结果与预期的结果不一样，这是一种很难调试的错误
- 图表：异常分类图（Throwable → Error → VirtualMachineError, AWTError；Throwable → Exception → IOException, RuntimeException）
画面9：
- 内容同画面8，无新增要点。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
无。

4) PPT 标题、架构图/流程图的结构、表格数据：
- 标题：4.1、异常概念；4.2、异常规范
- 架构图/流程图结构：
  - Throwable
    ├── Error
    │   ├── VirtualMachineError
    │   │   ├── StackOverflowError
    │   │   └── OutOfMemoryError
    │   └── AWTError
    └── Exception
        ├── IOException
        │   ├── EOFException
        │   ├── FileNotFoundException
        │   ├── ArithmeticException
        │   ├── MissingResourceException
        │   ├── ClassNotFoundException
        │   ├── NullPointerException
        │   ├── IllegalArgumentException
        │   ├── ArrayIndexOutOfBoundsException
        │   └── UnknownTypeException
        └── RuntimeException
            └── 运行异常（注释）
- 表格数据：无。

5) 无。
