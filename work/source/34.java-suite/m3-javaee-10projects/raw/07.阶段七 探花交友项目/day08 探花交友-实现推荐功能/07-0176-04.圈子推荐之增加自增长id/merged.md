# 04.圈子推荐之增加自增长id

- 阶段：07.阶段七 探花交友项目
- 章节：day08 探花交友-实现推荐功能
- 源文件：07.阶段七 探花交友项目\day08 探花交友-实现推荐功能\04.圈子推荐之增加自增长id_【海量资源尽在 666java.com】.mp4
- 时长 13分59秒（音频 839s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来实现我们圈子的推荐这个功能那么其实我们首先要做的第一件事情呢就是我们需要去对我们之前的动态的这样的一个数据结构的做一下调整我们就需要去增加一个增长的一个ID那我们为什么要去增加它呢大家可以回想一下前面我们所讲的Spark的一个MLlib中的推荐
[00:25] 那么在MLlib推荐了它的一个模型它的一个推荐模型就是用户ID加什么呢加一个产品ID然后去做一个推荐那么要注意的是这个产品ID它要求的是一个int类型或者说是一个none类型的而我们在之前我们的动态中我们的ID使用的是谁呢是mongodb中的一个object ID
[00:49] 那么显然的这个是不能够去匹配到我们的一个推荐模型的那么所以呢我们需要对我们之前的一个动态的这样的一个数据呢去做一下调整那我们需要给他增加一个至增长至增长的一个ID那么问题来了就是
[01:05] 在MongoDB中我们做不到和MySQL中一样我们只要设置一个自增长就可以实现自增长了这个是做不到的那我们必须自己来维护一套自增长的逻辑来去实现自增长所以说我们需要去做这样的一件事情好那么首先我们第一步就去修改我们之前的一个publish的这样的一个对象好那我们来找到这个对象是在我们的interface
[01:33] 项目中那么找到POJO下面有一个Public然后我们在这个位置我们去增加一个增加一个什么的Lung类型的我们ID叫PID那么就是Public IDPID那么这个要注意这个是我们的一个Lung类型对吧主要的用于什么用于我们的一个推荐系统的一个模型
[01:58] 那么通过它呢才能够去啊才能够去做一个推荐那么最终呢我们通过它呢也就能够找到我们当前的这个动态的这个数据了OK那么这第一步这个操作那么第二步呢我们就需要在我们的这个实现中啊那么在我们原有的这个实现中我们来找一下啊那么有一个这个圈子啊圈子API里面呢是有一个发布啊我们来找一下在最上面啊在这个位置
[02:28] 那么在这个发布这个位置中啊那么我们保存这个publist的时候那么就需要给他去什么呢去我们去增加一个去增加一个什么自增自增长的这个pid啊那么怎么样去做一个设置呢我们来set设置一下pid
[02:48] 那么如何去做一个支争长那么就需要我们自己来做一个维护了那我们如何自己来做一个维护呢其实我们是可以借助于谁呢借助于我们的Redis来做一个完成那么其实我们知道在Redis中呢有一个叫做什么呢INCR这个命令对吧那么就可以去做一个支争长我们借助于他呢来做一个完成啊那么下面呢我们就来写一个Service啊那我们在这个double这个Service这个
[03:16] 工程中我们创建一个包这个包就叫Service这样的一个包然后在这个下面我们去写一个叫做id什么的Service那么去在这个Service中去实现我们的一个自增长的一个Service那么这个Service我们就使用的是我们spring的一个Service那么使用的它Service好那么然后我们就在我们这个
[03:44] 圈子的中然后呢去把它呢注入进来啊那么就是这个ID Service然后呢ID Service好那么把它呢注入进来那么注入进来之后啊那我们在这个位置就可以调用谁呢调用我们这个ID Service点什么呢表示来一个creatorcreator ID啊那么这个方法那么这个方法需要传递什么内容呢
[04:09] 那我们可能啊暂时呢我们不需要传递什么那我们就直接来让他做一个生成啊那么一会儿呢我们如果有参数需要传递的话那我们再去增加这个参数那么接下来呢我们就把这个方法呢我们就先来啊创建出来他返回的是一个这个浪啊那么我们来写一下这个是什么呢去这个是我们去生成我们就还是写这个方法做事吧这个就是我们生成自增长的ID
[04:38] 那么前面我们分析过它是需要通过什么呢需要去什么呢需要它的原理原理就是以什么呢就是使用Redis的自增长自增长这个类型来实现我们的自增长的一个ID所以说我们在我们的工程中那么也需要去使用我们的Redis那么在这个里面我们又需要去
[05:07] 导入依赖了导入谁我们来看一下那么我们就需要上面是不是我们导入谁导入我们的readist是不是就可以了我们直接来改一下在这然后去导入的就是应该boot star然后后面加一个readist好这样的话是不是就可以导入进来可能依赖写的不对我们就来看一下之前在我们这个server中我们用过这个readist对不对好 那我们来看一下少了一个data
[05:36] 我们就把它拷贝过来我们就往上面走在Service的pub文件中我们这样来写写一个它好这样的话我们就把相关的redis的依赖就导入进来了那么接下来我们还需要把我们redis的一些配置也拷贝过来然后我们来找一下我们的resource下面的obligation然后我们把这个redis的一个配置在这
[06:03] 那我们就把它丢到我们的这个Service这个中那么在这啊那么丢到下面吧啊丢到这个位置来那么这样的话呢我们就完成了一个配置然后呢在我们的这个ID Service中啊那我们就可以注入我们的这个readies的一个template是不是去做一个这个操作呀对吧template然后呢street啊street好那么去写一个这个
[06:29] template然后呢把它呢注入进来这样的话呢就可以完成和redis的一个这样的一个交互了那么接下来我们就需要去考虑一下那么我们既然说使用redis的一个自增长那么我们是不是就可以直接去使用它的什么呢这个template中的这个方法对吧比如说我们来一个这个叫ops value然后呢是不是有一个increment然后呢去做一个这个自增长啊
[06:57] 对吧那我们给他设定一个这个key那么这个key我们又该如何去做一个定义呢那我们来想一下那我们是不是就可以这样来写比如说叫做叫做什么的
[07:12] 探花然后呢我们写什么呢写一个这个ID对不对啊但是大家可以想一下啊那我们现在是为圈子是不是去做一个自增长的一个ID啊那么如果后面呢比如说我们要为我们的这个小视频呢或者说其他的要去做一个自增长的话那么显然这个位置我们是不是不能够把这个ID把这个key是不是写死啊那必须要去写成一个
[07:39] 动态的对不对啊所以说呢在这个位置我们就需要去再去加一个什么呢比如说我们加一个type加一个这个type好那么这个type呢我们就要求调用我们这个参数之后呢传递过来你是哪个类型的对不对然后呢我们去做一个这个自增长那么自增长之后啊那么它的返回值那么它的返回值其实就是我们所要的这个值对不对
[08:07] 好那么我们来看一下把它就直接就丢到这个位置吧这样的话是不是就可以实现一个自增长对不对但是呢大家需要去思考一下那么如果说我们我们去调用这个credit id去生成我们这个id的时候那么每一次如果都去生成一个的话那么假设我们如果如果我们的这个我们来看一下比如说
[08:32] 如果我们所生成的这个ID它已经在之前就已经生成过这个ID如果再次调用它的时候是不是还会重新再生成一个ID这样的话就会导致什么呢
[08:46] 我们同一个我们这个就是object id可能会对应到我们多个这个pid这个显然是不可以的因为我们要保证我们这个object id跟我们的pid呢要一一对应所以说呢在我们这个create id这个方法中啊我们还需要去处理一个逻辑什么逻辑呢就是如果我们的一个这个object idobject做objectobject id
[09:16] 那么已经ID那么如果已经存在的话那么就应该什么呢返回对应的是不是返回对应的一个对应的一个这个ID并不是去做一个重新做一个生成那么也就是说我们需要在我们的ready中去记录我们的这个object ID
[09:40] 和我们这个生成的这个ID呢它的一个对应关系那么怎么样去保存这个对应关系呢那么其实呢我们需要通过这个hc来做一个保存了那我们可以是不是这样来玩一下啊就是通过this.this.template点一个什么呢ops4hc然后呢我们首先呢需要去做一个这个判断啊去做一个判断它是否是存在的对吧它是否是存在
[10:08] 那么如果它存在的话直接返回是不是就可以了那么这个位置呢我们又需要一个这个key对吧那么这个key我们怎么样定义呢是不是定义我们的一个这个叫做hckey那么它等于谁呢是不是可以这样去写写个碳花然后呢id应该叫做hc吧然后呢id下滑线再去加一个这个type好那么如果说它
[10:35] 存在这个Key是他那我们还是需要一个这个哈希中的一个Key那么这个Key呢我们是不是就需要去传入进来就是我们这个Object ID那么定义它叫什么呢Object ID就它然后呢把这个Object ID也传递过来那么这样的话呢我们是不是就可以去做一个这个判断了对吧那么如果
[10:57] 它要是存在的话那么就应该return啊return它那么return呢我们是不是就应该调用这个radius template.ops这个hc.get那么是不是传递这两个这个参数啊传递这两个参数ok好那么这样的话我们来看一下啊它拿到的是一个object那我们就需要去给它去做一个learn的value去做一个转化
[11:26] 那么他转不了那就toString然后再去做一个转化那么是不是就可以return就可以了那么既然在这个位置会有一个命中那么显然在下面这个位置就需要做一个写入对不对好那我们就把这个return放到我们的后面去我们就去去记录一下最后return id然后我们就需要去做一个写入了那么就通过一个template.opshc.
[11:54] 做一个什么呢put操作啊key呢就是我们的hash这个key然后呢再去写入一个叫做object id然后呢再去写入一个这个id这个值了好这样的话是不是就可以把这个数据呢是不是写入到对吧将这个生成的id生成的id写入到我们的一个hash表中
[12:19] 这样的话是不是前面就可以去做一个这样的命中了那么然后我们在我们的这个Service中我们是不是就需要去调用它了对吧我们来找一下我们那个Service是在这个位置那么调用它那么首先第一个参数来看一下第一个参数就type第二个参数是object id那么第一个参数type是谁我们肯定就是我们那个publish对吧publish然后第二个
[12:46] 第二个呢就是谁呢就是我们的一个publish叫做publish.getid然后呢去得到他的一个这个hashi这样的一个这不错啊然后呢大家呢这个里面还有个小的一个细节啊就是那么由于呢我们这个位置前面是不是都是大写那我们建议把它的是不是也设置为大写啊所以说呢我们就直接来做一个转换对吧然后呢调一个striptease
[13:14] 把它设置谁呢设置我们的一个设置我们的一个大写就可以了然后呢点我们去把它转成一个大写吧转成一个这个大写OK好这样的话呢就转成大写了那么这样的话我们这个ID是不是就比较统一了对不对啊好那么接下来呢我们来看一下我们这个讲义啊那么在我们讲义中呢是不是我们去修改这样的一个逻辑啊修改这样的一个这个逻辑
[13:42] 然后我们编写了一个ID Service这个显示实现了跟我们刚刚写的是一样的我们还需要去加入这个Redis这样的一个依赖OK好那么关于我们增加我们次增长的一个ID的一个实现我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何为 MongoDB 中的 Publish 对象动态增加自增 ID，并通过 Redis 实现 ID 的自增长逻辑。

2) 按时间顺序列出每张画面的要点：
画面1: 讲解动态增加自增 id 的背景，需要修改 Publish 对象使其支持 Long 类型的 id。
画面2: 展示 Publish.java 文件，定义了 Publish 对象的结构，包含 id、userId、text、medias、seeType、seeList、longitude、latitude、locationName、created 字段。
画面3: 展示 QuanzApiImpl.java 文件中 savePublish 方法的实现，其中包含设置 publish 对象的字段和调用 mongoTemplate.save(publish) 保存数据。
画面4: 展示 QuanzApiImpl.java 文件中 savePublish 方法的实现，其中包含校验 publish 对象的 userId 是否为空。
画面5: 展示 pom.xml 文件中 <build> 标签下的 <plugin> 配置，用于 Spring Boot 的 Maven 插件。
画面6: 展示 pom.xml 文件中 <dependencies> 标签下的 <dependency> 配置，用于引入 Spring Boot Starter Redis。
画面7: 展示 IdService.java 文件的包声明和注释，说明该服务用于实现 Redis 的自增长 ID。
画面8: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForValue().increment(0) 生成自增长 ID。
画面9: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForHash() 检查 ObjectID 是否已存在。
画面10: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForHash().get(hashKey, objectId) 获取已存在的 ID。
画面11: 展示 IdService.java 文件中 createId() 方法的实现，使用 redisTemplate.opsForValue().increment(key) 生成新的 ID。
画面12: 展示 QuanzApiImpl.java 文件中 savePublish 方法的实现，调用 idService.createId(type, objectId) 生成自增长 ID。
画面13: 展示 IdService.java 文件中 createId() 方法的实现，使用 StringUtils.center() 方法将生成的 ID 填充为指定长度。
画面14: 展示 day08.md 文件中 Publish 对象的定义，包含 id、userId、text、medias、seeType、seeList、longitude、latitude、locationName、created 字段。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2:
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;

// 发布表，动态内容
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "quanzi_publish")
public class Publish implements java.io.Serializable {
```

画面3:
```java
if (publish.getUserId() == null) {
    return false;
}
try {
    //填充数据
    publish.setUserId(ObjectId.get());
    publish.setCreated(System.currentTimeMillis()); //发布时间
    publish.setSeeType(1); //查看权限
    publish.setPid();
    //保存动态信息
    this.mongoTemplate.save(publish);
    //写入到自己的指针表中
    Album album = new Album();
    album.setPublish(publish.getId()); //动态id
    album.setCreated(System.currentTimeMillis());
```

画面4:
```java
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import java.util.ArrayList;
import java.util.List;

@Service(version = "1.0.0") implements QuanZiApi {
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public boolean savePublish(Publish publish) {
        //校验publish对象
        if (publish.getUserId() == null) {
            return false;
        }
        try {
            //填充数据
```

画面5:
```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-maven-plugin</artifactId>
            <configuration>
                <mainClass>com.tanhua.dubbo.server.DubboApplication</mainClass>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>repackage</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
    </plugins>
</build>
```

画面6:
```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

画面7:
```java
package com.tanhua.dubbo.server.Service;
import org.springframework.stereotype.Service;

/**
 * 原型：使用Redis的自增长类型，实现自增长的id
 */
@Service
public class IdService {
```

画面8:
```java
@Service
public class IdService {
    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    /**
     * 生成自增长的id
     * @return
     */
    public Long created() {
        this.redisTemplate.opsForValue().increment(0);
        return null;
    }
}
```

画面9:
```java
public Long created() {
    this.redisTemplate.opsForValue().increment(0);
    return null;
}
```

画面10:
```java
public Long createId(String type, String objectId) {
    String hashKey = "TANHUA_HASH_ID_" + type;
    if (this.redisTemplate.opsForHash().hasKey(hashKey, objectId)) {
        return this.redisTemplate.opsForHash().get(hashKey, objectId);
    }
```

画面11:
```java
public Long createId(String type, String objectId) {
    String hashKey = "TANHUA_HASH_ID_" + type;
    if (this.redisTemplate.opsForHash().hasKey(hashKey, objectId)) {
        return this.redisTemplate.opsForHash().get(hashKey, objectId).toString();
    }
    String key = "TANHUA_ID_" + type;
    Long id = this.redisTemplate.opsForValue().increment(key);
    this.redisTemplate.opsForHash().put(hashKey, objectId, id);
    return id;
}
```

画面12:
```java
publish.setPid(this.idService.createId("publish", publish.getUserId()));
```

画面13:
```java
public Long createId(String type, String objectId) {
    String hashKey = "TANHUA_HASH_ID_" + type;
    if (this.redisTemplate.opsForHash().hasKey(hashKey, objectId)) {
        return this.redisTemplate.opsForHash().get(hashKey, objectId).toString();
    }
    String key = "TANHUA_ID_" + type;
    Long id = this.redisTemplate.opsForValue().increment(key);
    this.redisTemplate.opsForHash().put(hashKey, objectId, id);
    return id;
}
```

画面14:
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.mapping.Document;
import java.util.Date;
import java.util.List;

// 发布表，动态内容
@Data
@AllArgsConstructor
@NoArgsConstructor
@Document(collection = "quanzi_publish")
public class Publish implements java.io.Serializable {
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无

5) 不要评价画面美观，不要输出与课程无关的内容。
无

