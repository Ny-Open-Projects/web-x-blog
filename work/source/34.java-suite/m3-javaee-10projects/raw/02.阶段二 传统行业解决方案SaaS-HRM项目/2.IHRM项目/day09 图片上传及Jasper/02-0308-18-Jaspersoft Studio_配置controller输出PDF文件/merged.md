# 18-Jaspersoft Studio：配置controller输出PDF文件

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day09 图片上传及Jasper
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day09 图片上传及Jasper\18-Jaspersoft Studio：配置controller输出PDF文件_【海量资源尽在 ubkz.com】.mp4
- 时长 11分42秒（音频 702s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 整个整合的这个工程结构我们已经写好了那接下来呢我们就完成最后一项就是可以配置一个Controller那通过浏览器进行访问那最终我们把pdf的JASPER文件以pdf的形式给它输出出来好了那我们应该如何去做呢其实也比较简单直接在这边右键创建一个class好了我把它放到Controller这个保下c-o-n-t-r-o-l-l-e-a Controller起一个名字呢叫做JASPER Controller
[00:32] GASPERJASPERCNTOLIA CONTROLLEROK那既然是我们的一个控制器类首先在上边ETA RESETCONTROLLER进行一个配置那接下来呢里面我们可以配置一个方法PUBLICVOID就叫做CREATE PDFPDF那在我创建的过程当中呢有可能需要两个参数第一个呢HTTP SERVERLETREQUEST这个都比较简单
[01:05] 好了接下来呢就request那接着再来一个httpservlet response因为最终呢是不是要以文件的形式输出到浏览器上所以需要response那这边给他配置我的请求路径at注意我这回就用get mapping了我就以get形式进行访问OK那我的请求路径呢这边也写上就叫做test jasperOK那接着我这个方法
[01:34] 大的轮廓我们已经写好了接下来关注的就是这个方法里面我们应该如何去去做首先呢是这样的就是说呢在我这个工程当中我已经把点JASPER文件是笔入进来了所以我需要对这个点JASPER文件的进行数据的一个填充那数据填充好了之后我们是不是可以得到一个叫做JASPER PRINT这个还有印象吗那有了JASPER PRINT那接下来JASPER PRINT里面已经有PDF的所有内容了
[02:03] 那接下来我们以流的形式进行响应输出到浏览器上以pdf的形式输出不就可以了吗所以对于我们来说我们要做的事情一共有这么几件事第一件事一起写一下好了就需要引入JASPER文件OK那文件引入进来之后接下来第二件事我们要做的事情就是创建JASPER print好了JASPER print也有了那接下来呢我们就是将JASPER print
[02:41] 以pdf的形式进行输出OK那好了接着第一个引入JASPER文件那引入JASPER文件呢其实比较简单比较简单那我们都知道对于一个叫做resource目录下的一个文件来说呢我们可以借助Sprint的机制来做那Sprint呢为我们提供了一个resource这么一个接口而以sourcresource这么一个接口别选错
[03:12] Spring提供的resource它是一个接口它指的是配置文件相应的内容就是要进行一个读取那读取呢其中有很多种方式我们借助的是class pass下的这个resource所以我需要你有一个class pass resource那这class pass resource里面我们就可以写class pass里面的相对路径要找到test jasper好了我们这边呢路径我怕写错我就call一下
[03:43] 这个也怕写错call一下那这样一来我们已经得到了当前它的一个resource对象那其实要resource没什么用我们主要是为了读取得到这个文件的相应的一些文件流信息所以接下来呢我需要进行一个加载创建出我的fill input stream就是一个文件的输入流信息好了比如说呢我就叫做fs等于new一个fill input stream
[04:13] 那么new的过程当中可以借助它的一些构造方法比如说我们可以拿到当前的文件那如何去做也不难resource对象里面提供了很多的方法比如说get fill那这样一来这边有一个异常我处理一下那这样一来我们就已经将Jasper report的文件引入进来了引入的是一个文件的输入流那文件输入流有了那接下来我们关注的点
[04:42] 就是创建Jasper Print那创建Jasper Print它主要目的是如何创建它就是向我们这个Jasper文件当中中填充数据因为别忘了我们主要目的Jasper文件其实就是一个模板的二进制的一种体现形式那拿到这个模板的二进制体现形式里面没有任何的数据那数据也需要填充所以我们要对这个内容进行一个填充那填充
[05:13] 简单如何做借助他提供的工具类JASPERJASPERFillManagerJASPERFillManager这是一个工具类它里面有很多的方法其实都差不多就是FillReportFillReport那FillReport的时候我们要做的事情要干嘛注意首先要往这个JASPER文件当中填内容第一个参数
[05:47] 那第二个参数注意new一个hashimap好了接着第三个参数我们要new一个jreempty data source好了这边呢也会有一个异常我写一try catch吧OK那接下来呢得到一个返回值就叫print了那我想跟各位来简单的说一下这边如果你去参照Jasper report他的官方文档去做的话这边呢有一个问题
[06:19] 有一个问题其实你会发现就是最后这个对象我写不写都没问题都不会报错但是如果你按这种写法的话你输出的这个pdf永远都为空这是它的一个小小的一个bug所以对于我们来说右边要填写上那对于这三个参数简单的做一个说明简单做一个说明那这三个参数里面第一个参数fs是我们的文件输入流那这个文件输入流呢说的准确一点是我们jasper文件的输入流
[06:54] 好了我们准备要向这个文件当中填充数据好了那接着第二个你有一个hashi map那这个hashi map其实代表的是一些参数这个指的是我们要往JASPER里面输入的一些参数输入的参数那好了接着呢还有第三个第三个呢叫做可以简介来看它叫做data source我写成JASPER data source吧JASPER data source
[07:32] 那这个Jasper Data Source指的是数据源注意这个数据源和就是我们的数据库数据源不同这个指的是我们填充模板的数据来源那只不过这个填充模板数据来源可以是一个我们的Connection数据库的Connection那可以呢是我们的一个Java Bean还可以呢是我们的一个Map集合所以有很多
[08:05] 但是不管是这三个哪一个我们现在虽然没用没用这个参数你也需要写因为它有一个小的bug那如果说你没有数据来源我们怎么办就是填充一个空的数据源这个填充的空的数据来源就是JR Empty Data SourceOK那这三个参数和各位做了一个简单的说明那这样一来我们就已经把
[08:34] 我们想要的数据填充到JASPER文件里虽然我这JASPER文件里面什么数据也没有但是必须要这么写如果其他形式就有一些小的bug在里面能理解吧OK好了我们填充好了之后接下来第三件事就是将JASPER以PDF的形式进行输出那PDF形式进行输出也是借助JASPER提供的工具类你会发现全部都是工具类JASPER这个叫做JASPER export manager好了解
[09:05] 打点点它有一个方法exportreportexportreportto pdfto pdf注意我们以流的形式进行输出以流的形式进行输出那各位通过调用这个方法它就会把你生成的这个printer这个流信息写入到outputsrm里ok拿过来那接下来我这个代码如何去写第一个printer要有
[09:35] 第二个我们现在是以一个请求的形式所有的最终响应是不是都是以response来做那以response来做的话我们就应该得到response的output stream所以这边我先在上边response打点get output stream得到输出的响应输出流比如说叫OS那好了接下来我们就可以把所有的内容填充到这个OS对象当中
[10:06] 并且进行响应当然了既然是一个OS对象的话那底下呢不管如何finally最终呢它可以进行一个刷新和关闭OK那这样一来我这个EMN Controller当中的代码也已经写好了其实重点没有别的就这么两个工具方法的使用第一个fill report那fill report主要目的就是把一些数据写入到Jasper文件当中
[10:33] 接着is part report to pdf stream它的主要目的就是将写入好的print文件以pdf形式给我输出出来我们这边是以流的形式放到response里面并且进行响应的OK那Controller代码我们都写好了接下来我们关注的就是把这个工程给它启动起来进行一个访问好了找到我们的启动类走这边我去打开浏览器
[11:11] 好了应该是已经启动差不多了并且启动的过程当中没有报任何错误OK那好了我们接下来就可以访问一把来看一下效果Localhost我们现在访问的是81818181没错吧好了接下来请求的路径TestJasper走TestJasperOK各位来看这个不就是我们的一个PDF的一个雏形吗

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过控制器方法使用 JasperReports 生成并返回 PDF 文件。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，选中 resources 目录，右侧编辑器显示 JasperApplication.java 的启动类代码。
画面2：在项目中创建 JasperController.java 文件，准备编写控制器逻辑。
画面3：在 JasperController.java 中编写 createPdf 方法，导入必要的类并使用 @RestController 注解。
画面4：在 createPdf 方法中添加 @GetMapping 注解，指定请求路径为 "/testJasper"。
画面5：在 createPdf 方法中引入 ClassPathResource 获取 jasper 文件，创建 JasperPrint 对象。
画面6：在 createPdf 方法中创建 FileInputStream 读取 jasper 文件，准备调用 JasperFillManager。
画面7：在 createPdf 方法中使用 JasperFillManager.fillReport() 方法填充报表。
画面8：在 createPdf 方法中使用 JasperExportManager.exportReportToPdfStream() 方法导出 PDF。
画面9：在 createPdf 方法中使用 JasperExportManager.exportReportToPdfStream() 方法导出 PDF。
画面10：在 createPdf 方法中使用 JasperExportManager.exportReportToPdfStream() 方法导出 PDF。
画面11：在 createPdf 方法中使用 JasperExportManager.exportReportToPdfStream() 方法导出 PDF。
画面12：在 createPdf 方法中使用 JasperExportManager.exportReportToPdfStream() 方法导出 PDF。
画面13：在 JasperApplication.java 中启动 Spring Boot 项目，控制台显示应用启动成功。
画面14：在浏览器中访问 http://localhost:8181/testJasper，页面显示正在等待响应。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package cn.itcast;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "cn.itcast")
public class JasperApplication {
    // 启动方法
    public static void main(String[] args) {
        SpringApplication.run(JasperApplication.class, args);
    }
}
```

画面2：
```java
package cn.itcast.Controller;

public class JasperController {

}
```

画面3：
```java
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http

