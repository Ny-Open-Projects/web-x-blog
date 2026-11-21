# 画面线理解：19-Jaspersoft Studio：中文乱码处理以及总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\19-Jaspersoft Studio：中文乱码处理以及总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 00:47, 01:11, 02:21, 03:09, 03:29, 04:02, 04:29, 04:58, 05:49, 06:05, 06:19, 06:51, 06:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:34:00

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中集成 JasperReports，并使用 JasperSoft Studio 设计和预览报表，同时配置自定义字体。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 浏览器显示一个简单的 HTML 页面，内容为 "Jasper !!"，URL 为 http://localhost:8181/test/jasper。
画面 2: 浏览器页面顶部出现 "传智播客 www.itcast.cn" 的 Logo。
画面 3: IntelliJ IDEA 项目视图，显示项目名为 "jasper springboot"，包含子模块 "jr-demo" 和 "qiniu demo"。
画面 4: 空白桌面，无任何应用程序窗口。
画面 5: IntelliJ IDEA 中弹出 "Copy" 对话框，源文件为 "strong.TTF"，目标目录为项目中的 "strong" 文件夹，新文件名输入为 "strong"。
画面 6: IntelliJ IDEA 中打开 "fonts.xml" 文件，内容为定义字体家族和导出字体的配置。
画面 7: JasperSoft Studio 报表设计器界面，显示 "test.jrxml" 报表，包含 "Page Header" 和 "Page Footer" 区域，其中 "Page Header" 显示 "Jasper 很强大!!"。
画面 8: IntelliJ IDEA 中弹出 "Register New File Type Association" 对话框，提示 ".TTF" 文件类型未关联，选择 "Text" 作为关联类型。
画面 9: PPT 页面，标题为 "5.3 开发流程概述"，内容包括 "制作报表模板"、"模板编译"、"构造数据"，并显示 "黑马程序员" 的 Logo。
画面 10: PPT 页面，标题为 "3.3 JasperReport框架的介绍"，内容介绍 JasperReports 是一个开源 Java 报表库，支持多种输出格式。
画面 11: PPT 页面，标题为 "4.3 开发流程概述"，内容包括 "制作报表模板"、"模板编译"、"构造数据"。
画面 12: IntelliJ IDEA 项目视图，显示 "jasper springboot" 项目结构，包含 "src/main/java" 和 "src/main/resources" 目录。
画面 13: PPT 页面，标题为 "5 模板工具Jaspersoft Studio"，内容介绍 JasperSoft Studio 是基于 Eclipse 的报表设计器，支持多种数据源和输出格式。
画面 14: JasperSoft Studio 中的 "Create a JasperReports project" 向导界面，选中 "JasperReports Project"。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 5:
Copy directory C:\Users\ThinkPad\Desktop\hrm\day04\资源\字体\strong
New name: strong
To directory: E:\workspace\hrm\jiqui-test\jasper-springboot\src\main\resources
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
        controller
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
