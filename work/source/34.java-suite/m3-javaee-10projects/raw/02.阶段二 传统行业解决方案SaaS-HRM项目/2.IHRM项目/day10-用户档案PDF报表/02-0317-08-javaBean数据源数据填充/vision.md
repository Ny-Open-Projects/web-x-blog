# 画面线理解：08-javaBean数据源数据填充

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\08-javaBean数据源数据填充_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 01:19, 03:22, 06:04, 07:23, 08:07, 09:27, 09:51, 10:18, 10:43, 12:02, 12:53, 13:26, 13:59
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:42:25

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 JasperReports 实现基于 JavaBean 的数据填充并生成 PDF 报表。

2) 按时间顺序列出每张画面的要点：
画面1：在 JasperReports Studio 中，讲解如何配置 JDBC 数据源，弹出的“Data Adapters Wizard”窗口中选中“Database JDBC Connection”。
画面2：在 JasperReports Studio 中，打开名为 testBean.jrxml 的报表设计文件，展示报表的结构（Title, Page Header, Column Header, Detail 1, Column Footer, Page footer）。
画面3：在 JasperReports Studio 中，选中“Field: Field_1”，属性面板显示其 Class 为 java.lang.String。
画面4：在 JasperReports Studio 中，拖拽字段到 Detail 1 区域，显示字段表达式如 $F{[id]}、$F{[username]}、$F{[mobile]}、$F{[dept]}。
画面5：在 JasperReports Studio 中，完成字段拖拽，显示报表设计界面，左侧 Outline 显示 Fields 下的 id、username、mobile、company、dept。
画面6：在 IntelliJ IDEA 中，打开 JasperController04.java 文件，展示如何通过 HttpServletResponse 返回 PDF 文件。
画面7：在 IntelliJ IDEA 中，展示项目结构，包含 src/main/java/cn/itcast/controller、src/main/java/cn/itcast/domain/User.java 等。
画面8：在 IntelliJ IDEA 中，编辑 User.java 文件，定义 User 类的私有字段：id、username、company、dept。
画面9：在 IntelliJ IDEA 中，编辑 JasperController04.java 文件，展示 try-catch 块中的异常处理，如 UnsupportedClassVersionError、IOException 等。
画面10：在 IntelliJ IDEA 中，编辑 JasperController04.java 文件，展示创建 List<User> 并循环添加数据的代码。
画面11：在 IntelliJ IDEA 中，编辑 JasperController04.java 文件，展示创建 List<User> 并循环添加数据的代码，使用 new User(...) 构造函数。
画面12：在 IntelliJ IDEA 中，编辑 JasperController04.java 文件，展示使用 JRBeanCollectionDataSource 填充数据并调用 JasperFillManager.fillReport()。
画面13：在 IntelliJ IDEA 中，编辑 JasperController04.java 文件，展示调用 JasperFillManager.fillReport() 方法时，IDE 提示选择重载方法。
画面14：在浏览器中访问 localhost:8081/testJasper4，页面显示正在等待响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
```java
package cn.itcast.controller;
import org.springframework.web.bind.annotation.*;
@RestController
public class JasperController04 {
    @GetMapping("/testJasper4")
    public void createReport(HttpServletRequest request, HttpServletResponse response) throws Exception {
        //1.引入jasper文件
        Resource resource = new ClassPathResource("templates/testConn.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        //2.创建输出流，把jasper文件中动态数据写入到输出流中
        ServletOutputStream os = response.getOutputStream();
        try {
            Map parameters = new HashMap<>();
            //3.获取数据库的连接
            Connection conn = getConnection();
            JasperPrint print = JasperFillManager.fillReport(fis, parameters, conn);
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException e) {
            e.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

画面7：
```
src
└── main
    ├── java
    │   └── cn
    │       └── itcast
    │           ├── controller
    │           │   └── JasperController04.java
    │           └── domain
    │               └── User.java
    └── resources
        ├── templates
        │   ├── testBean.jasper
        │   ├── testConn.jasper
        │   └── testProm.jasper
        └── application.yml
```

画面8：
```java
package cn.itcast.domain;
public class User {
    private String id;
    private String username;
    private String company;
    private String dept;
    private String mobile;
}
```

画面9：
```java
try {
    //...
} catch (Exception e) {
    e.printStackTrace();
}
```

画面10：
```java
public List<User> getUserList() {
    List<User> userlist = new ArrayList<>();
    for(int i=0;i<10;i++) {
        //...
    }
    return userlist;
}
```

画面11：
```java
public List<User> getUserList() {
    List<User> userlist = new ArrayList<>();
    for(int i=0;i<10;i++) {
        User user = new User();
        user.setId("id" + i);
        user.setUsername("用户名" + i);
        user.setCompany("公司" + i);
        user.setDept("部门" + i);
        user.setMobile("1380000000" + i);
        userlist.add(user);
    }
    return userlist;
}
```

画面12：
```java
//1.4）jasper文件
Resource resource = new ClassPathResource("templates/testConn.jasper");
FileInputStream fis = new FileInputStream(resource.getFile());
//2.创建输出流，把jasper文件中动态数据写入到输出流中
ServletOutputStream os = response.getOutputStream();
try {
    Map parameters = new HashMap<>();
    //1.获取javaBean的list集合
    List<User> userlist = getUserList();
    //2.通过list集合创建javaBean的数据填充对象
    JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userlist);
    JasperPrint print = JasperFillManager.fillReport(fis, parameters, ds);
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

画面13：
```java
//1.4）jasper文件
Resource resource = new ClassPathResource("templates/testConn.jasper");
FileInputStream fis = new FileInputStream(resource.getFile());
//2.创建输出流，把jasper文件中动态数据写入到输出流中
ServletOutputStream os = response.getOutputStream();
try {
    Map parameters = new HashMap<>();
    //1.获取javaBean的list集合
    List<User> userlist = getUserList();
    //2.通过list集合创建javaBean的数据填充对象
    JRBeanCollectionDataSource ds = new JRBeanCollectionDataSource(userlist);
    JasperPrint print = JasperFillManager.fillReport(fis, parameters, ds);
    JasperExportManager.exportReportToPdfStream(print, os);
} catch (JRException e) {
    e.printStackTrace();
} finally {
    os.flush();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：PPT 标题为“1.2 数据源填充数据”，子标题“1.2.1 JDBC数据源”，子子标题“1.2.1.1 配置数据连接”，文字说明“使用JasperReports Studio 先配置一个数据库连接”，并提示“填写数据源的类型，选择”Database JDBC Connection“”。

5) 无。
