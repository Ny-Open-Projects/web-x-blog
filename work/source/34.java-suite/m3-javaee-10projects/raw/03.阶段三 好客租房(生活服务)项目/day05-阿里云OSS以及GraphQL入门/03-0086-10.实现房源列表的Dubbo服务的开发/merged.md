# 10.实现房源列表的Dubbo服务的开发

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day05-阿里云OSS以及GraphQL入门
- 源文件：03.阶段三 好客租房(生活服务)项目\day05-阿里云OSS以及GraphQL入门\10.实现房源列表的Dubbo服务的开发【海量资源尽在 ubkz.com】.mp4
- 时长 16分22秒（音频 983s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么我们接着继续啊那么接下来呢我们来实现啊房源的列表这个功能那么在前面呢我们已经实现了房源的新增啊这个功能那么接下来我们来实现列表那么我们要想去实现这个列表呢首先我们其实要做的是实现这个列表服务对吧那么有了这个服务之后啊那么我们才能够去调用这个服务才能完成一个列表功能啊所以呢我们先来实现这个服务
[00:29] 那么首先呢我们在我们这个double这个服务的这个系统中啊interface这个系统中啊我们先来定义一个我们这个API的一个接口的一个方法啊那么咱们把这个来call一下拷贝啊拷贝它那么这么来call吧我们进入到进入到我们的这个API这个工程然后呢interface这个工程啊然后找到这个下面的有一个
[00:59] interface我们来看一下在这个interface这个工程中然后呢我们去创建啊在我们原有的这个API下面呢我们去追加一个方法那么这个是我们之前的一个新增房源这个功能那么下面呢我们把这个分页去查询我们这个房源列表这个方法我们定义出来来看一下好那么现在的话我们是不是就已经把这个方法定义出来了对吧
[01:29] 定义出来了但是呢我们来看一下那么这个方法定义好之后啊那么方法的名字叫做query host然后resource list这样的一个方法那么它所接受的参数呢有三个一个呢就是我们的一个page就是我们的这个当前页你是第几页然后呢page size呢就是我们这个页面大小那么后面的这个呢就是我们的一个查询的条件啊
[01:55] 那么如果没空的话呢代表的就是没有条件啊没有条件去做一个分页那么我们来看一下它的一个返回值呢叫做配置因素啊但是呢我们现在呢并没有去定义这个配置因素那么所以接下来呢我们要去把这个配置因素这个对象呢我们来定义一下那么这个对象呢我们把它写到下面吧写一个包啊叫VO去区别于我们的一个PO9啊它并不是一个实体啊那么我们来看一下这个VO
[02:24] 那么这个PagerInfo这个对象应该怎么样去定义那么在这个PagerInfo这个对象中其实我们有这么几个我们的一个属性对吧属性好那么我们把这个属性的扣过来OK那我们来看一下那么首先第一个是有一个叫做Total就是我们的一个数据的总条数然后还有就是我们的一个PageNumber就是当前页你的第几页
[02:52] 然后呢下面还有个page size就是你一页显示多少条数据然后呢我们来看一下这个位置有个t那么代表的是它是一个范形啊那么我们去要查询的数据列表叫recodes那么这个这个呢page info它是一个通用的一个这样的一个对象所以呢我们这个历史中存放什么样的对象那么我们需要去有个范形来做一个指定所以呢我们需要在这个位置给它去指定一个t这样的一个范形好那么
[03:20] 我们给他做一个初始化就是给他设置一个空的一个集合ok通过这个connections这个有tel下面的工具工具类然后去生成一个空的一个list好那么下面我们给他添加一些注解那么我们肯定需要添加这个date注解对吧帮我们去生成他的get和set方法ok并且要注意的是由于我们在这个位置所定义的是一个api的一个这个接口
[03:48] 那么这个对象是不是一定会通过我们double的一个协议是不是去传输我们的这个对象所以这个对象他一定需要怎么呢做一个序列化所以呢他需要继承我们IO下面的序列化接口点IO这个扫了一个关键字对吧然后他要去做一个实现实现我们这个java.io下面的我们的实例化序列化的一个接口然后呢并且呢要注意的是那么我们需要在这个位置呢去
[04:17] 给他去添加一个序列化的一个ID这个对象序列化的一个ID好那么现在我们这个对象的我们是不是就搞定了OK那么当然了我们来看一下讲义在讲义中我们还缺少一个这个就是全参数的这样的一个注解其实这个是需要的就是我们去方便我们去构造这个对象的时候去有一个全参数的这样的一个构造的一个方法那么我们是不是可以方便的去
[04:45] 构造我们这个对象哎好嘞那么到这呢我们这个呃我们这个API的一个接口是不是就已经定义好了哎那个接口在哪呢来找一下啊呃在这个里面是不是就已经定义好了哎这里面缺少什么呢是不是缺少哎缺少内容刚刚可能不小心吧把它删掉了啊好那么把它再回对回来这样的话呢我们这个接口是不是就定义完成了
[05:13] 这个好像多了一些这个信号把这个信号给他拿掉好那么接口就搞定那么接下来我们要做的事情呢是不是就是去实现这个接口那么继续往下面看那么下面呢我们就来实现这个double这个服务然后呢我们在这个double Service这个服务中呢去实现这个方法那么我们进入到我们这个double Service这个服务中呢我们打开我们的一个API这个包下面的一个实现列那么显然呢他肯定会报错对吧然后呢我们去
[05:43] 实现刚刚我们所定义的这个方法那么这个方法怎么样去做实现呢那么我们是不是就要去调用我们的一个叫做base Mapper里面的一个查询的方法对吧那么这个时候我们会发现在我们的这个在我们的这个Service中就是在这个Service中那么他有没有去实现这个方法呢可能并没有实现对吧所以我们就需要
[06:11] 这么来玩去做一个这样的一个实现好来看一下那我们实现它的我们这样先在这个位置我们就去直接去调用我们这个Service去做一个查询然后下面我们来看一下这个具体的一个实现好来看一下那我们实现它的我们这样先在这个位置我们就去直接去调用我们这个Service去做一个查询然后下面我们来看一下这个具体的一个实现
[06:41] 好,那么咱们就这么来玩吧直接去调用它,类似点这个Service点叫做名字就跟他叫的一样吧,一样的名字然后呢参数呢我们也给他传递相同的这个参数然后呢来一个配置set然后呢再来一个这个后面的我们一个查询的一个参数啊ok好,那么我们把这个方法呢在我们的这个业务的一个Service中呢去做一个创建好,那么定义先给他定义一个接口
[07:10] 定义好接口之后啊那我们再进入它的一个实现类去做一个实现好来看一下那么在这个里面呢去实现它的一个方法好把这个方法呢去做一个实现然后呢在这个里面呢我们来看一下那么在这个中啊我们就需要去调用什么呢这个我们的basebase Service中的一个方法对吧当然了在base Service中它呢会去
[07:39] 调用我们base Mapper中的这个方法哎呀ok好在这个业务的里面呢他才会调用我们base Mapper中的方法那我们来看一下这个里面怎么去玩呢那么我们来看在base Service中他有没有提供关于我们去分页啊查询的这样的一个方法呢我们来看一下在这个位置是不是有一个query page list by will就是我们根据我们的一个这个条件是吧去做一个分页的一个
[08:09] 查询但是呢我们要注意的是我们在查询的时候啊那么我们不仅仅是说要根据一个条件去做一个查询那么我们还是需要有一些其他额外的动作要去做比如说对于我们这个数据那么我们查询的这个列表我们其实希望它是什么呢按照我们的一个更新时间基本去做一个倒序的一个排序那么也就是说我们需要查询到的数据呢是
[08:38] 最新的数据是排到最前面的按照一个倒序去做这样的一个查询那么这个时候呢显然呢我们会发现这个方法它并不能够去满足我们的需求对吧并不能满足因为你只有一个查询条件并没有去设置我们的一个排序这样的一个效果那么这个应该怎么玩呢我们需要给这个
[09:01] base Service中再给他增加一个方法来看一下增加的这个方法呢他呢就是要做我们query page list然后他的参数呢我们可以看到那么他是通过一个query的一个wrap这样的一个方法一个对象啊去做一个查询这个对象呢是我们的这个mybattis plus这个插件中的所定义的一个这样的一个对象啊
[09:27] 然后再传递一个配置和一个漏死去做这样的一个查询那么我们把这个方法拷贝过来OK来拷贝过来我们再来看一下那么把它加到我们的这个位置好哎没有拷贝到然后呢拷贝一下来拷贝过来那么在这个里面呢我们其实可以看到那么他的查询条件刚刚我们已经说过了对吧然后我们来看他的一个返回值
[09:51] 那么它的返回值呢这个叫做ipage就是也是mybattles啊plus这个插件中的一个对象对吧哎ok好那么我们这个方法是不是就加好了那么接下来呢我们就要去做一个实现那么实现我们这个方法那么应该怎么样去做一个实现呢我们来看一下那么我们调用什么呢我们其实是调用这个sharp下面的叫做query page list啊呃配置
[10:20] 然后是不是调用这个pager list那么它需要传递三个参数第一个就是我们刚才所说的query drop就是我们的一个包装的一个对象对吧那么我们第一个参数先给它设置为null然后第二个参数我们叫page第三个参数是不是叫pagesizeok那么这个我们是不是就搞定了就搞定了然后我们接着继续往下面看
[10:46] 那么这个query这个rop这个对象那么怎么样去定义呢我们来看一下那我们就给它定义一个叫做queryrop这个对象queryrop这个对象然后呢等于怎么呢去new一个queryrop对象OK好那么把它是不是就可以去做一个传递进去啊那么刚刚我们说过我们是不是需要根据什么呢根据我们数据的更新时间做一个倒序的排序对不对
[11:16] 排序排序那么这个应该怎么设置呢我们来看一下它这个里面的一些方法点什么呢叫order byorder by什么呢desc那么根据什么去做一个desc是不是后面去传递一个colon对吧那么我们是不是希望它去根据谁呢根据update是不是去做一个
[11:41] 倒序的一个排序啊哎OK这个没有任何问题对不对然后呢这样的话他是不是就可以去做一个倒序的一个查询啊OK那么我们来看一下他的一个返回值呢是叫一个IP对吧那么拿到这个IP我们来看一下IP呢是这个mybattlesplus这个插件中的一个这个接口当然了他肯定有对应的这个实现类对吧来看一下有对应的这个实现类叫配着这个对象哎OK
[12:10] 好,那我们来看一下这个在我们这个方法中那么其实我们要求所返回的对象是不是这个配置info对吧,配置info那么我们是不是要通过这个iPage这个对象然后去构造我们这个配置info这个对象所以我们需要在这个位置再去new一个我们的配置info这个对象那我们来看一下这个配置info它有没有设置一个全参数的一个构造函数呢是不是有所以我们按照这个顺序
[12:40] 给他做一个添加第一个参数是不是叫total对吧那我们来看一下那么在这个ipage中是不是就可以拿到一个get什么呢total这是我们的第一个这个参数对吧第一个参数然后呢第二个参数呢我们来看一下通过这个ipage第二个参数是什么呢我们来看一下第二个参数叫page number这是我们当前页那么当前页呢其实就是我们这个page的这个数据是不是
[13:05] 所以直接传递进去那么第三个参数呢其实就是我们的叫做PageSign那么我们就把这个PageSign给他拿过去那么就是他PageSign那么第四个参数呢就是我们的数据对吧通过这个ipad.get什么呢records是不是就是拿到我们的数据啊那么这个t呢其实我们就是返回的是我们的houseResource啊这样的对象那么但是呢现在他还是会有点报错
[13:33] 来看一下这个错误在报什么呢显然是不是这个参数有问题啊就是我们现在要求的是一个硬的但是呢你拿到的是一个浪对象那么怎么玩呢我们就需要给他去做一个这个强转对吧强转但是呢他返回的又是一个这个数字类型的这个浪啊那么我们应该怎么玩呢这么来玩一下那么给他先去转成一个我们的一个先转成一个浪对象啊浪的一个对象类型
[14:02] 然后呢再int value好这样的话是不是就实现了这样的一个返回啊好那么现在呢我们是不是就完成了这样的一个完成了这样的一个操作对吧完成这样的操作好那么现在我们是不是就已经实现了它这个方法那么也就意味着我们这个接口是不是就已经做了一个实现啊ok好那么我们继续往下面看那么下面呢我们来启动这个服务啊启动这个服务来看一下
[14:32] 那么我们先来测试一下吧先来测试一下看他到底能不能够去把我们这个服务呢去注册到我们的注册中心然后呢这个到底这个服务呢可不可用啊好来测试一下然后呢我们在这个位置啊去把我们的这个这个这个double的一个去做一个重启啊provid做一个重启好等待他的一个重新做一个启动
[15:02] 我们来看一下他是否能够把这个服务呢去注册到我们的注册中心好那么这样我们等待他的一个启动我把视频呢暂停一下好那么现在呢我们这个服务呢就已经启动起来了然后呢我们进入到我们这个呃double的这个服务的一个这个ops中啊就是这个double的admin里面我们去查询一下啊查询一下我们这个Service通过我们这个application去做一个查询然后点击search然后呢会发现
[15:33] 是不是已经有一个服务了对吧ok 那说明现在基本上正常对吧那我们已经把这个服务是不是开发完成了那么在这特别要强调的一点就是我们在mybatties这个plus中我们想要去玩这个分页要玩这个分页那么一定别忘记了要加一个分页的一个插件要把这个bin加入到spin的容器中那么我们的分页才会生效那么如果你不添加这个分页插件的话
[16:02] 它是不会生效的啊这一点啊一定要注意啊一定要注意OK好那么现在我们是不是就已经实现了我们这个服务对不对好那么下面呢我们是不是就可以来实现我们的一个RESTful的一个接口对吧好那么关于我们的房源列表的服务的一个这个实现呢我们就讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现房屋资源列表服务的 Dubbo 接口定义、服务实现与服务注册。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示课程 PDF 文档，标题为“5. 房源列表服务”，并指出接下来要实现房源列表服务。同时显示了项目结构，当前位于“5.1、定义dubbo服务”。
画面 2: 显示 `ApiHouseResourcesService` 接口定义，包含 `saveHouseResources` 和 `queryHouseResourcesList` 方法。
画面 3: 显示 `PageInfo` 类的定义，包含 `total`、`pageNum`、`pageSize` 和 `records` 字段。
画面 4: 显示项目结构，突出 `PageInfo.java` 文件位于 `vo` 包下，并显示了 `@Data` 注解的 `PageInfo<T>` 类定义。
画面 5: 显示 `HouseResourcesServiceImpl` 类，实现了 `saveHouseResources` 方法，包含对标题为空的校验逻辑。
画面 6: 显示 `ApiHouseResourcesServiceImpl` 类，使用 `@Service(version = "1.0.0")` 注解，并注入 `HouseResourcesService`。
画面 7: 显示 `queryHouseResourcesList` 方法的实现，目前仅返回 `null`。
画面 8: 展示 PDF 文档“5.3、启动服务”章节，内容为“5.3、启动服务”标题和黑马程序员的页脚。
画面 9: 显示 `queryHouseResourcesList` 方法的实现，使用 `QueryWrapper` 构建查询条件并调用 `super.queryPageList`。
画面 10: 显示 `queryHouseResourcesList` 方法的实现，返回 `new PageInfo<>` 对象。
画面 11: 显示 `queryHouseResourcesList` 方法的实现，使用 `QueryWrapper` 设置排序条件并调用 `super.queryPageList`。
画面 12: 展示 PDF 文档“5.3、启动服务”章节，内容为“5.3、启动服务”标题和黑马程序员的页脚。
画面 13: 显示 Dubbo OPS 界面，展示服务提供者信息，IP 为 192.168.40.1，端口为 20880。
画面 14: 展示 PDF 文档“5.3、启动服务”章节，内容为“5.3、启动服务”标题和黑马程序员的页脚。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```java
package cn.itcast.haoke.dubbo.server.api;
import cn.itcast.haoke.dubbo.server.pojo.HouseResources;
import cn.itcast.haoke.dubbo.server.vo.PageInfo;
public interface ApiHouseResourcesService {
    /**
     * 新增房源
     * @param houseResources
     * @return -1:输入的参数不符合要求，0：数据插入数据库失败，1：成功
     */
    int saveHouseResources(HouseResources houseResources);
    /**
     * 分页查询房源列表
     * @param page 当前页
     * @param pageSize 页大小
     * @param queryCondition 查询条件
     * @return
     */
    PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize,
            HouseResources queryCondition);
}
```

画面 3:
```java
import java.util.Collections;
public class PageInfo {
    /**
     * 总条数
     */
    private Integer total;
    /**
     * 当前页
     */
    private Integer pageNum;
    /**
     * 一页显示的大小
     */
    private integer pageSize;
    /**
     * 数据列表
     */
    private List<T> records = Collections.emptyList();
}
```

画面 4:
```java
package cn.itcast.haoke.dubbo.server.vo;
import lombok.Data;
import java.util.Collections;
import java.util.List;
@Data
public class PageInfo<T> {
    /**
     * 总条数
     */
    private Integer total;
    /**
     * 当前页
     */
    private Integer pageNum;
    /**
     * 页显示的大小
     */
    private integer pageSize;
    /**
     * 数据列表
     */
    private List<T> records = Collections.emptyList();
}
```

画面 5:
```java
import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;
@Service
@Transactional
public class HouseResourcesServiceImpl extends BaseServiceImpl implements HouseResourcesService {
    /**
     * @param houseResources
     * @return -1:输入的参数不符合要求，0：数据插入数据库失败，1：成功
     */
    @Override
    public int saveHouseResources(HouseResources houseResources) {
        // 添加校验或者其他的逻辑
        if (StringUtils.isBlank(houseResources.getTitle())) {
            // 不符合要求
            return -1;
        }
        return super.save(houseResources);
    }
}
```

画面 6:
```java
@Service(version = "1.0.0")
public class ApiHouseResourcesServiceImpl implements ApiHouseResourcesService {
    @Autowired
    private HouseResourcesService houseResourcesService;
    @Override
    public int saveHouseResources(HouseResources houseResources) {
        return this.houseResourcesService.saveHouseResources(houseResources);
    }
}
```

画面 7:
```java
@Override
public PageInfo<HouseResources> queryHouseResourcesList(int page, int pageSize, HouseResources query) {
    return null;
}
```

画面 9:
```java
QueryWrapper<T> queryWrapper = new QueryWrapper<>();
// 根据数据的更新时间倒序排序
queryWrapper.orderByDesc(...columns: "updated");
IPage<IPage> iPage = super.queryPageList(queryWrapper, page, pageSize);
return new PageInfo<>(iPage.getTotal(), page, _);
```

画面 10:
```java
return new PageInfo<>();
```

画面 11:
```java
QueryWrapper queryWrapper = new QueryWrapper();
// 根据数据的更新时间倒序排序
queryWrapper.orderByDesc(...columns: "updated");
IPage<IPage> iPage = super.queryPageList(queryWrapper, page, pageSize);
return new PageInfo<>(iPage.getTotal(), page, _);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: PDF 文档标题为“5. 房源列表服务”，并指出接下来要实现房源列表服务。
画面 8: PDF 文档标题为“5.3、启动服务”。
画面 12: PDF 文档标题为“5.3、启动服务”。
画面 14: PDF 文档标题为“5.3、启动服务”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

