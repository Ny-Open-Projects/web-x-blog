# 画面线理解：18-模板制作：视图层模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\18-模板制作：视图层模板_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:08, 00:15, 00:40, 01:04, 01:45, 02:31, 02:57, 03:11, 03:28, 03:41, 03:49, 03:58, 04:20, 04:40
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 17:08:46

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 项目模板快速生成 CRUD 接口代码，并展示生成的 Controller、Service 层代码结构及配置文件内容。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示项目结构，选中 CompanyController.java 文件。
画面2：展示 CompanyController.java 代码，包含 @RequestMapping("/company") 和 save 方法。
画面3：展示 $ClassNameService.java 代码，包含 @Service 注解和 add 方法。
画面4：展示 $ClassNameController.java 代码，包含 @RestController 注解和 save 方法。
画面5：展示 $ClassNameController.java 代码，包含 @RequestMapping("/company") 注解。
画面6：在代码中搜索 "company"，显示多个匹配项。
画面7：展示搜索结果，包含 deleteById、findById、findAll 方法。
画面8：展示搜索结果，包含 update、delete、findById、findAll 方法。
画面9：弹出“代码生成器 1.0”窗口，模板选择“springboot项目模板”，项目名“company”，包名“com.ihm.system”，作者“ihm”，数据库用户名“root”，密码“111111”。
画面10：展示文件资源管理器，路径为“ihm_company/src/main/java/com/ihm/system”，包含 controller、dao、pojo、service 文件夹和 CompanyApplication.java。
画面11：展示 controller 文件夹下的多个 Controller 类文件，如 CityController.java、CompanyController.java 等。
画面12：展示 controller 文件夹下的多个 Controller 类文件，如 CityController.java、CompanyController.java 等。
画面13：展示 application.yml 文件，内容包含 server、spring、application、datasource、jpa 配置。
画面14：展示 application.yml 文件，内容包含 server、spring、application、datasource、jpa 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.ihm.company.controller;
import com.ihm.common.entity.Result;
import com.ihm.common.exception.CommonException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
//解决跨域问题
@CrossOrigin
@RestController
@RequestMapping(value = "/company")
public class CompanyController {
@Autowired
private CompanyService companyService;
//保存企业
@RequestMapping(value = "", method = RequestMethod.POST)
public Result save(@RequestBody Company company) {
//业务操作
companyService.add(company);
return new Result(ResultCode.SUCCESS);
}
}
```

画面3：
```java
package ${pPackage}.service;
import com.ihm.common.utils.IdWorker;
import ${pPackage}.dao.${ClassName}Dao;
import ${pPackage}.pojo.${ClassName};
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;
@Service
public class ${ClassName}Service {
@Autowired
private ${ClassName}Dao ${className}Dao;
@Autowired
private IdWorker idWorker;
//保存
public void add(${ClassName} ${classNameLower}) {
//基于自增的id
String id = idWorker.nextId()+"";
${classNameLower}.setId(id);
${classNameLower}Dao.save(${classNameLower});
}
}
```

画面4：
```java
import com.ihm.common.entity.Result;
import com.ihm.common.exception.CommonException;
import com.ihm.domain.company.Company;
import com.ihm.domain.company.CompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
//解决跨域问题
@CrossOrigin
@RestController
@RequestMapping(value = "/company")
public class ${ClassName}Controller {
@Autowired
private CompanyService companyService;
//保存企业
@RequestMapping(value = "", method = RequestMethod.POST)
public Result save(@RequestBody Company company) {
//业务操作
companyService.add(company);
return new Result(ResultCode.SUCCESS);
}
}
```

画面5：
```java
import com.ihm.common.entity.Result;
import com.ihm.common.exception.CommonException;
import com.ihm.domain.company.Company;
import com.ihm.domain.company.CompanyService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.List;
//解决跨域问题
@CrossOrigin
@RestController
@RequestMapping(value = "/company")
public class ${ClassName}Controller {
@Autowired
private CompanyService companyService;
//保存企业
@RequestMapping(value = "", method = RequestMethod.POST)
public Result save(@RequestBody Company company) {
//业务操作
companyService.add(company);
return new Result(ResultCode.SUCCESS);
}
}
```

画面6：
```java
//根据id删除企业
@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
companyService.deleteById(id);
return new Result(ResultCode.SUCCESS);
}
//根据id查询企业
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) throws CommonException {
Company company = companyService.findById(id);
return new Result(ResultCode.SUCCESS, company);
}
//查询全部企业列表
@RequestMapping(value = "", method = RequestMethod.GET)
public Result findAll() {
List<Company> list = companyService.findAll();
Result result = new Result(ResultCode.SUCCESS);
result.setData(list);
return result;
}
```

画面7：
```java
//根据id删除企业
@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
companyService.deleteById(id);
return new Result(ResultCode.SUCCESS);
}
//根据id查询企业
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) throws CommonException {
Company company = companyService.findById(id);
return new Result(ResultCode.SUCCESS, company);
}
//查询全部企业列表
@RequestMapping(value = "", method = RequestMethod.GET)
public Result findAll() {
List<Company> list = companyService.findAll();
Result result = new Result(ResultCode.SUCCESS);
result.setData(list);
return result;
}
```

画面8：
```java
//根据id删除企业
@RequestMapping(value = "/{id}", method = RequestMethod.DELETE)
public Result delete(@PathVariable(value = "id") String id) {
${classNameLower}Service.deleteById(id);
return new Result(ResultCode.SUCCESS);
}
//根据id查询企业
@RequestMapping(value = "/{id}", method = RequestMethod.GET)
public Result findById(@PathVariable(value = "id") String id) throws CommonException {
${ClassName} ${classNameLower} = ${classNameLower}Service.findById(id);
return new Result(ResultCode.SUCCESS, ${classNameLower});
}
//查询全部企业列表
@RequestMapping(value = "", method = RequestMethod.GET)
public Result findAll() {
List<${ClassName}> list = ${classNameLower}Service.findAll();
Result result = new Result(ResultCode.SUCCESS);
result.setData(list);
return result;
}
```

画面9：
```yaml
模板: springboot项目模板
代码生成路径: /ihm_company/src/main/java/com/ihm/system
项目名（英文）: company
包名: com.ihm.system
项目中文名称: 人力系统
作者: ihm
数据库: mysql
用户名: root
密码: 111111
```

画面10：
无代码或配置内容。

画面11：
无代码或配置内容。

画面12：
无代码或配置内容。

画面13：
```yaml
#服务配置
server:
port: 9001
#spring配置
spring:
application:
name: ihm_company #指定服务名
#数据库连接配置
datasource:
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihm?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
#jpa
jpa:
database: MySQL
show-sql: true
open-in-view: true
```

画面14：
```yaml
#服务配置
server:
port: 9001
#spring配置
spring:
application:
name: ihm_company #指定服务名
#数据库连接配置
datasource:
driver-class-name: com.mysql.jdbc.Driver
url: jdbc:mysql://localhost:3306/ihm?useUnicode=true&characterEncoding=utf8
username: root
password: 111111
#jpa
jpa:
database: MySQL
show-sql: true
open-in-view: true
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无 PPT 标题、架构图/流程图或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。
