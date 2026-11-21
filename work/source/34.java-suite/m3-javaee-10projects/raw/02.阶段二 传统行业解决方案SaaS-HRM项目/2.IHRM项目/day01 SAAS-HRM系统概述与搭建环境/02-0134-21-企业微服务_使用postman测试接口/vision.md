# 画面线理解：21-企业微服务：使用postman测试接口

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\21-企业微服务：使用postman测试接口_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:12, 00:24, 00:48, 01:02, 01:29, 01:45, 02:20, 02:55, 03:10, 03:40, 04:20, 04:44, 05:00, 05:27
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 13:02:18

1) 这一组画面整体在讲什么（一句话）：
演示一个基于 Spring Boot 的 HRM 企业信息管理 API 项目的开发与测试流程，包括代码编写、项目启动、接口调试和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- IDE 界面显示项目结构，当前打开的是 `CompanyApplication.java`。
- 代码内容：
```java
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication(scanBasePackages = "com.ihrm.company")
@EntityScan(value="com.ihrm.domain")
public class CompanyApplication {

    //启动方法
    public static void main(String[] args) {
        SpringApplication.run(CompanyApplication.class, args);
    }

    @Bean
    public IdWorker idWorker() {
        return new IdWorker();
    }
}
```

画面 2：
- 控制台输出 Spring Boot 启动日志，显示 Hibernate 初始化成功。
- 日志内容：
```
2018-11-22 14:35:27.261 INFO 18232 --- [main] j.LocalContainerEntityManagerFactoryBean : Building JPA container EntityManagerFactory
2018-11-22 14:35:27.380 INFO 18232 --- [main] org.hibernate.Version : HHH000412: Hibernate Core [5.2.17.Final]
2018-11-22 14:35:27.528 INFO 18232 --- [main] org.hibernate.cfg.Environment : HHH000406: Using dialect: org.hibernate.dialect.MySQL5InnoDBDialect
2018-11-22 14:35:28.999 INFO 18232 --- [main] j.LocalContainerEntityManagerFactoryBean : Initialized JPA EntityManagerFactory for persistence unit 'default'
```

画面 3：
- IDE 界面显示 `CompanyController.java` 的 `update` 方法。
- 控制台输出 Spring Boot 启动日志，显示应用已启动。
- 日志内容：
```
Spring Boot :: (v2.0.5 RELEASE)
2018-11-22 14:35:53.112 INFO 5732 --- [main] com.ihrm.company.CompanyApplication : Starting CompanyApplication on lemon-pc with PID 5732 (D:\workspace\src\main\java\com\ihrm\company\CompanyApplication.java)
2018-11-22 14:35:53.231 INFO 5732 --- [main] ConfigServletWebServerApplicationContext : Refreshing org.springframework.boot.web.servlet.context.AnnotationConfigServletWebServerApplicationContext
```

画面 4：
- IDE 界面显示 Spring Boot 启动后的 URL 映射信息。
- 控制台输出：
```
Mapping:
Mapped URL path "/**favicon.ico" onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
Mapped URL path "/company" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/error" onto handler of type [class org.springframework.http.ResponseEntity]
```

画面 5：
- 浏览器地址栏输入 `localhost:9001`，页面显示 Google 搜索首页。
- 浏览器标签页标题为“SaaS-HRM系统API文档”。

画面 6：
- 浏览器地址栏输入 `localhost:9001`，页面显示 Google 搜索首页。
- 浏览器标签页标题为“SaaS-HRM系统API文档”。

画面 7：
- 文档编辑器显示 `CompanyController.java` 的 `delete`、`findById` 和 `findAll` 方法。
- 代码内容：
```java
@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(name = "id") String id) throws Exception {
    companyService.deleteById(id);
    return Result.SUCCESS();
}

/**
 * 根据ID获取公司信息
 */
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(name = "id") String id) throws Exception {
    Company company = companyService.findById(id);
    return new Result(ResultCode.SUCCESS);
}

/**
 * 获取企业列表
 */
@RequestMapping(value = "", method = RequestMethod.GET)
public Result findAll() throws Exception {
    return new Result(ResultCode.SUCCESS);
}
```

画面 8：
- Windows 文件资源管理器界面，路径为 `ihrm > day1 > 软件`。
- 界面显示两个文件：`013 应用程序` 和 `006 360压缩 RAR 文件`。

画面 9：
- Postman 工具界面，准备发送一个 POST 请求到 `http://localhost:9001/company`。
- 请求头设置为 `Inherit auth from parent`。
- 请求体为空。

画面 10：
- IDE 界面显示 `application.yml` 配置文件。
- 控制台输出 Spring Boot 启动后的 URL 映射信息。
- 控制台输出：
```
Mapping:
Mapped URL path "/**favicon.ico" onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
Mapped URL path "/company" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/error" onto handler of type [class org.springframework.http.ResponseEntity]
```

画面 11：
- Postman 工具界面，准备发送一个 POST 请求到 `http://localhost:9001/company`。
- 请求体为 JSON 格式，内容为：
```json
{
  "name": "江苏云智科技有限公司",
  "managerId": "12",
  "version": "12",
  "expirationDate": "2020-01-01",
  "companyArea": "江苏",
  "businessLicense": "123456789012345678",
  "balance": "10000",
  "createTime": "2018-11-22"
}
```

画面 12：
- SQL 数据库管理工具界面，显示 `company` 表的数据。
- 表格内容：
```
id | manager_id | version | renewal_date | expiration_date | company_area | company_name | remark
123456789012345678 | 12 | 12 | 2020-01-01 | 2020-01-01 | 江苏 | 江苏云智科技有限公司 | 无
```

画面 13：
- IDE 界面显示 `CompanyController.java` 的 `findById` 方法。
- 控制台输出 Spring Boot 启动后的 URL 映射信息。
- 控制台输出：
```
Mapping:
Mapped URL path "/**favicon.ico" onto handler of type [class org.springframework.web.servlet.resource.ResourceHttpRequestHandler]
Mapped URL path "/company" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.controller.CompanyController]
Mapped URL path "/error" onto handler of type [class org.springframework.http.ResponseEntity]
```

画面 14：
- Postman 工具界面，发送一个 GET 请求到 `http://localhost:9001/company/123456789012345678`。
- 响应体为 JSON 格式，内容为：
```json
{
  "success": true,
  "code": 20000,
  "message": "操作成功",
  "data": {
    "id": "123456789012345678",
    "name": "江苏云智科技有限公司",
    "managerId": "12",
    "version": "12",
    "expirationDate": "2020-01-01",
    "companyArea": "江苏",
    "businessLicense": "123456789012345678",
    "balance": "10000",
    "createTime": "2018-11-22"
  }
}
```
