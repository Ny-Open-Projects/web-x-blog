# 18-构造个人详情报表：搭建环境

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\18-构造个人详情报表：搭建环境_【海量资源尽在 ubkz.com】.mp4
- 时长 6分31秒（音频 391s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的和各位对需求上面的问题做了一个介绍那接下来呢我们说过了要想完成PDF的这么一个制作我们关注的点呢一共是三点第一个点呢就是我们的模板好了第二个点呢就是我们的数据来源好了第三个点呢就是天充数据这是我们重点关注的点
[00:23] 那我们的模板呢在今天资料已经给各位准备好了刚才也跟各位做过一个简单的介绍其实这个模板里面呢咱们全部都是基于parameter的形式去构造这些数据的那这边呢有一张图片呢简单的和各位说一下这张图片从哪获取到的怎么加上来的其实比较简单来看这边有一个影媚制随便拖一个影媚制进来之后这边呢你可以是workspace等等随便写那接下来添加好了图片之后你呢
[00:52] 鼠标左键点击一下这个image那在property它的属性部分这边会看到有一个表达式那这个表达式我也是$P大括号的形式是不是也是一个Parameter参数啊所以这玩意儿我要传递到我当前的这个模板当中那传递的是什么就是我们用户头像的UIL地址能理解吧那它自动的就会把这个图片给我下载到我们的模板当中了
[01:17] OK好了这个模板呢咱们已经构造好了那接下来关注的就是第二点数据来源那数据来源从哪来那我们在页面部分发送请求是不是应该把当前这个用用户的ID比如这ID传递到我们的一个控制器方法里那在控制器方法里面根据ID是不是去查他的个人信息当然了这边呢还有他的岗位信息是不是全部都查询出来啊也就是说我们接下来第二件事就是构造一个构造
[01:47] 我们的方法根据ID查询我们的用户和岗位信息那查询到了之后把这些查询好的数据封装到MAP集合参数中然后是不是再去生成就可以了所以我们要做的事情一共有这么几步第一件事已经搞定了接着我们关注第二件事
[02:12] OK那首先呢我们需要构造一个Controller方法接收请求也就是我们需要写一个接口那这个接口写到哪呢其实都可以当然了我把它写到我们的员工微服务当中了那在写员工微服务之前首先呢我们这边是一个咱们这个HRM工程那这个工程里面是不是还没有相应的这个坐标啊也就是我们PDF相关的坐标所以呢我先把坐标呢也给它拷过来
[02:39] 那在我们之前写案例的工程当中呢把这个坐标需要的Ctrl Ccall到这边Ctrl VOK call过来之后不管了那接着打开我们的员工微服务在ControllerEployeeController这边我就写到最上方了打印员工PDF报表OK那好了我写一个请求方法atRequestMappingValue等于
[03:14] OK那我这边请求的呢首先来ID那接着后面呢咱们就可以来一个PDF就是根据ID去打印他的PDF信息了当然了我这边可以给他来一个MES等于注意我这边呢就用GET的形式进行请求其实就可以了因为不涉及到特别复杂的数据才传入传出OKPublic注意我们现在其实就是对于报表的一个显示和一个下载所以我的返回值呢就是VUID了PDF
[03:47] OK那接着这个方法里面的参数呢咱们其实也写过很多遍了并且这个方法都比较简单咱们直接从我们之前学的这个很多的案例当中把基本的方法内容抠过来就可以了随便来一个那需要request需要response那接着里面要做的事情引入Jadper文件OK那引入Jadper文件接下来第二件事我们说过了需要去查询需要构造构造
[04:20] 数据好了接着第三件事填充那填充的代码呢基本上都差不多填充pdf模板数据并输出pdf这代码呢相对来说都比较简单都不难OK那在这边呢有一些异常呢我也处理一下OK那好了接下来这些基本的注释呢咱们都删掉了都删掉了OK
[04:54] 那接下来呢我们关注的点呢就是第一个要引入JASPER文件那这个JASPER文件我习惯在Spring Boot当中呢给它放到了resource这个目录下了好了resource我去创建一个叫做temp-litz的一个文件夹那接下来把我今天资料给各位准备好的模板Ctrl-C拷过来Ctrl-V已经拷贝过来了
[05:21] OK copy过来了之后那这边呢我加载的就是我call一下这个名称我怕写错OK那这样一来文件引入进来了构造数据的事情我们一会儿再说一会儿再说但是但是我一会儿要把数据是不是应该转化成我叫做一个parameter的一个参数啊所以在这边呢我把这个parameter呢单独的给它拿出来就叫P-A-R-A-M-S吧等于new一个
[05:57] 哈希MapOK接着拿过来OK那这样一来呢其实我整个这个代码的一个结构就已经写好了那有的朋友会说我这个FillReport的时候这边怎么传那个JREmptyDataSource为什么不传比如说Connection为什么不传JavaBean集合它是这样的是因为我们这边是不是全部都是用Parameters传递数据那后面这个我们都没用咱们也不是构造列表所以我就这样写
[06:28] 各位能接受吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

