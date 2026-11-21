# day10-6-标的信息检索-内容检索服务-功能实现2

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-13 实现标的信息检索功能
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-13 实现标的信息检索功能\day10-6-标的信息检索-内容检索服务-功能实现2_【海量资源尽在 666java.com】.mp4
- 时长 13分16秒（音频 796s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱接着编写代码前面咱是不是主要把条件这方面封装好了对不对咱接着往下写接下来是这样我们接下来要封装什么排序封装分页包括上面条件我们也要进行封装封装到哪我们要把所有的信息全部放到一个总的封装对象里边叫search source builder因此对象我们也先在这创建一下直接6就行了叫
[00:29] search什么呀对source builder然后直接new出来无参构造就ok了对象创建出来之后我们先把这个条件放进去因为咱这个条件是不是在上面已经封装到这个core builder这个对象里边了对不对主要这个比较简单我们直接就是调用它的一个方法叫啥名呢叫core方法直接把上面这个core builder
[00:59] 放进去就行我们就把条件放到总的对象里边接下来我们要设置什么对排序的参数还有什么分页的参数这些代码相对来说比较简单比较好理解我就不再给他编写了我们看一下这个讲义就行你看设置排序信息这块代码有点像咱们之前在查询数据库的时候写的那个代码首先我们也是要判断sort by还有order它俩值为不为空对不为空的话我们还要判断
[01:31] 这个前端传过来的是升序还是什么呀对降序啊因为他调的方法是不一样的那么在es当中怎么进行排序查询呢或者怎么进行排序的封装呢我们要调用search source builder就是这个总的封装对象的一个方法叫塑造方法你比方两个字段第一个字段啊两个参数第一个参数塑造败就表示按哪个字段进行排序啊第二个参数呢大家看是不是一个这应该是枚具吧是什么呀
[02:00] 表示升序还是什么降序这是排序的参数的设置当然我们要考虑到万一客户那边他没有传这两个值我们自己采用一个策略就是按照标底的发表时间进行一个降序排名这是else对不对一个降序排名非业信息也比较简单调用它的两个方案就行了一个是form一个是sizeform就表示从哪一行开始查
[02:29] 所以你要根据这个公式来转换一下因为咱前端传过来这是页码是吧就第几页他这要的是第几行啊所以你要做一个转换这个我不在过头说大家都知道那赛子呢就是设置每页显示多少行的所以这是怎么设置排序还有分页的这个参数这个我就不再编写了啊我就直接粘过来拿用这个是设置什么呀排序的这是设置排序的然后啊这还有一部分
[03:06] 还有设置分页我们把这两行呢拿到下面那么大家看一下目前啊目前我们往总的封装对象里边都放了哪些东西条件有了排序的也有了分页的是不是也都有那该放进去的都已经封装好了那最终我们就要完成全部的这个封装完成封装是啥意思呢我们要把这个src source builder这个总的封装对象给谁啊给最上面这个请求对象
[03:49] 你看这个请求对象是不是他里边已经知道要查哪个索引库了然后我们再把这个总的封装对象给他那里边是不是带有条件带有分页带有排序是不是该有的都有是不是所以我们最终要完成这一步的封装就是调他的一个方法叫什么叫source然后把这个search把source builder总的封装对象呢放进去就行了这就完成了对最终的一个封装
[04:17] 这个封装完成了之后接下来就可以进行搜索到什么执行了就开始正式的我们从ES锁印库里边要进行什么查询了那在进行查询之前呢我们要做一些准备工作我们要创建一个集合这个集合的范围型呢就是这个project的detail因为我们将来查出来数据是要封装到集合里另外呢我们还要创建一个配置view对象因为我们最终返回的是不是配置view对不对
[04:45] 我要把这个准备工作给做好一会呢就等着接收数据了那首先先创建一个集合吧list的范形式project的dto就叫list吧list等于之间nearreleased这是一个准备工作然后还要创建配给vo对象范形式呀配给vo对象的范形仍然是project谁呀dto这个
[05:22] 然后名字呢就叫配几VO哎这不对啊这是project DTO这个对象呢是不是也是直接NEO的吧NEO配几VO好搞定啊这是两个准备工作准备工作做到位之后呢咱接下来就要进行搜索那么这个搜索功能主要就是靠我们上面注入进来这个谁啊这个扣端对象就靠他通过他发请求吧进行搜索
[05:55] 调用他的一个方案叫什么方法对这个方案其实就叫search我们要调用这个两个参数第一个参数大家看是不是我们上面这个search request的这个请求对象第二个参数呢是一个呃也是一个参数配置吧但是这呢我们暂时呢直接用他默认的这个default这个就行了大家就不用管他了主要是第一个参数你要给对那其实这一步其实就就是在进行什么呀对这一步就是在进行
[06:26] 搜索这不一执行完我们其实就拿到这个柴云出来这个结果就这个方法它是有反应值你看是不是叫47对吧所以说我们这要进行接收啊SEARSEARCHSEARCH RESPONSE响应回来的数据是不是这报错看看啊啊他要求必须进行什么呀一场处理那咱就
[07:00] 加上try catch咱一直给它包到哪包到最下面咱包到这个地方吧到这吧我这就写了总的一个负类对象它这强制要进隐藏处理所以说这我们其实就接收到这个什么呀结果接收到结果之后我们要从这里边取各种各样的信息对吧比方总记录说呀我们还要取出来里边的具体的数据还要循环封装成DTO对象等等等等
[07:41] 那咱们接下来一起看一下讲义上的代码你看这儿啊我们得到这个结果之后你看这里边呢我们要去获取想要的结果是要调用他的一个方法叫get piece就是他叫什么呀命中的数据啊命中的就是这个命中的数据说白了就是符合条件的呗查出来的这些数据叫命中的数据啊查出来数据的最终是封装的叫一个叫30 piece这样的一个内容
[08:09] 其实你可以把它当成就类似于一个集合一样的一个东西那然后呢我们再调他的一个方案叫get total hit点value就得到了总记录数然后我们就可以把这个总记录数立即封装到什么呀配置view对象里因为咱配view里边是要这个总记录数的然后呢我们再调这个对象的一个get hit方法得到那个什么呀他是封装成一个数组了search hit他是把这个大家看这
[08:40] 他是把这个查出来的每一个文档这个数据或者也就是一行记录吧是封装成什么呀封装成30 hit这个对象然后呢反而给我们的是一个数据不是集合你说呢这儿呢其实就是拿到了我们查出来的这个数据啊上面这是总记录数拿到这个数据之后呢我们要编辑这个数据从这里边取出来我们想要的数据啊因为你看他反而的这个数据是非常多啊这么多字段对不对
[09:07] 那我们不一定全要所以这里边你要啥你就挑啥呗一个一个取出来然后封装成DTO对象然后再把DTO对象存到这个谁啊对集合里边这是我们整个完成了这个封装啊这块代码呢咱之前也说过这儿呢我就不再一点一点给大家编写了这块我就直接拿过来用了那就是从这开始是不是一直到哪一直到这就是六和七六和七这一块那这里边
[09:43] 呃更详细的这个代码呢咱一起过一遍这块我刚才给大家说过了对不对我们重点说这个循环循环里边它是这样子的啊因为这里边呃你取出来的数据呢基本上都是先作为字部串去使用的然后呢你还要做相应的类型转换因为在DTO对象里边呢它每个属性都是有不同的这个对数据类型那咱接下来一起看一下
[10:14] 咱整个代码从上往下过一遍这是不是缺一个大我号然后呢我们就便利这个什么样数组啊便利的时候呢取出来的就是每一个都是47 hit对象啊这里边呢其实封装就是里边的每一个文档或者每一行数据这些数据我们最终是不是要存到dq对象里面随着这呢我每次都新建一个对象然后呢我们要把这个hit转换成一个什么map集合啊他有个方法叫get source as map然后呢我们就调用这个集合的get方法
[10:45] 根据这个字段名去相应的这个值去除下值之后你要做相应的类型转换当然你要看这个DTO对象里边它那个属性是啥类型你就转换成啥类型转换完之后呢就开始掉set的方法往DT对象里边开始存储存完之后呢把这个对象放到对List的集合里边整个这个循环封装DTO就完事这个代码比较多但是其实这个不难啊这个东西那整个这块我们全部搞定之后呢最终
[11:19] 就是我们要封装成什么呀配给view对象然后返回就行这个配给view对象的话我们是不是在前面已经创建过了对吧创建过的话在哪个地方我封装了一个数据在这我是把总记录算给封装除了要封装总记录算还要封装啥那还要封装啥你去这里边瞅一眼不就知道了这不总记录算吗然后就是那个集合吧那刚才一个然后就是这个分页数据那你在这又调用他的setter方法就行了
[11:51] 那就是配几Vo我们先放那个什么呀集合吧叫set content是不是咱上面的这个list吗对不对然后呢再把分页的数据也放进去配一size配一size就是配一size还有配几number配几number是吧这就封装到配几Vo里边了然后封装完之后这是我们最终想要的东西吗直接把它返回就行
[12:34] 然后上面这个catch这一块的话我们这样子吧我们做这么一个处理就一趟闹出问题了出问题了我就反而一个空嘛那这是咱们把整个这个实现类当中的代码就全部编写完了啊比较多我们一共分成了几个步骤啊八个步骤那么大家下去写代码的时候你也是啊先分成八个步骤啊整体先想一想想好了之后想清楚了之后呢我们再
[13:04] 一点一点去编写代码编写代码时候呢大家可以参考参考这个讲义因为这个API呢咱好久没有使用了啊所以你可以参考一下讲义慢慢把这个代码写出来就行了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中使用 Elasticsearch 的 SearchSourceBuilder 构建查询条件、设置排序和分页参数，并将搜索结果封装为 PageVO 对象返回。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 ProjectIndexServiceImp.java 文件中构建 QueryBuilder 的代码，用于处理项目名称和时间段的查询条件。
画面 2: 展示创建 SearchSourceBuilder 对象并设置查询条件的代码。
画面 3: 展示设置排序参数的代码，根据 sortBy 和 order 字段决定升序或降序。
画面 4: 展示设置分页参数的代码，包括 from 和 size。
画面 5: 展示执行搜索请求的代码，使用 restHighLevelClient。
画面 6: 展示获取搜索结果并封装为 PageVO 对象的代码。
画面 7: 展示获取搜索结果的总记录数并设置到 PageVO 中。
画面 8: 展示遍历搜索结果并封装为 ProjectDTO 对象的代码。
画面 9: 展示将 ProjectDTO 对象添加到列表中。
画面 10: 展示捕获异常并返回 null 的代码。
画面 11: 展示封装为 PageVO 对象并返回的代码。
画面 12: 展示 PageVO 类的结构，包括 pageNo、pageSize、content、total 等属性。
画面 13: 展示设置分页参数的代码。
画面 14: 展示封装为 PageVO 对象并返回的代码。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
if(StringUtils.isNotBlank(projectQueryParamsDTO.getNames()) {
    queryBuilder.must(QueryBuilders.termQuery("name", projectQueryParamsDTO.getNames()));
}
if(projectQueryParamsDTO.getStartPeriod() != null) {
    queryBuilder.must(QueryBuilders.rangeQuery("period").gte(projectQueryParamsDTO.getStartPeriod()));
}
if(projectQueryParamsDTO.getEndPeriod() != null) {
    queryBuilder.must(QueryBuilders.rangeQuery("period").lte(projectQueryParamsDTO.getEndPeriod()));
}
```

画面 2:
```java
//3. 创建SearchSourceBuilder对象
SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
//3.1 封装条件
searchSourceBuilder.query(queryBuilder);
//3.2 设置排序参数
```

画面 3:
```java
//3.2 设置排序参数
if(StringUtils.isNotBlank(sortBy) && StringUtils.isNotBlank(order)) {
    if(order.toLowerCase().equals("asc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.ASC);
    }
    if(order.toLowerCase().equals("desc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.DESC);
    }
} else {
    searchSourceBuilder.sort("createdate", SortOrder.DESC);
}
//3.3 设置分页参数
searchSourceBuilder.from((pageNo - 1) * pageSize);
searchSourceBuilder.size(pageSize);
```

画面 4:
```java
//3.2 设置排序参数
if(StringUtils.isNotBlank(sortBy) && StringUtils.isNotBlank(order)) {
    if(order.toLowerCase().equals("asc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.ASC);
    }
    if(order.toLowerCase().equals("desc")) {
        searchSourceBuilder.sort(sortBy, SortOrder.DESC);
    }
} else {
    searchSourceBuilder.sort("createdate", SortOrder.DESC);
}
//3.3 设置分页参数
searchSourceBuilder.from((pageNo - 1) * pageSize);
searchSourceBuilder.size(pageSize);
```

画面 5:
```java
//4. 完成封装
searchRequest.source(searchSourceBuilder);
```

画面 6:
```java
//6. 获取搜索的结果
//7. 封装为PageVO对象并返回
PageVO<ProjectDTO> pageVO = new PageVO<>();
```

画面 7:
```java
//5. 执行搜索
List<ProjectDTO> list = new ArrayList<>();
PageVO<ProjectDTO> pageVO = new PageVO<>();
try {
    SearchResponse searchResponse = restHighLevelClient.search(searchRequest, RequestOptions.DEFAULT);
    //6. 获取搜索结果
    SearchHits hits = searchResponse.getHits();
    long totalHits = hits.getTotalHits().value;
    pageVO.setTotalTotalHits(totalHits);
    //7. 遍历并封装DTO
    for (SearchHit hit : searchHits) {
        ProjectDTO projectDTO = new ProjectDTO();
        Map<String, Object> sourceASMap = hit.getSourceAsMap();
        Double amount = (Double) sourceASMap.get("amount");
        String projectStatus = (String) sourceASMap.get("projectstatus");
        Integer period = Integer.parseInt(sourceASMap.get("period").toString());
        String name = (String) sourceASMap.get("name");
        String description = (String) sourceASMap.get("description");
        projectDTO.setAmount(new BigDecimal(amount));
        projectDTO.setProjectStatus(projectStatus);
        projectDTO.setPeriod(period);
        projectDTO.setName(name);
        projectDTO.setDescription(description);
        list.add(projectDTO);
    }
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
//8. 封装为PageVO对象并返回
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
```

画面 8:
```java
//5. 执行搜索
List<ProjectDTO> list = new ArrayList<>();
PageVO<ProjectDTO> pageVO = new PageVO<>();
try {
    SearchResponse searchResponse = restHighLevelClient.search(searchRequest, RequestOptions.DEFAULT);
    //6. 获取搜索结果
    SearchHits hits = searchResponse.getHits();
    long totalHits = hits.getTotalHits().value;
    pageVO.setTotalTotalHits(totalHits);
    //7. 遍历并封装DTO
    for (SearchHit hit : searchHits) {
        ProjectDTO projectDTO = new ProjectDTO();
        Map<String, Object> sourceASMap = hit.getSourceAsMap();
        Double amount = (Double) sourceASMap.get("amount");
        String projectStatus = (String) sourceASMap.get("projectstatus");
        Integer period = Integer.parseInt(sourceASMap.get("period").toString());
        String name = (String) sourceASMap.get("name");
        String description = (String) sourceASMap.get("description");
        projectDTO.setAmount(new BigDecimal(amount));
        projectDTO.setProjectStatus(projectStatus);
        projectDTO.setPeriod(period);
        projectDTO.setName(name);
        projectDTO.setDescription(description);
        list.add(projectDTO);
    }
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
//8. 封装为PageVO对象并返回
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
```

画面 9:
```java
//7. 遍历并封装DTO
for (SearchHit hit : searchHits) {
    ProjectDTO projectDTO = new ProjectDTO();
    Map<String, Object> sourceASMap = hit.getSourceAsMap();
    Double amount = (Double) sourceASMap.get("amount");
    String projectStatus = (String) sourceASMap.get("projectstatus");
    Integer period = Integer.parseInt(sourceASMap.get("period").toString());
    String name = (String) sourceASMap.get("name");
    String description = (String) sourceASMap.get("description");
    projectDTO.setAmount(new BigDecimal(amount));
    projectDTO.setProjectStatus(projectStatus);
    projectDTO.setPeriod(period);
    projectDTO.setName(name);
    projectDTO.setDescription(description);
    list.add(projectDTO);
}
```

画面 10:
```java
} catch (Exception e) {
    e.printStackTrace();
    return null;
}
```

画面 11:
```java
//8. 封装为PageVO对象并返回
pageVO.setContent(list);
pageVO.setPageSize(pageSize);
```

画面 12:
```java
public class PageVO<T> {
    private Integer pageNo;
    private Integer pageSize;
    private List<T> content;
    private Long total;
    private Integer totalTotalHits;
    private Integer totalPages;
    private String status;
    private String message;
    private String code;
    private String url;
    private String method;
    private String request;
    private String response;
    private String ip;
    private String userAgent;
    private String referer;
    private String xForwardedFor;
    private String xRealIp;
    private String xRequestedWith;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String xFrameOptions;
    private String xXSSProtection;
    private String xContentTypeOptions;
    private String

