# 02-DataURL：概述

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\02-DataURL：概述_【海量资源尽在 ubkz.com】.mp4
- 时长 5分25秒（音频 326s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 对于Data URL其实不管是什么既然包含URL这三个字母那它其实就应该能在我们的浏览器上访问是不是才对呀那在我今天的资料当中其实也给各位准备了这么一个Data URL格式的这么一个数据好了在资源这边我们打开它有一个叫做Data URL.TIT
[00:27] 好了一会儿呢我们再去总结这个Data UL究竟它是由什么构成的我们先来看一下对于这玩意儿它能不能够通过浏览器打开那其实我们直观的发现它其实就是一个字符串没错吧那这个字符串究竟代表什么含义来Ctrl C复制过来在我们的浏览器上打开来看一下它究竟是什么来走各位会发现确确实实能够打开并且显示的是我们传之博客的一个logo的这么一张图片
[00:57] 没错吧那接下来呢我们就想跟各位说了那Data UL那它怎么就能变成了由一串字符串它就能够在浏览器上访问并且能够展示出效果那接下来我们就从头到尾开始去聊Data UL那首先呢所谓Data UL其实它指的就是具有数据的一个UIL地址那它是在这么一套规范当中提出来的
[01:24] 它的目的其实就是用于存储一些比较小的数据OK那并且呢这个Data UI可以在网页当中直接嵌入而不需要外部文件的一个载入了好了那这个呢其实看起来它的概念还不太直观咱们只有把这个Data UI全部都讲过了之后再回过头来说最后这一句话那其实各位就比较清晰了
[01:53] 好了我们到这儿只需要知道Data UL它是UIL的一部分那它呢是一种巧妙的形式可以把数据嵌入到一个字符串当中并且可以能够打开就够了那接下来呢我们就来看一下对于一个Data UL来说它究竟是由什么构成的那其实看我这一句话呢它后面部分看的还不太清晰那么回到最开头各位这个就比较清晰了为什么叫Data UL不叫别的呢是不是它是以Data
[02:22] 抱歉拖到最前面是不是它是以Data开头的那后面加一冒号接着中间部分那这个是什么呢其实这个就应可以把它理解成我们一个文件的Meme类型Meme类型那后面呢有一个Base64那Base64咱们学Java的都不陌生其实它指的是一种编码的格式没错吧那前面是用来对Data进行说明那后面是我真正的数据部分
[02:51] 也就是说前面部分是在对数据它的一个格式做说明后面才是我的数据部分那所以我们回到讲义对于一个Data UI来说它的完整的写法Data 冒号后面我们的MemoryType好了后面再加上Base64接着最后才是数据当然了这边有一个MedianType和我们这个Base64这两玩意儿其实是可选的可选的当然了如果说对于一些
[03:20] 文件来说比如说图片还是对于图片来说这两个还是要需要添加的因为只有拿上这些memo type浏览器才会把这个字幕串转化成对应的图片类型给我们输出出来OK好了那这个我们看过了之后接下来就是说对于这个meta type来说的或者就我们memo type有很多比如说呢可以是一个html的一个片段也可以是我们的一个png的一张图当然了也可以是其他类型的图片好了这个呢咱们都学习Java的这个呢各位应该都比较清晰了
[03:49] 好了那接下来呢底下呢其实给各位罗列了一些Data URL的这么几种形式那Data URL呢它有很多种形式有一个最简单的是什么注意Data冒号接着我们说过了MiniTab和Base64都可以省略好了加一逗号接着后面写我们的数据比如说呢很厉害Very good吧Very goodOK那你点回车确确实实它就能访问
[04:22] 并且呢把这very good有显示出来了那这不就是我们的文本内容吗OK那好了当然了底下还有很多的这么几种类型比如说呢可以是html代码片段比如说呢可以是css代码片段比如说呢这边还可以是java scriptgif图或者png图或者是我们的icont等等等等那这个呢是简单的和各位来聊了一下我们
[04:49] Data URL它基本的一个构成以及给各位举例来看了一下Data URL它大致有的这么几种形态那对于Data URL有很多那在我们做Java程序员或者在我们程序开发的过程当中用的最多的或者基本上90%以上的可能性我们是借助Data URL帮我们构造图片
[05:15] 构造图片所以接下来呢我们再去讲Data URL的时候就是以图片来分析以图片来进行说明

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解 Data URL 的概念、格式和基本原理，通过演示如何在浏览器中直接嵌入图片数据。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：桌面环境，显示“黑马程序员”和“博学谷”标志，桌面上有“ihrm”文件夹图标。
画面2：在“ihrm”文件夹下的“day9”目录中，右键点击“dataurl.txt”文件，弹出菜单，选择“用 Notepad++ 打开”。
画面3：Notepad++ 编辑器打开“dataurl.txt”，内容为一行 base64 编码的图片数据：data:image/png;base64,iVBORw0KG...
画面4：打开 PPT 文档“Sus5-HRM...”，当前页为“1.2 Data URL”，展示员工信息页面截图，介绍 Data URL 概述。
画面5：PPT 页面中高亮显示“Data URL 是指‘data’类型的Url格式...”文字。
画面6：Notepad++ 编辑器中，光标位于“data:image/png;base64,iVBORw0KG...”末尾，显示“dataurl.txt”文件内容。
画面7：PPT 页面中，高亮显示“data:text/plain,<文本数据>”和“data:text/html;base64,<base64编码的html代码>”等格式。
画面8：浏览器地址栏显示“data:image/png;base64,iVBORw0KG...”，页面为黑色背景，显示“传智播客”标志。
画面9：PPT 页面中，显示“data:text/plain,<文本数据>”等格式列表。
画面10：浏览器地址栏输入“data:very good”，页面仍为黑色背景，显示“传智播客”标志。
画面11：PPT 页面中，高亮显示“data:text/css;base64,<base64编码的css代码>”等格式。
画面12：PPT 页面中，显示“1.2.3 Data URL基本原理”，介绍 Data URL 将图片转换为 base64 编码字符串并存入 URL 中。
画面13：PPT 页面中，显示“data:text/css;base64,<base64编码的css代码>”等格式列表。
画面14：PPT 页面中，高亮显示“data:image/jpeg;base64,<base64编码的jpeg图片数据>”等格式。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAA...（完整 base64 数据）

画面6：
data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAIAAA...（完整 base64 数据）

画面7：
data:text/plain,<文本数据>
data:text/html,<html代码>
data:text/html;base64,<base64编码的html代码>
data:text/css,<css代码>
data:text/css;base64,<base64编码的css代码>
data:text/javascript,<javascript代码>
data:text/javascript;base64,<base64编码的javascript代码>
data:image/gif;base64,<base64编码的gif图片数据>
data:image/png;base64,<base64编码的png图片数据>
data:image/jpeg;base64,<base64编码的jpeg图片数据>
data:image/x-icon;base64,<base64编码的icon数据>

画面11：
data:text/css;base64,<base64编码的css代码>
data:text/javascript;base64,<base64编码的javascript代码>
data:image/gif;base64,<base64编码的gif图片数据>
data:image/png;base64,<base64编码的png图片数据>
data:image/jpeg;base64,<base64编码的jpeg图片数据>
data:image/x-icon;base64,<base64编码的icon数据>

画面12：
Data URL 将了我们一种很巧妙的将图片“嵌入”到HTML中的方法。跟传统的用 img 标记将服务器上的图片引用到页面中的方式不一样，在Data URL 协议中，图片被转换成base64编码的字符串形式，并存储在URL中，冠以mime-type。
图片在网页中的使用方法通常是下面这种利用 img 标记的形式：

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面4：
标题：1.2 Data URL
子标题：1.2.1 Data URL概述
内容：所谓DataURL是指“data”类型的Url格式，是在RFC2397中提出的，目的是对于一些“小”的数据，可以在网页中直接嵌入，而不是从外部文件载入。
子标题：1.2.2 Data URL入门
内容：完整的DataURL语法：DataURL = data:mediatype;base64,<Base64编码的数据>。
内容：mediatype：表述传递的数据的MIME类型（text/html, image/png, image/png）
内容：简单的说，data类型的Url大致有下面几种形式。
内容：data:,<文本数据>

画面7：
标题：1.2.2 Data URL入门
内容：完整的DataURL语法：DataURL = data:mediatype;base64,<Base64编码的数据>。
内容：mediatype：表述传递的数据的MIME类型（text/html, image/png, image/png）
内容：简单的说，data类型的Url大致有下面几种形式。
内容：data:,<文本数据>
内容：data:text/plain,<文本数据>
内容：data:text/html,<html代码>
内容：data:text/html;base64,<base64编码的html代码>
内容：data:text/css,<css代码>
内容：data:text/css;base64,<base64编码的css代码>
内容：data:text/javascript,<javascript代码>
内容：data:text/javascript;base64,<base64编码的javascript代码>
内容：data:image/gif;base64,<base64编码的gif图片数据>
内容：data:image/png;base64,<base64编码的png图片数据>
内容：data:image/jpeg;base64,<base64编码的jpeg图片数据>
内容：data:image/x-icon;base64,<base64编码的icon数据>

画面12：
标题：1.2.3 Data URL基本原理
内容：Data URL 将了我们一种很巧妙的将图片“嵌入”到HTML中的方法。跟传统的用 img 标记将服务器上的图片引用到页面中的方式不一样，在Data URL 协议中，图片被转换成base64编码的字符串形式，并存储在URL中，冠以mime-type。
内容：图片在网页中的使用方法通常是下面这种利用 img 标记的形式：

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

