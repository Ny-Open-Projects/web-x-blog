# 5.6 Flink程序调试

- 阶段：06.阶段六 冷链监控平台项目
- 章节：day5 Flink批处理与Table SQL
- 源文件：06.阶段六 冷链监控平台项目\day5 Flink批处理与Table SQL\5.6 Flink程序调试_【海量资源尽在 666java.com】.mp4
- 时长 5分21秒（音频 321s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 大家好下面呢我们来给大家介绍一下Flink程序的一个调试的一个过程这个调试的过程不单单是针对于dataset应用的一个调试针对于datastream的调试也是相同的过程那么为什么我们要来给大家讲解调试的一个过程大家可以想象得到在我们的分布式的一个集群中
[00:25] 那么在这种情况下我们必然要耗费很多的时间那么我们的程序逻辑呢又和数据无关
[00:52] 也就是说我们的程序逻辑正确对于小的数据集和大的数据集它运行的结果应该都是正确的对不对
[00:59] 所以基于这种情况下我们希望能够有一个非常简便的方式我不需要直接对接我的卡发卡数据我也不需要直接对接我的大量的文本文件的数据或者是说HDFS文件里面的数据我只是需要我有一个简单的数据集我就能够对它进行测试了那么这个测试呢我只是在我本地的这个环境里面进行测就OK了我并不需要把我的程序放到我们的Flink集群里面来运行
[01:28] 那么我们今天就给大家讲解一下我们这个调试的一个程序这个调试程序那么这个调试程序包含两部分从刚才我们解释过程中一部分来讲的话是说我的程序在哪运行那么如果我在本地运行其实就OK的那么我不需要在我们的服务器环境或者服务器集群里边来执行那么第二部分的话是说我们的数据集我希望如果有一个简单的数据集就可以直接运行而不需要
[01:58] 对接复杂的数据集那么我们来看一看我们的这个程序那么我们看一看我们上一次提交的一个程序这个程序来讲的话我们第一步设置我们的环境信息而这个环境信息呢我们有好几种方法第一种方法的话是叫getExecutionEnvironment是指我们当前这个程序运行的一个环境那么我们还有另外一个方法叫createLocalEnvironmentcreateLocalEnvironment它是什么意思呢
[02:28] 它是相当于是把我们的程序在当前的GVM下来执行这种GVM因为本身我们的程序可以放在我们机群环境里边那么其实就是机群的多台机器的一个GVM那么我们如果在我们本机我们本地的一个电脑里边来运行的时候我们可以使用Create Local Environment那另外一个的话是我们的数据集那么我们数据集我们设置数据源的时候我们可以
[02:57] 从我们的socket数据语言里边来读或者说从我们的Kafka数据语言里边来读或者读取一个文本文件但是呢如果我们知道我们的数据的结构是一个什么样子的结构我们就可以在本地的时候直接用一个java的一个对象java的集合类来设置就像我们在我们think demo里边案例里边给大家讲解的一样我设置一个arrow list
[03:21] 而给Aerolist的设置添加一些字符串那么此时我就可以用我们的dataset来或者说是用我们的这个form collection来直接把我们的java的一个集合封装成我们想要的dataset那么下一步就可以根据我们的dataset来做额外的一些处理比如说txt然后对于它来讲的一个mapmap方法那方法我可以创建一个
[03:51] 你有一个map function那么在这里边的时候我可以把我们的字符帅进行了一个更改我由一个s字符帅我变成了一个s加上一个什么呢比如说或者说是我们的用字符帅相加我们字符帅再加上我们的这个s这个时候我们就能够把我们的数据由一个结构变成了另外一个结构得到了我们一个新的一个dataset
[04:22] 或者在做额外的其他的一些操作比如说像K8或者说是像Group Group by我们什么呢Group by我们的G0个字段等等各种各样的一些操作那么此时我们并不需要关注我的数据语言到底是什么样子的我只需要验证我的逻辑是什么我关注点在我的逻辑上那么在这种情况下对于我们的开发过程其实是比较有用的我们当前这个例子非常简单
[04:50] 大家可以理解为是一个非常简单的一个dataset的一个应用但是实际的生产过程中实际的业务场景下整个业务逻辑可能会变得比较复杂那么在比较复杂的情况下如何简化一下我们在流程上的一些负担或者简化一下我们的一些流程那么对于我们开发整个过程是非常非常有利的这是我们给大家讲解的我们如何来调试本地的一个程序或者说是我们如何来调试程序给大家讲解到这

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何在 IntelliJ IDEA 中编写一个 Flink 批处理程序，通过创建 ExecutionEnvironment、定义数据集、使用 map 转换和 groupBy 操作，并最终将结果写入文件。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了 Flink 批处理程序的初始代码结构，包含设置执行环境、创建数据集和写入文件的代码片段。
画面 2: 在代码中调用 ExecutionEnvironment 的方法，弹出方法列表，显示了 createLocalEnvironment 等选项。
画面 3: 在代码中调用 text.writesText 方法，弹出方法列表，显示了 writeText、write、print 等方法。
画面 4: 代码中将 ExecutionEnvironment 设置为 createLocalEnvironment。
画面 5: 在代码中调用 text.map 方法，弹出方法列表，显示了 MapFunction、RichMapFunction 等类。
画面 6: 在代码中调用 text.map 方法，弹出方法列表，显示了 MapFunction 的方法。
画面 7: 在代码中定义了一个 MapFunction 的实现，弹出方法列表，显示了 MapFunction 的方法。
画面 8: 在代码中调用 text.map 方法，弹出方法列表，显示了 MapFunction 的方法。
画面 9: 在代码中调用 text.map 方法，弹出方法列表，显示了 MapFunction 的方法。
画面 10: 在代码中调用 text.groupBy 方法，弹出方法列表，显示了 groupBy 的方法。
画面 11: 在代码中调用 text.groupBy 方法，弹出方法列表，显示了 groupBy 的方法。
画面 12: 在代码中调用 text.groupBy 方法，弹出方法列表，显示了 groupBy 的方法。
画面 13: 切换到文档页面，显示了 Flink DataSet 和 SQL 基础教程的 1.5 节“调试程序”，其中 1.5.1 节“本地执行环境”介绍了如何使用 createLocalEnvironment。
画面 14: 切换到文档页面，显示了 1.5.2 节“收集数据源和接收器”，介绍了如何创建数据集和使用接收器。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
public class SinkDemo {
    public static void main(String[] args) throws Exception {
        //1.设置环境
        ExecutionEnvironment env = ExecutionEnvironment.getExecutionEnvironment();
        //2.设置输入源
        List<String> list = new ArrayList<>();
        list.add("def");
        DataSet<String> text = env.fromCollection(list);
        text.writeTextFile("d:\\1.txt");
        env.execute();
    }
}
```
画面 2:
```java
ExecutionEnvironment env = ExecutionEnvironment.
```
画面 3:
```java
text.writeText("d:\\1.txt");
```
画面 4:
```java
ExecutionEnvironment env = ExecutionEnvironment.createLocalEnvironment();
```
画面 5:
```java
text.map(new MapFunction<String, String>() {
    @Override
    public String map(String s) throws Exception {
        return s;
    }
});
```
画面 6:
```java
text.map(new MapFunction<String, String>() {
    @Override
    public String map(String s) throws Exception {
        return s;
    }
});
```
画面 7:
```java
@Override
public String map(String s) throws Exception {
    return s;
}
```
画面 8:
```java
text.map(new MapFunction<String, String>() {
    @Override
    public String map(String s) throws Exception {
        return s;
    }
});
```
画面 9:
```java
text.map(new MapFunction<String, String>() {
    @Override
    public String map(String s) throws Exception {
        return s;
    }
});
```
画面 10:
```java
text.groupBy();
```
画面 11:
```java
text.groupBy();
```
画面 12:
```java
text.groupBy();
```
画面 13:
```java
final ExecutionEnvironment env = ExecutionEnvironment.createLocalEnvironment();
DataSet<String> lines = env.readTextFile(pathToTextFile);
// build your program
env.execute();
```
画面 14:
```java
final ExecutionEnvironment env = ExecutionEnvironment.createLocalEnvironment();
// Create a DataSet from a list of elements
DataSet<Integer> myints = env.fromElements(1, 2, 3, 4, 5);
// Create a DataSet from any Java collection
List<Tuple2<String, Integer>> data = ...
DataSet<Tuple2<String, Integer>> mytuples = env.fromCollection(data);
// Create a DataSet from an Iterator
Iterator<Long> longIt = ...
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 13: PPT 标题为“1.5 调试程序”，子标题为“1.5.1 本地执行环境”，内容描述了如何使用 createLocalEnvironment。
画面 14: PPT 标题为“1.5.2 收集数据源和接收器”，内容描述了如何创建数据集和使用接收器。

5) 不要评价画面美观，不要输出与课程无关的内容。
只输出上述内容，不要客套开场白。

