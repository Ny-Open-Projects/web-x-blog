# 21_数据保存_频道_service_查询标签测试

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\21_数据保存_频道_service_查询标签测试【海量资源尽在 666java.com】.mp4
- 时长 7分57秒（音频 477s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面咱们就来去测试一下测试的话就在当前的caller当前爬熊系统中来打开当前test咱们在这去重新new一个类好吧new一个class看我们点黑马callerservice咱们叫啥咱们叫adlabel Service test好ok
[00:32] 然后你要去进行环境环境的话这个比较熟了Spring Boot然后是Run with然后SpringRunner.class是吧好你需要把当前的Service给注入进来private然后是adlabel Service注入进来注入进来之后下面咱们就可以在这去设置一个方法public void然后是test好吧然后下面咱们就可以去调用里面的方法去进行测试
[01:01] 一个叫做getlabel是下边这个是吧当然这个值是一个字幕块咱们一会再说返回的就是一个label是咱们也可以打印一下好labelids好在这儿去加一个test这个参数说是啥呢参数的话咱们可以设一个java这个java我这个目前数据库里面是有的啊你看一下java有Docker咱们可以设这个Docker比如说Docker我设这个没有的比如说我设这个
[01:32] 88888OK那这个东西肯定是没有的我要去测的时候其实就是他要给我返回过来这三项的什么这三项label的ID值他并且是一个字符号并且是要与逗号分割好吧但是这个没有这个没有的话你需要干嘛你需要去做保存操作咱们可以拷贝一下你到这去搜一下一下比如说筛选你找到前的name然后是他的你看有没有应用是没有的是吧
[02:02] 那咱们下面就来去执行执行咱们直接放行看看有没有报错稍等我正在运行稍等一下当然你这个买开的一定要启动要不然的话他可能会报错因为这个时候你要去操作数据库好爆红了爆红之后咱们可以看一下这块到底是哪一块有问题说你这个Docker有问题什么index什么name这块写的还是有问题是吧我看看index name
[02:45] 说你这个东西已经存在了为什么你还要去保存呢好因为这个咱们当前的这个类这个方法或者这个表这个表中你可以去打开设计表里边的所以里边是内幕是一个所以都说它重复的话不行因为它这个是一个unique它是唯一所以所以说这块你肯定是有问题咱们可以再去检查一下咱们的代码开这主要还是这个代码
[03:15] 就在那边啊好他get i contents name remove i包含就删除包含就删除他没有问题感觉啊说他不等于none最终amplify好这样咱们可以在这打断点好吧咱们再去执行一下啊走感觉上没有问题啊打断点的咱们再来去调试一下看看到底是哪里出了问题啊
[03:50] 他肯定会到这怎么没有东西了呢我删了啊就关掉省的影响好没有问题啊好到这了啊那到之后呢你可以简单的去看一下这个这个里边的值啊这个查出来两个是吧一个DAO客一个是扎罗是吧没问题这个呢是里边有三个对吧你可以看一下啊呃咱们分别是扎罗DAO口和888s ss是吧行那咱们下面就往下执行首先我循环的是他
[04:36] 它循环三次然后就去循环这个东西好第一次没有删第一次没有删然后再往下看然后这次删了是吧删了再走一次这次又没有删是吧ok没有删好你可以看一下这里边这里边有几个值这里边是有一个Docker和一个8888SSS是吧这个是不对的不对的又是为啥说不对的呢
[05:09] 因为这个Docker其实咱们已经存在了存在的话那就不应该存到这应该是只留下当前谁当前8888SS我简单看一眼咱们看一眼看看到底是哪个问题好这个其实这样咱们可以稍微改一改怎么改咱们把这个服务给停了是吧停了之后看这块你把这个循环咱们给它换一换把这个循环放到外边放到外边外边把下边是放到放到下边
[05:41] 咱们先去试一试一会我再去解释为什么要去这么改行现在你不用不用动只是把这个签套的方式稍微改了改好吧这时候咱们可以再来去测试一下走dbug然后放到这还是放到这咱们可以打断点再去看一看看看到底能不能进行这种是保存或者说有没有报错好稍等来看一看好正在运行稍等有点慢是吧
[06:27] 好到这了到这之后咱们可以往下走走走走走走还删了一个是吧好再往下看看看没有删除第二个删除第二个是吧我可以再往下好到这之后你可以看一下当前天p labels里边这是就是那一个没问题为什么刚才出现问题其实这样因为这个你一旦删除之后它是大循环有可能会少一次循环
[06:58] 比如说你删除一个它就可能这个下标就没了没了之后它就可以把这个集合给更新了更新完之后你可能就少于4集合那少于4集合的话有可能就把当前的Docker给跳过了明白了吧所以说咱们把这个不动的循环就是咱们不改变的当前这个集合放到外边OK这样的话就解决这个问题了好咱们再往下看看看能不能保存好吧走保存也没有问题最终这个里边就三条数据是吧你看
[07:27] 就是当前的Docker还有一个当前的8888SS这个是新增的一张数据好吧现在我们直接放行看看他最终过返回的是啥返回的是不是2129106你可以看一下29006是谁怎么可以到最后刷新一下29106是不是刚才这个字母趴了目前这个方法咱们就算是扫完了也没有任何问题好吧

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中编写并调试一个用于过滤标签的 Service 层方法，并通过单元测试验证其功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：
- 显示了 IntelliJ IDEA 中的项目结构，当前打开的文件是 `AdLabelServiceImp.java`。
- 代码内容：在 `addLabel` 方法中，创建了一个 `AdLabel` 对象，设置其属性（name, type, createTime），并调用 `adLabelMapper.insert(adlabel)` 插入数据库。
- 代码片段：
```java
private AdLabel addLabel(String label) {
    AdLabel adlabel = new AdLabel();
    adlabel.setName(label);
    adlabel.setType(true);
    adlabel.setCreateTime(new Date());
    adlabelMapper.insert(adlabel);
    return adlabel;
}
```

画面 2：
- 显示了测试类 `AdLabelServiceTest.java` 的开头部分。
- 代码内容：导入了 `@SpringBootTest` 和 `@RunWith(SpringRunner.class)` 注解，定义了测试类 `AdLabelServiceTest`。
- 代码片段：
```java
package com.heima.crawler.Service;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
@RunWith(SpringRunner.class)
public class AdLabelServiceTest {
```

画面 3：
- 显示了在测试类中编写测试方法 `test1()` 的过程。
- 代码内容：在方法中调用 `adLabelService.getLabelIds(labels: "java, Docker, 8888xxxx")` 并打印结果。
- 代码片段：
```java
@Test
public void test1() {
    String labelIds = adLabelService.getLabelIds(labels: "java, Docker, 8888xxxx");
    System.out.println(labelIds);
}
```

画面 4：
- 显示了测试方法 `test1()` 的执行结果。
- 控制台输出：`rationSHEnhancer:SpringOCLIB$18eda9fc1 is not eligible for getting processed by all BeanPostProcessors (for example; not eligible for auto-proxying)`。
- 说明：测试执行成功，但有 Spring 的警告信息。

画面 5：
- 显示了测试执行时的日志输出。
- 日志内容：显示了线程池关闭、HikariCP 数据库连接池关闭等信息。
- 日志片段：
```
2019-10-22 21:02:47,500 [DEBUG] Thread-5 log.springframework.scheduling.concurrent.ThreadPoolTaskExecutor: Shutdown (shutting down ExecutorService)
2019-10-22 21:02:47,500 [DEBUG] Thread-5 log.springframework.scheduling.concurrent.ThreadPoolTaskExecutor: Shutdown (destroying PA EntityManagerFactory)
2019-10-22 21:02:47,500 [DEBUG] Thread-5 log.zaxxer.hikari.pool.HikariPool-1: close [HikariPool-1] - Shutdown completed.
```

画面 6：
- 显示了测试类 `AdLabelServiceTest` 的完整代码。
- 代码内容：测试类中包含 `@Autowired` 注入的 `AdLabelService` 和 `@Test` 方法 `test1()`。
- 代码片段：
```java
@Autowired
private AdLabelService adlabelService;

@Test
public void test1() {
    String labelIds = adLabelService.getLabelIds(labels: "java, Docker, 8888xxxx");
    System.out.println(labelIds);
}
```

画面 7：
- 显示了 `AdLabelServiceImpl.java` 中的 `addLabelList` 方法。
- 代码内容：方法用于过滤模板标签列表，移除与已存在标签重复的标签。
- 代码片段：
```java
private List<AdLabel> addLabelList(List<String> tmplLabels, List<AdLabel> adlabelList) {
    if (tmplLabels != null && !tmplLabels.isEmpty()) {
        for (int i = 0; tmplLabels.size(); i++) {
            for (AdLabel adlabel : adlabelList) {
                if (tmplLabels.get(i).contains(adlabel.getName())) {
                    tmplLabels.remove(i);
                }
            }
        }
    }
}
```

画面 8：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`tmplLabels` 初始大小为 3，`adlabelList` 初始大小为 2。
- 调试信息：
```
tmplLabels = (ArrayList) size = 3
0 = Collecting data
1 = Collecting data
2 = Collecting data
```

画面 9：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`tmplLabels` 大小变为 2，`adlabelList` 大小仍为 2。
- 调试信息：
```
tmplLabels = (ArrayList) size = 2
0 = Collecting data
1 = Collecting data
```

画面 10：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`tmplLabels` 大小为 2，`adlabelList` 大小为 2。
- 调试信息：
```
tmplLabels = (ArrayList) size = 2
adlabelList = (ArrayList) size = 2
```

画面 11：
- 显示了 `addLabelList` 方法的完整代码。
- 代码内容：在过滤标签后，如果 `tmplLabels` 不为空，则将其添加到 `adlabelList` 中。
- 代码片段：
```java
if (tmplLabels != null && !tmplLabels.isEmpty()) {
    adlabelList.addAll(addLabelList(tmplLabels));
}
```

画面 12：
- 显示了调试模式下 `addLabelList` 方法的执行过程。
- 调试信息：`adlabelList` 大小变为 1。
- 调试信息：
```
adlabelList = (ArrayList) size = 1
```

画面 13：
- 显示了 `addLabelList` 方法的完整代码。
- 代码内容：方法最后返回 `adlabelList`。
- 代码片段：
```java
return adlabelList;
```

画面 14：
- 显示了测试类 `AdLabelServiceTest` 的测试方法 `test1()` 的执行结果。
- 控制台输出：`Tests passed`，表示测试通过。
- 代码片段：
```java
@Test
public void test1() {
    String labelIds = adLabelService.getLabelIds(labels: "java, Docker, 8888xxxx");
    System.out.println(labelIds);
}
```

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
见上文各画面的代码片段。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

