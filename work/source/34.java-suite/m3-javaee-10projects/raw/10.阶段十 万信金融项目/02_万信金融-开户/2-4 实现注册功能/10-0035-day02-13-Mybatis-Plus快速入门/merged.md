# day02-13-Mybatis-Plus快速入门

- 阶段：10.阶段十 万信金融项目
- 章节：02_万信金融-开户/2-4 实现注册功能
- 源文件：10.阶段十 万信金融项目\02_万信金融-开户\2-4 实现注册功能\day02-13-Mybatis-Plus快速入门_【海量资源尽在 666java.com】.mp4
- 时长 16分35秒（音频 995s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 刚才呢我们整体上了解了一下MP那后边呢咱会经常用MP慢慢你会发现呢它会成为我们程序员的好基友那由于MP呢它上手非常快也非常简单所以说呢咱这直接来个快速入门首先呢我们要准备数据库还有表因为MP是对数据库进行操作的所以我们要把这个准备工作做一下
[00:30] 我们创建一个数据库名字就叫MP编码你要注意选择UTF-8数据库创建完之后我们这给大家提供了有脚本我们会创建一个用户表这里边有一些字段然后会插入几条测试数据这个大家直接粘贴到速度样里边一执行就完事你看我这边都已经执行过大家看最终会有这么一个表
[01:01] 里面呢有些测试数据一会儿呢我们就会对这个表进行增删改查这是我们做的一个准备工作吧我就不再过头说了那咱接下来呢是不是需要准备一个Spring Boot工程在这个工程里面呢我们会使用MP进行数据库的一些操作那么至于这个搭建工程的这个过程呢我就不再演示了这些呢对于大家来说都非常熟我这儿呢直接已经搭建好了大家看一下
[01:31] 这个名字叫atcast-mp-Spring Boot那这里边最基本的一些东西呢我都已经提供过了只是一个框架里边好多代码都是空的那这个工程呢大家创建好之后呢我们首先要做的第一件事是不是导依赖是不是引用依赖主要是引入跟mp相关的一些依赖那咱看看啊咱这里边啊都需要引入哪些依赖咱通过讲义呢快速的过一遍
[02:01] 首先呢是引入了一个Long BookLong Book呢这个大家前面应该接触过吧Long Book呢通过它的一些注解我们可以在编写实体内的时候不用自己再动手编写什么getter setup方法啊有参无参勾到方法啊加一些注解那它会帮我们自动生成getter setup方法还有无参有参勾到方法咱一会儿编写实体内的时候大家看一看然后呢就是这个mybattles plus相关的这个依赖
[02:29] 这是他跟Spring Boot整合的一个包版本我们用的311自然我们由于要进行数据库操作也离不开数据库驱动我们这导入了一个MySQL的驱动包下面这些是日志等等这个依赖其实就这么多我们看我们提供的这个工程里面这些依赖导了没有我们看这些依赖是不是都已经导过了这些代码你不用敲你直接粘过去就行了知道他们都是什么意思就OK了这时候我们要导入什么
[02:58] 先导入依赖依赖导入之后咱接下来跟我们学习别的框架是一样的我们接下来是要搞配置对不对搞配置就是这个application.purpose这个配置那咱找一找咱工程当中的这个配置就是它了打开那么现有的一些配置呢都是咱见过的啊我直接提供给大家了大家看一下首先这是不是那个应用程序的名字对不对
[03:28] 这不再说了然后这次好像大家应该比较熟悉了是不是数据库连接的相关信息比如说驱动类比如说这个数据库连接字符串对吧我要连接哪台电脑上的哪个数据库是不是后边就是一些这个编码的一些设置然后这是我们的账号和密码这个你不能照抄啊你的密码是多少你这就写多少就行那这是我们以前吧经常要配置的一些这个代码
[03:56] 那么现在我们是不是要用MP这个框架对不对那么在用MP框架的时候呢我们要增加一些跟MP相关的一些配置都有哪些配置呢咱看一看讲义很简单就两个就两个大家看一下首先呢我们要增加一个配置叫mybattles-plus.Mapper-locations这个呢是用来设置什么呀有一个文件叫映射配置文件大家还有印象吗
[04:26] 就我们是不是将来会定一个Map接口然后呢Map接口会对应一个映射配有链有印象吗对我们这儿呢是配置这个映射配有链所在的路径的那我们在咱这个工程当中啊我准备把这个映射配有链呢全部都放到Resource下边Resource下边我新建了一个子文件夹叫MyBalance我准备全部放到这个文件夹里那因此呢你看我们这儿的这个配置这个值对不对
[04:56] 你是不是就卖Battis下边这个卖Battis就是这个卖Battis下边所有的什么呀星码所有的这个镜像配置软件全部让他扫描到啊所以说我们需要增加这么一个配置这是第一个配置啊第一个配置啊然后还需要增加一个配置这个配置呢是用来扫描这个实体类的实体类那么我们这个工程当中呢所有的实体类呢我们准备放到POGO这个包里
[05:26] 所有的实体类当然我们这个入门案例当中呢只有一个实体类这个实体类是不是就对应咱刚才这个谁啊对TB下航线user这个表对应他的那扫描这个实体类干嘛扫描这个实体类是因为我们要给他注册编名每个实体类我们都有都可以注册一个编名那这个编名呢将来我们在某些地方用的时候呢你就不用写这个类的全路径名
[05:52] 对不对直接写别人就想了用起来更方便当然你不配也可以啊你不配的话你将来就用它的全路径名就可以了所以我们加这么一个配置那么我们在使用MP的时候呢只需要增加这两个配置就够了其他的配置我们不用管暂时是用不着的这是咱搞一些配置配置搞完之后呢咱接下来还要做一个准备工作就是要编些什么呀实体类我们刚才说了这个实体类是不是就是跟这个
[06:26] tb下方有点这个表对应了这个实体应该这里边有一些字段吧我们需要写一些这个类这个类大概长什么样的咱先抽抽讲义过一遍然后咱自己编写一下你看这个类的名字呢你可以自己定义啊我就起个名字叫user在这里边有一些属性对不对然后大家整体观察一下我这个类当中有没有写什么getter search方法无参有参各种方法没有编写了没有编写不代表它不存在那这样呢我们就要用到
[06:55] 前面我们提到过呢有有一个工具叫什么叫LambookLambook就是它那么它呢也提供了一些注解可以帮我们生成这些方法哪些注解呢叫Add Data这个注解是帮我们生成Get-A-Third方法那这俩注解你应该能看出来见名之一了干啥了呀你看看名字能看出来吗干嘛了呀对这个表示要生成无参构造方法
[07:27] 这个是要生成代餐的主导方法所以说你看用longbook的这个注解我们是不是很省事对不对然后再往下你看这些注解都是干嘛的这些注解其实是用来配置我们这个类跟哪个表对应以及类当中的属性跟表里边的哪个字段进行对应的这个其实专业术语叫ORM映射就是对象关系映射有了这个映射之后呢我们就不用编写搜索语句了
[07:59] 不用编写搜索语句啊我们用MP的时候就是最基本的一些操作增加解码操作我们是无需编写搜索语句的这跟以前这个my balance相比是不是就方便了很多是不是你不用编写搜索语句那不用编写搜索语句他怎么知道我们要干啥呢那这样的你要注意就是我们配的这些东西非常关键他根据这些注解他就知道你操作了哪个对象相当于他就知道是操作哪个边你操作了哪个属性
[08:30] 他相当于就知道他要操作哪个子段啊这个咱到时候出效果的时候再说啊那咱现在呢先把这个实体类呢我们快速编写一下在PUGU这个包里边呢我们新建一个类就叫user吧然后呢我们是不是要编写一些这个属性吧private有一个叫什么呀叫id的我们都用这个这个什么包装类
[09:02] 这个属性有点多啊还有什么呀privatestringusername还有什么呀privatestringpassword密码还有什么呀然后姓名stringname对不对还有什么还有年龄嘛年龄的话我们用也用包装类吧intgintegerag对不对
[09:36] 然后最后一个是我记得应该是啥这个你可以参考这个表了对不对你看是不是还有一个什么电子邮件吗EM A I L E M 没了然后咱开始加刚才说到那些注解首先就是at data注解让它生成给的算法然后就是no args constructors它是生成无参构造方法然后再来一个叫奥什么奥
[10:07] 是生成代餐的做到方法然后呢我们开始加这个跟表之间这个映射关系的这些注解首先这个类呢要对应一个表这个注解叫table name对应的表名呢我们要放到这个小果号里边它叫什么呀tb下滑线user对不对你检查一下啊tb下滑线user然后呢每个属性这里边每个属性是不是都对应里边的
[10:39] 一个字段是不是那我们这也要进行用注解进行配置那第一个这个ID呢它比较特殊啊你要注意这个ID是主件主件这个字段用哪个注解来配呢它叫at table IDat table ID这个小果号里边呢你就写这个字段名又想了这个字段名不就是不就叫什么呀就叫ID嘛对不对那如果是非主件的字段我们应该用这个注解啊叫table
[11:09] table field对就是这个啊那小口号里边也是写什么呀对写这个字段名比如说叫user下滑线name打下写无所谓那后边这些都一样嘛对这些都一样我就不再挨个给大家进行编写了啊后边这些呢我就直接粘过来都一样然后最后还有一个什么email这是我们把什么呀这个实体类
[11:52] 编写完了吧对该家的注解也都已经加上了啊这是实体类咱就搞定了实体类搞完之后呢呃大家回忆一下我们这个之前学习过的mybillis对于mybillis来说他最重要的是不要写一个map接口还要提供一个相对应的映射配置文件对吧那接下来呢要编写这个map接口呃我们就放到这个map这个包里边新建一个接口啊接口
[12:23] 新的名字就叫userMapper其实对于mybass来说我们其实定义这么一个接口基本上就完事对不对但是我们现在用的是MP用MP的时候这个接口不能这么定义怎么定义呢大家看一下在使用MP的时候呢我们自定义的这个接口要继承MP提供的一个接口叫BassMapper而且呢这儿要指定那个实体类作为范形为什么要继承它呢咱先把这个代码先编写了然后我们再
[12:55] 说这个事啊叫什么呀叫basemapper啊范形呢就是咱刚才那个实体类就叫什么呀对就叫user为什么我们一定要继承这个接口呢那你去这个接口里边瞅一眼不就行了吗跟踪一下他这个啊这个basemapper这个代码是不是我们搜一下b a s e m a p p e啊是他吧对然后你看这里边哎我们把他的方法调出来
[13:26] 你看这里边放你大家自己过一遍吧这些发射名都是见名之义的是不是我们平时最常用的增伤改善那些方法在这个base map这个接口里边是不是全部都定义好了你看是不是有删除的有添加的有查询的对不对还有什么呀更新的是不是那你现在告诉我我们在定义接口的时候为什么要继承MP的这个接口为什么
[13:51] 对我们一旦继承这个接口咱自己定的这个接口里边是不是就已经有了那一堆增删改成那些方法明白什么意思吧所以就很方便嘛你也不用写什么搜寄语句不用搜寄语句将来它会生成它怎么生成啊就是根据这些注解这些注解是不是配置了我们的类跟这个表以及我们的属性跟字段之间的这个应声关系有了这个关系它能帮我们生成搜寄语句算非常方便
[14:20] 这个接口定义好之后呢咱们接下来还要提供跟他相配套的这个什么呀映射配置文件这跟当时这个谁啊Mapis基本上没有啥区别是不是那这个映射配置我们前面说了我们要放到什么地方是不是要放到这个Mapis这个文件夹里的在哪在这我们需要在这呢建一个XML文件啊我们起个名字就叫userMAPPR吧第二XML
[14:57] 那如果你你这不能生成这套东西的话你就从讲义里边干什么呀对从讲义里边直接这块复制过去就行了那我们唯一需要改的是这个地方这是要写啥是不是要写那个接口的那个那个全路径是不是cn点itcast点mp点就叫什么呀还有一个Mapper对吧点就可以啊这个映射配置文件就搞定了那最后呢我们再修改一下什么呀
[15:28] 启动类就行了启动类上呢其实你只需要加这么一个注解就是MapScan这个咱以前应该也学过就是设置一下这个Map接口所在的那个包的路径好让它扫描到这个什么呀Map接口然后生成了什么呀代理对象吧对不对所以我们只需要加上这么一个配置就OK了咱找一下咱的这个启动类在哪启动类这个啊在这儿呢我们加上这么一个配置就行了
[15:57] 你要检查一下这个路径对不对啊是不是没错吧对不对那这目前的话咱们就在入门案例的这工程当中啊把MP相关东西是不是全部加上去了有碰母件当中的依赖还有什么呀还有一些配置是不是还有什么对实体类还有接口以及对应的什么对映射配置这套东西全部搞好搞好之后呢一会儿咱就写一个测试用力
[16:28] 来给大家展示一下这个增长改查里边的一些基本功能吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 MyBatis-Plus 框架在 Spring Boot 项目中配置数据库连接、定义实体类、编写 Mapper 接口及对应的 XML 映射文件。

2) 按时间顺序列出每张画面的要点：
画面 1: 创建名为 "mp" 的数据库，字符集为 "utf8 -- UTF-8 Unicode"。
画面 2: Maven 项目导入依赖，显示 "ArtifactId: icast-mp-Spring Boot"，版本 "1.0-SNAPSHOT"。
画面 3: 展示 `pom.xml` 文件内容，包含 Spring Boot、MyBatis-Plus、MySQL 等依赖配置。
画面 4: 展示 `application.properties` 文件内容，配置了 Spring Boot 应用名、数据库驱动、连接 URL、用户名和密码。
画面 5: 展示 `application.properties` 文件内容，包含数据库配置和 MyBatis-Plus 的配置项，如 `mybatis-plus.type-aliases-package`。
画面 6: 展示 PPT 页面，标题为 "2.2.5 编写 Mapper 接口和配置文件"，并显示了 `User` 类的注解说明。
画面 7: 在 IDEA 中新建 `User.java` 文件，准备编写实体类。
画面 8: 在 `User.java` 中导入 `lombok.Data` 注解。
画面 9: 在 `User.java` 中添加 `@TableId` 注解，指定主键字段。
画面 10: 在 `User.java` 中为其他字段添加 `@TableField` 注解，指定数据库列名。
画面 11: 在 IDEA 中新建 `UserMapper.java` 文件，准备编写 Mapper 接口。
画面 12: 展示 PPT 页面，标题为 "2.2.6 修改启动类"，并显示了 `MyApplication` 类的导入语句。
画面 13: 展示 `mybatis-config.xml` 文件内容，包含 MyBatis 的配置信息。
画面 14: 展示 `User.java` 文件内容，已添加 `@TableId` 和 `@TableField` 注解。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 3:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
    <scope>test</scope>
</dependency>
<!-- 自定义代码的工具包 -->
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>
<dependency>
    <groupId>com.baidou</groupId>
    <artifactId>mybatis-plus-boot-starter</artifactId>
    <version>1.1.0</version>
</dependency>
```

画面 4:
```properties
spring.application.name=icast-mp-Spring Boot
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true
spring.datasource.username=root
spring.datasource.password=123
```

画面 5:
```properties
spring.application.name=icast-mp-Spring Boot
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/mp?useUnicode=true&characterEncoding=utf8&autoReconnect=true&allowMultiQueries=true
spring.datasource.username=root
spring.datasource.password=123
# 设置Mapper接口所对应的XML文件位置，如果放在Mapper接口中自定义方法，需要进行动态配置
mybatis-plus.Mapper-locations=classpath:mybatis/*.xml
# 设置每个包扫描路径，通过注解属性可以给包中的类注解别名
mybatis-plus.type-aliases-package=cn.itcast.mp.pojo
```

画面 6:
```java
@TableId("ID")
private Long id;
private String userName; // 姓名字段，但无需注解
private String password;
private String name;
private Integer age;
private String email;
```

画面 7:
```java
package cn.itcast.mp.pojo;
```

画面 8:
```java
import lombok.Data;
```

画面 9:
```java
@TableId
private Long id;
```

画面 10:
```java
@TableId("id")
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
```

画面 11:
```java
package cn.itcast.mp.Mapper;
import com.baidou.mybatisplus.core.Mapper.BaseMapper;
public interface UserMapper extends BaseMapper<User> {
}
```

画面 12:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.mp.Mapper.UserMapper">
</Mapper>
```

画面 13:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
        "http://mybatis.org/dtd/mybatis-3-Mapper.dtd">
<Mapper namespace="cn.itcast.mp.Mapper.UserMapper">
</Mapper>
```

画面 14:
```java
@TableId("id")
private Long id;
@TableField("user_name")
private String userName;
@TableField("PASSWORD")
private String password;
@TableField("NAME")
private String name;
@TableField("AGE")
private Integer age;
private String email;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 5: PPT 标题为 "2.2.4 编pojo"，内容包含 MyBatis-Plus 的配置说明。
画面 6: PPT 标题为 "2.2.5 编写 Mapper 接口和配置文件"，内容包含 `User` 类的注解说明。
画面 12: PPT 标题为 "2.2.6 修改启动类"，内容包含 `MyApplication` 类的导入语句。

5) 不要评价画面美观，不要输出与课程无关的内容。

