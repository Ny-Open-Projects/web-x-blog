# 10.新增房源服务实现之搭建工程

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day04-服务的具体实现以及MybatisPlus的入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day04-服务的具体实现以及MybatisPlus的入门\10.新增房源服务实现之搭建工程【海量资源尽在 ubkz.com】.mp4
- 时长 10分52秒（音频 652s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么下面呢我们来看一下新增房源的服务的一个开发啊前面呢我们已经把工程呢打建好了下面我们来看一下这个服务的一个开发具体的一个实现那么首先呢我们来看一下数据结构那么在我们新增房源这个业务中啊那么会涉及到先涉及到两个表那么第一个表呢就是我们的楼盘表第二个表呢就是我们的这个房源信息表
[00:26] 那么其实我们这个项目的浩克租房项目呢是一个做租房啊这样的一个项目啊那么他肯定的是会有很多的一些房源的信息那么这个房源呢一定要有一个什么的楼盘的数据是吧比如说这个房源呢是在哪一个小区啊在哪个楼盘那么一定要有这个楼盘的数据哎好那么我们呃接下来把这两个
[00:51] 表我们来创建一下那么我们给大家资料中有一个 circle.txt 文档然后我们打开之后就可以去得到一个我们的一个 circle 的脚本然后把这个脚本的靠一下然后我们找到我们的 toolkit然后在这个里面去创建一个查询然后把它贴过来然后执行走我们脚本就已经执行完成了好那么到这个里面我们来刷新一下就会多了两张表
[01:20] 一个呢是这个E-State就是我们的房源啊那么在这个是楼盘啊楼盘数据那么在楼盘数据中呢我们初始化了有五条数据然后呢我们的这个房源数据呢是没有做初始化啊那么这个就需要我们一会去添加数据的啊那么这个四段啊相信大家应该也不陌生了前面我们再去讲我们的这个前端的实现的时候呢是不是也看到一些这样的一些这个数据结构对吧
[01:50] OK那么这个大家可以每一个字段都去看一下我在这呢就不带着大家一点一点去读了啊那么呃简单说一下吧就是在这个里面呢他有一个叫楼盘的ID啊楼盘ID对应的就是这张表里面的这个数据啊呃所以说这个楼盘和我们的房源数据呢是一对多的关系啊一对啊多的关系啊是这样的一个关系啊一对多的关系哎呀OK好那么呃那反过来讲啊这个
[02:20] 房源和楼盘是一对一的一个房源只能属于一个楼盘OK好那么这个就是他有记录了一个楼盘的IDOK好那么下面这个应该都是基本的一些我们的信息了好那么咱们接着继续往下面看那么数据库现在我们都已经创建好了下面我们来创建我们的工程那么在我们前面说的时候我们是不是有一个叫这个double server这个服务
[02:49] 在这个下面它其实会有很多的服务对吧有什么新增有这个房源有房源的服务有房东的服务有各种服务所以说我们先来去创建的是房源我们这个房源叫house resource就是我们的房源那么创建这个工程咱把这个名字扣一下然后去创建一个工程然后注意要点击这个工程要创建它下面的子工程new一个module
[03:18] 然后我们注意选择要选择下面这个JDK 8然后下一步我们把它拷过来然后下一步把它拷过来然后点击这个Fenix完成好那么这个工程就创建好了我们这个名字好像是有点长大家应该能够看懂这个意思接着继续往下面看那么刚刚把这个Resolve11工程是不是创建好了那么我们还是需要把这个工程继续做一个拆分
[03:45] 那么我们是不是前面他是搞定了对吧然后我们需要在这个下面继续的拆分两个工程一个叫做double interface一个叫做Service那么为什么要去拆分我们先把这两个项目这两个工程它的作用先讲明白那么 interface这个里面我们存的是一些什么像我们的一些puzzle还有一些我们的一些接口的定义注意只是一些double这个接口的定义那么下面这个double的Service
[04:12] 这个呢就是去存的一些我们具体的一些实现具体实现那么前面我们在讲W入门的时候也提到过这个问题就是说我们不能把这个接口的定义和我们接口的实现都丢到一个包里面对外提供对不对那么如果你这样提供出去的话那么其实就是没有意义了对不对那么这个包里面是不是已经包含了我们的实现对吧所以说不能这样提供所以我们把它做一个拆分那么其实我们下面可以看到那么在这个interface这个包
[04:40] 在这个工程下面那么我们提供的是什么呢Pozo以及它的接口不提供实现类也就是它是对外的一个SDK包然后呢我们这个double Service呢它呢是做一个具体的一个实现OK好那么我们接下来呢把这两个工程呢也创建出来那么我们来靠一下这个名字吧靠下它然后呢拷贝到这个下面呢我们继续来创建工程啊这工程就有点多了
[05:08] 那么一定要分清楚分清楚然后把它贴过来这个是interface然后拷贝一下非你是完成好那么这工程我们是不是就创建好了然后我们继续往下面创建还有一个是Service那么Service是做具体的实现具体实现那么我们依然选择resource这个那么在我们后面再做一些其他功能的时候是不是又需要在这个下面再创建其他的一些
[05:34] Service-后面的一些比如说像房东这样的一些工程好那么我们继续往下面创建具体的一个实现选择它然后点击next然后把它贴过来double Service然后点击next然后我们再点击finish完成好那么这个工程是不是就创建好了那么最终我们创建的结构是不是我们刚刚截图的这样的一个结构ok好那么现在这个就搞定了那么下面我们去
[06:02] 看一些配置文件那么我们在resource工程中就是我们外面resource这个工程的配置文件中我们要给它添加一些配置项我们先把dependencies我们先考进来先写好然后我们去拷贝一些依赖那么我们要把这个这个怎么呢叫longbook那么是不是
[06:31] 他要考过来这个呢其实我们前面是不是也讲过他了对吧好那么在这个位置需要注意的是我们是不是给他设置为这个Option是不是就是一个Virtual那么也就是说在做依赖传递的时候如果你需要的话那么就需要你显示的去做一个引入如果你不做一个显示的一个引入的话那么是不会去被做一个依赖的传递的这个前面也提了一下OK好那么我们接着继续往下面去看
[06:59] 然后把下面的这两个拷过来这两个呢就是我们的mybatties plus这个spin boot的一个支持以及我们的mycircle的一个驱动哎呀ok好那么这样的话呢我们就是不是就搞定了哎这样的话就搞定了那么同样的我们可以看到在我们的mycircle的这个驱动这个包它是不是也是设置了为处对吧当然这个也是为处也就是说
[07:25] 当你的有工程需要去做一些这种依赖传递的时候那么如果你需要那么就去显示的去指定它就ok了那么这个一定要注意这是一个我们去创建工程的一个小的一个细节这个一定一定要注意ok好那么我们继续往下面看好这是这个工程然后我们继续往下面看它的一些子工程就是interface
[07:51] 那么在这个interface中呢需要导入什么依赖呢我们把这个也贴过来拷贝然后呢借用我们这个interface然后我们把它拿过来来看一下那么这个是不是多了一个回车啊这个回车有点问题把这个给它拿掉把这个把这个处理一下处理一下好这样应该就好了那么这个doubleint扫一个横杠啊
[08:24] 好那这样的话就OK了这个包有点这个这个坐标有点不一样有点不一样那么什么不一样呢是我们的这个这个以及他的Golper IDGolper ID有点不一样那么我们把它拷过来Golper ID在这好这样的话就好了那么我们来看一下他的一个依赖关系就是我们这个我们来看一下
[08:57] 依赖关系是这样的那么我们这个是interface这个是不对的这个是不对的我们这个考错了那么我们来看一下这个是谁这个是double Service的依赖要注意的是interface中我们现在看到的是interface的依赖这个依赖它其实不需要目前先不要去写什么依赖了那么我们下面这个double Service
[09:26] 是下面这个工程中所要依赖的内容是我们刚刚所写这个内容刚刚call的有点问题那么也就是说我们这个是一个server的一个实现那么task其实要是依赖于我们的这个具体的一个接口的定义然后才能做一个实现OK有这样的一个依赖关系这个别搞错那么由于我们在我们的工程中是不是会涉及到一些我们的事务的一些操作
[09:52] 所以呢我们要把这个Springboard的这个GDPC这个要靠近来一会儿呢我们要去做一些事务的一些控制啊OK好那么这个就搞定了好那么到这里呢我们这个工程就创建好了那么大家在创建的时候呢一定要理清楚啊他们之间的关系啊我们来重复的吧再说一遍啊那么这个是这个是我们的后台系统啊
[10:17] 那我们的后台系统会分为两个一个是API这个是对外去提供的这种接口服务而这个是我们内部的对吧内部的一个实现那么内部的一个实现它是我们Double的一个服务那么在这个Double服务下面会有很多的服务其中我们做的第一个就是房源这个服务然后在房源这个服务下面我们又继续做一个拆分拆分为是interface接口还有一个叫Service具体的一个实现OK
[10:45] 好那么这个呢就是我们新增房源的这个工程的一个搭建好那么关于这个工程搭建就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解如何创建并配置一个用于管理房产服务的 Spring Boot + Dubbo 项目，包括数据库表结构设计和 Maven 项目模块化配置。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：
- 标题：4. 新增房产服务
- 子标题：4.1. 数据结构
- 展示了数据库表 tb_estate 的创建语句：
CREATE TABLE `tb_estate` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL COMMENT '楼盘名称',
  `province` varchar(10) DEFAULT NULL COMMENT '所在省',
  `city` varchar(10) DEFAULT NULL COMMENT '所在区',
  `area` varchar(10) DEFAULT NULL COMMENT '所在区',
  `address` varchar(100) DEFAULT NULL COMMENT '具体地址',
  `year` varchar(10) DEFAULT NULL COMMENT '建成年代',
  `type` varchar(10) DEFAULT NULL COMMENT '建筑类型',
  `property_cost` varchar(10) DEFAULT NULL COMMENT '物业费',
  `property_company` varchar(20) DEFAULT NULL COMMENT '物业公司',
  `developers` varchar(20) DEFAULT NULL COMMENT '开发商'

画面2：
- 展示了项目目录结构，包含三个子工程：
  - itcast-haoke-manage-dubbo-server-house-resources
  - itcast-haoke-manage-dubbo-server-house-resources-interface
  - itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service

画面3：
- 展示了 Navicat Premium 连接数据库的界面，连接到名为 "haoke" 的数据库。

画面4：
- 标题：4.2. 创建 itcast-haoke-manage-dubbo-server-house-resources 工程
- 展示了数据库表 tb_payment_method 的创建语句：
CREATE TABLE `tb_payment_method` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL COMMENT '支付方式',
  `code` varchar(20) DEFAULT NULL COMMENT '支付方式编码',
  `created` datetime DEFAULT NULL,
  `updated` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COMMENT='支付方式表';

画面5：
- 展示了项目结构图，突出显示了三个子模块：
  - itcast-haoke-manage-dubbo-server-house-resources
  - itcast-haoke-manage-dubbo-server-house-resources-interface
  - itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service

画面6：
- 展示了 IntelliJ IDEA 中右键创建 Maven 项目时的弹出菜单，但提示“failed to create a Maven project”。

画面7：
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-interface</artifactId>
    <packaging>pom</packaging>
    <modules>
      <module>itcast-haoke-manage-dubbo-server-house-resources-interface</module>
      <module>itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service</module>
    </modules>

画面8：
- 展示了 pom.xml 文件内容，其中包含：
  <dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
  </dependency>

画面9：
- 展示了 pom.xml 文件内容，其中包含：
  <dependency>
    <groupId>com.baidou</groupId>
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

画面10：
- 标题：4.3.2. itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service</artifactId>

画面11：
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface</artifactId>

画面12：
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-interface</artifactId>

画面13：
- 标题：4.3.2. itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service
- 展示了 pom.xml 文件内容，其中包含：
  <project xmlns="http://maven.apache.org/POM/4.0.0"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
      <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
      <groupId>cn.itcast.haoke</groupId>
      <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources-dubbo-Service</artifactId>

画面14：
- 展示了 pom.xml 文件内容，其中包含：
  <dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-jdbc</artifactId>
  </dependency>
  <dependency>
    <groupId>cn.itcast.haoke.manage</groupId>
    <artifactId>itcast-haoke-manage-dubbo-server-house-resources</artifactId>
    <version>1.0-SNAPSHOT</version>
  </dependency>

