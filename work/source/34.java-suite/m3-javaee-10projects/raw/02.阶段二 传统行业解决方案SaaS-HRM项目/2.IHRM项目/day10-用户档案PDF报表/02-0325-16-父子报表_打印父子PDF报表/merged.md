# 16-父子报表：打印父子PDF报表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\16-父子报表：打印父子PDF报表_【海量资源尽在 ubkz.com】.mp4
- 时长 8分4秒（音频 484s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们把负子报表传递数据的这一个部分呢其实也已经解决了那接下来呢还有一个问题那最后一个问题是这样的在我的Java代码当中注意在我的Java代码当中我其实是通过Java代码只能找到负报表那负报表里面现在并没有子报表所有的内容所以我应该想办法以Java代码在Java代码当中告诉负报表你去引用的子报表的一个路径或者它的地址究竟在什么地方
[00:31] 那所以我这边map集合里面还需要传递一个key还需要传递一个值这个key现在代表的是比如说呢就叫做subpass就是我子报表代表的路径那value其实代表的就是我子报表的叫做路径地址OK那接下来我们回到studio所以我这边呢需要再去创建一个parametersub就叫passOKclass类型没问题
[01:06] 那接下来呢我们关注的就是说刚才在studio当中各位能够看到这个是我拖过来的一个已经存在的报表但是你如果放到Java程序当中就未必了那针对这种情况怎么办呢诶注意看这边有一个impression这个impression指的是子报表这个路径那现在子报表路径我们以参数的形式传递过来了那所以在这边我要写表达式$P代表的是parameter那中间关注的
[01:37] 是不是就应该是刚才写好的叫做sabo pass没错吧OK那这样一来我整个的这个报表其实全部都已经搞定了那这个报表我们写好了之后接下来呢就需要把咱们涉及到的副报表meng01进行一个编译那接下来把需要的子报表叫做test chart编译吧把这边编译的时候出错了各位来看双吉他
[02:13] 其实这个错误呢这边problem里面已经有显示了其实说的也比较简单我们可以打开看一下基本上出现什么bound area这个基本上就是它站在这个边框有点太多了因为刚才做过一个调整左右调一下或者调一下这个bound的它长宽就可以了OK这回呢再保存一下再去进行一个编译OK那这样一来主要的复报表编译好了
[02:44] 还有我们的一个子报表都编译好了Ctrl C把这两个报表全部call到我们templates目录下call过来了好了全部都copy过来之后接下来我们就开始写一个程序去运行起来看一下能不能把父子报表的数据全部都拼接到一起Ctrl C Ctrl Vcopy份工程07好了在这个工程里面我首先主要读取的其实就是父报表的内容meng01meng01
[03:24] 接下来这里面的代码先拿过来都删掉都删掉OK接下来我这里面的代码应该如何去写别忘了我们传递给副报表的时候需要设置一些它的基本参数这个参数有两方面第一个子报表的路径这是第一个第二个参数是我们子报表需要的数据没错接下来我们就开始parameter打点put
[04:04] 那子报表的路径回来子报的路径呢叫做subpasssubpassctrlc这边拷过来还有一个呢就是子报表的一个叫做subpass一个叫做sublist这个太热口了OK那接着这个subpass代表的是子报表的路径好了这个代表的是子报表需要的数据那子报表需要的数据比较简单直接getusercountlist就可以
[04:46] OK那子报表的路径那子报表路径现在是不是只有在我们的Java程序当中才能拿到这个test charts所以对于我们来说呢也需要做一个配置其实比较简单如何获取呢resource这边呢就来个sub resource就是去获取一下当前这个子报表它的路径那这个子报表叫什么名字test charts靠一下名字copy过来那接下来
[05:20] 如何获取它的路径比较简单直接通过subresource打点get fill打点get pass就能得到当前这个子报表它的一个路径了OK那这样一来我们这个传递的参数都已经复制到parameter里面了所以parameter拿过来那接着我们这回数据其实就没有了就new一个叫做jrempty data source就可以
[05:49] OK那这样一来我这个代码呢其实也已经写好了这边改成7我们现在测试的就是复子报表OK重新启动一下当前这个工程这边让它去重启我切换到浏览器好了现在访问的是第七个接口点击回车各位来看现在呢其实已经进入到我们刚才这个报表当中了只不过现在显示的还是不太理想那接着呢简单的对它进行一个调整其实就可以了
[06:21] 好了回到我们刚才写的父子报表这边首先不太理想的点第一个就是上边的这个标题那中文没有显示设置一下中文华文送体那这边呢可以给他来一个12号字就可以了那接下来就是说那我现在这一块你会他他的这个用户份额这张图啊是在太右边了没错吧他为什么会有这样一个设计呢是因为对于我们这个报表而言子报表
[06:51] 在副报表里占的位置首先在左边这是一个空格一大块那接下来你看子报表这边是不是前面又有一大块所以你加上这个空格的话其实就代表的比较多了那针对这种情况我们可以把它放到最前边放到最前边OK那这边保存一下我们接下来呢就是把这两个报表同时再给它进行一个编译拿到我们的表格当中右键编译吧
[07:29] 好了闷右键编译好了编译好了之后把这个Ctrl C和这个图表Ctrl C两个全部都拿过来放到我们的Java代码程序当中Ctrl VOK全部覆盖那再去重新启动一把回到浏览器来F5刷新看一下效果好了那这样一来其实我们是不是就已经完成了父子报表的这种形式填充过来了一个子报表的一个图形
[08:02] OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

