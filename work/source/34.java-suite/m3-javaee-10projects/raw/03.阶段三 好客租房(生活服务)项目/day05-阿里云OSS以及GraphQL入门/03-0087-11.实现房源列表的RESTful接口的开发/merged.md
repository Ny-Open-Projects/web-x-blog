# 11.实现房源列表的RESTful接口的开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\11.实现房源列表的RESTful接口的开发【海量资源尽在 ubkz.com】.mp4
- 时长 9分8秒（音频 548s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现RESTful这个接口啊那么我们在API server这个工程中呢我们去做一个实现那么导入这个依赖啊这两个依赖呢在我们前面讲的过程中啊其实已经导进去了对吧所以呢我们就不做一个导入了下面我们来编写我们的Controller那么咱们把这个代码把这个代码贴过来吧这个也是一个比较简单的一个代码啊我们来贴过来来看一下
[00:26] 那么我们进入到我们这个工程中进入到我们前面这个API这个Service的工程中来看一下在这个里面在这个里面找到我们写这个Controller然后在这个Controller中去把这个方法我们靠进来靠到这个位置好那么现在我们已经考过进来了考过进来之后会有点报错报两个错误第一个是它的响应的对象叫做table without
[00:55] 那么这个对象呢我们现在并没有所以我们需要创建一个这样的一个对象那么还有一个呢是Service中缺少这样一个方法那么这样咱们一个一个来解决这个问题啊那么首先第一个问题呢就是呃这个table result啊这个对象啊是哪来的呢那其实这个是我们自己去定义的一个对象而这个对象的结构它呢其实是要参考于我们的这个antDirant啊antDirant呃它中的一个table
[01:24] 然后呢去响应的一个数据结构去做这样的一个参考啊那么咱们就不去看他这个文档了啊那么我们就去来看一下我们的一个实现啊那么在我们的这个VO这个包下面呢我们创建一个table result这个对象它呢有两个属性一个是list那么显然去所存放的就是我们的一个列表就是我们数据的列表还有一个对象呢叫做
[01:52] Pager,PagerAscent那么就是去存放我们的一些分页相关的一些信息而这个又是一个对象又是我们自定义的一个对象这个对象中又会有三个属性一个叫Character就是我们当前的一个页数然后一个PageSize每页显示的大小Total就是我们的总的一个页数那么OK那么我们来看一下那么我们接下来把这个来创建出来首先先进入我们的工程
[02:21] 看一下这个下面的view并没有这个类我们咱们把这个类创建出来这个类就叫什么叫tableResult好那么把它创建出来可以看到这样的一个实现对吧好那么这个就是我们左边写的一个tableResult这样的一个类那么它还缺少一个PageAscent这样的一个对象但是你发现它已经导入进来了但是它导入这个类它不对不应该导入这个包
[02:51] 把它删掉那么他会报错那么接下来呢我们把这个类呢也拷过来配置H的这个类拷过来放到Viu这个包下面去那么在这个里面呢其实我们可以看到他呢是不是有三个这样的属性并且呢也都加了这个Data这样的一个注解那么我们就可以在这个里面说把这个table result是不是就
[03:13] 导入进来了哎OK好那么这样导入进来之后呢我们刚刚看到的第一个问题就解决了那么下面第二个问题呢就是在这个Service中啊它并没有这样的一个query list方法那么怎么办呢给它去创建一个啊这个方法OK那么这个方法它的返回值我们来看一下它的返回值其实要求我们返回这个table result对吧把它改成table result那么这个t是谁呢显然是我们那个host resource是不是这个对象啊哎OK
[03:43] 好那么我们去这样去写好没有问题好嘞那么这样的话我们这Controller是不是就写好了把这个代码的格式呢去简单的去调一下这个显然这样不太好看对吧去调一下那我们来看一下这个方法那么这个方法呢它呢接收三个参数啊一个就是我们这个查询的一个对象还有一个呢就是我们的一个当前的一个页索curric的page还有叫做page size
[04:11] 那么这两个的参数的参数名那么其实是要去参考我们的前端的这个按照底站中的所传递的这个参数名是不是做这样的一个参考对吧然后呢我们通过它来去设置我们这样的一个参数名哎呀OK好那么我们这样的话呢是不是就实现了一个Controller的一个编写那么接下来我们就要去实现在这个在我们的这个Service中的一个实现
[04:39] 而在这个Service中呢他呢其实要调用我们的double的这个API去做一个查询是不是通过query这个list对吧然后呢传递啊这么几个参数那么三个参数第一个参数呢把我们这个pager是不是当前页数是不是传递过去第二个参数呢就是我们的pager set第三个参数呢就是我们的查询的一个条件对吧那么把这个查询条件是不是也给他传递过去
[05:05] 那么它所返回的一个对象我们来看一下它其实是一个叫配置info这样的一个对象那么我们就需要是不是通过这个配置info这个对象把它做一个回车通过一个这样把这个点也回车一下那效果是一样的那就这样就这样好了然后我们通过这个配置info这个对象需要去构造一个我们这个table园的对象对吧所以我们需要在这个位置去
[05:34] new一个什么呢叫table result这样的一个对象那么table result我们来看它是不是需要有两个有两个这样的一个属性那我们来给它构造一下那么第一个属性呢就是list那么通过这个配置info点get什么recode然后第二个呢参数呢需要的一个配置配置info这样的配置ation这样的一个对象那么所以我们需要给它去new这样的一个对象去new一个
[06:04] Page,Vision这样的对象那么这个对象呢又需要去做一个我们做一个这个做一个这样的一个构造那么三个参数的构造那么第一个参数我们来看一下就是current第二个PageSize第三个是total所以我们给他来设置一下第一个参数第一个参数的是current就是我们现在写传递的currentPage这个对象
[06:29] 第二个参数呢就是我们的这个PageSet第三个参数呢就是我们的这个Total对吧通过这个PageInfo去get什么呢Total拿到这样的一个数据就可以了是不是就可以去得到我们一个叫tableResult这样的一个对象哎OK这样的话是不是就实现了我们的control的一个编写那么接下来呢我们就需要把我们这个API这个server呢做一个重启然后呢我们去
[06:59] 将他的我们这个所编写的这个接口啊我们就做一个调试啊做一个测试看他是否能够实现这样的一个查询那个结果好嘞那么我们这个等待他的一个启动啊OK那么我们先把视频的暂停一下好那么我们继续啊那么我们现在这个服务呢已经启动起来了我们来测试一下那么依然的还是打开我们的restclient然后呢在这个里面的我们去做一个调试那么
[07:28] 我们来找一下吧是不是就是这样的一个请求啊那我们把这个页数呢改成1那么去发起一个什么请求哎呃错了一块身上发起一个get请求好点击它send发送好那我们可以看到是不是已经查询到我们这个数据了那么可以看到这个concern这个精密房源这个数据呢其实是我们最后查询的数据那么也就是说他是不是已经做了一个
[07:56] 倒序的一个这样的一个排序把最新的数据是不是给我们返回了那么总数据总条数是9条每页显示的是两条所以我们的总页数是总页数这个没显示出来对吧然后我们会一直去做一个分页那么当然你通过这个数据的总条数然后去和我们这个PageSize去做一个计算是不是就能够得出我们的一个总页数OK那我们尝试一下设置为2
[08:25] 那么去发送那么可以看到是不是这样的一个数据那么答案你改成这个三是不是可以继续往下面去做一个分页OK好那么显然我们现在是不是查询一个列表这个功能我们是不是就搞定了好那么我们来看一下我们的这个讲义在这个讲义中我们来看一下这个Service的实现那么这个实现的过程是不是刚刚跟我们去写这个代码的实现是一样的
[08:49] 好嘞,那么做一个测试会发现分叶这个效果是不是已经搞定了那么也就是说我们现在的一个房源列表这个功能就搞定了那么其实我们接下来要做的事情就是去整合我们的前端去做一个开发好,那么关于我们rest4接口的开发我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中实现 RESTful 接口，包括控制器编写、服务层实现、分页结果封装及接口测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为在 itcast-haoke-manage-api-server 工程中导入依赖（joda-time）和编写 Controller。
画面 2: 展示 HouseResourcesController.java 文件，其中定义了 @GetMapping 注解的 list 方法，用于查询房源列表，参数包括 houseResources、currentPage 和 pageSize。
画面 3: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为编写 TableResult。
画面 4: 展示项目结构，选中了 TableResult.java 文件，其内容为一个泛型类，包含 List<T> list 和 Pagination pagination 两个私有属性。
画面 5: 展示 HouseResourcesController.java 文件，高亮显示了 @GetMapping 注解的 list 方法。
画面 6: 展示 HouseResourcesController.java 文件，高亮显示了 @GetMapping 注解的 list 方法。
画面 7: 展示 HouseResourcesService.java 文件，高亮显示了 queryList 方法，该方法调用 apiHouseResourcesService 的 queryHouseResourcesList 方法。
画面 8: 展示 HouseResourcesService.java 文件，高亮显示了 queryList 方法，该方法调用 apiHouseResourcesService 的 queryHouseResourcesList 方法。
画面 9: 展示 HouseResourcesService.java 文件，高亮显示了 queryList 方法，该方法调用 apiHouseResourcesService 的 queryHouseResourcesList 方法，并返回 new TableResult<>(pageInfo.getRecords(), new Pagination())。
画面 10: 展示项目运行日志，显示 DubboApplication 启动成功，以及 Tomcat 服务启动。
画面 11: 展示 Advanced REST Client 浏览器插件界面，准备发送 HTTP 请求。
画面 12: 展示 Advanced REST Client 浏览器插件界面，显示了返回的 JSON 数据，包含房源信息。
画面 13: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为 Service 实现部分，展示 queryList 方法的实现。
画面 14: 展示课程讲义 PDF 中“5.4. 实现 RESTful 接口”章节，内容为测试部分，展示返回的 JSON 数据，包含房源信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <version>1.18.4</version>
</dependency>
<dependency>
    <groupId>joda-time</groupId>
    <artifactId>joda-time</artifactId>
    <version>2.9.9</version>
</dependency>
```

画面 2:
```java
return ResponseEntity.status(HttpStatus.INTERNAL_SERVER_ERROR).build();

/**
 * 查询房源列表
 * @param houseResources
 * @param currentPage
 * @param pageSize
 * @return
 */
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage",
        defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize",
        defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面 4:
```java
package cn.itcast.haoke.dubbo.api.vo;
import ...
@AllArgsConstructor
public class TableResult<T> {
    private List<T> list;
    private Pagination pagination;
}
```

画面 5:
```java
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage",
        defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize",
        defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面 6:
```java
@GetMapping
@ResponseBody
public ResponseEntity<TableResult> list(HouseResources houseResources,
        @RequestParam(name = "currentPage",
        defaultValue = "1") Integer currentPage,
        @RequestParam(name = "pageSize",
        defaultValue = "10") Integer pageSize) {
    return ResponseEntity.ok(this.houseResourcesService.queryList(houseResources, currentPage, pageSize));
}
```

画面 7:
```java
@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }

    public TableResult<HouseResources> queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
        this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
        return null;
    }
}
```

画面 8:
```java
@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }

    public TableResult<HouseResources> queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
        PageInfo<HouseResources> pageInfo = this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
        return null;
    }
}
```

画面 9:
```java
@Service
public class HouseResourcesService {
    @Reference(version = "1.0.0")
    private ApiHouseResourcesService apiHouseResourcesService;

    public boolean save(HouseResources houseResources) {
        int result = this.apiHouseResourcesService.saveHouseResources(houseResources);
        return result == 1;
    }

    public TableResult<HouseResources> queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
        PageInfo<HouseResources> pageInfo = this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
        return new TableResult<>(pageInfo.getRecords(), new Pagination());
    }
}
```

画面 13:
```java
public TableResult queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) {
    PageInfo<HouseResources> pageInfo = this.apiHouseResourcesService.queryHouseResourcesList(currentPage, pageSize, houseResources);
    return new TableResult(pageInfo.getRecords(), new Pagination(currentPage, pageSize, pageInfo.getTotal()));
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 3: PPT 标题为“5.4. 实现 RESTful 接口”，内容为“编写 TableResult”。
画面 13: PPT 标题为“Service 实现”，内容为“public TableResult queryList(HouseResources houseResources, Integer currentPage, Integer pageSize) { ... }”。
画面 14: PPT 标题为“测试”，内容为“返回的 JSON 数据”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

