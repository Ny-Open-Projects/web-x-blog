# 画面线理解：18-POI文件导入：跨服务器调用查询部门信息

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day07 员工管理及POI入门
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day07 员工管理及POI入门\18-POI文件导入：跨服务器调用查询部门信息_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:36, 02:06, 02:53, 03:52, 04:25, 05:00, 05:34, 06:34, 07:03, 07:37, 07:52, 08:21, 08:43
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 14:58:40

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Cloud 的分布式 HRM 系统中，部门和用户模块的后端代码实现、数据库操作及前后端交互流程。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 展示了 SQLyog 数据库管理工具界面，查询了 `hrm_company` 数据库中的 `t_user` 表，筛选条件为 `resignation_time` 在 '2018-02' 和 '2019-02' 之间。
- SQL 查询语句：`SELECT * FROM em_resignation WHERE resignation_time LIKE '2018-02%' OR (o.resignation_time LIKE '2019-02%')`

画面 2：
- 展示了 IntelliJ IDEA 中 `DepartmentController.java` 文件的代码，包含对部门的增删改查接口。
- 代码片段：
  ```java
  @RequestMapping(value = "/department", method = RequestMethod.GET)
  public Result findAll() {
      Company company = companyService.findById(companyId);
      List<Department> list = departmentService.findAllAll(company);
      DeptListResult deptlistResult = new DeptListResult(company, list);
      return new Result(ResultCode.SUCCESS, deptlistResult);
  }

  @RequestMapping(value = "/department/{id}", method = RequestMethod.GET)
  public Result findById(@PathVariable(value = "id") String id) {
      Department department = departmentService.findById(id);
      return new Result(ResultCode.SUCCESS, department);
  }

  @RequestMapping(value = "/department/{id}", method = RequestMethod.PUT)
  public Result update(@PathVariable(value = "id") String id, @RequestBody Department department) {
      //1.验证参数
      //2.调用service更新
      departmentService.update(department);
      return new Result(ResultCode.SUCCESS);
  }
  ```

画面 3：
- 展示了 `DepartmentController.java` 文件中新增的 `delete` 和 `findByCode` 方法。
- 代码片段：
  ```java
  @RequestMapping(value = "/department/{id}", method = RequestMethod.DELETE)
  public Result delete(@PathVariable(value = "id") String id) {
      departmentService.deleteById(id);
      return new Result(ResultCode.SUCCESS);
  }

  @RequestMapping(value = "/department/search", method = RequestMethod.POST)
  public Department findByCode(@RequestParam(value = "code") String code, @RequestParam(value = "companyId") String companyId) {
  }
  ```

画面 4：
- 展示了 `DepartmentService.java` 文件，包含 `toPredicate` 方法用于构建查询条件，以及 `deleteById` 和 `findByCode` 方法。
- 代码片段：
  ```java
  Specification<Department> spec = new Specification<Department>() {
      @Override
      public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> cq, CriteriaBuilder cb) {
          //根据公司id查询
          return cb.equal(root.get("companyid"), companyid);
      }
  };
  return departmentDao.findAll(spec);

  public void deleteById(String id) {
      departmentDao.deleteById(id);
  }

  public Department findByCode(String code, String companyId) {
  }
  ```

画面 5：
- 展示了 `DepartmentDao.java` 接口，继承自 `JpaRepository` 和 `JpaSpecificationExecutor`，定义了 `findByCodeAndCompanyId` 方法。
- 代码片段：
  ```java
  public interface DepartmentDao extends JpaRepository<Department, String>, JpaSpecificationExecutor<Department> {
      Department findByCodeAndCompanyId(String code, String companyId);
  }
  ```

画面 6：
- 展示了 Postman 工具，准备发送一个 GET 请求到 `http://localhost:9001/hrm/test/1063676015212913664`，并设置了 Authorization 头。
- Authorization 值：`Bearer 7caefc6c-385e-4f0-8ec5-85912a6066e4`

画面 7：
- 展示了 Windows 桌面的多窗口视图，包括 Excel、Postman、IntelliJ IDEA、SQLyog、SaaS-HRM 等多个应用窗口，用于说明系统集成和数据流转。

画面 8：
- 展示了 `DepartmentFeignClient.java` 文件，定义了通过 Feign 调用远程服务的接口。
- 代码片段：
  ```java
  @FeignClient("hrm-company")
  public interface DepartmentFeignClient {
      @RequestMapping(value = "/company/department/{id}", method = RequestMethod.GET)
      public Result findById(@PathVariable(value = "id") String id);
  }
  ```

画面 9：
- 展示了 `UserService.java` 文件，包含 `findByMobile` 和 `saveAll` 方法。
- 代码片段：
  ```java
  public User findByMobile(String mobile) { return userDao.findByMobile(mobile); }

  @Transactional
  public void saveAll(List<User> list, String companyId, String companyName) {
      for (User user : list) {
          user.setPassword(new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString());
          user.setId(idWorker.nextId()+"");
          user.setCompanyId(companyId);
          user.setCompanyName(companyName);
          user.setInServiceStatus(1);
          user.setEnableState(1);
          user.setLevel("user");
          userDao.save(user);
      }
  }
  ```

画面 10：
- 展示了 SQLyog 数据库管理工具界面，查询了 `hrm_company` 数据库中的 `t_user` 表，筛选条件为 `resignation_time` 在 '2018-02' 和 '2019-02' 之间。
- SQL 查询语句：`SELECT * FROM em_resignation WHERE resignation_time LIKE '2018-02%' OR (o.resignation_time LIKE '2019-02%')`

画面 11：
- 展示了 `UserService.java` 文件，包含 `save` 方法，用于保存用户并设置其部门。
- 代码片段：
  ```java
  public void save(User user) {
      String id = idWorker.nextId()+"";
      String password = new Md5Hash(source: "123456", user.getMobile(), hashiterations: 3).toString();
      user.setId(id);
      user.setPassword(password);
      user.setLevel("user");
      user.setEnableState(1);
      user.setInServiceStatus(1);
      user.setCompanyId(companyId);
      user.setCompanyName(companyName);
      user.setDepartmentId(department.getid());
      user.setDepartmentName(department.getname());
      userDao.save(user);
  }
  ```

画面 12：
- 展示了 IntelliJ IDEA 中 `DepartmentFeignClient.java` 文件，显示了 `findById` 方法的定义。
- 代码片段：
  ```java
  @RequestMapping(value = "/company/department/{id}", method = RequestMethod.GET)
  public Result findById(@PathVariable(value = "id") String id);
  ```

画面 13：
- 展示了 SQLyog 数据库管理工具界面，查询了 `hrm_company` 数据库中的 `t_user` 表，筛选条件为 `resignation_time` 在 '2018-02' 和 '2019-02' 之间。
- SQL 查询语句：`SELECT * FROM em_resignation WHERE resignation_time LIKE '2018-02%' OR (o.resignation_time LIKE '2019-02%')`

画面 14：
- 展示了 SaaS-HRM 系统的 PPT 页面，标题为“4.2 员工导入”，子标题“4.2.1 搭建环境”，并展示了 `pom.xml` 中需要添加的依赖。
- 依赖代码：
  ```xml
  <dependency>
      <groupId>org.apache.poi</groupId>
      <artifactId>poi</artifactId>
      <version>4.0.1</version>
  </dependency>
  ```
