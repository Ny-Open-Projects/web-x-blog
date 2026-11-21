# 14.轮播广告实现之前后端整合测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\14.轮播广告实现之前后端整合测试【海量资源尽在 ubkz.com】.mp4
- 时长 6分52秒（音频 412s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来做一下测试啊呃刚刚呢在我启动的过程中啊发现呢呃启动呢启动之后是可以的但是呢请求不到数据啊请求不到数据为什么呢原因是呢是刚刚我们在写代码的时候有一个点啊写的可能当时没注意啊写错了就在这个位置那我们去引入我们的double的一个服务的时候这个是Watson啊当时敲错了这个位置啊大家一定要注意啊这个也指定是Watson啊
[00:27] 刚刚当时敲的是这个validate就是做成敲成一个校验了都是V开头的刚才写代码没太注意然后我们把它改成一个Warsen之后启动就没有任何问题了然后我们进行做一个测试走那么可以看这个地址就是这样的一个地址对吧AD这个地址然后get请求然后没有参数然后它返回的数据就是这样的一个数据可以看到跟我们所要求或者说期望的一个数据结构
[00:56] 是不是一模一样啊OK好那么也希望大家呢能够掌握这种我们刚刚去分装这个webwebreductor这样的一个一种思想就是你最终所看到的这个响应的一个结果跟我们的一个对象加上对象的一个结构啊不一定要一致啊不一定一致可以通过我们的json一些这个enclose来控制一些哪些进行响应哪些不做响应啊OK
[01:25] 好 那么接下来我们就来整合我们的前端的一个系统我们来看一下那么我们打开我们的前端的系统在前端系统中我们去进我们的home这个页面中然后他所请求的是不是这个地址对吧那么我们这样咱们给他去去把这个去改一下我们做一个注释然后把这个地址我直接把它贴过来就是我们这个地址
[01:52] 那么当然了我这样一贴肯定有同学就会去想前面的我们在讲这个他的流程的时候我们说过这个地址在最终请求的时候会去前面再加一个这个base url对不对那么当我在这个位置给他添加这样的一个地址的时候他还是否会给我前面再增加一个啊这个base url呢其实是不会的因为呢这个axi os这个
[02:22] 组件呢他呢会做一个判断就说你这个URL他本身呢是一个绝对路径的话就不再添加前面的base URL了这样的话大家就放心了是吧好那么我们就可以来刷新页面来看一下这个效果了到这个里面我们来刷新一下走看他是否能够啊能够去查询到我们的数据呢很遗憾并没有查询到为什么呢来看一下
[02:50] 那么显然我们可以看到它是不是有一个403的这样的一个错误OK那么就是说我们的服务端没有去支持CORS其实就是我们跨域那么我们并没有在我们的刚刚写的AD的Controller中给它开启一个跨域的支持我们给它开启一下这个我简单的提一下我相信大家应该也
[03:18] 也懂啊也懂这个跨域啊就是说我们现在的这个前端的是在9000这个端口而我们的服务呢是在118080这个端口那么这个显然会有一个跨域的一个问题那么解决跨域呢有两种解决方案第一种解决方案呢就是我们采用JSNP的方案第二种方案呢就是这种CORS的这种方案那么而这个
[03:45] AXLS它所采用的是第二种方案就是这个CORS一种方案所以我们需要服务端对它做一个支持而在Springboard中在Spring中或者在Spring MVC里面对一个CORS的一个跨域支持非常简单你直接去写一个CORSS这样的一个注解就可以了OK加一个这样的注解那么它就支持这样的一个
[04:15] 跨域请求了那么究竟什么是这个CLSS那么这个也希望大家如果不太了解的同学那么自行去学习一下那么我在这就不再去做展开了这个应该属于一个比较基础的一个知识好那么下面我们对我们这个服务给它做一个重启我们再来做一个测试OK好那么我们等待它的一个启动那么我们先把这个视频先暂停一下
[04:45] 好那么我们现在呢重启好了但是呢我们经过测试呢发现依然是有问题的因为他之前呢发起的是一个post请求对不对你可以看到啊这个位置一个post请求所以呢我们要去改一下啊那么我们希望他发起的是一个get请求啊这个点错了啊这个位置要发起一个get请求不要发起post请求了因为我们服务端支持的是一个get请求所以呢我们再来测试一下
[05:15] 你发现这个时候是不是就拿到数据了那么其中我们可以看一下他的一个请求那么请求的时候他首先要发起一个opposite是这样的一个请求就去询问服务端就说我要去跨域get请求你的数据你允许不允许呢ok那么现在他的响应的就是说允许的方法是有这么多对吧ok允许的方法是get允许的方法是get的
[05:42] 那么下面的就可以去做一个具体请求了你可以看到下面的就会找到一个AD那么他就去做一个get这样的请求就会拿到我们的一个数据了OK就这样的一个逻辑那么这样的话我们是不是就成功的去访问到我们这个数据了是吧OK好嘞好那么现在我们是不是就相当于什么呢前后端我们是不是做一个整合开发的时候是不是现在已经就OK了对吧
[06:08] OK好那么要注意的是在这个位置呢首先第一个我们设置一个绝对的一个路径然后呢我们要把它改进get请求OK好的我们暂时呢先以这样的方式先做一个编写到后面呢我们再做一些统一的一个处理啊OK好那么这样的话就搞定了那么刚刚是不是我们也看到对cos呢并没有做一个支持所以我们需要服务端的添加这样的一个注解去给他去做一个支持好嘞好那么可以看到最终我们的一个
[06:38] 是不是就成功的去获取到我们这个数据了OK好那么关于我们前后端整合去实现我们的一个首页的一个轮播的这样的一个广告的功能呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过修改前端 JavaScript 代码，将原本调用本地 API 的请求改为调用后端服务（127.0.0.1:18080）的跨域请求，以实现前后端系统的整合。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 PDF 文档中“3.4.5、测试”章节，内容为 Java 代码片段，定义了 getMeta 方法，用于返回包含 msg 和 status 的 Map。
画面 2: 展示 Advanced REST Client 工具中一个 GET 请求的响应，状态码为 200，响应头包含 Content-Type 和 Date。
画面 3: 展示 IntelliJ IDEA 中的项目结构和 AdService.java 代码，其中 AdService 类通过 @Reference 注解注入了 apiAdService，并定义了 queryAdList 方法。
画面 4: 展示 WebResult.java 代码，其中定义了静态方法 ok 和 getData，用于构建返回结果。
画面 5: 展示 home.js 文件中的 JavaScript 代码，其中定义了 swipe、menu、info 三个 Promise，分别用于异步请求 /homes/swipe、/homes/menu、/homes/info。
画面 6: 展示浏览器中本地服务器（localhost:9000/home）的页面，显示一个绿色的 Carousel 组件。
画面 7: 展示浏览器开发者工具 Network 面板，显示了对 /ad 的请求，响应状态码为 200。
画面 8: 展示 AdController.java 代码，其中定义了 @RequestMapping("ad") 和 @GetMapping 注解的 queryIndexAd 方法。
画面 9: 展示浏览器开发者工具 Network 面板，显示了对 /ad 的请求，响应状态码为 200。
画面 10: 展示 AdController.java 代码，其中添加了 @CrossOrigin 注解，用于支持跨域请求。
画面 11: 展示 home.js 文件中的 JavaScript 代码，其中将 axios.post 的 URL 从 /homes/swipe 修改为 http://127.0.0.1:18080/ad。
画面 12: 展示浏览器开发者工具 Network 面板，显示了对 http://127.0.0.1:18080/ad 的 OPTIONS 请求，响应头包含 Access-Control-Allow-Origin 等 CORS 相关信息。
画面 13: 展示 PDF 文档中“4.5、整合前端系统”章节，内容为修改 home.js 文件中请求地址的代码示例。
画面 14: 展示浏览器中本地服务器（localhost:9000/home）的页面，显示了整合后的完整前端页面，包含轮播图和多个功能按钮。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public Map<String, Object> getMeta() {
    HashMap<String, Object> meta = new HashMap<String, Object>();
    meta.put("msg", this.msg);
    meta.put("status", this.status);
    return meta;
}
```

画面 3:
```java
@Service
public class AdService {
    @Reference(version = "1.0.0")
    private ApiAdService apiAdService;

    public PageInfo<Ad> queryAdList(Integer type, Integer page, Integer pageSize) {
        return this.apiAdService.queryAdList(type, page, pageSize);
    }
}
```

画面 4:
```java
@JsonIgnore
private Integer status;
@JsonIgnore
private String msg;
@JsonIgnore
private List<?> list;

public static WebResult ok(List<?> list) {
    return new WebResult(status: 200, msg: "成功!", list);
}

public static WebResult ok(List<?> list, String msg) {
    return new WebResult(status: 200, msg, list);
}

public Map<String, Object> getData() {
    Map<String, Object> map = new HashMap<>();
}
```

画面 5:
```javascript
let swipe = new Promise(resolve, reject) => {
    axios.post('/homes/swipe').then((data) => {
        resolve(data.data.list);
    });
};

let menu = new Promise(resolve, reject) => {
    axios.post('/homes/menu').then((data) => {
        resolve(data.data.list);
    });
};

let info = new Promise(resolve, reject) => {
    axios.post('/homes/info').then((data) => {
        resolve(data.data.list);
    });
};
```

画面 8:
```java
@RequestMapping("ad")
@RestController
public class AdController {

    @Autowired
    private AdService adService;

    @GetMapping
    public PageInfo<Ad> queryIndexAd() {
        List<Ad> records = adPageInfo.getRecords();
        return adPageInfo;
    }
}
```

画面 10:
```java
@RequestMapping("ad")
@RestController
@CrossOrigin
public class AdController {

    @Autowired
    private AdService adService;

    @GetMapping
    public PageInfo<Ad> queryIndexAd() {
        List<Ad> records = adPageInfo.getRecords();
        return adPageInfo;
    }
}
```

画面 11:
```javascript
let swipe = new Promise(resolve, reject) => {
    axios.post('http://127.0.0.1:18080/ad').then((data) => {
        resolve(data.data.list);
    });
};

let menu = new Promise(resolve, reject) => {
    axios.post('http://127.0.0.1:18080/ad').then((data) => {
        resolve(data.data.list);
    });
};

let info = new Promise(resolve, reject) => {
    axios.post('http://127.0.0.1:18080/ad').then((data) => {
        resolve(data.data.list);
    });
};
```

画面 13:
```javascript
let swipe = new Promise(resolve, reject) => {
    axios.post('/homes/swipe').then((data) => {
        resolve(data.data.list);
    });
};

let menu = new Promise(resolve, reject) => {
    axios.post('/homes/menu').then((data) => {
        resolve(data.data.list);
    });
};

let info = new Promise(resolve, reject) => {
    axios.post('/homes/info').then((data) => {
        resolve(data.data.list);
    });
};
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: PDF 文档标题为“3.4.5、测试”，左侧目录结构显示了章节“3.4.5、测试”。
画面 13: PDF 文档标题为“4.5、整合前端系统”，内容为“修改 home.js 文件中请求地址：”，并附有代码示例。
画面 14: 无 PPT 标题或架构图。

5) 不要评价画面美观，不要输出与课程无关的内容。

