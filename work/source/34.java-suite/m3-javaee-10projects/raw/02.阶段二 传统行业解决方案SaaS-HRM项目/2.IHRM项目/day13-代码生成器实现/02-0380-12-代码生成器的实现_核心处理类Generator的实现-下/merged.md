# 12-代码生成器的实现：核心处理类Generator的实现-下

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\12-代码生成器的实现：核心处理类Generator的实现-下_【海量资源尽在 ubkz.com】.mp4
- 时长 6分0秒（音频 361s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 那模板的最核心操作的代码我们已经写好了接下来就是把我们的入口类和我们这个模板给它联系到一起那这个入口类呢我们要做的事情就是在genitor by database这个方法当中循环的去调用genitor我们的核心工程没错吧好了那接下来我们来看一下这个比较简单这个比较简单
[00:26] 那如何去做呢由于这个genal return我不可能每一个表我都new一下每一个表都new一下那这种方式呢就太啰嗦了当然我这边注视也把它注视起来这个打印刚才测试的给它注视起来那我这边不可能每一次都去new一个genal return这么一个核心类那我怎么办是不是就可以在我的入口操作这边当调用它的构造方法的时候
[00:51] 当调用构造方法的时候我把这个对象给我new出来那底下我直接调用对象里面的方法一个一个的进行生成其实就可以了所以在这边类似点genitor等于new一个genitor好了那new genitor的时候是不是这边传递过来模板的路径和我们输出的路径那模板路径timeliter pass好输出路径alt pass当然了这边会有一个小小的异常
[01:20] 那这样一来当我创建出我们的入口类的时候核心类就已经准备好了那当我这边调用generator by database的时候我们这边就可以得到每一个数据库表得到表之后通过我们的核心处理类打点调用方法scan and generator对每一套表进行一次代码的生成工作那我们这边把每一套表
[01:50] 构造的模型对象传递进去是不是就可以了呢OK那这样一来呢我这个代码里面所有的内容就跟各位都写好了我们可以最后联系起来做一个简单的测试看一下能不能够生成文件好了那我们都知道对于我们这边的其中有一个要求我这边的UI它已经固定死了只能去读取模板下某一个文件里面的内容所以我这边的做的测试比较简单粗暴
[02:21] 那我在Spring Boot程序的模板当中给它创建一个我们的模板好了这个Fill当然了这个文件的模板名称叫什么其实无所谓你可以是点Java结尾的也可以是其他的那注意这个文件名不能随便写那这个文件名呢应该用什么比较合适呢我就用一个我们之前看过的注意$className好了点Java那这样一来
[02:51] 是不是就根据从数据库当中得到的表名表的名称转化成的实体类以实体类的名称给我生成这么一个Java代码OK或者生成这么一个类接下来这模板当中我就不搞那么复杂了什么get set因为我们一会儿要去专门讲定义模板我主要是测试一下我整个这套程序能不能够给它跑通能不能够生成文件界面
[03:17] 到入口程序到我们最后生成代码程序之间每个环节是否有问题咱们主要是为了测这个不是为了写代码不是为了写模板我们一会还会讲可以吧所以我在这边主要是来看一下我们这个类名等于dollar大括号class我主要是看一下能不能使用那好了那这样一来我这个已经写好了写好了之后我们找到UI database youtube来执行问方法
[03:53] 好了这边找到mycircleroot123456测试连接没问题im点击下一步那这样一来其实我就是要对整个im数据库里面的所有表进行代码生成那一个表要生成一套代码一个表要生成一套代码也就意味着最终我生成的代码有很多那这些很多的代码根据我这边来说是不是就根据我们这个模板
[04:23] 要创建很多个.java文件有多少个表创建多少个没错吧好了那接下来模板选择那输出的文件路径给它写到哪咱们就给它放到今天资源有一个测试就放到这个生成代码路径当中OK项目英文名呢我这边随便写了去ihim报名com.ihim.tm好了项目中文名称呢就是人力资源
[04:55] 作者itcast随便写OK那接着生成代码好了这边告诉我代码生成成功那我们找到刚才指定的代码生成的路径生成代码路径各位会发现生成了好多个什么什么Java那我们随便打开两个一起来看比如说打开一个角色打开一个CT你发现
[05:21] 角色的就是角色CT就是CT没错吧那这样一来我们这个代码生成器其实代码就已经验证了是没有问题的那代码生成器所有的这些代码全部写好了之后接下来由于我们这个模板制作的过程当中会有很多的细节问题我们不是生成一个什么简单的Java文件我可能要生成一套代码比如说有DO有Service有Controller有实体类所以这些制作这个模板是一个比较复杂的内容
[05:50] 所以我们代码生成代码生成器代码只写完了不是最重要的还有模板是如何做出来的这是我们接下来要搞的内容

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过 Java 代码结合模板引擎（FreeMarker）实现根据数据库表结构自动生成 Java 实体类和相关文件。

2) 按时间顺序列出每张画面的要点：
画面1: 展示 Generator.java 中的 executeGenerator 方法，用于处理模板文件、设置输出路径、创建文件并调用模板处理。同时展示 main 方法，用于初始化 Generator 并执行代码生成。
画面2: 展示 GeneratorFacade.java 中的 generatorByDatabase 方法，用于遍历数据库表，获取数据模型并调用 Generator 核心类处理。
画面3: 展示 GeneratorFacade.java 中的 generatorByDatabase 方法，光标位于 for 循环内部，准备处理每个表的数据模型。
画面4: 展示 GeneratorFacade.java 的构造函数，用于初始化模板路径、输出路径、配置和数据库对象。
画面5: 展示 GeneratorFacade.java 中的代码，光标位于构造函数内部，准备初始化 Generator 核心类。
画面6: 展示 Generator.java 中的 scanAndGenerator 方法，用于扫描模板路径下的所有模板文件并进行生成。
画面7: 展示 GeneratorFacade.java 中的 getDataModel 方法，用于根据表对象获取数据模型，并自定义配置。
画面8: 展示项目结构，选中 GeneratorFacade.java，右键菜单中选择“Create Git...”。
画面9: 展示运行结果，生成的 $ClassName.java 文件为空，终端显示 Java 进程成功结束。
画面10: 展示代码生成器对话框，模板选择为“通用模板”，项目路径为“E:\Users\ThinkPad\Desktop\day13”，用户名为 root，密码为 111111。
画面11: 展示数据库管理工具界面，显示表结构，包含 id、name、age、email、phone 等字段。
画面12: 展示代码生成器对话框，模板选择为“Spring Boot程序的模板”，项目路径为“E:\Users\ThinkPad\Desktop\day13”，用户名为 root，密码为 111111。
画面13: 展示生成的 Java 文件列表，包含 City.java、Company.java、Department.java 等实体类。
画面14: 展示 PPT 页面，标题为“2 实现代码生成”，子标题“2.1 需求分析”和“2.2 模板生成”，并列出 GeneratorFacade 和 Generator 两个类的作用。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1:
```java
private void executeGenerator(Map<String, Object> dataModel, File file) throws Exception {
    //1.文件路径：E:\项目路径
    //TemplatePath：E:\项目路径
    String templateFileName = file.getAbsoluteFile().getParent().replace(this.templatePath, replacement: "");
    //2.读取文件数据
    Template template = cfg.getTemplate(templateFileName);
    template.setEncoding("utf-8"); //指定生成文件的字符编码
    //3.创建文件
    File file1 = FileUtils.mkdir("outPath", outFileName);
    FileWriter fw = new FileWriter(file1);
    template.process(dataModel, fw);
    fw.close();
}

public String processTemplateString(String templateString, Map dataModel) throws Exception {
    Template template = new StringWriter();
    Template template = new Template("ts", new StringReader(templateString), cfg);
    template.process(dataModel, out);
    return out.toString();
}

public static void main(String[] args) throws Exception {
    String templatePath = "C:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径";
    String outPath = "C:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径";
    Generator generator = new Generator(templatePath, outPath);
}
```

画面2:
```java
public GeneratorFacade(String templatePath, String outPath, Settings settings, DataBase db) {
    this.templatePath = templatePath;
    this.outPath = outPath;
    this.settings = settings;
    this.db = db;
}

/**
 * 1.点备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public void generatorByDataBase() throws Exception {
    List<Table> tables = DataBaseUtils.getObjInfo(db);
    for (Table table : tables) {
        //为每一个table对象,进行代码生成
        //获取模型
        //调用Generator核心处理类
        Map<String, Object> dataModel = getDataModel(table);
        for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
        System.out.println("--------------------------------");
    }
}
```

画面3:
```java
/**
 * 1.点备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public void generatorByDataBase() throws Exception {
    List<Table> tables = DataBaseUtils.getObjInfo(db);
    for (Table table : tables) {
        //为每一个table对象,进行代码生成
        //获取模型
        //调用Generator核心处理类
        Map<String, Object> dataModel = getDataModel(table);
        for (Map.Entry<String, Object> entry : dataModel.entrySet()) {
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
        System.out.println("--------------------------------");
    }
}
```

画面4:
```java
/**
 * 1.点备数据模型
 * 2.调用核心处理类完成代码生成工作
 */
public class GeneratorFacade {
    private String templatePath;
    private String outPath;
    private Settings settings;
    private DataBase db;
    private Generator generator;

    public GeneratorFacade(String templatePath, String outPath, Settings settings, DataBase db) {
        this.templatePath = templatePath;
        this.outPath = outPath;
        this.settings = settings;
        this.db = db;
    }
}
```

画面5:
```java
// 拷贝Generator核心处理类
Map<String, Object> dataModel = getDataModel(table);
```

画面6:
```java
public void scanAndGenerator(Map<String, Object> dataModel) throws Exception {
    //1.根据模板路径找到此路径下的所有模板文件
    List<File> fileList = FileUtils.searchAllFile(new File(templatePath));
    //2.对每个模板进行文件生成（调用模板）
}
```

画面7:
```java
private Map<String, Object> getDataModel(Table table) {
    Map<String, Object> dataModel = new HashMap<>();
    //1.自定义配置
    dataModel.putAll(PropertiesUtils.customMap);
    //2.配置
    dataModel.put(key, table); //table.name
}
```

画面10:
```text
模板：通用模板
代码生成路径：E:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径
项目名（英文）：
包名：
项目中文名称：
作者：
数据库：
用户名：root
密码：111111
```

画面12:
```text
模板：Spring Boot程序的模板
代码生成路径：E:\Users\ThinkPad\Desktop\day13\资源\模板\生成代码路径
项目名（英文）：
包名：
项目中文名称：
作者：
数据库：
用户名：root
密码：111111
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面14:
PPT 标题：2 实现代码生成
子标题：2.1 需求分析
内容：
- 为了代码更加直观和易于调用，实现代码生成共有两个类组成：
  - UI 界面统一调用入口类：GeneratorFacade
    - 方便多种界面调用，主要完成数据模型获取，调用核心代码处理类完成代码生成
  - 代码生成核心处理类：Generator
    - 根据数据模型和模板文件路径，统一生成文件到指定的输出路径

子标题：2.2 模板生成
内容：
(1) 配置统一调用入口类 GeneratorFacade
代码：
```java
// 1.根据传入数据模型信息构造数据
// 2.根据模板完成代码生成
// 3.公共数据模型Map集合（处理文件路径等公共代码替换）
public class GeneratorFacade {
    private Generator generator;
}
```

5) 无。

