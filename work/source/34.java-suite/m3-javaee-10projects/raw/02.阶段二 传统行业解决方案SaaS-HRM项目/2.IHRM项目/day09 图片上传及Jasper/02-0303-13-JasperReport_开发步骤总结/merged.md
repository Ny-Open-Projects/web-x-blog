# 13-JasperReport：开发步骤总结

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\13-JasperReport：开发步骤总结_【海量资源尽在 ubkz.com】.mp4
- 时长 7分32秒（音频 452s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那我们可以看到呢第一个方法那这边呢需要来一个pass参数那这些pass参数呢其实在今天的资源当中就在这儿我把这个路径也拷一下拷贝过来那各位会发现其实就是对一个JRS描也就是我们刚才的这个模板的文件的一个路径没错吧那接下来我要做的事情呢其实就是执行第一个方法好了我们执行它Ctrl C拿过来再闷方法进行一个简单的执行
[00:36] OK执行成功你会发现这边回去进行刷新它得到了一个Jasper这么一个文件那这个文件我们知道它是什么呢其实就是通过编译这个XML得到的这么一个Jasper的这么一个文件对象那这个文件对象它是一个二进制的一个文件那我们接下来要做的事情就是对这个二进制文件里面的一些内容进行填充
[01:03] 其实对于JASPER对象其实它已经有了一个PDF的一个雏形了只不过的是它里面还没有相应的数据数据从哪做我们通过createJR print的方法来做来走好了这就是我们的第二个阶段好了第二个阶段这边有一个问题就是我这边的路径又写错了路径又写错了OK把这路径补全走
[01:36] 好了这边也执行成功了那继续回到这边你会发现又多了这么一个文件这个文件呢现在变成JR print什么了其实这个玩意儿打开呢基本上这都是一些二进制的一些文件但是我想跟各位说的你表面上看这三个是差不多的但是要有清楚第一个阶段生成JASPER第二个阶段生成print第三个阶段我们是不是就可以对这个print文件进行一个预览或者对它进行一个PDF的一个输出啊
[02:06] 所以接下来呢我们再去运行第三个方法售PDF走这边呢同样的有这个问题啊路径好了接下来我们一起来看一下走一执行你会发现这边弹出一个框框里面就是一个PDF的一个文件了那对于这个PDF来说中间有一句话什么好强大我们刚才看过底下还有这么一句话一个PDF的一个页尾一个页头OK那这个其实是跟各位来聊的就是说传统的方式
[02:38] 我们要想去完成一个PDF文报表的生成它有三个生命周期首先第一个就是进行一个模板制作并且得到JASPER文件第二个就是将JASPER文件和我们的数据进行填充获取到一个JRPRINT这么一个文件接着第三个根据JRPRINT我们是不是可以去生成对应的PDF或者进行预览或者进行打印下载等等没错了OK好了通过这三个主要想跟各位来
[03:07] 了解的就是它生命周期的这三个阶段以及这三个生命周期它的一些产出物并不是让跟各位要聊这些代码其实这些代码很负责任跟各位说有些代码我们以后都不用写但是我需要各位要指导我需要各位要指导这个过程其实还是比较复杂的它里面涉及到比如说解析第一个其实就是对XML文件的一个解析
[03:36] 好了接着第二个其实就是对我们这个JASPER文件进行一个数据处理那第三个其实就是进行一个流的一个操作能理解吧好了那这个能理解的话接下来呢这边就是对JASPER的原理做了一个简单的描述也是一张图形这张图形里面其实就是刚才我们自己写代码的一些部分比如说JRX秒什么都不晚第二个JASPER
[04:00] 是我们的一个数据填充的这么一个对象第三个JARPRINT其实就是我们的一个报表打印对象这个里面呢有数据有我们的数据模板所有内容全部综合到一起接着来我们开始输出好了这个里面呢有一些点简单的来看一下JRXML本质XML本质XML这个XML里面封装了整个布局那由XML编译生成的JASPR那JASPR是一个二进制文件
[04:29] 那通过将这个二进制文件和数据进行结合得到我们的JR Print那JR Print其实就已经有报表的所有内容接下来就是决定输出何种形式接着把它打印出来没错吧好了这个就是简单的说了一下它的内部的一个构造那这个我们看过了之后并且呢这个代码也让各位看过了那以后我们要去设计一个PDF那有的朋友就说了那这太麻烦了你得先把
[04:59] 模板得搞定吧那你有模板了之后是不是还得生成扎刺文件呀那有了扎刺文件是不是还有填充数据呀是不是还要进行预览打印呀那这个太麻烦了我害怕了我不想搞PDF了行不行不是这样的那所以最后要跟各位简单的来总结一下我们完整的开发PDF那我们关注的点以及我们开发的流程究竟是什么样的首先第一件事报表这个模板
[05:29] 你不做都不行没错吧所以第一件事首先的就是要去制作爆冷网板那第二件事这边我写的是一个模板编译啊模板编译其实就是生成渣滓粉文件那接着我想说对于模板编译不是我们重点关注的点为什么它可以帮助我们自动生成所以我们不关注它那接下来第二件事你构造了一个模板必然要往里面填充数据没错吧那这个数据究竟是什么数据在哪是我们业务里面关注的点所以我需要构造数据
[05:58] 那数据也构造好了之后接着就是一个点叫做填充模板因为模板里面预留了一些空格比如说用了这些比如说你用户叫什么名字是不是要从构造的数据里面往里面填充所以第三件事就是往模板里面填充数据这个谁都替代不了所以我们重点关注的一个开发流程来说模板一定要做数据一定要准备第三个填充有的朋友说了刚才我们经历了编译的过程进行了一个
[06:28] 预览的这个过程好像都没有体现是吧没错吧那为什么没有体现是因为我们要去开发PDF的时候要用的是一个制作模板制作模板我们用了一个工具这个工具叫做JASPRsoft Studio那这个工具当中已经帮助我们以图形化的形式制作模板并且这个工具可以帮助我们
[06:56] 进行模板的一个编译并且这个工具可以帮助我们进行模板的一个预览的一个操作所以各位你就会发现单独使用Draftsport Report的形式太麻烦了X名号模板你得自己写但是我们用了工具以图形化的形式来做其实就可以了所以我们一会儿结合这个工具再去进行开发的时候我们关注的点就这么三点第一个模板用工具帮助我们去创建去绘制第二个
[07:25] 构造数据构造数据有了之后接着第三个填充模板其实就可以了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 JasperReports 在 Java 中生成报表，包括编译 .jrxml 文件、填充数据生成 .jprint 文件、以及预览 PDF 报表。

2) 按时间顺序列出每张画面的要点：
画面1: 在 IntelliJ IDEA 中展示 Java 代码，定义了 `createJasper` 方法用于将 .jrxml 文件编译为 .jasper 文件。
画面2: 在 Windows 资源管理器中，显示了项目目录结构，包含 `test01.jrxml` 和 `test01.jprint` 文件。
画面3: 在 IntelliJ IDEA 中，代码中注释了 `createJprint` 方法，用于将 .jasper 文件填充数据生成 .jprint 文件。
画面4: 在 Windows 资源管理器中，右键点击 `test01.jprint` 文件，弹出菜单，显示了“使用 Windows Defender 打开”等选项。
画面5: 在 Windows 资源管理器中，显示了 `test01.jprint` 和 `test01.jrxml` 文件。
画面6: 在 IntelliJ IDEA 中，代码中添加了 `showPdf` 方法，用于预览生成的 PDF 报表。
画面7: 在 IntelliJ IDEA 中，代码中 `showPdf` 方法的注释被修改为“预览”。
画面8: 在 IntelliJ IDEA 中，代码中 `main` 方法调用 `showPdf` 方法。
画面9: 在 PPT 中，标题为“4.2 JasperReport原理简述”，下方有一个流程图，从“JRXML”指向“Jasper”。
画面10: 在 PPT 中，流程图继续，从“Jasper”指向“Jrprint”，再指向“Exporter”，最后指向“PDF/DOC/HTML”。
画面11: 在 PPT 中，显示了关于 JRXML、Jasper、Jrprint 和 Exporter 的说明文字。
画面12: 在 PPT 中，高亮显示了“Jasperreport可以输出多种格式的报表文件，常见的有HTML/PDF/XLS等”。
画面13: 在 IntelliJ IDEA 中，代码中 `main` 方法调用 `showPdf` 方法。
画面14: 在 PPT 中，显示了“4.3 开发流程概述”和“5 模板工具Jaspersoft Studio”标题。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面1:
```java
package cn.itcast.jr;
import net.sf.jasperreports.engine.JREmptyDataSource;
import net.sf.jasperreports.engine.JasperCompileManager;
import net.sf.jasperreports.engine.JasperFillManager;
import net.sf.jasperreports.engine.JasperViewer;
import java.util.HashMap;
public class JrDemo {
    public static void main(String[] args) {
        //1.将pdf模板转为jasper文件
        createJasper();
    }
    //1.将pdf模板转为jasper文件
    public static void createJasper(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jrxml";
            JasperCompileManager.compileReportToFile(path);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    //2.将jasper文件和数据进行填充，获取jprint
    public static void createJprint(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jasper";
            JasperFillManager.fillReportToFile(path, new HashMap(), new JREmptyDataSource());
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
```

画面6:
```java
//3.预览
public static void showPdf(){
    try{
        String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jprint";
        JasperViewer.viewReport(path, isXMLFile: false);
    }catch(Exception e){
        e.printStackTrace();
    }
}
```

画面8:
```java
public class JrDemo {
    public static void main(String[] args) {
        showPdf();
    }
    //1.将pdf模板转为jasper文件
    public static void createJasper(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jrxml";
            JasperCompileManager.compileReportToFile(path);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    //2.将jasper文件和数据进行填充，获取jprint
    public static void createJprint(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jasper";
            JasperFillManager.fillReportToFile(path, new HashMap(), new JREmptyDataSource());
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    //3.预览
    public static void showPdf(){
        try{
            String path = "C:\\Users\\ThinkPad\\Desktop\\ihrm\\day9\\资源\\生命周期测试\\test01.jprint";
            JasperViewer.viewReport(path, isXMLFile: false);
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面9: 标题“4.2 JasperReport原理简述”，下方流程图：JRXML → Jasper。
画面10: 流程图：Jasper → Jrprint → Exporter → PDF/DOC/HTML。
画面11: 文字说明：
1. JRXML-报表填充模板，本质是一个XML。
2. Jasper-由JRXML模板编译生成的二进制文件，用于代码级填充。
3. Jrprint-当用数据填充完jasper后生成的文件，用于输出报表。
4. Exporter-决定要输出的报表为何种格式，报表输出的管理类。
5. Jasperreport可以输出多种格式的报表文件，常见的有HTML/PDF/XLS等。
画面14: 标题“4.3 开发流程概述”和“5 模板工具Jaspersoft Studio”。

5) 无。

