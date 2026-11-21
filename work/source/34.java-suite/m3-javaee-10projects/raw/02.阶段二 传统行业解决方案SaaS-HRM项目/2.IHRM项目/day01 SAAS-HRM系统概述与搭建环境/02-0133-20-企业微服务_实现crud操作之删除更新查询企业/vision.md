# 画面线理解：20-企业微服务：实现crud操作之删除更新查询企业

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\20-企业微服务：实现crud操作之删除更新查询企业_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:45, 01:29, 02:15, 02:47, 03:18, 03:56, 04:27, 05:08, 05:28, 06:06, 06:33, 07:01, 07:48
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:01:28

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中为“企业”实体实现完整的 CRUD（增删改查）API 接口，并通过 API 文档展示其功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 CompanyController.java 中的 save 方法，用于保存新企业，调用 companyService.add(company)。
画面 2: 展示 API 文档中 POST /company 接口，用于添加企业。
画面 3: 展示 API 文档中 GET /company 接口，用于查询全部企业列表。
画面 4: 展示 API 文档中 PUT /company/{companyId} 接口，用于修改企业。
画面 5: 展示 CompanyController.java 中的 update 方法，用于根据 ID 更新企业，调用 companyService.update(company)。
画面 6: 展示 CompanyController.java 中的 delete 方法，用于根据 ID 删除企业，调用 companyService.deleteById(id)。
画面 7: 展示 CompanyController.java 中的 findById 方法，用于根据 ID 查询企业，调用 companyService.findById(id)。
画面 8: 展示 CompanyController.java 中的 findById 方法，调用 companyService.findById(id) 并设置返回结果。
画面 9: 展示 CompanyController.java 中的 findById 方法，调用 companyService.findById(id) 并设置返回结果。
画面 10: 展示 API 文档中 GET /company/{companyId} 接口，用于根据 ID 查询企业。
画面 11: 展示 CompanyController.java 中的 findById 方法，调用 companyService.findById(id) 并设置返回结果。
画面 12: 展示 API 文档中 GET /company/{companyId} 接口，用于根据 ID 查询企业。
画面 13: 展示 CompanyController.java 中的 findById 方法，调用 companyService.findById(id) 并设置返回结果。
画面 14: 展示 CompanyController.java 中的 findById 方法，调用 companyService.findById(id) 并设置返回结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
import org.springframework.web.bind.annotation.*;
@RestController
@RequestMapping(value = "/company")
public class CompanyController {
    @Autowired
    private CompanyService companyService;

    @PostMapping(value = "", method = RequestMethod.POST)
    public Result save(@RequestBody Company company) {
        //正常操作
        companyService.add(company);
        return new Result(ResultCode.SUCCESS);
    }
}
```

画面 5:
```java
//根据id更新企业
@RequestMapping(value = "/{id}", method = RequestMethod.PUT)
public Result update(@PathVariable(value = "id") String id, @RequestBody Company company) {
    //1.方法
    //2.请求参数
    //3.响应
    company.setId(id);
    companyService.update(company);
    return new Result(ResultCode.SUCCESS);
}
```

画面 6:
```java
//根据id删除企业
@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
    companyService.deleteById(id);
    return new Result(ResultCode.SUCCESS);
}
```

画面 7:
```java
//根据id查询企业
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    Company company = companyService.findById(id);
    Result result = new Result(ResultCode.SUCCESS);
    result.setData(company);
    return result;
}
```

画面 11:
```java
//根据id查询企业
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) {
    Company company = companyService.findById(id);
    Result result = new Result(ResultCode.SUCCESS);
    result.setData(company);
    return result;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
