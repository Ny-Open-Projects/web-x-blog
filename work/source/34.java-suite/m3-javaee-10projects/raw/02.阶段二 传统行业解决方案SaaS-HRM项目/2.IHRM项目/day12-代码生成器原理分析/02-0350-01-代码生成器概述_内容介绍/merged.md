# 01-代码生成器概述：内容介绍

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day12-代码生成器原理分析
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day12-代码生成器原理分析\01-代码生成器概述：内容介绍_【海量资源尽在 ubkz.com】.mp4
- 时长 6分11秒（音频 371s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 各位朋友大家好那今天呢我们继续去完成SaaS人力资源管理系统的开发那对于今天呢和各位要聊的内容呢叫做代码生成器那其实对于代码生成器来说呢大部分朋友可能都用过市面上一些比较好的代码生成器那还有一部分朋友呢可能自己也设计自己也写过代码生成器
[00:27] 那我们今天它的主要目的就是系统的去学习一下代码生成器咱们来分析对一个代码生成器它的内部原理究竟是什么样的它是有什么构成的内部需要咱们一些什么样的技术作为补充那直至我们完成属于我们自己的一个代码生成器的一个代码编写那对于咱们今天的课程安排是这样的首先呢第一个和各位来谈一谈代码生成器的它的前世今生它为什么要有
[00:56] 它内部的一些注意事项是什么它内部是由什么构成的如果我们自己要写代码生成器我们需要掌握那样的技术主要是一些原理性的一些分析那接下来第二块呢我们要聊的一个点呢叫做FreeMarker那我们很多朋友呢其实也是玩过一些FreeMarker那我们今天呢系统呢对它进行一个回顾那除了FreeMarker之外要想去设计一个代码生成器之外还需要各位掌握的是数据库里面的一个小的细节叫做原数据
[01:25] 那对这个原数据里面存在的一些内容比如说要有数据库的原数据比如说要有我们参数的原数据比如说还会有我们查询结果集的原数据那这些原数据也需要跟各位讲清楚那其实FreeMarker和原数据就已经对我们代码升级器打下了一个比较坚实的基础那这两块基础我们补充完成之后最终我们去完成属于我们自己代码升级器所以对于我们来说今天一共就四块第一块重点是一些原理部分内容
[01:55] 第二块第三块是补充一些之前的一些支点第四块我们开始着手写代码好了咱们先来看第一个就是要浅谈代码生成器那首先需要跟各位简单的看一下我们之前写的这个项目那我们写这个项目其中呢有一个包叫做model咱们就从咱们的实体类读门开始说起那在这个实体类当中呢咱们写过了比如说呢企业写过了雇员
[02:24] 还写了系统等等等等的这些实体类咱们只说实体类比如说有company比如说department好了这边呢还有user还有角色等等我不就一一打开了那我想跟各位来聊的是啊那对于这几个实体类当中它从哪开始咱们着手去写咱们进行一个代码开发是不是先拿到数据库接着把数据库里面表抽象成一个实体类啊那这些一个一个的我们实体类当中的属性是不是就是
[02:52] 我们数据库当中代表的一个字段那拿到了这些内容之后我们接下来开始去着手去编写DAO好了我随便打开一个DAO我们一起简单的再来看一下OKcompany DAOdepartment DAO那这个DAO里面首先这是一个接口后面这都是一些比如说GPA response gridGPA specificationexecutor
[03:17] 这些内容你各位来看不管是department的部门还是我们的企业是不是写法基本上都是差不多接着还有serviceservice这边咱们打开来看其实也是差不多的增删改查的逻辑我只说咱们大面上的增删改查逻辑是不是都是差不多的我们之前学过一套我们是不是开始写第二套的时候copy一份拿过来改改的过程其实这无形当中增加了我们成全的副本
[03:46] 那所以对于这些基本上逻辑都相似的一些功能那我们自己去写的话就有点麻烦那可不可以用一个代码生成器让计算机自动的帮助我们生成呢那它帮助我们生成从哪开始生成它的起点是什么有朋友说了是不是应该是实体类那实体类从哪来是不是就数据库表所以对于这些内容
[04:12] 特别是重复性比较强的内容完全可以告诉代码生成器我的数据库比较在那边你自动帮我生成其实就可以了所以有很多的大牛程序员就写了很多的优秀代码生成器帮助我们从数据库自动的生成我想要的实体类想要的DO想要的Service那当然了还有一些共性的比如说那Controller它里面的一些基本增长给啥方法
[04:39] OK那这边呢在讲义上呢我也跟各位简单的说过了其实呢我们写很多代码的时候呢都是有规律的而这些代码呢往往都是比较重复性重复性比较强基本上都是一样的比如刚才看过的部门比如刚才看到的企业都有基本增传改差那都是调用save方法update方法delete方法等等等等它传的参数把当前10些类对象传进去其实就可以了这些都是一些共性的一些内容
[05:06] 所以对于这些共用性的内容我们就可以让计算机帮助我们进行生成OK那如果说计算机帮助我们生成了那其实最大的一个好处就是减少了我们手工的这种重复性的一个劳动没错吧那刚才我们说过了那我们的最终目的是不是只需要告诉代码生成器我的数据库表在那摆着你自动的根据表去创建是不是就可以了所以呢对于这些内容完全可以交给代码生成器来做
[05:36] 那对于我们成语言自己写的内容要不要写呢肯定也要啊那我们刚才说过了代码生成器生成的是不是全部都是一些共性的一些内容那如果明天给你来个需求你帮我去写一个下单电商的一个买东西的一个下单需求那代码生成器能生成吗不可能对不对啊所以对于我们成语言来说如果使用代码生成器共性的内容代码生成器生成那对于我们成语言来说
[06:02] 关注的就是更加复杂的这些业务逻辑那这样就可以极大的提高我们程序员的工作效率了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解代码生成器原理，通过分析公司和部门实体的代码结构，展示如何使用 Spring Data JPA 实现数据访问层、服务层的代码自动生成。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程PPT第12章“代码生成器原理分析”的第1节“浅谈代码生成器”，介绍传统开发中重复性代码（如Controller、Service、Dao）的痛点，引出代码生成器的价值。
画面2：展示IntelliJ IDEA项目结构，根目录为`ihrm_parent`，包含多个子模块如`ihrm_common_model`、`ihrm_company`等。
画面3：在IDEA中打开`Department.java`文件，展示实体类代码，包含`@Entity`、`@Table`、`@Data`等注解，以及`id`、`pid`、`companyId`、`name`等字段。
画面4：在IDEA中切换到`Company.java`文件，展示实体类代码，包含`@Entity`、`@Table`、`@Data`等注解，以及`id`、`name`、`managerId`、`version`等字段。
画面5：在IDEA中展示`Company.java`文件，光标位于`@Entity`注解下方，显示实体类的注解和字段。
画面6：在IDEA中展示`Company.java`文件，光标位于`@Entity`注解下方，显示实体类的注解和字段。
画面7：在IDEA中打开`CompanyDao.java`文件，展示接口代码，使用`@Repository`注解，继承`JpaRepository`和`JpaSpecificationExecutor`。
画面8：在IDEA中展示`CompanyDao.java`文件，光标位于`JpaSpecificationExecutor`的`<Company>`泛型参数处。
画面9：在IDEA中打开`CompanyService.java`文件，展示服务层代码，包含`@Service`注解，`@Autowired`注入`CompanyDao`，并实现`add`方法。
画面10：在IDEA中展示`DepartmentService.java`文件，光标位于`findALL`方法的`Specification<Department>`参数处，展示使用`Specification`构建查询条件的代码。
画面11：在IDEA中展示`DepartmentService.java`文件，光标位于`deleteById`方法的`String id`参数处，展示删除方法的代码。
画面12：展示课程PPT第12章“代码生成器原理分析”的第1节“浅谈代码生成器”，内容与画面1相同。
画面13：展示课程PPT第12章“代码生成器原理分析”的第1.2节“需求分析”，包含“用户界面”和“代码生成器”两个模块，以及“数据库信息”作为连接。
画面14：展示课程PPT第12章“代码生成器原理分析”的第1.2节“需求分析”，内容与画面13相同。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面3：
```java
import ...

@Entity
@Table(name = "co_department")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Department implements Serializable {
    private static final long serialVersionUID = 90884332495284488553L;
    //ID
    private String id;
    //父级ID
    private String pid;
    //企业ID
    private String companyId;
    //部门名称
    private String name;
    //部门编码，同级部门不可重复
    private String code;
}
```

画面4：
```java
import ...

@Entity
@Table(name = "co_company")
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Company implements Serializable {
    private static final long serialVersionUID = 594829328797158219L;
    //ID
    private String id;
    //公司名称
    private String name;
    //企业登录账号ID
    private String managerId;
    //当前版本
    private String version;
    //创建时间
    private Date createTime;
}
```

画面7：
```java
package com.ihrm.company.dao;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.JpaSpecificationExecutor;

/**
 * 自定义dao接口继承
 * JpaRepository<实体类,主键>
 * JpaSpecificationExecutor<实体类>
 */
public interface CompanyDao extends JpaRepository<Company,String>, JpaSpecificationExecutor<Company> {
}
```

画面9：
```java
@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;
    @Autowired
    private IdWorker idWorker;
    //...
    public void add(Company company) {
        String id = idWorker.nextId()+"";
        company.setId(id);
        company.setAuditState("0");//0:未审核，1：已审核
        company.setState(1);//0:未删除，1：已删除
        companyDao.save(company);
    }
}
```

画面10：
```java
//...
public List<Department> findAll(String companyId) {
    //用户检查查询条件
    //1.查询所有对象
    //2.很多的地方都需要根据companyId查询
    //3.很多的对象都拥有companyId
    //...
    Specification<Department> spec = new Specification<Department>() {
        @Override
        public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            //root:包含了所有的对象数据
            //cq: 一般不用
            //cb: 构造查询条件
            return cb.equal(root.get("companyId").as(String.class),companyId);
        }
    };
    return departmentDao.findAll(getSpec(companyId));
}
```

画面11：
```java
//...
public void deleteById(String id) {
    departmentDao.deleteById(id);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1、12：PPT标题为“第12章 代码生成器原理分析”，子标题为“1 浅谈代码生成器”，内容包括“理解代码生成器的需求和实现思路”、“掌握freemaker的使用”、“理解数据库中的元数据”、“完成环境搭建工作”。
画面13、14：PPT标题为“第12章 代码生成器原理分析”，子标题为“1.2 需求分析”，包含两个模块：“用户界面”和“代码生成器”，以及“数据库信息”作为连接，表示“用户界面”通过“数据库信息”连接到“代码生成器”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（已按要求执行）

