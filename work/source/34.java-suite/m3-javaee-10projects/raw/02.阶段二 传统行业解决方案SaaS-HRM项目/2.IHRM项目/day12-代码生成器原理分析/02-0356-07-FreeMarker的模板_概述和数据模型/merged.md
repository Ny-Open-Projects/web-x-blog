# 07-FreeMarker的模板：概述和数据模型

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\07-FreeMarker的模板：概述和数据模型_【海量资源尽在 ubkz.com】.mp4
- 时长 8分12秒（音频 492s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 通过刚才两个入门的这个案例呢其实各位不难发现啊我们去玩FreeMarker其实Java代码呢它的步骤基本上都是差不多的要有配置对象要有加载器还要获取到它的磁幅创模板获取到它的模板那接下来构造数据接着处理模板其实就可以了没错吧所以呢这个步骤Java代码很简单我们Java代码关注的
[00:30] 难道真的是第一步第二步第三步或者是第五步处理吗显然不是基本上写法都差不多那么关注的Java代码部分是不是就是想方设法的构造数据这个数据才是模板里面第一重要的内容在我们的页目当中只需要通过数据库把数据查询出来其实就够了剩下的套路咱们用这一个套路12345几个步骤去套一下把代码写出来其实就可以了好了
[01:00] 入门案例咱们说的比较清晰了主要是Java代码让各位熟悉一把那接下来其实在FreeMarker里面Java代码是其次的那最难的就是模板的这个定义那这个模板定义它也有很多的细节问题需要各位关注那么接下来回到讲义一起来看一下FreeMarker它这个模板那首先呢需要跟各位简单的声明一下对于FreeMarker它的模板而言它
[01:30] 总共是包含这么五个部分这五个部分第一个数据模型数据模型是干嘛呢刚才我们知道了模板当中需要数据模型是不是最终给我填充数据所以这个数据模型其实是我们Java程序传入到模板当中的数据没错吧除了数据模型之外还有第二个部分就是文本这个文本其实在我们刚才的简单案例当中欢迎您
[02:00] 这不就是普通文本吗这个也能理解没错吧好了那接下来第三部分就是注释其实Fremark这个文本这个文件当中也能写注释那这个注释怎么写就这种格式就这种格式我们可以简单的一起拿过来看一下井好了监控号井杠杠杠杠这里面就可以随便写了这是一个注释
[02:35] 好了那接下来咱们在第一个模板当中写了一段注释我们执行一下这个程序看一下会有什么效果好了你会发现只输出了欢迎您传至博客那底下这个注释的内容是不是没有输出啊哎没错吧各位OK好了那接下来咱们继续来看前三个都比较简单都比较好理解好了我们继续往下看就是这个差值那这个差值呢其实通过的是两种符号一个是道路大框一个是警号大框
[03:06] 通过这种的形式写到模板上那就是把模板当中插入了一个站位符那这个站位符最终要通过数据的形式给我进行替换那比如说我们刚才写过井号大括号那这个就叫做插纸那当然除了井号大括号之外呢还支持DAO了大括号之外呢它还支持井号大括号这种写法所以它是两种写法都可以进行使用那对于现在来说我们一般用的是DAO了大括号用的比较多一些能理解吧
[03:35] OK好了这个我们简单的看了一下我们一会儿呢也会重点的去说一下这个内容那这个看过了之后还有第五部分内容第五部分内容呢叫做FTL指令它其实是FreeMarker的一些指令这个指令呢和HTML标签其实相似只不过是在标签的前面加了一个警号预区分它呢也不会输出那这个指令呢其实是可以通过FTL这些指令帮助我们在模板当中进行一些逻辑判断进行一些循环等等的
[04:04] 很好用的一些功能那这回我们都会一个一个跟各位简单的来介绍所以对于FreeMark模板一共有五个部分前三个部分比较好理解数据Java代码传递过去的文本就输出的一些不会发生变化的内容好了注释注释这个比较怪各位简单的看一下就可以了当然了还有差值那对于差值来说其实说白了就是两种符号一种dollar大括号dollar大括号是用来显示数据的
[04:34] 好了警号大括号是用来写FTL指令的那这FTL指令呢有很多就是在前面加警号其实就可以了那各位如果呢在FreeMarker当中你碰到了这些碰到了这些碰到了这些什么警号大括号到了大括号希望各位能知道它是什么含义好了这个FreeMarker这几个组成部分呢和各位简单的做了一个介绍那接下来呢我们就继续往下看这五部分里面的第一部分数据模型
[05:04] 那我们刚才通过案例你会发现啊只要说呢把一个数据存入到map集合里面它是不是这边就能够通过user name来进行获取啊那接着我想说的是我想说的是如果你这里面要传递一对象那我这边又该咋获取呢那如果我这里面是嵌套的数据结构那又该如何去做呢那要想去理解这个代码的写法
[05:31] 需要看一下它数据模型它的结构所以我们继续往下看FreeMarker其实并不关注数据是如何获取的或者是如何计算的这个计算和获取的过程Java代码去做FreeMarker真正关心的其实数据它究竟是什么没错吧关注的是模板当中如何去使用这些数据如何去使用这些数据这些数据首先称之为Data Model数据模型
[06:01] 那这个数据模型的结构在这边有一张图形跟各位罗列出来了首先呢有一个跟节点那跟节点底下比如说这边有一个例子叫做user bigadj好了这边还有last什么product好了那接着跟节点的内容是什么跟节点内容我们直接这样存放map.put一个基本属性那这个基本属性其实就存放到了跟节点下跟节点下
[06:29] 那接下来如果说你存递的是一个比如说如果传递的是一个用户对象user对象那这个user对象那它就理解为根节点的内容那user对象里面如果说有其他的属性比如说有userrl属性有username属性那其实就代表的是user根节点下对象里面的属性这个应该也能理解吧那接下来我们关注的是我们关注的是map集合.put
[07:02] 它存放到根节点下那根节点下获取如何获取注意我写到模板这边吧获取数据首先用的符号dollar大括号那dollar大括号里面获取到节点根节点下的数据那如果是对象或者是一个符合结构的数据那你就继续打点继续打点直到获取到你想要的属性为止
[07:45] 这个能理解吧好了这个语法和各位说过了之后那如果是我想要获取URL那各位应该就比较清晰了根据点下叫做lasted product那继续打点是不是URL啊那如果是我指向哪个user那是不是就直接user就能够获取到了没错吧好了和各位讲这个数据模型主要是为了咱们存放数据获取数据的时候方便一些

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 FreeMarker 模板引擎的基本用法，包括模板文件创建、数据模型准备、模板处理及输出。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 Java 代码，演示如何创建 Configuration、设置模板加载器、加载模板、准备数据模型并处理模板输出。
画面 2: PPT 展示 FreeMarker 模板的组成，包括数据模型、文本、注释、插值和 FTL 指令。
画面 3: 展示模板文件 template01.ftl，内容为“欢迎您，${username}”。
画面 4: 展示 PPT 页面，同时显示了多个窗口，包括 PDF 阅读器、IDEA 项目结构和代码编辑器。
画面 5: 展示模板文件 template01.ftl，内容为“欢迎您，${username}”。
画面 6: PPT 展示 FreeMarker 模板的组成，包括数据模型、文本、注释、插值和 FTL 指令。
画面 7: 展示模板文件 template01.ftl，内容为“欢迎您，${username}”。
画面 8: 展示 PPT 页面，同时显示了多个窗口，包括 PDF 阅读器、IDEA 项目结构和代码编辑器。
画面 9: PPT 展示 FreeMarker 的数据模型，以树状结构展示 root、user 和 latestProduct。
画面 10: PPT 展示 FreeMarker 模板的常用标签，重点讲解 $(...) 插值语法。
画面 11: PPT 展示 FreeMarker 模板的常用标签，重点讲解 $(...) 插值语法。
画面 12: PPT 展示 FreeMarker 模板的常用标签，重点讲解 $(...) 插值语法。
画面 13: 展示 Java 代码，演示如何创建 FileTemplateLoader、获取模板、准备数据模型并处理模板输出。
画面 14: PPT 展示 FreeMarker 的数据模型，以树状结构展示 root、user 和 latestProduct。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class FreeMarkerTest02 {
    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载模板
        String templateString = "欢迎您，${username}";
        Template template = new Template( name: "name1", new StringReader(templateString), cfg);
        //4.准备数据模型
        Map<String, Object> dataModel = new HashMap<>();
        dataModel.put("username", "张三");
        //5.处理模板
        template.process(dataModel, new PrintWriter(System.out));
    }
}
```

画面 5:
```java
欢迎您，${username}
```

画面 13:
```java
//2.设置模板加载器
cfg.setTemplateLoader(new FileTemplateLoader(new File(pathname: "templates")));
//3.加载模板
Template template = cfg.getTemplate( name: "template01.ftl");
//4.准备数据模型
Map<String, Object> dataModel = new HashMap<>();
//5.处理模板
//参数一：数据模型（文件输出），printWriter（控制台输出）
//参数二：writer (FileWriter (文件输出), PrintWriter (控制台输出))
//template_process(dataModel, new FileWriter(new File("C:/Users/ThinkPad/Desktop/123/test1.txt")));
template_process(dataModel, new PrintWriter(System.out));
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 2:
标题：2.4 Freemarker模板
2.4.1 概述
FreeMarker模板文件主要有5个部分组成：
1. 数据模型：模板能用的所有数据
2. 文本，直接输出的部分
3. 注释，即#--->格式的部分，不会输出
4. 插值（Interpolation）：即${}或者#(...)格式的部分，将使用数据模型中的部分替代输出
5. FTL指令：FreeMarker指令，和HTML标记类似，名字前加#予以区分，不会输出。

画面 6:
标题：2.4.1 概述
FreeMarker模板文件主要有5个部分组成：
1. 数据模型：模板能用的所有数据
2. 文本，直接输出的部分
3. 注释，即#--->格式的部分，不会输出
4. 插值（Interpolation）：即${}或者#(...)格式的部分，将使用数据模型中的部分替代输出
5. FTL指令：FreeMarker指令，和HTML标记类似，名字前加#予以区分，不会输出。

画面 9:
标题：2.4.2 数据模型
FreeMarker（还有模板开发者）并不关心数据是如何计算的，FreeMarker 只是知道真实的数据是什么。模板能用的所有数据被包装成 data-model 数据模型

内容：
(root)
+ user = "Big Joe"
+ latestProduct
++ url = "products/greenmouse.html"
++ name = "green mouse"

画面 10:
标题：2.4.3 模板的常用标签
在FreeMarker模板中可以包括下面几个特定部分：
1. ${...}：称为interpolations，FreeMarker会在输出时用实际值进行替代。
o ${name}可以取得root中key为name的value，
o ${person.name}可以取得成员变量为person的name属性

画面 11:
标题：2.4.3 模板的常用标签
在FreeMarker模板中可以包括下面几个特定部分：
1. ${...}：称为interpolations，FreeMarker会在输出时用实际值进行替代。
o ${name}可以取得root中key为name的value，
o ${person.name}可以取得成员变量为person的name属性

画面 12:
标题：2.4.3 模板的常用标签
在FreeMarker模板中可以包括下面几个特定部分：
1. ${...}：称为interpolations，FreeMarker会在输出时用实际值进行替代。
o ${name}可以取得root中key为name的value，
o ${person.name}可以取得成员变量为person的name属性

画面 14:
标题：2.4.2 数据模型
FreeMarker（还有模板开发者）并不关心数据是如何计算的，FreeMarker 只是知道真实的数据是什么。模板能用的所有数据被包装成 data-model 数据模型

内容：
(root)
+ user = "Big Joe"
+ latestProduct
++ url = "products/greenmouse.html"
++ name = "green mouse"

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

