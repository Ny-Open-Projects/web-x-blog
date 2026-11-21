# 11.新增房源服务实现之AutoGenerator使用以及创建pojo对象

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\11.新增房源服务实现之AutoGenerator使用以及创建pojo对象【海量资源尽在 ubkz.com】.mp4
- 时长 13分38秒（音频 819s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢我们就开始做编码的工作那么首先呢要做的呢就是我们要编写这个pozo那么我们呢首先呢需要去给这个pozo呢就是我们后面所要写的pozo给它一个附类叫base pozo那么在这个里面呢可以去写一些它们一些通用的一些这个属性那么其实我们可以看到在这个base pozo中啊
[00:25] 它其实是有两个属性一个是created,一个是update那么也就意味着我们后面的一些Pozo所继承BasePozo的话那么它都会有这两个属性那么也就意味着你的表中是不是都会有这两个字段OK好,那么我们把它创建出来那么这个Pozo在哪里创建我们来看一下是不是要回到我们 interface是不是这个里面来好,那么在这我们去创建一个包
[00:54] 就是pojo这个包把这个包我们去包名拷贝一下然后在这点击右键new一个package然后去创建一个pojo这个包然后我们把代码拷过来那么其实可以看到在代码中我们使用的是不是就是一个data在那个注解它会帮我们自动去生成这get和set的方法并且我们可以发现的是
[01:24] 我们的这个base puzzle它实现了一个可序列化的一个接口然后呢这个为什么要去实现它的原因是不是我们前面那个double所要去传输这个对象的时候要求必须去实现这个序列化的接口所以我们要去实现它好嘞那么这个我们就搞定了对吧base puzzle就搞定了那么下面我们是不是就可以去写我们的一些具体的一些puzzle了对吧比如说像我们的这个房源对吧以及我们的这个
[01:53] 楼盘对吧楼盘数据那么是不是都要去写对应的一个poll那么如果我们去手动一个一个去写非常的麻烦前面我们在讲这个plus这个工具或者这个plus这个插件的时候那么提到过他也提供了一个功能是不是就是帮我们去自动生成我们代码那么我们就接下来来使用一下这个自动生成这个代码这个功能那么为了不去干扰我们的这个项目那么我们在
[02:21] 再来创建一个新的项目去实现这个功能那么就叫server下面再来创建一个吧这个工程就叫generator这个工程把它拷贝一下然后呢我们在这个double server这个下面创建一个module然后呢我们选择它然后呢下一步然后把它贴过来好然后呢下一步然后呢把它贴过来finish完成是不是我们又创建了一个工程啊这个工程其实目的呢就是来去生成一下
[02:49] 生成一下我们所需要的一些代码就做这么简单的一个工程好那么我们把具体的这个具体这个POM文件的依赖拷过来那么在生成的这个在生成我们这个代码的时候它所需要一个叫frame mark这样的一个模板引擎所以我们把这个给它拷过来那么它需要什么就给它提供什么就好了好那么这个就搞定那么下面我们来编写一个它的一个
[03:18] 代码这个代码呢就不要求大家去去写了对吧那么我这个代码呢也是去拷贝的官方的这个失利中的一个代码做了一些这个修改所以呢我们就直接来做一个拷贝啊那么把就拷这个吧把这个拷一直往下面拷拷到先拷到这然后呢我们把它不能这么拷得得这么来这样吧先我们创建一个类吧
[03:47] 先创建一个class然后呢我们在这个class中再去拷贝它那个代码然后呢从这儿然后呢一直到下面的这个位置然后呢拷到这儿然后我们继续往下面拷从这个位置一直往下面拷拷到这儿结束好嘞把这个代码贴过来好那么我们整理一下代码把一些相关的一些包我们都拷进来那么把这个包这个是
[04:18] 这个是我们的util下面的然后呢street utils这个呢我们使用这个浪包下面然后呢这个呢是抛出的mybatties的这个异常mybatties plus这个异常那么这个下面是没有mybatties我看一下啊它缺少mybatties没有这个依赖就缺少这个依赖那么也就是说我们这个GDREAD这个工程缺少依赖那我们来给它去
[04:52] 考虑一下依赖吧那么在复工程中注意在这个server复工程中是不是这个没这个里面他所需要的依赖我们来看一下外面有没有这个里面也没有那么在这个下面来看一下这个下面需要把这个myvictus的插件依赖的拷过来这两个也都需要我们都给他贴过来是在generator这个里面generator在这
[05:22] 好,靠过来然后呢它就可以去使用到了因为它肯定是需要这个MyBed Plus这样的一些插件才能够去执行对吧好,那么这个是回撤的问题那么来给它解决一下然后等于这个有空格这个格式有点问题简单调一下把这个调一下等于TF8调一下
[05:54] 有多了一些空格咱们把这个格式呢调一下然后呢就OK把它拿掉好那这样的话呢我们这个连接这么串就基本上搞定了对吧还有报错的地方吗是不是就没有报错的地方了好那么应该没有吧还有吗多了一个多了一个括号多了括号好那么现在呢我们这个代码呢就已经已经整理完了那么其实我们需要来
[06:26] 观察或者说我们需要去关注啊这么几个呃配置啊或者几个位置的代码那么像这个呢是他生成我们这个代码的一个目录啊然后呢再是一个作者啊然后这个是我们的数据库的一个连接啊那么把这个也拿上去吧这个封号啊封号啊封号拿上去好这个是我们数据库连接是不是连接到我们这个号客啊这个数据库然后呢一个下面是一个驱动
[06:56] 以及这个用户名和密码然后下面是我们去生成我们的一些这个模块名然后去写我们自己的一个parent设置一个这个parent然后下面这个是设置的一些这个模板这个其实我们就不用去管它了然后下面这个是我们设置我们的一些这个叫什么
[07:21] 复类是吧就是我们生成这个posal它的一个复类就是baseposalok那么Controller呢是一个basecontroller当然我们现在还没有Controller先这么去写好的我们先来执行一下吧运行一下那么看一下它的一个效果我们去运行的时候呢来看一下它呢会做一个询问那我们去输入一些内容它说请输入这个模块名那么模块名呢我就来call一下吧
[07:51] 就是我们这个resource是吧house resource然后呢咱们这么来写啊就是这么来写吧然后呢表明那就是它好然后呢它就会帮我们去做一个生成那么到这里呢它代码就生成好了那么要注意的是这个代码生成呢它那个生成的并不是在我们这个目录下面啊由于它找的是我们的一个这个usr的一个dl就是我们的根目录其实生成到
[08:20] 根目录下面根的工程下面在下面有一个src它其实是写到这个里面来了你看是不是写到这个里面来了生成了有很多的这种代码包括有这个Controller有Controller你看有Controller有这个act其实就是实体其实这个是我们所需要的然后Mapper其实也比较简单是不是就是去继承一个base Mapper这个我们也说过还有叫Service
[08:50] 以及它的一个实现ok它其实生成的代码还是挺多的实际上对网而言什么controllermapper Service并不实用其实比较实用的一个就是它所以我们就需要它就可以了那么我们把这个类拷贝到我们的一个拷贝到我们所需要的这个是在resource下面 interface下面的
[09:20] 会有一个podio包咱们拷贝到这个包下面来把它靠到这那么我们这个类注意类我们改个名字我们前面不要这个tb不要tb这两个字那么咱们把它拷贝过来那么这样的话我们来看一下这个效果把这个先关掉那么在这个里面我们先做一些处理这个data注解我相信这个大家都认识了对吧
[09:45] 那么下面这个EQ是按照Hashcode是他会重写这个EQ是和Hashcode的这个方法那么这个我们就不需要他重写了就把它就删掉了那么这个是什么意思呢这个叫这个是他生成的是一个链式的一个编程那么这个在我们的讲义中有我们来简单的把这个说一下那么链式的编程是这个样子的就是当我们去给我们的这个
[10:14] 属性去生成一些set方法的时候那么它返回的不是一个word空而是返回的当前的一个对象那我们就可以通过这种链式编程一直点点点的这种方式去做一个编程那么我们也是建议大家去做一个保留做一个保留把它保留下来就可以了那么细心的同学会发现就是我们这个类的名字跟我们的这个
[10:41] 表明是不是有点不一样对吧那么怎么办呢就需要在这个位置去给他指定我们的一个table nametable name来指定我们的表明就是他就是这样的话可以做一个指定你这个实体的所对应的表是这张表如果你不这样去指定的话那么他默认是不是会找一个表示这个house里source这样的一个表其实发现他是找不到的OK好那么我们做这样的一个处理
[11:10] 那么我们接着继续往下面看还需要做哪些处理呢这个是它的生成的一个序列化的ID那么我们需要让它去生成一个生成一个真正的一个序列化的ID而不是采用一个默认的一个虚拟序列化的IDOK做这样的一个生成那么接下来呢我们需要给它设置一个ID我发现这个ID呢它并没有生成那么我们来
[11:39] 把这个ID呢给它拷贝一下在这那么把这个ID的信息拷过来好那么拷贝到这个里面来把它拷过来好那么我们这个ID的类型是不是做一个自增长来看一下那么这个ID是不是做一个在这是不是自增长好那么到这里呢我们基本上我们这个房源表的这个实体那么我们就搞定了然后呢我们并且
[12:07] 要注意还有个问题啊就是这create和update是不是我们就不需要了因为呢我们是不是已经在副类中啊就是base puzzle中是不是做了一个啊base puzzle中是不是我们去做了一个定义那么我们现在这个类去继承它是不是就不需要再去写了对吧好那我们大致的来检查一下看有没有问题啊然后呢这个是ID啊这个是标题
[12:33] 应该是没有什么问题了在这还有点问题就是我们这种叫就是我们在数据库里面设置的像租赁方式来看一下租赁方式呢一是整租二是合租它所对应的其实我们应该给它是一个int类型因为我们是一和二然后呢在我们这个生成的实体中设置的boil类型这个是有点问题的那我们就用
[13:01] 这个包装类型吧integ这种类型啊然后呢我们去给它设置一下把这个也改一下那么这个可能会有点问题去调一下啊然后这个也有点问题然后呢继续往下面看啊这个看房时间也有点问题好到这儿应该就没什么问题了来检查一下啊应该就没什么太大的问题了好那么大家呢可以去对照一下我们的这个蒋易中啊所提供的这个呃这个实体那么基本上应该是ok的没有问题
[13:31] 好那么到这里我们实体是不是就已经就搞定了好那么我们先把这个视频先保存一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
使用 MyBatis-Plus 的 AutoGenerator 插件，基于数据库表结构自动生成 Java 实体类（Entity）和对应的 Mapper 文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 PDF 文档中关于编写 BasePojo 文件的说明，要求所有 pojo 类继承该类并包含 created、updated 字段。
画面 2：展示 Navicat Premium 中的数据库表结构，包含 `tb_house_resources` 表的 CREATE TABLE 语句，定义了字段如 id、title、estateId、buildingNum 等。
画面 3：在 IntelliJ IDEA 中展示 Maven 项目结构，焦点在 `pom.xml` 文件，显示了父工程的配置。
画面 4：展示 PDF 文档中关于数据源配置的说明，包含 `PackageConfig` 的配置代码片段。
画面 5：在 IntelliJ IDEA 中展示 `CodeGenerator.java` 文件，显示了 `main` 方法中初始化 `AutoGenerator` 并配置数据源和包路径的代码。
画面 6：在 IntelliJ IDEA 中展示 `pom.xml` 文件的 `<dependencies>` 部分，列出了 MyBatis-Plus、Freemarker、MySQL Connector 等依赖。
画面 7：在 IntelliJ IDEA 中展示 `CodeGenerator.java` 文件的开头部分，导入了 MyBatis-Plus 相关的包和类。
画面 8：在 IntelliJ IDEA 中展示 `CodeGenerator.java` 文件中配置 `InjectionConfig` 的代码。
画面 9：在 IntelliJ IDEA 中展示生成的 `TbHouseResources.java` 文件，显示了继承 `BasePojo` 的类结构和部分字段。
画面 10：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了类定义和部分字段。
画面 11：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了类定义和部分字段。
画面 12：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了 `rent`、`rentMethod`、`paymentMethod` 等字段。
画面 13：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了 `houseType`、`coveredArea`、`useArea` 等字段。
画面 14：在 IntelliJ IDEA 中展示 `HouseResources.java` 文件，显示了 `floor`、`orientation` 等字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
package cn.itcast.haoke.dubbo.server.pojo;
import lombok.Data;
import java.util.Date;
@Data
public abstract class BasePojo implements java.io.Serializable{
    private Date created;
    private Date updated;
}
```

画面 2：
```sql
CREATE TABLE `tb_house_resources` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL COMMENT '楼盘名称',
  `province` varchar(10) DEFAULT NULL COMMENT '所在省',
  `city` varchar(10) DEFAULT NULL COMMENT '所在市',
  `address` varchar(100) DEFAULT NULL COMMENT '详细地址',
  `year` varchar(10) DEFAULT NULL COMMENT '建楼年份',
  `type` varchar(10) DEFAULT NULL COMMENT '房屋类型',
  `property_coos` varchar(10) DEFAULT NULL COMMENT '物业公司',
  `developers` varchar(20) DEFAULT NULL COMMENT '开发商',
  `created` datetime DEFAULT NULL COMMENT '创建时间',
  `updated` datetime DEFAULT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1006 DEFAULT CHARSET=utf8 COMMENT='楼盘表';
```

画面 3：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <parent>
        <artifactId>itcast-haoke-manage-dubbo-server</artifactId>
        <groupId>cn.itcast.haoke.manage</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>
    <artifactId>itcast-haoke-manage-dubbo-server-generator</artifactId>
</project>
```

画面 4：
```java
PackageConfig pc = new PackageConfig();
pc.setModuleName(scanner(tp, "模块名"));
pc.setParent("cn.itcast.haoke.dubbo.server");
mpg.setPackageInfo(pc);
```

画面 5：
```java
throw new MybatisPlusException("请输入正确的" + tip + "!");
public static void main(String[] args) {
    AutoGenerator mpg = new AutoGenerator();
    GlobalConfig gc = new GlobalConfig();
    String projectPath = System.getProperty("user.dir");
    gc.setOutputDir(projectPath + "/src/main/java");
    gc.setAuthor("itcast");
    gc.setOpen(false);
    mpg.setGlobalConfig(gc);
    DataSourceConfig dsc = new DataSourceConfig();
    dsc.setUrl("jdbc:mysql://172.16.55.185:3306/haoke?useUnicode=true&characterEncoding=utf-8&autoReconnect=true&allowMultiQueries=true");
    dsc.setDriverName("com.mysql.jdbc.Driver");
    dsc.setUserName("root");
    dsc.setPassword("root");
    mpg.setDataSource(dsc);
    PackageConfig pc = new PackageConfig();
    pc.setModuleName(scanner(tp, "模块名"));
    pc.setParent("cn.itcast.haoke.dubbo.server");
    mpg.setPackageInfo(pc);
}
```

画面 6：
```xml
<dependencies>
    <!-- freemarker 模板引擎 -->
    <dependency>
        <groupId>org.freemarker</groupId>
        <artifactId>freemarker</artifactId>
        <version>2.3.28</version>
    </dependency>
    <dependency>
        <groupId>com.baozimou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.0.5</version>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>mysql</groupId>
        <artifactId>mysql-connector-java</artifactId>
        <version>5.1.47</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

画面 7：
```java
package cn.itcast.haoke.generator;
import com.baozimou.mybatisplus.core.toolkit.StringTool;
import com.baozimou.mybatisplus.generator.AutoGenerator;
import com.baozimou.mybatisplus.generator.config.*;
import com.baozimou.mybatisplus.generator.config.rules.NamingStrategy;
import com.baozimou.mybatisplus.generator.engine.FreemarkerTemplateEngine;
import org.apache.commons.lang3.StringUtil;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
```

画面 8：
```java
InjectionConfig cfg = new InjectionConfig() {
```

画面 9：
```java
@Data
@EqualsAndHashCode(callSuper = true)
@Accessors(chain = true)
public class TbHouseResources extends BasePojo {
    private static final long serialVersionUID = 1L;
    /**
     * 房源标题
     */
    private String title;
    /**
     * 楼盘id
     */
    private Long estateId;
    /**
     * 楼号（栋）
     */
    private String buildingNum;
```

画面 10：
```java
public class HouseResources extends BasePojo {
    private static final long serialVersionUID = 1L;
    /**
     * 房源标题
     */
    private String title;
    /**
     * 楼盘id
     */
    private Long estateId;
    /**
     * 楼号（栋）
     */
    private String buildingNum;
```

画面 11：
```java
package cn.itcast.haoke.dubbo.server.pojo;
import ...
@Data
@Accessors(chain = true)
@TableName("tb_house_resources")
public class HouseResources extends BasePojo {
    private static final long serialVersionUID = 1L;
    /**
     * 房源标题
     */
    private String title;
    /**
     * 楼盘id
     */
    private Long estateId;
```

画面 12：
```java
private Integer rent;
    /**
     * 租赁方式，1-整租，2-合租
     */
    private Boolean rentMethod;
    /**
     * 支付方式，1-付一押一，2-付三押一，3-付六押一，4-年付押一，5-其它
     */
    private Boolean paymentMethod;
    /**
     * 户型，如：2室1厅1卫
     */
    private String houseType;
    /**
     * 建筑面积
     */
    private String coveredArea;
    /**
     * 使用面积
     */
    private String useArea;
```

画面 13：
```java
private String buildingUnit;

