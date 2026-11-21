# 07-部门微服务：抽取公共代码和测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\07-部门微服务：抽取公共代码和测试_【海量资源尽在 ubkz.com】.mp4
- 时长 11分48秒（音频 708s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 我们已经把这些基本的代码都写好了那其实我们这个代码当中呢还有一些可以修改的点或者抽取的一些内容在里面比如说我们现在的企业微服务当中可能会在这边获取到我的企业ID那以后呢员工的微服务雇员的微服务系统的微服务等等等等很多是不是都有可能要获取到你的企业ID啊所以如果说每一个Controller当中都要自己去写一把这样类似的方法的话第一太麻烦第二维护起来
[00:32] 就变成了我们的一种负担那么其实可以把这些内容完整的给它抽取出来那抽取出来之后呢我们直接使用负类当中的内容其实就可以了所以在这边我在common这个包下去设置一个我们公共的一个Controller出来或者一个抽象的一个负类出来在其中我们把公共内容放置进去其实就可以了好在这边呢我去创建一个公共的Controller
[01:02] 把它放到c1troc1trol1controller这个包下我就叫做base controllerOK那比如说呢我之后呢可能要获取很多的内容private不行咱们来一个publicpublic比如说呢我可能还要获取到http servlet requestservlet requestrequest比如说呢还要获取到http servlet
[01:41] response比如说呢可能还要获取到private死菌类型的company idok那我们应该如何去做呢其实很简单其实很简单在sprintmvc当中它支持一个注解那个这个注解指的是执行所有control的方法之前它去干的一些事情比如说呢在在这边我可以写一方法publicvoid比如说就叫做setres
[02:14] and requestrequest and responsereqok那好了这边可以http servlet requestrequesthttp servletresponse那好了接下来我们就可以list.request等于requestlist.response就等于request
[02:46] bounce当然了我们可以类似点companycompanycompany id等于我现在先写上1这个问题以后再去解决company id的问题当然了注意我现在写上的其实这个方法什么都代表不了那我需要在这个方法之前配置一个注解这个注解叫做atamodal attribute那配置上atamodal attribute之后
[03:20] 配上modal attribute之后如果说如果说抱歉这边有一个错误刚才注意到了response没给复制responseOK那接着继续说modal attribute那这个modal attribute指的是在进入控制器方法之前执行的内容那这样一来如果说我department Controller那我在这边如果说是继承base Controller
[03:52] 那如果继承base Controller之后比如说要执行C5那执行C5之前它就会执行model attribute里面执行的内容那这样一来它其实就会对requestresponse以及company进行复制那这样一来值其实就已经有了那对于我们这回company已经有值了那我在这边是不是直接就能从我的副类当中获取到这个company的值其实就可以了当然了我们这边publicok就可以了
[04:27] 当然了我这个public现在定义的范围有点大我们可以把它定义为protect受保护的当然了我们以后可能还会用到死菌类型的company name我这边的一并也都给它写出来其实就可以了同样的这边先不管它我们都用默认值就可以company name刚才把这个不小心删掉了我们这边再声明一下目前使用使用
[05:12] company id等于1company name比如说呢就等于传职博客先以这种形式的方式呢先给它复制当我们以后学习了其他内容之后呢我们还会对它进行修改OK那这样一来我公共的Controller已经写好那写好了之后在我们的子类当中直接就能拿到副类里面的内容其实就能完成的操作比如说这边company id都改了都已经改了那底下还有了
[05:51] 没有了OK那这样一来我们全部都改好了那改好了之后其实还有一个内容呢我们也可以做修改比如说在我们的Service当中department的Service我们一起找到看一下可能需要的改的点那比如在这边呢我们可以构造了一个special case那这个special case首先它满足这么两件事情第一个事情呢是我只查询company
[06:25] 那第二件事呢就是有很多的地方很多的地方它都有都都需要根据common id来进行查询好了还有第三件事就是我们可能这个common id呢要在很多的对象当中都需要这种都具有
[06:51] company id这个属性那这样一来你就会发现我部门里面有这个属性对应的字段company id那比如说呢我明天用户里面也有后天呢其他的东西都有都是一模一样那我们其实就可以把这个special case也给它抽取出来那抽取出来搞一个灵活自动加载的这么一个special case那我们写起来其实就更加简单一些了嘛所以既然呢我们可以抽取一个公共的比如说叫Service重点就是为了
[07:20] 获取spatial location好了那我们怎么做呢其实也把公共的内容抽取到我们的common这个包下好了那这边同样的去写一个类比如说呢我就叫做Service-base-Service那这个base-Service当中呢我这边提供一个范形提供一个范形为啥这样提供范形呢是因为这个Service里面获取到的spatial location它是有范形的OK
[07:57] 那好了接下来呢我们base survey当中可以添加一个方法也是protectspecification好了t比如说呢我就叫做get spcok当然了你需要传递一个company id过来ok我这边呢倒下包啊抱歉倒包是不行的我们需要引入一下pom坐标好了pom文件的坐标需要用的是sprintdata.jpasprintdata.jpa
[08:36] 把这个坐标也加加到我们common这个包下defendaseok 已经进来那接下来呢我们这边可以把这个包也导进来哦有了好那接下来呢我们可以构造special case那就是special casespec等于new一个special case好了这边就t吧
[09:08] 好了那接下来呢里面的这个代码的一个写法呢其实比较简单了跟我们刚才departments这里面写的是一模一样的根据企业ID进行查询即可OK这边呢CB但是呢我们刚才就强调过要想这样去做的话或者要想去使用当前的这个方法的话有这么几个条件一定要遵守就是说表和属性当中必须要有common ID必须要有并且呢是一模一样的
[09:38] 并且呢你当前完成的是只根据common id查因为我里面代码之后可能要写很多很多的这种方式所以我把它抽取出来自己去构造其实就可以了这边有一个返回值return好了那这样一来在我Service层当中我们就可以把这一段全部都注入起来那我底下find就可以继承flaybase Service那继承flay之后我们这边find
[10:17] 就叫做get s p e c即可把company id传递过去OK那这样一来我这个代码呢其实也已经都抽取成功了抽取成功了之后还有最后一步我们要做就是看一下我们当前的这个微服务能不能跑起来并且是否能够正常的获取到企业这些操作和我们的部门这些内容而这边呢我找到我们的启动类去执行
[10:52] 那接下来呢我们目前微服务测试呢我们还是借助postman这种形式来做的所以我打开postman各位耐心等待一下这个postman呢打开可能有一点点慢啊OK它在当启动好了启动成功了之后呢接下来呢我们请求的其实就是昨天的commy微服务好了就是departmentget方式提交代表查询全部列表走我们来看一下效果各位会发现所有内容都有
[11:27] 那继续我们在这边呢再来一个杠根据ID查一把走哎也没问题没错吧好了那这样一来呢我们基本的这个程序做过了测试并且我们也抽取出来了两个工具方法

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中，通过创建 BaseController 和 BaseService 基类，实现对 Controller 和 Service 层中公共逻辑（如设置公司 ID）的抽象和复用，以简化业务代码。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示 DepartmentController.java 文件，其中包含 save 和 findAll 方法。
- save 方法中设置了 companyid = "1"，并调用 departmentService.save(department)。
- findAll 方法用于查询指定公司下的部门列表。

画面 2：
- 展示 BaseServletRequest 类的源码，用于演示 HTTP 请求处理。

画面 3：
- 展示 BaseServletRequest 类的源码，用于演示 HTTP 请求处理。

画面 4：
- 展示 BaseServletRequest 类的源码，用于演示 HTTP 请求处理。

画面 5：
- 展示 DepartmentController.java 文件，其中包含 save 和 findAll 方法。
- save 方法中设置了 companyid = "1"，并调用 departmentService.save(department)。
- findAll 方法用于查询指定公司下的部门列表。

画面 6：
- 展示 BaseServletRequest 类的源码，用于演示 HTTP 请求处理。

画面 7：
- 展示 CompanyService.java 文件，其中包含 add 方法。
- add 方法中设置了 id、companyName、state 等属性，并调用 companyDao.save(company)。

画面 8：
- 展示 DepartmentController.java 文件，其中包含 findAll 方法。
- 在 findAll 方法中，创建了一个 Specification<Department> 对象，并调用 departmentDao.findAll(spec)。
- 弹出“Create New Class”对话框，提示创建新类。

画面 9：
- 展示 BaseService.java 文件，其中包含 getSpec 方法。
- getSpec 方法用于根据 companyid 获取 Specification 对象。

画面 10：
- 展示 pom.xml 文件，其中包含 <parent> 标签，指定了父项目信息。
- <groupId>com.ihrm</groupId>，<artifactId>ihrm_common</artifactId>，<version>1.0-SNAPSHOT</version>。

画面 11：
- 展示 DepartmentService.java 文件，其中包含 findAll 方法。
- 在 findAll 方法中，创建了一个 Specification<Department> 对象，并调用 departmentDao.findAll(spec)。
- 弹出“Create New Class”对话框，提示创建新类。

画面 12：
- 展示 DepartmentService.java 文件，其中包含 save 方法。
- save 方法中设置了 department 的 companyid，并调用 departmentDao.save(department)。

画面 13：
- 展示 CompanyApplication.java 文件，其中包含 main 方法。
- main 方法中调用 SpringApplication.run(CompanyApplication.class, args)。
- 定义了一个 @Bean 方法，返回一个 IdWorker 对象。

画面 14：
- 展示 Postman 工具界面，正在发送一个 GET 请求到 http://localhost:9001/company/departments/105238836272664578。
- 请求正在加载中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
public Result save(@RequestBody Department department) {
    // 企业id：目前使用固定值，以后会解决
    String companyId = "1";
    department.setCompanyId(companyId);
    // 2. 用Service完成企业
    departmentService.save(department);
    // 3. 轮询返回
    return new Result(ResultCode.SUCCESS);
}

// 查询企业的部门列表
// 指定企业id
public Result findAll() {
    // 1. 指定企业id
    String companyId = "1";
    // 2. 定义查询
    Company company = companyService.findById(companyId);
    // 3. 查询部门
    List<Department> list = departmentService.findAll(companyId);
    DeptListResult deptlistResult = new DeptListResult(list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 5：
```java
@RequestBody Department department) {
    // 企业id：目前使用固定值，以后会解决
    String companyId = "1";
    department.setCompanyId(companyId);
    // 2. 用Service完成企业
    departmentService.save(department);
    // 3. 轮询返回
    return new Result(ResultCode.SUCCESS);
}

// 查询企业的部门列表
// 指定企业id
public Result findAll() {
    // 1. 指定企业id
    String companyId = "1";
    // 2. 定义查询
    Company company = companyService.findById(companyId);
    // 3. 查询部门
    List<Department> list = departmentService.findAll(companyId);
    DeptListResult deptlistResult = new DeptListResult(list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 7：
```java
@Service
public class CompanyService {
    @Autowired
    private CompanyDao companyDao;
    @Autowired
    private IdWorker idWorker;
    // 1. 保存企业
    // 2. 设置idworker
    // 3. 通过idworker生成id
    // 4. 保存企业
    public void add(Company company) {
        // 基本属性的设置
        String id = idWorker.nextId() + "";
        company.setId(id);
        company.setAuditState("0"); // 0：未审核，1：已审核
        company.setState(1); // 0：未激活，1：已激活
        companyDao.save(company);
    }
}
```

画面 8：
```java
public List<Department> findAll(String companyId) {
    // 用户构造查询条件
    // 1. 只查询companyId
    // 2. 很多地方都需要根据companyId查询
    // 3. 很多的对象都具有companyId
    Specification<Department> spec = new Specification<Department>() {
        @Override
        public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            // 根据企业id查询
            return cb.equal(root.get("companyId").as(String.class), companyId);
        }
    };
    return departmentDao.findAll(spec);
}
```

画面 10：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    <parent>
        <artifactId>ihrm_parent</artifactId>
        <groupId>com.ihrm</groupId>
        <version>1.0-SNAPSHOT</version>
    </parent>
    <artifactId>ihrm_common</artifactId>
</project>
```

画面 11：
```java
public List<Department> findAll(String companyId) {
    // 用户构造查询条件
    // 1. 只查询companyId
    // 2. 很多地方都需要根据companyId查询
    // 3. 很多的对象都具有companyId
    Specification<Department> spec = new Specification<Department>() {
        @Override
        public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
            // 根据企业id查询
            return cb.equal(root.get("companyId").as(String.class), companyId);
        }
    };
    return departmentDao.findAll(spec);
}
```

画面 12：
```java
@Service
public class DepartmentService extends BaseService<Department> {
    @Autowired
    private DepartmentDao departmentDao;
    @Autowired
    private IdWorker idWorker;
    // 1. 保存部门
    public void save(Department department) {
        // 设置主键的值
        String id = idWorker.nextId() + "";
        department.setId(id);
        departmentDao.save(department);
    }
}
```

画面 13：
```java
package com.ihrm.company;
// 1. 扫描的包扫描
// 2. 扫描的包扫描
// 3. 扫描的包扫描
// 4. 扫描的包扫描
// 5. 扫描的包扫描
// 6. 扫描的包扫描
// 7. 扫描的包扫描
// 8. 扫描的包扫描
// 9. 扫描的包扫描
// 10. 扫描的包扫描
// 11. 扫描的包扫描
// 12. 扫描的包扫描
// 13. 扫描的包扫描
// 14. 扫描的包扫描
// 15. 扫描的包扫描
// 16. 扫描的包扫描
// 17. 扫描的包扫描
// 18. 扫描的包扫描
// 19. 扫描的包扫描
// 20.

