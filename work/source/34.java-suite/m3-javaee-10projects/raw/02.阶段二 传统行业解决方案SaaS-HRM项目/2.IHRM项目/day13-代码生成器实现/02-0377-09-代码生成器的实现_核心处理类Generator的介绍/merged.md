# 09-代码生成器的实现：核心处理类Generator的介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\09-代码生成器的实现：核心处理类Generator的介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 7分0秒（音频 421s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们这个程序入口已经搞定了那接下来关注的就是这个核心处理类Generator那这个核心处理类它的主要目的呢其实就是获取到所有的模板那接着针对数据模型和模板完成代码生成的这么一个工作那这边要想获取所有模板呢是不是就应该传递过来一个模板所在的路径那你的模板都在什么地方是不是要告诉我那接下来你生成的这个代码
[00:30] 你要生成到什么地方是不是也应该要告诉我呀所以这个类当中必然包含这两个参数第一个参数模板的路径第二个参数就应该有我们文件生成的路径这个应该也能理解所以接下来呢我们可以把这些基本的内容先给它填充过来好了找到我们的generator在这里面写两个私有属性第一个呢就叫做stringtimeLater
[00:59] P-L-A-T-Etablet path模板路径好了private死菌类型的好了autopath代码生成路径OK那这两个路径我们已经搞定了剩下的事情其实就是说呢对于这个代码生成来说呢我要new这个对象new这个对象我可以给它来一个public购到方法OK那好了借来那对于我们这个当中数据部分是它给我传过来的
[01:42] 但是我这里面是不是要用FreeMarker要进行文件的一个生成没错吧那进行文件的生成我们可以简单的一起再来看一下我们之前玩过FreeMarker程序的一个简单测试TestFreeMarkerTest但是咱们就玩第一个在这个里面各位发现FreeMarker程序当中其中有一个比较重要的这么一环就是一个Configuration对象那这个Configuration对象当中是不是要指定文件加载器啊
[02:11] 那这些内容那我可不可以把这个内容以私有属性的形式给它提取到这边呢那我底下进行文件生成我是不是直接用一个已经创建好的对象来生成就可以了没错吧所以呢我把这玩意也提取出一个私有属性privateconfiguration别选凑包非marker里面的比如说我就叫做cfcfg吧ok那这个cfg对象
[02:43] 那在什么时候进行初始化更加合适在什么时候进行初始化更加合适那我是不是就可以在调用generator的时候也就是在调用构造方法new这个对象的时候把这个cfg对象也给我初始化出来所以我这边cfg初始化或者实例化我们的configuration对象cfg等于new一个configuration
[03:18] 那扭过了configuration那接下来我们紧接着就应该给它指定我们的模板加载指定模板加载器那对于这个模板加载器可以通过CFG打DMsetTemplateLoader那我们都知道对于模板加载器来说有很多种形式可以有SGIN的模板加载器可以有我们的文件路径的模板加载器没错吧文件路径那文件路径的模板加载器
[03:49] 那怎么去做呢咱们可以一起来看一下我们之间的代码直接给你一个fail你用一个fail这个fail当中是不是要指定一下你这个输出的路径在哪啊你模板所在的文件夹在哪没错吧是这意思吧那我们是不是同样跟这个代码是类似的搞一个模板加载器那这个模板加载器你用一个fail那这个fail现在显然不能是你随便写的一个timelate
[04:23] 那这个timelapse应该换成什么是不是我们的所有模板路径都在这个timelapse的pass这边所以直接拿过来那这样一来我们就已经指定了我们要去找你给我路径的这个里面从这个当中找到所有的模板OK那好了把它添加过来那这样一来我在程序实例化generator核心类的时候就已经把CFG对象也准备好了那我们这个构造方法
[04:57] 咱们已经写好了那接下来呢需要在这个类当中提供一个方法去完成代码生成的这么一个操作好了在这边底下关注的就是代码生成那这个代码生成呢public就没有返回值了vyd那这边方法名呢我就可以给它随便起一个sccan skinscanandgeneratorj-e-n-e-r-a-t-o-r
[05:29] 好了这个方法它的主要目的简单的和各位来写一下那这个方法它首先第一件事就是去扫描我们模板路径下的所有模板因为你这个路径下不仅是一个它有可能有do层的代码survey层代码Controller层代码还有我们的实体类那这些可能在不同的路径下在不同的子目录下
[05:57] 但是这些子目录或者这些文件是不是都应该在这个模板路径之下呀所以在里边我们要扫描所有的模板那扫描到所有模板之后接下来第二件事才是真真正正的对每个模板进行代码的一个填充进行代码的一个进行生成进行文件生成吧OK那接下来那在我们这边进行文件生成的过程当中是不是要借助我们的数据
[06:28] 模型那数据模型从哪来这一边我们不产生模型数据模型不是这个类产生的通过哪通过其他地方给我传递过来所以你从其他地方应该给我传递一个参数map类型的数据模型data model倒下包OKOK那这样一来我们这个核心的方法就是我们接下来重点关注的了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 FreeMarker 框架实现代码生成器的核心逻辑，包括配置初始化、模板加载和数据模型绑定。

2) 按时间顺序列出每张画面的要点：
画面1：展示系统架构图，UI界面通过 GeneratorFacade 调用 Generator，Generator 负责获取模板和生成代码。
画面2：在 IDEA 中打开 Generator.java 文件，展示类的包声明和注释。
画面3：在 IDEA 中，光标位于 Generator 类的 private 字段声明处，提示需要指定类型。
画面4：展示项目目录结构，包含 src、test、resources 等目录，以及 templates 文件夹。
画面5：在 Generator.java 中，光标位于构造函数的参数声明处，提示需要指定类型。
画面6：在 IDEA 中，光标位于 Generator 类的 private 字段声明处，提示需要指定类型。
画面7：在 IDEA 中，光标位于 Generator 类的 private 字段声明处，提示需要指定类型。
画面8：在 Generator.java 中，光标位于构造函数的参数声明处，提示需要指定类型。
画面9：在 IDEA 中，光标位于 Generator 类的 private 字段声明处，提示需要指定类型。
画面10：在 IDEA 中，项目结构视图显示 test 目录下的 FreeMarkerTest01.java 文件。
画面11：在 Generator.java 中，光标位于构造函数内部，正在初始化 Configuration 对象并设置模板加载器。
画面12：在 Generator.java 中，光标位于构造函数内部，正在初始化 Configuration 对象并设置模板加载器。
画面13：在 Generator.java 中，光标位于构造函数内部，正在初始化 Configuration 对象并设置模板加载器。
画面14：在 Generator.java 中，光标位于 scanAndGenerator 方法的开始处，准备编写代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
UI界面
1.模板路径
2.输出路径
3.工程配置对象
4.数据库配置对象
统一调用的入口程序
GeneratorFacade
1.采集UI界面的输入数据
2.根据数据传递信息获取数据模型
3.调用核心生成器完成代码生成
代码生成核心处理类
Generator
1.获取到所有的模板
2.根据数据模型和模板完成代码生成

画面2：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {

画面3：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {
private String templatePath;//模板路径
private String outPath;//代码生成路径
private Configuration cfg;

画面4：
coduits
.idea
custom.properties
typeConverter.properties
src
main
java
cn.itcast
generate
core
Generator
CodeUtil.java
DatabaseUtil.java
test
target
templates
pom.xml
External Libraries

画面5：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {

画面6：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {

画面7：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {

画面8：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {

画面9：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {

画面10：
coduits
.idea
custom.properties
typeConverter.properties
src
main
java
cn.itcast
generate
core
Generator
CodeUtil.java
DatabaseUtil.java
test
target
templates
pom.xml
External Libraries

画面11：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {
private String templatePath;//模板路径
private String outPath;//代码生成路径
private Configuration cfg;
public Generator(String templatePath, String outPath) throws Exception {
this.templatePath = templatePath;
this.outPath = outPath;
cfg = new Configuration();
FileTemplateLoader ftl = new FileTemplateLoader(new File(templatePath));
cfg.setTemplateLoader(ftl);
}

画面12：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {
private String templatePath;//模板路径
private String outPath;//代码生成路径
private Configuration cfg;
public Generator(String templatePath, String outPath) throws Exception {
this.templatePath = templatePath;
this.outPath = outPath;
cfg = new Configuration();
FileTemplateLoader ftl = new FileTemplateLoader(new File(templatePath));
cfg.setTemplateLoader(ftl);
}

画面13：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {
private String templatePath;//模板路径
private String outPath;//代码生成路径
private Configuration cfg;
public Generator(String templatePath, String outPath) throws Exception {
this.templatePath = templatePath;
this.outPath = outPath;
cfg = new Configuration();
FileTemplateLoader ftl = new FileTemplateLoader(new File(templatePath));
cfg.setTemplateLoader(ftl);
}

画面14：
package cn.itcast.generate.core;
/**
 * 代码生成器的核心处理类
 * 使用Freemarker完成文件生成
 * 数据模型
 * 模板位置
 * 生成文件的路径
 */
public class Generator {
private String templatePath;//模板路径
private String outPath;//代码生成路径
private Configuration cfg;
public Generator(String templatePath, String outPath) throws Exception {
this.templatePath = templatePath;
this.outPath = outPath;
cfg = new Configuration();
FileTemplateLoader ftl = new FileTemplateLoader(new File(templatePath));
cfg.setTemplateLoader(ftl);
}
/**
 * 代码生成
 * 1.扫描模板路径下的所有模板
 * 2.对每个模板进行文件生成（数据模型）
 */
public void scanAndGenerator(Map<String, Object> dataModel) {

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：架构图，UI界面指向 GeneratorFacade，GeneratorFacade 指向 Generator。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

