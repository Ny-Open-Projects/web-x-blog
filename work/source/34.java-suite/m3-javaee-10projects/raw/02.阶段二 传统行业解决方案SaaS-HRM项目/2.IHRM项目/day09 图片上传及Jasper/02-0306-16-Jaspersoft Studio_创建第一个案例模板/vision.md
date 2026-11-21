# 画面线理解：16-Jaspersoft Studio：创建第一个案例模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\16-Jaspersoft Studio：创建第一个案例模板_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:20, 00:36, 01:03, 01:42, 04:01, 04:06, 04:09, 04:12, 04:17, 04:19, 04:36, 04:42, 04:46, 05:14
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:31:45

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
