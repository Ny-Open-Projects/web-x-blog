# 22_数据保存_频道_service_查询频道信息

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day09-黑马头条-爬虫内容解析
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day09-黑马头条-爬虫内容解析\22_数据保存_频道_service_查询频道信息【海量资源尽在 666java.com】.mp4
- 时长 9分8秒（音频 548s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好咱们就继续讲刚才咱们是把第一个方法给已经完成了然后下面还有一个咱们的实现里边还有一个方法这个方法咱们也要去做一次这个方法是干嘛的呢就是通过根据当前的标签的IDIT的字符串它是以逗号分割最终你要查出来什么查出来一个Channel ID返回一个Channel ID你只要返回一个integer就可以了
[00:30] 咱们也有需求如果说他要是没找到当前的这种频道的话默认返回谁默认返回0是未登类OK咱们在这先去定义一个东西叫integer我先去定义一个channel的IDchannel的ID等于0然后下面咱们就可以通过当前的东西去直接去直接去查询是吧通过当前的label 去查询但是咱们在这
[01:00] 也是打印一个东西我打印的就是设一个tackage好这是execution好咱们在这里边就可以去查询了咱们这个地上咱们在这去写了一个方法冲刷那个方法然后咱们是dd-tino然后是by-label-ids这个参数就是当前的label-ids
[01:35] 反回的就是当前这个China ID好咱们先把这个主方法就是最主要的方法咱们先点出来最终咱们在这就可以去打印一个日志日志的话就是错误日志是吧说什么呢说获取China信息失败然后是咱们有一个 error message我们就可以设置一个错误信息1.get message
[02:07] 这个咱们就算是说着了最后你把这个channel id给返回就行了然后下面咱们再去写第二个方法就是前的这个方法这个方法其实主要业务都在这里边是吧好我们来看一下这个方法该怎么去写呢就咱们这样咱们也是按照之前的方式去写首先咱们也要在这去记录上前的什么这种时间好时间给记录一下
[02:37] 那这里面最主要的业务呢就是通过当前查询出来当前的China ID就可以啊去查询出来啊现在咱们就往下面去写代码这去设立一个先去写写这些东西吧比如说咱们要获取的获取China信息然后呢是交签的ids交签ids呢其实就是咱们的参数是吧还有呢没了是吧
[03:09] 这样咱们就做到这就可以这东西给删了然后下面咱们就这个参数label 给打印一下下面咱们就可以再去设置你也先去做一个判断最好判断就是label string utils.is not complete然后label 如果说它不为空的话这时候咱们再去操作好吧这时候咱们先在这先在这去
[03:38] 设置一个东西怎么设置呢integerPanelID还是等于0最后我们再去获取当前这个ID就可以了刚才说了这个它是一个什么串123是不是一个这种字符串并且是以字号分割是吧所以说你要干嘛对你要去进行对进行分割
[04:07] 那分割的话其实跟咱们之前的一样咱们也可以直接让它转成一个什么转成一个当前的字母范LabelList等于一个Race.js这里边咱们可以写LabelIds.Split这是一个数组是吧直接就转成了当前的一个集合为什么转成集合呢因为转成集合之后咱们就可以用ADLabel
[04:38] myport.curry根据当前的label 去查询就把这个label list装进去最终它返回的就是一个adlabel的集合好那拿到这个集合之后咱们首先要去判断还是要非空判断那不等于当前的什么adlabel list并且adlabel list.isempty里面啊通常会忘加一个非
[05:08] 那不为空的话呢那这时候呢咱们就可以去拿东西了可以这样啊咱们再去封装一个方法叫atadchannel什么呢id啊by labelid根据当前的labelid去查询这个啊咱们咱们之前也说过这个id啊直接附到这啊也说过这个东西呢这个东西啊咱们
[05:41] 复制的时候参数怎么默认如果说你要是查出来之后怎么不可能这三个比如说查出来三个怎么不可能这三个都查出来咱们只按照什么默认是几个默认是第一个对默认是第一个所以说咱们在这直接去设置一个三重就可以了d label list.get0.get什么的OK那就可以了
[06:10] 行这个设置完之后咱们这个方法也可以去念出来好这个方法咱们一会再完成接着往下走最终如果说你的穿透ID已经拿到了最好还干嘛还得去建议再去做一个判断因为防止出错如果说他等一浪怎么办呢有一浪吗那就是零不然就是还是穿透ID好吧重新附下值这写错了这是冒号OK好了行这个
[06:39] 这时候就算是完成了这时候咱们就可以打印入字包括点info里边写说获取China信息完成标签是啥标签是当前的又在写用英文的好再往下咱们是有一个China ID是谁好然后还有一个就是耗时是多长时间
[07:12] 号识一个标签就是label 然后第二个是channel ID三个就是system.current然后减去当前的一个量就完了好这个号识我们也拿到了好吧你把这个return当前channel ID就可以了好目前的话还有一个方法没完成是吧咱们下面我来去
[07:41] 通过这个方法去完成这个方法其实已经很明显了你要查询当前Channel ID并且是通过Label ID其实咱们之前都知道就是通过哪个中间表是吧你说通过这一列去查询对列那很简单来看一下怎么写其实咱们就可以直接去通过当前的什么当前的这种ID有一个叫Channel Myport.select
[08:09] label id我们可以把前label id装进去这个改了名影像一些label id好把label id装进去它返回的就是一个ad channelad channel table好咱们下面就可以去做一个判断说ad channel它不等于num不等于num的时候咱们就可以通过它点get什么的一个channel id
[08:40] 这个其实就是一个channel id这个就是channel idchannel id最终你直接去return就可以了也这么干吧再多定义一个等于0然后把它给删了最终你把channel id返回就可以了好吧目前这个方法咱们就给完了咱们一会就再来去测试一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示在 IntelliJ IDEA 中开发一个 Java 服务类（AdLabelService）的代码实现过程，包括方法定义、异常处理、日志记录和数据库操作。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1：展示 `addLabelList` 方法的代码，包含一个 for 循环用于遍历 `adLabelList` 并移除 `tplLabels` 中包含的标签。
画面 2：展示 `getAdChannelByIds` 方法的代码，其中包含一个 try-catch 块，用于捕获异常并返回 null。
画面 3：展示 `getAdChannelByIds` 方法中，创建 `adLabel` 对象并设置属性，然后调用 `adLabelMapper.insert` 方法。
画面 4：展示 `getAdChannelByIds` 方法中，使用 `Log` 类记录错误日志，日志内容为“获取channel信息失败”。
画面 5：展示 `getAdChannelByIds` 方法中，使用 `Log` 类记录信息日志，日志内容为“获取channel信息，标签ids: 0”。
画面 6：展示 `getAdChannelByIds` 方法中，使用 `StringUtils.isNotBlank` 方法判断标签 ID 是否为空。
画面 7：展示 `getAdChannelByIds` 方法中，使用 `Arrays.asList` 方法将标签 ID 字符串数组转换为 List。
画面 8：展示 `getAdChannelByIds` 方法中，调用 `adLabelMapper.queryAdLabelIds` 方法查询标签 ID。
画面 9：展示 `getAdChannelByIds` 方法中，调用 `getAdChannelIdByLabelId` 方法获取 channel ID。
画面 10：展示 `getAdChannelByIds` 方法中，记录日志“获取channel信息完成，标签: 0, channelId: 0”。
画面 11：展示 `getAdChannelByIds` 方法中，使用 `System.currentTimeMillis()` 计算耗时。
画面 12：展示 `getAdChannelByIds` 方法中，使用 `Arrays.asList` 方法将标签 ID 字符串数组转换为 List。
画面 13：展示 `getAdChannelByIds` 方法中，使用 `adChannelLabelMapper` 查询标签 ID。
画面 14：展示 `getAdChannelByIds` 方法中，使用 `StringUtils.isNotBlank` 方法判断标签 ID 是否为空，并记录日志“获取channel信息完成，标签: 0, channelId: 0, 耗时: 0”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1：
```java
private List<AdLabel> addLabelList(List<String> tplLabels, List<AdLabel> adLabelList) {
    if(tplLabels==null && !tplLabels.isEmpty()){
        for (AdLabel adlabel : adLabelList) {
            if(tplLabels.get(i).contains(adlabel.getTagName())){
                tplLabels.remove(i);
            }
        }
    }
}
```

画面 2：
```java
@Override
public Integer getAdChannelByIds(String labelIds) {
    Integer channelId = 0;
    try {
    } catch (Exception e) {
        return null;
    }
}
```

画面 3：
```java
adlabel.setTypes(true);
adlabel.setCreatedTime(new Date());
adlabelMapper.insert(adlabel);
return adlabel;
```

画面 4：
```java
log.error("获取channel信息失败");
return null;
```

画面 5：
```java
log.info("获取channel信息，标签ids: 0");
```

画面 6：
```java
if(StringUtils.isNotBlank(labelIds)){
```

画面 7：
```java
List<String> labelList = Arrays.asList(labelIds.split(regex, ""));
```

画面 8：
```java
List<AdLabel> adlabelList = adLabelMapper.queryAdLabelIds(labelList);
```

画面 9：
```java
channelId = getAdChannelIdByLabelId(adlabelList);
```

画面 10：
```java
log.info("获取channel信息完成，标签: 0, channelId: 0");
```

画面 11：
```java
long start = System.currentTimeMillis();
```

画面 12：
```java
List<String> labelList = Arrays.asList(labelIds.split(regex, ""));
```

画面 13：
```java
AdChannelLabel adChannelLabel = adChannelLabelMapper.selectByLabelId(labelId);
```

画面 14：
```java
log.info("获取channel信息完成，标签: 0, channelId: 0, 耗时: 0");
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

