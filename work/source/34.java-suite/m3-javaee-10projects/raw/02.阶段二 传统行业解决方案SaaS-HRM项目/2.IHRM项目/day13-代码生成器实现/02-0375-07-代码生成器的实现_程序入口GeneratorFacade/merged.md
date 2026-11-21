# 07-代码生成器的实现：程序入口GeneratorFacade

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\07-代码生成器的实现：程序入口GeneratorFacade_【海量资源尽在 ubkz.com】.mp4
- 时长 9分24秒（音频 565s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 对我们代码生成这两个类做了一个简单的介绍那我们接下来呢就把这个代码给它完善出来首先呢第一个就是Generator Fix那Generator Fix它的主要目的采集用户UI界面的这些数据那这些数据只需要给我创建这个对象的过程当中给我传递过来其实就可以了那我们如何去做呢其实也不难来咱们一起把它完成那首先我需要的几个属性我把这几个属性呢就以
[00:33] 属性的形式就以私有属性的形式配置到它的方法配置到这个类当中好了首先呢第一个就是我们模板的位置死菌类型的我就叫做temp t e m t e m p l a t e passok那好了接着第二个private死菌类型的我叫做autopass就是输出的路径好了接着第三个死菌类型的我就不叫死菌类型了setting
[01:08] SETTNGSetting别选错包Settings别选错包SettingOK那接着第四个private好了我这边叫做Database就叫DB了那接下来呢这几个值呢我不习惯用复制的set方式的形式复制了我这边就写一个构造方法当你创建这个对象的时候把这些参数给我传递过来即可来一publicpublicOK
[01:45] 好了这边用一下生成吧再把生成一下contractor所有内容control c control v全部给我拿过来那这样一来呢其实当你创建对象的时候已经把这些值给我附上了那我们构造方法写好了接下来呢我们就是关注的数据库的一些数据关注的就是如何去构造这个数据模型
[02:12] 那构造数据模型这边呢我也可以写一个我们自己的方法public will id这个方法呢比如说就叫做denerator就是by data base好了这边呢来一个source exception好了那我们写了一个方法那对于这个方法我们要做的事情我这边呢简单的和各位说一下其实这里面要做的事情呢就只有这么两个方面第一个呢就是准备数据模型
[02:50] 第二个呢就是调用核心的处理类完成代码的生成工作OK那这两个方法呢这个方法写起来呢其实相对来说比较简单它也不难那我们的数据模型之前呢做个分析一共有三部分内容第一部分第二部分第三部分没错吧好了那接下来我们就开始一起来看一下如何去做首先我们拿到原数据那对于原数据的处理我们有一个Data
[03:23] base utils打点打点get dbinfo把db传递进去那这样一来我们得到了所有的table列表那所有table列表里面包含的其实就是一个数据库当中所有的表的信息那对于我们生成代码的时候比如说实体类叫user比如说实体类叫city比如说叫company那一套表
[03:51] 一个表是不是要创建这么一套模型啊所以我生成模型的时候这边是不是应该来一个for循环的形式进行生成没错吧所以这里面要对每一个table对象进行代码生成这个应该各位也能理解好了那接下来那我这个要对每一个table对象进行代码生成的时候那这个时候我们要关注的其实就是
[04:24] 数据模型第二个调用generator这一言一啊 a a a t o r核心处理类好了那对于数据模型数据模型这个数据模型一个table咱们就需要构造一个一个table咱们就需要构造一个所以在这边我去构造一个数据模型我们都知道数据模型对于我们而言全部都是死菌类型的ok 好了我比如就叫做data model
[05:06] OK 以下包比如说这边呢为了让我们代码看起来简洁一些我把它抽象到一个方法比如说就是getDataDataModel好了 对于这个DataModel而言我们是根据table生成的所以我在底下写一个我自己的方法table对象获取数据模型public写的严谨一点吧private好了 这边getDataModel传递过一个table过来
[05:46] dble好了那在这个里面呢我们要做的事情呢其实比较简单等于new一个hashi map好了底下为了不报错我先把它返回好了那我们中间要处理的部分其实就是一个数据模型我们刚才分析的三部分内容有自定义配置有原数据有settingok那对于自定义配置我们往里存放datamodel.
[06:24] put那我们放到哪了呢是不是放到了一个propertyutils打点castmap自定义的数据好了接着原数据那原数据datamodel.put注意我直接把这个table对象存进去了那我们一会要用的时候我们一会要用的时候是不是要加一个table
[06:52] 这个节点的名称啊所以说如果用名称是不是就table.nametable.name等等好了接着还有settingdatamodel.put那我们这边这个setting呢各位来看是一个对象那这个对象当中有很多的内容有很多的内容那我由于这个setting对象用起来可能比较特殊啊我就不把这个setting对象放进去了注意在这个setting当中我写了一个get setting map
[07:22] 我把setting当中的所有属性以key value的形式给它获取到这里面我写了一个简单的一个方法其实就是通过反射得到当前对象里面的所有的属性名称接着以属性做key value做value的形式给它存放到一个map集合里面并且获取到OK所以在我这边在我这边直接拿到类似点settings打点
[07:51] get setting map那这样一来我已经把自定义的配置放进去了原数据放进去了setting放进去了那这边呢我想跟各位做一个简单的说明这个说明是这样的就是说那我很多地方都可能要用到你生成的列明那这个列明我们之前都知道是不是给它放到这个table里面了那所以我一会儿要用的时候是不是就应该是table打点关注一下列明
[08:19] 就这实体名是不是就应该是这样的table.抱歉table.name2那这个写法呢其实写起来有点太麻烦了那我就专门再去抽取一个类名给它直接放到我们的根结点下所以data model打点put我就来一个class name那这class name其实就是用table.get name2来用
[08:54] 就可以了当然这边不能用putall了OK那这样一来我们已经获取到了数据模型那获取到了数据模型之后我们就可以完成这个代码调用的这个工作那调用代码用的是genorator来进行调用的所以我在这边在这边咱们要想方设法new出来genorator调用里面的方法完成操作没错吧OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个 Java 代码生成器（GeneratorFacade）的实现过程，包括配置类、数据库连接类和核心生成逻辑的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 GeneratorFacade.java 文件的初始结构，包含类定义和注释，说明其职责是“程序配置对象”、“数据库对象”、“自定义配置”、“元数据”、“setting”和“调用核心处理类完成代码生成工作”。
画面 2: 展示 GeneratorFacade 类的 import 区域，导入了多个 Java 标准库和并发工具类。
画面 3: 展示在 import 区域中，选中并导入了 cn.itcast.generate.entity 包下的 Database 类。
画面 4: 展示 GeneratorFacade 类的构造函数，定义了 templatePath、outPath、settings 和 db 四个私有成员变量，并在构造函数中初始化它们。
画面 5: 展示在构造函数下方，添加了 public void generatorByDatabase() throws Exception 方法的声明。
画面 6: 展示在 generatorByDatabase 方法中，调用 DatabaseUtils.getDbInfo(db) 获取数据库表信息，并在 IDE 中提示需要输入参数。
画面 7: 展示在 generatorByDatabase 方法中，使用 for 循环遍历 List<Table> tables，并在循环体内添加注释“遍历每一个Table对象进行代码生成”。
画面 8: 展示在循环体内，调用 getDataModel(table) 方法，并在 IDE 中提示需要输入参数。
画面 9: 展示在 getDataModel 方法中，调用 ReturnInstruction 类的 getReturnInstructionType 方法，并在 IDE 中提示需要输入参数。
画面 10: 展示在 getDataModel 方法中，定义了一个 Map<String, Object> 类型的变量 dataModel，并在 IDE 中提示需要输入参数。
画面 11: 展示 Settings.java 文件，定义了 Settings 类的私有成员变量，包括 project、pPackage、projectComment、author、path1、path2、path3、path4。
画面 12: 展示 Settings.java 文件，定义了 Settings 类的构造函数，对 pPackage 进行空值判断和路径分割处理。
画面 13: 展示 Settings.java 文件，定义了 getSettingMap 方法，用于获取配置信息。
画面 14: 展示 GeneratorFacade.java 文件，定义了 getDataModel 方法，用于获取表对象的模型信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 程序配置对象
 * 数据库对象
 * 1.自定义配置
 * 2.元数据
 * 3.setting
 * 3.调用核心处理类完成代码生成工作
 * 方法：Generator
 */
public class GeneratorFacade {
    private
}
```

画面 2:
```java
import java.lang.*;
import java.util.*;
import java.security.*;
import java.nio.charset.*;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.*;
import java.util.concurrent.atomic.*;
import java.util.concurrent.locks.*;
import java.util.function.*;
import java.util.stream.*;
import java.util.regex.*;
import java.util.zip.*;
import java.util.jar.*;
import java.util.logging.*;
import java.util.spi.*;
import java.util.concurrent.atomic.AtomicBoolean;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.atomic.AtomicLong;
import java.util.concurrent.atomic.AtomicReference;
import java.util.concurrent.atomic.AtomicReferenceArray;
import java.util.concurrent.atomic.AtomicMarkableReference;
import java.util.concurrent.atomic.AtomicStampedReference;
import java.util.concurrent.atomic.AtomicLongArray;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicIntegerFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLongFieldUpdater;
import java.util.concurrent.atomic.AtomicBooleanFieldUpdater;
import java.util.concurrent.atomic.AtomicReferenceFieldUpdater;
import java.util.concurrent.atomic.AtomicLong

