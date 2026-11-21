# 18-模板制作：视图层模板

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day13-代码生成器实现
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day13-代码生成器实现\18-模板制作：视图层模板_【海量资源尽在 ubkz.com】.mp4
- 时长 4分42秒（音频 282s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 那我们现在实现了实体类do和Service这个编写那除了这些之外还有一个就是我们的web层Controller那在web层Controller这边跟之前的逻辑其实都差不多首先第一个package那package这边的代码呢我从之前的逻辑这边拷一份过来首先第一个class name也就是我们的类名要进行处理这个都是我们成员约定俗成的一些比如说呢
[00:28] Controller某某Controller咱们就用类名来进行编写OK好了接下来找到里面的类名进行统一替换那好了第一步我们搞定了那接下来在这里面呢也要用到小写的名称的一部分内容所以这边把小写名称也准备好这个应该也能理解那剩下的事情替换包那我们这边是不是就是一个Ppackage的这么一个选项Ctrl C拿过来Ctrl V
[00:57] OK什么resultresultcode还有公共的exception这些都在common包下我们就不管了我们就不管了剩下这些什么company它的Service好了什么我们的实体类那实体类我们之前也做过一个配置Ctrl C拿过来实体类经替换那现在我们关注的是Service层Service层首先包名没问题好了接着用哪个Service是不是类名咱们也要做一个替换
[01:29] OK那好了这样一来我们上边定义包以及引入内容咱们就已经替换了那替换了之后接下来咱们继续往下看解决跨域没什么说的result Controller也没什么说公共的我们的附录镜company那这个company注意是不是就应该是我们这个小写的class name lower所以这边注意替换OK
[01:59] 好了那接下来里面的很多地方呢咱们都需要做一个统一替换的这么一个过程比如说大写的company咱们要替换Ctrl F错了Ctrl RCtrl R咱们要替换吧Ctrl R好了接着替换那对于大写的company我们替换成$className没错吧好了我们一起来试一下好了目前我这个匹配的是区分大小写的那这个没问题好了replace allOK搞定那接下来小写的className
[02:41] 好了替换成class name lowercontrary好了接着replace all那好了这样一来我们就来了一个统一替换的这么一个过程OK保存企业没什么问题当然了这边不能叫保存企业了我们这边根据ID更新也搞定了好了接下来再来根据ID删除也没什么问题根据ID查询OK没问题好了根查询全部
[03:18] OK那这样一来我们这个Controller部分的内容咱们就已经都替换结束了好了那接下来呢回到我们的代码生成器在这边把所有之前生成的内容全都都删掉我们再来生成一把生成代码好啊各位这回来看Controller全部都有do全部都有pojo也没问题Service也没问题同时Controller对不我以一个举例咱们一起来看company
[03:52] company这边所有内容全部都已经替换了并且把代码生成出来了那除了这个Controller我们替换之外呢其实还有一点点细节问题呢也是需要我们考量的点比如说resourcesresources这边呢是不是应该有一个我们当前生成工程的这么一个sprintboot的一个配置文件好了所以接下来呢我们就把这个sprintboot的配置文件也做一个相应的修改application.yml
[04:22] 而这里面的修改呢其实就是跟我们之前的逻辑都是一模一样的当然这边有HM Company等等等等那这个替换的过程呢其实各位应该都已经会了那这个替换过程就留给各位有兴趣的话自己去完成就可以了我在这边就不再浪费各位时间了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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
画面9：弹出“代码生成器 1.0”窗口，模板选择“Spring Boot项目模板”，项目名“company”，包名“com.ihm.system”，作者“ihm”，数据库用户名“root”，密码“111111”。
画面10：展示文件资源管理器，路径为“ihm_company/src/main/java/com/ihm/system”，包含 Controller、dao、pojo、Service 文件夹和 CompanyApplication.java。
画面11：展示 Controller 文件夹下的多个 Controller 类文件，如 CityController.java、CompanyController.java 等。
画面12：展示 Controller 文件夹下的多个 Controller 类文件，如 CityController.java、CompanyController.java 等。
画面13：展示 application.yml 文件，内容包含 server、spring、application、datasource、jpa 配置。
画面14：展示 application.yml 文件，内容包含 server、spring、application、datasource、jpa 配置。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.ihm.company.Controller;
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
package ${pPackage}.Service;
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
模板: Spring Boot项目模板
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

