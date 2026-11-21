# day10-7-标的信息检索-功能测试

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-7-标的信息检索-功能测试_【海量资源尽在 666java.com】.mp4
- 时长 11分30秒（音频 691s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 好通过咱们的努力刚才呢我们把业务层的代码全编写完了最后呢我们完善一下Controller这边代码就搞定了Controller代码非常简单嘛你把业务层注入进来然后调他的这个curryproject的index方法就行了最终呢把pvue对象是不是封装成rest response给前端就ok了这个代码非常简单然后快速的编写一下Controller就是它了
[00:30] 首先我们是要搞注入atoutview是吧然后注入的是业务层叫projectindexservice注入进来之后呢我们在方法里边我们就要调用他的这个叫queryprojectindex方法把上面这一堆参数全部给扔进去就行了
[01:12] 什么呀配置配置赛子是吧还有谁呀sort by然后谁呀然后呢接收他返回的数据返回的是一个配置view对象吗配置V o范形呢是project D T O接收一下然后呢再把这个配置view给他封装成rest response我放到这个rest response
[01:50] 那我们直接调用rest response的一个方法应该叫对success啊配给view给他放进去就ok了这是Controller的这个代码咱也就全部搞定搞定完之后呢咱接下来就可以进行测试那么一提到测试的话还是跟之前一样大家首先要想一想我们都需要启动哪些东西这次我们启动的也不少啊你看啊Apollo要启动es
[02:21] 还有黑的插件这些都要启动还有前端工程要启动因为我们要进行前后端几成测试那还有就是后端我们看都需要启动的还未服那你要搞前端几成测试你得登录对吧那所以说consumer就网关啊啊看他又哎呀对吧都要启动然后呢就是这个交易中心还有内容简单服务都要启动这个存款代理服务这次用到剩下这些你都得请
[02:54] 那我这边呢是该启动都已经全部提前启动好了咱为了节省时间你看前端工程呢我在这都已经打开了是不是就等着测试但咱接下来先这样咱先通过Postman先测一测Postman啊Postman里边测试还是比较灵活的在为了节省时间呢这个该填的这些信息我都已经填好了咱一起看一下你看我这是往哪发的请求啊53060Translation是不是往哪发的请求啊网交易中心对吧
[03:23] 为什么往交易中心发请求呢你看这个图呗看这个需求分析当实际图我们是不是前端发请求先到交易中心吧是不是然后交易中心再通过分引到内容检测服务然后再进行查询所以我在铺图卖里边就先往交易中心发请求然后你看看这是分页数据这是什么呀排序排序呢我没有给值没有给值我们说了没有给值我们是不是会按照发标的时间倒去排练了对不对说这俩你不给值无所谓但分页的数据你得给
[03:53] 条件呢条件呢是封装成JSON在这儿放上JSON而且咱刚才在实现右层的代码的时候大家知道我们的条件就给了三个吧是不是一个是根据什么呀是哪个呀这个一个是根据名字做的这个词条查询还有就是这个借款期限的一个范围的一个查询别的全在没加啊所以你看我这个pose卖里边我这就先拿着内部做一个测试
[04:29] 那这就准备完了咱就点击4呢开始进行测试了走查出来了吧你看对不对这不是数据吗冯璐女是第一次借款这边不是有借款这个词吗是不是还有啥赵森第六次借款对吧等等等等四条数据那咱看咱黑的里边总共几条数据啊总共就四条是不是全查出来我咋全查出来因为我这里边是每页显示几条啊每页显示十条啊是不是
[05:00] 你可以改小一点改成二你再你再试试散的走然后你看几条数据是不是两条数据吗总共四条但是查出来是几条两条吗这非也是没问题的然后其他的场景条件你自己在这儿是吧我在这儿就不再挨个演示了这是破坏漫画测试通过测试通过之后我们还要去前端做这个前后端集成测试那咱就直接打开前端这个登录页面直接进行登录我们挑一个账号
[05:30] 这个账号还用这个吧以前这个密码呢还是这个手机号对吧好登录登录进来之后呢咱应该点哪应该点哪是不是点出借对不对然后呢你看这这就是我们的前端搜索界面大家一看会发现我们这个搜索条件就一种相当于是不是没有加别的条件就是根据这个什么呀借款的期限按照月份对吧
[06:00] 0到6个月的6到12个月的12月以上的所以说我们其实跟前端集成测试的时候我们前端界面上这个搜索条件还是比较少的那你接下来直接进行测试就行了你就点点试试比如说这个目前是全部默认全部是4条记录因为刚才让大家看了咱们这个Elasticsearch里边是不是就一共4条数据那全部肯定就意味着是4条数据都查出来了是不是你看
[06:29] 那咱接下来试试这个什么呀0到6个月没查出来是不是这可没报错你看它就是什么呀没查出来对不对然后6到12个月的6到12个月的一下查出来什么呀4条是不是4条你看这吧result是吧是不是4条是不是那证明咱们这里边的数据全是6到12个月的吗那你看这360
[07:03] 这个单位咱以前可是说过它的单位是天对不对360天你自己算吧那它的范围就是6到12个月这个范围是不是6到12月这个范围所以说呢这是咱测试数据的问题另外呢咱这里边呢还有一个小问题大家看一下咱这边取到的这个年化利息这些值是不是全都是零啊
[07:27] 对不对证明这个值咱没有取到啊没有取到那这个原因在哪呢大家注意一下这是一个小问题原因在这大家看这块代码这块代码大家应该还有印象吧这是不咱这个检索完成之后是不是在做数据封装对吧我们在这在做数据封装的时候呢并没有把那个年化利息那个值给它封装到什么呀project的dto对象里边啊所以说造成呢
[07:57] 这个值呢并不存在所以说前端那边呢就是一个0那你在这呢可以稍作处理就行了就跟这些代码一样你把那个年化利息给他取出来就行了那个键的名字呢大家可以查一下这个黑的插件里面我们看一下那个值那个值应该是应该是这个这个值我要取的就是他的值年化利息那这个代码怎么写呢跟上边一样呗
[08:29] 你就往这接着加我这呢就他应该是一个什么类型啊他应该是一个啊big decimal类型的吧我看看这个封装的时候应该是一个big decimal是不是那我们就可以这么的来写吧我们声明一个变量啊来接收一下呃然后呢接下来呢还是从s o u rsource as map当中对吧通过get方法去取这个值
[09:05] 然后呢大家看他报错了对吧这是需要做类型转换的你看这个get方法返回来是不是一个object类型的对不对那我怎么把它转换成big decimal类型呢那咱进来直接new一下看看他的这个构造方法是否支持啊big decimal我们直接new一个对象然后呢把它直接放进来看行不行不行是吧不行的话那也好办我们给他转换成什么呀字幕串就ok了
[09:35] 对我们把那个应该是0.1吧我记得刚才是不是0.1啊但是呢他取出来是一个对象我们把它转成字符串啊然后呢通过这个big decimal的这个代参的勾当方法就可以把它转成big decimal这种类型的数据然后呢我们就可以怎么着呢在这吧把它往project DTO里边进行什么呀封装我们调用他的set方法啊应该是找找啊应该是哪个嘞
[10:06] 这个然后呢把刚才这个值给他放进去就OK了对不对稍微加点代码然后呢你要想测试的话你是不是需要就是把哪个服务需要重启一下对content search把它重启一下重启完之后呢你前面这边是不是继续刷新看看这个值呢有没有拿到手就行了那我们这边呢等待它启动完毕我们需要稍等片刻
[10:37] 好这样的应该是启动完了啊启动完之后呢咱这边是得刷新刷新对不对看他有没有取到值哎大家看一下这个值是不是已经取到了啊当然呢我们这四条记录给的这个利息都是这个0.1就是到这边一换算就是10%嘛这数据都一样啊但是呢这个呃一个小问题吧我们就解决了所以目前呢咱们在进行搜索的时候呢前端这边啊6到10个月呢是能把数据搜出来了其他是搜不出来了这跟咱的这个数据有关
[11:07] 那咱前端这个测试就到这儿因为咱这上面就摆了这些条件那其他的这个条件你要想测试还是跟我们刚才一样你在Postman里边可以这个随便玩对吧进行各种各样测试这是目前吧咱就把标底信息的快速检索功能呢全部测试完了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 P2P 项目中通过创建内容搜索服务，结合 Elasticsearch 和 Logstash 技术栈，实现对交易数据的全文检索功能。

2) 按时间顺序列出每张画面的要点：
画面 1:
要点：展示 ContentSearchController 中的 queryProjects 方法，其中调用 contentSearchAgent 查询索引，并在响应不成功时抛出业务异常。
代码：
```java
@Override
public PageVO<ProjectDTO> queryProjects(ProjectQueryDTO projectQueryDTO) {
    RestResponse<PageVO<ProjectDTO>> response = contentSearchAgent.queryProjectIndex(projectQueryDTO, 
        projectQueryDTO.getOrder(), projectQueryDTO.getPageNo(), projectQueryDTO.getPageSize(), projectQueryDTO.getSortBy());
    if (!response.isSuccess()) {
        throw new BusinessException(CommonErrorCode.UNKNOW);
    }
    return response.getResult();
}
```

画面 2:
要点：展示 ContentSearchController 中的 queryProjectIndex 方法，其方法体中调用 projectIndexService 的 queryProjectIndex 方法。
代码：
```java
public RestResponse<PageVO<ProjectDTO>> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortBy) {
    return projectIndexService.queryProjectIndex(projectQueryParamsDTO, pageNo, pageSize, sortBy);
}
```

画面 3:
要点：展示 ContentSearchController 中的 queryProjectIndex 方法，其方法体中调用 projectIndexService 的 queryProjectIndex 方法，代码自动补全。
代码：
```java
public RestResponse<PageVO<ProjectDTO>> queryProjectIndex(ProjectQueryParamsDTO projectQueryParamsDTO, Integer pageNo, Integer pageSize, String sortBy) {
    return projectIndexService.queryProjectIndex(projectQueryParamsDTO, pageNo, pageSize, sortBy);
}
```

画面 4:
要点：展示 PPT 中的代码片段，说明 ContentSearchController 中的 queryProjectIndex 方法如何调用 projectIndexService。
代码：
```java
@PostMapping(value = "/l/projects/indexes/q")
public RestResponse<PageVO<ProjectDTO>> queryProjectIndex(
    @RequestBody ProjectQueryParamsDTO projectQueryParamsDTO,
    @RequestParam Integer pageNo,
    @RequestParam Integer pageSize,
    @RequestParam(required = false) String sortBy) {
    PageVO<ProjectDTO> projects = projectIndexService.queryProjectIndex(projectQueryParamsDTO, pageNo, pageSize, sortBy);
    return RestResponse.success(projects);
}
```

画面 5:
要点：展示 PPT 中的“4.1 需求分析”章节，说明为提高数据查询性能，需要创建内容搜索服务，采用 Elasticsearch 和 Logstash 技术栈。
架构图：
- 潘发APP → 交易中心 → 内容搜索服务 → ES索引
- 交易中心 → 内容搜索服务 → ES索引
- 内容搜索服务 → ES索引

画面 6:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将 PageVO 的内容设置为 list，设置分页信息。
代码：
```java
// 将为 PageVO 设置分页信息
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
pageVO.setTotalCount(totalCount);
return pageVO;
```

画面 7:
要点：展示 Elasticsearch 的 head 插件界面，显示 wanxing2p_project 索引中的数据，其中一条记录的 status 字段值为 "FULLY"。
数据：
```json
{
  "_index": "wanxing2p_project",
  "_type": "doc",
  "_id": "2135463643093290627",
  "_score": 1.0,
  "_source": {
    "amount": 22320,
    "period": 360,
    "version": 1,
    "consumerId": 25,
    "name": "个人生活贷款",
    "description": "个人生活贷款",
    "projectStatus": "FULLY",
    "createdate": "2019-06-30T02:20:20.252Z",
    "status": "FULLY"
  }
}
```

画面 8:
要点：展示万信金融网站的首页，以及浏览器开发者工具中的 Network 面板，显示了多个请求的响应时间。
数据：
- 请求 1: 30 ms
- 请求 2: 100 ms
- 请求 3: 150 ms
- 请求 4: 230 ms

画面 9:
要点：展示万信金融网站的“金融投资”页面，以及浏览器开发者工具中的 Network 面板，显示了多个请求的响应时间。
数据：
- 请求 1: 1000 ms
- 请求 2: 2000 ms
- 请求 3: 3000 ms
- 请求 4: 4000 ms

画面 10:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将搜索结果转换为 ProjectDTO 对象并添加到 list 中。
代码：
```java
for (SearchHit hit : searchHits) {
    ProjectDTO projectDTO = new ProjectDTO();
    Map<String, Object> sourceMap = hit.getSourceAsMap();
    Double amount = (Double) sourceMap.get("amount");
    String projectStatus = (String) sourceMap.get("projectStatus");
    Integer period = Integer.parseInt(sourceMap.get("period").toString());
    String name = (String) sourceMap.get("name");
    String description = (String) sourceMap.get("description");
    projectDTO.setAmount(new BigDecimal(amount));
    projectDTO.setProjectStatus(projectStatus);
    projectDTO.setPeriod(period);
    projectDTO.setName(name);
    projectDTO.setDescription(description);
    list.add(projectDTO);
}
```

画面 11:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将搜索结果转换为 ProjectDTO 对象并添加到 list 中，代码高亮显示了 name 字段的赋值。
代码：
```java
String name = (String) sourceMap.get("name");
```

画面 12:
要点：展示 ProjectIndexServiceImpl 中的 queryProjectIndex 方法，其中将搜索结果转换为 ProjectDTO 对象并添加到 list 中，代码高亮显示了 pageSize 字段。
代码：
```java
Integer pageSize = Integer.valueOf(projectQueryParamsDTO.getPageSize());
```

画面 13:
要点：展示 Elasticsearch 的 head 插件界面，显示 wanxing2p_project 索引中的数据，其中一条记录的 status 字段值为 "MISCARRY"。
数据：
```json
{
  "_index": "wanxing2p_project",
  "_type": "doc",
  "_id": "21455063275464705",
  "_score": 1.0,
  "_source": {
    "amount": 2000,
    "period": 360,
    "version": 1,
    "consumerId": 19,
    "name": "个人生活贷款",
    "description": "个人生活贷款",
    "projectStatus": "MISCARRY",
    "createdate": "2019-06-30T02:20:20.252Z",
    "status": "MISCARRY"
  }
}
```

画面 14:
要点：展示万信金融网站的“金融投资”页面，以及浏览器开发者工具中的 Network 面板，显示了多个请求的响应时间。
数据：
- 请求 1: 2000 ms
- 请求 2: 4000 ms
- 请求 3: 6000 ms
- 请求 4: 8000 ms

