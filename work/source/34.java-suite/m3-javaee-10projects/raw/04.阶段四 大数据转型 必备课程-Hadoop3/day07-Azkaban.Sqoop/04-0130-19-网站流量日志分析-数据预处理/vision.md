# 画面线理解：19-网站流量日志分析-数据预处理

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\19-网站流量日志分析-数据预处理【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:17, 01:21, 02:39, 03:40, 04:37, 05:39, 06:37, 07:11, 08:02, 08:49, 10:14, 10:35, 11:25, 12:02
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:14:02

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
        pages.add("hadoop-family-roadmap");
        pages.add("hadoop-hive-intro");
        pages.add("hadoop-zookeeper-intro");
        pages.add("hadoop-mahout-roadmap");
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
