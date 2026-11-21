# 画面线理解：07-部门微服务：抽取公共代码和测试

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\07-部门微服务：抽取公共代码和测试_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:11, 01:35, 02:21, 03:08, 04:05, 04:56, 06:10, 07:35, 08:21, 08:39, 09:34, 10:10, 10:48, 11:33
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:31:01

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
    // 2. 用service完成企业
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
    // 2. 用service完成企业
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
