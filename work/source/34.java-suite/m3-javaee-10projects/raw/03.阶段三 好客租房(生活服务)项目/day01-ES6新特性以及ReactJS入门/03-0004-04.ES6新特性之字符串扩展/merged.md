# 04.ES6新特性之字符串扩展

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day01-ES6新特性以及ReactJS入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day01-ES6新特性以及ReactJS入门\04.ES6新特性之字符串扩展【海量资源尽在 ubkz.com】.mp4
- 时长 7分56秒（音频 476s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下ZipTor的扩展那么在ES6中呢为ZipTor这种数据类型呢做了一些扩展那么我们主要呢是讲两个方面第一个呢是它扩展了一些新的API那么让我们使用ZipTor呢使用的就更加的方便一些啊那么第二个方面呢就是它呢扩展了什么呢叫做ZipTor模板的这样的一个书写的格式那么究竟什么是ZipTor模板一会儿我们再说
[00:27] 那么我们先来看一下它增加的这么几个API那么最常用的增加呢有这三个一个呢叫includes那么显然呢就是在判断是否找到了参数这幅创也就是说在我们的某一个这幅创中是否包含了啊什么那么下面这个叫start位置那么它的表示是这幅创中是否也是否是以什么开头的那么end位置呢是以什么结尾的啊那这两个其实跟我们的加码中那个
[00:56] start位置和end位置类似好 那么下面我们来测试一下这两个测试一下这么新增的几个方法那么我们首先我们给它定义一个这么串叫什么呢叫hello我们的黑码hello黑码那么下面我们就判断一下判断什么呢打一个日志console.log打一个日志打什么呢先把stl打出来然后我们去判断这个钟
[01:25] 是否存在是否包含了什么是否包含了这个叫黑码是否包含了黑码呢我们来打印一下str.什么呢includes什么呢黑码它是否包含了黑码呢那么我们来打印一下那么我们同样是不是也可以去打印一下什么呢它是否包含了什么呢白码你看把这个黑码改成
[01:55] 白马我们来看一下刷新一下走那么我们可以看到你看hello黑马中包含了黑马后面是去那么hello黑马中是否包含了这个白马force所以我们可以看到当我们去判断某一个字符串中是否包含了包含了什么那么是不是就通过这个inclog就可以做一个判断
[02:21] OK这个的使用起来比较简单那么还有两个呢是start位置和end位置啊那么我们分别呢来做一个演示就是说下面呢我们来看啊这个字符串中是否是否什么呢不是包含了是否以以什么开头以这个hello以hello开头是不是以它开头呢我们来判断一下把这个改成
[02:51] 什么呢是不是点star的位置来一个hello那么我们是不是同样可以来看一下是不是以什么呢以这个黑码开头呢黑黑码开头呢我们来看一下刷新一下走你可以看到第三个hello这个黑码是否以hello开头呢true那么是否以他以这个黑码开头呢force那么有了这个star的位置那么就会有什么的n的位置我们来看一下
[03:23] 那么它是否以hello开头结束不是开头了结束结束结束好那么这个呢我们就要使用的是什么呢叫做endways点endways不是startwaysendways那么下面呢我们来判断是否以黑马结束不是开头了也是结束好那么导装来测试一下刷新走你可以看到
[03:52] 那么它是否以hello结束不是force那么是否以黑码结束ok好所以这是支付券所增加的三个API用起来是不是非常的方便ok好那么下面其实还讲了什么讲的是说支付券的模板那么支付券的模板是什么意思是这个意思那么之前我们在我们的解释中我们去写一个支付券的时候
[04:20] 比如说我们来一个str2的时候那么我们写一个字符串是不是可以这样去写那么abc123可以这样去写那么假设我们这个字符串中它有换行怎么办你这样行不行当然了这样的话是我们编译器为我们签了一个加号的联机服务对不对那么我们来看一下这样我看一下这样行不行回车咱们测一下这样把它拿掉
[04:50] 这个拿不掉这个不太好测不太好测那这样咱们在这里测咱们在这测在下面在这个位置是不是直接可以去输入好咱们来说一个Lint什么呢str2等于你看123然后呢abc这是没问题的对不对那么如果在这个里面我们想要回车怎么办你是回车不了对吧那么如果想要回车的话
[05:23] 哎他说已经定义了对吧那么来一个str3吧str3然后呢这个里面来一个回车对吧回车你看可以吗是不可以的对不对他是不能够啊去做一个这个回车的那么呃在es6中呢他提供了一个什么提供了一个这个字符号模板什么意思呢是这样的啊那么是通过一个这个符号啊这个符号
[05:50] 来去标记我们字幕创的一些这个模板也就是说只要在这两个符号之间的一些内容它都属于一个字幕创那我们来测试一下那么咱们就在这个位置做测试那么我来一个strstrstr几呢str4吧str4然后呢这个地方我们来这个符号注意
[06:20] 这个符号可不是那个单引号啊他是在我们的键盘上面的一左边的啊这个符号啊然后呢我们这个里面就可以输入你的内容ABC然后呢你可以回车按住shift加回车然后呢我们写123然后呢我们再写456再写789然后到这回车走那么我们可以看到哎他说这个已经啊已经定义了啊所以我们要重新来给他来一个
[06:50] STL5你可以看到那么这个STL5是不是就可以设置成功了那么我们是不是就可以把这个STL5给它打印出来看一下那么它的字幕创是不是就这样的一个字幕创那么也就是说我们通过这个符号通过这个符号那么就可以去定义任意的我们的这个字幕创
[07:12] 认识支付创这个我们在ES6中把它称之为叫做什么支付创的模板就是这个意思你看我这个安利写一个str等于hello黑马itcast那么我中间是不是有回车中间有个回车
[07:26] 那么在我们的控制台去输出的时候是不是就会这样的一个输出那么OK那么在这个两个这个符号之间呢都会被认为这个支付券的值可以做一个任意的一个换行哎呀OK这个呢就是我们所讲的在ES6中呢对支付券的一个扩展那么首先呢扩展了三个新的API然后呢提供了一个支付券模板啊这样的一种用法哎呀OK好那么关于支付券的扩展呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 ES6 中字符串扩展的 API，包括 includes、startsWith、endsWith 方法，并演示模板字符串的用法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 ES6 字符串扩展的介绍，列出 includes、startsWith、endsWith 方法，并给出实验代码示例。
画面 2: 在 HTML 文件中，定义了一个字符串变量 str 并输出。
画面 3: 在代码中，将变量 str 的值修改为 "hello heima"。
画面 4: 在代码中，调用 str.includes("heima") 方法并输出结果。
画面 5: 在浏览器控制台中，显示了语法错误：Assignment to constant variable。
画面 6: 在浏览器控制台中，显示了字符串包含检查的结果。
画面 7: 在代码中，调用 str.startsWith("hello") 方法并输出结果。
画面 8: 在代码中，调用 str.endsWith("hello") 方法并输出结果。
画面 9: 在代码中，调用 str.endsWith("heima") 方法并输出结果。
画面 10: 在代码中，定义了一个新的字符串变量 str2。
画面 11: 在代码中，将变量 str2 的值修改为 "abc" + "123"。
画面 12: 在浏览器控制台中，显示了语法错误：Identifier 'str' has already been declared。
画面 13: 展示了 ES6 模板字符串的用法，并给出示例代码。
画面 14: 展示了模板字符串的输出结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```javascript
console.log("a", "a");
```
```javascript
// Uncaught TypeError: Assignment to constant variable.
at [code].html:11
```
```javascript
// 实验一下：
<script>
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
console.log(str, "中是否包含了 baima", str.includes("baima"));
console.log(str, "中是否以 hello 开头", str.startsWith("hello"));
console.log(str, "中是否以 heima 开头", str.startsWith("heima"));
console.log(str, "中是否以 hello 结束", str.endsWith("hello"));
console.log(str, "中是否以 heima 结束", str.endsWith("heima"));
</script>
```
画面 2:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>ES6新特性的学习</title>
</head>
<body>
<script>
const str = "abc";
console.log(str);
</script>
</body>
</html>
```
画面 3:
```javascript
let str = "hello heima";
```
画面 4:
```javascript
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
```
画面 6:
```javascript
hello heima 中是否包含了 heima true
hello heima 中是否包含了 baima false
hello heima 中是否以 hello 开头 true
hello heima 中是否以 heima 开头 false
hello heima 中是否以 hello 结束 false
hello heima 中是否以 heima 结束 true
```
画面 7:
```javascript
let str = "hello heima";
console.log(str, "中是否包含了 heima", str.includes("heima"));
console.log(str, "中是否包含了 baima", str.includes("baima"));
console.log(str, "中是否以 hello 开头", str.startsWith("hello"));
console.log(str, "中是否以 heima 开头", str.startsWith("heima"));
console.log(str, "中是否以 hello 结束", str.endsWith("hello"));
console.log(str, "中是否以 heima 结束", str.endsWith("heima"));
```
画面 10:
```javascript
let str2 = "abc" + "123";
```
画面 13:
```javascript
// 半符模板
ES6中提供了 作为字符串模板标记，我们可以这么玩：
<script>
let str = `
hello
itheima
str
`;
console.log(str);
</script>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PPT 标题为“1.3、字符串扩展”，并列出 includes、startsWith、endsWith 方法。
画面 13: PPT 标题为“半符模板”，并给出模板字符串的示例。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

