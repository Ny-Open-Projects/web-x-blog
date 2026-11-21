# 画面线理解：19-代码生成器：测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\19-代码生成器：测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:06, 01:53, 02:21, 02:36, 02:53, 03:42, 04:21, 04:46, 05:15, 05:43, 06:26, 07:09, 07:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:09:31

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的权限管理系统中，城市（City）实体的 POJO、DAO、Service、Controller 层的代码结构与配置，以及如何通过 Shiro 实现权限控制，并最终在数据库中验证实体表结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示项目目录结构，当前选中 `pojo` 文件夹，其中包含 `City.java`、`Department.java` 等实体类文件。
画面 2：展示 `City.java` 实体类代码，使用 `@Entity` 和 `@Table` 注解，定义了 `id`、`name`、`createTime` 字段及其 getter/setter 方法。
画面 3：展示 `application.yml` 配置文件，包含服务端口、Spring 配置、数据源（MySQL）和 JPA 配置。
画面 4：展示 `dao` 文件夹下的文件列表，包含 `CityDao.java`、`CompanyDao.java` 等。
画面 5：展示 `service` 文件夹下的文件列表，包含 `CityService.java`、`CompanyService.java` 等。
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
C:\Program Files\Java\jdk1.8.0_91\bin\java -jar ...
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
