# 11.轮播广告实现之common工程的抽取

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\11.轮播广告实现之common工程的抽取【海量资源尽在 ubkz.com】.mp4
- 时长 8分51秒（音频 531s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊前面呢我们已经把这个数据呢准备好了那么接下来呢我们要做的呢就是实现我们这个查询的这个接口当然了我们首先要做的是我们这个double这个服务的一个实现啊那么我们简单做一个分析啊其实前面我们也分析过
[00:18] 第一个呢就是我们现在要做的虽然是一个轮播广告的一个功能但是呢我们不能把它只看作是一个轮播的广告而是呢我们要把它看作是我们整个网站的一个广告的一个功能来做一个开发首先这个定位一定要定好这第一个点那第二个点呢就是我们呢要去给它开发一个是个独立的一个double的服务那么什么叫做独立的double服务呢也就是说
[00:46] 我们的这个后台系统啊它们主要是分为了两部分啊第一部分呢是不是就是API Server第二部分呢就是我们这个Double的这个服务那么我们这个Double的服务下面呢目前是不是已经实现了一个房源的一个服务啊所以说我们下面要实现的是我们这个广告也就是AD的一个服务那么我们所以要把它独立开来独立开来的一个好处呢就是便于我们后期的一个拓展以及我们这个维护哎OK这个我相信大家能够理解啊
[01:15] 第三个呢就是我们多个这个double的服务也就是说之前我们是不是只有一个服务对吧只有一个这个房源这个服务而我们现在是不是又要有一个我们的广告的服务对吧那么我们未来是吧后面我们还会有一些其他的一些服务那么我们是不是就非常有必要将我们的一些公用的一些这个类或者说我们的一些方法
[01:41] 我们去把它挪到一个common工程也就是我们公用的一个工程中以便我们的一些其他工程的一个共用啊对不对所以我们在实现我们这个查询这个接口那之前呢我们首先要去完成的是一个common工程的一个改造那么也就是说我们要先建一个工程把我们一些公用的一些这个类我们都丢到这个里面来OK这个就是我们先要
[02:07] 做的一个事情那么接下来我们就来创建我们的一个common这个工程那么我们把这个工程创建出来名字就是叫这个名字就是也是有点长叫double server common这个工程然后我们将一些base puzzle以及base serviceimpl移动到这个该工程中好那么我们先来去把这个工程我们先创建出来在哪个位置创建要注意的是这个别搞错
[02:36] 在下面的这个里面做一个创建不是他供应,而是在这个里面做供应所以我们需要在这个位置创建一个module然后我们选择这个选择这个JDK然后下一步然后我们去把这个名字我们拷过来然后下一步然后我们把名字拷过来点击非离子完成OK创建好之后我们就需要把一些公用的类
[03:03] 挪到这个里面来那么我们来看一下需要有哪些类我们去做一个移动那么我们进入到我们这个house resource这个工程中它有两个工程一个是interface一个就是Service那么在interface中它有一个类叫做base module这个类这个类是不是一定会作为一个公用的一个类所以我们有必要把这个类是不是给它拿走然后我们看一下
[03:31] 在这个下面呢我们来创建一个包啊他就是叫啊这个包那么我们创建一个包哎呃但是呢我们发现啊他是并没有标记为是一个啊Java的一个资源啊那我们给他去标记一下吧标记为是一个source啊然后呢我们给他创建一个package包然后呢是这个呃puzzle这个包哎ok然后呢我们把这个base puzzle给他去挪到这个里面来
[04:02] 先把它拷贝过来好那么这个类是不是就OK了但是呢它缺少一些依赖这个我们一会儿再给它导入一些这个依赖那么接着呢这个我们是不是就可以把它删除了对吧把它删掉好然后呢我们来看一下这个Service下面它也有一个叫做base Service impl对不对这个类我们是不是也可以把它挪走那么我们先拷贝一下这个包
[04:29] 然后呢我进入这个common下面的加了下面创建一个这个包那么这个包呢我们就不需要后面的impl了把它去掉直接到Service那么我们把这个具体这个实现的我们拷贝到啊这个Service里下面啊拷贝到下面那么我们点击之后呢进入之后他肯定也会报错啊是不是缺少一些依赖啊那我们就把一些错误给他解决掉是不是就ok了
[04:58] 那么显然呢在这个common这个包下面他是缺少一些依赖那么缺少哪些依赖呢我们来看一下那么呃他首先他缺少的肯定是一个什么呢是不我们这个long book啊他因为我们看到他是缺我们使用了这个data这个注解对吧这是第一个第二个呢就是我们这个mybatties的一个这个plus的一个这个插件啊把这个导入进来哎ok
[05:29] 来看一下还缺少东西吗那么这个里面它还缺少还缺少一些内容我们来先看一下这个里面这个已经已经是导入进来了但是它并没有生效为什么呢有可能是我们的这个Maren没有去自动去刷新那我们来看一下它自动的一个刷新那我们进入到这个setting这个文件中
[06:00] 申请文件然后咱们找到这个build的这个工具build的工具然后找到build的工具marin下面有一个叫做inglow来可以看到这个里面它的你看这个勾是不是已经被打了勾了对吧所以我们把这勾去掉要不然它不会生效的好嘞那么这个时候我们得来刷一下了刷一下我们看一下这个位置它有没有一些
[06:34] 说明呢也没有啊哎OK好可以啊那么现在呢我们可以看到在我们这个combo的一个工程中啊他的错误他自身的一个错误是不是已经解决了啊没有问题了那我们来看一下下面的这个错误啊来展开来看一下下面这个错误呢是不是集中在这个工程里面对吧那么由于呢我们是不是把这个相关的一些这个这个内容你看这个里面是不是他缺少缺少这个依赖对吧
[07:02] 全都这个包然后下面的这个里面我们再来看一下它里面是不是也是相同的这个问题当然了这个我们就给它删掉了这个我们就不需要了把它删掉好那么删掉之后它就会报错了对吧它就会报错那么我们来看一下这个问题怎么解决那么由于我们把这个类是不是挪到这个里面来所以我们需要在它里面两个里面是不是导入这个common的工程
[07:30] 那么在他们两个里面导入那么是不是我们是不是可以直接在这个里面去导入就可以了所以我们进入他的一个依赖泡沫文件在这个里面我们把这common导入进来我们放到dependency的最上面那么我们去引入一个叫做commoncommon什么common我们来看一下他能不能找到这个gum是不是就是我们的servercommon把它引入进来
[08:00] 多了一个common把这个common拿掉好这样这样的引用进来那么他就不会去报错了我们来看一下好了没有还有没有报错展开来看一下那么这个里面当然还有错因为这个包是我们已经发生了改变对吧我重新把它导入一下重新把这个包导入进来导入进来了吗导入进来了好这个是不是就搞定了那么之前这个interface这个是不是也搞定了
[08:32] 好嘞那么现在呢我们是不是就把一些公用的一些内容我们都丢到这个里面来了OK那么后面呢我们一些公用的一些代码是不是都可以往这个里面去丢啊哎好嘞好那么关于啊关于我们的这个公用工程的一个抽取common工程的一个抽取那我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 IntelliJ IDEA 中创建并配置一个名为 "itcast-haoke-manage-dubbo-server-common" 的 Maven 项目模块，用于存放公共的 POJO 和 Service 接口实现，以支持 Dubbo 服务的开发。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了项目结构，当前选中模块为 "itcast-haoke-manage-dubbo-server"，并显示了 GraphQL 文件中的字段定义，如 coveredArea、floor、orientation 等。
画面 2: 在项目结构中选中了 "itcast-haoke-manage" 项目根目录。
画面 3: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了该模块的 pom.xml 文件内容，其中包含 <parent> 和 <artifactId> 等配置。
画面 4: 在项目结构中右键点击 "itcast-haoke-manage-dubbo-server-common" 模块，弹出创建新文件的菜单。
画面 5: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 BasePojo.java 文件内容。
画面 6: 在项目结构中右键点击 "itcast-haoke-manage-dubbo-server-common" 模块，弹出创建新文件的菜单。
画面 7: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 8: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 BaseServiceImpl.java 文件内容，其中包含 @Autowired 注解和 queryById 方法。
画面 9: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 10: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-common" 模块，右侧编辑器显示了 BaseServiceImpl.java 文件内容，其中包含 queryAll 方法。
画面 11: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-house-resources" 模块，右侧编辑器显示了 HouseResourcesServiceImpl.java 文件内容，其中包含 @Transactional 注解和方法参数。
画面 12: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-house-resources" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 13: 在项目结构中选中了 "itcast-haoke-manage-dubbo-server-house-resources" 模块，右侧编辑器显示了 pom.xml 文件内容，其中 <dependencies> 节点被高亮。
画面 14: 显示了 PDF 文档 "定义.pdf" 的第 3.3.2 节，标题为“3.3.2. 创建 common 工程”，内容说明创建 "itcast-haoke-manage-dubbo-server-common" 工程，并将 BasePojo、BaseServiceImpl 移动到该工程中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```GraphQL
coveredArea:String
useArea:String
floor:String
orientation:String
decoration:Int
facilities:String
pic:String
houseDesc:String
contact:String
mobile:String
time:Int
propertyCost:String

type TableResult{
  list:[HouseResources]
  pagination:Pagination

type Pagination{
  current:Int
  pageSize:Int
```

画面 3:
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
    <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
```

画面 5:
```java
package cn.itcast.haoke.dubbo.server.pojo;

import ...

@Data
public abstract class BasePojo implements java.io.Serializable {

    private Date created;
    private Date updated;
}
```

画面 6:
```java
// 代码片段未完整显示
```

画面 7:
```xml
<dependencies>
    <dependency>
        <groupId>cn.itcast.haoke.manage</groupId>
        <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
</dependencies>
```

画面 8:
```java
@Autowired
private BaseMapper<T> Mapper;

/**
 * 根据id查询数据
 * @param id
 * @return
 */
public T queryById(Long id) { return this.Mapper.selectById(id); }

/**
 * 查询所有数据
 * @return
 */
public List<T> queryAll() { return this.Mapper.selectList(null); }
```

画面 10:
```java
@Autowired
private BaseMapper<T> Mapper;

/**
 * 根据id查询数据
 * @param id
 * @return
 */
public T queryById(Long id) { return this.Mapper.selectById(id); }

/**
 * 查询所有数据
 * @return
 */
public List<T> queryAll() { return this.Mapper.selectList(null); }
```

画面 11:
```java
package cn.itcast.haoke.dubbo.server.Service.impl;

import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.Service.HouseResourcesService;
import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import org.apache.commons.lang3.StringUtils;
import org.springframework.transaction.annotation.Transactional;

@Service
@Transactional
public class HouseResourcesServiceImpl extends BaseServiceImpl<HouseResources> {

    @Override
    public HouseResources queryById(Long id) {
        if (StringUtils.isBlank(id.toString())) {
            throw new RuntimeException("输入的参数不符合要求，0：数据插入数据库失败，1：数据更新失败");
        }
        return this.baseMapper.selectById(id);
    }
}
```

画面 12:
```xml
<dependencies>
    <dependency>
        <groupId>cn.itcast.haoke.manage</groupId>
        <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.0.5</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

画面 13:
```xml
<dependencies>
    <dependency>
        <groupId>cn.itcast.haoke.manage</groupId>
        <artifactId>itcast-haoke-manage-dubbo-server-common</artifactId>
        <version>1.0-SNAPSHOT</version>
    </dependency>
    <dependency>
        <groupId>org.projectlombok</groupId>
        <artifactId>lombok</artifactId>
        <optional>true</optional>
    </dependency>
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.0.5</version>
        <optional>true</optional>
    </dependency>
</dependencies>
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 14:
标题：3.3.2. 创建 common 工程
内容：
- 实现独立的 dubbo 服务，便于后期的扩展和维护
- 多个 dubbo 服务，需要抽取公共的类、方法到 common 工程中
- 创建 itcast-haoke-manage-dubbo-server-common 工程，将 BasePojo、BaseServiceImpl 移动到该工程中。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

