# 12_爬虫系统初始化_初始化URL的获取_测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day08-黑马头条-爬虫系统搭建&下载url初始化
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day08-黑马头条-爬虫系统搭建&下载url初始化\12_爬虫系统初始化_初始化URL的获取_测试【海量资源尽在 666java.com】.mp4
- 时长 3分29秒（音频 210s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那咱们就继续往下讲刚才这块其实忘了返回了这时候你需要去把它给返回一下这样的话咱们就可以了然后的话稍等我看看咱们需要去负载值负载值忘了负值了这块行这样的话咱们最终是一个这样的效果就出来了效果出来之后咱们在这儿当前的优先级咱们可以默认先给它给一个10完之后这时候咱们可以去测试一下
[00:37] 去测试一下测试其实比较简单这时候你只要在这去创建一个测试类就可以了比如说咱们在这去创建一个测试类com kima test color什么test咱们叫csd orange data process pro test创建完之后咱们在这就可以直接去sprint boot test然后是run with sprint runner rclass
[01:16] 好设置完之后下面呢咱们就可以把当前的这个类注入进来叫c s e norange data source processc s d n然后去设立一个autoware我们写一个测试方法public void然后teste这个名字随便起啊打一个test然后呢让他呢直接去用就可以了然而有一个方法叫parseorangenow就这个啊
[01:53] request date就它这边需要一个参数就是有一个process flow date我们可以去new一个出来好设置完之后它会去返一个集合我们可以把这个集合打印一下好吧好印完之后咱们可以在这去打个脸去看一下里面的内容稍等一下咱们直接去debug运行稍等看看会不会出现什么问题有问题咱们就调一调没问题就直接过
[02:45] 好像是没什么问题啊稍等好来了啊来了之后呢你可以往下走一步走一步之后呢你可以去看把手标放到这你可以看一下当前是不是12条数据是吧是12条数据啊你可以看一下他的URLURL呢这个是扎过啊后边是拼了一个当前的时间窗你可以看一下他的类型是否的出手画的文档类型是出手画是吧
[03:10] 然后你也可以看一下第二条是吧刚刚看了一条啊咱们可以看一下再看其他的其他的你看刚才是Java现在这边是不是AIS也是然后第二条应该是web应该是webOK那这个内容啊咱们就算是设置完了准备内容设置完了下面咱们去做第二步就是做下载

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何为一个名为 CsdnOriginalDataProcess 的 Java 类编写 Spring Boot 单元测试，验证其 parseOriginalRequestData 方法的返回值。

2) 按时间顺序列出每张画面的要点：
画面1：展示 CsdnOriginalDataProcess.java 文件，其中 parseOriginalRequestData 方法的实现，用于处理原始请求数据并返回一个 ParseItem 列表。
画面2：切换到测试类 CsdnOriginalDataProcessTest.java，开始编写测试方法。
画面3：在测试类中导入 SpringBootTest 和 @RunWith(SpringRunner.class) 注解。
画面4：使用 @Autowired 注解注入 CsdnOriginalDataProcess 实例。
画面5：编写测试方法 test1()，调用被测方法。
画面6：在 test1() 方法中调用 parseOriginalRequestData 方法。
画面7：为 parseOriginalRequestData 方法传入一个 ProcessFlowData 对象。
画面8：在 test1() 方法中添加 System.out.println(parseItemList); 语句用于打印结果。
画面9：运行测试，控制台显示 Spring Boot 启动日志。
画面10：控制台显示 Hibernate 初始化日志。
画面11：控制台显示 Spring Boot 启动完成日志。
画面12：在调试模式下，查看 parseItemList 变量，其大小为 12。
画面13：展开 parseItemList 中的第一个元素，查看其 documentType 字段值为 "INIT"。
画面14：展开 parseItemList 中的第一个元素，查看其 url 字段值为 "https://www.csdn.net/nav/arch?id=157113728046"。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面1：
```java
@Override
public List<ParseItem> parseOriginalRequestData(ProcessFlowData processFlowData) {
    List<String> initCrawlerList = crawlerConfig.getInitCrawlerUrlList();
    if (initCrawlerList == null || initCrawlerList.isEmpty()) {
        parseItemList = initCrawlerList.stream().map(url -> {
            crawlerParseItem = new CrawlerParseItem();
            crawlerParseItem.setUrl(url);
            crawlerParseItem.setDocumentType(CrawlerEnum.DocumentType.INIT.name());
            crawlerParseItem.setHandelType(processFlowData.getHandelType().name());
            return crawlerParseItem;
        }).collect(Collectors.toList());
        return parseItemList;
    }
    return parseItemList;
}
```

画面6：
```java
import com.heima.crawler.process.original.impl.CsdnOriginalDataProcess;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

@SpringBootTest
@RunWith(SpringRunner.class)
public class CsdnOriginalDataProcessTest {

    @Autowired
    private CsdnOriginalDataProcess csdnOriginalDataProcess;

    @Test
    public void test1() {
        csdnOriginalDataProcess.parseOriginalRequestData();
    }
}
```

画面7：
```java
@Test
public void test1() {
    csdnOriginalDataProcess.parseOriginalRequestData(new ProcessFlowData());
}
```

画面8：
```java
@Test
public void test1() {
    List<ParseItem> parseItemList = csdnOriginalDataProcess.parseOriginalRequestData(new ProcessFlowData());
    System.out.println(parseItemList);
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

