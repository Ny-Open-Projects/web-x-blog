# 画面线理解：06-Jdbc数据源数据填充：传递Connection填充数据并展示PDF

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\06-Jdbc数据源数据填充：传递Connection填充数据并展示PDF_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:09, 01:24, 02:28, 04:34, 05:23, 06:08, 06:29, 07:10, 07:59, 08:14, 09:33, 10:00, 10:24, 10:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:41:10

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 JasperReports 实现带参数的数据库报表导出功能，包括报表设计、参数传递和数据库连接配置。

2) 按时间顺序列出每张画面的要点：
画面1：在 JasperReports Studio 中打开名为 testConn.jrxml 的报表文件，设计界面显示“用户列表”标题和 Detail 1 区域，左侧 Outline 显示字段如 id, username, mobile, company_name, department_name。
画面2：在报表设计界面中，拖拽并放置了多个 Static Text 元素，分别显示 SF(id), SF(username), SF(mobile), SF(company_name), SF(department_name)，并调整了其中一个元素的位置和大小。
画面3：报表设计界面显示了完整的表格布局，包含“用户列表”标题和五个字段的静态文本框，布局为 Free Layout。
画面4：在 Detail 1 带中，调整了布局高度为 125px，Split Type 设置为 Stretch。
画面5：在 Detail 1 带中，将 Layouts 设置为 Free Layout，Height 设置为 125px，Split Type 设置为 Stretch。
画面6：在 IntelliJ IDEA 中，查看 JasperController02.java 文件，代码中使用 HashMap 设置参数并调用 JasperFillManager.fillReport() 方法。
画面7：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中使用 HashMap 设置参数并调用 JasperFillManager.fillReport() 方法。
画面8：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中添加了 public Connection getConnection() 方法的声明。
画面9：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中在 getConnection() 方法中使用 DriverManager.getConnection() 方法。
画面10：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中在 getConnection() 方法中使用 Class.forName("com.mysql.jdbc.Driver")。
画面11：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中在 getConnection() 方法中使用 DriverManager.getConnection("jdbc:mysql://localhost/lhrm", "root", "111111")。
画面12：在 IntelliJ IDEA 中，查看项目结构，显示 testConn.jasper 文件位于 templates 目录下。
画面13：在 IntelliJ IDEA 中，查看控制台输出，显示 Tomcat 启动日志和一个错误：Cannot render error page for request。
画面14：在浏览器中，显示生成的 PDF 报表，标题为“用户列表”，包含用户 ID、姓名、部门等字段的数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
```java
@GetMapping("/testJasper2")
public void createPdf(HttpServletRequest request, HttpServletResponse response) throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/testParam.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.创建JasperPrint,向jasper文件中填充数据
    ServletOutputStream os = response.getOutputStream();
    try {
        Map parameters = new HashMap<>();
        //设置参数,参数的key = 模板中使用的parameters参数的name
        parameters.put("username", "张三");
        parameters.put("mobile", "120");
        parameters.put("dept", "销售部");
        parameters.put("company", "传智播客");
        JasperPrint print = JasperFillManager.fillReport(fis, parameters, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException c) {
        c.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面7：
```java
package cn.itcast.controller;
import org.springframework.web.bind.annotation.*;
@RestController
public class JasperController03 {
    @GetMapping("/testJasper2")
    public void createPdf(HttpServletRequest request, HttpServletResponse response) throws IOException {
        //1.引入jasper文件
        Resource resource = new ClassPathResource("templates/testParam.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        //2.创建JasperPrint,向jasper文件中填充数据
        ServletOutputStream os = response.getOutputStream();
        try {
            Map parameters = new HashMap<>();
            //设置参数,参数的key = 模板中使用的parameters参数的name
            parameters.put("username", "张三");
            parameters.put("mobile", "120");
            parameters.put("dept", "销售部");
            parameters.put("company", "传智播客");
            JasperPrint print = JasperFillManager.fillReport(fis, parameters, new JREmptyDataSource());
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException c) {
            c.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

画面8：
```java
public Connection getConnection() {
```

画面9：
```java
public Connection getConnection() {
    Connection conn = DriverManager.getConnection();
    return conn;
}
```

画面10：
```java
public Connection getConnection() throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection();
    return conn;
}
```

画面11：
```java
public Connection getConnection() throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/lhrm", "root", "111111");
    return conn;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
