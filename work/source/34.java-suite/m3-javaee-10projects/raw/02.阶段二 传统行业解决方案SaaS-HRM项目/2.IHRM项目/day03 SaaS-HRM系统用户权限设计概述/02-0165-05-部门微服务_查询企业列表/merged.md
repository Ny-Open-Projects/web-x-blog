# 05-部门微服务：查询企业列表

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day03 SaaS-HRM系统用户权限设计概述
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day03 SaaS-HRM系统用户权限设计概述\05-部门微服务：查询企业列表_【海量资源尽在 ubkz.com】.mp4
- 时长 13分3秒（音频 783s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:03] 那保存构造好了之后呢接着咱们继续按照API往下去写那好了接下来就是查询全部列表那查询全部列表在这边at request买品好了我这边呢value等于好了value呢跟上面这个基本上是一样的只不过最终我的请求方式变了变成了getOK那接下来呢public同样的result我们叫做finder
[00:40] 那各位来看我翻到的时候呢咱们查询企业列表来查询企业的部门列表那查询企业的部门列表也要指定我们的企业ID所以要指定企业ID那这个企业ID呢跟刚才是一样的是一样的我这边拿过来Ctrl COK那好了接下来呢我们就可以调用Department Service来完成操作
[01:13] 来完成操作所以department Service打点打点叫做find out那各位现在来看那我们刚才写的Find out方法没有考虑我们企业ID的这种情况所以我这边呢需要对这个方法进行改造死菌类型的来一个ID放进去company IDOK好了那我们这边就可以通过company ID来进行构造所以对于我们来说呢第一件事呢就是指定企业ID
[01:46] 好了那接下来第二件事就是完成查询好了跟刚才一样第三件事我们叫做构造返回结果那构造返回结果我们一会再说先把我们完成查询的这一步先给它搞定因为就目前来说因为就目前来说我这边return find out没用到这个参数那没用到这个参数所以显然是有问题的那我在这边怎么根据起ID查询
[02:15] 好了我们这边要用到一个比较特殊的叫做specialcation的方式来操作好了那我们一起来看一下如何去做其实department.do这个方法find all它有很多个重载的方法那我们现在要用哪个方法呢咱们就可以用接收一个specialcation这么一个接口的一个方式来做所以我在这边可以构造一个specialcation
[02:45] 好了他需要我们指定范型spec等于new一个specspecspecOK那接下来我们里面的代码如何去写呢注意我们现在查询的时候是不是就是根据叫做根据企业ID来进行查询那根据企业ID进行查询那我们这边就可以通过注意我把这个改一下cb好了这边叫root没问题
[03:19] 那根据企业ID查询我们可以通过cb.eco那eco其实指的是我们构造了一个等于比较的这么一个函数或者这么一个sql语句那我这边eco那eco这边呢eco里面接收的其实有这么几个参数首先你跟我对象的哪个属性比较root里面有所有的对象属性所以getc-o-m-p-a-n-y
[03:51] ID那你这个属性究竟是什么类型的所以S死菌.class好了接下来你这个值应该叫什么就是你传递过来的company ID即可好了这个special case就是这样去编写当了有的朋友可能对这个to proceedproc.cate这个方法呢可能会有疑问啊我在这里面呢把这几个参数给你各位简单的说一下首先呢这个
[04:24] 方法究竟在干什么它是用来用于构造查询条件的那构造的过程当中有三个参数第一个root好了第二个呢我叫CQ好了第三个呢我叫CB那这三个参数首先第一个它里面包含了所有的我们的对象属性
[04:52] 我们是根据对象属性的形式让它来进行Circle语句的一个生成那它除了Root之外呢还有一个CQCQ呢其实是用来更加高级的一些查询目前来说一般一般也不用好了接着还有第三个第三个是用来构造查询条件那构造查询条件那我们都知道查询的时候呢可能有很多种方式
[05:21] 比如说呢是等于号的这种形式比如说呢是模糊查询lack比如说大于等于比如说小于等于等等所以这个CP里面有所有的查询的一种方式和它的查询的内容那比如说呢我们现在用的是eco那其实除了eco之外呢可能还有打点打点比如说lack那比如说呢这边呢还有CB打点比如说not in或者not或者not lack等等等等很多都有其实跟我们的circle呢比较像
[05:50] 比较像只不过是以面相对象的形式来做那其实C比里面呢咱们构造的内容一般是有这么两个方面第一方面你根据哪个属性去比较第二个这个属性叫什么那我们都知道第一个构造的是属性那属性是不是在root当中啊所以我root打点get拿属性名那这样一来就根据这个属性去比较
[06:16] 那比较的内容是什么呢就是我们传递过来的company id那这样一来他查询拼接的circle语句就变成了注意company id当然了这个是我们的对象那我们的对象和circle语句有映射关系所以指的是company id等于比如说我这边传的1那他就变成了注意死菌类型搜创是一个1ok那这个就是跟各位简单的来看了一下这个special case好了上面呢我们就是构造条件
[06:50] 那条件构造好了之后我们这一回直接调用Find Out方法把我们的查询条件也传递进去就可以了那这样一来我们的Find Out方法就已经写好了那好了那我们这边呢再回来再回来那这样一来完成了查询完成查询之后构造返回结果
[07:14] 那在构造返回结果的时候其实有一点细节需要各位来看就是它我们API里面的返回的一个内容那这个返回内容其实还是相对来说有一点点复杂和我们的实体类对象现在就对应不上了那对应不上了各位会发现Data当中有这么三条这三条其实指的是你当前企业企业的名字企业究竟叫什么以及
[07:44] 底下包含的是当前这个企业里面的所有部门那其实这个里面是一数组那所有部门那部门里面的有ID这些其实跟我们的部门对象是不是在对应着呀所以对于我们来说呢先把这个基本的Data部分给它构造出来那构造出来怎么办呢注意我呢把所有的模型全部都放到Model这边
[08:11] 放到model这边那注意我们现在只需要构造data里面的内容就可以了result里面已经包含了这些已经包含了这些所以我们构造data部分是一个对象那既然是一个对象我把它放到model当中那是我们company里面的所以在这边我去构造一个我们需要的对象出来好了我把它放到我们的响应这个保持resresponseponse比如说呢我这边呢就叫做de
[08:41] PT list resultok好了那接下来呢这里面的数据都有什么呢我们可以一起看一下API一共有这么一段内容ok其中呢有common id private死菌类型的common id好了多来几条还有common name还有common managerok那这样一来上面部分我们已经构造出来了
[09:17] 那还有一个就是DEPTS那DEPTS里面是不是包含的应该是我们的部门的这么一个数组对象啊所以呢我在这边构造一个privatelist类型的department注意名字DEPTSOK那这样一来那这样一来我上边这些内容也就不需要了也就不需要了那好了为了我们这边的写起来简单一点我构造上它的get set方法
[09:50] 构造上它的无参构造构造方法那接下来为了让我这个代码写起来看起来更加舒服一些更加舒服一些public我习惯呢给它来以构造方法的形式去创建这个对象构造方法的形式去创建对象那比如说呢我可以传递过来一个company比如说呢我还可以传递过来一个我们叫做部门的历史集合OK
[10:26] 那好了接下来的事情呢就比较简单了好了就可以类似点company id就等于company打点get id类似点company name等于company打点get name好了类似点company manager等于company打点get注意这个呢指的是我们的公司的联系人我把这个
[11:04] 写到这儿公司的联系人那这些我们看过了之后呢接下来还有一个list集合那list集合这个比较简单list.dptlist等于dptsOK那这样一来我们这个返回的响应对象其实也已经给它写好那也已经写好了之后那我们在这边构造返回结果那就比较简单了那构造返回结果呢怎么去做dptlistresult
[11:34] 而DEPT list result等于new一个DEPT list resultOK那接下来呢由于我这个构造方法需要company需要DEPT这个list集合那我们现在find out之后得到的不就是一个list集合吗所以我构造方法的第二个参数就已经满足了我们还少前面这个那前面这个其实也好办我们可以通过at all to where注入进来一个company Service
[12:09] 我们查一把不就可以了所以在这边底下company打点find by id把company id传进去那这样一来我们就能够得到我们的企业对象那这样一来我这个数组构造成功了那好了接下来我们可以returnnew一个result那new result的时候首先注意首先它代表的是成功
[12:41] 那接着是不是这回有数据data部分有数据data部分所以把这个result构造出来就可以了result code.sqs逗号数据也放进去OK那这样一来我们的根据查询全部的企业列表也已经搞定了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

