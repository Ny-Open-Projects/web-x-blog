# 画面线理解：14.轮播广告实现之前后端整合测试

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\14.轮播广告实现之前后端整合测试【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:03, 00:42, 01:01, 01:21, 01:36, 02:37, 02:48, 03:14, 03:50, 04:39, 05:02, 05:45, 06:09, 06:50
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 21:15:21

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
