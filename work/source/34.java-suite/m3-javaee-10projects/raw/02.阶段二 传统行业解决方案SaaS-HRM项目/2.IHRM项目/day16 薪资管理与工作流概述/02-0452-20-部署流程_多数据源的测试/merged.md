# 20-部署流程：多数据源的测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day16 薪资管理与工作流概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day16 薪资管理与工作流概述\20-部署流程：多数据源的测试_【海量资源尽在 ubkz.com】.mp4
- 时长 7分31秒（音频 452s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好了我们现在呢已经解决了这个双数据源的这个配置那接下来呢我们可以一起做一个小小的测试来看一下效果那在我这边的数据库当中呢对于IHMI来说我配置了这么一个表这个表的名字就叫POC User Group那我们可以试一下能不能够通过查询得到对应的数据那需要各位一定要注意的是
[00:31] 在这个双数元配置do我这边已经准备好了不啰嗦直接Ctrl Ccall到do目录下那实体类也是准备好了Ctrl C同样call到我们的entity目录下那各位这个其实就是一些常规的配置咱们主要是为了做一个测试那entity对应的table表那do没什么可说的那我们可以写一段测试来看一下效果好了在我们这个test目录下创建一个
[01:01] 包啊要跟上面这个包保持一个名字啊我把上面这个包名Ctrl C靠到底下Ctrl V创建一个包那接着在里面呢去配置一个我们的测试类好了就叫做AUDIT test好了这是我们的测试类那在测试类上边首先at sprint boot test来at run with sprint j unit
[01:35] for class runner.class那接下来我们开始进行测试那首先呢咱们来测试一下对于这个do能不能注入进来并且连到我们的业务数据也就是IHM数据库当中测试业务数据库at auto where注入进来c user group d a d d a o注入进来那at test
[02:11] public with id test那好了我们来测试一下这边来一个比较简单的直接find all那我们查询出来之后直接打印一下这个list集合数量就可以了.says来走好了这个执行来说呢相对来说没有那么慢啊好了这边还在执行有一点点慢
[03:12] 好了各位来看现在已经结束了这边呢是不是已经打印出我们一共有12条数据哎没错吧好了那这个是我们一起测试了一下业务数据库那除了业务数据库之外接下来呢我们还可以去测试一下测试咱们的ACTIACTIVITIACTIVITI数据库那咱们这个测试呢就需要用到使用ACTIVITI
[03:47] 提供的一些提供的提供的接口来进行测试因为我们说过了对于activity来说呢我们不能直接查数据库我们通过它提供的一些对象或者一些接口调用你们的方法间接着完成数据库的操作好了比如说呢它提供了这么一个对象那这个对象呢叫做Repository ServiceEPORepositoryPRE
[04:17] P-O-S-I-T-O-R-Y-S-E-R-V-I-C-E注意这个是Activity为我们提供的对象A-C-T-I-V-I-T-Y提供的提供的这么一个内置的对象那这个对象呢它跟Spring现在已经无缝集成起来了所以我们直接可以通过AutoWear把它注入进来好了引下包别引错Activity为我们提供好的好了有了这个对象之后呢我们就可以进行查询
[04:54] 好了,at test public willid test acvi test测试一下这个数据库public写错了,替换一下那我们这边呢,先做一个简单的测试就是测试查看中的所有流程因为最终你部署一个流程之后呢我们可以通过activity把这个流程给它查询出来
[05:28] 那这个查询呢很简单直接调用这个对象直接调用这个对象RepositoryService.correctProcessDefinitionQuery那这样一来就定义了一个查询对象注意这个是获取一个查询对象那查询对象获取到了之后我们要查询所有的流程就是点List
[06:01] 那这样一来呢就能获取到所有的流程它是一个list集合那sot我们一起打印一下查询的流程点says好了我们一起来试一下走因为这个单元测试呢其实还会执行sprint boot它的一些内置的一些程序所以这个测试相对来说呀会会会比直接测呢会慢一点各位耐心等待一下咱们来看一下结果
[06:46] 好了各位会发现这边呢是不是打印出来了一共有两条没错吧好了那接着需要跟各位验证一下我数据库当中第一个查的是IHM这套数据库表这个表里面各位来看有12条记录这是我们自己查的什么什么group那接下来呢我们通过activity查询了一下所有的已部署的工作流那我已部署的工作流呢其实是在这个工作流提供的这个表里那在什么位置就在这个
[07:15] GE byte array各位来看我部署了是不是就有两个所以他查询出来是不是只有两条没错吧OK那这样一来咱们也就从侧面验证了咱们的多数据源部署没有问题并且执行起来是成功的

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 Spring Boot 项目中通过 JPA 实现对流程组（ProcUserGroup）的数据库操作，并通过 Activiti 流程引擎查询流程定义。

2) 按时间顺序列出每张画面的要点：
画面1：展示项目结构，打开 `AuditDataSourceConfig.java`，其中配置了数据源和实体管理器工厂，包含 Hibernate 的属性设置。
画面2：在 IDE 中复制 `ProcUserGroupDao.java` 文件，准备进行测试。
画面3：展示 `ProcUserGroup.java` 实体类，包含 `@Entity`、`@Table`、`@Id` 等注解，定义了实体字段。
画面4：展示 `AuditTest.java` 文件，导入了 Spring Boot 测试相关的依赖。
画面5：在 `AuditTest.java` 中添加 `@SpringBootTest` 和 `@RunWith(SpringRunner.class)` 注解。
画面6：在 `AuditTest.java` 中使用 `@Autowired` 注入 `ProcUserGroupDao`。
画面7：在 `AuditTest.java` 中编写测试方法 `test()`，调用 `findAll()` 方法并打印结果大小。
画面8：运行测试，控制台输出 Spring Boot 启动日志。
画面9：在 `AuditTest.java` 中添加注释说明测试内容。
画面10：在 `AuditTest.java` 中添加 `@Autowired` 注入 `RepositoryService`。
画面11：在 `AuditTest.java` 中编写测试方法 `testActiviti()`，调用 `repositoryService.createProcessDefinitionQuery().list()`。
画面12：运行测试，控制台输出 Activiti 流程引擎启动日志。
画面13：控制台输出 Activiti 流程定义查询结果。
画面14：测试成功，显示“1 test passed”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
@Qualifier("ihrmDataSource")
private DataSource ihrmDataSource;

@Bean
public LocalContainerEntityManagerFactoryBean ihrEntityManager() {
    LocalContainerEntityManagerFactoryBean em = new LocalContainerEntityManagerFactoryBean();
    em.setDataSource(ihrmDataSource);
    em.setPackagesToScan(new String[]{"com.ihrm.audit.entity"});
    em.setJpaVendorAdapter(new HibernateJpaVendorAdapter());
    HashMap<String, Object> properties = new HashMap<>();
    properties.put("hibernate.hbm2ddl.auto", env.getProperty("hibernate.hbm2ddl.auto"));
    properties.put("hibernate.dialect", env.getProperty("hibernate.dialect"));
    em.setJpaPropertyMap(properties);
    return em;
}

//平台事务管理器
@Bean
public PlatformTransactionManager ihrmTransactionManager() {
    JpaTransactionManager transactionManager = new JpaTransactionManager();
    transactionManager.setEntityManagerFactory(ihrmEntityManager().getEntityManagerFactory());
    return transactionManager;
}
```

画面3：
```java
package com.ihrm.audit.entity;

import org.springframework.data.jpa.domain.support.AuditingEntityListener;
import javax.persistence.*;
import java.io.Serializable;

@Entity
@Table(name = "proc_user_group")
@Data
@org.springframework.data.jpa.domain.support.AuditingEntityListener
public class ProcUserGroup implements Serializable {
    @Id
    private String id;
    private String name;
    private String param;
    private String isql;
}
```

画面5：
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@RunWith(SpringRunner.class)
@SpringBootTest
public class AuditTest {
}
```

画面6：
```java
@Autowired
private ProcUserGroupDao procUserGroupDao;
```

画面7：
```java
@Test
public void test() {
    List<ProcUserGroup> list = procUserGroupDao.findAll();
    System.out.println(list.size());
}
```

画面10：
```java
@Autowired
private RepositoryService repositoryService;
```

画面11：
```java
@Test
public void testActiviti() {
    //测试activiti中的所有流程
    List<ProcessDefinition> list = repositoryService.createProcessDefinitionQuery().list();
    System.out.println(list.size());
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

