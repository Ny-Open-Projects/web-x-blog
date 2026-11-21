# 画面线理解：20-网站流量日志分析-获取PageView表模型

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\20-网站流量日志分析-获取PageView表模型【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:10, 02:39, 03:49, 04:56, 06:12, 07:44, 08:05, 08:35, 09:22, 10:35, 11:30, 12:32, 13:22, 14:26
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:17:06

1) 这一组画面整体在讲如何通过 Hadoop MapReduce 实现对 Web 访问日志的分析，核心是将连续的访问记录按会话（session）划分，并为每次访问分配序号（step）。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了原始的 Web 访问日志数据，包含 IP、时间戳、URL 等字段，用于后续分析。
画面 2: 展示了 MapReduce Job 的配置代码，设置输入路径为 HDFS 上的 `day07_weblog`，输出路径为 `hdfs://node01:9000/pageViewOut`，并设置了输入输出格式。
画面 3: 与画面 1 相同，再次展示原始日志数据。
画面 4: 展示了 MapReduce Job 的 Mapper 配置，设置 Mapper 类为 `ClickStreamMapper.class`，并定义了 Mapper 的 map 方法，用于解析日志行并提取字段。
画面 5: 展示了 MapReduce Job 的 Reducer 配置，设置 Reducer 类为 `ClickStreamReducer.class`，并定义了 reduce 方法，用于对数据进行分组和排序。
画面 6: 展示了 Reducer 中的辅助方法，包括将字符串转换为 Date、计算时间差等。
画面 7: 展示了 MapReduce Job 的配置代码，设置输入路径为 HDFS 上的 `day07_weblog`，输出路径为本地文件夹 `E:/bigdata/output`。
画面 8: 展示了 `Date` 类的源码，用于理解时间比较和格式化。
画面 9: 展示了 Reducer 中的注释，说明核心思想是将连续的访问记录按会话划分，并为每次访问分配序号。
画面 10: 展示了 Reducer 中的代码，用于处理单条数据，设置默认会话超时时间为 30 分钟。
画面 11: 展示了 Reducer 中的代码，用于处理多条数据，比较相邻记录的时间差，如果小于 30 分钟，则认为属于同一个会话。
画面 12: 展示了 Reducer 中的代码，用于处理多条数据，如果时间差大于 30 分钟，则认为是新的会话，并更新序号。
画面 13: 展示了 Reducer 中的代码，用于对 WebLogBean 对象按时间排序。
画面 14: 展示了另一组 Web 访问日志数据，包含 URL、时间戳等字段，用于后续分析。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 2:
```java
job.setJarByClass(ClickStreamPageView.class);
String inputPath = "hdfs://node01:9000/weblog/" + DateUtil.getYestDate() + "/weblogPreOut";
String outputPath = "hdfs://node01:9000/weblog/" + DateUtil.getYestDate() + "/pageViewOut";
Filesystem filesystem = Filesystem.get(new URI("hdfs://node01:9000"), conf);
if (filesystem.exists(new Path(outputPath))) {
    filesystem.delete(new Path(outputPath), true);
}
filesystem.close();
job.setInputFormatClass(TextInputFormat.class);
job.setOutputFormatClass(TextOutputFormat.class);
TextInputFormat.setInputPaths(job, new Path(inputPath));
TextOutputFormat.setOutputPath(job, new Path(outputPath));
job.setMapperClass(ClickStreamMapper.class);
job.setReducerClass(ClickStreamReducer.class);
job.setMapOutputKeyClass(Text.class);
job.setMapOutputValueClass(WebLogBean.class);
job.setOutputKeyClass(Text.class);
job.setOutputValueClass(Text.class);
boolean b = job.waitForCompletion(true);
return b ? 1 : 0;
```

画面 4:
```java
static class ClickStreamMapper extends Mapper<LongWritable, Text, Text, WebLogBean> {
    Text k = new Text();
    WebLogBean v = new WebLogBean();
    @Override
    void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] fields = line.split(" ");
        if (fields.length < 9) return;
        //将分出来的字段设置到WebLogBean中
        v.set("true".equals(fields[0]) ? true : false, fields[1], fields[2], fields[3], fields[4], fields[5], fields[6]
```

画面 5:
```java
@Override
protected void reduce(Text key, Iterable<WebLogBean> values, Context context) throws IOException, InterruptedException {
    ArrayList<WebLogBean> beans = new ArrayList<WebLogBean>();
    try {
        for (WebLogBean bean : values) {
            //为什么List里不能只放一个bean，而是要放多个bean？
            //因为要对多个bean进行排序，所以要放到List中
            WebLogBean webLogBean = new WebLogBean();
            BeanUtils.copyProperties(webLogBean, bean);
            beans.add(webLogBean);
        }
    } catch (Exception e) {
        e.printStackTrace();
    }
    //将bean按时间先后顺序排序
    Collections.sort(beans, new Comparator<WebLogBean>() {
        @Override
        public int compare(WebLogBean o1, WebLogBean o2) {
            try {
                Date d1 = toDate(o1.gettime_local());
                Date d2 = toDate(o2.gettime_local());
                if (d1 == null || d2 == null) {
                    return 0;
                }
                return d1.compareTo(d2);
            } catch (Exception e) {
                e.printStackTrace();
                return 0;
            }
        }
    });
```

画面 6:
```java
private String toStr(Date date) {
    SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.US);
    return df.format(date);
}

private Date toDate(String timeStr) throws ParseException {
    SimpleDateFormat df = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss", Locale.US);
    return df.parse(timeStr);
}

private long timeDiff(String time1, String time2) throws ParseException {
    Date d1 = toDate(time1);
    Date d2 = toDate(time2);
    return d1.getTime() - d2.getTime();
}

private long timeDiff(Date time1, Date time2) throws ParseException {
    return time1.getTime() - time2.getTime();
}
```

画面 7:
```java
job.setJarByClass(ClickStreamVisitView.class);
job.setMapperClass(ClickStreamVisitMapper.class);
job.setReducerClass(ClickStreamVisitReducer.class);
job.setMapOutputKeyClass(Text.class);
job.setMapOutputValueClass(PageViewsBean.class);
job.setOutputKeyClass(NullWritable.class);
job.setOutputValueClass(VisitBean.class);
boolean res = job.waitForCompletion(true);
return res ? 0 : 1;
```

画面 9:
```java
/*
以下逻辑为：从有bean中分出各次visit，并对一次visit中所访问的page按顺序标号step
核心思想：
就是比较相邻两条记录中的访问时间，如果时间差<30分钟，则将该两条记录属于同一个session
否则，就属于不同的session
*/
int step = 1;
String session = UUID.randomUUID().toString();
for (int i = 0; i < beans.size(); i++) {
    WebLogBean bean = beans.get(i);
    //如果只有1条数据，则直接输出
    if (i == beans.size() - 1) {
        //设置默认会话超时时间为30s
        v.set(session + "001" + key.toString() + "001" + bean.getRemote_user() + "001" + bean.gettime_local() + "001" + bean.getStatus());
        context.write(NullWritable.get(), v);
        session = UUID.randomUUID().toString();
        break;
    }
```

画面 10:
```java
//如果不止1条数据，则将第一条跳过不输出，遍历第二条后再输出
if (i == 0) {
    continue;
}
```

画面 11:
```java
//求最近两次时间差
long timeDiff = timeDiff(toDate(bean.gettime_local()), toDate(beans.get(i - 1).gettime_local()));
if (timeDiff < 30 * 60 * 1000) {
    v.set(session + "001" + key.toString() + "001" + beans.get(i - 1).getRemote_user() + "001" + beans.get(i - 1).getHttp_user_agent() + "001" + beans.get(i - 1).getBody_bytes_sent() + "001" + bean.getRemote_user() + "001" + bean.getHttp_user_agent() + "001" + bean.getBody_bytes_sent());
    context.write(NullWritable.get(), v);
    step++;
} else {
```

画面 12:
```java
//如果本次访问的是最后一次，则将本条直接输出
if (i == beans.size() - 1) {
    //设置默认会话超时时间为30s
    v.set(session + "001" + key.toString() + "001" + bean.getRemote_user() + "001" + bean.gettime_local() + "001" +
