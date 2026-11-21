# 画面线理解：09-FreeMarker的模板：include和assign指令

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\09-FreeMarker的模板：include和assign指令_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:25, 00:50, 01:49, 02:14, 03:20, 04:10, 04:23, 05:11, 06:08, 06:37, 06:55, 07:05, 07:13
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 16:47:16

1) 这一组画面整体在讲什么（一句话）：
演示 FreeMarker 模板引擎的基本语法、内置函数和在 Java 中的应用，包括条件判断、列表遍历、包含指令和变量赋值等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 FreeMarker 模板中用于列表遍历的语法：`<#list ["星期一", "星期二", ...] as x> ... </#list>`。
- 介绍了 `include` 指令的语法格式：`<#include filename [options]></#include>`。
- 介绍了 `assign` 指令用于创建或替换顶层变量：`<#assign name = zhangsan />`。
- 介绍了内置函数，如 `?cap_first`、`?lower_case`、`?upper_case`、`?trim`、`?substring`、`?length`、`?size`、`?int`。

画面 2：
- 展示了 FreeMarker 模板中 `if` 条件判断语法：`<#if flag>...<#else if flag2>...<#else>...<#endif>`。
- 展示了 `list` 指令用于遍历列表：`<#list weeks as abc>...<#list>`。
- 展示了模板中引用变量：`$abc_index`。

画面 3：
- 展示了项目结构，包含 `templates` 目录下的 `template01.ftl` 和 `template02.ftl` 文件。

画面 4：
- 展示了 Java 代码中创建 FreeMarker 模板对象并设置数据模型：`Template template = cfg.getTemplate("template01.ftl");`。
- 展示了数据模型的设置：`dataModel.put("username", "张三"); dataModel.put("flag", 3);`。
- 展示了列表数据的设置：`List<String> list = new ArrayList<>(); list.add("星期一"); ... dataModel.put("weeks", list);`。
- 展示了文件输出：`template.process(dataModel, new PrintWriter(System.out));`。

画面 5：
- 与画面 1 内容相同，再次展示 FreeMarker 模板语法和指令。

画面 6：
- 展示了模板中 `assign` 指令用于定义变量：`<#assign username = "zhangsan">`。
- 展示了 `include` 指令用于包含其他模板：`<#include "template02.ftl">`。
- 展示了 HTML 标签的列表：`<button>`, `<br>`, `<input>`, ...。

画面 7：
- 展示了 FreeMarker 测试失败的错误信息，提示 `Process finished with exit code -1`。

画面 8：
- 展示了 Java 代码中创建 FreeMarker 配置对象：`Configuration cfg = new Configuration();`。

画面 9：
- 与画面 1 内容相同，再次展示 FreeMarker 内置函数。

画面 10：
- 展示了模板中 `include` 指令用于包含其他模板：`<#include "template02.ftl">`。
- 展示了模板中引用变量：`$username`。
- 展示了语法错误提示：`identifier expected`。

画面 11：
- 展示了 FreeMarker 测试通过的输出结果：`zhangsan`。
- 展示了 Java 代码中调用模板：`template.process(dataModel, new PrintWriter(System.out));`。

画面 12：
- 展示了项目目录结构，包含 `day1` 到 `day12` 文件夹。
- 展示了 `day11` 文件夹下的 `suss-hrm-11rm.xlsx` 文件。

画面 13：
- 展示了课程目录结构，包含“第一部分 程序开发基础”、“第二部分 模板引擎”、“第三部分 数据模型”等章节。

画面 14：
- 展示了课程 PPT 的第 2 页，标题为“2.1 什么是 FreeMarker”。
- 内容描述：FreeMarker 是一款模板引擎，用于生成输出文本，是为 Java 程序员提供的一款应用程序。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```freemarker
<#list ["星期一", "星期二", "星期三", "星期四", "星期五"] as x>
${x.index + 1}.${x} <#if x_has_next>,</#if>
</#list>
```
```freemarker
<#include filename [options]></#include>
```
```freemarker
<#assign name = zhangsan />
```

画面 2：
```freemarker
<#if flag>
传入数据-1
<#else if flag2>
传入数据-2
<#else>
传入数据-其他
</#if>
```
```freemarker
<#list weeks as abc>
${abc_index} = ${abc}
</#list>
```

画面 4：
```java
Template template = cfg.getTemplate("template01.ftl");
Map<String, Object> dataModel = new HashMap<>();
dataModel.put("username", "张三");
dataModel.put("flag", 3);
List<String> list = new ArrayList<>();
list.add("星期一");
list.add("星期二");
list.add("星期三");
list.add("星期四");
list.add("星期五");
dataModel.put("weeks", list);
```
```java
template.process(dataModel, new PrintWriter(System.out));
```

画面 6：
```freemarker
<#assign username = "zhangsan">
<#include "template02.ftl">
```

画面 8：
```java
Configuration cfg = new Configuration();
```

画面 10：
```freemarker
<#include "template02.ftl">
${username}
```

画面 14：
```text
FreeMarker 是一款模板引擎：一种基于模板的、用来生成输出文本（任何来自于 HTML 格式的文本）来自动生 成源代码的通用工具。它是为 Java 程序员提供 的一个开发包或者说是类库。它不是面向最终用户，而是为程序员提供 的可以嵌入他们开发产品的一款应用程序。
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13：
- 标题：课程目录结构。
- 内容：
  - 第一部分 程序开发基础
    - 1.1 创建项目
    - 1.2 创建模板模型
    - 1.3 获取模板
    - 1.4 合并模板和数据模型
    - 1.5 将代码放在一起
  - 第二部分 模板引擎
    - 2.1 基本内容
    - 2.2 容器
    - 2.3 方法
  - 第三部分 数据模型
    - 3.1 基本内容
    - 3.2 容器
    - 3.3 方法

画面 14：
- 标题：2.1 什么是 FreeMarker
- 内容：FreeMarker 是一款模板引擎：一种基于模板的、用来生成输出文本（任何来自于 HTML 格式的文本）来自动生 成源代码的通用工具。它是为 Java 程序员提供 的一个开发包或者说是类库。它不是面向最终用户，而是为程序员提供 的可以嵌入他们开发产品的一款应用程序。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
