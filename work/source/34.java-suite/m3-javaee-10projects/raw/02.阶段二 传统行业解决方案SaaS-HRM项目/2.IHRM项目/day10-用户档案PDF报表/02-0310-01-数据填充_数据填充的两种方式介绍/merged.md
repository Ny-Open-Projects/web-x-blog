# 01-数据填充：数据填充的两种方式介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day10-用户档案PDF报表
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day10-用户档案PDF报表\01-数据填充：数据填充的两种方式介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 4分29秒（音频 270s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 各位朋友大家好今天是SaaS人力资源管理系统的第十天那首先需要跟各位简单的介绍一下我们今天要学习的内容那对于今天的内容呢总的来看不是那么的难重点就是使用我们昨天安装好的Jasper Studio也就是这个工具通过这个工具去完成一些报表的一些开发
[00:27] 的一些工作当然了我们是通过ZO2工具创建模板通过Java填充数据的形式来做的那我们昨天呢简单的写了一个是一个基本的静态的PDF所以我们今天第一块要看的就是说如果说你这个PDF里面要去填充数据的话应该如何去做也就是第一块数据填充那数据填充我们讲过了之后其实一个PDF报表我们已经可以去制作了但是里面报表可能还涉及到很多细节的一些内容比如说呢
[00:57] 报表里面可能会有分组的一个报表显示比如说呢在一个报表里面可能会用到一些chart的一些图形比如说呢饼状图啊线状图啊柱状图啊等等那接下来那对于一些复杂的一些报表或者说是一些咱们在一个报表里面解决不了的问题那这个时候就需要用到父子报表去进行解决了那前四点呢我们看过了之后其实都是去基于studio以及Jasper report去
[01:26] 完成报表的一个生成和制作的这么一个过程那最后一个就是我们可以把这些所有的基础的一些内容整合到一起完成我们SaaS里面的用户个人信息档案的一个PDF打印OK所以对于我们今天的内容来说呢一共做的某块但是呢它不难其实最重要的就是这个工具的一个使用OK咱们先看第一点就是一个叫做数据填充那么我们在讲数据填充之前呢首先需要跟各位简单的
[01:55] 看一下我们之前写过的静态的代码,在静态代码当中和各位昨天来聊过,它的一个JASPER REPORT,它的一个开发的一个步骤,我们昨天说过了,关注的首先是第一个去创建模板,我们用工具,接下来我们要去构造一些数据,第三步就是去填充数据,填充数据的数据应该以什么形式体现出来,昨天我们看过了,其实一共有这么一个方法,
[02:26] 叫做Fail Report这个Fail Report其实就是像我们的模板当中去填充数据的那这个数据可以借助这个方法可以看到其实数据部分呢一共有两个两个参数第一个参数呢叫做New一个HashiMap第二个参数是一个什么什么Data Source没错吧所以咱们可以简单的得知如果真的想往PDF当中去填充数据的话那我们的途径往大的说其实就两个方向
[02:55] 第一个方向搞一个map集合出来第二个方向我们可以搞一个Jasper Data Source也就是我们的填充数据数据源所以接下来我们来看一下在我们真正的要想往一个PDF报表当中要想去填充数据的话我们关注的其实就是它的这两种方式第一种方式叫做Parameters也就是参数填充第二种方式叫做Data Source也就是数据源这种填充方式
[03:24] 那这个Parameters其实代表的就是我们代码当中的这个Map集合那还有一个DataSource代表的就是JRDataSource是我们数据的数据来源其实这两个是我们Java代码层面上的这两种方式其实这两种方式也契合了Jasper Studio这个工具里面的一些组件也就是说人家不是平白无故的给你搞一个Map
[03:54] 给你搞一个JRDataSource之所以这么做是因为可以很方便的我们在这个工具里面方便我们去使用能理解吧所以这边你如果传递的是Map那我这边其实就可以以ParameterMap的形式往这个工具里面拖那如果是JRDataSource那我们可以从这里面也是往里面拖就这个含义所以它们两个是非常契合的这么一个关系OK那我们接下来先看第一个也就是
[04:24] 参数MAP也就是Parameter的方式进行数据填充

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何使用 JasperReport 实现动态数据填充到 PDF 报表，重点介绍参数 Map 填充数据的方式。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示文件资源管理器，当前路径为“ihrm/day10”，其中包含“代码”、“测试”、“SaaS-HRM--第10章.pdf”等文件夹和文件。
画面2：PDF 文档第10章“用户档案PDF报表”的第1页，标题为“第10章 用户档案PDF报表”，列出学习目标：理解数据填充的两种方式、熟练构造分组报表、熟练构造Chart图形报表、实现个人档案的PDF输出。正文介绍将研究如何填充动态数据到PDF报表。
画面3：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2内容相同，但页面滚动条位置略有不同。
画面4：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3内容相同，但页面滚动条位置略有不同。
画面5：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4内容相同，但页面滚动条位置略有不同。
画面6：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，包含一个 @RestController 注解的类，其中定义了 createPdf 方法，用于生成 PDF 报表。
画面7：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，与画面6相同，但光标位置不同。
画面8：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4、5内容相同，但页面滚动条位置略有不同。
画面9：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4、5、8内容相同，但页面滚动条位置略有不同。
画面10：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，与画面6、7内容相同，但光标位置不同。
画面11：JasperSoft Studio 软件界面，显示项目结构“Project E”包含“MyReports”和“TestReports”两个文件夹。
画面12：JasperSoft Studio 软件界面，与画面11内容相同，但光标位置不同。
画面13：IntelliJ IDEA 编辑器中显示 JasperController.java 文件内容，与画面6、7、10内容相同，但屏幕底部显示了多个窗口的预览，包括 JasperSoft Studio 和 PDF 文档。
画面14：PDF 文档第10章“用户档案PDF报表”的第1页，与画面2、3、4、5、8、9内容相同，但页面滚动条位置略有不同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面6、7、10、13 中的代码：
```java
package cn.itcast.Controller;

import org.springframework.web.bind.annotation.*;

@RestController
public class JasperController {

    @GetMapping("/test.jasper")
    public void createPdf(HttpServletResponse response) throws IOException {
        //1.引入jasper文件
        Resource resource = new ClassPathResource("templates/test.jasper");
        FileInputStream fis = new FileInputStream(resource.getFile());
        //2.创建JasperPrint,向jasper文件中填充数据
        ServletOutputStream os = response.getOutputStream();
        try {
            // fis: jasper 文件输入流
            // parameters: 向模板中输入参数
            // dataSource: 数据源
            JasperPrint print = JasperFillManager.fillReport(fis, new HashMap<>(), new JREmptyDataSource());
            //3.将JasperPrint PDF格式输出
            JasperExportManager.exportReportToPdfStream(print, os);
        } catch (JRException e) {
            e.printStackTrace();
        } finally {
            os.flush();
        }
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面2、3、4、5、8、9、14 中的 PPT 标题和内容：
- 标题：“第10章 用户档案PDF报表”
- 子标题：“1 数据填充”
- 子标题：“1.1 参数Map填充数据”
- 子标题：“1.1.1 模板制作”
- 子标题：“（1）创建新模板，删除不需要的Band”

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

