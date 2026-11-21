# 19-网站流量日志分析-数据预处理

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\19-网站流量日志分析-数据预处理【海量资源尽在 ubkz.com】.mp4
- 时长 12分4秒（音频 725s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来看一下大数据分析的第二步就是对数据做一个预处理所谓的预处理呢我们主要是呢去过滤一些不合格的数据然后清洗了一些无意义的数据对它的格式呢做一个统一这里边呢我们要实现一个预处理呢我们要去写这个myproducer的代码在这里呢我已经把代码给大家提供好了来打开我们的爱店在这里呢
[00:30] 这里边有一个包叫PIE就是预处理的一个意思在这里边呢有三个类我们来看中间这个类这个呢就是对于我们的数据做一个最前期的预处理其实我们对数据的预处理呢可能一次并不能达到我的要求我要做多次处理而这个PIE process是我们的第一次预处理我们来看一下我们从上到下看这个呢其实是一个MapReduce
[00:59] 你看这个类叫weblogpreprocess它继承了一个configured实现了一个to接口这个不就是我们的myproduce吗那么对于myproduce来讲呢我们来先看我们程序的入口也就是这里的mint方法我们来看一下这里有一个mint方法这个mint方法呢它创建了一个configuration对象然后启动一个任务来找一下这个run方法向上好这是run方法
[01:29] 这个run方法呢我们以前写过无数次那在这里呢哈我们来看我们首先呢去创建一个job对象然后呢打包的话呢要设置一个打包的一个类接下来我们来设置输入和输出这个没什么好说的其实对于myproducer来讲呢我们最关心的有几个参数那么输入的话呢我们用test input format那么输出的话呢我们用test output format在这里呢
[01:59] 大家看这里边一个Mapper我们来看这个Mapper我们这个Mapper用的是Weblog Pre Process Mapper这个Mapper是我们预处理的一个重点来我们按住Ctrl键进去好进去之后呢你会发现它两个在同一个文件其实这个Mapper这个类呢它是一个内部类前面加了一个Static是一个静态内部类这个内部类呢继承了一个Mapper
[02:28] 这个K是long writableV是一行的文本而这个K2是test这是non writable好那么我们来看一下这里边的一些代码这个地方呢它定了一个集合这个集合是hashset那么这个集合呢待会我们看到它的一个作用而这里边有一个setup方法在我们的myper里面呢setup其实是做一个初始化
[02:58] 那么这个呢是在我们第一次运行这个myproduce的时候它会执行这个里面干了什么事呢你看上面有一个集合它呢把在这个集合中添加了一些一些这个路径那这个呢其实主要是来过滤我们的URL的就是说我们向一个网站的服务器发送一些请求呢发送了一个请求之后呢在访问这个网页的时候呢它会访问很多一些静态的一些页面资源或者说静态的一些其他的资源
[03:28] 这些资源并不是我们想分析的那么这个时候我们需要把这些静态的没有什么分析意义的数据呢给它过滤掉所以说我在这定了一个集合把这些没有意义的一些路径呢添加到这个配几次这个集合中那么方便我们后期来使用那么这是setup接下来我们再向下看一个map这个map呢就干一件事情将我们的k1和v1转成我们的k2和v2
[03:57] 那我们来看在这个地方呢我们value是一行的数据我们拿到这一行的数据之后呢我们在这里做了一个事用这个weblogparser这个类它呢去调了一个方法叫pass拿到这个一行数据之后它返回了一个类叫weblogbin这个weblogbin是什么呢我们来按住control键进去哦这个原来是一个java bin类它封装了我们这个原始数据中所有的字段
[04:27] 来判断数据是否合法value的还有呢它的这个请求地址请求用户还有这个时区啦等等好我们再回来那也就是说这句话调了这个pass方法之后它将一行的数据进行了封装封装成一个加外并也就是weblog并那我们接下来看一看它的这个pass解析是怎么实现的我们来进来好进来之后呢我们来看一下
[04:55] 它在这个里面呢实现了weblogbin的一个封装那么拿到这个一行数据之后呢它在这里按照这个空格来进行了切分那这个空格切分呢你看我们的原始数据来看一下打开我们刚才的原始数据在这里你看这个是原始数据这个原始数据的字段呢中间是用空格来隔开的好那么也就是这个地方呢我们用这个空格来切分切分的时候呢我们来判断长度
[05:25] 那么这个里边大概有11个字段如果说呢你的长度的大于11我觉得你的这个数据才有意义如果说你这个切分之后这个数字的长度是小于等于11的我觉得你这个数据呢是不完整的我在这里呢给它附一根钥所以说呢其实就是判断你这一行是否是有效的一个日志数据好假如说有效我们就进来进来之后呢对这个
[05:53] weblogbin里面的数据呢进行复制复制复制在这里呢它做了一个日期的转换这个在第三列呢在第四列有一个日期它要对这个日期呢做一个格式转换OK转换之后呢把它设置到这个set设置本地时间好设置完之后呢分别设置其他一些字段在这里呢还做了一件事情它说如果你的程度大于12那这个时候呢它从11开始把剩余的字符串呢进行一个追加
[06:24] 追加之后呢设置这个http user2gint这个什么意思呢是这样的我们来看我们的原始数据在原始数据的最后一个参数我们来找一个吧这个位置这就是浏览器的一个类型那么这个我们是按照空格来切割的那最后一个地方呢你看它有很多的空格也就是切割的时候其实它会被切割成多份但是它们合在一起表示的是一个user2gint
[06:55] 那怎么做处理呢是这样的我们先把前面的切割切分成11份然后呢如果说最后还剩下很多的字段我们把它合在一起合在一个整体作为一个参数作为一个字段它是这样做的所以说呢如果大于12我把剩余的作为一个字段然后设置给这个U字二进的好 这样去做的那如果说呢你不是你不是大于12个那我就把
[07:24] 剩余的这个子弹呢设给U字二进它也就U字二进它呢可能有很多个空格你就走上面这个如果说它中间没有空格那就走这个好这是这个还有呢它做了一个判断它会判断你这个里边这个steadus也就是我们的响应状态是否是大于400如果说大于等于400的话呢比如说呢404出现了一些地质错误或者500出现了一些服务器异常
[07:53] 那么这些呢并不是一些有效的数据我在这里设置一个valuevalidvalid呢它呢其实是我们weblogbin的第一个字段这个判断数据是否合法到刚才这个地方那这个地方呢判断数据是否合法我们设为false好还有呢这个地方呢判断它是不是一个无效的时间如果是我们也设为false
[08:19] 那么我们最后呢在清洗完数据之后就可以根据这个触和false来判断这个数据是否有效好那么这是它的一个weblogbin它的一个解析不管怎么样经过这个方法之后它就可以将一行数据封装到weblogbin并且在每行数据呢做一个标记你是合法还是不合法好那么我们回到刚才这个位置
[08:48] 好,经过这么一个解析之后呢,我们终于得到了weblogbin这个对象。
[08:53] 接下来呢,我们来判断它是否为no,如果不为no,表示呢,我们的数据是有效的。
[08:59] 哦,在这里呢,我们又调了一个方法,这个方法呢,是对我们weblogbin中的数据进行过滤。
[09:06] 因为我们刚才说过了,当你访问一个页面的时候呢,它会产生很多无效的一些请求,比如说请求一些静态的图片了,那么要把这些资源给过滤掉。
[09:17] 怎么过滤呢?
[09:17] 我们来看一下这是一个集合这个集合中存的就是这些路径我要过滤的路径那我们来进来看这个方法进来这个方法很简单就是如果说你这个集合中包含了我想要的请求路径那我觉得你就应该被过滤掉我就给你设为false所以说呢这个地方也是set valid设成false也就是给它打个标记回来好打个标记之后呢接下来我们用这个k
[09:47] K呢其实就是我们这个地方的什么东西呢K我们来看一下量上翻这个K呢其实就是我们的test的对象我们用test呢来set一个值这个值就是weblogbin把它变成走串好set之后呢我们就通过上下文呢把我们的K2和V2写到下一集我们的K2就是我们的这个K而我们的V呢我们的V呢按这个地方我们的V是在向上
[10:17] 有个not readable也就是v呢其实是一个空置OK这个就把map写完了写完之后呢接下来我们再回到刚才的这个主方法里边去主方法来调run我们再看run我们刚才呢在这个地方map你会发现下面没有这个并没有这个radius因为我们只是做一些预处理并不需要把数据做一个合并所以说没有radius那么处理完之后呢
[10:45] 它直接写到结果文件那么经过这个预处理之后呢我们来看一下结果文件长什么样子在这里呢在我们的资料里面有一个有一个data目录有个input目录这是我们的原数据而在这里面有一个output1这里面是我们第一次处理之后的数据我们来打开看一下好用它打开打开之后你会发现这就是我们把原数据经过了一个第一级预处理
[11:16] 之后的结果你会发现前面都有一个标记标记这一行是否是有效数据这里边都是出那看看有没有false呢我们向下翻这个地方有个false这个就不是一个有效数据那么中间这个地方呢你看它这个地方是soh其实是我们的分隔符这个分隔符呢我们用的是-001所以说这个地方它显示什么soh其实是-001
[11:46] OK后面呢都是把这个格式呢进行了统一好这是经过第一步清洗那么经过清洗之后呢其实这个数据呢我们还要做进一步的一些处理好那么关于呢我们数据清洗它的一个内容呢我们就先说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何通过编写 Java 程序解析 Web 日志，提取关键信息并进行分类处理，最终输出到 Hadoop 分布式文件系统。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 PPT 页面“1. 主要目的”，图 2.4 描述了数据预处理流程：原始日志 → 数据清洗 → 用户识别 → 会话识别 → 路径补全 → 按用户会话文件。
画面 2：展示 IntelliJ IDEA 中 WeblogPreProcess.java 的 main 方法，启动 Job。
画面 3：展示 WeblogPreProcessMapper 类的 setup 方法，初始化 pages 集合并添加多个 URL 分类。
画面 4：继续展示 setup 方法，添加更多 URL 分类。
画面 5：展示 map 方法，调用 WeblogParser.parser 解析日志行。
画面 6：展示 WeblogParser 类的 parser 方法，解析日志行并设置 WeblogBean 的字段。
画面 7：展示 Notepad++ 中的原始 Web 日志文件内容，包含用户访问记录和 User-Agent 信息。
画面 8：展示 WeblogParser 类中处理 User-Agent 字段的代码逻辑。
画面 9：展示 WeblogBean 类的定义，包含多个私有字段和 set 方法。
画面 10：展示 WeblogPreProcessMapper 的 map 方法，过滤静态资源并写入输出。
画面 11：展示 WeblogPreProcessMapper 的 map 方法，处理日志行。
画面 12：展示 WeblogPreProcess.java 中配置 Hadoop Job 的代码，设置输入输出路径、Mapper/Reducer 类。
画面 13：展示 Notepad++ 中的处理后日志文件内容，包含过滤后的访问记录。
画面 14：展示 PPT 页面“2. 实现方式”，内容为 WeblogPreProcess 类的简化代码结构。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2：
```java
public static void main(String[] args) throws Exception {
    Configuration configuration = new Configuration();
    int run = ToolRunner.run(configuration, new WeblogPreProcess(), args);
    System.exit(run);
}
```

画面 3：
```java
static class WeblogPreProcessMapper extends Mapper<LongWritable, Text, Text, NullWritable> {
    // 用来存储url分类数据
    Set<String> pages = new HashSet<>();
    Text k = new Text();
    NullWritable v = NullWritable.get();

    @Override
    protected void setup(Context context) throws IOException, InterruptedException {
        pages.add("about");
        pages.add("black-ip-list");
        pages.add("cassandra-cluster");
        pages.add("finance-rhive-repurchase");
        pages.add("Hadoop-family-roadmap");
        pages.add("Hadoop-Hive-intro");
        pages.add("Hadoop-ZooKeeper-intro");
        pages.add("Hadoop-mahout-roadmap");
    }
```

画面 5：
```java
@Override
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    WeblogBean weblogBean = WeblogParser.parser(line);
    // 过滤js/图片/css等静态资源
    WeblogParser.filterStaticResource(weblogBean, pages);
    /* if (!weblogBean.isValid()) return; */
    k.set(weblogBean.toString());
    context.write(k, v);
}
```

画面 6：
```java
public static WeblogBean parser(String line) {
    WeblogBean weblogBean = new WeblogBean();
    String[] arr = line.split(" ");
    if (arr.length > 11) {
        weblogBean.setRemote_addr(arr[0]);
        weblogBean.setRemote_user(arr[1]);
        String time_local = formatDate(arr[3].substring(1));
        if(null == time_local || !"".equals(time_local) time_local = "-invalid_time-";
        weblogBean.setTime_local(time_local);
        weblogBean.setRequest(arr[6]);
        weblogBean.setStatus(arr[8]);
        weblogBean.setBody_bytes_sent(arr[9]);
        weblogBean.setHttp_referer(arr[10]);
        // 如果UserAgent元素较多，并且UserAgent
        if (arr.length > 11) {
            StringBuilder sb = new StringBuilder();
            for(int i=11; i<arr.length; i++) {
                sb.append(arr[i]);
            }
            weblogBean.setHttp_user_agent(sb.toString());
        } else {
            weblogBean.setHttp_user_agent(arr[11]);
        }
        // 如果没有UserAgent元素，就设置为默认值
        if (weblogBean.getHttp_user_agent().equals("")) {
            weblogBean.setHttp_user_agent("unknown");
        }
    }
}
```

画面 8：
```java
// 如果UserAgent元素较多，并且UserAgent
if (arr.length > 11) {
    StringBuilder sb = new StringBuilder();
    for(int i=11; i<arr.length; i++) {
        sb.append(arr[i]);
    }
    weblogBean.setHttp_user_agent(sb.toString());
} else {
    weblogBean.setHttp_user_agent(arr[11]);
}
```

画面 9：
```java
public class WeblogBean implements Writable {
    private boolean valid = true; // 判断数据是否合法
    private String remote_addr; // 记录客户端的ip地址
    private String remote_user; // 记录客户端用户名，忽略操作
    private String time_local; // 记录访问时间与日期
    private String request; // 记录请求状态
    private String status; // 记录请求状态
    private String body_bytes_sent; // 记录请求状态
    private String http_referer; // 用来记录从哪个页面跳转过来的
    private String http_user_agent; // 用来记录客户端的相关信息

    public void set(boolean valid, String remote_addr, String remote_user, String time_local, String request, String status, String body_bytes_sent, String http_referer, String http_user_agent) {
        this.valid = valid;
        this.remote_addr = remote_addr;
        this.remote_user = remote_user;
        this.time_local = time_local;
        this.request = request;
        this.status = status;
        this.body_bytes_sent = body_bytes_sent;
        this.http_referer = http_referer;
        this.http_user_agent = http_user_agent;
    }
```

画面 10：
```java
@Override
protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
    String line = value.toString();
    WeblogBean weblogBean = WeblogParser.parser(line);
    // 过滤js/图片/css等静态资源
    WeblogParser.filterStaticResource(weblogBean, pages);
    /* if (!weblogBean.isValid()) return; */
    k.set(weblogBean.toString());
    context.write(k, v);
}
```

画面 12：
```java
// 配置HDFS路径
FileSystem filesystem = FileSystem.get(new URI("hdfs://node1:9000"), conf);
if (filesystem.exists(new Path(outputPath))) {
    filesystem.delete(new Path(outputPath), true);
}
filesystem.close();

// 设置输入输出格式
job.setInputFormatClass(TextInputFormat.class);
FileInputFormat.setInputPaths(job, new Path(inputPath));

// 设置Mapper和Reducer类
job.setMapperClass(WeblogPreProcessMapper.class);
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(NullWritable.class);
job.setOutputFormatClass(TextOutputFormat.class);
FileOutputFormat.setOutputPath(job, new Path(outputPath));

// 等待Job完成
boolean res = job.waitForCompletion(true);
return res ? 0 : 1;
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1：
- 标题：1. 主要目的
- 图 2.4 数据预处理过程：
  - “原始日志” → “数据清洗” → “用户识别” → “会话识别” → “路径补全” → “按用户会话文件”

画面 14：
- 标题：2. 实现方式
- 内容：展示 WeblogPreProcess 类的简化代码结构，包括 Mapper 和 parser 方法。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

