# 画面线理解：05-部门微服务：查询企业列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\05-部门微服务：查询企业列表_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:06, 00:36, 02:20, 02:58, 04:21, 05:45, 07:23, 09:04, 09:50, 10:32, 10:50, 11:37, 12:16, 13:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:29:21

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现部门管理的 API，包括控制器、服务层、数据访问层和响应结果类的编写，以及对应的 API 文档展示。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 API 文档中 GET /department 和 GET /department/{departmentId} 两个接口的响应示例，响应体为 JSON 格式，包含 code、success、message 和 data 字段。
画面 2: 展示 DepartmentController.java 文件，定义了 @RequestMapping 注解和 @CrossOrigin 注解，以及 Controller 类的声明。
画面 3: 展示 DepartmentService.java 文件，包含 save 和 update 方法，用于保存和更新部门信息。
画面 4: 展示 DepartmentService.java 文件，包含 findById 和 findAll 方法，其中 findAll 方法使用了 Specification 接口进行条件查询。
画面 5: 展示 DepartmentService.java 文件，正在编写 Specification 的 toPredicate 方法，用于构建查询条件。
画面 6: 展示 DepartmentService.java 文件，完成 toPredicate 方法的编写，使用 cb.equal(root.get("companyId").as(String.class), companyId) 来匹配 companyId。
画面 7: 展示 API 文档中 GET /department 接口的响应示例，响应体为 JSON 格式，包含 code、success、message 和 data 字段，其中 data 包含 company 和 depts 信息。
画面 8: 展示 DeptListResult.java 文件，正在定义类的私有字段，包括 companyId、companyName、companyManage 和 depts。
画面 9: 展示 DeptListResult.java 文件，添加了 @Getter 和 @Setter 注解，并定义了私有字段。
画面 10: 展示 DeptListResult.java 文件，正在编写构造函数，初始化 companyId、companyName、companyManage 和 depts 字段。
画面 11: 展示 DeptListResult.java 文件，完成构造函数的编写，使用 this 关键字初始化字段。
画面 12: 展示 DepartmentController.java 文件，正在编写 findAll 方法，用于查询企业下的部门列表。
画面 13: 展示 DepartmentController.java 文件，正在编写 findAll 方法，使用 companyService.findById(companyId) 获取企业信息。
画面 14: 展示 DepartmentController.java 文件，完成 findAll 方法的编写，创建 DeptListResult 对象并返回 Result 对象。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```json
{
  "code": 0,
  "success": true,
  "message": "string"
}
```

画面 2:
```java
@CrossOrigin
@RequestMapping(value = "/company")
@RestController
public class DepartmentController {
```

画面 3:
```java
public void save(Department department) {
    String id = idworker.nextId();
    department.setId(id);
    departmentDao.save(department);
}

public void update(Department department) {
    Department dept = departmentDao.findById(department.getId()).get();
    dept.setCompanyId(department.getCompanyId());
    dept.setDepartmentName(department.getDepartmentName());
    dept.setManager(department.getManager());
    dept.setDepartmentCode(department.getDepartmentCode());
    dept.setDepartmentIntroduce(department.getDepartmentIntroduce());
    dept.setDepartmentManager(department.getDepartmentManager());
    departmentDao.save(dept);
}
```

画面 4:
```java
public Department findById(String id) {
    return departmentDao.findById(id).get();
}

public List<Department> findAll(String companyId) {
    Specification<Department> spec = new Specification<Department>() {
        @Override
        public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
            return null;
        }
    };
    return departmentDao.findAll();
}
```

画面 5:
```java
public Predicate toPredicate(Root<Department> root, CriteriaQuery<?> criteriaQuery, CriteriaBuilder criteriaBuilder) {
    return criteriaBuilder.equal(root.get("companyId").as(String.class), companyId);
}
```

画面 7:
```json
{
  "code": 0,
  "success": true,
  "message": "string",
  "data": {
    "companyId": "string",
    "companyName": "string",
    "companyManage": "string",
    "depts": [
      {
        "id": "string",
        "parentId": "string",
        "name": "string",
        "code": "string",
        "introduce": "string",
        "manager": "string"
      }
    ]
  }
}
```

画面 8:
```java
package com.ihrm.domain.company.response;

private
```

画面 9:
```java
package com.ihrm.domain.company.response;
import lombok.Getter;
import lombok.Setter;
import java.util.List;

@Getter
@Setter
public class DeptListResult {
```

画面 10:
```java
import com.ihrm.domain.company.Company;
import com.ihrm.domain.company.Department;
import lombok.Getter;
import lombok.Setter;
import java.util.List;

@Getter
@Setter
public class DeptListResult {
    private String companyId;
    private String companyName;
    private String companyManage;
    private List<Department> depts;
```

画面 11:
```java
import com.ihrm.domain.company.Company;
import com.ihrm.domain.company.Department;
import lombok.Getter;
import lombok.Setter;
import java.util.List;

@Getter
@Setter
public class DeptListResult {
    private String companyId;
    private String companyName;
    private String companyManage;
    private List<Department> depts;

    public DeptListResult() {
        this.companyId = companyId;
        this.companyName = companyName;
        this.companyManage = companyManage;
        this.depts = depts;
    }
}
```

画面 12:
```java
@RequestMapping(value = "/department", method = RequestMethod.GET)
public Result findAll() {
    String companyId = "1";
    Company company = companyService.findById(companyId);
    List<Department> list = departmentService.findAll(companyId);
    DeptListResult deptlistResult = new DeptListResult(company, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

画面 14:
```java
@RequestMapping(value = "/department", method = RequestMethod.GET)
public Result findAll() {
    String companyId = "1";
    Company company = companyService.findById(companyId);
    List<Department> list = departmentService.findAll(companyId);
    DeptListResult deptlistResult = new DeptListResult(company, list);
    return new Result(ResultCode.SUCCESS, deptlistResult);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
