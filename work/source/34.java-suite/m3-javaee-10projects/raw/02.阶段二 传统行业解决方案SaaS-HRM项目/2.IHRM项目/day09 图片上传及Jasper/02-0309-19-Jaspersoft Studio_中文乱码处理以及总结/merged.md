# 19-Jaspersoft Studio：中文乱码处理以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\19-Jaspersoft Studio：中文乱码处理以及总结_【海量资源尽在 ubkz.com】.mp4
- 时长 7分14秒（音频 434s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们已经通过Springboard的程序通过浏览器访问可以预览到当前的这个PDF文件当然这边也可以对这个PDF文件进行一个下载和打印的一些内容这个就不归我们管了那接下来我想跟各位来聊的就是说你仔细去观察生成好的这个PDF仔细观察你会发现好像和我们刚才通过死丢丢创建预览的内容不一样
[00:29] 那我们一起回到我们的死丢丢模板当中各位仔细观察你发现这个预览这边logo中间Jasper很强大有三个字底下传志博客出品六个字那这个是不是叫做中文那你再回到我们的论览器各位来看你会发现只要是一道中文的地方好像它都没有显示没错吧所以接下来我们重点要解决的就是在Jasper
[00:58] Report当中对中文的一个处理那对中文的处理如何去做呢注意这个其实是Jadper Report的一个经典问题就是说他其实默认对我们中文的支持呢还是不够友好的但是他可以通过打补丁的形式把中文解决掉那我们应该如何去做呢注意这个解决起来基本上都是一个固定的套路那这个套路呢一共分成两个阶段第一个阶段是这样的
[01:27] 注意这个乱码处理呢需要两个阶段第一个阶段在设计阶段只要涉及到中文的地方我们需要对这个中文进行一个编码的处理比如说这张材我扎扎子盆很强大这个很强大我对它进行了一个中文说明华文送体没错吧好了比如说底下这边传志博客出品我也指定了华文送体这个不是随便指定的能理解啊所以对于涉及到中文首先要指定
[01:54] 它的字体注意这个字体呢可以指定成宋体等等等等所有都可以只要涉及到中文就需要指定那比如说我的所有中文设计成华文宋体那第一件事搞定了那第二件事回到我们的代码在我们的代码当中开始打补丁那打的补丁如何去做找到我们的Java代码部分好了各位在今天的资料当中
[02:20] 我已经把这个补定给各位准备好了资源里面有一个乱码问题的解决那这个补定分成两个部分第一个是一个配置文件Properties的一个属性配置文件Ctrl C把它copy到你工程的resource目录下好了copy过来之后在这个上边我以显示声明的形式就是明确的告诉他明确的告诉他我这个PDF当中可能要设计到一些字体
[02:50] 那这个字体在哪写着在一个叫做strongs里面的fonts.xml当中声明了也就是说我里面用到中文这个中文在哪进行了一个说明在这个里面那我需要各位把这个字元当中的strongs这个目录control c也全部都copy到resource目录下control v好了copy过来之后各位打开这个fonts.xml里面写了一个华文送体
[03:16] 那这个华文送体它的字体样式究竟是什么样的究竟是什么样的全部在这个ttf文件当中有描述全部在这个ttf文件当中有描述直接引用让他自己去查找就可以了所以这样一来我们就通过打补丁的形式以更加明确的形式告诉他我只要涉及到中文的字体你去找放死的XML那放死的XML里面
[03:45] 写了一个如果说你这里面涉及到中文中文这个字体名字叫做华文宋体那我们就开始对华文宋体进行一个补丁的一个处理能理解吧OK那好了这样一来我们这个中文也已经处理好了当然了如果说你用的是其他的一些中文的话比如说你用其他的中文什么华文凯提华文彩云等等那你这边是不是也要做相应的配置这个没错吧各位OK那好了这个我们处理好了之后
[04:16] 接下来我们可以重新启动一下我们这个微服务好了这边让它去重启让它去重启那我这边呢刚才有一个点没有说到就是这个stone.ttf那这个文件呢其实是所有的字体文件这个文件不是我提供的也不是我准备的是我从扎斯普官方文档下载下来的这个里面有所有的字体文件字体的一些格式OK好了这边呢已经启动成功了我们再去回到我们的
[04:45] 浏览器刷新一把看一下中文现在是否已经有了没错了那这样一来我们的中文其实就已经彻底解决掉了好了那到目前为止呢其实我们今天的所有内容就跟各位都说过了对于我们今天呢一共是分成两大块内容那分成了细分的分成五小节这两块内容第一块就是图片上传那对于图片上传首先跟各位介绍的是Data UIL希望各位还有印象
[05:16] 那是以这种巧妙的形式字符创的形式去体现一个UIL地址那接着呢就是对于某一些格式容量比较大的一些图片的话我们是不是可以借助一些优良的产品比如说七牛云存储帮助我们去快速更加实惠的去搭建这么一个存储平台那七牛云存储我们之前也玩过那也比较简单直接使用人家提供的SDK就能完成文件的上传完整的查看
[05:45] 等等接下来我们聊的就是一个报表打印对于报表打印有很多种方式我们采用的是Jasper Report对于Jasper Report来说希望各位知道它开发的一个阶段和它的一个生命周期我们通过一些简单的代码我们得知了我们自己要去创建Jasper Report生成PDF的时候我们关注的点就三个第一个制作模板第二个构造数据第三个填充数据那剩下的事情
[06:14] 比如说我们这边这个案例你会发现你如果就是要把一个PDF生成的话我们关注的点比如说上边什么FS这代码读取扎字本文件是不是固定的那底下这边生成print这个代码可能我们要关注了因为我们说过数据可能是千变万化的我们的数据如何传递过去是我们关注的那最后这个一PDF形式输出是不是也是固定啊所以对于我们之后写代码关注的内容关注的点就这么几个了
[06:43] 模板制作好你把数据给我查出来接着调用方法把模板里面内容填充好所以就关注这三个点就可以了当然我们也介绍了一下这个Studio工具应该如何去使用如果各位有Eclipse基础的话你会发现都比较简单那最后就跟各位来了一个最简单的入门案例它是一个静态文字静态图片的一种形式那剩下一些更加高级的使用我们在明天的课程还会跟各位重点进行讲解OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 JasperReports，并使用 JasperSoft Studio 设计和预览报表，同时配置自定义字体。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 浏览器显示一个简单的 HTML 页面，内容为 "Jasper !!"，URL 为 http://localhost:8181/test/jasper。
画面 2: 浏览器页面顶部出现 "传智播客 www.itcast.cn" 的 Logo。
画面 3: IntelliJ IDEA 项目视图，显示项目名为 "jasper Spring Boot"，包含子模块 "jr-demo" 和 "qiniu demo"。
画面 4: 空白桌面，无任何应用程序窗口。
画面 5: IntelliJ IDEA 中弹出 "Copy" 对话框，源文件为 "strong.TTF"，目标目录为项目中的 "strong" 文件夹，新文件名输入为 "strong"。
画面 6: IntelliJ IDEA 中打开 "fonts.xml" 文件，内容为定义字体家族和导出字体的配置。
画面 7: JasperSoft Studio 报表设计器界面，显示 "test.jrxml" 报表，包含 "Page Header" 和 "Page Footer" 区域，其中 "Page Header" 显示 "Jasper 很强大!!"。
画面 8: IntelliJ IDEA 中弹出 "Register New File Type Association" 对话框，提示 ".TTF" 文件类型未关联，选择 "Text" 作为关联类型。
画面 9: PPT 页面，标题为 "5.3 开发流程概述"，内容包括 "制作报表模板"、"模板编译"、"构造数据"，并显示 "黑马程序员" 的 Logo。
画面 10: PPT 页面，标题为 "3.3 JasperReport框架的介绍"，内容介绍 JasperReports 是一个开源 Java 报表库，支持多种输出格式。
画面 11: PPT 页面，标题为 "4.3 开发流程概述"，内容包括 "制作报表模板"、"模板编译"、"构造数据"。
画面 12: IntelliJ IDEA 项目视图，显示 "jasper Spring Boot" 项目结构，包含 "src/main/java" 和 "src/main/resources" 目录。
画面 13: PPT 页面，标题为 "5 模板工具Jaspersoft Studio"，内容介绍 JasperSoft Studio 是基于 Eclipse 的报表设计器，支持多种数据源和输出格式。
画面 14: JasperSoft Studio 中的 "Create a JasperReports project" 向导界面，选中 "JasperReports Project"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
Copy directory C:\Users\ThinkPad\Desktop\hrm\day04\资源\字体\strong
New name: strong
To directory: E:\workspace\hrm\jiqui-test\jasper-Spring Boot\src\main\resources
Use Alt+Shift for path completion
画面 6:
<fontFamily name="华文宋体">
  <normal>strong/strong.TTF</normal>
  <bold>strong/strong.TTF</bold>
  <italic>strong/strong.TTF</italic>
  <boldItalic>strong/strong.TTF</boldItalic>
  <pdfEncoding>Identity-H</pdfEncoding>
  <pdfEmbedded>true</pdfEmbedded>
</fontFamily>
<exportFonts>
  <export key="net.sf.jasperreports.html">"华文宋体", Arial, Helvetica, sans-serif</export>
  <export key="net.sf.jasperreports.xhtml">"华文宋体", Arial, Helvetica, sans-serif</export>
</exportFonts>
画面 12:
src
  main
    java
      cn.itcast
        Controller
          JasperApplication.java
    resources
      strong
        strong.TTF
      templates
      application.yml
      jasperreports_extension.properties
    test
      JasperSpringbootImpl.java
      pom.xml
    target
画面 13:
JasperSoft Studio 是 JasperReports 库和 JasperReports 服务器的基于 Eclipse 的报告设计器。它可以作为 Eclipse 插件或作为独立的应用程序使用。JasperSoft Studio 允许您创建包含图表、图像、子报表、交叉表的复杂布局。您可以通过 JDBC、TableModels、JavaBeans、XML、Hibernate（如 Hive）、CSV、XML/AI 及自定义来源等各种来源访问数据，然后将报告发布为 PDF、RTF、XML、XLS、CSV、HTML、文本、DOCX 或 OpenOffice。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9:
标题: 5.3 开发流程概述
内容:
- 制作报表模板
- 模板编译
- 构造数据
底部: 北京市昌平区建材城西路金鼎龙办公楼一层 电话：400-618-9090
Logo: 黑马程序员 www.itheima.com
画面 10:
标题: 3.3 JasperReport框架的介绍
内容:
1. iText PDF: iText 是著名的开源项目，是用于生成 PDF 文档的 Java 类库。通过 iText 不仅可以生成 PDF 或 rtF 的文档，而且可以将 XML、HTML 文件转换为 PDF 文件。
2. Openoffice: openoffice 可以在 Windows 和 Linux 平台下运行，可以灵活的将 Word 或者 Excel 转化为 PDF 文件。
3. Jasper Report: 是一个强大、灵活的报表生成工具，能够展示丰富的页面内容，并将其转换成 PDF。
画面 11:
标题: 4.3 开发流程概述
内容:
- 制作报表模板
- 模板编译
- 构造数据
底部: 北京市昌平区建材城西路金鼎龙办公楼一层 电话：400-618-9090
Logo: 黑马程序员 www.itheima.com
画面 13:
标题: 5 模板工具Jaspersoft Studio
内容:
5.1 概述
JasperSoft Studio 是 JasperReports 库和 JasperReports 服务器的基于 Eclipse 的报告设计器。它可以作为 Eclipse 插件或作为独立的应用程序使用。JasperSoft Studio 允许您创建包含图表、图像、子报表、交叉表的复杂布局。您可以通过 JDBC、TableModels、JavaBeans、XML、Hibernate（如 Hive）、CSV、XML/AI 及自定义来源等各种来源访问数据，然后将报告发布为 PDF、RTF、XML、XLS、CSV、HTML、文本、DOCX 或 OpenOffice。
5.2 安装配置
画面 14:
标题: Create a JasperReports project
内容:
Wizards:
  CVS
    JasperSoft Studio
      JasperReports Project
      JasperReports Samples
    Java
    Plug-in Development
    SVN
  Show All Wizards.

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

