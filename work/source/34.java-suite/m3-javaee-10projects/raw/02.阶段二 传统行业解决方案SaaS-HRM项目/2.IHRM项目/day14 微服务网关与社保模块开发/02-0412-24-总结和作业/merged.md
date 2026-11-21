# 24-总结和作业

- 阶段：02.阶段二 传统行业解决方案SaaS-HRM项目
- 章节：2.IHRM项目/day14 微服务网关与社保模块开发
- 源文件：02.阶段二 传统行业解决方案SaaS-HRM项目\2.IHRM项目\day14 微服务网关与社保模块开发\24-总结和作业_【海量资源尽在 ubkz.com】.mp4
- 时长 2分1秒（音频 121s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:02] 好了那到目前为止呢我们今天的这个所有内容呢就跟各位都聊过了那对于今天呢咱们一起看的内容呢一共就这么三块首先呢看了一下做网关那对于这个做网关而言呢这个是我们微服务当中用的比较多的这么一种组件通过做网关可以做到统一的请求进行分发并且呢在做网关我们可以做到统一的权限交易那这个权限呢咱们说过两种
[00:32] 一种是基于这种JWT的这种权限交易的方式一种是基于咱们说过的这种Shera的统一健全的方式不管是哪种其实都比较简单如果是基于JWT的涉及到就要用到组网关里面的这个过滤器当然我们说过了定义过滤器其实也比较简单那咱们统一健全的这一块和组网关咱们都搞定了之后又去完成了我们的核心业务就是社保
[00:58] 那对于社保呢里面相对的内容比较多我们完全就是围绕这么一张图来做的比如说呢在社保刚进来的时候我们让他设置你要制定的社保的年月份那接下来呢去展示我们当前月份这个员工他的社保缴纳的情况那对于某些员工比如说新入职的或者要调整他的社保参数那这边可以社保设置员工的社保情况那接下来
[01:23] 当前这个月所有社保我们搞定了之后可以生成月报表那月报表可以进行归档那需要各位注意的是在我们这个里面呢还有一块内容没有做啊就这边有一个历史归档的这么一个界面那其实这个很简单点击到历史归档里面这里面去查询当前所有的归档数据那我们查询什么注意查询的其实就是这个归档的主表这主表那这个主表当中又去关联我们的明细表
[01:54] 得到详细情况这个就留一个作业让各位去完成

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示基于Zuul的统一鉴权实现，包括Zuul过滤器的生命周期、自定义过滤器及JWT鉴权逻辑，并结合后台数据展示社保信息。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示iHRM系统社保信息页面，显示员工列表，筛选条件为“部门：test1”、“社保城市：北京”、“公积金城市：北京”，并展示员工编号、姓名、工号、部门、入职时间、离职时间、社保城市、公积金城市、社保基数、公积金金额等字段。
画面2：PPT页面，标题为“3.5 社保设置”，子标题“3.5.1 获取不同城市的社保缴费项目”，展示代码片段：
```java
@RequestMapping(value = "/list", method = RequestMethod.POST)
public ResultList<SearchListVo> searchListVo(@RequestBody SearchListVo searchListVo, @RequestParam(defaultValue = "1") int page,
        @RequestParam(defaultValue = "10") int pageSize, @RequestParam(defaultValue = "1") int companyID, @RequestParam(defaultValue = "1") int departmentChecks,
        @RequestParam(defaultValue = "1") int socialService, @RequestParam(defaultValue = "1") int providentFundChecks) {
    PageResult<SearchListVo> pageResult = new PageResult<>(itemPage.getTotalElements(), itemPage.getContent());
    return new Result(ResultCode.SUCCESS, pageResult);
}
```
画面3：PPT页面，标题为“2 基于Zuul的统一鉴权”，子标题“2.1 Zuul的过滤器”，展示ZuulFilter抽象类代码：
```java
public abstract ZuulFilter implements IZuulFilter(
    abstract public String filterType();
    abstract public int filterOrder();
    boolean shouldFilter(); // 灭火ZuulFilter
    Object run() throws ZuulException; // IZuulFilter
)
```
画面4：PPT页面，标题为“2.1.2 自定义过滤器”，展示自定义过滤器的代码片段：
```java
@Override
public String filterType() {
    // 定义过滤器类型
    return "pre";
}
@Override
public int filterOrder() {
    // 过滤器执行顺序
    return 1;
}
```
画面5：PPT页面，标题为“2.1.3 过滤器执行生命周期”，展示Zuul请求生命周期图，图中包含“Http Request”、“Http Response”、“pre filters”、“routing filters”、“post filters”、“error filters”、“custom filters”和“Origin Server”等组件。
画面6：PPT页面，标题为“2.2 统一鉴权”，子标题“2.2.1 基于JWT的统一鉴权”，展示自定义过滤器代码：
```java
@Component
public class AuthFilter extends ZuulFilter{
    @Override
    public String filterType() {
        // 请求类型，指定为鉴权过滤器
        return "pre";
    }
    @Override
    public int filterOrder() {
        // 过滤器执行顺序
        return 1;
    }
}
```
画面7：PPT页面，展示自定义过滤器的`shouldFilter()`方法代码：
```java
@Override
public boolean shouldFilter() {
    // 连接true，代表过滤器生效
    return true;
}
```
画面8：PPT页面，展示自定义过滤器的`run()`方法代码：
```java
@Override
public Object run() throws ZuulException {
    // 获取请求对象
    RequestContext ctx = RequestContext.getCurrentContext();
    // 获取请求头中的token
    String token = ctx.getRequest().getHeader("token");
    // 判断token是否为空
    if (StringUtils.isEmpty(token)) {
        ctx.setSendZuulResponse(false);
        ctx.setResponseStatusCode(401);
        ctx.setResponseBody("token不能为空");
        return null;
    }
    // 判断token是否有效
    try {
        Claims claims = Jwts.parser().setSigningKey("secret").parseClaimsJws(token).getBody();
        ctx.set("claims", claims);
    } catch (Exception e) {
        ctx.setSendZuulResponse(false);
        ctx.setResponseStatusCode(401);
        ctx.setResponseBody("token无效");
        return null;
    }
    return null;
}
```
画面9：PPT页面，标题为“3.5 社保设置”，子标题“3.5.1 获取不同城市的社保缴费项目”，展示代码片段：
```java
@RequestMapping(value = "/list", method = RequestMethod.POST)
public ResultList<SearchListVo> searchListVo(@RequestBody SearchListVo searchListVo, @RequestParam(defaultValue = "1") int page,
        @RequestParam(defaultValue = "10") int pageSize, @RequestParam(defaultValue = "1") int companyID, @RequestParam(defaultValue = "1") int departmentChecks,
        @RequestParam(defaultValue = "1") int socialService, @RequestParam(defaultValue = "1") int providentFundChecks) {
    PageResult<SearchListVo> pageResult = new PageResult<>(itemPage.getTotalElements(), itemPage.getContent());
    return new Result(ResultCode.SUCCESS, pageResult);
}
```
画面10：展示iHRM系统社保信息页面，显示员工列表，筛选条件为“部门：test1”、“社保城市：北京”、“公积金城市：北京”，并展示员工编号、姓名、工号、部门、入职时间、离职时间、社保城市、公积金城市、社保基数、公积金金额等字段。
画面11：展示iHRM系统社保信息页面，显示员工列表，筛选条件为“部门：test1”、“社保城市：北京”、“公积金城市：北京”，并展示员工编号、姓名、工号、部门、入职时间、离职时间、社保城市、公积金城市、社保基数、公积金金额等字段。
画面12：展示iHRM系统历史归档页面，标题为“全公司”，并显示“copyright© 2018 iHRM 系统 版权所有”。
画面13：展示SQLyog数据库管理工具界面，连接到本地数据库，当前打开的表为`ss_archive_detail`，显示数据记录。
画面14：展示SQLyog数据库管理工具界面，连接到本地数据库，当前打开的表为`ss_archive_detail`，显示数据记录。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
@RequestMapping(value = "/list", method = RequestMethod.POST)
public ResultList<SearchListVo> searchListVo(@RequestBody SearchListVo searchListVo, @RequestParam(defaultValue = "1") int page,
        @RequestParam(defaultValue = "10") int pageSize, @RequestParam(defaultValue = "1") int companyID, @RequestParam(defaultValue = "1") int departmentChecks,
        @RequestParam(defaultValue = "1") int socialService, @RequestParam(defaultValue = "1") int providentFundChecks) {
    PageResult<SearchListVo> pageResult = new PageResult<>(itemPage.getTotalElements(), itemPage.getContent());
    return new Result(ResultCode.SUCCESS, pageResult);
}
```
画面3：
```java
public abstract ZuulFilter implements IZuulFilter(
    abstract public String filterType();
    abstract public int filterOrder();
    boolean shouldFilter(); // 灭火ZuulFilter
    Object run() throws ZuulException; // IZuulFilter
)
```
画面4：
```java
@Override
public String filterType() {
    // 定义过滤器类型
    return "pre";
}
@Override
public int filterOrder() {
    // 过滤器执行顺序
    return 1;
}
```
画面6：
```java
@Component
public class AuthFilter extends ZuulFilter{
    @Override
    public String filterType() {
        // 请求类型，指定为鉴权过滤器
        return "pre";
    }
    @Override
    public int filterOrder() {
        // 过滤器执行顺序
        return 1;
    }
}
```
画面7：
```java
@Override
public boolean shouldFilter() {
    // 连接true，代表过滤器生效
    return true;
}
```
画面8：
```java
@Override
public Object run() throws ZuulException {
    // 获取请求对象
    RequestContext ctx = RequestContext.getCurrentContext();
    // 获取请求头中的token
    String token = ctx.getRequest().getHeader("token");
    // 判断token是否为空
    if (StringUtils.isEmpty(token)) {
        ctx.setSendZuulResponse(false);
        ctx.setResponseStatusCode(401);
        ctx.setResponseBody("token不能为空");
        return null;
    }
    // 判断token是否有效
    try {
        Claims claims = Jwts.parser().setSigningKey("secret").parseClaimsJws(token).getBody();
        ctx.set("claims", claims);
    } catch (Exception e) {
        ctx.setSendZuulResponse(false);
        ctx.setResponseStatusCode(401);
        ctx.setResponseBody("token无效");
        return null;
    }
    return null;
}
```
画面13：
```sql
SELECT
    bu.id,
    bu.username,
    bu.work_number,
    bu.department.name departments,
    bu.time_of_entry,
    bu.time_of_departure,
    bu

