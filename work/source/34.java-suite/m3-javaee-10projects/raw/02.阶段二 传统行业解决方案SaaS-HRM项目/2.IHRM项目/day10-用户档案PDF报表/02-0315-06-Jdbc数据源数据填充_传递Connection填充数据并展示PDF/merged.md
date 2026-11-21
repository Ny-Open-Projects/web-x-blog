# 06-Jdbc数据源数据填充：传递Connection填充数据并展示PDF

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\06-Jdbc数据源数据填充：传递Connection填充数据并展示PDF_【海量资源尽在 ubkz.com】.mp4
- 时长 11分10秒（音频 671s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那现在呢我们已经把所有的fields全部都构造出来了剩下的事情就比较简单了我们要做的事情就是搞这么一行出来把你所需要填充的内容给它拖拙过来其实就可以了那接下来我们一个一个来看比如说呢在这个detail部分我们要去创建报表创建报表要用到哪些属性用到哪些字段你就从这边从fields往里拖其实就可以了比如说我要用到ID
[00:32] 好了拖过来一个ID那除了ID之外呢比如说我还要用到其他的NameUserName也拖拽过来那我先拖拽过来一会儿呢再做一个简单的删除就可以了那除了UserName之外呢我还要用到Mobile还要用到CompanyName以及DepartmentName就需要这些那不知道各位有没有发现啊就是我一拖拽过来的时候呢这边生成了两个看到了吧我把这个最大化也稍微放大一点各位来看
[01:05] 那不仅有一个叫做Uder Name还有一个Uder Name各位这俩玩意儿它不一样它不一样那这俩玩意儿它代表的什么含义来各位来看左边其实生成的是一个来看是不是一个Static叫Test这什么意思这个是一个静态的文本也就是说这玩意儿其实相当于是一个Label标签或者相当于对这玩意儿的字段名做了一个说明也就是说你如果这样写的话它其实构造的内容
[01:34] 最后最终打印的效果其实就是user nameOK后面张三也就是说前面会把这个字段名称给你罗料到这边没错吧OK接下来就是说这些静态的我们不需要我们只要里面的数据其实就够了OK当然了我们如何删点其实可以像我这边一样定位到一个进行删除如果说有朋友说太多了删起来太麻烦也有很好的方式如何去做我们把所有内容放到了detail这个班子下
[02:07] 那我们就可以找到detail这个band在这个detail band里面你会发现这个呢static teststatic teststatic那把这些static一个一个的删掉其实就可以了定位到鼠标勾选到之后点击delete把它删掉即可OK那这样一来我已经把这些多余的static的文件给它删掉了那剩下的事情就是做一个基本的排版OK拿过来拿过来
[02:42] 好了往右边稍微拖一点点就做一个基本对齐那当然上面这个也可以对它进行一个适当的位置修改好了那我们现在把这个模板已经做的差不多了还是跟之前一样把涉及到的可能存在中文的这些内容给它做一个基本样式的一个修改设置一下我们资本的字体比如说华文宋体这边可以给它一个字体的大小当然了还可以对它进行水平居中垂直居中等等
[03:13] OK那剩下的事情呢就是说呢这个玩意儿要想让它好看一点其实可以构造一些就是包等也就是构造它的边框那这个边框呢跟刚才处理起来是一模一样的把所有涉及到的这些全部给它选起来选中之后找到包等那还是跟刚才一样填充四周都有的包等然后呢对它这个包等的自己打小做一个设置改成1.5好了点击保存那保存好了之后
[03:41] 我们就可以完成预览那预览如何去做preview走好了那这样一来各位会发现啊我预览了之后呢它的数据格式呢已经出来了并且呢数据也已经查明出来了但是各位会发现我整个的这个数据打印好像跟我们推测的就不太一样了就不太类似了没错吧那为什么有这样一个效果我们需要做一个简单的说明是这样的我找到设计部分
[04:12] 注意再去找到detail那这个detail里面各位会发现我的右边找到它的properties那这边会有一个hat的一个声明这个是不是就是一个高度啊那这个高度代表什么含义它代表的其实可以理解为一条数据代表的总高度一条数据代表的总高度所以你会发现我这边预览的数据的时候它会有很多内容但是它外面
[04:42] 怎么不管怎么去进行设置不管是怎么去进行展现都是我们设置所决定的我们刚才设置了一个要展示125一个要展示125像素是不是有点高啊所以对于我们而言最好的方式把他们并排的展示出来那怎么做回到我们的设计部分好了把这个hat做一个修改那有的朋友说这个高度应该配置多高合适和我们
[05:08] 每一个字段里面的高度给它匹配上就可以了比如说这边我定位到其中一个右边看查找一下它当前的size宽度100高度是不是叫30所以我把这个detail也给它改成30好了接着把这些所有内容慢慢的向上移全部都移到detail部分保存一下preview预览
[05:42] 那各位这回来看生成的格式是不是就变成比较理想了OK那现在呢已经生成好了这么一个报表那这个报表我们都知道了是在这个Studio里面借助它内置的或者模拟出来的一个数据源帮助我们构造的那接下来呢我们是不是真正的要在渣滑代码里面去使用啊所以我们要做的事情右键编译编译好了之后Ctrl C拖拽到我们的工程当中
[06:10] 还是跟之前一样一个项目拖拽到它的resource templates里面control v搞过来放过来之后同样的跟之前的道理是一样的control c control v模拟一个Controller在Controller里面我们想办法去填充数据模板在Java大版里面首先我们现在是基于JDBC数据源的形式形式填充数据OK好了这边做一个基本的修改
[06:46] 三那里面的代码基本上都是差不多的只不过现在我们这个parameter里面没有任何的参数了没错吧那接着后面也不用什么JRempty Data Source了我们现在缺少的是一个叫做数据库连接所以接下来我写一个简单的方法PublicConnection我叫做GetConnection叫GetConnection
[07:16] 那我们去构造一个数据库连接我为了不抱错先写一个None好了那接下来我里面就可以获取数据库连接好了ConnectionC-O-N-N等于GetConnection得到了那接下来就是说对于这个FillReport的方法里面第一个参数我们的Jasper二进制数据流第二个是我们的ParameterMap参数那第三个是我们的数据
[07:48] 数据源链接这个数据链接它直接可以接受一个connection传递过去其实也可以好了这个代码我们抱歉是点错了这个代码我们已经写好了剩下就是关注构造一个connection这个就比较简单了connecdconnectionconn等于driver managerdriver d r iv e r manager打点叫做getconnection注意这回connection其实就可以
[08:18] 用你当前数据库的连接地址也可以用你其他数据库连接地址只要能够找到刚才我们处理的表是不是就可以啊OK好了那接下来呢里面可以填写我们的UIL接着可以填写我的用户名好了可以填写我数据库密码123456好了这个UIL地址呢也比较简单jdbc冒号mycircle冒号杠杠localhostihmOK
[08:49] 那当然了我们这边呢还需要进行一个class.forname.forname.ess好了我们里面写的其实就是驱动了这个比较简单com.mycircle.jdbc.driver底下把connection返回即可当然了这边会有一些基本的异常我处理一下
[09:21] 我这个异常处理的其实有一点点简单粗暴主要是为了稍微快一点演示那对于各位来说肯定是以Tricash形式包裹上自己去处理异常那代码我们写好了代码我们写好了这边呢也需要去解决一下异常这边IO来一个最大的当然了我们现在是让它读取TestConN这个模板没错吧Con这个模板我习惯call一下这个模板名称防止它出错Ctrl Ccall到这边
[09:55] Ctrl-AOK接下来我们就可以运行一把一起来看一下效果了重新启动这边让它去启动我们打开浏览器这回访问的TestJasper3回车各位来看一下效果这边没有出来我们来看一下是不是哪有问题回到代码这边确实出了一个问题各位一起来看一下这边告我一个Unknown HostLocal Host
[10:30] 我们来看一下好了回到这边呢我们关注的其实就是连接的部分了他告诉我主机名有问题JDBC my circle哦抱歉这边是localhost这个问题太原始了太低级了好了这边继续重启然后回到我们的浏览器我们可以再来刷新一下看一下数据是否查明出来了走好了现在呢PDF报表已经给我们展示出来了那各位其实也看到了就目前而言
[11:02] 所有的数据已经和我们刚才制作模板预览其实是一模一样的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中使用 JasperReports 实现带参数的数据库报表导出功能，包括报表设计、参数传递和数据库连接配置。

2) 按时间顺序列出每张画面的要点：
画面1：在 JasperReports Studio 中打开名为 testConn.jrxml 的报表文件，设计界面显示“用户列表”标题和 Detail 1 区域，左侧 Outline 显示字段如 id, username, mobile, company_name, department_name。
画面2：在报表设计界面中，拖拽并放置了多个 Static Text 元素，分别显示 SF(id), SF(username), SF(mobile), SF(company_name), SF(department_name)，并调整了其中一个元素的位置和大小。
画面3：报表设计界面显示了完整的表格布局，包含“用户列表”标题和五个字段的静态文本框，布局为 Free Layout。
画面4：在 Detail 1 带中，调整了布局高度为 125px，Split Type 设置为 Stretch。
画面5：在 Detail 1 带中，将 Layouts 设置为 Free Layout，Height 设置为 125px，Split Type 设置为 Stretch。
画面6：在 IntelliJ IDEA 中，查看 JasperController02.java 文件，代码中使用 HashMap 设置参数并调用 JasperFillManager.fillReport() 方法。
画面7：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中使用 HashMap 设置参数并调用 JasperFillManager.fillReport() 方法。
画面8：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中添加了 public Connection getConnection() 方法的声明。
画面9：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中在 getConnection() 方法中使用 DriverManager.getConnection() 方法。
画面10：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中在 getConnection() 方法中使用 Class.forName("com.mysql.jdbc.Driver")。
画面11：在 IntelliJ IDEA 中，查看 JasperController03.java 文件，代码中在 getConnection() 方法中使用 DriverManager.getConnection("jdbc:mysql://localhost/lhrm", "root", "111111")。
画面12：在 IntelliJ IDEA 中，查看项目结构，显示 testConn.jasper 文件位于 templates 目录下。
画面13：在 IntelliJ IDEA 中，查看控制台输出，显示 Tomcat 启动日志和一个错误：Cannot render error page for request。
画面14：在浏览器中，显示生成的 PDF 报表，标题为“用户列表”，包含用户 ID、姓名、部门等字段的数据。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6：
```java
@GetMapping("/testJasper2")
public void createPdf(HttpServletRequest request, HttpServletResponse response) throws IOException {
    //1.引入jasper文件
    Resource resource = new ClassPathResource("templates/testParam.jasper");
    FileInputStream fis = new FileInputStream(resource.getFile());
    //2.创建JasperPrint,向jasper文件中填充数据
    ServletOutputStream os = response.getOutputStream();
    try {
        Map parameters = new HashMap<>();
        //设置参数,参数的key = 模板中使用的parameters参数的name
        parameters.put("username", "张三");
        parameters.put("mobile", "120");
        parameters.put("dept", "销售部");
        parameters.put("company", "传智播客");
        JasperPrint print = JasperFillManager.fillReport(fis, parameters, new JREmptyDataSource());
        JasperExportManager.exportReportToPdfStream(print, os);
    } catch (JRException c) {
        c.printStackTrace();
    } finally {
        os.flush();
    }
}
```

画面7：
```java
package cn.itcast.Controller;
import org.springframework.web.bind.annotation.*;
@RestController
public class JasperController03 {
    @GetMapping("/testJasper2")
    public void createPdf(HttpServletRequest request, HttpServletResponse response) throws IOException {
        //1.引入jasper文件
        Resource resource = new ClassPathResource("templates/testParam.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        //2.创建JasperPrint,向jasper文件中填充数据
        ServletOutputStream os = response.getOutputStream();
        try {
            Map parameters = new HashMap<>();
            //设置参数,参数的key = 模板中使用的parameters参数的name
            parameters.put("username", "张三");
            parameters.put("mobile", "120");
            parameters.put("dept", "销售部");
            parameters.put("company", "传智播客");
            JasperPrint print = JasperFillManager.fillReport(fis, parameters, new JREmptyDataSource());
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException c) {
            c.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

画面8：
```java
public Connection getConnection() {
```

画面9：
```java
public Connection getConnection() {
    Connection conn = DriverManager.getConnection();
    return conn;
}
```

画面10：
```java
public Connection getConnection() throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection();
    return conn;
}
```

画面11：
```java
public Connection getConnection() throws Exception {
    Class.forName("com.mysql.jdbc.Driver");
    Connection conn = DriverManager.getConnection("jdbc:mysql://localhost/lhrm", "root", "111111");
    return conn;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

