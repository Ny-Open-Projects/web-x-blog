# 09-FreeMarker的模板：include和assign指令

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\09-FreeMarker的模板：include和assign指令_【海量资源尽在 ubkz.com】.mp4
- 时长 7分30秒（音频 450s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那FreeMarker除了刚才说过的这if和list指令之外还有一些其他的指令在我们的讲义上也跟各位简单的说过好了还有一个include指令一个一个assigns指令其实除了这些指令还有很多对于那些不是常用的这些指令我们用到的时候再说OK我们接着再来看include而这个include什么意思它其实就是在一个模板当中包含另一个模板就是模板包含include
[00:36] 好了那接着来我们来看一下那对于这个include指令它是多个模板之间的一个包含关系所以这边呢我再去创建一个模板这个模板比如说tmplate我叫做02.ftl好了这个里面呢我就开始就是写一句话吧就是第二个模板好了第二个模板我想试一下能不能够在第二个模板也去获取到一些数据比如说呢$user name
[01:03] OK那我要做的事情要在第一个模板包含第二个模板那怎么做比较简单尖号 景号include那注意这个include的语法那中间只需要配置一下你第二个模板它代表的地址路径其实就可以了那这边呢它其实也能接收相对路径的这么一种写法相对于01的路径02那我们写相对路径即可template02.ftl那同时它也能够自动的帮我提示出来
[01:34] OK那这样一来呢其实我们两个模板就已经写好了注意这边那这个模板包含的时候这个双引号一定要写不写就会包错了OK那好了这样一来呢我其实已经把当前的这两个模板都体现在01当中了那我们这边再去执行一下看一下是否有01跟02的所有数据走好了你会发现第一个模板的数据有第二个模板是不是也同一都出来了那这样一来是不是就可以通过一个模板通过include
[02:04] 其他的一些公共的模板也包含过来啊OK好了这个模板包含不多说了那除了这个模板包含之外呢还有一个标签这个标签呢叫做assign指令好了这个assign指令它究竟在做什么我需要跟各位简单的做一个说明assign指令它主要目的呢其实就是在ftl模板中定义数据存入到我们的存入到root
[02:39] 节点下也就是说呢有可能啊你在这个模板当中呢你可能要操作很多个字符创要写很多次的一些内容那操作这些内容的时候它可以支持你assign的这种形式自定义一些数据存到我们的数据模型里能理解吧其实就相当于你在模型当中你在这个模板当中往模型当中存点值OK那看一下
[03:06] 如何去使用这个 assign 指令呢一般来说呢我个人习惯写到最上边因为它其实就相当于我定义一个当前页面可以使用的一些数据那比如说呢我们可以定义一些警号 assign定义一个数据那这个语法是什么样的其实这个语法比较简单好了左边你可以定义你当前要用到的这个变量名比如说有一个变量名等于 name那后面就是这个变量它取的它的值了
[03:39] 那这个值比如说呢就叫做张三抱歉这回抱歉三指令那这样一来呢其实就相当于我定义了一个数据这个数据呢它叫做NIM它放到了我们的root节点下它的值叫做张三那好了我们就可以获取一下咱们自己定义的内容而这边直接NIM拿到其实就可以了OK我们一起再来试一下好了这边报了一个错误啊这个错误应该在这儿
[04:15] 我这个Name应该是一个说明号扩起来因为是一个词词OK再来那各位你会发现我现在呢真真正正的定义了一个叫做Name的这么一个数据这个数据叫做张三那我如果在其他地方用直接到了大括号拿到它的名称其实就可以了OK这个就是刚才跟各位介绍的这些指令
[04:43] 那我们常用的指令呢一般来说有if指令有list指令有include指令还有这个assign指令那有朋友说这个assign指令一般什么地方用比如说呢其实定一些公共的一些信息比如说呢你要用时间那这个时间其实可以这边直接触手画出来接着在这个解点下直接用属性名称去获取就省了用很多的代码去编写了OK那好了这些指令我们都看过了之后那在free marker当中呢还有一些内置的一些函数
[05:13] 这个内置的函数这些呢比较多比较多这边呢也不会跟各位一个一个的都去讲了其实这些指令呢这些函数呢只需要跟各位说一下如何去用其实就可以了比如说呢我举一个例子啊比如说这边有一个问号cup first那我就以它为例来看一下如何去用这个指令那就去这些内置的一些函数好了这些我就打它都注视起来了都注视起来好了我写到最下边
[05:49] 那对于这个函数而言呢它如何去用呢其实很简单直接$比如说我们可以显示user name那接着问号来一问号后面说明我要用函数了那这个函数我要用上比如说是lowercase字符串的小写形式lowercaseOK那这样一来我就已经写好了函数就开始使用了那接下来我在我的Java代码当中传递user name的时候我可以传递一个比如说呢
[06:20] 注意我这边有大写字母张三吧有大乙字母那好了接着我执行一下看一下这个函数究竟是否诶皮皮生效了你会发现是不是已经把当前的这个字符串给我转化成小写的呀所以对于它的内置函数使用起来很简单直接问号函数名即可OK当然了这个remarker呢其实还有很多的内容这些内容呢其实
[06:47] 由于我们也不常用所以一些其他内容呢就没跟各位再去往细的去讲那如果各位有兴趣的话呢其实可以关注一下今天给各位下发的这个资料这个里面有Fremark它的一个使用手册里面详细的记载了这个Fremark应该如何去使用当然里面有模板等等等等还有它的内置函数所有内容都有OK那其实呢通过我们刚才的讲解这个Fremark大家会发现我们使用起来不难重点关注的是模型
[07:17] 模板加数据模型那数据模型我们自己查询模板就有点麻烦了要借助它的指令借助它的函数借助它的一些标签去获取数据OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

