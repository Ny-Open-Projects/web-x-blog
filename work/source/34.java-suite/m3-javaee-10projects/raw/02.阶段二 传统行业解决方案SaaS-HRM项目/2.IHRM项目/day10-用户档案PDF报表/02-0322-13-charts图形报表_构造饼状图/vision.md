# 画面线理解：13-charts图形报表：构造饼状图

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\13-charts图形报表：构造饼状图_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:13, 01:02, 02:03, 03:13, 03:41, 06:05, 06:28, 06:46, 07:19, 07:52, 09:02, 09:38, 09:56, 10:55
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:44:47

1) 这一组画面整体在讲如何在 Jaspersoft Studio 中设计一个饼图报表，并通过 Spring Boot 后端生成并预览该报表。

2) 按时间顺序列出每张画面的要点：
画面1：在 Jaspersoft Studio 中，打开名为 testCharts.jrxml 的报表文件，左侧 Outline 面板显示报表结构，右侧面板显示可拖拽的图表元素（Chart），底部 Preview 预览窗口显示空白报表。
画面2：在 Outline 面板中，展开 Fields 节点，选中 company 字段，准备用于图表数据绑定。
画面3：打开 Chart Wizard 的 Dataset 配置页，选择 Main Dataset 作为数据源，准备配置图表数据。
画面4：在 Chart Wizard 中，将 Label 设置为 $F{company}，准备配置图表标签。
画面5：将配置好的饼图元素拖拽到报表设计区域，图表元素被选中，Properties 面板显示其位置和大小属性。
画面6：切换到 IntelliJ IDEA，打开 JasperController05.java 文件，查看 Java 代码中创建报表的逻辑。
画面7：在 JasperController05.java 中，查看生成报表的代码，包括创建 JRBeanCollectionDataSource 和 JasperPrint 对象。
画面8：在 IntelliJ IDEA 中，展开项目结构，查看 domain 包下的 User 类。
画面9：在 IntelliJ IDEA 中，打开 UserCount.java 文件，查看 UserCount 类的定义。
画面10：在 IntelliJ IDEA 中，查看 UserCount 类的源码，显示其属性和方法。
画面11：在 IntelliJ IDEA 中，查看 UserCount 类的源码，显示其属性和方法。
画面12：在 IntelliJ IDEA 中，打开 JasperController05.java 文件，查看 createPdf 方法，用于生成 PDF 报表。
画面13：在浏览器中预览生成的饼图报表，显示“用户份额图形”，包含“传智播客”、“黑马程序员”、“baidu”三个部分。
画面14：在 Jaspersoft Studio 中，预览报表，显示“用户份额图形”饼图，图表元素已正确配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6代码：
```java
Map parameters = new HashMap<>();
//1.获取javaBean的数据
List<User> userList = getUserList();
//2.通过javaBean的list集合
JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userList);
JasperPrint print = JasperFillManager.fillReport(fis, parameters, ds);
JasperExportManager.exportReportToPdfStream(print, os);
```

画面7代码：
```java
public List<User> getUserList() {
    List<User> list = new ArrayList<>();
    for(int i=0;i<10;i++) {
        User user = new User(id: i, username: "itcast" + i, company: "传智播客", dept: "讲师", mobile: "1380000000" + i);
        list.add(user);
    }
    for(int i=0;i<5;i++) {
        User user = new User(id: i, username: "itboim" + i, company: "黑马程序员", dept: "讲师", mobile: "1380000000" + i);
        list.add(user);
    }
    return list;
}
```

画面8目录结构：
```
src
  main
    java
      cn.itcast
        controller
          JasperController02.java
          JasperController03.java
          JasperController04.java
          JasperController05.java
          JasperController06.java
        domain
          User.java
          UserCount.java
    resources
      templates
        test.jasper
        testCharts.jasper
        testConn.jasper
        testGroup.jasper
```

画面12代码：
```java
public void createPdf(HttpServletRequest request, HttpServletResponse response) throws Exception {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/testCharts.jasper");
    FileInputSream fis = new fileInputStream(resource.getFile());
    //2.创建jasperPrint对象
    ServletOutputStream os = response.getOutputStream();
    try {
        Map parameters = new HashMap<>();
        //1.获取javaBean的数据
        List<UserCount> userList = getUserCountList();
        //2.通过javaBean的list集合
        JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userList);
        JasperPrint print = JasperFillManager.fillReport(fis, parameters, ds);
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
