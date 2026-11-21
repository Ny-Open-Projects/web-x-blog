# 画面线理解：07-Jdbc数据源数据填充：使用parameter为sql语句传递参数

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\07-Jdbc数据源数据填充：使用parameter为sql语句传递参数_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:51, 01:02, 01:39, 02:04, 03:09, 03:27, 04:02, 04:12, 04:17, 04:33, 04:52, 05:01, 05:14, 05:18
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:41:42

1) 这一组画面整体在讲如何在 Spring Boot 项目中集成 JasperReports，通过 Java 代码动态生成并导出带参数的用户报表 PDF。

2) 按时间顺序列出每张画面的要点：
画面1：浏览器显示 JasperReports 报表预览页面，标题为“用户列表”，展示包含 id、username、mobile、company_name、部门等字段的用户数据表格。
画面2：Jaspersoft Studio 空白界面，准备新建或打开报表项目。
画面3：Jaspersoft Studio 中打开名为 testConn.jrxml 的报表设计文件，左侧 Outline 显示报表结构，右侧 Properties 面板显示参数 cid 的配置（Name: cid, Class: java.lang.String, Default Value Expression: <NULL>）。
画面4：在 Jaspersoft Studio 中打开“Dataset and Query Dialog”窗口，设置查询语言为 SQL，字段列表显示 id、username、mobile、department、company_id、company_name 等字段，右侧 Properties 面板显示数据源 testConn 的配置（Language: java, No Data Type: <NULL>）。
画面5：在 Jaspersoft Studio 中，输入参数 cid 的值为 1，点击“Reset”按钮后，报表预览区显示筛选后的用户数据。
画面6：Jaspersoft Studio 中，报表设计界面显示“用户列表”标题，字段包括 SF([id])、SF([username])、SF([mobile])、SF([company_name])、SF([department])。
画面7：Jaspersoft Studio 中，Outline 面板显示 testConn 报表的结构，包括 Parameters、Fields、Sort Fields、Title 等。
画面8：IntelliJ IDEA 中打开 JasperController03.java 文件，代码中定义了创建 PDF 报表的方法 createPdf，通过 ClassPathResource 加载 testConn.jasper 文件，使用 JasperFillManager 填充报表并导出为 PDF。
画面9：IntelliJ IDEA 中，JasperController03.java 文件的代码中，注释“//获取企业id为1的所有用户”被选中，下方代码块中参数设置为 parameters.put("cid", "1")。
画面10：IntelliJ IDEA 中，JasperController03.java 文件的代码中，注释“//获取企业id为1的所有用户”被选中，下方代码块中参数设置为 parameters.put("cid", "1")。
画面11：IntelliJ IDEA 中，点击“Run”按钮，准备运行 JasperController03.java 文件。
画面12：IntelliJ IDEA 中，控制台显示 Spring Boot 应用启动日志，包括 Tomcat 初始化、Servlet 映射、JasperApplication 启动成功等信息。
画面13：浏览器显示 JasperReports 报表预览页面，标题为“用户列表”，展示包含 id、username、mobile、company_name、部门等字段的用户数据表格。
画面14：IntelliJ IDEA 中，Project Explorer 面板显示项目结构，包括 src/main/java/controller/JasperController03.java、resources/templates/testConn.jasper、application.yml 等文件。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面8、9、10、14 中的代码：
```java
public void createPdf(HttpServletResponse response) throws Exception {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/testConn.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.创建jasperPrint,同jasper文件中填充数据
    ServletOutputStream os = response.getOutputStream();
    Map parameters = new HashMap<>();
    //获取企业id为1的所有用户
    Connection conn = getConnection();
    JasperPrint print = JasperFillManager.fillReport(fis, parameters, conn);
    JasperExportManager.exportReportToPdfStream(print, os);
    os.flush();
}

public Connection getConnection() throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/ihrm", "root", "111111");
    return conn;
}
```

画面4 中的 SQL 查询配置：
Language: sql
Field Name: id, username, mobile, department, company_id, company_name
Class Type: java.lang.String

画面3 中的参数配置：
Parameter: cid
Name: cid
Class: java.lang.String
Description: 
Is For Prompting: 
Default Value Expression: <NULL>
Evaluation Time: 

画面6 中的报表字段配置：
SF([id])、SF([username])、SF([mobile])、SF([company_name])、SF([department])

画面14 中的目录结构：
```
src
└── main
    ├── java
    │   └── icast
    │       └── controller
    │           └── JasperController03.java
    └── resources
        ├── templates
        │   ├── test.jasper
        │   └── testConn.jasper
        └── application.yml
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面中未出现 PPT 标题、架构图/流程图或表格数据。

5) 无。
