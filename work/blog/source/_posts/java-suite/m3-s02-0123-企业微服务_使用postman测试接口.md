---
title: "接口写完不等于能用：用 Postman 把企业微服务的五个接口测一遍"
date: 2026-11-18
categories: [Java后端进阶全套, M3 十大中级项目, 阶段二 传统行业解决方案SaaS-HRM项目]
tags: [Java, 项目实战]
---

# 接口写完不等于能用：用 Postman 把企业微服务的五个接口测一遍

Controller 五个方法刚写完，代码能不能跑、参数接得对不对，全靠跑一遍才知道。麻烦在于浏览器地址栏只会发 GET，表单只会发 GET 和 POST，而接口清单里明明有 PUT 和 DELETE。这一环节就是把服务启动起来，按正确的顺序把五个接口都验证到，Postman 就是补上这个缺口的工具。

## 先给结论

- 启动方式只有一种：运行引导类的 `main` 方法，启动日志里 `Mapped URL path` 一段会列出每个接口的映射，是排障的第一现场。
- 微服务端口是 `9001`，来自 `application.yml` 的 `server.port`，不是 Web 工程习惯的 8080。
- 浏览器只能直接测 GET，带 JSON 请求体的 POST、以及 PUT 和 DELETE，交给 Postman（或等价的 curl 命令）。
- 测试顺序建议：GET 列表确认服务通、POST 保存、查库确认落库、用新 id GET 回读，写操作最后验证。
- 路径占位符必须写成 `{id}`，写成 `$id` 会让地址参数失效，服务启动即报错。

## 一、启动与自检：先看日志里的映射清单

企业微服务的引导类承担三件事：组件扫描、实体扫描、注册雪花 id 工具：

```java
@SpringBootApplication(scanBasePackages = "com.example.company")
@EntityScan(value = "com.example.domain")
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

第一次启动就报错了，原因在地址参数上：映射路径写成了 `$id`，而地址参数声明不能用美元符，占位符必须用花括号 `{id}` 包住。改完重启，控制台出现一段映射日志：

```text
Mapped URL path "/company" onto handler of type [class com.example.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.example.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.example.company.controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.example.company.controller.CompanyController]
```

`/company` 一条对应保存与列表（POST、GET 各一条），`/company/{id}` 三条对应更新、删除、按 id 查询。这段日志等价于框架替你做了一次路由自检：五个方法全部注册成功，请求方式与路径的组合没有冲突。看不到自己写的路径出现在这里，说明注解没生效，测也是白测。

端口来自配置文件：

```yaml
#服务配置
server:
  port: 9001
#spring配置
spring:
  #1.应用配置
  application:
    name: company-service #指定服务名
  #2.数据库连接池
  datasource:
    driver-class-name: com.mysql.jdbc.Driver
    url: jdbc:mysql://localhost:3306/company?useUnicode=true&characterEncoding=utf8
    username: root
    password: 111111
  #3.JPA
  jpa:
    database: MySQL
    show-sql: true
    open-in-view: true
```

## 二、浏览器能测的部分：GET 列表

服务起来之后，浏览器地址栏直接访问 `http://localhost:9001/company`，请求方式是 GET，命中查询列表接口，页面返回 JSON 数组，里面是数据库里现有的几条企业记录。这一步的意义是确认三件事同时成立：服务在 9001 端口活着、`/company` 路由匹配正确、数据库连接正常。列表接口天然适合打头阵，它是只读操作，失败了也不会弄脏数据。

浏览器的能耐到此为止。地址栏只发 GET，表单只发 GET 和 POST，PUT 和 DELETE 在浏览器里没有原生入口，而保存接口还需要构造 JSON 请求体，这已经超出地址栏的能力范围。

## 三、Postman：把剩下的动词补齐

Postman 是一款 HTTP 调试工具，可以模拟 GET、POST、PUT、DELETE 等各类请求，自定请求头与请求体，用请求地址加请求方式加请求体的组合把接口逐个打一遍。

测保存接口的完整动作是：请求方式选 POST，地址填 `http://localhost:9001/company`，在 Body 里选 raw 并把格式切到 JSON，填入企业数据：

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

点 Send，下方面板返回响应体：

```json
{
  "success": true,
  "code": 10000,
  "message": "操作成功",
  "data": null
}
```

响应与 `Result` 的结构完全一致，code 是 `ResultCode.SUCCESS` 约定的 10000。保存类接口的响应只是第一层证据，落没落库要看第二层：打开数据库客户端刷新 `company` 表，多出了刚才那条记录，才算测试闭环。

按 id 查询的测法是拿保存后的 id 回读。从库里复制新记录的主键，拼到地址末尾，请求方式改回 GET，访问 `http://localhost:9001/company/123456789012345678`，响应的 data 里就是这条企业的完整 JSON。更新与删除的测法相同：PUT 请求把改过的 JSON 发到 `/company/{id}`，DELETE 请求直接打到 `/company/{id}`，各自用回读和查库确认结果。

整个流程的推荐顺序如下：

```mermaid
flowchart LR
    A["GET /company 查列表"] --> B{"服务与路由是否正常"}
    B -->|正常| C["POST /company 保存 JSON"]
    C --> D["查库确认新增记录"]
    D --> E["GET /company/{id} 回读"]
    E --> F["PUT /company/{id} 更新"]
    F --> G["GET 回读确认字段变更"]
    G --> H["DELETE /company/{id} 删除"]
    H --> I["GET 回读确认已删除"]
    B -->|异常| J["回看启动日志与端口配置"]
```

顺序的原则是先用只读接口探路，再做写操作，每一步写操作之后都用读操作验证，任何一步不符合预期都能立刻定位是请求没发对，还是后端没接住。

## 四、命令行的等价测法：curl

Postman 之外，curl 能完成完全相同的验证，便于写进脚本或在没有图形界面的服务器上用：

```bash
# 查询企业列表
curl http://localhost:9001/company

# 保存企业，JSON 请求体必须显式声明 Content-Type
curl -X POST http://localhost:9001/company \
  -H "Content-Type: application/json" \
  -d '{"name":"江苏云智科技有限公司","managerId":"12","version":"12"}'

# 按 id 查询
curl http://localhost:9001/company/123456789012345678

# 按 id 更新
curl -X PUT http://localhost:9001/company/123456789012345678 \
  -H "Content-Type: application/json" \
  -d '{"name":"江苏云智科技有限公司（改）"}'

# 按 id 删除
curl -X DELETE http://localhost:9001/company/123456789012345678
```

`-X` 指定请求方式，`-H` 声明请求头，`-d` 放请求体。POST 保存那条里的 `Content-Type: application/json` 不能省，它对应 Postman 里把 Body 格式切到 JSON 的那个动作，缺了它 `@RequestBody` 解析不到内容。

## 常见误区

- **占位符写成 `$id`**：`@RequestMapping(value = "/$id")` 里没有花括号模板，`@PathVariable` 取不到值，启动即抛异常或访问报错。地址参数一律写 `{id}`。
- **Postman 忘了切 Body 格式**：默认的 form-data 或 x-www-form-urlencoded 发过去，后端 `@RequestBody` 解析失败，实体对象字段全空。Body 选 raw，格式选 JSON。
- **端口习惯性写 8080**：这个微服务的端口在 `application.yml` 里定义成 9001，测之前先看配置，而不是凭 Web 工程的老习惯猜。
- **只看响应就认为保存成功**：响应成功只代表 Controller 正常返回，是否落库要查表确认，日期、数字这类字段在反序列化时最容易悄悄出错。

## 面试可能被问到的问题

1. 面试官追问：「写完一个接口后，你的测试顺序是什么？」
   答：先启动服务确认无报错，看日志里的 URL 映射是否齐全；再用只读接口（列表或按 id 查询）验证服务、路由、数据库三链路；然后测写操作，每完成一次保存或更新，查库或回读确认数据真正落地，最后测删除并验证结果。

2. 面试官追问：「Postman 发 JSON 请求需要设置什么，后端靠什么解析？」
   答：Body 选 raw 并把格式切到 JSON，等价于设置请求头 `Content-Type: application/json`。后端 `@RequestBody` 依据这个头选择 Jackson 消息转换器，把请求体反序列化成实体对象。

3. 面试官追问：「浏览器地址栏为什么测不了 PUT 和 DELETE？」
   答：地址栏只会发起 GET，HTML 表单只支持 GET 和 POST，这是浏览器端的限制。Ajax 请求或 Postman、curl 这类工具不受此限，可以直接发 PUT、DELETE。

4. 面试官追问：「启动日志里的 Mapped URL path 有什么用？」
   答：它是 Spring MVC 注册处理器方法的记录，能看出每个路径被哪个 Controller 接管、同一路径注册了几次。接口访问 404 或路径冲突时，先来这里核对映射是否如预期，能快速缩小排查范围。

5. 面试官追问：「访问接口返回 404 和 405 分别是什么问题？」
   答：404 是路径没匹配到任何处理器，常见于路径写错、类级前缀漏拼或组件没被扫描到；405 是路径存在但请求方式不匹配，比如对只声明了 GET 的路径发了 POST，说明路由对了、动词错了。

## 配套资料

- 服务配置（端口、数据源、JPA）：`materials/code/02/day13-代码生成器实现/day13-代码生成器实现/资源/测试/生成代码路径/ihrm_company/src/main/resources/application.yml`
- 被测接口的成例：`materials/code/02/day13-代码生成器实现/day13-代码生成器实现/资源/测试/生成代码路径/ihrm_company/src/main/java/com/ihrm/system/controller/CompanyController.java`（包名已改写为 `com.example`）
- 同类启动类成例：`materials/code/02/day07 员工管理及POI入门/员工管理及POI入门/资源/后端/ihrm_employee/src/main/java/com/ihrm/employee/EmployeeApplication.java`；企业微服务启动类不在资料包中，文中代码按画面与本课写法补全
