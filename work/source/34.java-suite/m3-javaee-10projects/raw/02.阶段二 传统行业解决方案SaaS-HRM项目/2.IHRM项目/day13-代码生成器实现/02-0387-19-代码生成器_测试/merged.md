# 19-代码生成器：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\19-代码生成器：测试_【海量资源尽在 ubkz.com】.mp4
- 时长 8分22秒（音频 503s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了我们现在已经把这个模板制作成功了那接下来我们可以一起来测试一下通过这个模板生成的这些代码究竟好不好使那咱们生成的代码有很多我不可能全部都给各位重新再搞一遍搞到我们的这个工程里那我就以一个我们之前没写过的City为例那这个City对应的数据库的表呢叫做BSCity里面的字段就比较少有ID NAME和GREAT TIME
[00:30] 那接着我们来看一下怎么去使用它好了在这边我也不会去写一个新的工程了我就在这里面呢可以给它随便的配置到其中的某一个咱们一起来看一下如何去用其实就可以了那首先咱们生成的有实体类对象把这个实体类对象你需要哪个直接就call到你的工程当中即可需要CT糖出Ccall那call到什么地方比如说我就把它call到我这边的一个POJO这个包下
[00:59] 好 周围好了 抠过来之后各位会发现这边有个小小的问题是不是我们这边模板少一个分号好了 少一分号把这个分号给它添加上OK好了 当然了这边我们做了一个修改同样的我们这边的模板也要做一个修改这个就是刚才专门写这个代码因为它没有任何的提示所以咱们盲写就容易出现这种问题所以咱们需要做一个简单的测试好了 这边分号
[01:51] 真好OK好了那POJO我们已经导过来了那接下来呢是不是还应该对应的应该有DAO的这么一套程序那DO要靠到DO这个包下那同样的在这边咱们找到DO也是CTDOC拿过来OK这回没报错那DO咱们也已经搞定了接下来关注的就是Service那同样的找到Service
[02:24] City Service Control C也拿过来Control V拷过来那我们来看一下Service呢也没有什么问题那Service我们搞定了接下来关注的就是最后一个Controller那Controller我们找到Controller找到City ControllerOKControl C把它copy到我们的Controller目录下好了copy到Controller目录下之后各位来看
[02:53] 就目前来说它都没有报错它都没有报错那我们现在请求的路径呢是不是叫做杠C体下呀但是呢咱们根据逻辑而言我们目前当前的这个system系统下的是不是咱们默认前面都习惯给它加一个杠SOS所以对于我们来说直接做一点点简单的修改那这样以来你已经完成了当前城市的增深改查的基本操作
[03:19] OK那我们把代码都已经搞进去之后那接下来我们可以启动一下看一下是否能够完成我们数据库对应的这些增删改查的操作OK当然了我们要想去完成这个操作这个操作我这边呢为了简单我不想进行一个登录了我不想进行登录了所以呢我在这个shareware page这边啊做一个简单的逻辑判断就是说如果你碰到的是
[03:53] C体下的我就匿名访问主要是为了我不想做登录了咱们主要是看一下代码生成的逻辑究竟对不对OK那好了接下来启动Erica走好了Erica启动好了之后启动我们的系统微服务走好了这边呢就让它去启动好了这边启动咱们一起来看一下这边报了一个错误啊就是说这个实体内呢
[04:36] 没有被管理为什么是这样的是因为我们这个系统呢跟我们这个这套逻辑呢还是有一点点小小的一些不太一样的地方因为我们是把它放到了PUJO这里面了所以这边呢我们把所有的实体类都已经放到了model这个包下刚才是为了偷懒那接下来呢我们再给它放回model这个包下OK那这边的city我就把它删掉了那删掉了之后呢这里面的do我们来看一下
[05:08] 就要做香的修改这个就有点麻烦了OK好了Dio呢做了一个修改City也做了一个修改当然了其实这个倒是无所谓如果各位有兴趣的话呢其实可以做一个简单的模板上面的一个配置就是说你模板叫什么名字你单独的给它拿出来往里面去引用其实就可以了好了Ctrl这边呢也要做一个处理City删掉OK全部都引入来了
[05:37] 引入进来之后注意我这边再去重新启动一下System Application好了这边呢让它去启动我呢打开Postman咱们来测试一下哎究竟好不好使OK Postman呢已经打开了我们这边访问的是Sys-City这个启动有点点慢啊各位耐心等待一下好了现在呢已都启动起来了好了我这边Postman呢已经打开了那接下来呢我们就开始做一个访问了
[06:16] localhost 9092好了我们现在访问的是叫做city那我以post的形式来进行提交那提交呢其实就相当于我在这边要执行保存的这个操作那保存的操作我把所有的内容全部封装到一个city对象里所以在这边我传递一个内容肉而这边呢我传递的是jason好了那city当中有多少属性其实属性并不多
[06:45] 咱们就用一个Name其实即可Create Time呢其实不应该是我们前端传递的是不是最好是在我们的业务逻辑层自己New York Days传进去啊OK那好了我们一起来看一下来一个Name那这个Name呢可以给他来一个比如说就叫做北京OK那好了我们Send走来看一下返回好了他告诉我操作成功来看一下数据库数据刷新一把北京已经传递进去了那除了这个之外呢我们是不是还有
[07:20] get方式进查询ID放过来来一个get方式查询走操作成功北京也能够查询出来那还有其他的比如说呢我什么都不传以get方式是不是就查询列表那走各位列表其实也已经出来了那其实这样一来呢各位就已经看到了我们可以通过代码生成器给我们自己生成出这么一套代码并且是可用的那对于各位而言那对于各位而言其实很简单
[07:51] 在代码生成的其实完成的基础之上我们只需要制作符合我们系统当中的模板其实就可以了当然了这个模板制作的过程刚才希望各位也能够看懂怎么做是不是就是根据已有的一套代码咱们开始按照一定的规则进行改改类名改包名改引入的我们的实体类的这些名称改它的一个调用的名称的一个关系OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的权限管理系统中，城市（City）实体的 POJO、DAO、Service、Controller 层的代码结构与配置，以及如何通过 Shiro 实现权限控制，并最终在数据库中验证实体表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目目录结构，当前选中 `pojo` 文件夹，其中包含 `City.java`、`Department.java` 等实体类文件。
画面 2：展示 `City.java` 实体类代码，使用 `@Entity` 和 `@Table` 注解，定义了 `id`、`name`、`createTime` 字段及其 getter/setter 方法。
画面 3：展示 `application.yml` 配置文件，包含服务端口、Spring 配置、数据源（MySQL）和 JPA 配置。
画面 4：展示 `dao` 文件夹下的文件列表，包含 `CityDao.java`、`CompanyDao.java` 等。
画面 5：展示 `Service` 文件夹下的文件列表，包含 `CityService.java`、`CompanyService.java` 等。
画面 6：展示 `CityController.java` 控制器代码，包含 `save`、`update`、`delete`、`findById` 等 REST 接口方法。
画面 7：展示 `ShiroConfiguration.java` 配置类，定义了 Shiro 的 `SecurityManager`、`FilterChainDefinitionMap`，设置登录和权限拦截规则。
画面 8：展示 `EurekaServer.java` 启动类，使用 `@EnableEurekaServer` 注解启用 Eureka 服务注册与发现功能。
画面 9：在 IDEA 中点击 `City.java` 文件，出现编译错误提示：`Not a managed type: class com.ihm.system.pojo.City`。
画面 10：展示 `CityDao.java` 接口代码，继承 `JpaRepository`，定义了对 `City` 实体的操作。
画面 11：IDEA 项目结构视图，选中 `CityController`。
画面 12：在终端运行 `java -jar` 命令，输出数据库表结构的生成日志。
画面 13：在 Navicat 数据库管理工具中，查看 `hs_city` 表的结构，包含 `id`、`name`、`create_time` 等字段。
画面 14：展示 `City.java` 实体类代码，与画面 2 内容一致，但 `createTime` 字段的注释被修改为 `@Column(name = "create_time")`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
package com.ihm.system.pojo;
import ...
@Entity
@Table(name = "hs_city")
public class City implements Serializable {
@Id
private String id;
private String name;
private java.util.Date createTime;

public void setId(String value){ this.id = value; }
public String getId(){ return this.id; }
public void setName(String value){ this.name = value; }
public String getName(){ return this.name; }
public void setCreateTime(java.util.Date value){ this.createTime = value; }
public java.util.Date getCreateTime(){ return this.createTime; }
}
```

画面 3：
```yaml
#服务配置
server:
  port: 9081
#spring配置
spring:
  application:
    name: ihm-company #指定服务名
#2.数据源配置
datasource:
  driver-class-name: com.mysql.jdbc.Driver
  url: jdbc:mysql://localhost:3306/ihm_system?useUnicode=true&characterEncoding=utf8
  username: root
  password: 111111
jpa:
  database: MySQL
  show-sql: true
  open-in-view: true
```

画面 6：
```java
//新增
@RequestMapping(value = "", method = RequestMethod.POST)
public Result save(@RequestBody City city) {
    //业务操作
    cityService.add(city);
    return new Result(Resultcode.SUCCESS);
}

//根据id更新
@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(value = "id") String id, @RequestBody City city) {
    //业务操作
    city.set(id);
    cityService.update(city);
    return new Result(Resultcode.SUCCESS);
}

//根据id删除
@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
    cityService.deleteById(id);
    return new Result(Resultcode.SUCCESS);
}

//根据id查询
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) throws CommonException {
    City city = cityService.findById(id);
    return new Result(Resultcode.SUCCESS, city);
}
```

画面 7：
```java
@Bean
public ShiroFilterFactoryBean shiroFilter(SecurityManager securityManager) {
    //1.创建过滤器工厂
    ShiroFilterFactoryBean filterFactory = new ShiroFilterFactoryBean();
    filterFactory.setSecurityManager(securityManager);
    //2.设置登录url
    filterFactory.setLoginUrl("/login");
    //3.设置未授权url
    filterFactory.setUnauthorizedUrl("/unauthorized");
    //4.设置拦截规则
    Map<String, String> filterMap = new LinkedHashMap<>();
    filterMap.put("/sys/login", "anon");
    filterMap.put("/sys/faceLogin", "anon");
    filterMap.put("/authc", "authc");
    filterMap.put("/**", "authc");
    filterFactory.setFilterChainDefinitionMap(filterMap);
    return filterFactory;
}
```

画面 10：
```java
package com.ihm.domain.system;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;
public interface CityDao extends JpaRepository<City, String>, JpaSpecificationExecutor<City> {
}
```

画面 12：
```bash
C:\Program Files\Java\JDK 8.0_91\bin\java -jar ...
```

画面 13：
```sql
CREATE TABLE `hs_city` (
  `id` varchar(32) NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

