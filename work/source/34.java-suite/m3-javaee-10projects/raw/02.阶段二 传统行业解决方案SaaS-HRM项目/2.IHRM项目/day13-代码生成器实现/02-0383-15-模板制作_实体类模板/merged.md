# 15-模板制作：实体类模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\15-模板制作：实体类模板_【海量资源尽在 ubkz.com】.mp4
- 时长 13分16秒（音频 796s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那我们现在呢已经把这个包和我们的工程的一些目录相关的内容咱们已经搞定了接下来呢我们就一个一个开始拙拙处理那首先呢我们去对实体类开始进行修改那对于我们来说呢实体类company.java那company其实我们都知道其实是不是就是通过表得到的类的名称啊所以要对这玩意儿先给它修改一下名称rename fill好了这个名称我们用什么dollar
[00:34] 大括号那名称呢我们专门通过class name的形式来进行了配置没错吧好了那这样一来PUGO我们已经搞定了那接下来类名呢咱们都知道那剩下就是关注我们这个里面的一些属性那属性首先第一个首先第一个那我们希望把这个类呢放到什么位置比如说呢我要放到com.ihm.注意这个路径不对啊点我们叫做
[01:05] companysostm抱歉点下的一个pojo这个包下才对没错吧所以我们要放到这个路径下那这个路径下首先咱们关注的是前面前面是不是应该是包名那这个包的名称是不是就是我们自己填写的这段内容没错吧各位OK那好了咱们继续往下看接下来name等于table这个是在配置jpa的配置那jpa配置里面这个是不是配置的是类跟表定式关系
[01:37] 那表是不是应该用表的名称来做啊OK也没问题好了接下来这玩意儿类名不多说了好了这边有一个serial relation的uid啊OK好了那这个uid来说呢我们一般不配置其实也可以用一个辅移默认值OK好了接下来底下这边有一个id剩下的这边全部都是它的属性当然了除了这些属性之外还应该有属性对应的guess i方法所以在这边我们把这些全部给它删掉那我们都得知首先要替换的是包名
[02:07] 那包名如何替换也不难$大括号那我们的包可以去找一下P package完整包名OK那接着这边表的名称大括号那表的名称就要从table里面获取了所以我这边拿的是table.表名nameOK那这样一来我们这边也配置好了那接着class
[02:36] 那class这个类名呢实体类的类的名称是不是跟我们这个文件名称是一模一样的所以我这边直接classnameok也没问题那好了剩下的事情我们关注的是中间的这些所有的属性那关注中间这些所有的属性所有的属性在哪咱们一起来看是不是在table的column4列表当中那我们这边就要去循环列表
[03:03] 那循环列表我们之前就学过一种方式学过一种方式是不是可以通过尖括号井号的这种形式来做好了list给它起一个名称table.column好了s-c-o-l-u-m-nOK咱们是要做粒子循环井号粒子结尾OK那好了
[03:37] 那中间我们关注的究竟是啥中间关注的内容呢其实比较简单了我们这样一来其实就是循环好了每一个column拿到里面的每一个对象那拿到每一个对象一个对象它代表的是一个属性private比如说呢privatepriprivate死菌类型的比如说叫ID那接着我们想方设法是不是得到当前这个column它的java类型以及当前这个属性的名称啊没错吧
[04:06] 好了那接下来我们如何去做我们已经循环了把每一个属性呢放到了column当中所以column代表的是就是当前的每一个column对象那每一个column对象我们关注的继续来看首先java类型column type好了接着$大括号column点这回关注的就变成了属性名称column2ok那这样一来我们这个属性其实也给它填写好了
[04:37] 那接下来我们想说的是对于GPA应用来说是不是还有一个叫做主件那主件从哪配置那注意我们是不是可以关注一下当前这一列这个列对象是否包含columnK如果有columnK并且它不为空我是不是给它可以来一个ID的一个属性啊所以在循环的过程当中我可以加一个if判断if那我这边的判断逻辑呢很简单c-o-l-u-m-n点注意
[05:07] column key 拷过来column key 拷过来问号问号就是在做判断看一下它是否为空井 ifok那这个判断的其实说明了什么呢就是当前这个column对象的column key属性如果这个key属性不为空它就能够进来如果为空就进不来那各位还有印象我往里存的时候呢是不是如果它不为空的话
[05:37] 我存了一个值如果它是主件的话我存了一个值只要存值是不是就不为空不为空那好了我这边来一个ata idok那这样一来我们的所有属性就已经构造好了那所有属性构造好了之后别忘了是不是还应该有get set方法那对于get set方法同样的跟这个逻辑一样private方法我们有了那接下来关注的就是get set当然了我们习惯先写所有属性接着底下是不是去写它的get set方法所以我再来一层循环
[06:07] 当然这个虽然浪费一点点效率但是符合我们的书写逻辑把所有属性罗列出来底下才写它的所有的get set吧OK好了这边就不需要判断了那我们关注的就是一个get set应该如何去写比如说呢public这是一个正常的set方法比如说set user name那我这边就可以传递过来一个参数比如说死菌类型的user name那我代码的写法
[06:40] 是不是就是类似点类似点user name等于user name当然了我这边不想用user name我用一个value来替换是不是也可以啊好了那接着除了set方法之外还应该有get方法那get方法呢这个get方法呢注意我先写扎娃代码咱们一会去做替换比如说呢返回此句类型的叫做get username好了这边没有参数那我直接return类似点user name
[07:16] 那我们接下来要做的事情是不是根据这个微模板咱们开始使用column对象当中的属性来进行替换没错吧首先我们先说这个死菌这个死菌是不是应该是我当前这个属性里面的类型那属性的类型是不是就可以column type替换过来没错吧好了那接着底下这边是不是也应该有类型能接受吧好了那接下来
[07:48] 那list.username那这回这个list.username是不是就应该是属性名称所以我属性名称拿过来来进行替换当然了底下这边也是属性名称来进行替换OK那接下来我们关注的是不是就是set username和get username那我们都知道这种形式得到的属性名称往往的首字母是小写的而我们这边关注的是不是首字母应该大写那这个没关系
[08:16] 咱们可以进行替换但是我先把这个给它构造出来OK但是这个并不符合我们的规则我们的规则是让它进行首字母大写的一个操作那对于首字母大写这个如何做很简单这边问号用它的一个内置函数First这样一来它就会把首字母进行大写了OK那这样一来我们的这个实体类这个模板也给它构造好了
[08:48] 那构造好了之后各位我们再去做一个测试测试之前把这个代码生成路径里面的这些所有的代码全部删掉好了注意走代码生成好了他告诉我生成成功那好了我们点进去来看包名呢我们之前处理过不关注了我们关注的是POJO好了我们看一下这边是不是什么地方报错了columncolumn tab
[09:23] 好了对于这个出现了一个小小的问题这个问题其实在FreeMarker里面经常常见那出现这个问题其实在FreeMarker它有一点点不太好的地方就是出现问题不太好调那我们可以一起简单的来看一下当然了从哪看呢注意我们关注的是代码生成的这个文件那我们都知道数据库表当中呢有很多个表那我们生成的实体类应该有很多个所以在这边我们找到POJO找到实体类实体类里面呢我们找到user
[09:54] 找到这几个对象全部给他打开我们一起来看一下好了首先我们关注CT没什么问题好了这个permission也没什么问题好了这边有一个user这边出问题了那各位来看对我们现在private死菌已经到了level这个字段那对照一下我们的数据库user从上面往下找找找一直到levellevel已经没问题了那是不是还有一个叫做我们的用户头像那用户头像后边是不是紧跟着是他的这个类型啊
[10:25] 所以我们这边我就可以知道了那我们这边哪出错了就是这个类型转化咱们没有配置那类型转化我这边通过FreeMarker程序是不是要把它转化为columnType那各位来看注意观察问题他说了有一个columnType没找到那这columnType我们在哪定义的是不是在TypeConvert这里面所以这边出现了问题咱们就应该这样去找那好了我们把这个给它填写过来
[10:53] 配成死剧那当然了除了这个之外呢其实还有很多咱们需要处理的这边都找一下吧比如说呢还有tinyint应该也没有那除了tinyint继续来看一下啊这边呢其他的内容看一下有没有了就找一些这些特殊的我没有做过处理来这边呢哎哎这边还有一个long text这些都要做处理好了当然了这边呢需要给它改成大写
[11:30] 使用一下快捷键这边呢勾上Ctrl Shift UU U那对于Tinyint来说呢我们把它转化成int类型的好了这两个呢就把它转化成死菌即可OK好了那接下来呢为了不影响我们这个测试啊我这边关掉重新再来一下启动好了启动了之后呢我们快速的把这些内容填充上root好了1 2 3 4 5 6走没问题接下来
[12:02] 找到数据库点击下一步好了代码生成路径再去填写一下这个就是有点麻烦但是是一个体力活测试勾选过来好了像名称我们叫compy包名呢我就叫做com.ihim.sostem了好了项目中名人人力资源好了作者itcast好了那接下来呢在这边把
[12:36] 之前生成的内容呢全部都删掉好了走重新生成一把好了那我们来看一下是否还报错啊好这回没有报任何的错误OK那接着我们来观察一下POGO是否已经全部都生成好了POGO哎各位来看都已经有了OK那这样一来其实我们的这个实例就已经生成好了咱们可以打开一个CT来看一下打开CT来看一下哎第一个at id没问题好了id name这边
[13:10] Data OK Ganser的方法也都有没错吧 OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用代码生成器（如Freemarker模板）自动生成Spring Boot项目的实体类（POJO）代码，包括配置数据格式、模板编写、调试和最终生成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 展示了“SaaS HRM”文档的第7页，标题为“(3) 数据格式”。
- 表格列出了数据格式字段：author（作者）、project（工程名）、path1（包名1）、path2（包名2）、path3（包名3）、pPackage（完整包名）、projectComment（工程描述）、ClassName（类名）、table（数据库信息）。
- 表格下方有“table中数据内容”子表，包含：name（表名）、comment（表注释）、key（表主键）、columns（所有列信息）、columnName（字段名列名）、columnName2（属性名）。

画面2：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`private String mailbox;`、`private String companySize;`、`private String industry;`等字段定义，以及对应的注释。

画面3：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`private String legalRepresentative;`、`private String companyPhone;`、`private String mailbox;`、`private String companySize;`、`private String industry;`等字段定义，以及对应的注释。

画面4：
- 展示了“SaaS HRM”文档的第7页，标题为“(3) 数据格式”。
- 表格列出了数据格式字段：path1（包名1）、path2（包名2）、path3（包名3）、pPackage（完整包名）、projectComment（工程描述）、ClassName（类名）、table（数据库信息）。
- 表格下方有“table中数据内容”子表，包含：name（表名）、comment（表注释）、key（表主键）、columns（所有列信息）、columnName（字段名列名）、columnName2（属性名）。

画面5：
- 展示了“SaaS HRM”文档的第7页，标题为“3.2 需求分析”。
- 内容包括“制作适用的Spring Boot程序的通用模板”，子项为“实体类”，并列出“类路径、类名、属性列表（getter, setter方法）”。

画面6：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`@Entity`、`@Table(name = "${table.name}")`注解，以及`public class ${ClassName} implements Serializable {`类定义。
- 代码中包含`<list table.columns as column>`、`<if column.columnKey??>`、`private ${column.columnType} ${column.columnName};`等Freemarker模板语法。

画面7：
- 展示了Windows资源管理器中的文件夹结构。
- 路径为：`.../ihrm/day13/资源/生成代码路径/ihrm_company`。
- 当前选中文件为`pom.xml`（XML文档，2 KB）。

画面8：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`@Entity`、`@Table(name = "${table.name}")`注解，以及`public class ${ClassName} implements Serializable {`类定义。
- 代码中包含`<list table.columns as column>`、`<if column.columnKey??>`、`private ${column.columnType} ${column.columnName};`等Freemarker模板语法。
- 底部显示了错误信息：`freemarker.core.InvalidReferenceException: ...`，提示`$column.columnType`在模板中未定义。

画面9：
- 展示了Notepad++中`Permission.java`文件的内容。
- 代码片段显示了`@Entity`、`@Table(name = "bs_permission")`注解，以及`public class Permission implements Serializable {`类定义。
- 代码中包含`private String id;`、`private String userId;`、`private String companyId;`、`private String administratorName;`、`private String managementModule;`等字段定义，以及对应的getter/setter方法。

画面10：
- 展示了Notepad++中`User.java`文件的内容。
- 代码片段显示了`private String mobile;`、`private String username;`、`private String password;`、`private Integer enableState;`、`private java.util.Date createTime;`等字段定义，以及对应的getter/setter方法。
- 画面中还显示了多个窗口的缩略图，包括IntelliJ IDEA、Notepad++、PDF文档等。

画面11：
- 展示了IntelliJ IDEA中`$ClassName.java`文件的内容，是生成的实体类模板的一部分。
- 代码片段显示了`@Entity`、`@Table(name = "${table.name}")`注解，以及`public class ${ClassName} implements Serializable {`类定义。
- 代码中包含`<list table.columns as column>`、`<if column.columnKey??>`、`private ${column.columnType} ${column.columnName};`等Freemarker模板语法。
- 底部显示了错误信息：`freemarker.core.InvalidReferenceException: ...`，提示`$column.columnType`在模板中未定义。

画面12：
- 展示了IntelliJ IDEA中“代码生成器 1.0”对话框。
- 对话框中“模板”下拉框选中“Spring Boot程序的模板”。
- “项目名（英文）”为“company”。
- “包名”为“com.ihrm.system”。
- “项目中文名称”为“人力资源”。
- “作者”为“Root”。
- “用户名”为“root”，“密码”为“111111”。
- “生成代码”按钮被点击。

画面13：
- 展示了IntelliJ IDEA中“代码生成器 1.0”对话框。
- 对话框中“模板”下拉框选中“Spring Boot程序的模板”。
- “项目名（英文）”为“company”。
- “包名”为“com.ihrm.system”。
- “项目中文名称”为“人力资源”。
- “作者”为“Root”。
- “用户名”为“root”，“密码”为“111111”。
- “生成代码”按钮被点击。

画面14：
- 展示了Notepad++中`City.java`文件的内容。
- 代码片段显示了`@Entity`、`@Table(name = "bs_city")`注解，以及`public class City implements Serializable {`类定义。
- 代码中包含`private String id;`、`private String name;`、`private java.util.Date createTime;`等字段定义，以及对应的getter/setter方法。
- 代码中包含`public void setId(String value) { this.id = value; }`、`public String getId() { return this.id; }`、`public void setName(String value) { this.name = value; }`、`public String getName() { return this.name; }`、`public void setCreateTime(java.util.Date value) { this.createTime = value; }`、`public java.util.Date getCreateTime() { return this.createTime; }`等方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面6代码：
```java
@Entity
@Table(name = "${table.name}")
public class ${ClassName} implements Serializable {
    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>

    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>
}
```

画面8代码：
```java
@Entity
@Table(name = "${table.name}")
public class ${ClassName} implements Serializable {
    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>

    <list table.columns as column>
    <if column.columnKey??>
    @Id
    </if>
    private ${column.columnType} ${column.columnName};
    </list>
}
```

画面9代码：
```java
package com.ihrm.system.pojo;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;
import java.io.Serializable;

@Entity
@Table(name = "bs_permission")
public class Permission implements Serializable {

    @Id
    private String id;
    @Id
    private String userId;
    private String companyId;
    private String administratorName;
    private String managementModule;

    public void setId(String

