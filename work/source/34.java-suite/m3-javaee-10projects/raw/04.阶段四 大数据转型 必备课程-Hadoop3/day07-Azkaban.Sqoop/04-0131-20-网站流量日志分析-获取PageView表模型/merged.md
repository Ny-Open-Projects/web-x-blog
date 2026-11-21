# 20-网站流量日志分析-获取PageView表模型

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\20-网站流量日志分析-获取PageView表模型【海量资源尽在 ubkz.com】.mp4
- 时长 14分41秒（音频 881s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们来继续刚才呢我们对数据做了一个清洗接下来我们在这个清洗后的基础上呢对数据呢做进一步的处理来看我刚开始给大家画的这张图那么左边呢是一个语言数据现在我们已经对这个数据做了一个格式的统一接下来呢我们需要在这个语言数据的基础上给大家得出一个PageView表模型也就通过它来得到这么一个表模型这个PageView表模型呢
[00:30] 要求啊在每一次访问的前面呢我要加上一个session加上一个session那么它俩呢如果他们的访问时间小于30分钟他们在一个session里面这两个每一条记录前面都要加session也就是我最终得的是什么格式呢应该是这么一个数据要求好session1这个也是session1不仅要这么一个数据我还要求呢后面呢有它的一个停留时间而且呢
[00:59] 在最后面呢还有这个session中你是第几个页面我要做这么一个事情还有呢我们需要对这个时间呢做一个排序这个是在我们清洗后的数据上我们要得出这样的一张表那怎么去做呢同学们我们可以这样做这个地方呢我们既然呢要按照这个时间排序而且呢它们的IP相同我们要去把它们放在一起排序
[01:28] 那你说这个地方要做MapReduce的时候我们应该把谁作为我们的K2呢来思考一下那么既然呢我们现在的要求呢同一个IP他们进行一起排序那这个时候我们就可以把IP作为K2然后呢你的IP相同他们就跑到同一个集合里面去然后我可以对这个集合呢按照时间排序而这个时间呢
[02:00] 我可以利用上一次的时间减下一次这个上一次访问时间然后减下一次时间我是不是就得出来他的一个停留时间如果你是最后一次访问这个页面我给你一个默认时间是不是就可以了而且我在排完序之后呢我可以对这个里面的每一条记录呢打一个标记也就是对对他呢做一个排序哎打一个标记123等等好那接下来我们就来看这个代码如何去实现好回到我们的ID
[02:29] 在这里呢我们有一个代码在clickstream也就是点击流里边呢有一个clickstream配置就是这个代码我们来分析一下这个代码的话呢首先要注意这个代码在分析的时候它的数据要来自上一次的一个输出我们刚才给大家讲了一个数据清洗你的输入目录必须是上一次的一个输出这个地方要注意一下好咱们看这个代码重点还是看myper和reducer
[02:59] 我们来看这个MAPR这个MAPR是这个我们打开这个MAPR呢首先呢它需要做一件事情将我的K1VE转成K2VR好我们这个是我们一行的文本数据一行的文本数据在这里而我们的K2VR呢K2是应该是我们的IPIP而VR呢是一个weblogbin也就是我们的那个javabin对象我们进来是这个bin对象
[03:29] 我们回来回来之后呢来回到我们刚才的位置好那么接下来呢我们来看这个map方法怎么去实现这个map方法这个map方法呢首先是拿到一行的数据也就是这里的value这里的value那么拿到这一行数据这一行数据长什么样子呢其实就是我们刚才分析后的这一行数据前面有一个true和false大家注意好拿到这一行数据之后呢我做一个切割
[03:58] 根据-001来切割切割完之后呢我来判断你的长度是否满足我的需求如果小于9我认为这个数据没有意义直接return好否则的话呢我给这个v设一个值这个v呢就是我们的v2这个v呢是谁呢是weblogbin好给它去设置值这个地方呢我一次性把它们全设置了第一个呢设为true或者false而后边这个地方呢分别切割完之后分别来设置
[04:27] 好 设置完之后呢我在这里做了一个判断那么VD is valid表示呢如果说你第一列是true我才写到下一季目录里面去注意我在这个里边只挑选前面是true的false的呢像这些是false的我就不选择所以说呢这地方加了一个判断只有是true我才写到下一季好 那么这就是我们的map方法非常简单
[04:56] 看完map之后呢咱们接下来再看看这个reduce好看看这里边有reduce因为我们要排序我们要合并所以说这里边呢应该有reduce来看click stream reducer进来好这是我们的reduce我们的reduce呢干了什么事呢我们来看这个地方呢定了一个集合这个集合里边放的是weblogbin好这个集合来干什么呢其实它就相当于把
[05:25] 这个集合中的数据转移到这个集合中去对它做一些排序了等等我们注意啊这个地方呢这个地方是K2这是VR那我们的K2呢是手机号相同手不是手机号说错了是IP这个相同的IP呢数据会放在同一个集合这要注意所以说呢我在这里呢我来编辑这个集合好编辑集合的时候呢我就会把相同IP的数据呢给它编辑出来
[05:54] 便利出来之后你看我在这里有new了一个weblogbin然后在这个位置用binutils来做一个深度拷贝相当于把这里的每个bin拷贝出拷贝到我自己的webbin里面去为什么要做个拷贝呢因为如果你不拷贝的话我在这里进行操作其实操作的还是这里面的weblogbin那么它这个时候它相当于多个引用都指向同一个对象所以为了避免出错我自己新建一个
[06:23] yvlogbin将这个etriterable这个集合中的数据给它拿出来放在我自己的集合OK那么这个地方呢就是把它每遍的一个添加到我自己的集合里面去这个for循环其实就完成了将这个reduce集合的数据拷贝了我自己的集合好做完这个事情之后呢接下来我们来看collection4.sort这个其实就是对我们自己的集合做一个排序
[06:53] 这个地方有个比较器它来指定一个排序规则我们刚才说过呢我要给每次访问的按照时间来排序而且我要打个标记对这个排序规则呢其实它比较的就是时间这个地方你看用compare to这个地方呢用第一这第一是一个时间第二呢也是一个时间通过compare to来比较时间那这个地方呢我们来看这个to data
[07:23] 这个to data呢其实就是把一个美国的时间呢转成我们一个本地时间然后呢最后呢对这个地方呢做一个解析OK解析完之后解成一个data对象好那么这个地方大家注意这个我再回到刚才这地方这个地方呢这个美国时间在哪里呢我们来看这个看这个地方你看我们拿到的这个时间稍等一下我们向后看一下向后看一下
[07:55] 好这个地方呢还看不出来是吧那我们回到刚才的位置好回到刚才的位置稍等一下回到刚才位置我们再进入这个Reducer进入Reducer好进来之后呢我们来继续去看继续看稍等一下继续进入这个Reducer应该在这上面来我们继续来到这位置这个Collection Sort好经过这个Sort之后呢我们对这个
[08:25] 每一条访问记录按照日期来进行排序排序的时候呢我们来看这个compare2稍等我们来进来这件compare2呢其实是将每个时间呢变成一个毫秒值它在排序的时候它其实比的毫秒值那么谁的毫秒值大那么谁的时间是不是最新呢根据这个规则来排序好经过这么一个经过这么一个操作之后呢我们集合的数据已经有序了
[08:55] 大家注意我们的集合数已经有序了好有序了之后呢接下来我们还没有完我们还要去统计每个页面的停留时间以及呢我们要在每个页面的访问的后面加一个编号你是第一个还是第二个好那这个怎么做呢我们来这样做我们是比较相邻的两条记录的时间差如果小于30分钟那么属于同一个session否则就属于不同的session来看一下首先呢因为他们呢
[09:25] 同一个集合里边放的都是IP地址一样的那这个地方呢我们首先呢生成一个UUID生成一个字幕串其实这个字幕串呢我们就把它当成一个session ID然后便利我们的集合好便利完之后呢我们从bin里边得到一个ylogbin对象得到第一个对象好如果说这个size等于1也就是说你数组的长度是1条相当于你这个相当于呢
[09:54] 你IP这个IP呢就一条记录那这个时候呢我就把这个数据呢直接向后写就行了那么即使是一条向后写我们看这个数据写的什么注意第一个我们要给它加上一个session这个session呢其实就是产生的这个字母串好后面呢是一个K变成一个字母串好这个K呢其实你就认为是手机号不是手机号是IPIP号OK这个K呢
[10:23] 应该是在上面已经写好了是这个就是这个我们的IP地址好那么这个IP地址拿到这个位置好在这里接下来呢是我们获取它的用户了获取它的一个时间了还有获取的请求路径了这个没什么好说的大家请看在这里这个地方的60其实是我们这个页面的停留时间这个地方是60秒其实这个值呢是写死的或者说给它一个默认值好在后面呢基本上就是
[10:53] 其他的一些参数好那么这个就行了写完之后呢我们来跳出再来我们向下看如果说i等于0那这个时候呢我们直接呢把它呢continue也就是这个时候呢其实没有必要向下走了直接回去就行了为什么这个i等于0要回去呢比如说我有三条记录其实我们有三条记录的话呢我们还要求这个一条记录与另外一条记录的时间差
[11:22] 如果你是第一条这个时间差我是求不出来的所以说这个肯定度之后呢下一次再进行这个循环i是不是1了好1那我就走这里走这里之后呢我们来看其实我们是求啊这个时间差这一次的时间和i-1就是上一次的时间减上一个时间差这个时间差是一个毫秒值然后我来判断这个毫秒值呢是否小于30分钟这就是一个30分钟好如果说小于30分钟
[11:51] 那么我们两个呢在一个绘画里边一个绘画里边这个时候呢你看我开始写了那这里面呢把V其实就是我们的一个test把这个呢给它去写上写上的话呢我来注意写上完了之后呢这个地方有一个有一个东西要注意这个step++这个表示我们的步数你是这个session中的第几步好把这个呢先后写这是小于三十分钟
[12:20] 那如果你俩不是小于30分钟那么你们俩是在不同的绘画中我们来走else那走else的话呢写数据还是一样的这个地方我step从一开始因为你俩不在一个绘画所以说呢我有另外起了一个step也就是步数表示你是第一次这个session的第一次好那么接下来呢我们来向后再走如果说呢按照这个循环的话如果是最后一条那这个时候呢
[12:49] 我们就直接写直接把这个数据呢向后写OK那这个是它的整个一个过程经过了这个过程之后呢你会发现我们的Session这个号编号有了我们的这个Step也有了我们来看这个Step在哪里在它的Step也在这里我们来看一下哎Step在这里我们的Step也有了如果你们同一个绘画那么Step就是1 2 3等等而且呢他们经过这个位置呢
[13:20] 也经过了一个排序那这个时候呢我们就把数据呢写到文件中OK这是它的一个map reduce一个核心的代码好写完之后呢我们呢可以把它放在机群上运行在这里我就不运行了我们来直接看这个代码结果好在这里呢我们有一个audit boot2刚才是audit boot1这个地方是audit boot2我们打开这个文件来看看它产生的结果走一下你看前边就是session
[13:49] 这个就是IP后面呢我们向后看向后看好这个地方应该就是它的一个仿那个部署就是你是这个session的第一个页面那我们再向下看看看有没有session一样的哎你看这三个session是一样的那session一样的话呢它就会按照时间来排序49 50 59好排完序之后呢并且给它打一个编号你看再向下看你看123
[14:18] 这个三项中的第一个页面第二个页面第三个页面OK那这个说明了我们就达到了我们一个要求就是我们要得到一个什么模型呢我们要得到一个配机view表模型OK得到这个模型之后呢我们就可以进行其他的一些分析好那么关于配机view表模型呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

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

