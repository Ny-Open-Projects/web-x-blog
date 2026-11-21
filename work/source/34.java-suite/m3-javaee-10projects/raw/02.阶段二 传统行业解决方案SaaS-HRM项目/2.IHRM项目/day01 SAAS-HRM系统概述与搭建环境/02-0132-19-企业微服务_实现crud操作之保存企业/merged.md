# 19-企业微服务：实现crud操作之保存企业

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\19-企业微服务：实现crud操作之保存企业_【海量资源尽在 ubkz.com】.mp4
- 时长 8分48秒（音频 529s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 到目前呢我们实体类do Service都已经写好了那接下来我们就开始写控制器那在这边呢右键创建一个class放到cuntrolia Controller这个包下我叫做companym-p-a-n-y controllerOK好了那在这个Controller当中呢首先
[00:33] 它是一个我们控制器的这么一个类那我需要在这个控制器类上给它注入或者标注一下写一注解ata reset Controller好了那接下来在Controller当中我们一般调用的是Service所以先把基本的结构给它写出来ata auto where private借助company Service完成操作company Service
[01:05] 好了那接下来我们要完成的是基本CIOG的操作那这些操作我们这回不能瞎写我们完成的其实第一个呢就是叫做保存企业好了第二个根据ID更新企业好了接着第三个根据ID删除企业好了以及第四个根据ID查询企业和第五个
[01:35] 查询叫做全部企业列表这是我们接下来要完成的这么五件事情那这五件事情我们这个时候不能随便写因为这个时候真正涉及到前端要跟后端进行交互那前端和后端进行交互的时候你这个参数叫什么你返回值叫什么这个就不是我们随便定义的而是根据API文档那我们可以一起打开API文档一起来看
[02:04] 首先第一个增加那增加的时候这边说的很清楚你需要以pose的形式提交到一个-company这么一个请求地址上好了那接下来呢第二个列表同样的也是company这个地址上只不过这一回变成了get方式提交以及第三个根据ID那根据ID查还是get那只不过中间加的是我们reset-的编程风格
[02:32] 后面这玩意儿是不是代表的是一个地址参数指的是它要把公司ID传给你OK第四个put提交提交到我们company后面传递参数地址参数reset复风格会把ID传给你第五个删除地址参数OK那这些我们都简单的看过了之后看过了之后那接下来我们先把基本的工程结构大家好了
[03:02] 那接下来呢就是这个请求地址给他一个一个的都匹配过来即可好了那这些地址我们匹配过来之后接着一个一个方法攻克他就搞定了那接下来我们首先干第一件事就是把地址给他搞定首先我请求地址各位会发现请求地址很有规律啊附路径companycompanycompanycompanycompany后面ididid那我们可以是不是在这个代码当中进行一个
[03:29] 抽取比如说我可以给他指定你请求的最外层路径好了来一个ata request卖品好了里面可以指定value等于-注意company好了那接下来保存企业我们可以写一个方法public will id比如说就叫sealok好了当然了你可以抛出一个异常当然这异常我也就省略了那保存企业的时候那我们同样的
[04:02] at request叫做myping那这回请求的子路径呢打开API简单的来过一下没有没有好办那就是空好了那接下来接下来那保存期我们看过了之后那它保存的时候会不会传递一些参数呢那这个是我们重点关注的那参数究竟是什么样子还是来看API打开它
[04:32] 来参数有很多ID name等等等等等等好了这边呢你的请求方式是post抱歉这post刚才没注意忘记了好了我们这边就给它配置上你请求的方式request错了method等于好吗post好了那这样一来请求的链接和请求方式我们定义好了接着参数参数回到APA你会发现它传递的是一个
[05:01] 我们叫做企业实体类,其中有ID,NAME等等等等,那如果各位细心观察的话,你会发现他请求的这些参数,其实和我company实体类是一模一样的,是一模一样的,这是第一个点,第二个点,你请求过来的时候,前端往后端发送数据,前后端分离,他必然是以阿贾克斯或者以杰森串的形式给我请求,
[05:33] 所以这边我们参数如何进行处理就很简单了找到我们的Controller我们可以将你把自动的将你前端传递的json搜创转化成对象但是有前提了解你传递的这个对象的你传递的这个参数的属性名要跟我对象属性名要对应上我们就可以使用ata request把你请求的参数
[06:03] 封装成对象封装成我们的company好了那是请求参数我们搞定了我们还应该给它响应那我们再来观察API看响应响应有code有flag有message那针对这些怎么做注意响应体现造返回值当中那我们现在world就需要改那我们之前做过把所有的数据封装到了一个result当中
[06:30] 所以返回值result当然了我们前面也可以配合上at response包带自动的把你的对象转化成字符串响应给我们的前端当然了这个response其实你也可以把它删掉可以把它删掉为什么可以把它删掉是因为reset Controller一个注解能抵很多的内容抱歉拿错了
[06:55] 点进去来看一个注解里面能够包含很多的内容其实它已经包含了response包含了at Controller所以一个注解底所有那这样一来可以省略掉OK那这些基本的概念性的内容和我们的前端请求如何封装成对象响应数据如何封装成对象这些我们都做过介绍了那我们接下来就可以把这个代码给它补充完整好了那对于保存企业来说
[07:25] 很简单你传递的参数封装到company我们可以调用company Service打点我们封装那个方法addcompany好了这个就是我们的业务操作那剩下来之后呢就可以封装对象那封装对象直接returnnew一个以sult result但是new result的不行啊new result不行啊因为我这result里面它有这些基本的属性success code和message都要给它附上值
[07:57] 并且我data属性是空没有我只要告诉他三个属性就可以了因为API里面有规定所以我这个代码写法就比较简单了我这个result里面封装了一个布导码这构造方法你可以把你的code给我传过来没举那这个没举第一个success是不是代表成功所以我这边resultcode.success把这些信息传过来就能构造这些内容
[08:28] 好了那接下来呢我们这边就可以resultcode打点successok你传递过来这个code它自动的被里面的successcode和message进行复制嘛你code有什么我拿什么即可ok那这样一来我保存起就已经搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写公司信息的 RESTful API 控制器，包括添加、查询、更新和删除功能，并展示如何使用 Result 类封装统一返回结果。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 项目结构：展示 `ihrm_parent` 项目下的 `ihrm_company` 模块，当前选中 `src/main/java/com/ihrm/company/Service/CompanyService.java`。
- 代码内容：`CompanyService` 类中定义了 `deleteById`、`findById` 和 `findAll` 方法，分别用于删除、根据 ID 查询和查询所有公司。

画面 2：
- 项目结构：选中 `src/main/java/com/ihrm/company/Controller/CompanyController.java`。
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
package com.ihrm.company.Controller;
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

