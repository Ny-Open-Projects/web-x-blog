# 画面线理解：19-企业微服务：实现crud操作之保存企业

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\19-企业微服务：实现crud操作之保存企业_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:04, 00:56, 02:16, 03:40, 04:04, 04:17, 04:53, 05:17, 05:40, 06:12, 06:35, 07:30, 08:07, 08:44
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:01:00

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写公司信息的 RESTful API 控制器，包括添加、查询、更新和删除功能，并展示如何使用 Result 类封装统一返回结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：展示 `ihrm_parent` 项目下的 `ihrm_company` 模块，当前选中 `src/main/java/com/ihrm/company/service/CompanyService.java`。
- 代码内容：`CompanyService` 类中定义了 `deleteById`、`findById` 和 `findAll` 方法，分别用于删除、根据 ID 查询和查询所有公司。

画面 2：
- 项目结构：选中 `src/main/java/com/ihrm/company/controller/CompanyController.java`。
- 代码内容：`CompanyController` 类的开头，包含 `@RestController` 注解和 `@Autowired` 注解，准备编写控制器方法。

画面 3：
- 界面内容：显示了 API 文档页面，包含公司信息的 CRUD 操作接口：
  - POST `/company`：增加公司
  - GET `/company`：查询公司列表
  - GET `/company/{companyId}`：根据 ID 查询公司
  - PUT `/company/{companyId}`：修改公司
  - DELETE `/company/{companyId}`：删除公司

画面 4：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 5：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 6：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 7：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 8：
- 项目结构：选中 `ihrm_common_model` 模块下的 `Company.java`。
- 代码内容：展示 `Company` 实体类的字段，包括 `id`、`name`、`companyPhone`、`companyAddress` 等。

画面 9：
- 项目结构：选中 `Company.java`。
- 代码内容：展示 `Company` 实体类的字段，包括 `id`、`name`、`companyPhone`、`companyAddress` 等。

画面 10：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 11：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 12：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：在 `@RestController` 注解后，光标位于 `public class CompanyController {` 行，准备编写方法。

画面 13：
- 项目结构：选中 `Result.java`。
- 代码内容：`Result` 类的定义，包含 `success`、`code`、`message` 和 `data` 字段，以及多个构造方法。

画面 14：
- 项目结构：选中 `CompanyController.java`。
- 代码内容：`save` 方法中调用 `companyService.add(company)` 并返回 `new Result(ResultCode.SUCCESS)`。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
/**
 * 删除企业
 */
public void deleteById(String id) {
    companyDao.deleteById(id);
}

/**
 * 根据id查询企业
 */
public Company findById(String id) {
    return companyDao.findById(id).get();
}

/**
 * 查询企业列表
 */
public List<Company> findAll() {
    return companyDao.findAll();
}
```

画面 2：
```java
package com.ihrm.company.controller;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CompanyController {

@Autowired
}
```

画面 3：
无代码，为 API 文档页面。

画面 4：
无代码，为 IDE 编辑器界面。

画面 5：
无代码，为 IDE 编辑器界面。

画面 6：
无代码，为 IDE 编辑器界面。

画面 7：
无代码，为 IDE 编辑器界面。

画面 8：
```java
package com.ihrm.common.model;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class CompanyController {

@Autowired
private CompanyService companyService;

//保存企业
@RequestMapping(value="",method = RequestMethod.POST)
public void save() {

}
```

画面 9：
无代码，为 IDE 编辑器界面。

画面 10：
无代码，为 IDE 编辑器界面。

画面 11：
无代码，为 IDE 编辑器界面。

画面 12：
无代码，为 IDE 编辑器界面。

画面 13：
```java
@Data
@NoArgsConstructor
public class Result {
    private boolean success;//是否成功
    private Integer code;//返回码
    private String message;//返回信息
    private Object data;//返回数据

    public Result(ResultCode code) {
        this.success = code.success;
        this.code = code.code;
        this.message = code.message;
    }

    public Result(ResultCode code, Object data) {
        this.success = code.success;
        this.code = code.code;
        this.message = code.message;
        this.data = data;
    }

    public Result(Integer code, String message, boolean success) {
        this.code = code;
        this.message = message;
        this.success = success;
    }
}
```

画面 14：
```java
public Result save(@RequestBody Company company) {
    companyService.add(company);
    return new Result(ResultCode.SUCCESS);
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
