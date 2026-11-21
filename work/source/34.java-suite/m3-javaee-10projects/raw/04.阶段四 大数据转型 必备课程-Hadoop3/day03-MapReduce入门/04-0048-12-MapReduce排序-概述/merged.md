# 12-MapReduce排序-概述

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day03-MapReduce入门
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day03-MapReduce入门\12-MapReduce排序-概述【海量资源尽在 ubkz.com】.mp4
- 时长 4分32秒（音频 273s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 在学习完MapReduce的分区之后接下来我们来学习MapReduce的序列化和排序咱们先看这个序列化什么是序列化呢在加文里面呢所谓的序列化呢就是将一个对象转成一个字节流比如说呢我们要将一个对象呢保存在磁盘上或者通过网络的方式进行传输那这个时候呢必须要做序列化那反序列化呢
[00:30] 和序列化刚好相反比如说我们要从磁盘上读取一个对象或者从一个网络中呢接收一个对象这个时候呢我们要去做反序列化那在Java中如何去实现序列化呢有一个接口叫Serializable我们只需要实现这个接口就可以实现序列化但是我们的Hadoop呢并没有使用我们Java这一套它认为呢我们Java中的一个序列化呢
[00:59] 比较臃肿或者说呢在加尔的序列化里面呢他加了很多一些附加的信息比如说一些教验呢或者一些继承体系啊所以说呢它的效率不是太高那Hadoop呢为了去实现这个序列化他开发了自己的一套机制OK他不用我们加尔那套他自己开发的开发之后呢他呢可以做到什么呢你想序列化哪个属性你就传输哪个属性这样呢
[01:27] 大大减少了网络开销那我们Hadoop里如何去实现序列化呢这里有个接口叫WriteableOK我们Hadoop就是通过这个Writeable接口来实现序列化也就是说如果你想让你的类去实现序列化只需要去实现这个接口就可以了来我们来看一下打开我们的ID在这里我们输一个Ctrl加N我们开在这个一个
[01:56] Writeable回车这是一个Writeable接口只要实现了这个接口就可以实现一个Hadoop的序列化这里边有两个方法我们要去重写OK那这个Write的方法是实现一个序列化的一个方法而这个ReadFields呢是实现一个反序列化的一个方法好这是关于序列化那这里边呢还有一个呢此接口叫WriteableCompareable这个呢
[02:27] 它是WriteAble的一个子接口这个WriteAbleCompatible呢它不仅可以实现序列化它呢还可以实现排序功能也就是说如果你实现了这个接口那你的对象呢不仅可以实现一个序列化而且呢还可以用来做排序我们来看一下这个来在这里呢我们搜一下Ctrl加N我们搜一下WriteAble
[02:59] OK,Writeable,然后Compatible我们来看,OK,就是这个接口你发现这个接口呢它自己继承了一个Writeable和一个CompatibleOK,而这个Compatible呢它是一个负接口而我们刚才呢这个Writeable,Compatible呢它是一个子接口OK,这是它们之间的关系所以说我们今天呢要给大家讲这个序列化和排序呢其实就记录一个结论
[03:27] 不管是实现序列化也好还是排序也好我们只需要去实现一个writeablecopyable接口就可以了好那接下来呢我们这里有一个案例这个案例呢是这样的这里有些数据这个数据呢是一个字母然后呢后面加上一个数字那么我们需要干嘛呢我们需要呢使用mypreduce对这个一组数据进行排序
[03:56] 排序的规则是什么呢如果说你前面都是A前面都是单是一个字母那我就按照字典顺序来排A呢在最前面那B呢在后面如果说你两个都是A那我再按照后面这个数字进行排序你比如说呢A1在前面A9呢在后面按照这个数字的升序排那要实现这个功能我们就要用到我们的一个序列化和排序好那咱呢
[04:25] 这个序列化和排序的概念咱先说到这里接下来我们就来实现这么一个功能

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 MapReduce 中的序列化与排序机制，重点介绍 Writable 和 WritableComparable 接口的使用。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示 IDE 中的项目结构和 WritableComparable 接口的源码，光标在接口定义处。
画面 2: 在 IDE 中搜索类名，弹出搜索结果，高亮显示 WordCountReducer。
画面 3: 在 IDE 中高亮显示 Writable 接口的 write 和 readFields 方法。
画面 4: IDE 窗口下方出现两个 Typora 文档窗口，显示课程笔记。
画面 5: Typora 中显示 PPT 内容，标题为“6. MapReduce序列化和排序”，介绍序列化、反序列化、Writable 和 WritableComparable。
画面 6: Typora 中 PPT 页面，展示数据格式和排序要求。
画面 7: IDE 中光标在 WordCountReducer 类名上，下方显示“void readFields(DataInput var1) throws IOException;”。
画面 8: IDE 中搜索“Writable”，弹出 Maven 依赖列表，高亮显示 WritableComparable。
画面 9: IDE 中显示 JobMain.java 代码，设置 Reduce 任务数、输出格式和路径。
画面 10: Typora 中 PPT 页面，展示数据格式和排序要求。
画面 11: Typora 中 PPT 页面，展示排序要求。
画面 12: Typora 中 PPT 页面，展示排序要求和解决方案。
画面 13: Typora 中 PPT 页面，展示数据格式和排序要求。
画面 14: Typora 中 PPT 页面，展示数据格式和排序要求。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 9 代码：
```java
//设置Reduce的个数
job.setNumReduceTasks(2);
//第八步:设置输出类
job.setOutputFormatClass(TextOutputFormat.class);
//设置输出的路径
TextOutputFormat.setOutputPath(job, new Path("hdfs://node01:8020/wordcount_out"));
boolean b = job.waitForCompletion(true);
return b ? 0 : 1;

public static void main(String[] args) throws Exception {
    Configuration configuration = new Configuration();
    //启动一个任务
    int run = ToolRunner.run(configuration, new JobMain(), args);
    System.exit(run);
}
```

4) PPT 标题、架构图/流程图的结构、表格数据：
画面 5 PPT 标题：“6. MapReduce序列化和排序”
PPT 内容：
- 序列化(Serialization)是将结构化对象转化为字节流
- 反序列化(Deserialization)是序列化的逆过程
- Java 的序列化(Serializable)是一个重量级序列化框架
- Writable 是 Hadoop 的序列化格式，Hadoop 定义了这样一个 Writable 接口，一个类要支持可序列化只需实现这个接口即可
- 另外 Writable 有一个子接口是 WritableComparable，WritableComparable 是即可实现序列化，也可以对key进行比较，我们这里可以通过自定义 Key 实现 WritableComparable 来实现我们的排序功能

画面 6 PPT 数据格式：
```
a 1
b 3
a 7
b 10
```

画面 11 PPT 要求：
- 第一列按字典顺序进行排列
- 第一列相同的时候，第二列按升序进行排列

画面 12 PPT 解决思路：
- 将 Map 输出的 <key,value> 中的 key 和 value 组合成一个新的 key (newKey)，value 不变
- 里边就变成 <(key,value),value>，在针对 newKey 排序的时候，如果 key 相同，就对 value 进行排序

5) 无

