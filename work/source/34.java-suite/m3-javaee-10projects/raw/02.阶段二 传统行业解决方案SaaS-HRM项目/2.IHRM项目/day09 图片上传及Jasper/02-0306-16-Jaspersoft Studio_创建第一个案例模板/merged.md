# 16-Jaspersoft Studio：创建第一个案例模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\16-Jaspersoft Studio：创建第一个案例模板_【海量资源尽在 ubkz.com】.mp4
- 时长 5分29秒（音频 330s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 简单的看了一下通过C99工具创建出的模板它的一个工程结构接下来我们就可以一起通过C99工具去对我们第一个模板进行一个简单的设计工作其实这几块区域其实可以根据个人的不同情况它能做不同的删减比如说你如果这个title不想要它选中之后注意这边有一个选中的提示选中之后直接删掉delete就可以了比如说
[00:30] column header也不想要delete删掉好了footer不想要delete删掉j要不想要delete删掉就可以了那接下来呢就是说比如说这个头部分那你觉得头部分呢可能比较比较窄那你可以往下去调往上去调都可以那接下来那对于我们而言对于我们而言你想要在头里面去填写一些内容那比如说想填出一张图片那怎么做那注意我们关注的是右边的这些组件
[01:00] 比如说你想要填充一张图片,你直接拖拽过来一张图就可以了,这边的图呢,有很多种形式可以让我们进行选择,比如说呢,可能可以是当前这个工程里面的一张图片,那也可以是你的一个系统路径当中的一个图片,你当前这个电脑磁盘当中的一个图片,也可以是你的一个UIL地址,当然你可以也从服务器上进行一个选择,也可以自定义,都可以有很多种方式,比如说呢,我就想要存储一张URL的这么一张图形,
[01:30] 我就选UIL这边就让你去填写这个UIL图片的地址这个地址在哪我就用我们传职博客的logo图来做了Ctrl C这是我们传职博客网络的一个logo图Ctrl V 靠过来OK 这边有一个简单的一个预览的这么一个功能好了 接下来点击OK这个图片就给我填充到这边了这个图片其实填过来之后有的朋友说这个图片好像有点小我们可以做一个简单的调整
[01:58] 哎调整一下其实就可以了当然这调整好像有点大了好了调整一下那调整好了之后那我们的头部分其实就已经搞定了那中间部分那对于这个中间部分的内容比如说我想填充一句话那填充一句话怎么做注意这边去选那有text field注意我们不用它我们用的是static text是一些静态的哎内容好了静态的内容比如说呢我可以填充一句话双击
[02:28] 拖过来的组件里面我们就可以填写比如说呢叫做扎斯珀啊is very很强大吧强大ok很强大来两个参号ok那接着我们中间的这个内容也填充好了那填充好了之后呢这个里面呢我们可以对这个字体做一个设置比如说呢我可以把它设置成很多的字体那我底下就开始去找比如说呢我们就来一个华文送题吧
[03:04] 还送体当然你也可以对这个字体大小做一个调整比如说我可以来一个18号字OK你会发现这个其实就是一个支持拖拽的这么一个工具其实就跟拼图一样就跟做游戏一样OK拼好了那接下来呢底下这边来一footer那footer里面呢你如果想用图片喜欢用一些文字的话也可以静态文字拖拽过来比如说呢这个就是我们传志博客出品哎出品
[03:36] OK当然了对于中文来说呢我们也可以调整一下这个字体调整字体就从上面去找就可以了比如说就用华文宋体华文宋体十号字其实就可以了OK那我这边呢进行一个保存Ctrl S进行保存那保存好了之后这个其实我们就已经设计成功了那设计成功了之后那这个它的原码是什么样我们可以看一下通过哪Source那点进来过来之后你会发现这边Header部分是一张图
[04:07] 图片的一个网络地址在中间接着detail部分里面打印了一句话Jasper很强大华文宋体18号字底下是我们的page footer里面也是一句话代表的传承不可出品接下来就是说你究竟生成的pdf它究竟什么样子的别忘了我们是要把这些内容填充到一个A4纸里面还有一下那填充到什么样子能不能预览可以这边有一个按钮还有一下PowerView
[04:35] 好了点击这个就是我们生成预览之后的这么一个pdf形式那上边我们的图形中间一句话那底下最后的一个结尾部分OK那这样一来我们就已经生成好了这么一个jrxml的这么一个模板那对于这个模板咱们生成好了接下来还记着我们刚才写的那个简单的案例还要进行编译等等预览等等这个预览过程我们已经有了接下来就少编译了
[05:04] 那如何编译很简单我们可以在这边txt右键底下往下找有一个comment report那各位你点击你会发现当前路径下多了一个文件test.jasper那这样一来我们就可以通过我们这个studio工具直接设计并且得到我们的jasper本件了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 JasperReports Studio 中设计一个包含图片和静态文本的报表，并通过源码视图进行配置和预览。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 JasperReports Studio 的设计界面，报告名为 test.jrxml，包含 Title、Page Header、Column Header、Detail 1 等默认带的带区。
画面2: 鼠标选中了 Page Footer 带区，Outline 面板中显示了 Band: Summary。
画面3: 弹出“Create new image element”对话框，选择“URL (a remote URL referring to an image, will be the expression value)”选项。
画面4: 在“Create new image element”对话框中，用户在“Enter a URL referring to an external resource:”输入框中输入了 URL。
画面5: 切换到 Source 视图，显示了 test.jrxml 文件的 XML 代码，其中包含 <image> 和 <staticText> 元素。
画面6: 在 Source 视图中，光标位于 <image> 元素的 <imageExpression> 标签内。
画面7: 在 Source 视图中，光标位于 <staticText> 元素的 <textElement> 标签内。
画面8: 在 Source 视图中，光标位于 <staticText> 元素的 <textElement> 标签内，准备修改内容。
画面9: 在 Source 视图中，光标位于 <staticText> 元素的 <textElement> 标签内，准备修改内容。
画面10: 在 Source 视图中，光标位于 <staticText> 元素的 <textElement> 标签内，准备修改内容。
画面11: 切换到 Preview 视图，显示报告预览，内容为“Static Text”。
画面12: 切换到 Preview 视图，显示报告预览，内容为“Jasper 很强大”。
画面13: 切换到 Preview 视图，显示报告预览，内容为“Jasper 很强大 II”。
画面14: 点击“Compile Report”按钮后，弹出“Progress Information”对话框，显示“Compiling: test.jrxml”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**：
画面5-10 中的 XML 代码：
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/jasperreports.xsd">
    <property name="com.jaspersoft.studio.data.defaultDataAdapter" value="One Empty Record"/>
    <queryString>
        <![CDATA[]]>
    </queryString>
    <background>
        <band splitType="Stretch">
            <image>
                <reportElement x="1" y="6" width="168" height="40" uuid="0754a0ad-8c58-4a3c-990b-8c356e0c2387"/>
                <imageExpression><![CDATA["http://www.itcast.cn/images/logo.png"]]></imageExpression>
            </image>
        </band>
    </background>
    <pageHeader>
        <band height="125" splitType="Stretch">
            <staticText>
                <reportElement x="210" y="58" width="180" height="62" uuid="75e0c03-9f10-4a80-b4f7-35cf1c6c4d00">
                    <font fontName="黑体" size="18"/>
                </reportElement>
                <textElement>
                    <text><![CDATA[传智播客]]></text>
                </textElement>
            </staticText>
        </band>
    </pageHeader>
    <detail>
        <band height="44" splitType="Stretch">
            <staticText>
                <reportElement x="247" y="23" width="180" height="30" uuid="51e575c-08b7-4011-7405-9e1f5137">
                    <font fontName="黑体" size="18"/>
                </reportElement>
                <textElement>
                    <text><![CDATA[【Jasper 很强大！】]]></text>
                </textElement>
            </staticText>
        </band>
    </detail>
    <pageFooter>
        <band height="44" splitType="Stretch">
            <staticText>
                <reportElement x="247" y="23" width="180" height="30" uuid="51e575c-08b7-4011-7405-9e1f5137">
                    <font fontName="黑体" size="18"/>
                </reportElement>
                <textElement>
                    <text><![CDATA[【Jasper 很强大！】]]></text>
                </textElement>
            </staticText>
        </band>
    </pageFooter>
</jasperReport>

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

