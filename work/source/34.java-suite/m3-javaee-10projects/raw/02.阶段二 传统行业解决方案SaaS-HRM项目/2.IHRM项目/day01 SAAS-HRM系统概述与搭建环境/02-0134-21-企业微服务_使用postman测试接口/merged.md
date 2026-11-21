# 21-企业微服务：使用postman测试接口

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\21-企业微服务：使用postman测试接口_【海量资源尽在 ubkz.com】.mp4
- 时长 5分34秒（音频 334s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 基本的代码我们写好了那接下来呢我们就可以启动当前并且运行来看一下效果那Spring Boot程序启动起来很简单找到我们刚才的启动类执行问方法即可好这边程序在启动啊可能有点点慢各位耐心等待一下哎他报了一个错误当然了不报错误也不可能啊消了这么长时间好了各位来看看这边有一个错误什么道啊抱歉
[00:34] 在我们去编写空气类的时候呢这边地址参数声明的时候不能用dollar抱歉鸽子刚才有点粗心了不能用dollarOK那我们再重启一下看一下效果这个启动相对来说有一点点慢各位耐心懂得好了现在已经启动起来了并且没有报错那通过日志我们可以看到当前我们这个工程请求的地址companycompanycompany请求方式等等都已经罗列出来了那罗列出来了之后呢我们可以
[01:09] 拿一个做一个测试比如说Gang Company Get方式那Gang Company Get方式我们刚才写过是不是代表查询全部列表啊那我们可以打开浏览器开始敲地址LocalhostLocalhost那我们现在请求的端口是多少呢我们刚才创建微服的过程当中有一个配置文件各位应该还记着在配置文件里面指定了part是9001
[01:40] 所以我这边90 01OK点击回车不对点击回车好了那这个端口叫company点击回车走那各位来看现在没什么问题数据也已经有了那数据已经有了那我想跟各位说的是那我还有更新还有保存那这些我们应该如何去测试呢因为我们浏览器发送请求很简单啊
[02:10] 它发送的就是一个get请求或者post请求但是我们要测试put测试delete等等那针对这些内容那我们怎么测试呢这边和各位来介绍一个测试工具那这个测试工具呢在底下叫做postman这个测试工具呢是一个比较强大的web应用的一个测试工具啊当然使用起来比较简单它可以模拟去发送getpostdeleteput等等这些请求
[02:39] 那我在这边今天的资料当中已经把这个工具啊给各位准备好啊资料里面有一个软件Postman那对于各位来说直接双击安装去运行即可那运行我这边打开我自己已经解压安装好的Postman好了这个有一个初始化的过程好了那接下来呢我在这边咱们就可以完成一个测试我请求的端口刚才拷过来了抱歉
[03:16] 请求的端口9001company那我请求方式这边可以选post我用的是get请求那get请求代表所有走你发现数据都已经有了那接下来除了get请求之外呢我们还可以发送post请求那post请求回到我们的代码我们来回想一下post请求发送过来company是不是保存一个企业呀
[03:46] 那保存企业我们就开始数点数据一起来做一下那数据写到哪呢写到body部分注意写到body部分那我这边传递的是一个json形式的字符串那这边我们用大括号来描述比如说呢我传递的参数有很多有很多比如说我只写一name好了这个name比如说我就叫江苏传至波克教育股份
[04:22] 有限公司好了那接下来呢接下来打开数据库来看一下目前数据库只有三条记录走send底下有响应往上拖它告诉我操作成功一万处我们的约定那接着看一下数据库有没有保存进去刷新你会发现多了这么一条记录OK那这样一来保存我们就也测试成功了
[04:51] 那其实除了保存之外呢我们还有一些操作这些操作比如说还有根据ID查询那根据ID查询我们只需要后面挂上一个ID地址参数即可比如说我想查询一下我刚刚保存的这个江苏传说博客Ctrl C复制一下ID配置到我的Postman地址部分后边地址参数那接下来我这回的请求方式就是Get走
[05:21] 你发现也能查询出来那当然了除了这个之外呢还有delete删除或者put等等等等这些内容它都有我这边就不再一一测试了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
Mapped URL path "/company" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
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
Mapped URL path "/company" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
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
Mapped URL path "/company" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
Mapped URL path "/company/{id}" onto handler of type [class com.ihrm.company.Controller.CompanyController]
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

