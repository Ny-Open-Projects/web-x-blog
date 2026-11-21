# 画面线理解：12-JasperReport：声明周期

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\12-JasperReport：声明周期_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:25, 00:44, 01:36, 02:52, 03:31, 03:51, 04:03, 04:17, 04:40, 04:52, 05:10, 05:50, 06:25, 08:09
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:29:32

1) 这一组画面整体在讲JasperReport的生命周期（设计、执行、输出三个阶段）及其在Java项目中的开发步骤和相关代码实现。

2) 按时间顺序列出每张画面的要点：
画面1: 展示JasperReport生命周期图，包含设计阶段（MyReport.jrxml）、执行阶段（MyReport.jasper + Data）、输出阶段（MyReport.pdf），并说明三个阶段分别为设计、执行、输出。
画面2: PPT标题为“4.2 JasperReport原理简述”，下方有地址和电话信息。
画面3: PPT标题为“4 JasperReport的开发步骤”，子标题“4.1 JasperReport生命周期”，内容与画面1相同。
画面4: 与画面1内容相同，展示JasperReport生命周期图。
画面5: IntelliJ IDEA界面，显示项目“qinlu-demo”。
画面6: Windows资源管理器，显示“生命周期测试”文件夹下的“PDFTest.java”、“pom.xml”、“test01.jrxml”文件。
画面7: IntelliJ IDEA中打开的“pom.xml”文件，内容为Maven配置。
画面8: IntelliJ IDEA中右键“jr-demo”项目，弹出“Find Usages”等选项。
画面9: Windows资源管理器，显示“生命周期测试”文件夹下的“PDFTest.java”、“pom.xml”、“test01.jrxml”文件。
画面10: IntelliJ IDEA中打开的“JDemo.java”文件，包含三个方法：createJasper、createJprint、showPdf。
画面11: PPT标题为“4.2 JasperReport原理简述”，内容与画面1相同。
画面12: Notepad++中打开的“test01.jrxml”文件，内容为JasperReport设计文件。
画面13: PPT标题为“4.2 JasperReport原理简述”，内容与画面1相同。
画面14: IntelliJ IDEA中打开的“JDemo.java”文件，显示“createJprint”方法的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面7: pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>jr-demo</artifactId>
    <version>1.0-SNAPSHOT</version>
    <pr>

画面10: JDemo.java
public static void main(String[] args) {
    try {
        String path = "C://Users//ThinkPad//Desktop//ihrm//day9//资源//test01.jrxml";
        JasperCompileManager.compileReportToFile(path);
    } catch (Exception e) {
        e.printStackTrace();
    }

    public static void createJprint(){
        try {
            String path = "C://Users//ThinkPad//Desktop//ihrm//day9//资源//test01.jasper";
            //通过Jasper文件填充数据，生成报表
            JasperFillManager.fillReportToFile(path, new HashMap(), new JREmptyDataSource());
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    public static void showPdf(){
        try {
            String path = "C://Users//ThinkPad//Desktop//ihrm//day9//资源//test01.jasper";
            JasperViewer.viewReport(path, isXMLFile: false);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

画面12: test01.jrxml
<?xml version="1.0" encoding="UTF-8"?>
<jasperReport xmlns="http://jasperreports.sourceforge.net/jasperreports" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/jasperreports.xsd">
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="6.14.0"/>
    <property name="ireport.jasperReportVersion" value="
