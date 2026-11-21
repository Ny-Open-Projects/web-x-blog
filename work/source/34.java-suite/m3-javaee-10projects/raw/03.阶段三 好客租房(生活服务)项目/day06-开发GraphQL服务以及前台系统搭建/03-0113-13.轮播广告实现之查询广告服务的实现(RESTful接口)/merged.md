# 13.轮播广告实现之查询广告服务的实现（RESTful接口）

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day06-开发GraphQL服务以及前台系统搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day06-开发GraphQL服务以及前台系统搭建\13.轮播广告实现之查询广告服务的实现（RESTful接口）【海量资源尽在 ubkz.com】.mp4
- 时长 19分50秒（音频 1191s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现API接口的服务当然这个我们实现的是RESTful的一个接口那么我们就要回到我们的这个API的这个server这个工程呢那么整理一下那么是在这个里面那么首先呢我们要给它去引入一个依赖那么什么依赖呢就需要把我们的这个AD的这个interface这个依赖引用进来要不然你调用不了对不对那么我们就调到这OK
[00:29] 这样的话呢我们就把这个ad下面interface引入到我们这个工程里面来那么下面呢我们是不是就可以做具体的实现了对吧好那么我们可以在这个位置啊我们这样来编写那么我们先写这个Service那么这个Service呢我们是不是应该这样去写写一个叫做ad Service这个Service首先把它标记为是一个我们的一个Service对吧
[00:57] 就是我们的一个Spring的一个Service然后在这个里面我们需要去注入一个叫做api ad Service这个是double所提供的一个服务我们把它refresh去refresh去引入进来那么引入的是这个包然后我们指定它的一个werson是多少1.0.0
[01:26] 这个要和我们所写的 ad服务中的接口的定义在下面 Service里面我们来找一下它的一个定义这个一定要一致要不然的话是有问题的是肯定是拿不到的它的一个版本号好然后我们进入 ad Service那么下面我们是不是要去查询一个查询我们的一个
[01:55] adlist对吧那么我们返回呢就返回这个pager infopager infot呢就是我们这个ad这个数据然后呢就叫query adlist那么它需要几个参数呢是不是需要有三个参数对吧第一个呢就是我们的这个什么呢叫type就是你的这个广告的类型那第二个呢就是pager第三个呢就是pagerpagesizepagesize
[02:24] 然后我们是不是就可以returnreturn谁呢race.api.idservice.querylist把这三个参数给它传递过去是不是就可以了page然后page sizeok好这样的话是不是就实现了一个我们在API这个工程中的一个调用是不是调用我们double所提供的这样的一个服务ok好那么我们现在这个是不是API Service就搞定了
[02:53] ad Service搞定了那么下面我们来写一个control因为我们现在要写的是不是提供的rest for的一个接口所以我们写一个ad control那么ad control呢我们首先把它标记为呢这是一个就叫rest control吧rest control啊ok那么这样写了rest control之后就省了我们再去下面写那个response body了啊然后呢我们写一个requestrequestmapping
[03:24] 然后我们写一个名字就叫路径就叫ad好那么下面我们就可以在这个位置在这个位置我们去写具体的一个实现那么public public返回值返回什么对吧这个我们需要一起来探讨一下然后我们要查询什么查询的是不是就是叫做query index ad就是我们首页的
[03:53] 广告对不对那么我们给他去标明这是一个什么请求呢是不是get请求对吧get请求然后呢他有没有参数呢他没有参数是不是直接去做一个查询啊就可以了好那么在这个里面我们怎么样去查询呢显然我们是不是需要调用我们刚刚所写的这个ad Service去做一个查询那么ad Service把这个ad Service呢去注入进来
[04:20] 然后在这个里面我们是不是就可以调用this.adservice.queryadlist那么这三个参数传递一下那我们来看一下我们的数据那我们的数据所有type都是1对不对那么也就意味着我们首页的一个轮播广告它的type就是1然后它的配置我们设置为是1它的配置赛页我们设置为3我们查询三条数据那么它所返回的就是一个叫pager info那么我们通过pager info
[04:49] 是不是就可以拿到我们的一个数据啊哎OK好那么到这儿我们基本上呢我们就已经把这个基本的一些这个逻辑写好了接下来我们就来看一下我们该如何去返回这个数据那么我们想要去正确的返回数据那我们就需要去看一下前端所要求的这个数据结构那么这个数据结构相对而言呢还是一个稍微复杂一点点的这个
[05:19] 结构啊那么我来找一个工具啊在这个里面有个叫做jsonville的工具啊jsonville的工具我们把这个打开来看一下jsonville的工具是这样的一个结构啊这样的一个结构那么在这个结构中呢我们可以看到它最呃最外面是一个对象对吧来看一下啊最外面这个是个对象然后呢对象中的有两个属性一个date叫matter还有呢这个date下面的又是一个对象
[05:49] 对象中的又有一个listlist又是一个宿主又是宿主或者是集合下面又是一个对象对象里面的又包含一个adj这样的一个url地址然后下面这个meta里面又有一个对象又有这两个属性相对还是比较复杂的一个这样的一个对象那么这个对象我们又该如何去做一个分装一个返回呢大家可以去
[06:17] 考虑一下如果说我们按照这个结构去创建对象的话那么我们会创建几个对象呢来看一下首先第一个外面这个对象是一个对象对吧第二个是这个是不是一个对象两个对象然后呢这个matter是不是一个对象是不是三个对象对应的类似中的这个对象是不是需要创建四个对象哎呀OK这个是相对比较复杂的那么其实我们可以分析一下在这个结构中
[06:44] 他真正其实我们需要给他返回或者说真正我们需要去处理的一些这个数据是不是就是一个是URL一个就是states一个就是message对不对啊那么我们是不是可以这么来玩啊这么来玩那么我们就可以在我们这个VO这个里面呢我们创建一个类啊叫什么呢就叫web吧web-resultweb-result一个类然后呢这个类里面呢
[07:13] 我给他定义一个我关键的一些属性关键的属性比如说什么我的状态状态那么状态是硬的类型那么就是taste还有什么还有一个messagemsg messageok private然后street message这个也是一个关键的信息
[07:36] 其实这个message没有什么太大的用但是我们也给它定义出来还有个就是我们的这个url对吧把它也拷过来stream是它但是你要注意的是我们并不能够直接对这个对象是不是做一个响应那我们给它加一些这个注解首先它需要一个date注解是不是然后是第一个第二个是我们需要给它去设置什么呢我们给它设置一个叫做jsonjson-inglow
[08:06] 就是说我们对在对这个对象做序列化的时候啊我们忽略这个字段OK忽略这个字段这个字段我们把这个字段的全部给他忽略掉忽略掉之后我们是不是就来思考一下最终我们响应的这个数据是不是就需要有两个对吧因为最终我们响应的注意啊你看啊最终我们响应的这个对象啊我来画一个图啊那么最终响应的这个对象
[08:35] 其实就是我们这个对象是不是对吧那么我们这种响应这个对象中包含两个属性一个是date一个是matter但是我们这个里面并没有date和matter怎么办呢我们是不是可以这么来玩那么我们可以给它设置一个方法返回值来看一下那么这个date返回的是不是一个对象对象我们是不是可以把它看作是或者说
[09:00] 把它看作是使用一个什么呢使用一个这个map是不是来来代表这个对象啊所以我们可以写一个这个map写一个这个mapkey呢就是stringvalue呢就是一个object这样的一个对象那么这个方法名呢我们是不是可以把它认为叫做一个什么呢getData就是get一个Data对吧OK那么它的这个方法被序列化的时候是不是就会被序列化成一个
[09:30] data的一个属性啊ok那么return啊先给它return on吧好那么我们设置为一个它然后呢还需要一个设置呢是不是就是我们下面呢还有一个叫做get什么呢meta啊meta那么把这个date我们改改成什么呢meta这样的话是不是我们保证了这个对象中有两个属性一个是date一个是meta而这个date它是怎么玩的呢是不是我们去具体做一个分装就可以了
[09:59] 那么这个我们先分装这个mapMatter吧Matter因为比较简单那么它是不是需要有两个这个属性对不对那么我们就在这个位置给它去定义一个这个map就叫什么呢String来一个object就叫map吧等于new一个什么呢hashi map因为这个不需要顺序然后我们直接return这个map
[10:29] map中的包含两个内容的一个是谁呢一个是stace那么我们就拿到stace的值那么还有一个是message那么我们就拿到这个message这样的值这样的话我们是不是就省去了一些对象的分装ok这个是不是就搞定了然后呢我们紧接着呢在这个里面呢给他去做一些这个实现那么他里面所响应的是一个list本身他也是个对象啊那么我们也是不是可以这样去给他分装一下
[11:00] 那么首先定义我们的一个map最终返回的是一个map然后呢map中又去put一个谁呢put一个是不是一个list而这个list它就是一个集合是不是又是一个集合啊哎OK那么这个集合对吧那这个集合那我们怎么去做一个构造呢哎呃注意啊这个位置我们不能这么去构造啊不能这么去构造那么这个不能这么构造啊那么我们来看一下这个地方应该怎么构造呢
[11:30] 这个应该放到他这个里面啊那我们来看一下那么在外面呢我们所需要的是一个这个list的一个这个呃集合对吧list的这个集合那这样呢我们就直接给他去做这样的一个分装吧做这样分装那我们就直接这样来写吧就是写一个list然后呢写一个写一个t吧写一个t那么这个里面我们就去存什么呢
[12:01] 就去存的是我们的一个这个设置为就是一个list但是我们把它忽略掉这个位置为了方便使用我们就不使用这个t了我们使用一个问号做一个站位就可以了你如果你存什么东西都行ok然后在这个里面怎么玩来看一下这个结构稍微有点麻烦繁琐然后list代表的是不是就是它
[12:32] 对不对然后呢这个里面丢什么东西呢丢的是每一个对象所以呢在这个里面呢我们又要去分装一个对象了对吧那么怎么这个对象怎么分装呢我们就需要去对我们上面的一个我们的一个集合去做一个便利便利我们这个list是不是拿到这个拿到这个O对不对拿到这个O那么这个O呢我们怎么样去哎这个有点问题啊那就那这样啊不对
[13:03] 那就这样我们在这个list中直接拿到的其实就是这个list这个有点有点绕了拿到其实就这个list那么就说你传给我什么我直接拿到什么做return就可以了来看一下那么我这个list中是不是就拿到就是这个list就分装的就是这一块内容对吧分装就这一块内容这个逻辑稍微有一点的绕所以有一点绕
[13:28] 那么我们这么绕的目的其实就是想要去减少我们的一些对象的一个创建这样的话是不是就保证了我们一个对象中有两个属性一个是data一个是meta好那么我们是不是就已经确定了我们在我们 ad Controller中它所返回的一个类型是不是就是一个web result对不对咱们把它拷进来那么在web result中我们最终是不是去要构造web result
[13:57] 那么为了方便使用呢我们给这个webreducer我们给他设置一些静态的一些构造方法那么方便我们使用啊来一个static然后呢我们返回类型呢就是一个他啊然后呢我们去给他设置一些静态的方法去构造比如说ok那么ok呢我需要你传递的其实是一个list对吧list那么我就这么来玩是不是我可以
[14:25] 然后他return一个new一个web result那么第一个呢是states那就是200他是不是没有一个全参数的构造构造函数啊那我们来给他去加一个然后呢第一个参数是200那么第二个呢就是message呢我们就说成功吧随便写个东西啊就成功默认就是简直成功然后list呢那就是传递进来的这个listok
[14:53] 这是第一个啊那么有些时候呢我们可能需要这样去做一个构造当然我们看一下啊是不是他现在没有无参的构造函数啊有没有来看一下他这个里面的有一个全参数的但是没有无参的了那么我们就需要无参的也是需要的啊因为我们外面也需要这样的一个配置那写一个无参的构造的函数来看一下这个下面是不是就有一个无参的构造函数了OK好
[15:22] 那么这样的话我们就搞定了那么下面呢OK呢我们是不是还可以再来一个什么呢message好那么在这个里面message呢就却不是这个成功了那就是这个message好这样的话呢我们是不是就实现了两个这个OK这个方法其他的我们就不做一个分装了好那么我们回到刚刚的我们这个Controller中回到我们的Controller中那么在这个Controller中我们就需要去这样去玩就可以了吧
[15:54] 直接return一个叫做webresult.okok拿到一个list是不是就可以了其实我们这样做的目的就是让我们使用起来更方便一点按了page info然后点get什么的recode好这样的话是不是就可以了不行为什么不行因为你这个recode拿到是不是都是adad中是不是包含了很多的属性而我们现在不需要
[16:21] 只需要一个就可以了对不对所以这个位置还不行我们还需要去便利一下它那么我们得这么玩得这么玩拿到一个ad page info.getrecode我们去拿到它的一个集合拿到一个集合拿到一个集合拿到一个集合拿到一个recodes然后我们对它去做一个便利
[16:52] 当然了我们先得这么玩先得定义一个listlist里面存什么呢其实我们存的是list里面我们存的是看一下啊list里面所存的呢都是一些对象是不是那么这个呢我们就需要这么来玩了那我就这样吧简单一点写呢就来一个object吧就是我们那个resultresult等于new一个arraylist
[17:23] 然后呢我们最终拿到的应该是他去做一个返回但是呢我们需要对定主要是做一个分装那么分装谁呢是不是我们就拿到这个ad是不是做一个这个分装ad对吧然后呢我们每次每一次遍历这个ad呢我们就需要去拿到他的url去给他丢到这个里面来对吧那么我在这个位置还是需要去定一个map那么stream来一个object吧然后来一个map
[17:52] 等于new一个hcmap然后呢这个map.putput谁呢是不是就是刚刚我们看到他的一个这个autorization然后呢我们把它拿过来url呢是不是就是ad.get什么呢url哎呀ok然后呢我们将这个map呢呃将这个result啊result.end是不是添加一个map把这个map丢到这个集合中
[18:21] 然后把这个集合最后返回就可以了OK这就是一个这样的一个结果所以我们针对于前端所要求的这样一个数据结构我们去分装了一些对象好那么接下来我们来做一个测试看它是否能够正常的跑起来OK那么这样我们就先看一下我们的讲义测试的我们放到下一个视频中来做一个讲解
[18:48] 那么在前面呢我们可以看到是不是我们编写了这个Controller而这个Controller呢我们可以看到这个位置呢做了些这些分装啊那么这个需要大家去去理解一下这样的一些分装啊哎OK然后呢我们这个Service相对比较简单可能比较麻烦一点的是这个web这个controlweb result啊web result因为这个web result的一个分装啊需要你去根据前端的一个这个所要求这个结构
[19:16] 在结合我们的一个加码对象的一个分装的一个特点去做出这样的一个分装OK当然了我们这个代码中还缺了一点点东西就是刚刚我们在分装这个web.youtube的时候这两个不需要它做一个序列化所以给它添加一个json.include把它忽略掉就可以了好但是这下面这两个呢我们不忽略啊这两个保留可以看一下讲义啊OK
[19:41] 好那么测试我们就放到下一个环节再做一个测试好那么关于 API 接口服务的一个编写我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何使用 Spring Boot 和 Dubbo 构建并注册一个提供广告服务的微服务，包括服务接口、实现类、控制器、返回结果封装以及配置文件的编写。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Dubbo 服务提供者的配置文件 application.properties，其中定义了服务扫描包、应用名称、协议、端口和注册中心地址。
画面2：展示服务接口类 AdService.java，定义了服务方法 queryAdList。
画面3：展示服务实现类 AdServiceImpl.java，定义了 queryAdList 方法。
画面4：展示控制器类 AdController.java，定义了 @Reference 注解用于注入服务。
画面5：展示桌面文件夹，其中包含多个开发工具的快捷方式。
画面6：展示返回结果类 WebResult.java 的定义。
画面7：展示 WebResult 类中 @Data 注解和 @JsonIgnore 注解的使用。
画面8：展示 WebResult 类中 getData 方法的实现。
画面9：展示 WebResult 类中 getMeta 方法的实现。
画面10：展示 WebResult 类中静态方法 ok 的实现。
画面11：展示 AdController 类中 queryIndexAd 方法的实现。
画面12：展示 AdController 类中 queryIndexAd 方法的完整实现。
画面13：展示 PDF 讲义中关于实现 API 接口服务（RESTful 接口）的章节，包括引入依赖和编写 Controller。
画面14：展示 PDF 讲义中关于测试的章节，包括 getData 和 getMeta 方法的实现。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```
# 服务的扫描包
dubbo.scan.basePackages = cn.itcast.haoke.dubbo.server.api

# 应用名称
dubbo.application.name = dubbo-provider-ad

# 协议以及端口
dubbo.protocol.name = dubbo
dubbo.protocol.port = 21880

# 注册中心
dubbo.registry.address = ZooKeeper://172.16.55.185:2181
```

画面2：
```
package cn.itcast.haoke.dubbo.api.Service;

import cn.itcast.haoke.dubbo.server.api.ApiAdService;
import org.springframework.stereotype.Service;

@Service
public class AdService {
```

画面3：
```
import cn.itcast.h
import cn.itcast.h
import cn.itcast.h
import com.alibaba
import org.spring
@Service
public class AdSer
@Reference (val
private ApiAd
public PageInfoAd queryAdList(Integer type, id) {
}
```

画面4：
```
package cn.itcast.haoke.dubbo.api.Controller;
import org.springframework.web.bind.annotation.*;
@Reference (jdk.nashorn.internal.ir
@RequestMapping (org.springframework.web.bind.annotation
@RestController (org.springframework.web.bind.annotation
```

画面6：
```
package cn.itcast.haoke.dubbo.api.vo;
public class WebResult {
    private Integer status;
    private String msg;
    private Stri
```

画面7：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
```

画面8：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
    public Map<String,Object> getData() {
        return null;
    }
```

画面9：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
    public Map<String,Object> getData() {
        Map<String,Object> map = new HashMap<>();
        map.put("list", list);
        return map;
    }
```

画面10：
```
@Data
public class WebResult {
    @JsonIgnore
    private Integer status;
    @JsonIgnore
    private String msg;
    @JsonIgnore
    private String original;
    public static WebResult ok(List<?> list) {
        return new WebResult();
    }
```

画面11：
```
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@Autowired
private AdService adService;
@GetMapping
public WebResult queryIndexAd() {
    PageInfo<Ad> adPageInfo = new PageInfo<Ad>();
    return WebResult.ok(adPageInfo);
}
```

画面12：
```
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
@Autowired
private AdService adService;
@GetMapping
public WebResult queryIndexAd() {
    PageInfo<Ad> adPageInfo = new PageInfo<Ad>();
    return WebResult.ok(adPageInfo);
}
```

画面13：
```
3.4.1、引入依赖
<dependencies>
    <groupId>cn.itcast.haoke_manage</groupId>
    <artifactId>itcast-haoke-manage-dubbo-server-ad-interface</artifactId>
    <version>1.0-SNAPSHOT</version>
</dependencies>

3.4.2、编写Controller
package cn.itcast.haoke.dubbo.api.Controller;
import cn.itcast.haoke.dubbo.api.Service.AdService;
```

画面14：
```
public Map<String, Object> getData() {
    HashMap<String, Object> data = new HashMap<String, Object>();
    data.put("list", this.list);
    return data;
}
public Map<String, Object> getMeta() {
    HashMap<String, Object> meta = new HashMap<String, Object>();
    meta.put("msg", this.msg);
    meta.put("status", this.status);
    return meta;
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

