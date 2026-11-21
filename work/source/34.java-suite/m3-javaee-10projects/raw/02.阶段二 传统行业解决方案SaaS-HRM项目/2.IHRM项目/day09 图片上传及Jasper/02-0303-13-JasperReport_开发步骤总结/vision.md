# 画面线理解：13-JasperReport：开发步骤总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\13-JasperReport：开发步骤总结_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:05, 00:37, 01:00, 01:44, 02:03, 02:11, 02:43, 03:16, 03:48, 04:10, 04:43, 05:16, 06:25, 06:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:30:08

1) 这一组画面整体在讲如何使用 JasperReports 在 Java 中生成报表，包括编译 .jrxml 文件、填充数据生成 .jprint 文件、以及预览 PDF 报表。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IntelliJ IDEA 中展示 Java 代码，定义了 `createJasper` 方法用于将 .jrxml 文件编译为 .jasper 文件。
画面2: 在 Windows 资源管理器中，显示了项目目录结构，包含 `test01.jrxml` 和 `test01.jprint` 文件。
画面3: 在 IntelliJ IDEA 中，代码中注释了 `createJprint` 方法，用于将 .jasper 文件填充数据生成 .jprint 文件。
画面4: 在 Windows 资源管理器中，右键点击 `test01.jprint` 文件，弹出菜单，显示了“使用 Windows Defender 打开”等选项。
画面5: 在 Windows 资源管理器中，显示了 `test01.jprint` 和 `test01.jrxml` 文件。
画面6: 在 IntelliJ IDEA 中，代码中添加了 `showPdf` 方法，用于预览生成的 PDF 报表。
画面7: 在 IntelliJ IDEA 中，代码中 `showPdf` 方法的注释被修改为“预览”。
画面8: 在 IntelliJ IDEA 中，代码中 `main` 方法调用 `showPdf` 方法。
画面9: 在 PPT 中，标题为“4.2 JasperReport原理简述”，下方有一个流程图，从“JRXML”指向“Jasper”。
画面10: 在 PPT 中，流程图继续，从“Jasper”指向“Jrprint”，再指向“Exporter”，最后指向“PDF/DOC/HTML”。
画面11: 在 PPT 中，显示了关于 JRXML、Jasper、Jrprint 和 Exporter 的说明文字。
画面12: 在 PPT 中，高亮显示了“Jasperreport可以输出多种格式的报表文件，常见的有HTML/PDF/XLS等”。
画面13: 在 IntelliJ IDEA 中，代码中 `main` 方法调用 `showPdf` 方法。
画面14: 在 PPT 中，显示了“4.3 开发流程概述”和“5 模板工具Jaspersoft Studio”标题。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```java
package cn.itcast.jr;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperViewer;
import java.util.HashMap;
public class JrDemo {
    public static void main(String[] args) {
        //1.将pdf模板转为jasper文件
        createJasper();
    }
    //1.将pdf模板转为jasper文件
    public static void createJasper(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jrxml";
            JasperCompileManager.compileReportToFile(path);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    //2.将jasper文件和数据进行填充，获取jprint
    public static void createJprint(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jasper";
            JasperFillManager.fillReportToFile(path, new HashMap(), new JREmptyDataSource());
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
```

画面6:
```java
//3.预览
public static void showPdf(){
    try{
        String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jprint";
        JasperViewer.viewReport(path, isXMLFile: false);
    }catch(Exception e){
        e.printStackTrace();
    }
}
```

画面8:
```java
public class JrDemo {
    public static void main(String[] args) {
        showPdf();
    }
    //1.将pdf模板转为jasper文件
    public static void createJasper(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jrxml";
            JasperCompileManager.compileReportToFile(path);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    //2.将jasper文件和数据进行填充，获取jprint
    public static void createJprint(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jasper";
            JasperFillManager.fillReportToFile(path, new HashMap(), new JREmptyDataSource());
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    //3.预览
    public static void showPdf(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jprint";
            JasperViewer.viewReport(path, isXMLFile: false);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面9: 标题“4.2 JasperReport原理简述”，下方流程图：JRXML → Jasper。
画面10: 流程图：Jasper → Jrprint → Exporter → PDF/DOC/HTML。
画面11: 文字说明：
1. JRXML-报表填充模板，本质是一个XML。
2. Jasper-由JRXML模板编译生成的二进制文件，用于代码级填充。
3. Jrprint-当用数据填充完jasper后生成的文件，用于输出报表。
4. Exporter-决定要输出的报表为何种格式，报表输出的管理类。
5. Jasperreport可以输出多种格式的报表文件，常见的有HTML/PDF/XLS等。
画面14: 标题“4.3 开发流程概述”和“5 模板工具Jaspersoft Studio”。

5) 无。
