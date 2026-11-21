# 08-FreeMarker的模板：if指令和list指令

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\08-FreeMarker的模板：if指令和list指令_【海量资源尽在 ubkz.com】.mp4
- 时长 11分15秒（音频 676s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的和各位看了一下FreeMarker模板当中的数据模型那这个数据模型呢其实比较简单那只要各位记住那我们在Java代码当中呢通过Map这种形式进行数据传值Map这种形式进行数据模型的传值那你Map Put的这个数据它其实就存放到了root节点下OK那接下来呢
[00:29] 这边和各位补充了一个就是我们模板的一些常见的一些标签在模板当中它支持的标签其实一共有这么几种类型第一种类型就是W大括号W大括号是叫做差值它其实它主要做的就是把数据显示到模型上进行一个数据替换的这么一个过程好了还有一个就是井号尖夸号井号这个尖夸号井号指的是TFTL标记
[00:56] 那这个FTL标记它是干嘛的呢其实它是可以写一些FreeMarker的一些指令那这些指令可以进行一个FreeMarker页面上的一个编程那可以比如说呢进行判断进行循环还有进行一些其他的一些操作等等那还有一个就是监控号at那这个监控at呢其实干嘛的它是定义红
[01:21] 那这个红它的主要目的呢其实就是可以定义一些我们自己的标签当然这个红来说呢我们一般用的也不多它也不是我们今天学习的重点那还有一个就是注视注视就是尖夸号井号刚刚那对于我们来说呢常用模板当中的常用标签呢就两个dollar大括号那这个dollar大括号里面这边有一个例子也跟各位说一下就是dollar name这个dollar大括号name其实指的是root下面有一个节点叫name指的是root节点下的name属性
[01:51] 那还有一个person.name那这个person.name啥意思指的是root节点下一个叫做person的一个对象那这个对象当中有一个name属性能理解吧好了接下来就是这个监控号警号那这个监控号警号里面可以写一些指令那这些指令其实组成了组成了VMarker模板的一些功能它的一些逻辑判断的一些功能那我们接下来关注的就是
[02:21] 尖块井号它后面可以跟的指令究竟有什么首先第一个指令叫做if指令其实这个if指令见名之意你就知道是干嘛了它是用来做分支逻辑判断的那接下来我们来研究一下这个if指令究竟如何去做那其实各位会发现这个指令写起来跟渣滑代码还是有点像的没错吧好了那接着我们打开模板
[02:48] 抱歉打开这边的模板我们就开始使用if指令一起来玩一下OK好了在这边来一株式我们现在玩的是if标签if指令指令吧OK那对这个if指令如何去写呢其实不难先括号井号if好了这if里面呢这边可以写我们的条件条件那好了接下来那有的朋友说他有很多的渣滑习惯
[03:21] 那有的朋友说写完if之后这边立马就来一个else那这个不符合这个这个其实不太符合Vimarker标签里面的语法那它这个语法是这样的if里面写条件那接着如果有else继续写井号else ifelse这边提示一下else if那这边呢继续写条件条件
[03:55] 好了那接下来最后不是有的朋友说还喜欢写一个叫做else吗那好了接着井号else好了它是这种一个条件它是这种一个写法那如果满足第一个里面写第一个的内容那如果满足第二个写第二个内容如果满足第三个写第三个内容这个是它的语法这个应该能看懂吧OK那好了接着我们可以写一个简单的案例一起来看效果
[04:20] 那这边呢一般来说呢我们这个条件那这个条件要进行判断那这个判断呢有可能需要你从Java代码进行传递那比如说我可以传递一个数据比如说传递一个数据叫做flag这个flag呢我可以传递的是true或者false当然我可以传递1或者传递2都可以比如说我就传递一个1好那这边我就可以做判断那做判断在这种警号监控
[04:48] 尖块井号的这种判断体当中要想获取数据不就不用写什么道乐大括号了直接写属性名你要用哪个值你就用它就可以了我们这样一来放到root节点下那它的名字叫做flag所以我这边直接flask如果flag等于1注意我这边可以写我就让它去输出比如说呢传入数据等于1好了如果说你这边flag这
[05:23] 等于2好了我这边传入数据等于2好了那这边else传入数据等于其他OK那这个if指令我们写好了之后接下来我们一起来看一下如果传1就要显示第一句话如果传2第二句话如果传其他就是其他OK一起来试一下好了现在传的是1来走各位看空台假印传入数据是1没有问题那接下来
[05:54] 来一二走传输数据是二没有问题接下来我来一三走会发现传输数据其他好了那这个if指令呢我们看过了其实需要各位要了解的就是第一它这个语法ifelse ifelse最后-if结尾那还有就是里面进行判断的一个逻辑呢直接用等号其实就可以了不用写两个等这个跟Java代码有点区别
[06:30] OK好了EF这个我们看过了之后接下来呢其实它还有一些指令比如说呢接下来我们来的是叫做list指令好了那这个list指令它的主要目的是干嘛的就是循环迭代好了那接下来那接下来我们来看一下如何去玩这个list指令那首先呢我往里面存点数据比如说呢我这边可以往里面存一数据存一list集合进去因为list指令其实就是对某一个数组进行一个循环迭代
[07:06] 那这个呢我写一个stringstring呢叫做就叫list了等于new一个relist好了这个里面呢给他存一点点数据进去list.add第一个呢叫做星期一好了星期二好了这边星期三好了星期四我就会写四个了可以吧ok接着传入到数据模型当中点put给他起一个名字ok
[07:47] 好了接着把list存进去那这样一来其实我的root节点下已经有了个叫做vix里面的这么一个数组这个数组里面四条数据那接下来我们要在模板当中循环迭代获取到里面的每一个元素给它打印出来那接着这里面我们应该如何去循环迭代获取那其实比较简单OK它的语法是这样的首先呢警号list正因为我其实声明了这么一个标签接着我把b和标签也写好
[08:15] 那list的中间呢它支持的语法OK我写到上面它支持语法数组数组名称接着s接着写我们的对象名也就是说你把数组当中的每一个元素给它起了一个叫做别名OK那我们可以一起来看一下数据模型里面有一个wix那wix呢就是我们第一个wix as比如说呢我对其中的每一个元素起一个名字叫做
[08:51] ABC那接着我要获取这个每一个元素那我怎么做注意这回不是在标签题里面不是在锦号标签题里面了那我们怎么获取dollar大括号那ABC别名直接就能够获取到那这样一来它其实就相当于我循环数组里面1234这么几条数据那循环的过程当中对每一个数据起一个名字叫ABC接着把它显示出来OK那我们一起执行一下看一下效果
[09:24] 好了各位来看现在1234都已经给我显示出来了没错吧好了这个就是跟各位来聊的list循环那其实这个list循环里面呢它也可以结合break等等的这些语法来做结合break的这些语法来做那比如说呢在这边咱们讲义上也有一些简单的案例比如说那比如说呢这边呢它给我传递了一个例子数组那例数组SX那这个代表什么含义其实代表的是我有一个数组那数组给它起一个名字叫X
[09:55] 那底下$x进行循环输出那如果碰到的等于星期四那我break就不再循环了那当然了这个里面除了这个break之外呢它还有一些内置的一些变量那内置的变量比如说item下滑线indexitem下滑线has next那这两个一个代表的是当前变量的所以一个代表是否存在下一个对象
[10:21] 那这个atom注意这个atom代表的是什么这个atom代表的是你当前的这个差你起的是什么名字你就以差下滑线index进行替换即可那比如说比如说我这边代码当中想要去获取索引那索引如何去获取ABC下滑线index那要使在我们的文本当中进行替换的话dollar大括号别忘了等于OK那好了我们再来看一下
[10:53] 走各位01234索引是不是也能够获取到啊那当然了你这边也可以做判断如果说当前这个索引等于1你不REQ不执行其实哎就可以了OK好了这个就是跟各位来聊的前两个指令第一个IF指令第二个是我们的LIST指令OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 FreeMarker 模板引擎的常用标签和指令，通过 Java 代码演示如何加载模板、传入数据模型并输出结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：PPT页面，标题“2.4.3 模板的常用标签”，展示 FreeMarker 模板数据结构示例：(root) + user = "Big Joe" + latestProduct + url = "products/greenmouse.html" + name = "green mouse"，并列出标签类型：$(...)、<#if>、<#else>、<#assign>。
画面2：PPT页面，标题“2.4.3 模板的常用标签”，内容与画面1相同，顶部有“黑马程序员”Logo和联系方式。
画面3：PPT页面，标题“2.4.3 模板的常用标签”，内容与画面1相同，下方开始出现“2.4.4 模板的常用指令”标题。
画面4：IDEA 编辑器，打开 `template01.ftl` 文件，光标在第一行，内容为：欢迎，${username}。
画面5：IDEA 编辑器，`template01.ftl` 文件中添加了条件判断标签：<#if flag==1>...<#else>...</#if>。
画面6：IDEA 编辑器，`template01.ftl` 文件中，光标在 `<#if flag==1>` 行，显示了条件判断标签。
画面7：IDEA 编辑器，显示 `FreeMarkerTest01.java` 文件，代码为：
```java
public class FreeMarkerTest01 {
    @Test
    public void test01() throws Exception {
        //1.创建FreeMarker配置，有模板存入缓存中
        Configuration cfg = new Configuration();
        //2.指定模板路径，将模板存入缓存中
        FileTemplateLoader ftl = new FileTemplateLoader(new File(pathname: "templates"));
        cfg.setTemplateLoader(ftl);
        //3.获取模板
        Template template = cfg.getTemplate(name: "template01.ftl");
        //4.创建数据模型
        Map<String, Object> dataModel = new HashMap<>();
        //user对象
        dataModel.put("username", "传智播客");
        dataModel.put("flag", 3);
        //文件输出
        //处理模型
        //参数一：数据模型
        //参数二：writer（fileWriter（文件输出）.printWriter（控制台输出））
        //template.process(dataModel,new FileWriter(new File("C:\\Users\\ThinkPad\\Desktop\\zhrm\\day12\\test1.txt")));
        template.process(dataModel, new PrintWriter(System.out));
    }
}
```
画面8：IDEA 编辑器，`template01.ftl` 文件中，光标在 `<#if flag==1>` 行，显示了条件判断标签。
画面9：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `list<String> list` 行，显示了创建列表的代码。
画面10：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `list.add("星期一");` 行，显示了添加列表元素的代码。
画面11：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `dataModel.put("weeks", list);` 行，显示了将列表放入数据模型的代码。
画面12：IDEA 编辑器，`FreeMarkerTest01.java` 文件中，光标在 `Configuration cfg = new Configuration();` 行，显示了创建配置对象的代码。
画面13：Word 文档，内容为：
1. 动态页面：
   替换 jsp
2. 静态化：
3. 代码生成器
画面14：IDEA 编辑器，`template01.ftl` 文件中，光标在 `<#list weeks as abc>` 行，显示了遍历列表的标签。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7：
```java
public class FreeMarkerTest01 {
    @Test
    public void test01() throws Exception {
        //1.创建FreeMarker配置，有模板存入缓存中
        Configuration cfg = new Configuration();
        //2.指定模板路径，将模板存入缓存中
        FileTemplateLoader ftl = new FileTemplateLoader(new File(pathname: "templates"));
        cfg.setTemplateLoader(ftl);
        //3.获取模板
        Template template = cfg.getTemplate(name: "template01.ftl");
        //4.创建数据模型
        Map<String, Object> dataModel = new HashMap<>();
        //user对象
        dataModel.put("username", "传智播客");
        dataModel.put("flag", 3);
        //文件输出
        //处理模型
        //参数一：数据模型
        //参数二：writer（fileWriter（文件输出）.printWriter（控制台输出））
        //template.process(dataModel,new FileWriter(new File("C:\\Users\\ThinkPad\\Desktop\\zhrm\\day12\\test1.txt")));
        template.process(dataModel, new PrintWriter(System.out));
    }
}
```

画面9：
```java
list<String> list
```

画面10：
```java
list.add("星期一");
```

画面11：
```java
dataModel.put("weeks", list);
```

画面12：
```java
Configuration cfg = new Configuration();
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、2、3：PPT标题“2.4.3 模板的常用标签”，内容包括：
- 数据结构示例：(root) + user = "Big Joe" + latestProduct + url = "products/greenmouse.html" + name = "green mouse"
- 标签类型：
  1. $(...)：称为interpolations，FreeMarker会在输出时用实际值进行替代。
     - $(name)可以取得root中key为name的value。
     - $(person.name)可以取得成员变量为person的name属性。
  2. <#if>：FTL标记（FreeMarker模板语言标记）：类似于HTML标记，为了与HTML标记区分。
  3. <#else>：宏，自定义标签。
  4. 注释：包含在<#-- 和 -->之间。

画面13：Word 文档，内容为：
1. 动态页面：
   替换 jsp
2. 静态化：
3. 代码生成器

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

