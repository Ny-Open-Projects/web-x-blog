# 07-Jdbc数据源数据填充：使用parameter为sql语句传递参数

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\07-Jdbc数据源数据填充：使用parameter为sql语句传递参数_【海量资源尽在 ubkz.com】.mp4
- 时长 5分27秒（音频 327s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那各位来看目前呢我们已经实现了这个用户列表的一个PDF的一个打印但是还有一些细节问题需要我们去完成它那首先这个问题是这样的就是说我们这个SaaS人力管理系统当中用户表里面是各个企业里面的所有的用户那可以有这么一个需求不同的用户我只打印不同的企业我只打印我当前企业当中的所有用户其实就可以了那我现在是不是打印的是全部啊各位
[00:32] 所以我们接下来要做的就是可不可以往这个连接当中动态的传递一个参数动态的去构造sql动态的给我展示出查询结果而不是查询全部那这个我们如何去做呢好了这个时候其实就需要结合我们的connection需要去结合我们的parameter参数两个结合去使用
[01:00] 好了我们首先回到死丢丢部分在死丢丢部分当中先去构造一个参数Parameters那这个参数呢刚才说过了它其实是整个的所有参数当然了除了所有参数之外它也可以给你查询的Circle语句传递的一些数据那这个Parameter呢我们可以自己定义一个右键创建一个Parameter
[01:25] 好了这个Parameter呢我可以给它起一个名字当然这个名字你随便起一会Map集合里面跟它能够对应上就可以了比如说我叫CID代表的是Company ID应该能理解吧那对于Company ID呢回到这边它是一个死菌类型的可以给它一点点我们的基本说明比如说就是企业IDOK那好了接下来我们刚才的写的语句应该如何去处理从哪找语句注意
[01:54] 回到我们这个outline找到testconnect右键还是跟刚才一样dataset and query好了各位耐心等待一点它有点慢好了这边呢各位发现我们刚才执行的是selectionfrom bs下滑线user那这回我要加条件where那where我们以哪个条件进行查询呢各位我们关注的是这个里面的抱歉bsuser这里面的
[02:25] 叫做company id所以我要写company下划线id等于好了后面这个如何去写这个就相对来说有一点点麻烦了是因为我们要用到parameter里面的数据那用到parameter的数据刚才简单的说过它的语法到这p大括号好了我们刚才写了一个cid没错吧ok那这样一来我这个语句进行一个更新即可
[02:55] 好了语句我们更新好了同样再去preview一下走好了这回你就会发现它让我要输入一个PID了那这PID我要查询其ID为1的走你发现这一回查询的全部都是其ID为1的我们可以打开浏览器对比一下少了一条CGX没错吧好了
[03:19] 那这样一来其实我们已经把这个模板制作好了这个模板呢需要各位注意的是我们刚才一共完成了这么两个操作第一个操作由于我sql里面需要参数这个参数需要传递所以我写到parameters里面那parameters除了能够写到一些我们比如说呢对象的一些属性之外还可以对咱们模板当中用到的任意参数进行说明比如说现在我用到的是一个条件所以我设置了一个条件好了那
[03:48] 这个条件构造好了之后接下来右键去对我们刚才这个语句进行一个更新操作好了这边用的是一个$P大括号这种形式去拿到参数里面的内容好了就干这么两件事我们把这个写好了之后再去右键编译一下ConnectOK编译好了之后把它Ctrl C拿到Java代码部分进行覆盖TimeLite进行覆盖
[04:15] 好了那接下来在Java代码里面如果说我只想要去查询企业ID唯一的用户企业ID唯一的所有用户那这个时候我们就不得不接触Parameters那这边Parameters打点Put还记着刚才说过了Parameters传递你那边用到什么Name这边的Key就应该用什么那我这边传递一个1进去
[04:47] 即可OK好了我这边已经改造好了我们可以重新启动一下这个微服再去回到我们的浏览器右键刷新来看一下是否能够查询1的所有数据这边还没启动成功刷新一把各位会发现少了一条我们现在只关注的是ID为1的所有用户这个其实就是和各位简单的来说了一下第一个Connection
[05:18] 这个连接确实可以填充数据第二个就是配合上Parameters为我们的Circle传递参数OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面14：IntelliJ IDEA 中，Project Explorer 面板显示项目结构，包括 src/main/java/Controller/JasperController03.java、resources/templates/testConn.jasper、application.yml 等文件。

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
    │       └── Controller
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

