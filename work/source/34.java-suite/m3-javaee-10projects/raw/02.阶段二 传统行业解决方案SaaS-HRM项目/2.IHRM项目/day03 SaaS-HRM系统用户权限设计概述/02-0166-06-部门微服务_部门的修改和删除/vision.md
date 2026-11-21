# 画面线理解：06-部门微服务：部门的修改和删除

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\06-部门微服务：部门的修改和删除_【海量资源尽在 666java.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:28, 00:53, 01:13, 01:39, 02:03, 02:31, 03:11, 03:33, 03:55, 03:59, 04:27, 04:41, 04:49
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:30:09

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中为部门（Department）实体实现完整的 CRUD（增删改查）接口，包括控制器层的代码编写与 API 文档的对应关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 IntelliJ IDEA 中的 DepartmentController.java 文件，其中包含 findALL 方法。
- 画面中嵌入了多个窗口，包括：
  - 一个名为“SaaS-HRM 的API文档”的网页，显示了 GET /department/{departmentId} 接口。
  - 一个名为“SQLyog Ultimate - localhost/h...”的数据库管理工具窗口。
  - 一个名为“index.js - project-sass-hrm-vue...”的前端项目代码窗口。
  - 一个名为“SaaS-HRM 的接口.pdf”文档窗口。
  - 一个名为“SaaS-HRM 的接口.pdf”文档窗口。
- 代码片段：
  ```java
  department.setCompanyId(companyId);
  //2.调用service层逻辑
  departmentService.save(department);
  ```

画面 2:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 3:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 4:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 5:
- 展示了 SaaS-HRM 的 API 文档页面。
- 画面中显示了 PUT /department/{departmentId} 接口的详细信息。
- 接口参数：
  - Name: departmentId (required)
  - Description: DepartmentID
  - body: Department实体
  - Example Value:
    ```json
    {
      "id": "string",
      "companyId": "string",
      "parentId": "string",
      "code": "string",
      "introduce": "string",
      "manager": "string"
    }
    ```

画面 6:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 7:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 8:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 9:
- 展示了 Result.java 文件的代码。
- 代码注释：
  ```java
  /**
   * 返回结果
   */
  @Data
  @AllArgsConstructor
  public class Result {
      private boolean success; //是否成功
      private Integer code; //返回码
      private String message; //返回信息
      private Object data; //返回数据
  }
  ```

画面 10:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 11:
- 展示了 SaaS-HRM 的 API 文档页面。
- 画面中显示了 DELETE /department/{departmentId} 接口的详细信息。
- 接口参数：
  - Name: departmentId (required)
  - Description: DepartmentID
  - Responses:
    - Code: 200
    - Description: 成功

画面 12:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 13:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```

画面 14:
- 展示了 DepartmentController.java 文件中 findALL 方法的完整代码。
- 代码注释：
  ```java
  /**
   * 查询企业的部门列表
   * 指定企业id
   */
  @RequestMapping(value="/department",method = RequestMethod.GET)
  public Result findAll() {
      //1.指定企业id
      String companyId = "1";
      //2.查询
      Company company = companyService.findById(companyId);
      //3.校验返回结果
      DeptListResult deptlistResult = new DeptListResult(company,list);
      return new Result(ResultCode.SUCCESS,deptlistResult);
  }
  ```
