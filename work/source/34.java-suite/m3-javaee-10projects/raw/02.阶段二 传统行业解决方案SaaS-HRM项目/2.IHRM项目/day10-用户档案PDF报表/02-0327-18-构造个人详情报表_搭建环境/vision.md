# 画面线理解：18-构造个人详情报表：搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\18-构造个人详情报表：搭建环境_【海量资源尽在 ubkz.com】.mp4
- 抽帧：13 帧 @ 00:11, 00:56, 02:20, 02:37, 02:50, 03:06, 03:33, 03:54, 04:11, 04:38, 05:01, 05:16, 05:29
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 15:48:00

1) 这一组画面整体在讲如何在 Java 后端通过 JasperReports 生成并返回员工个人资料的 PDF 报表。

2) 按时间顺序列出每张画面的要点：
画面1：展示一个空白的 Word 文档，内容为“员工的个人档案：下载员工的pdf详情资料”，用于说明最终用户下载 PDF 的场景。
画面2：展示 JasperReports Studio 的设计界面，正在编辑一个名为“testBean.jrxml”的报表，其中包含“姓名”、“电话”、“学历”、“毕业院校”、“工作信息”等字段，以及一个“Image”元素，其“Expression”设置为“$P{staffPhoto}”，用于显示员工照片。
画面3：展示 IntelliJ IDEA 中的项目结构，当前选中的是“ihm_parent”模块，显示了项目包含的多个子模块，如“ihm_common”、“ihm_company”、“ihm_employee”等。
画面4：展示“ihm_parent”模块下的“pom.xml”文件内容，其中包含对“org.apache.poi”和“com.qiniu.qiniu-java-sdk”的依赖配置，以及一个名为“Spring Snapshots”的仓库配置。
画面5：展示 IntelliJ IDEA 中的项目结构，当前选中的是“pom.xml”文件。
画面6：展示“EmployeeController.java”文件内容，其中定义了一个用于保存员工个人信息的 PUT 请求映射方法“savePersonalInfo”，并注释了“打印员工pdf报表”。
画面7：在“EmployeeController.java”文件中，光标位于“@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)”方法的注释上方，该方法用于生成并返回 PDF 报表。
画面8：在“EmployeeController.java”文件中，光标位于“public void pdf() {”方法的开头，该方法用于生成并返回 PDF 报表。
画面9：在“EmployeeController.java”文件中，光标位于“Resource resource = new ClassPathResource("templates/test.jasper");”语句后，该语句用于加载报表模板文件。
画面10：在“EmployeeController.java”文件中，光标位于“JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());”语句后，该语句用于填充报表数据并生成 PDF。
画面11：在“EmployeeController.java”文件中，光标位于“JasperExportManager.exportReportToPdfStream(print, os);”语句后，该语句用于将生成的 PDF 输出到响应流中。
画面12：展示 Windows 资源管理器中“ihm”文件夹下的“day10”子文件夹，其中包含多个开发工具的窗口截图，如“Jaspersoft Studio”、“SaaS-HRM-第10章.pptx”、“Log4jconfig”、“editorconfig”等。
画面13：在“EmployeeController.java”文件中，光标位于“JasperExportManager.exportReportToPdfStream(print, os);”语句后，该语句用于将生成的 PDF 输出到响应流中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面4 的 pom.xml 内容：
```xml
<dependencies>
    <dependency>
        <groupId>org.apache.poi</groupId>
        <artifactId>poi-ooxml</artifactId>
        <version>4.0.1</version>
    </dependency>
    <dependency>
        <groupId>org.apache.poi</groupId>
        <artifactId>poi-ooxml-schemas</artifactId>
        <version>4.0.1</version>
    </dependency>
    <dependency>
        <groupId>com.qiniu</groupId>
        <artifactId>qiniu-java-sdk</artifactId>
        <version>[7.2.0, 7.2.00]</version>
    </dependency>
</dependencies>

<repositories>
    <repository>
        <id>spring-snapshots</id>
        <name>Spring Snapshots</name>
        <url>https://repo.spring.io/snapshot</url>
        <snapshots>
            <enabled>true</enabled>
        </snapshots>
    </repository>
</repositories>
```

画面6 的 EmployeeController.java 内容：
```java
@autowired
private UserCompanyJobsService userCompanyJobsService;
@autowired
private ResignationService resignationService;
@autowired
private TransferPositionService transferPositionService;
@autowired
private PositiveService positiveService;
@autowired
private ArchiveService archiveService;

/**
 * 为员工信息保存
 */
@RequestMapping(value = "/{id}/personalInfo", method = RequestMethod.PUT)
public Result savePersonalInfo(@PathVariable(name = "id") String uid, @RequestBody Map map) throws Exception {
    UserCompanyPersonal sourceInfo = BeanMapUtils.mapToBean(map, UserCompanyPersonal.class);
    if (sourceInfo == null) {
        sourceInfo = new UserCompanyPersonal();
    }
    sourceInfo.setUserId(uid);
    sourceInfo.setCompanyId(super.companyId);
    userCompanyPersonalService.save(sourceInfo);
    return new Result(ResultCode.SUCCESS);
}
```

画面7 的 EmployeeController.java 内容：
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() {
```

画面8 的 EmployeeController.java 内容：
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() {
```

画面9 的 EmployeeController.java 内容：
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/test.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());
```

画面10 的 EmployeeController.java 内容：
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/test.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());

    //2.构造数据
    ServletOutputStream os = response.getOutputStream();

    try {
        JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面11 的 EmployeeController.java 内容：
```java
/**
 * 打印员工pdf报表
 */
@RequestMapping(value = "/{id}/pdf", method = RequestMethod.GET)
public void pdf() throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/test.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());

    //2.构造数据
    ServletOutputStream os = response.getOutputStream();

    try {
        JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException e) {
        e.printStackTrace();
    } finally {
        os.flush();
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面12：展示 Windows 资源管理器中“ihm”文件夹下的“day10”子文件夹，其中包含多个开发工具的窗口截图，如“Jaspersoft Studio”、“SaaS-HRM-第10章.pptx”、“Log4jconfig”、“editorconfig”等。未出现 PPT 标题、架构图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
