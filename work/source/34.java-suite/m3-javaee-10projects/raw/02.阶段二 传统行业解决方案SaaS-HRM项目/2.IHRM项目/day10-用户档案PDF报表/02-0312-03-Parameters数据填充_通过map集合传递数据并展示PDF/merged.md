# 03-Parameters数据填充：通过map集合传递数据并展示PDF

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\03-Parameters数据填充：通过map集合传递数据并展示PDF_【海量资源尽在 ubkz.com】.mp4
- 时长 5分35秒（音频 335s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 现在已经可以生成了这么一个PDF的预览的报表接下来我们要完成的事情就是通过当前的模板把它导入到Java代码里面通过Java代码的形式构造一个PDF报表的一个下载这么一个功能我们应该要如何去做其实各位应该也还有印象
[00:20] 那这是一个XML的这么一个模板的一个文件我们需要对它进行编译生成.Jasper文件只有在Jasper文件才可以以二进机的形式为里面的数据进行真实的填充没错吧所以我们要做的事情首先第一件事编译那编译呢在这边右键当前的模板继续往下找找到completereport好了接下来编译好了.Jasper那我们可以把它Ctrl Ccall到我们的Java工程当中
[00:50] 那这个Java工程呢我就沿用我们昨天自己搭建的这么一个Spring Boot环境那我习惯呢把一个模板放到了Template下OKCtrl Vcall过来那call过来之后接下来我们进行访问那访问的时候其实访问的是某一个Controller这个里面那访问到Controller那这个Controller呢我就重新写一个从之前这边Ctrl C Ctrl Vcall一个就叫做02
[01:17] 这个里面的代码呢其实跟之前的内容都是大同小异的我把这个注释呢简单的删一下调整一下首先呢第一件事需要引入JASPER文件那我们这个JASPER文件刚才呢大家也看过它叫做testparam.jasper好了我把这个文件名称Ctrl C拷到这边Ctrl VOK那引入进来之后接下来咱们就开始着手需要往这个里面填充数据了
[01:48] 那我们现在测试的是基于parameter map的形式填充数据基于parameter是以map的形式填充数据OK那好了接下来呢我们这里面如何去构造呢各位还是调用fillreport的方法这个report方法这个第二个参数呢我就不能写一个空的map了我要往里面去构造数据了map
[02:28] 就叫parameters等于new一个hashimap好了里面要存的值注意里面设置设置参数那这个参数参数的key必须要等于必须要等于我们刚才在studio里面构造的这个parameter它的名称我们刚才构造了三个构造了四个
[02:54] 这四个其中第一个名称叫Uder Name第二个是不是叫Mobile Company以及DPT所以各位一定一定要注意你往里面要传值的时候Map那这个Map的Parameter里面的Key一定要等于我们模板中使用的Parameter参数的Name必须要等于那好了接下来我们开始往里面设置Parameter打点Put
[03:23] 那put的值呢首先第一个我们刚才写了一个user name那比如说我现在往里填充的举个例子就填充一张三了还有parameter打点往里去put那这回put的是什么呢我就来一个mobile那这个mobile呢我就来120了继续打点put那我们还存了一个叫做dept部门就是讲师还有打点put一共四个参数嘛company c-o-m-p-a-n-y
[04:00] 所属企业就是传之博客OK那这样一来我们这个parameter也构造好了把它传入到第二参数即可注意我们现在是基于parameter也就是以map集合的形式传参那后面这个数据的数据源还是以空数据源使用就可以了OK那这样一来我当前的这个案例呢Java代码已经写好了当然了我需要改造一下我请求的这个路径那这个我们改造好了之后可以
[04:29] 启动一下我们当前的这个微服务好了启动一下好了这边微服务让他去启动我呢需要去打开我的浏览器那我们当前的这个微服务的请求路径localhost我叫81818181好了现在访问的是叫做2走
[05:04] Test Jasper2那各位来看现在已经进入到了我们的PDF界面并且已经把箱的数据给我构造出来比如说用户名张三手机号120等等这些是不是就是通过我Java代码的形式把一个数据传入到了我的PDF模板当中进行数据填充并且展示所以咱们第一种方式以Map传递参数的形式是不是相对来说也是比较简单的
[05:33] OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

