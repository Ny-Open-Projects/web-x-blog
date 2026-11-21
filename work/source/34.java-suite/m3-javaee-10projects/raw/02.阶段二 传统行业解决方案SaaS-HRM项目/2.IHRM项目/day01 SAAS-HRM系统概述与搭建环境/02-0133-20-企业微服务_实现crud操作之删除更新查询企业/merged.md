# 20-企业微服务：实现crud操作之删除更新查询企业

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day01 SAAS-HRM系统概述与搭建环境
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day01 SAAS-HRM系统概述与搭建环境\20-企业微服务：实现crud操作之删除更新查询企业_【海量资源尽在 ubkz.com】.mp4
- 时长 7分56秒（音频 477s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 其的保存我们做过了之后接下来就是根据ID更新根据ID更新根据我们刚才总结的套路希望各位还有印象总结的套路首先第一件事我们可以配置一个我们的方法接着第二件事看我们的请求参数第三件事构造我们的响应OK配置一个方法Public注意我们现在的响应全部都是Result
[00:30] resultresultresult好了这个方法呢我叫做updateupdate那这个update的方法那你的请求路径是什么我们再来看API更新更新更新就修改OK好了后面呢是不是接着是一个ID啊接着是一个ID那在我们这边再去进行一个配置request mapping好了request mapping这一回呢它就
[01:04] 有此地址了那这个地址是什么呢注意$ID表明我这边是一个地址参数注意它其实不仅仅是地址一部分它还是一个参数好了那接下来呢我的请求方式method一般来说更新没别的都是putok我们来看一下put没问题
[01:32] 那接下来就是说我们需要把请求参数给它全部都构造出来请求参数根据IDID是地址的一部分那我们就可以通过一个注解at pass varb从地址当中获取给它封装到一个ID属性上当然了你前面这边可以给它指定你要拿的是ID从ID我们的地址链接上获取到获取到之后复制到ID属性那好了接下来那除了有ID之后
[02:01] 你剩下的那些内容是不是可以封装到一个company对象里所以request body company那我们来看一下是不是这样看一下API接口根据ID修改你发现第一个地址参数ID第二个代表的是我们company对象OK没什么问题那里面的代码写法比较简单比较简单业务逻辑操作那业务逻辑操作直接调用company Service打点
[02:36] update把company传进去即可但是我想说这么传不行因为当前这company里面没有ID所以company打点setID把ID传进去前面是我们的ID后面是它这个所有的属性那传过来之后在里面根据ID查记得修改属性啊OK那这些都搞定了之后我们可以返回当然了这个也不是我瞎写的也是根据我们的接口
[03:05] 来的接口其实也是code flag message我们封装到result对象里好了更新搞定了剩下的事情就是搞删除删除首先public配置一个方法result代表返回数据delete接下来有没有方法写好了方法写好了配置请求地址路径request mapping我们这个配置请求地址路径和上边这个是一样的daughter id
[03:40] 好了我们现在的请求方式刚才做过介绍删除一般就是delete没别的好了那接下来既然有ID的话我们就可以通过password从地址参数当中获取获取之后要用业务逻辑操作companyservice我们写好了直接delete把ID把ID传下去即可当然了你的响应跟我们之前一样之前一样OK好了那根据ID我们删除
[04:10] 搞定了接下来根据ID查询企业那根据ID查询企业public写的方法result我叫做find by id那find by id配置一把at request mapping根据ID查也是以ID传递的形式拿过来只不过这回不叫做delete叫做打点get你的请求方式是get那同样的你有地址参数OK那接着我们里面的写法是什么样的
[04:47] 根据Service打点,点find byid,把id传过去比如说就叫company,id传过去得到company之后我们把它封装到result对象里面即可result查阅成功了你有一个result,result.successok result那需要各位注意的是就是根据id查询我们来看一下API接口根据id查询
[05:25] 那根据ID查询的时候它会给你传过来一个ID那接着你的返回有code有flag有message那注意各位我这个result里面现在已经构造了success构造了code构造了message那这些我们都构造成功了之后是不是还有data是一个缺失的这么一个部分啊所以我们接下来关注的就是data返回数据
[05:53] 那返回数据究竟是什么看它data里面的内容那这个data里面的内容是不是就是应该是我们这个对象啊所以我这个data现在没值没值怎么办很简单result.setdata是把我们的company传进去就可以了好了接下来我们可以returnresultok
[06:24] 好了那根据ID查询我们也搞定了之后接着就是最后一个查询企业列表同样的看一下API接口查询全部列表那这个全部列表呢get方式提交那里面的响应code等等一大堆还有datadata这回是一数组了各位是一数组了所以对于我们而言很简单data现在是一粒子集合查据来放到result里面就可以了吧
[06:55] OK好了根据套路我们这边先写一个方法好了我叫Find Out好了请求的Request Mapping呢直接copy一下请求路径我们看过了没有地址直接用副路径Company即可好了接下来呢里面的代码呢很简单很简单Company Service我们写过一个方法打点翻到得到所有列表List那接下来呢我们构造一个Result对象接着Result对象
[07:33] 打点set data把list放进去好了接着最后returnOK那这样一来我整个的web层的Controller所有的增深改查方法咱们就已经全部都写好了OK

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

