# 10-代码生成器的实现：核心处理类Generator的实现-上

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\10-代码生成器的实现：核心处理类Generator的实现-上_【海量资源尽在 ubkz.com】.mp4
- 时长 13分16秒（音频 797s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 各位我们已经把这个基本的代码生成的核心处理类基本的这些属性咱们填写好了剩下就是关注代码生成的这个逻辑那对于这个代码生成逻辑首先呢咱们这个方法scan and generator这个方法首先要做的是扫描模板下的扫描这个模板路径下的所有模板那这一步我们如何去做呢其实比较简单也不难我们要做的事情根据模板路径找到此此
[00:32] 路径下的所有文件当了文件模板文件当了这个路径下的所有模板文件它其实也有一些子的层级目录在里面这些呢我们在之前给各位提供的一个叫做FillUtils这个工具类当中专门给各位写了一个方法这个方法呢叫做SearchSearchAllFill这个SearchAllFill你只需要提供一个
[01:04] 相对路径即可那这个相对路径怎么做new一个fail好了接着把这个模板路径拿过来注意这个timelet path是一个文件夹的路径那这样一来它就会去这个文件夹下找到所有的文件能理解吧ok找到所有的文件当了这个文件夹下的子的文件夹它也存在它都会给我找过来
[01:35] 好了这样一来呢这边有一个异常我做一个简单的处理那我们就可以得到所有的模板文件了那所有的模板文件获取到了之后要针对每一个模板文件进行代码生成那好了比较简单ITR for循环没错吧那这个进行模板生成的过程当中这个代码如果都写到这个里面就实在太乱了所以我底下再去写一个方法比如说呢这个方法就叫exe cu
[02:10] 好了这个方法呢就开始进行生成那这个方法生成的时候我们需要两个参数第一个参数数据第二个参数模板文件OK拿过来好了当然了这个方法我们还没有那接着把这个方法也给它创建出来好了两个参数第一个数据模型第二个模板文件好了那这样一来我们关注的就是底下这个方法
[02:48] 那底下这个方法呢首先跟各位说明一下它是干什么它就是对模板进行文件生成好了需要传递两个参数第一个参数是我们的数据模型第二个参数是我们的模板模板文件没错吧好了OK那接下来对这个模板进行文件生成那这个文件生成那这个代码我们又该如何去编写
[03:18] 这都是一环套一环上面代码生成那代码生成呢扫描到某一个模板每一个模板找到所有找到所有之后针对这里面的每一个进行生成因为我们的模板太多了一个一个的模板进行生成嘛没错吧那针对每一个文件模板进行生成的话调用的是Excuse Generator这个方法那Excuse Generator这个方法我们要做的事情咱们一起来分析一下首先第一个我想问各位的那你这个比如说你这个模板文件
[03:48] 咱们把它存放到了文件比如说呢我就放到了C盘下叫abc.ftl当了这个模板文件呢除了叫abc.ftl可以也叫Java叫什么这个模板文件叫什么无所谓只要里面符合frame marker的一些语法其实就可以了当了我们这个Java文件呢有可能你要存到的一个包里是比如说com.ihim.sostem这个包下能理解吧
[04:21] 那这个包往这个包下里面存存代码那我想说的这个包名有可能也要进行替换那这个文件名也要可能进行替换那这个Java这个就不用替换了没错吧所以我们想方设法的创建一个文件的时候是不是这个包名也就是你的目录的这个名称也要进行替换也要进行处理所以我们第一件事要做的事情就是文件路径的处理那文件路径的处理我们这边feel
[04:54] 能够获取到你当前文件的真实的路径就相当于这样一来获取到一个真实的路径但是你这个真实路径你不能写成comma点什么什么什么其实说白了你这个路径就是一个字符串那有字符串那字符串我们是不是可以通过死剧模板的形式写一些符合我们需要的一个格式那职业者是不是就能替换成类似这种格式所以我们要做的事情第一件事想方设法获取文件的路径要对它进行处理
[05:24] 那文件路径处理好了之后那接下来我们要完成的其实就是模板的一些处理了比如说我们要读取我们的文件模板那文件模板获取到了之后接下来我们可以创建新的创建文件了创建一些新的文件创建了之后接着最后一些模板处理其实说白了就是文件生成OK这个就是我们接下来要关注的这么四个方面那咱们一个一个看
[06:02] 首先文件路径的一个处理那文件路径处理的时候首先拿到这个fill文件OK这个fill文件呢首先我们获取到死菌比如说呢就是template fill name得到它的一个完整路径名称那这个完整路径名称呢其实获取起来比较简单就是fill打点get这有一个叫做absolute path这个absolute path其实得到的是它的绝对路径
[06:35] 比如说呢我这个模板比如说呢我就在这边叫模板在这模模板当中我给它一个路径那所有的代码呢我就写到这个里面比如说呢我有一个包cn.ititcast好了再来hrm这里面我再来来一文件比如说呢就是叫做user.java
[07:10] 那我给它指定的模板文件就在这儿那接下来我扫描到这里面的每一个目录下是不是扫描到了一个模板叫user.java那user.java那这样一来它传递到我这个方法当中其实这就一个废物文件那这个废物文件代表的就是这个user.java注意这不是一个java类这代表的是一个模板那针对这个模板我通过get absolute path得到的是它的完整的路径user.java
[07:44] 这个能理解吗各位好了这个能够理解的话那接下来那我们这个文件格式的一个处理我说过cn.itcast.htm.user这个其实都不是固定的这是文件名称是一个字符串但是这些内容都不是固定的能理解吗那接着我们可不可以借助死讯模板的这种形式通过死讯模板把它进行一个替换呢
[08:11] 当然可以那我们有一个简单的约定就是这个包名是三层第一层叫做path1还记着吧刚才我们看过数据接着第二层path2好了接着第三层dollarpathpath叫做3没错吧接着这回这个user是不是应该是我们的类名我们的类名刚才是不是网里面专门存放过叫做classname抱歉classname
[08:46] 那这样一来我们的模板文件它的目录名称目录名称和我们的类名称咱们是不是就可以定义成这样的一个字符串那有了这样一个字符串是不是就可以通过我们之前玩的字符串模板的形式把它进行替换成我们真实的一些内容这个能不能理解
[09:09] OK当然了这个数据从哪来是不是data model里面要有pass1有pass2有pass3有passName它就能够给我做一个字符串的处理过程OK但是我想跟各位来说的就是说对这个文件路径的处理其实我只需要处理后半部分这一段就可以了也就是说模板路径之前的这段内容我怕它有问题所以我模板之前这段内容就不处理了
[09:37] 但是呢你fill.upload这些一拿到之后你就得到这么一个路径完整的那接着我这边做一个简单的替换工作点replace那这个replace替换什么就是类似点template path因为我们这边模板的template path针对我这个案例来说我们这个template模板路径是不是就应该是一盘下的这一项
[10:06] 这一项没错吧那这样一来我进行一个替换把它替换为空是不是关注的就是我们这个文件以及它所在的包的这么一个路径没错吧OK好了这样一来呢我们已经得到了咱们的一个死郡模板的一个字幕串死郡模板字幕串我们获取到了之后接下来我们通过死郡模板对它进行处理那对于死郡模板的处理我们之前代码咱们自己玩过不就在这儿呢吗
[10:37] 没错吧所以接下来呢我们把这段代码Ctrl C给它call过来简单的做一个修改当然了我这个呢到这边做一个修改泰斯特不要了好了这个里面的方法Template这个应该要留着好了那这边呢给的方法就是来一个叫做Template T-M-P-L-E-T-ESGENP-L-O-C-E-S-S就是处理磁幅创模板的
[11:12] 好了那对于字符串模板来说首先呢你应该有你要替换的这个字符串的名称timelit screen好了接着有我们的数据模型跟你些都一样modlok里面的代码首先configure我们不需要了这些我们都不需要了我们第一件事准备一个screenwriter比如说就叫out了等于new一个screenwriter因为这回我通过writer的形式把替换好的内容
[11:47] 要进行一个输出得到它的内容OK那好了接下来Z-Reader有了之后我们去自己构建模板构建模板当然了这个模板名称你叫什么都可以比如说我就叫做TS随便写的好了你用一个Reader然后呢把这个传递过来CFG也有没问题模板已经有了之后数据我也有好了接下来timelit.process进行处理那这回处理的时候我把所有的内容给它输出到out对象里面
[12:19] 好了底下return out.to死菌这边return out.to死菌死菌类型的没问题OK那这样一来我可以通过调用字符串模板的形式把这个文件路径就进行一个替换了好了那这样一来我在上边就可以输出你当前这个文件out比如说就叫out fill pass
[12:52] 输出文件它的名称好了把它拿过来Ctrl C这边Ctrl V接着把我们的模型也传递过来这边有个异常我做一个处理上面也就有异常这边来最大的OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Java 中的 FreeMarker 模板引擎，通过代码动态生成文件，包括配置模板加载器、扫描模板文件、处理数据模型并输出生成文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Generator.java 文件的开头部分，定义了模板路径、输出路径和配置对象，并初始化了 FileTemplateLoader。
画面2：在代码编辑器中，光标位于“File”类的自动补全列表中，准备输入“File”。
画面3：在代码编辑器中，光标位于“Print”类的自动补全列表中，准备输入“Print”。
画面4：展示 Generator.java 文件中 scanAndGenerator 方法的注释和部分代码，用于扫描模板路径下的所有模板文件并逐个生成。
画面5：在代码编辑器中，光标位于“String”类的自动补全列表中，准备输入“String”。
画面6：展示 Windows 文件资源管理器，路径为 E:\hrm，选中了名为“模板文件.txt”的文件。
画面7：在文件资源管理器中，选中了名为“新建文本文件.txt”的文件。
画面8：展示 Generator.java 文件中 generatorByDatabase 方法的注释和部分代码，用于根据数据库表生成模板。
画面9：展示 Generator.java 文件中 scanAndGenerator 方法的注释和部分代码，用于扫描模板路径下的所有模板文件并逐个生成。
画面10：在代码编辑器中，弹出“Select Classes to Import”对话框，选中了“freemarker.template.Template”类。
画面11：展示 Generator.java 文件中 processTemplateString 方法的注释和部分代码，用于处理模板字符串并生成输出。
画面12：展示 Generator.java 文件中 processTemplateString 方法的注释和部分代码，用于处理模板字符串并生成输出。
画面13：在代码编辑器中，光标位于“String”类的自动补全列表中，准备输入“String”。
画面14：展示 Generator.java 文件中 processTemplateString 方法的注释和部分代码，用于处理模板字符串并生成输出。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
import java.io.File;
import java.io.IOException;
import java.util.Map;

/**
 * 代码生成器的核心处理类
 * 使用Freemaker完成文件生成
 * @author
 * 数据模型
 * 模板的位置
 * 生成文件的路径
 */
public class Generator {
    private String templatePath;//模板路径
    private String outPath;//代码生成路径
    private Configuration cfg;

    public Generator(String templatePath, String outPath) throws Exception {
        this.templatePath = templatePath;
        this.outPath = outPath;
        //初始化Configuration对象
        cfg = new Configuration();
        FileTemplateLoader ftl = new FileTemplateLoader(new File(templatePath));
        cfg.setTemplateLoader(ftl);
    }
```

画面4：
```java
/**
 * 扫描生成
 * 1.扫描模板路径下的所有模板
 * 2.对每个模板进行文件生成（默认模板文件）
 */
public void scanAndGenerator(Map<String,Object> dataModel) throws IOException {
    //1.根据模板路径获取此路径下所有模板文件
    List<File> filelist = FileUtils.searchAllFile(new File(templatePath));
    //2.对每个模板进行文件生成
    for (File file : filelist) {
        executeGenerator(dataModel,file);
    }
}
```

画面8：
```java
/**
 * 根据数据库表生成模板
 */
public void generatorByDatabase() throws Exception {
    List<Table> tables = DatabaseUtilis.getTbInfo(db);
    for (Table table : tables) {
        //对每个table对象进行代码生成
        Map<String,Object> dataModel = getDataModel(table);
        for(Map.Entry<String,Object> entry:dataModel.entrySet()){
            System.out.println(entry.getKey() + "--" + entry.getValue());
        }
        System.out.println("........................");
    }
}
```

画面9：
```java
/**
 * 扫描生成
 * 1.扫描模板路径下的所有模板
 * 2.对每个模板进行文件生成（默认模板文件）
 */
public void scanAndGenerator(Map<String,Object> dataModel) throws IOException {
    //1.根据模板路径获取此路径下所有模板文件
    List<File> filelist = FileUtils.searchAllFile(new File(templatePath));
    //2.对每个模板进行文件生成
    for (File file : filelist) {
        executeGenerator(dataModel,file);
    }
}
```

画面10：
```java
// Select Classes to Import
// The code fragment which you have pasted uses classes that are not accessible by imports in the new context.
// Select classes that you want to import to the new file
freemarker.template.Template
```

画面11：
```java
/**
 * 1.读取文件模板
 * 2.创建文件
 * 3.模板处理（文件生成）
 */
public void processTemplateString(String templateString,Map dataModel) throws Exception {
    //1.字符串模板
    String templateString = "欢迎${username}";
    //2.创建模板
    Template template = new Template(name:"nam1",new StringReader(templateString),cfg);
    //3.处理模板
    Map<String,Object> dataModel = new HashMap<>();
    dataModel.put("username","张三");
    //4.处理模板
    template.process(dataModel,new PrintWriter(System.out));
}
```

画面12：
```java
private void executeGenerator(Map<String,Object> dataModel,file file) throws Exception {
    //1.文件路径处理
    String templateFileName = file.getAbsolutePath().replace(this.templatePath, replacement: "");
    //2.读取文件模板
    //3.创建文件
    //4.模板处理（文件生成）
}
```

画面13：
```java
public String processTemplateString(String templateString,Map dataModel) throws Exception {
    StringWriter out = new StringWriter();
    Template template = new Template(name:"ts",new StringReader(templateString),cfg);
    template.process(dataModel,out);
    return out.toString();
}
```

画面14：
```java
public String processTemplateString(String templateString,Map dataModel) throws Exception {
    StringWriter out = new StringWriter();
    Template template = new Template(name:"ts",new StringReader(templateString),cfg);
    template.process(dataModel,out);
    return out.toString();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

