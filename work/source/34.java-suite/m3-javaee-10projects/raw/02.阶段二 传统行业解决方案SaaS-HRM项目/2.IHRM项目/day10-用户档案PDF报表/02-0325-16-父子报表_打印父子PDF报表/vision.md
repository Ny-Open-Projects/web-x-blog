# 画面线理解：16-父子报表：打印父子PDF报表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\16-父子报表：打印父子PDF报表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:50, 02:05, 02:51, 03:11, 03:58, 04:25, 05:11, 05:41, 06:06, 06:54, 07:17, 07:40, 07:53
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:46:28

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 JasperReports 实现子报表（Subreport）功能，包括设计报表、配置数据源和编写控制器代码。

2) 按时间顺序列出每张画面的要点：
画面1: 在 JasperReports Studio 中，展示 main01.jrxml 报表设计界面，其中 Detail 1 区域被选中，右侧属性面板显示 Subreport 的配置，Expression 为 "testCharts.jasper"。
画面2: 展示一个手绘的流程图，说明子报表的调用关系：java程序 -> map (key: sublist, value: List<UserCount> list) -> 交报表 -> 功能1/2 -> 子报表1/2。
画面3: 在 JasperReports Studio 中，右键点击 testCharts.jrxml 文件，弹出菜单，选中 "Open With" 选项。
画面4: 在 IntelliJ IDEA 中，展示 Jasper Spring Boot 项目的目录结构，左侧为项目结构，右侧为 JasperController05.java 代码，其中包含创建 JasperPrint、设置参数、填充报表和导出 PDF 的代码。
画面5: 在 IntelliJ IDEA 中，展示 Jasper Spring Boot 项目的目录结构，左侧为项目结构，右侧为 JasperController05.java 代码，其中包含创建 JasperPrint、设置参数、填充报表和导出 PDF 的代码。
画面6: 在 IntelliJ IDEA 中，展示 JasperController07.java 代码，其中包含 createPdf 方法，用于创建 PDF 报表。
画面7: 在 IntelliJ IDEA 中，展示 JasperController07.java 代码，其中 createPdf 方法中添加了 parameters.put("sublist", ...); 语句。
画面8: 在 IntelliJ IDEA 中，展示 JasperController07.java 代码，其中 createPdf 方法中添加了 Resource subResout = new ClassPathResource("templates/testCharts.jasper"); 语句。
画面9: 在 IntelliJ IDEA 中，展示 JasperController07.java 代码，其中 createPdf 方法中添加了 parameters.put("subpath", subResout.getFile().getPath()); 语句。
画面10: 在 IntelliJ IDEA 中，展示 JasperController07.java 代码，其中 createPdf 方法中添加了 Resource subResout = new ClassPathResource("templates/testCharts.jasper"); 语句。
画面11: 在 JasperReports Studio 中，展示 testCharts.jrxml 报表设计界面，其中 Detail 1 区域被选中。
画面12: 在 JasperReports Studio 中，展示 main01.jrxml 和 testCharts.jrxml 两个报表并排显示，右侧属性面板显示 Subreport 的配置，Stretch 选项被选中。
画面13: 在 IntelliJ IDEA 中，展示 JasperController07.java 代码，其中 createPdf 方法中添加了 Resource subResout = new ClassPathResource("templates/testCharts.jasper"); 语句。
画面14: 在浏览器中，显示 localhost:8181/testlasper7 页面，页面为空白。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面4:
```java
//2.创建JasperPrint,把jasper文件中填充数据
ServletOutputStream os = response.getOutputStream();
try {
    Map parameters = new HashMap<>();
    //构建javaBean的数据源
    //通过List集合构建javaBean的数据源
    List<UserCount> userlist = getUserCountList();
    JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userList);
    JasperPrint print = JasperFillManager.fillReport(fis, parameters, ds);
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
public List<UserCount> getUserCountList() {
    List<UserCount> list = new ArrayList<>();
    return list;
}
```

画面6:
```java
@GetMapping("/testJasper6")
public void createPdf(HttpServletResponse response) throws Exception {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/main01.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.创建JasperPrint,把jasper文件中填充数据
    ServletOutputStream os = response.getOutputStream();
    try {
        Map parameters = new HashMap<>();
        //参数，子报表的路径，子报表需要的数据
        parameters.put("sublist", ...);
        JasperPrint print = JasperFillManager.fillReport(fis, parameters,);
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
public List<UserCount> getUserCountList() {
    List<UserCount> list = new ArrayList<>();
    return list;
}
```

画面7:
```java
//参数，子报表的路径，子报表需要的数据
parameters.put("sublist", ...);
```

画面8:
```java
Resource subResout = new ClassPathResource("templates/testCharts.jasper");
parameters.put("sublist", getUserCountList());
parameters.put("subpath", subResout.getFile().getPath());
```

画面9:
```java
Resource subResout = new ClassPathResource("templates/testCharts.jasper");
parameters.put("sublist", getUserCountList());
parameters.put("subpath", subResout.getFile().getPath());
```

画面10:
```java
Resource subResout = new ClassPathResource("templates/testCharts.jasper");
parameters.put("sublist", getUserCountList());
parameters.put("subpath", subResout.getFile().getPath());
```

画面13:
```java
Resource subResout = new ClassPathResource("templates/testCharts.jasper");
parameters.put("sublist", getUserCountList());
parameters.put("subpath", subResout.getFile().getPath());
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面2: 流程图结构：
- java程序 -> map (key: sublist, value: List<UserCount> list) -> 交报表 -> 功能1/2 -> 子报表1/2
- list -> 交报表

5) 无。
