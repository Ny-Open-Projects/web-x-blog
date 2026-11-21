# 11.支付渠道参数配置-根据服务类型查询支付渠道列表-交易服务接口测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\11.支付渠道参数配置-根据服务类型查询支付渠道列表-交易服务接口测试【海量资源尽在 666java.com】.mp4
- 时长 6分47秒（音频 407s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们来测试一下交易服务刚才写的这个根据服务类型来查询支付渠道的这个接口那么这个测试呢因为我们还没有写http的接口还没有写商户平台应用的接口所以这个测试我们只能走单元测试那走单元测试的方法我相信之前我演示过应该还没有忘吧我们来看一下当初呢我们是不是在写商户服务的时候老师也给大家测试过对吧
[00:29] 在哪呢比如你看在这儿这是不当初我们自己写的一个单元测试的方法对不对好那么这种测试方法呢在我们企业开发当中特别常见对于一些大型的Service呢都需要来进行单元测试好那我们现在来看一下那怎么进行单元测试呢我们现在要在哪里啊是不是在交易服务当中来进行单元测试那交易服务当中来进行单元测试的话好那首先呢我们是需要把这个包呢给它创建一下在我们说的这个
[00:59] test当中是不是啊在这儿那么我们来看一看这个目录好像还没有我们键一下和这个在SRC下边是不是有一个min与min平级的是不是有一个test对不对好在这儿那在这儿呢我们就需要来创建一个test好然后在test当中我们要做一件事是不是就是创建一个加码然后呢这儿呢我们是不是就可以有时候老是不对你看
[01:30] 这个加法应该变成这个颜色它没有变对不对很简单注意看啊我给你教你像这种情况呢只是它的工程没有识别出这个Maven的一个目录的结构的逻辑那我们就把它这个什么呀它这个POM文件给它刷新一下然后一刷新这个时候呢它应该图标就变过来了然后变过来之后呢注意这时候我们要做的事是不是叫创建包呀
[01:54] 下面我们刚才说了嘛我们准备做的事呢是把刚才我们写的这个Service的这个接口呢进行单元测试对不对所以这里边呢我们这么做通常我们写单元测试的话就是单元测试的类名和它的这个Service的类呢保持一致所以这里边呢我们就加一个test这样是吧好然后在前面呢我们是要加一些对注解的sprintboot test它的注解然后还有
[02:25] run with这个我相信大家应该之前都做过对吧还有如果打日志的话sl4j也加上好那下边我们要做的事是不是就是测试根据服务类型来查询支付什么渠道对不对好那加一个test没错吧好那么你要测哪个方法呢你要测哪个方法那我没找到这个方法嘛就是最后我们写的这个对吧所以
[02:55] 各位这个测试的方法的名字定义呢也是test然后加上一个这个方法名嗯好那么你是不是需要把刚才我们说的这个Service给它注进去因为现在它是同一个工程嘛虽然它是个double接口但是你是在同一个工程来进行调用嘛所以我们就用autowire来注入就可以了所以这里是就是配怎么样channel Service没错吧然后呢这儿我们是不是就开始调用啊调用哪个
[03:27] 是不是就是看一下是不是调用它是不是这个方法调用它然后呢传进谁是不是传服务类型服务类型的代码是不是它各位我这个方法是不是就OK了看懂了吧然后最后呢你可以打一个断点来看一下就行了我们这个测试呢我们现在就直接手动在这打一个断点来测行不行好但是
[03:56] 跑这个单元测试之前老师给大家说过啊说什么呀说他还会启动这个读Spring Boot的文件然后呢来启动整个工程所以为了避免double端口的冲突你把原来的这个交易服务给他停掉然后呢直接单独来跑这个什么单元测试方法我们主要测试我们刚才是不是Mapper是自定义的呀看看他能不能成功的来执行好那最终执行的结果应该是这么样一个结果对不对好
[04:26] 那注意看注意看因为我们测试的目的就是发现其中的bug好我们来看这里边它就返回了这么一个什么list对不对好这list大家看到是不是就是我们说的微信微信支付宝两个是不是都OK了是不是就返回来了对所以这个就是我们的一个什么单元测试至于这里边我给你一个建议虽然这个
[04:58] 看一下我们测试通过了但是我还是建议你在写这个MAP的时候一定要注意参数的映射啥意思呢假如说我们现在找到这个当初我们写的看好看好你现在你用这个PayChannelDTO是不是来接参PayChannelDTO是不是对应的是PayChannel这一张什么表吧所以这里边呢你注意看啊你是不是把这三张表子但是你看全返回了对不对所以我建议你为了更准确的进行参数映射你可以把这个信号
[05:29] 改成只取配channel表的数据看好是吧ID这个是支部渠道名称支部渠道代码对吧这样我觉得是更稳妥是吧也就是我们呢只取这几列然后呢正好映射到里头对吧那有时候老师刚才那你刚才怎么也是正确的你现在为啥要改它因为我跟你说刚才是正确的原因是因为它正好能够映射上啥意思就是它正好能找到那个字段
[05:58] 那硬舌糖你别忘了你看ID你看都重复了你没发现吗看吧包括这个channel的名称看见吗都重复了所以为了保险起见我们要建议你这么做你看这个channel的name和channel的code是不是就正好对应我们这个DTO里面channel的name和channel的code大家看到了吗所以有时候你这个代码你说运行通过了没问题了我跟你说它就会有一个潜在的bug所以这里面呢我们要这么做你学过mybthes应该知道老师为什么这么做对吧
[06:28] 也就是这三列正好映射你的DTO这三个属性好了那么这个就写完了这个呢就是我们说的交易服务来查询根据服务类型查询它的支付渠道的测试咱们就完成了吧好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过代码实现根据服务类型查询支付渠道，并展示对应的数据库表结构和前端配置页面。

2) 按时间顺序列出每张画面的要点：
画面1：展示文档“5.4.2.1 接口定义”，图示说明“服务类型”与“支付通道”的多对多关系，包含三个实体框（pay_channel、platform_channel、PLATFORM_CHANNEL/PAY_CHANNEL）及连接线。
画面2：IDE中展示项目结构，选中“src/main/java”目录，右侧编辑器显示RestTemplateTest.java代码。
画面3：IDE中鼠标悬停在“src”目录上，展示项目结构。
画面4：IDE中鼠标悬停在“target”目录上，展示项目结构。
画面5：IDE中选中“pom.xml”文件，右侧编辑器显示Maven依赖配置。
画面6：IDE中选中“src/main/java”目录，弹出“Create New Class”对话框，提示“Invalid VCS root mapping”。
画面7：IDE中编辑器显示TestPayChannelService.java，光标在注释“//测试根据服务类型查询支付渠道”后。
画面8：IDE中编辑器显示TestPayChannelService.java，光标在方法“queryPayChannelByPlatformChannel”中，显示方法签名。
画面9：IDE中编辑器显示TestPayChannelService.java，光标在“System.out.println(shanj_c20);”语句后。
画面10：IDE中运行后，控制台显示日志信息，包括“[project.name]”和“3.1.0”等。
画面11：IDE中调试器显示变量“l”的值为“PayChannelDTO{...}”，并高亮显示“channelName”和“channelCode”字段。
画面12：IDE中编辑器显示PayChannelDTO.java类定义，包含字段“channelName”和“channelCode”。
画面13：数据库管理工具中展示“platform_pay_channel”表，查询结果包含“CHANNEL_NAME”和“CHANNEL_CODE”字段。
画面14：展示文档“5.4.2 交易服务原始支付渠道查询接口（接口⑤）”，图示前端配置页面，包含“服务类型”和“支付通道”两个下拉框。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面5 的 pom.xml 依赖配置：
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
</dependency>
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-pool2</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
<dependency>
    <groupId>com.alibaba</groupId>
    <artifactId>fastjson</artifactId>
    <version>1.2.60</version>
</dependency>

画面7 的 TestPayChannelService.java：
@org.junit.Test
public class TestPayChannelService {
    @Autowired
    PayChannelService payChannelService;
    //测试根据服务类型查询支付渠道
}

画面8 的 TestPayChannelService.java：
public void testQueryPayChannelByPlatformChannel() {
    List<PayChannelDTO> shanj_c20 = payChannelService.queryPayChannelByPlatformChannel("platform_channel");
    System.out.println(shanj_c20);
}

画面12 的 PayChannelDTO.java：
@ApiModelProperty(value = "PayChannelDTO", description = "原始第三方支付渠道")
public class PayChannelDTO implements Serializable {
    private long id;
    @ApiModelProperty("支付渠道名称")
    private String channelName;
    @ApiModelProperty("支付渠道编码")
    private String channelCode;
}

画面13 的 SQL 查询语句：
SELECT * FROM platform_pay_channel ppc, pay_channel plc WHERE ppc.CHANNEL_CODE = plc.CHANNEL_CODE AND plc.CHANNEL_CODE = 'ALIPAY_MAP' AND ppc.PLATFORM_CHANNEL = 'platform_channel';

4) PPT 标题、架构图/流程图的结构、表格数据：
画面1 的 PPT 标题：“5.4.2.1 接口定义”，图示说明“服务类型”与“支付通道”的多对多关系。
画面14 的 PPT 标题：“5.4.2 交易服务原始支付渠道查询接口（接口⑤）”，图示前端配置页面，包含“服务类型”和“支付通道”两个下拉框。

5) 无。

