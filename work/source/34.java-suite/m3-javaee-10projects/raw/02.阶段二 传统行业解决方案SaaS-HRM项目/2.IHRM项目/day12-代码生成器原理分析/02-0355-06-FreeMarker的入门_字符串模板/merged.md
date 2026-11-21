# 06-FreeMarker的入门：字符串模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\06-FreeMarker的入门：字符串模板_【海量资源尽在 ubkz.com】.mp4
- 时长 9分17秒（音频 557s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那我们看过了这个FreeMarker第一个案例程序之后呢其实各位心里有个直观的感觉我们使用FreeMarker开发首先搞到FreeMarker的模板接着在这边写Java代码把数据搞到获取到数据之后调用FreeMarker的程序自动的是不是帮助我们把一个文件生成出来或者输出到某一个目录当中啊
[00:26] OK那对于它在生成的过程当中其实这个就好比它把我们模型当中的内容读取出来接着是不是做了一个字符串替换那替换的内容是不是就是以$大括号这种形式以站位符的形式给我标注出来接着把map当中的数据进行一个替换就可以了没错吧好了那刚才我们使用Fremarker其实是操作的文件的这么一种模板
[00:54] 那其实呢在Fremarker除了文件模板之外它还可以支持字符串模板形式那字符串模板形式什么意思就是说你提供一个死菌字符串那在字符串当中它也可以通过Fremarker进行模板替换那接下来我们来看一下那字符串模板究竟是什么含义好了在这边呢我再去创建一个新的测试类好了我叫做Fremarker F-R-E-E-M-A-R
[01:22] 可以压FreeMarkerTest我叫02OK好了这边我们测试的叫做测试字符串模板测试字符串模板首先不管是什么只要跟FreeMarker只要使用FreeMarker其实它的操作步骤基本上都差不多只不过需要各位注意的是我们在第一个程序这边模板是以文件的形式给我体现出来的说白了这边是从文件当中把模板给我加载出来
[01:58] 那接下来我第二个程序这个模板我没有那怎么办我需要自己通过子幅创创建模板差别不大那我们接下来看一下如何去做好了艾塔 testpublicvydtest好了那这个里面首先它的操作步骤基本上都是一模一样的首先第一件事我们要创建free marker的配置对象好了接下来第二件事呢也可以指定
[02:31] 它这个加载器好了接着第三件事那第三件事呢我们需要获取到模板那这个模板不是获取了我们现在要创建字符创模板好了那接着第四件事构造数据跟刚才一模一样第五件事我们叫做处理模板好了那接下来创建配置类对象configurationcfg等于new一个configurationok那这回指定
[03:04] 它的加载器打点settime-laterloader那需要各位注意的是现在我们就不能用刚才那个什么fill文件的这个模板加载器了那我们这边还是点开它的方法一起来看一下这个接口好了这回呢我们用的是string time-laterloaderok string time-laterloader点进来好了这些太多了关掉那我们就可以new一个string time-laterloader告诉它我现在用的是一个字符串模板
[03:38] 那接下来呢就是创建字符串模板那创建字符串模板如何去做呢其实也很简单那这里面呢分成这么几个阶段第一个阶段呢我们可以自定义一个搞一个字符串出来那有了字符串之后接着第二件事就是可以通过字符串创建模板OK那好了接下来这个字符串代表什么其实这个字符串就可以理解成我们模板里面的内容
[04:07] 那比如说这个是我们的模板内容Ctrl C拿到这边死菌TMPTMP LATE来一个死菌字符串OK那这个死菌字符串呢我同样是用TimeLate或者说FreeMarker里面模板的这个语法来定义这有一个占为符那接下来我们就可以通过字符串创建模板那这个模板呢叫做TimeLateTimeLateTimeLate等于New一个这回呢
[04:41] 我们需要去自己Nu出来自己去创建出来Nu一个timelate那Nutimelate的过程当中这边需要调用它的构造方法来做那这个构造方法注意我们用第二个构造方法那这个构造方法里面有三个参数第一个参数是Gyn指的是你可以对这个模板起一个名字为啥要有名字是因为你放到内存当中它通过模板名称从内存里面去获取当了这个名称我们可以给它搞到独一无二一点
[05:09] OK那好了接着第二个reader那这个reader呢其实就是把你这个字符创读取到我这个模板当中所以要需要一个字符创reader好了接着还有一个configuration这个configuration呢其实就是free marker的配置CFG对象了OK那接着我们可以把这个方法给它补充完整另一个timelapse首先呢第一个参数我们说过了是它的名称好了比如说呢我就叫做随便写了内幕1了
[05:37] OK那第二个参数第二个参数指的是一个reader对象好了你有一个stringreader那这个stringreader可以通过将字符串读取这种方式来进行创建好了接着第三个参数cfg我们的配置对象这边有一个问题我处理一下OK好了这个异常呢给它来一个最大的吧好了那我们这回已经根据字符串创建出了模板
[06:05] 那创建模板呢由于模板有一个username这么一个站位符那我们还要构造数据那构造数据和我们底下处理模板和我们之前写的代码基本上都是一模一样的来map集合string object好了data model等于new一个hashimap好了这个mapped key其实就是模板的站位符的名称打点putusername拿过来好了我这边同样传递一个值叫做张三
[06:41] 那好了接下来模板处理好了之后我们就可以通过这个模板它去处理处理的过程当中可以以文件的形式生成也可以把它输出到我们的控制台上这个其实就是人者见人 智者见智我们为了方便演示直接在控制台上输出就可以了好了tomlet.process好了 process第一个参数data model第二个参数我们可以new一个printwriter
[07:11] 好了 system.sostm.aut当然了我是为了方便就是输出到控制台上了如果你不想输出到控制台上你想要得到一个生成好的新的字符串其实我们用一个其他的StreamWriter其实也可以我主要是为了简单咱们可以看一下能够直观的到效果OK好了我们一起来看一下是否能够将它进行替换替换为欢迎您是不是叫做张三好了我们执行一把
[07:42] 看一下效果走好了各位你会发现同样的也能得到这个数据那其实呢这种方式生成一个这种方式呢去替换就有点像字符串替换了我们把字符串里面的这个阵符的内容是不是替换成我们指定的数据这个内容啊OK那有的朋友就说啊用这个这种字符串模板它有没有什么用处其实用处在我们的代码生成器当中会有
[08:14] 而且用处会比较多我举一个例子就是在代码生成器里面的这个应用啊死去模板是这样子我们生成代码的时候有可能可以给它指定某一个类所在的包我们指定它所在的包的时候我们一般的包名是不是叫做com.xx.xx.xx然后呢是我们的对象没错吧那接下来呢就是说这个1
[08:38] 1234这一些呢我们如果字符串替换的话要替换一次两次三次四次太麻烦了那么就可以通过字符串模板的形式比如说呢这边我可以给他来一个dollarP1那接着我后面去写P2P3我直接通过字符串模板替换一次是不是就能得到里面真完整的这个字符串呀所以呢这玩意儿他虽然有朋友说是不是没有用但是确实是有一些应用场景的同时呢
[09:09] 它也可以把字符串以文件的形式给我们输出出来所以这个字符串模式版跟各位简单的来聊一下OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中使用 FreeMarker 模板引擎，通过 Java 代码加载模板、设置数据模型并输出处理后的文本。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 Windows 桌面，有“黑马程序员”和“博学谷”标志，无代码或操作。
画面 2: 在 IntelliJ IDEA 中打开 FreeMarkerTest01.java，展示第一个 FreeMarker 程序的代码框架，包含创建模板加载器、获取模板、设置数据模型和处理模板的注释。
画面 3: 在 IntelliJ IDEA 中打开 FreeMarkerTest02.java，展示一个使用 @Test 注解的测试类，代码中包含 JUnit 注解和 Java 标准库的导入。
画面 4: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 5: 在 IntelliJ IDEA 中，显示了 freemarker-2.3.20.jar 的源码，展示了 StringTemplateLoader 类的实现，包括 putTemplate、findTemplateSource 等方法。
画面 6: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 7: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 8: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 9: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 10: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 11: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 12: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 13: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。
画面 14: 在 IntelliJ IDEA 中，FreeMarkerTest02.java 代码中，用户正在编写测试方法，注释说明了创建配置、设置模板加载器、加载模板、处理模板等步骤。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

//第一个FreeMarker程序（数据+模板→文件输出）
//1.操作步骤
public class FreeMarkerTest01 {
    //创建新类
    public static void main(String[] args) {
        //1.创建模板加载器
        FileTemplateLoader ftl = new FileTemplateLoader(new File("templates"));
        //2.获取模板
        Template template = ftl.getTemplate("template01.ftl");
        //3.构造数据模型
        Map<String, Object> dataModel = new HashMap<>();
        dataModel.put("username", "张三");
        //4.处理模板
        try {
            template.process(dataModel, new PrintWriter("output.txt"));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

画面 3:
```java
package cn.itcast.freemarker.test;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import org.junit.runner.RunWith;
import org.junit.runners.JUnit4;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        //4.处理模板
    }
}
```

画面 4:
```java
package cn.itcast.freemarker.test;
import freemarker.template.Configuration;
import org.junit.Test;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        //4.处理模板
    }
}
```

画面 5:
```java
package freemarker.cache;

import ...

public class StringTemplateLoader implements TemplateLoader {
    private final Map templates = new HashMap();

    public StringTemplateLoader() {
    }

    public void putTemplate(String name, String templateSource) {
        this.putTemplate(name, templateSource, System.currentTimeMillis());
    }

    public void putTemplate(String name, String templateSource, long lastModified) {
        this.templates.put(name, new StringTemplateSource(name, templateSource, lastModified));
    }

    public void closeTemplateSource(Object templateSource) {
        this.templates.remove(templateSource);
    }

    public Object findTemplateSource(String name) {
        return this.templates.get(name);
    }

    public long getLastModified(Object templateSource) {
        return ((StringTemplateSource)templateSource).lastModified;
    }
}
```

画面 6:
```java
import freemarker.template.Configuration;
import org.junit.Test;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        //4.处理模板
    }
}
```

画面 7:
```java
import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 8:
```java
import freemarker.template.Template;
import org.junit.Test;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 9:
```java
import java.io.IOException;
import java.io.StringReader;
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 10:
```java
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //3.加载字符串模板
        String templateString = "欢迎您，${username}";
        //4.处理模板
        Template template = new Template("name1", new StringReader(templateString), cfg);
        //5.处理模板
    }
}
```

画面 11:
```java
import java.util.HashMap;
import java.util.Map;

//测试字符串模板
public class FreeMarkerTest02 {

    @Test
    public void test() throws Exception {
        //1.创建配置对象
        Configuration cfg = new Configuration();
        //2.设置模板加载器
        cfg.setTemplateLoader(new StringTemplateLoader());
        //

