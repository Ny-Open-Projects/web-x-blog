# 1.19 公共组件工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.19 公共组件工程_【海量资源尽在 666java.com】.mp4
- 时长 6分44秒（音频 404s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 下面我们来看一下公共工程组件code common那么这个code common里边包含了什么东西呢一方面它包含了一些道层包括了一些实体类那么同时呢它还包括了一些公共的工具类那么为什么我们要这样设计我们可以想象一下假设我有一个工程而这个工程呢比如说叫code admin这个工程这个工程里边它
[00:29] 有一些自己的Controller层有自己的Service同时还有自己的道层和自己的这种实体那我们放到我们的code comment里面是可以的对吧那另外一个工程假设我们的code monitor这个工程这工程也有相同的实体类也要访问相应的这个同样的一个表那在这种情况下因为它是我的服务已经拆成了两个微服务对吧那么我的
[00:59] 但是我访问的数据库呢或者访问的这个表呢还是同一张表那或者是说我即使不访问同一张表那我有些实体那我想一些公共的使用那我用了一些比如说code monitor它用了code admin里面的一个实体类那在这种情况下我一方面如果我在code monitor里面再添加一个类这是不合适的对吧那在这种情况怎么办呢我们就把这个实体类往code comment里面抽抽离出来我把它
[01:28] 公共的两个工程公共使用的一些类这个类的话就是道层的类和我们的实体类我们放到code common里边去这就是我们code common里边包含了道和实体类的一个原因那么在我们的code common里边我们包含了admin工程里边的实体和道层我们包含了job实体里边的就是code job
[01:54] 这个工程里边用到的一些实体和道场还有一个就是我们在native服务器里边用到的在这儿那还有一个地方或者还有一些公共的本身我们这个工程可以如果是作为公共的工程被其他工程来引用的时候那么有一些公共的一些方法公共的一些类我们就可以放到这里边了这种公共的包括什么呢包括我们的错误的异常处理
[02:23] 我可以自定义我们的异常我可以比如说我定义这个异常比如说像我们的这个myException这个myException来讲的话我们定义它有两个字段一个叫做message一个叫code我code可以等于500或者说我code等于401等于这个多少多少我可以自己定义定义出来而不是用这个系统提供的那么它在使用上来讲的话它可以使用直接是through一个new
[02:49] myException然后呢添加我们的这个类型或者添加我们的这个message的一个一个文字我直接在我们的应用里面就可以就可以调用这个异常的一个处理了那另外的一个公共的在这里我想给大家介绍的其实就是一个R这个R你可以理解为它就是一个返回数据的类型比如说我们返回我们的一个Controller层
[03:18] 这个Controller层我们需要给前端来返回那返回什么呢返回肯定是说第一我要返回我们的code到底是属于200属于正常的或者是或者说属于失败的那么我们可以在这来使用我们的这个这个R这个返回那同样同时我们还可以返回一个自己定义的一个一个K也就是说我在返回的时候它是一个json trimmer
[03:47] 这个系统圈里边有code有message我还可以加别的你自己想想添加什么就添加什么我们可以把我们的列表list列表然后返回给前台那前台来使用那么我们可以看看我们在实际的这个工程里边用到的在我们的这个code admin里边我们可以看到我们的codecompany controllercompany Controller的时候我们就直接用R点ok然后呢把我们的这个配置
[04:17] 配置的这个就是说每一页分一页的数据给它返回过来我们还可以用R.OK然后put就添加一个我们的这个company给它来返回这是我们使用了一个就是在我们的这个common工程里边公共的一个类这个公共的类里边我们其他的几个工程啊比如说无论是说我们的这个monitor或者是user或者是admin
[04:46] 他们都会用到了我们这种返回给前端也就是说我们的API直接把结果返回给前台那么返回给前台我们把这个类是作为一个公共的一个类了那还有一个类的话是属于我们的PageUtilsPageUtils是一个分页的工具对吧那么我们在使用它的时候呢我们会定义我们每一页整个的查询它查询的总的记录数每一页的记录数
[05:14] 每一页总的记录数和当前的页数以及我们的一个数据列表它是个类似类型的那么我们这个PageUtil它的使用上是在我们的Service层里面因为Service本身你要查询一个company我们查询company的时候我们要根据我们的参数查询条件我们要返回一个我们的查询结果而把查询结果返回过来的时候实际上就是一个PageUtil
[05:43] 我们把查询的结果按照分页的方式来放到我们的配置Util这个实体里边那么我们再把这个实体用R这个返回值返回给我们的天台这是实现的是简单的这个分页这是我们的这个code common工程那code common工程里边我们还可以定义我们的一个公共的变量我们还可以定义我们的redis的一个实体或者redis的一些方法
[06:13] 包括我们对于YAML文件的一个公共的工具这些都是我们在CodeCommon里边可以用到的或者说是定义好的一些类那么这些类呢我们在其他的其他的工程里边会用到那么以后呢我们后边呢我们在其他工程里边介绍一些这个工程的时候或者介绍一些项目代码的时候我们会讲解一些我们在CodeCommon里边用到的其他的一些类

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示一个冷链监控系统中，如何在 common 模块中定义统一的异常类和分页工具类，并在 admin 模块的控制器和业务层中使用它们。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示项目结构，选中 cold_admin 模块，准备进入代码编辑。
画面 2: 选中并打开 cold-common 模块下的 MyException.java 文件，展示自定义异常类的定义。
画面 3: 在 MyException.java 中，展示构造函数和 main 方法，用于演示异常抛出。
画面 4: 在项目结构中选中 CompanyController.java，展示控制器层的代码。
画面 5: 在 cold-common 模块中选中 R.java，展示统一的响应结果封装类。
画面 6: 在项目结构中选中 HostController.java，展示另一个控制器。
画面 7: 在 cold-common 模块中选中 PageUtils.java，展示分页工具类。
画面 8: 在项目结构中选中 CompanyServiceImpl.java，展示业务层代码。
画面 9: 在 CompanyServiceImpl.java 中，展示分页查询的实现逻辑。
画面 10: 在 CompanyServiceImpl.java 中，展示分页查询的实现逻辑，光标在 QueryWrapper 的 lambda 表达式上。
画面 11: 在 PageUtils.java 中，展示 Pageable 的构造函数和分页数据的封装方法。
画面 12: 在 cold-common 模块中，选中并打开 R.java 文件。
画面 13: 在 R.java 文件中，展示 R 类的静态方法，用于返回统一的响应结果。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
super(msg, e);
this.msg = msg;
this.code = code;
}
public MyException(String msg, int code, Throwable e) {
super(msg, e);
this.msg = msg;
this.code = code;
}
public static void main(String[] args) throws MyException{
try{
int i = 1;
}catch (Exception e){
throw new MyException("异常中分号不能为空");
}
```

画面 3:
```java
public R() {
put("code", 0);
put("msg", "success");
}
public static R error() {return error(HttpStatus.SC_INTERNAL_SERVER_ERROR, "未知异常，请联系管理员");}
public static R error(int code, String msg) {
R r = new R();
r.put("code", code);
r.put("msg", msg);
return r;
}
public static R ok(String msg) {
R r = new R();
r.put("msg", msg);
return r;
}
```

画面 4:
```java
@RequestMapping("/list")
public R list(RequestParam Map<String, Object> params) {
PageUtils page = companyService.queryPage(params);
return R.ok(page.getPage());
}
@RequestMapping("/info/{id}")
public R info(@PathVariable("id") String id) {
CompanyEntity company = companyService.getById(id);
return R.ok().put("company", company);
```

画面 5:
```java
package com.thema.cold.common.utils;
import ...
@Data
public class R extends HashMap<String, Object> {
private static final long serialVersionUID = 1L;
public R() {
put("code", 0);
put("msg", "success");
}
public static R error() {return error(HttpStatus.SC_INTERNAL_SERVER_ERROR, "未知异常，请联系管理员");}
public static R error(int code, String msg) {
R r = new R();
r.put("code", code);
r.put("msg", msg);
return r;
}
public static R ok(String msg) {
R r = new R();
r.put("msg", msg);
return r;
}
```

画面 7:
```java
package com.thema.cold.common.utils;
import ...
@Data
public class PageUtils implements Serializable {
private static final long serialVersionUID = 1L;
// 总记录数
private int totalCount;
// 每页记录数
private int pageSize;
// 总页数
private int totalPages;
// 当前页码
private int curPage;
```

画面 8:
```java
@Service("companyService")
public class CompanyServiceImpl extends ServiceImpl<CompanyDao, CompanyEntity> implements CompanyService {
@Override
public PageUtils queryPage(Map<String, Object> params) {
//分页参数
int current = params.get("page") == null ? 1 : Integer.valueOf(params.get("page").toString());
int size = params.get("pageSize") == null ? 10 : Integer.valueOf(params.get("pageSize").toString());
Page<CompanyEntity> page = new Page<>(current, size);
//查询条件
String company = params.get("company") == null ? "" : params.get("company").toString();
QueryWrapper<CompanyEntity> wrapper = new QueryWrapper<>();
wrapper.lambda().like(CompanyEntity::getCompany, company);
//执行查询
IPage<CompanyEntity> result = this.page(page, wrapper);
//返回分页化数据
return new PageUtils(result);
```

画面 9:
```java
@Override
public PageUtils queryPage(Map<String, Object> params) {
//分页参数
int current = params.get("page") == null ? 1 : Integer.valueOf(params.get("page").toString());
int size = params.get("pageSize") == null ? 10 : Integer.valueOf(params.get("pageSize").toString());
Page<CompanyEntity> page = new Page<>(current, size);
//查询条件
String company = params.get("company") == null ? "" : params.get("company").toString();
QueryWrapper<CompanyEntity> wrapper = new QueryWrapper<>();
wrapper.lambda().like(CompanyEntity::getCompany, company);
//执行查询
IPage<CompanyEntity> result = this.page(page, wrapper);
//返回分页化数据
return new PageUtils(result);
```

画面 10:
```java
@Override
public PageUtils queryPage(Map<String, Object> params) {
//分页参数
int current = params.get("page") == null ? 1 : Integer.valueOf(params.get("page").toString());
int size = params.get("pageSize") == null ? 10 : Integer.valueOf(params.get("pageSize").toString());
Page<CompanyEntity> page = new Page<>(current, size);
//查询条件
String company = params.get("company") == null ? "" : params.get("company").toString();
QueryWrapper<CompanyEntity> wrapper = new QueryWrapper<>();
wrapper.lambda().like(CompanyEntity::getCompany, company);
//执行查询
IPage<CompanyEntity> result = this.page(page, wrapper);
//返回分页化数据
return new PageUtils(result);
```

画面 11:
```java
public PageUtils(List<?> list, int totalCount, int pageSize, int curPage) {
this.list = list;
this.totalCount = totalCount;
this.pageSize = pageSize;
this.curPage = curPage;
this.totalPage = (int)Math.ceil((double)totalCount/pageSize);
}
public PageUtils(Page<?> page) {
this.list = page.getRecords();
this.totalCount = (int)page.getTotal();
this.pageSize = (int)page.getPageSize();
this.curPage = (int)page.getCurrent();
this.totalPage = (int)page.getPages();
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

