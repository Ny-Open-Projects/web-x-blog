# 15-Activiti7表结构生成（java代码方式）

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：1.Activiti7/Activiti7-day01-基础原理与使用
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\1.Activiti7\Activiti7-day01-基础原理与使用\15-Activiti7表结构生成（java代码方式）_【海量资源尽在 ubkz.com】.mp4
- 时长 18分39秒（音频 1119s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们通过前期的准备工作我们完成了MySQL数据库以及我们的这个Activity这个库的创建目前这里面没有任何的表我们现在就可以通过我们的这个加密代码的方式来创建我们的这个数据库表按照我们的这个操作步骤我们接着往后来走这个过程第一个我们可以去创建一个工程
[00:29] 好现在我们就回到我们的idea工具我在这里面直接去file new一个新的project对吧file new一个新的project好下一步是吧这个我就可以直接叫做comit黑码叫做activiti那具体的artifact的id比如说我就来一个activity
[00:58] viti activity01好吧那这样我们就创建好了一个新的工程啊然后呢具体放在位置在哪个地方呢这个地方我直接啊放到我们的01底下去啊所以呢我打算在这个地方进行选择叫day01放到我们的代码里面去OK对吧在代码里头呢我就再去起一个新的工程啊就叫这个名字这样基本上就可以了啊然后finish
[01:27] OK好这样我就有了一个新的工程啊他问我是否打开一个新的窗口比如说我在一个新的窗口里再去做这个工作啊那我们的这个坐标就出来了啊那现在我们要去使用我们的这个加密代码的方式来生成我们的这个activity所需要的25张表啊那现在我们就需要去加入相关的一些jar 包对吧
[01:57] 但是我们这一次使用的是MIME工程来做所以我们就需要把这些价包所对应的坐标添加到我们的POM.xml文件中来比如说我们activity所需要的这个价包activity所依赖的价包以及我们依赖的这个Spring的数据库的驱动以及我们连接池单元测试这样的一些价包所对应的坐标我们通通需要给它加过来
[02:27] 在加这个jar 包的时候你可以直接这样去做到这里头去复制这是一种方式啊除了这种方式呢我们也可以考虑啊使用我们今天给各位的这个资料现在我们呢资料在这个位置啊那我就直接进到这里头来叫做有一个叫做素材那我可以把我们的这个POM文件比如说啊就是它啊我直接打开
[02:53] 然后我下一步就可以直接把这个properties以及我们的这个dependent东西直接添加进来好我们这个时候就直接加把这一段直接加过来我们这个部分也可以把它的这个仓库是吧nexus这个伺服的仓库位置给它加入进来然后我就直接复制到我们的这个本地上来唐小微连到这来好我们一起再来回顾一下一起来看一下
[03:25] 这一次我们所加入的这个坐标其中的第一个是我们的这个activity的引擎对吧以及我们activity与sprint整合的一个一个坐标像这个部分就是我们的activity的BPMN模型对吧BPMN的模型图我们要加然后就是这个BPMN的转换转换的这个坐标需要加入进来
[03:51] 那就是转换成json的这个坐标啊以及我们的这个bpm的布局对吧然后我们再去走的是这一段什么close Service api这个呢咱们会根据情况啊去加啊然后再到这个部分呢就是我们的这个mycircle的对吧mycircle的这个依赖加薄啊以及我们的这个就unit对吧还有我们的这个log4j的这一段坐标啊我们的这个mybusiness的坐标对吧
[04:20] 以及我们的这个dbcp这个数据源的这个坐标啊各位呢这些其实呢都相对来说比较简单啊咱们同学应该是呃我认为基本上没啥问题啊那么这个坐标准备好了下一步我们要做的工作就是呢在这个部分我们需要去需要去啊把我们的这个呃编写相关的java代码以及我们的这个resource里下放置相关的一些配置信息
[04:50] 那这个配置信息主要包括有哪些配置信息啊我们主要包括两个一个是我们的logo4界就是我们的这个日志的一些配置信息那就是这个那我这边呢都直接啊拿过来就开始用了啊好你像这就是我们把这个日志直接OK那我们的这个日志文件啊就给它加入进来了那下一个我们还有一个文件啊就是我们的activity
[05:20] 本身呢它作为一个工作流的引擎那我们在使用它的时候也是需要有专门的一个配置文件那这个配置文件就叫activity.configure.xml当然我们呢在这里面你可以直接把我这一段扔进去那你也可以呢直接在这里再去创建一个新的xml文件比如说我就新建一个新的
[05:48] xml文件比如说叫做activiti.cfg.xml注意这个是我们的configurability默认的配置文件ok这样我们就直接再去把 xml文件直接给它补充上就可以了好下面我对于这一段我还是打开对于前边的部分我们基本上没有什么特别的地方看巧为能够
[06:18] 然后呢对于我们的这个结束位置对吧我们可以来一个就斜杠并子对吧这样呢我们基本上就完成了我们的这个activityconfigure.xml的具体的具体的这个具体的这个开始开始和结束就是一些并子啊然后呢我们在这个具体的这个里边可以写什么呢对吧在这个具体的里边呢我们可以去写上比如说
[06:46] 我们将来也需要有数据源的配置数据源的配置那我们这一次使用的是dbcp这个数据源这是一项然后我们这边还有一项工作要配置那就是我们的这个activity我们这一次使用的是单独运行单独运行单独运行的这个
[07:16] 叫做Process Engine叫做Process Engine也就是我们的这个引擎流程引擎Process Engine它的一个配置所以我们这一次真正配就配这两项Process Engine以及我们DBCP数据源的配置其中这个DBCP数据源的配置我们是比较简单我们只要使用叫做Basic DbSource就这一项这一项来进配置
[07:46] 然后它里面将来要注入的一个是driver class nameurl user name password以及它的最大连接数和我们的空显时最大连接数那这个我们copy直接扔到这里头来这是比较简单好当然这两项你如果不配置的话也有它的默认值对吧这两个你可以不配置那我们接着接着要去做一些修改比如说我这一次
[08:12] 我们用的这个数据库的名字是叫做activity对吧所以我改了啊然后就是改成自己的用户名和密码那这一项也非常简单啊那我们的这个process engine具体怎么来配置呢我们这里头啊要注意我们的这个process engine将来有很多种运行有有有有多种运行方式啊或者多种启动方式我们这一次使用的是啊使用单独启动啊单独启动
[08:40] 单独启动的方式来运行单独启动方式所以在这个地方我们要用的是有一个叫做Standard LANStandard LANProcess Engine Configuration这样我们就可以得到一个我们的Process Engine Configuration的对象好了这个地方我直接copy也把它直接拿过来Ctrl V扔到这里头来
[09:11] 这样我们基本上就完成了我们这一次项目所对于我们activity具体的配置文件的配置信息各位可以看到这边也有一些错误我们可以这样我们先对于我们的mywin工程我先给它刷一下这样的话就可以把它所需要依赖的这样的一些依赖的价包就通通给它导入进来
[09:40] 那这些jar 包一旦导入进来我们这个时候再回头去看一下我们的这个配置文件啊这边呢就没有报错了对吧好这样我们配置文件就已经搞定了啊那接着下一步呢我们就可以到这边来编写我们的这个具体的测试代码对吧那个编写我们测试代码我可以直接到这边啊再去new一个新的package啊比如说我就来一个叫做com.it黑码黑码.test啊我就放在这个包下
[10:10] 在这个包厢呢我再去创建一个我们的这个具体的测试类啊比如说我就来一个啊叫做我们的SETI VITIActivityTest啊OK这样呢我就可以去具体啊去写我们的这个实现了啊比如说这个就是我们的测试类啊测试类主要作用是什么呢它的这个主要作用就是啊测试测试我们的这个Activity啊
[10:41] SATI VITIActivity所需要的25张表的生成25张表的生成这就是我们要做的事情那下面我们就需要具体去搞一个这样的测试方法对吧比如说我这个地方就来一个public.moid搞一个这样的test我们的叫做generate table对吧好这就是我搞的一个这样的
[11:10] 搞了一个这样的方法它的主要作用就是去生成我们的这个表结构对吧那具体里头这个代码就是怎么去搞我们可以来看一下我们这也是编写这个程序的时候非常简单我们只需要去创建一个Process Engine Configuration的对象然后用我们的这个Process Configuration去构建我们的这个Process Engine的这个对象就可以了那两个步骤
[11:38] 两个步骤我们基本上就可以完成这个工作好那下面我们就可以直接到这里边来把这个代码直接给它搞定那我们第一个是叫做创建一个叫做process engine叫做configuration对吧创建一个这样的对象
[12:10] 然后第二个呢我们要创建的是我们的process engine的对象对吧第二个叫做创建我们的这个process engine对象就这两步子啊那我们先来做第一个工作啊就是叫做process engineconfiguration对吧就这个对象啊那这个对象比如说我来一个叫做configuration等于那这个对象我们可以啊
[12:40] 直接去使用它里头的叫做Colate Process Engine ConfigurationFromResource这个从字面的意思我们也能够看到创建一个Process Engine Configuration的对象FromResource从我们的配置文件中去找好那下面我们就直接去调用到这边来叫做
[13:06] process engine configuration只要去直接调用它的点created process process engine process engineconfiguration对吧好已经出来了from resource对吧我们应该要的是from resource对应的这个方法吧所以现在我们直接就可以直接从这里面去选取一个from resource好
[13:42] 我们可以换一下然后点这样就可以了然后在这个部分我们创建的这个里头你还可以去写上一个叫做我们的这个activityconfigure.xml这个是activityconfigure.cfg.xml对不对这样我们就完成了我们的这个process engine configuration的创建
[14:10] 那有了这个configuration我们下一步就可以直接用configuration点里头有个叫builder process engine对吧这样呢我们就可以得到一个process engine的这个这个对象对不对比如说我们就叫做process engine这样我们就完成了process engine的创建啊就完成了它的这个具体的创建啊那下一步其实你可以啊第三步这个就是可写可不写啊比如说我就在这里头来一个
[14:41] sout输出输出我们的这个输出我们的这个叫做process engine输出我们的这个对象看它是否已经创建出来了process engine就来它这样基本上我们就完成了这个测试再加上一个eta test作为我们junit的标志现在我们就可以去测试了这时候我们再去运行
[15:12] 来看一下啊它是否可以啊真正执行成功啊好这里边就有一个我们的这个测试啊这个各位呢就可以看到最终呢它是已经啊pass了对吧已经通过了那在这个通过的过程中啊其实我们呢来观察它的这个观察它的这个具体的
[15:37] 具体的这个执行过程的时候其实各位可以看到这里边有很多我们的这个create table的语句看见了吗这里头直接到这段结束吧这样我们是不是就相当于命行的一个create table这样的脚本那你想这个脚本一旦在我们的activity这个表里头Ctrl V扔进来如果你自己这么去执行的话你也一样可以
[16:06] 去生成我们的一张表对不对对吧那你想想我们这一次在刚才运行我们的这个加码代码的时候运行我们这一段加码代码的时候其实呢运行这一段加码代码的时候其实它的背后已经执行了若干过create table的语句你看一下啊这里面是不是又有一个又有一个create table然后你看看这个地方又有一个create table
[16:33] 这个corridor table的步骤是很多的如果你去数的话这里面这里有如果你去数的话各位其实可以看到将来这里的corridor table的过数应该是25个因为我们最终开始说了最终我们是需要生成activity所需要的25张表你看看这里面类似的还有corridor index以及我们的这个索引autotable修改表结构对吧
[17:03] 那你可以看到这里边的其实内容是比较多的后面又有Gradetable对吧好这些具体的过程我没有详细给各位一个一个去看Gradetable具体哪25张表对吧以及每个表里头就有些什么字段对不对而且每张表的意义是什么这个不各位先别着急我们后面会去给各位介绍的然后我们现在如果
[17:31] 但我这边一旦测试成功了让我回到我们的这个数据库我现在没刷新啊现在我可以直接在这里refresh刷新一下各位可以看到activity里头就已经有了我们很多相关的这个表我们来数一下啊2 4 6 8 12 14 16 18 20 22 24有25张表
[18:04] 这样我们就创建了25张表那以后我们的activity运行真正所需要的这个表结构的支撑通过这种方式我们就会快速完成好这是我们在这个里头给各位呢演示了一下我们的这个activity本身所需要的所需要的支持的这个25张表是如何被创建出来的那这个过程也不难对吧好我们
[18:34] 关于activity表结构创建的工作就说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IDEA 中创建 Activiti 项目，配置数据库连接，编写测试类并运行以自动创建 Activiti 数据库表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：打开 MySQL Workbench，连接到本地数据库，显示数据库列表，包括 activiti、crm、test 等。
画面 2：在 IDEA 中新建项目，项目名为 activi001，路径为 G:\Activiti\开发计划\Activiti\day01\代码。
画面 3：在 Windows 资源管理器中，显示 Activiti 项目文件夹，选中名为“代码”的文件夹。
画面 4：在 IDEA 中打开 pom.xml 文件，显示项目依赖配置，包括 activiti-engine、activiti-spring、activiti-bpm-model 等。
画面 5：在 IDEA 中继续编辑 pom.xml，添加了 activiti-cloud-services-api 和 mysql-connector-java 依赖。
画面 6：在 IDEA 中弹出“Copy”对话框，将 log4j.properties 文件复制到项目 resources 目录下。
画面 7：在 IDEA 中打开 activiti.cfg.xml 文件，显示 Spring 配置文件的 XML 声明和命名空间。
画面 8：在 IDEA 中编辑 activiti.cfg.xml，配置数据源和 ProcessEngineConfiguration。
画面 9：显示 PPT 页面，标题为“3.3.6.5 编写程序”，内容是创建 ProcessEngineConfiguration 并调用 buildProcessEngine() 方法。
画面 10：在 IDEA 中编写并运行 ActivitiTest 测试类，控制台输出日志，显示创建数据源和数据库表。
画面 11：在 MySQL Workbench 中，显示数据库连接状态，准备执行 SQL。
画面 12：在 IDEA 中，控制台日志显示创建表 ACT_RU_EXECUTION。
画面 13：在 IDEA 中，控制台日志显示创建表 ACT_RU_VARIABLE。
画面 14：在 IDEA 中，显示 ActivitiTest 测试类代码，注释说明了创建 ProcessEngineConfiguration 和 ProcessEngine 的步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 4 的 pom.xml 片段：
```xml
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-spring</artifactId>
    <version>7.0.0.0</version>
    <packaging>jar</packaging>
    <name>activiti-spring</name>
    <description>Activiti Spring integration</description>
    <properties>
        <slf4j.version>1.6.6</slf4j.version>
        <log4j.version>1.2.17</log4j.version>
    </properties>
    <dependencies>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-engine</artifactId>
            <version>7.0.0.0</version>
        </dependency>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-spring</artifactId>
            <version>7.0.0.0</version>
        </dependency>
        <dependency>
            <groupId>org.activiti</groupId>
            <artifactId>activiti-bpm-model</artifactId>
            <version>7.0.0.0</version>
        </dependency>
    </dependencies>
</project>
```

画面 5 的 pom.xml 片段：
```xml
<dependency>
    <groupId>org.activiti</groupId>
    <artifactId>activiti-cloud-services-api</artifactId>
    <version>7.0.0.0</version>
</dependency>
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>5.1.40</version>
</dependency>
<dependency>
    <groupId>junit</groupId>
    <artifactId>junit</artifactId>
    <version>4.12</version>
</dependency>
<!-- log start -->
<dependency>
    <groupId>log4j</groupId>
    <artifactId>log4j</artifactId>
    <version>1.2.17</version>
</dependency>
```

画面 7 的 activiti.cfg.xml 片段：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
</beans>
```

画面 8 的 activiti.cfg.xml 片段：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource">
        <property name="driverClassName" value="com.mysql.jdbc.Driver"/>
        <property name="url" value="jdbc:mysql://localhost:3306/activiti"/>
        <property name="username" value="root"/>
        <property name="password" value="root"/>
    </bean>
    <bean id="processEngineConfiguration" class="org.activiti.engine.impl.cfg.ProcessEngineConfigurationImpl">
        <property name="dataSource" ref="dataSource"/>
        <property name="databaseSchemaUpdate" value="true"/>
    </bean>
</beans>
```

画面 9 的 PPT 内容：
```java
//创建ProcessEngineConfiguration
ProcessEngineConfiguration configuration = ProcessEngineConfiguration
        .createProcessEngineConfigurationFromResource("activiti.cfg.xml")
//通过ProcessEngineConfiguration创建ProcessEngine，此时会创建数据库
ProcessEngine processEngine = configuration.buildProcessEngine();
System.out.println(processEngine);
```

画面 10 的 ActivitiTest.java 代码：
```java
import org.activiti.engine.ProcessEngine;
import org.activiti.engine.ProcessEngineConfiguration;
import org.junit.Test;

public class ActivitiTest {

    @Test
    public void testGenTable() {
        //1. 创建ProcessEngineConfiguration配置
        ProcessEngineConfiguration configuration = ProcessEngineConfiguration
                .createProcessEngineConfigurationFromResource("activiti.cfg.xml");
        //2. 通过ProcessEngineConfiguration创建ProcessEngine
        ProcessEngine processEngine = configuration.buildProcessEngine();
        //3. 调用processEngine创建数据库表
        System.out.println(processEngine);
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 9：PPT 标题为“3.3.6.5 编写程序”，内容为创建 ProcessEngineConfiguration 并调用 buildProcessEngine() 方法，下方有注释说明“activiti 数据库创建，通过改变 activiti.cfg.xml 中的配置，可以执行不同的数据表处理策略”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

