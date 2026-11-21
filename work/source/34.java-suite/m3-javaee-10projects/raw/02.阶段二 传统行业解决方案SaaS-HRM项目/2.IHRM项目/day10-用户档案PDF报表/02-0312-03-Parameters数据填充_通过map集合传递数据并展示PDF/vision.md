# 画面线理解：03-Parameters数据填充：通过map集合传递数据并展示PDF

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\03-Parameters数据填充：通过map集合传递数据并展示PDF_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:38, 01:02, 01:08, 01:21, 01:36, 01:53, 02:47, 03:34, 03:45, 04:28, 04:42, 04:50, 05:18, 05:31
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:39:23

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 JasperReports，通过控制器方法动态填充参数并导出 PDF 报表。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 JasperReports Studio 中的报表设计界面，正在编辑名为 testParam.jrxml 的报表，包含“用户名”、“第二”、“手机号”、“ID”、“所属企业”、“传智播客”、“所属部门”、“讲师”等字段。
画面2: 在 IntelliJ IDEA 中，将 testParam.jrxml 文件复制为 testParam.jasper，目标路径为项目中的 templates 目录。
画面3: 在 IntelliJ IDEA 中，项目结构视图显示了 resources/templates 目录，准备用于存放报表模板。
画面4: 在 IntelliJ IDEA 中，展示 JasperController02.java 文件，其中包含一个 @GetMapping("/testJasper") 方法，用于创建 PDF 报表。
画面5: 在 IntelliJ IDEA 中，展示 JasperController02.java 文件，方法中使用 ClassPathResource 加载 testParam.jasper 文件。
画面6: 在 IntelliJ IDEA 中，展示 JasperController02.java 文件，方法中创建了 ServletOutputStream 用于输出 PDF。
画面7: 在 JasperReports Studio 中，展示 testParam.jasper 文件的属性，大小为 21411 字节。
画面8: 在 IntelliJ IDEA 中，展示 JasperController02.java 文件，方法中调用 JasperFillManager.fillReport 方法填充报表。
画面9: 在 IntelliJ IDEA 中，展示 JasperController02.java 文件，方法中创建了一个 HashMap 用于存储参数。
画面10: 在 IntelliJ IDEA 中，展示 JasperController02.java 文件，方法中向 HashMap 中添加了 "username"、"mobile"、"dept"、"company" 四个参数。
画面11: 在 IntelliJ IDEA 中，展示项目启动日志，显示 Spring Boot 应用成功启动在端口 8080。
画面12: 在浏览器中，访问 localhost:8080，显示黑马程序员的首页。
画面13: 在浏览器中，访问 localhost:8181/testJasper2，显示生成的 PDF 报表，内容为“用户信息”表格。
画面14: 在 PDF 阅读器中，展示关于 JasperReports 参数填充的文档内容，包括“1.1 参数Map填充数据”和“1.1.1 模板制作”等章节。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4:
```java
public class JasperController02 {
    @GetMapping("/testJasper")
    public void createPdf(HttpServletResponse response) throws IOException {
        //1.引入jasper文件
        Resource resource = new ClassPathResource("templates/test.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        //2.创建jasperPrint,向jasper文件中填充数据
        ServletOutputStream os = response.getOutputStream();
        try {
            JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
            //3.jasperPrint以PDF的形式输出
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException e) {
            e.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

画面5:
```java
//1.引入jasper文件
Resource resource = new ClassPathResource("templates/test.jasper");
FileInputStream fis = new FileInputStream(resource.getFile());
//2.创建jasperPrint,向jasper文件中填充数据
ServletOutputStream os = response.getOutputStream();
try {
    JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
    //3.jasperPrint以PDF的形式输出
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

画面6:
```java
//2.创建jasperPrint,向jasper文件中填充数据
ServletOutputStream os = response.getOutputStream();
try {
    JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
    //3.jasperPrint以PDF的形式输出
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

画面8:
```java
//2.创建jasperPrint,向jasper文件中填充数据
ServletOutputStream os = response.getOutputStream();
try {
    JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
    //3.jasperPrint以PDF的形式输出
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

画面9:
```java
//2.创建jasperPrint,向jasper文件中填充数据
ServletOutputStream os = response.getOutputStream();
try {
    Map parameters = new HashMap<>();
    //设置参数，参数的key = 模板中使用的parameters变量的name
    parameters.put("username", "第二");
    parameters.put("mobile", "120");
    JasperPrint print = JasperFillManager.fillReport(fis, parameters, new JREmptyDataSource());
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

画面10:
```java
//2.创建jasperPrint,向jasper文件中填充数据
ServletOutputStream os = response.getOutputStream();
try {
    Map parameters = new HashMap<>();
    //设置参数，参数的key = 模板中使用的parameters变量的name
    parameters.put("username", "第二");
    parameters.put("mobile", "120");
    parameters.put("dept", "传智播客");
    parameters.put("company", "传智播客");
    JasperPrint print = JasperFillManager.fillReport(fis, parameters, new JREmptyDataSource());
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面14:
PPT标题: “1.1 参数Map填充数据”
子标题: “1.1.1 模板制作”
内容:
- 通过这段填充数据的源代码得知，JasperReport对报表模板中的数据填充有很多中方式，最典型的有两种：
  - Parameters（参数）填充
  - DataSource（数据源）填充
- Parameters 通常是用来在打印的时候从程序里传值到报表里。也就是说 parameters 通常起着参数传递的作用。他们可以被用在一些特定的场合（比如应用中SQL 查询的条件），如report中任何一个需要从外部传入的变量等（如一个Image对象所包含的char或报表link的字符串）。parameters 也需要在创建的时候定义它的数据类型。parameters 的数据类型是标准的Java对象。

5) 不要评价画面美观，不要输出与课程无关的内容。
