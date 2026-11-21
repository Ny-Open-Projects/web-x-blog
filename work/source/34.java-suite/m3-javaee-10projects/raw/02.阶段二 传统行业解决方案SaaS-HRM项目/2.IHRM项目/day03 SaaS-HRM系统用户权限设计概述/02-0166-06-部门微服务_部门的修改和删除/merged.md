# 06-部门微服务：部门的修改和删除

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\06-部门微服务：部门的修改和删除_【海量资源尽在 666java.com】.mp4
- 时长 4分52秒（音频 293s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好了那已经把部门列表我们搞定了那接下来呢咱们继续往下看还有三个方法根据ID查询那根据ID查询这个应该如何去做呢也比较简单Ctrl Ccall过来Ctrl V好了那咱们注意一下我请求的API后面呢需要接收一个我们的地址参数一个地址参数所以呢接下来呢我在这边
[00:30] 构造出我的地址参数比如说给它起一个名字就叫做ID那我们的请求方式也叫get没问题public result好了find by ID那我们都知道会给我把一个地址参数ID传过来所以我这边借助的是pass variable直接把地址参数获取过来就可以了死巨类型的ID当然了pass variable你可以给它指定你地址参数的名称等于IDOK那咱们的方法
[01:04] 写好了之后里面就可以构造代码但当然了我这个代码比较简单直接调用Service打点find by id获取对象即可那这样一来department有了那接着就是构造返回结果return都是一模一样的都是一模一样的好了这回把返回结果department存进去好了那接下来呢根据id查询我们已经有了那接下来继续往下看还有叫做修改department
[01:41] 那当然了我们修改的时候其实也是根据ID进行修改那我们的请求链接呢各位来看地址参数以及数据所以对于我们来说数据可以封装成一个对象request body那这边pass variable是不是得到参数啊所以接下来呢我们可以把这个方法也给它写出来publicpublic result类型返回值update那update
[02:17] 好了那给他可以指定我的请求链接跟上面这个差不多只不过请求方式变成了put那我在这边呢需要指定他的IDOK那我还需要把你请求的这个对象封装到底他的门当中OK那这样一来我们的参数也已经搞定了那接下来呢我们要做的第一件事呢其实就可以调用Service打点我们叫做update
[02:51] 但是我update之前需要我们做的第一件事就是设置我们修改的部门ID好了接着第二件事才是真真正正的调用哎完成更新操作好了设置其ID呢很简单department打点打点set IDID好了把ID传过来那接下来调用我们的Service更新就可以了好了更新之后构造返回结果return
[03:28] 又一个result好了注意了我这里面的构造方法写的比较多其中有一个直接传code那这个传code的时候我data部分其实就是空那也可以传code谈data那这样一来success code message就有了但是data部分是不是也就已经有值了OK那接下来呢我们这边返回的其实没有任何的内容直接success就可以了OK那这样一来根据ID查
[03:55] 根据ID修改咱们都已经搞定了还有最后一个方法就是根据ID来进行删除那根据ID进行删除呢也比较简单请求链接是一样的只不过我的请求方式变成了delete所以我从上边的直接Ctrl C Ctrl Vcall一个方法根据ID删除好了这边的请求方式delete那方法呢delete
[04:27] 好了我只需要一个参数ID就可以那接着这个删除方法比较简单就不做任何的多说了Department Service打点调用方法Delete by ID把ID传进去即可那这样一来我们当前部门管理的VFU Controller就已经全部都写好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中为部门（Department）实体实现完整的 CRUD（增删改查）接口，包括控制器层的代码编写与 API 文档的对应关系。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1:
- 展示了 IntelliJ IDEA 中的 DepartmentController.java 文件，其中包含 findALL 方法。
- 画面中嵌入了多个窗口，包括：
  - 一个名为“SaaS-HRM 的API文档”的网页，显示了 GET /department/{departmentId} 接口。
  - 一个名为“SQLyog Ultimate - localhost/h...”的数据库管理工具窗口。
  - 一个名为“index.js - project-sass-hrm-Vue...”的前端项目代码窗口。
  - 一个名为“SaaS-HRM 的接口.pdf”文档窗口。
  - 一个名为“SaaS-HRM 的接口.pdf”文档窗口。
- 代码片段：
  ```java
  department.setCompanyId(companyId);
  //2.调用Service层逻辑
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

