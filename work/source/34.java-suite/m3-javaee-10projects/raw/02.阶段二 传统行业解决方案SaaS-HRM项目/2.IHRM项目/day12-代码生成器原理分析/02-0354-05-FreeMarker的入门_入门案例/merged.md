# 05-FreeMarker的入门：入门案例

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\05-FreeMarker的入门：入门案例_【海量资源尽在 ubkz.com】.mp4
- 时长 15分1秒（音频 901s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 简单的介绍了一下FreeMarker那接下来呢我们就开始写一个程序和各位一起来看一下FreeMarker应该如何去使用那其实对于FreeMarker来说呢先跟各位要声明一点玩FreeMarker我们重点关注的是两方面内容一方面内容呢其实就是扎瓦代码那第二方面内容才是最重要的就是模板应该如何进行编写所以我们学FreeMarker重点扎瓦代码不是重点
[00:32] 我们重点关注的是模板OK那好了接下来我们开始着手去玩一下复原码口如何去用好了在这边呢我打开我的idea创建一个新的工程new一个project好了这个工程呢是一个maven工程了我就用maven工程去玩了OK点击next好了这边呢group id cn.itcastit artifact id呢我就叫做codeutil我们要完成codeutil
[01:04] 点击next好了接着把它放到什么地方呢我把它放到HRM这个包下code utilsok没问题没问题点击finish有windowok那我们这个工程呢已经创建出来了那接下来呢玩free marker需要引入free marker框架它的依赖包那在这边dependence那这个依赖呢在今天的资料当中呢也给各位准备好了
[01:38] 12天资料工具代码抱歉资源是在代码这边啊pom.txt把它打开把它打开好了里面相应的坐标Ctrl C直接拿到我这边Ctrl V那我们拿过来了之后需要跟各位简单的来说一下第一个就是我们FreeMarker它的核心包核心包OK那我们现在呢已经
[02:15] 工程创建出来了并且呢也把坐标引入进来了那接下来我们在这边重点着手的要干这么两件事第一件事要定一个模板第二件事通过free marker解析模板并且把模板当中的内容进行替换那接着我去定义一个基础的一个模板那注意这个模板我把它放到哪呢我把它放到SRC目录跟SRC平级的这个目录也就是当前工程的目录下边
[02:46] OK创建一个目录我叫做templatestemplatesok那这个模板的名称呢叫什么呢注意开始创建一个模板这个模板名称呢我就叫做temp叫01了那我们都知道对于frame marker来说了它的后缀这模板的后缀一般是以ftl来命名的OK那在这个模板当中呢我们可以写一些最简单的一些代码
[03:21] 比如说呢可以来一个叫做欢迎欢迎您注意欢迎您代表的是我们最终要生成的一些普通的一些字符那我们要想替换的内容用什么去描述你最终要想用书籍替换是什么我这边就用dollar大括号的形式来进行描述那这个dollar大括号其实可以理解为我定义的一个站位符那最终我要用数据把站位符的内容进行替换
[03:48] 那比如说呢我来一个user nameOK那这样一来我第一个模板咱们已经定义好了好了模板定义好了之后接下来我们去完成第二件事光有模板不行我们还要写fremark程序把数据替换当前的模板上没错吧OK好了那接下来呢这个代码呢我就写到testmulu下右键创建一个包
[04:13] 我叫cn.itcast.freemarker.test好了我叫free marker test我叫01吧OK抱歉这个应该是类名啊写了一个包啊创建一classnew一个class好了接下来我们关注的第一个free marker程序OK
[05:03] 那要在这第一个服务marker程序里面我们要想各位能够了解的点一共有这么几个第一个就是使用服务marker的一个操作步骤为什么要了解这个操作步骤呢是因为咱们这个服务marker呢Java代码写的比较简单并且呢它这个不管是什么应用玩服务marker它的步骤基本上都是一模一样的所以要对这个操作步骤希望各位要能够理解OK那接着我们这边可以按它test
[05:35] 写一个方法一起来测试一下free markervoid test我叫01了OK那我们这个操作步骤一共是分成这么五个步骤首先第一个创建free marker的free marker的我们叫做配置类好配置类有了之后接下来我们需要指定注意我们需要指叫做模板加载器
[06:04] 那指定模板加载器它的主要目的是干嘛呢就是说呢对于这个模板而言呢可以有这么几种加载方式第一种加载方式你用一次加载一次第二种加载方式用一次之后把它存到缓存里那你用模板加载器的话它会将模板存入缓存当中就是节省我们的效率吧OK好了接着指定了模板加载器之后接下来我们可以关注的第三个点我们就是获取模板
[06:35] 那模板获取到了之后接下来第四个点别忘了FreeMarker它有一个非常好的这么一个特点就是叫做数据加上模板等于文件输出所以对于我们第四步接着要做什么就是构造数据模型数据了好了接着第五件事就是文件输出所以对于FreeMarker来说我们只需要牢牢把握住这么五个步骤这么五点就可以了
[07:02] 那接着我们一个一个把这个代码给他补充完成首先创建 free marker配置类那这个叫做 configurationso figconfiguration 别选错 free marker好了我叫做 cfg 了等于 new 一个configuration好了接下来第二个指定模板加载器那这个模板加载器如何指定很简单 cfg 打点set time later
[07:36] loaderok那这个settime link loader里面可以打开它的源码简单来看一下你会发现你发现这里面接收一个参数time late loader就是一个模板加载器那这个模板加载器我们可以简单的看一下它它是一个接口它有很多个实现类有很多个实现类那这个实现类其中有class time late loader这个是类路径查找fill文件路径上进行查找
[08:08] 还有SGIN就是我们文本模板的还有UIL地址模板的加载还有web应用程序的加载等等那对于我们而言呢我没把它放到类路径下我不是类路径下我是一个文件路径所以我用的是Field Terminator Loader所以我在这边Field Terminator LoaderFTL等于new一个好了这里面呢注意注意这个里面它是我们的文件
[08:41] 路径加载器文件路径加载器那这个文件路径加载器什么含义它指的是你给我指定一个文件这个它的路径你就是说你模板所在的目录就在这儿就是咱们这个timelates目录下那你需要把这个目录下告诉所以接下来呢我可以这样去做new一个fail那这个fail里面我写什么呢写一个timelates注意timelates在这边
[09:18] 那他这句话代表的含义就是在指定我所有的模板都在这个timeless目录下边那我一会获取模板的时候我直接给他这个模板的名称其实就可以了他自动的从这个目录下去给我找能理解吧OK好了抛出一个异常解决一下那接下来呢把这个ftl传递进来那我们的模板加载器搞定了之后接着加载模板加载模板比较简单cfg.gettimeless
[09:52] 好了模板的名称我们的模板名称呢起了一个名字叫做tmplat01.ftlok好了接下来构造数据模型注意这个数据模型和你模板里面的站位符息相关你模板里面的站位符名称呢叫做username那你构造的数据必须也要包含username它才能进行替换可以吧好了接下来那在free marker当中
[10:20] 你这个数据模型全部都是以Map集合的形式往里面存放的所以我这个数据模型其实就是一个Map集合死剧类型的ObjectOK我叫做DataModel等于New一个HashiMapOK那好了DataModel.putUserName这个UserNameKey就是我们的占位符OK那里面可以给它传递一个比如说呢叫做传直播客
[10:55] 好了那这样一来我们第四步也已经搞定了好了那接下来就是最后一步就是文件输出那当然了对于这个文件输出来说呢其实也可以把它叫做模型处理处理模型那处理模型的时候我们调用的是一个方法这个方法呢咱们可以简单的来看一下好了刚才这边忘了补充反位值了通过获取的模板模板里面打点方法Process好那对于这个Process方法呢它接收的呢有这么
[11:29] 两个参数它的主要目的就是用来处理模板的它接收的两个参数第一个参数参数一代表的是我们的数据模型好了参数二那对于参数二而言这边接收的是一个writer对象writer对象那对于这个writer对象呢各位应该不陌生其实它代表的是一个文件的fill writer或者是print writer那如果是fill writer的话
[12:09] 那它就会把你处理好的内容以文件的形式给我输出出来那接着如果是printwriterprintwriter它就会把这个文件的内容全部都打印到控制台上好了这个就是文件输出控制台输出OK那接下来我们一起来看一下tablet.process好了第一个参数model data model那接着第二个参数代表的writer那好了我就可以先以文件的形式进行输出fill
[12:46] 好了那接着接着一个new fill那这个fill你想要把这个文件输出到什么位置比如说我就想要输出到我们今天在这边呢可以给它写一文件夹叫做test我就想生成到这个test文件夹下Ctrl C拷过来叫什么名字呢我就叫A点比如说就叫dit了OK这边异常呢我这边用最大的处理即可
[13:21] OK那这样一来我这个代码就已经写好那接着我们可以执行一下看一下效果走好了这边程序在执行的已经执行成功了那需要各位注意的是我们的模板叫做欢迎你dollar.username那接下来我生成了一个文件就在刚才的泰斯特这个目录下我可以打开它来看一下欢迎您传至博客是不是就已经将
[13:52] 我们这边站位符的内容替换成我们数据模型里面的传辑播客了OK这个其实就是简单的和各位来看了一下我们这个free marker它的一个基本的使用当然了除了这个使用之外呢我们为了方便测试我们可以通过timelate.process第二个接收的是一个newprintwriter这种方式把所有内容打印到空这种方式
[14:20] 把数据打印到控制台上当然了你有一个printwriter还要接收一个out参数我就来一个system.out这样一来它其实就是不会往文件输出了而是把所有内容输出到我们的控制台上OK一起再来看一下走主要是为了方便测试好了各位来看欢迎您传直播客效果是一样的没错吧OK这样一来我们简单的来看了一下第一个free marker程序我们
[14:51] 关注的两点第一点模型第二点就是Java代码的编写Java代码编写这几个操作步骤都是固定的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 FreeMarker 模板引擎在 Java 中实现数据模型到文件的输出。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，`Company` 类中包含 `@Table`、`@Data`、`@AllArgsConstructor` 等注解，用于定义数据库表映射和生成 getter/setter。
画面2：展示 `pom.xml` 文件，正在编辑 `<dependencies>` 标签，准备添加依赖。
画面3：在 `pom.xml` 中添加了 FreeMarker、JUnit、MySQL Connector 的依赖。
画面4：在项目中右键，选择“New” -> “Java Class”，准备创建测试类。
画面5：创建了 `FreeMarkerTest01.java` 文件，位于 `test/java` 目录下。
画面6：在 `FreeMarkerTest01.java` 中编写了 FreeMarker 的导入语句和类定义。
画面7：在 IDEA 中查看 `Configuration.class` 的源码，定位到 `setTemplateLoader` 方法。
画面8：在 `FreeMarkerTest01.java` 中编写了初始化 FreeMarker 配置和模板加载器的代码。
画面9：打开 `template01.ftl` 模板文件，内容为“欢迎你，${username}”。
画面10：在 `FreeMarkerTest01.java` 中编写了获取模板、构建数据模型的代码。
画面11：在 `FreeMarkerTest01.java` 中编写了处理模板、设置输出流的代码。
画面12：运行测试，成功输出文件内容“欢迎你，任意值”。
画面13：在 `FreeMarkerTest01.java` 中添加了 `import` 语句和注释。
画面14：运行测试，提示“Cannot resolve variable 'username'”，说明变量未正确传递。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面2：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <groupId>cn.itcast</groupId>
    <artifactId>codetutils</artifactId>
    <version>1.0-SNAPSHOT</version>
    <pr>
```

画面3：
```xml
<dependencies>
    <dependency>
        <groupId>org.freemarker</groupId>
        <artifactId>freemarker</artifactId>
        <version>2.3.28</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.17</version>
        <scope>test</scope>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.6</version>
    </dependency>
</dependencies>
```

画面8：
```java
import freemarker.cache.FileTemplateLoader;
import freemarker.template.Configuration;
import org.junit.Test;

public class FreeMarkerTest01 {

    @Test
    public void test01() throws IOException {
        //1.创建FreeMarker的配置类
        Configuration cfg = new Configuration();
        //2.指定模板加载器，将模板存入硬盘中
        FileTemplateLoader ftl = new FileTemplateLoader(new File("templates"));
        cfg.setTemplateLoader(ftl);
        //3.获取模板
        Template template = cfg.getTemplate("template01.ftl");
        //4.构造数据模型
        Map<String, Object> dataModel = new HashMap<>();
        //5.文件输出
    }
}
```

画面9：
```ftl
欢迎你，${username}
```

画面10：
```java
//4.构造数据模型
Map<String, Object> dataModel = new HashMap<>();
dataModel.put("username", "任意值");
```

画面11：
```java
//处理模板
// 一、设置模型
// 二、writer（文件输出）
template.process(dataModel, new FileWriter(new File("C:\\Users\\(thinkPad)\\Desktop\\ihm\\day12\\test\\a.txt")));
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不评价画面美观，不输出与课程无关的内容。

