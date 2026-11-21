# 20.支付渠道参数缓存-缓存测试

- 阶段：09.阶段九 聚合支付平台-闪聚支付项目
- 章节：day05 支付渠道参数配置 Redis
- 源文件：09.阶段九 聚合支付平台-闪聚支付项目\day05 支付渠道参数配置 Redis\20.支付渠道参数缓存-缓存测试【海量资源尽在 666java.com】.mp4
- 时长 11分8秒（音频 669s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下边呢我们就来测试一下支付渠道参数缓存的具体的方法刚才我们已经实现了在保存支付渠道的时候呢我们看到它是不是要缓存对吧然后在查询支付渠道参数的时候也要缓存那我们一个一个测假如现在呢我们来保存支付渠道参数那保存的时候呢注意看啊我们在测试之前我们先要把这个给它交易服务重启一下嗯然后呢
[00:30] 重启的时候呢我们得思考一会儿呢我们怎么测对不对好然后呢这个三户平台应用也重启一下好那下面我们来看吧这个接口是不是就是支付渠道参数配置这是不是就是像我们的哪里呀这个支付渠道参数这边我们这个是不是就来保存了呀对吧我们之前是不是写代码如果有我们要更新是不是啊所以这个这个数据库
[00:58] 这个是没有关系的啊留在这也行反正不管是插入和更新我们都向Redis保存那我也有一点我们要用Redis连接对吧连接到我们的Redis来看一下啊刷新看一下啊现在我们看到这里头是没有东西的对不对那没有东西的话我们注意看啊我们把它起起来我们只要执行一个什么保存支付渠道参数好这个呢接口还正在向Nexus注册啊不要着急好
[01:28] 那下面呢我们是不是就可以怎么弄啊发送一下未知错误你猜是啥错这个我觉得大家应该遇到好多了是不是还是我们说的这个JCRO向Nexus注册的时候还没有注册成功是吧稍等一小会儿啊稍等一小会儿那么我们说当你去保存的时候向Redis保存那查询呢我们这个查询呢查询我们之前是不是在这个SWAG当中测试的以后我们也在这测一下行不行好来我们继续
[01:59] 执行应用没有绑定服务类型把这个干掉走哎为之错误这是咋回事看一下哎抛了个异常这是个空你看你点它你看这一点是啥空我想呃在save这个方法的时候对吧然后呢我们这抛了个异常来我把它清一下啊咱们再来测一下再执行好那来
[02:54] 咦看啥情况一只茶蕴好像类似于死循环的样子对不对来看一下啊这是茶蕴的这张表对吧好这张表应该是地归了看好看好走你看我这查的是你看我这个是保存缓存的时候对吧我现在是缓存的时候我现在查对吧那查的时候你看
[03:27] 你看你查的时候这里边是不是也调用了这个方法你看这是本身是不是查调用这个缓存大家看见了吗所以这里边你会发现它在查的时候呢它又调用了这个缓存缓存又调用查那是不是就是一个死循环呢对地归对不对那现在我们怎么做那我们应该在查询的时候呢对这里边保存缓存这里头
[03:57] 我们要注意一些怎么来不能让他再查那这个怎么做呢我们可以思考一下我们应该是在更新缓存这里更新缓存这里你是通过这个来查询对吧那么很简单我们不让他查这个我们换一个方法也可以实现查询行不行那换一个什么方法呢注意
[04:30] 原来你看一下我们查询的时候是怎么做的首先是不是找到他的ID然后呢我们是不是就得到了这个什么这个具体的list我不让他实现刚才说的这个什么地归调用就行了行不行就是如果说哎看好我根据APP的ID和服务类型code我来查查到绑定ID吧如果绑定ID
[05:01] 不为空我接下来做的事是不是就是准备查list对不对查完list之后呢是不是要将它存入我们说的redis这个过程就是我不让它调刚才外部的这个方法这不就行了吗OK好我们再来你会发现我们在写代码的时候这个难免会出现刚才我说的这种什么
[05:34] Bug甚至刚才我们出现一个典型的就是地归调用这个缓存的方法就调用这个查询查询又调用缓存缓存又调用查询那我们解决的思路就是呢不让它形成地归我在更新缓存的时候呢我不去调这个我们说的这个查询方法让它查我们呢通过Mapper来查这不就行了吗好那我们把它重启一下我们再来测试一下
[06:03] 这个bug我觉得特别好对吧大家在调试的时候呢也会出现这种稀奇古怪的问题啊好那我们再来执行你看这样就成功了吧成功了之后呢我们就可以在redis当中来刷新你看这个key看一下你看这个是不是就是我们说的这个key啊你看前缀是固定的对吧
[06:31] 中间这里是不是就是我们说的APP ID后边就是我们的服务类型那中间这一堆参数是不是就是我们说的什么啊是不是就是我们说的支付渠道参数配置的内容啊对吧好下面它呢是OK了接下来注意看啊我再给你测一个查询因为我们说嘛查询的时候要先查换存对我把断点打在这行不行看好啊
[07:05] 现在查询的方法我们要把断点打在这行不行来我要执行查询了也就是我不通过数据库我照样可以查到这个支付渠道参数那你打开SWG看好因为原来查询我们是通过SWG对不对来我们找到那个根据应用和服务类型来查询的这个什么这个测试看好走进来你看我现在是不是
[07:34] 如果存在redis我是不是从redis取出来了取出来之后我把jsonchart转成什么转成list对不对这个list呢我们要拿到就是这个走哎未知错误你看还是有问题你看好啊我们把它重启一下注意保存缓存是不是没有问题了下面我们是不是要做的是
[08:09] 查询的时候先从redis查如果redis没有我们要从数据库查保存redis对不对我们现在呢先看redis有的情况我们让它从redis取看能不能正常取出来大家理解我意思吧嗯好来看一下这个整个的测试呢我们还没有结束啊那我呢就在这儿来打断点行吧在这儿打断点然后呢这里边呢我们通过Swagger
[08:43] 来执行查询当然这个呢还是我刚才说的它这个Netcast的接口呢还是正在注册中啊稍等一小会儿好好那下边呢我们来点击这个执行然后它就进到了我们查询的方法好那这里边呢我们打断点来跟进一下首先取出key对吧然后因为现在呢Redis里面是有的所以这里边呢你看它就开始从Redis来查那Redis查的话大家来看最后中
[09:21] 查到了这个健身串是不是要转成我们说的list你看这个转成list里边的数据是不是就有了你看组件因为这个是从数据库查询出来数据库你看它根本没有那个什么APP ID所以APP ID是空这不要紧但是它有一个APP和服务类型的绑定ID也就是这个是数据库里边的记录是不是都被查出来了对吧所以这个就是我们说的什么查询的时候先从redis查
[09:50] 那好了那假如说现在呢Redis你看大家看Redis现在是不是有啊那如果说各位那我把Redis这个里头的这个东西啊咱们把它给删除我问你它是不是就没有了那么它没有的情况下各位我再来执行那你说这时候呢它从Redis它取它是不是就取不到取不到现在它是不是开始查数据库
[10:18] 对不对然后呢一直到这里开始更新那到这儿是不是就开始更新到Redis了那这时候你再来刷新Redis里面是不是就在查询的时候如果Redis里面没有它是不是就开始把数据更新到Redis里面这就是我们说的整个缓存的一个什么查询如果这个时候呢它又一次的来进行执行你会发现Redis就有了那么这时候呢
[10:47] 它就开始从Redis又取出来了对以上呢就是我们整个支付渠道参数缓存的一个具体的实现那么大家呢要仔细的去测试一下保存的时候呢添加缓存查询的时候呢先从缓存查然后呢再保存到缓存好

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在支付服务中通过 Redis 缓存查询支付渠道参数，实现先查缓存、缓存不存在则查数据库并写入缓存的逻辑。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了文档中“5.6.4 查询缓存”章节，说明查询渠道参数的逻辑：先从 Redis 查询，存在则返回，否则从数据库查询并存入 Redis。同时显示了要修改的代码方法名：queryPayChannelParamByAppAndPlatform。
画面 2: 展示了 Redis 客户端连接到本地 Redis 服务（localhost:6379），并显示了多个 key（如：sh1, sh2, ... sh14）及其值为 0，用于演示缓存数据。
画面 3: 在 IDE 中显示了 PayChannelServiceImpl.java 文件，其中 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 4: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 5: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 6: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 7: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 8: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 9: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 10: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 11: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 12: IDE 中显示了 queryPayChannelParamByAppAndPlatform 方法的代码，注释说明“从redis查询，如果有则返回”，并显示了 SQL 查询语句。
画面 13: 展示了 Swagger UI 界面，输入了 appid 和 platformChannel，点击 Execute 后，页面显示“LOADING”，并最终在响应中返回了 JSON 数据。
画面 14: 展示了文档中“5.6.4 查询缓存”章节，说明查询渠道参数的逻辑：先从 Redis 查询，存在则返回，否则从数据库查询并存入 Redis。同时显示了要修改的代码方法名：queryPayChannelParamByAppAndPlatform。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从缓存查询
    String redisKey = RedisUtil.keyBuilder(appid, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 3:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从redis查询，如果有则返回
    String redisKey = RedisUtil.keyBuilder(appId, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 4:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从redis查询，如果有则返回
    String redisKey = RedisUtil.keyBuilder(appId, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 5:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从redis查询，如果有则返回
    String redisKey = RedisUtil.keyBuilder(appId, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 6:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从redis查询，如果有则返回
    String redisKey = RedisUtil.keyBuilder(appId, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 7:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从redis查询，如果有则返回
    String redisKey = RedisUtil.keyBuilder(appId, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 8:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid, String platformChannel) {
    //从redis查询，如果有则返回
    String redisKey = RedisUtil.keyBuilder(appId, platformChannel);
    Boolean exists = cache.exists(redisKey);
    if (exists) {
        //从缓存获取支付渠道参数列表（json串）
        String PayChannelParamDTO_String = cache.get(redisKey);
        List<PayChannelParamDTO> payChannelParamDTOs = JSON.parseArray(PayChannelParamDTO_String, PayChannelParamDTO.class);
        return payChannelParamDTOs;
    }
}
```

画面 9:
```java
/**
 * 查询支付渠道参数
 * @param appid 应用id
 * @param platformChannel 服务类型代码
 * @return
 */
@Override
public List<PayChannelParamDTO> queryPayChannelParamByAppAndPlatform(String appid

