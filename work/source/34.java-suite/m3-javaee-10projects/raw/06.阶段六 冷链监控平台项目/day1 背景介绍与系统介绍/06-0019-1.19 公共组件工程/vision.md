# 画面线理解：1.19 公共组件工程

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day1 背景介绍与系统介绍
- 源文件：06.阶段六 冷链监控平台项目\day1 背景介绍与系统介绍\1.19 公共组件工程_【海量资源尽在 666java.com】.mp4
- 抽帧：13 帧 @ 00:24, 02:21, 03:35, 04:07, 04:34, 04:48, 04:59, 05:29, 05:32, 05:33, 05:48, 05:57, 06:00
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 16:49:12

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
