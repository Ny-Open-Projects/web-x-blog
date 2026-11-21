# 08.圈子功能实现之发布动态（上）

- 阶段：07.阶段七 探花交友项目
- 章节：day03 探花交友-实现圈子功能
- 源文件：07.阶段七 探花交友项目\day03 探花交友-实现圈子功能\08.圈子功能实现之发布动态（上）_【海量资源尽在 666java.com】.mp4
- 时长 8分22秒（音频 502s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们就来看一下发布动态的这个实现那么就是在我们圈子中呢我们可以去发布我的动态啊那么也就是说我们可以去发布这个朋友圈了啊好那么下面我们来看一下接口的定义啊那么首先呢我们需要在我们的double的这个接口中呢去定义我们的一个圈子啊这样的一个API然后呢我们首先呢先实现第一个这个方法就是什么呢我们发布动态啊这个save publish
[00:28] 然后我们就把这个接口我们就直接来做一个拷贝了来拷贝到我们的API里面来这个是我们接口的一个定义那么接下来我们将去实现我们这个接口那么实现是在我们Service这个工程中让我们去做一个实现那么在这个里面我们去写一个类叫什么就叫圈子
[00:54] 圈子然后呢这个APIIMPL去做一个实现那么它呢去实现就是我们刚刚所写的这个圈子API这样的一个接口然后呢我们去实现我们这个接口这个方法OK好那么首先呢我们先写这个相关的一些注解那我们把它标记为这是一个Service要注意那我们使用的是这个阿里巴巴的这个double的这样的一个注解
[01:23] 那么Service那么写给他然后呢指定这个版本啊Watson的是1.0.0啊这样的一个版本好那么有了这个Service之后呢就会把它注册为这是一个服务了那么接下来呢我们将去实现我们这个save这个方法就是我们去发布动态这个方法那我们来看一下这个应该怎么去做那么首先呢可以看到这个方法的输入呢是一个publish的一个对象那输出呢是一个布尔值也就是说
[01:53] 是否成功这样的一个布尔值那么下面我们来看一下怎么去操作那么首先其实我们应该去做一个校验对吧我们去校验我们的一个publish对象publish对象那么我们在这简单去做一个校验教练谁呢我们就校验他的一个UraID那么UraID肯定是不能等于空的对不对对吧那么如果他等于空那return什么呢force这样的话是不是就
[02:21] 可以了对吧当然了啊那么我们大家可以写一下是不是可以再去写些什么呢其他的啊其他的这个注解啊其他的啊其他的这个逻辑啊现在我们这个逻辑呢就类似了啊类似了好那么呃这个呢关于教业呢我们就啊写到这那么接下来呢我们来看一下在我们的啊在我们的这个publish啊publish中
[02:47] 我们看一下哪些字段需要我们去做一些填充那么你比如说这个ID这个字段肯定不能由外部去调用我们这个类的方法给我们传入ID那么一定是随我们自己是不是来生成所以我们调用这个object ID然后点get的方法来获取一个ID那么还有什么我们来看一下还有比如说我们的像一些其他的一些基本的这种就是我们数据的一些
[03:17] 这个字段那么肯定的都是由我们外部给我们去做一个填充那么你比如说呢像我们这个credit的时间呢我们就直接来做个填充吧那么续写给他这是我们的一个发布的一个时间对吧然后呢我们再来看一下啊比如说呢这个里面呢我们还有一个这个ctype就是查看类型那么我们来看一下这个类型呢我们需要去给他看一下啊那么这个类型呢是什么呢就是
[03:46] 一呢是公开二呢是私密三呢是部分可见四呢是不给谁看那么我们默认的把它设置为一那么大了我们再来说明一下就是我们当前的这个项目呢我们并没有去实现相关这样的一些权限啊但是我们先可以给他些这个默认值然后呢后续如果有这样需求的话就直接就可以去写了对吧好那么这个就是一个什么呢查看的一个权限了对吧查看这个权限或者说类型啊都可以
[04:16] 那么这个里面呢比如说这个clist和notclist那么这两个呢我们就不填了那么如果后续我们有需要的话再去填哎呀OK好那么到这里呢基本上我们的一些这个我们的这个数据是不是就填充完整了对吧填充我们的一些这个数据那么接下来呢是不是就可以做保存了那么保存呢我们是不是就需要去注入谁呢注入我们的一个这个mongo对吧mongo的一个template
[04:46] 就把它注入进来那么我们做一个注入那么注入进来之后呢我们就可以去调用我们的这个Mongo这个sale这个啊sale这个方法去做一个保存了那我们是直接保存我们这个publish就可以了那么我们这个publish呢它呢是所有的用户都会保存在一张表中啊所以说这个表明呢就使用我们注解中所写的这个表明呢啊就可以了那么这个呃这个操作呢其实我们就就完成了什么呢完成了我们这个
[05:16] 保存我们的一个动态信息对不对那么接下来我们来看一下还有一些其他的一些操作那么在前面我们去讲流程的时候来看一下那么我们在讲发布流程的时候第一是不是要去写入到发布表第二要写到什么的自己的相册表中那么第三就需要去写入到时间线表所以说
[05:42] 除了我们这个发布表这个写入动作之外呢还会有两个这个动作需要去操作一下啊那么接下来呢我们来看一下下面这个操作呢我们将数据什么呢写入到什么呢我们自己的相册啊表中啊表中呃表中那么我们来看这个逻辑怎么写那么首先呢我们去构建我们的一个这个相册对象啊叫什么二本啊这样的一个对象
[06:10] 然后呢我们把它构建出来之后啊那我们就可以去做一个写入我们的这个内容了对吧好那我们先把这个对象呢去构建出来然后呢首先呢给它一个ID那么就是这个object这个ID然后呢我们再给它一个什么呢public这个ID那么就是谁呢我们上面的这个public对象中的这个ID这个呢就是我们的一个什么呢动态的一个ID
[06:38] 然后呢我们再去set一个什么呢set一个这个created啊created呢我们就是当前的时间戳了那就给他哎呀OK好那么接下来呢我们是不是就需要去把我们这个什么二本对象呢去写入到我们的一个这个mongodb中那么就通过这个mongodb template做一个sale这个操作那么显然呢我们可以知道啊那么我们每一个人是不是都会有一个自己的一个相册表所以说呢
[07:08] 这个我们的mongo dp中的这个表明呢就不能固定那么显然呢需要使用下面的这个方法对吧两个参数那么第一个参数呢就是我们这个对象那第二个参数呢就是我们的表明那么表明我们怎么去写呢我们来看一下那么我们先来找到我们的这个urban对象然后呢我们去拷贝一下它的一个名字然后呢我们在这个位置啊那我们再去做一个操作再去下滑线去添加一个谁呢
[07:37] 添加一个用户ID那么我们就通过上面的一个publist点get什么get user ID那么这样的话是不是就拿到这个用户ID了那么这样我们就可以将什么将我们的这个什么项册对象是吧写入到mongo db中写入进去那么这是我们的第二个写入这个操作对不对那么写入完成之后
[08:03] 接下来呢我们是不是就将要写入的是谁呢写入的啊我们的这个除了这个相册之外是不是还有一个我们要把这个写到别人的我觉得我的好友中啊他们的时间线中那所以说呢我们需要在写入到时间线这张表OK好那我们来看这个逻辑呢是怎么写

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Dubbo 服务中实现发布动态功能，包括定义接口、编写实现类、处理数据对象和与 MongoDB 数据库交互。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“2.2.1. 定义接口”部分，包含接口定义代码。
画面2：在 IDEA 中右键点击包目录，准备新建实现类。
画面3：在 QuanzApiImpl.java 文件中，添加 @Service 注解并导入相关依赖。
画面4：在 savePublish 方法中，添加对 publish 对象 userId 为空的校验逻辑。
画面5：在 savePublish 方法中，为 publish 对象设置 id、created 和 seeType。
画面6：在 savePublish 方法中，尝试使用 ProcessBuilder 设置环境变量。
画面7：展示 Publish 类的完整字段定义，包括 id、userId、text、medias、seeList、notSeeList、longitude、latitude、locationName 和 created。
画面8：在 savePublish 方法中，为 publish 对象设置 id、created 和 seeType。
画面9：再次展示 Typora 文档中“2.2.1. 定义接口”部分，包含接口定义代码。
画面10：在 savePublish 方法中，尝试使用 Album 类并引入相关依赖。
画面11：在 savePublish 方法中，使用 mongoTemplate.save 保存 publish 对象，并创建 Album 对象。
画面12：在 savePublish 方法中，尝试使用 album.getCreated(System.currentTimeMillis())。
画面13：在 QuanzApiImpl.java 文件中，导入 MongoTemplate 并声明其为私有成员变量。
画面14：在 savePublish 方法中，创建 Album 对象并将其保存到 MongoDB 中。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhu.dubbo.server.api;
import com.tanhu.dubbo.server.pojo.Publish;
public interface QuanzApi {
    /**
     * 发布动态
     * @param publish
     * @return
     */
    boolean savePublish(Publish publish);
}
```

画面3：
```java
@Service(version = "1.0.0")
public class QuanzApiImpl implements QuanzApi {
    @Override
    public boolean savePublish(Publish publish) {
        //校验publish对象
        if (publish.getUserId() == null) {
            return false;
        }
        // ...... 其他的逻辑类似
        return false;
    }
}
```

画面5：
```java
import org.bson.types.ObjectId;
@Service
public class QuanzApiImpl implements QuanzApi {
    @Override
    public boolean savePublish(Publish publish) {
        //校验publish对象
        if (publish.getUserId() == null) {
            return false;
        }
        // ...... 其他的逻辑类似
        return false;
    }
}
```

画面7：
```java
public class Publish implements java.io.Serializable {
    private static final long serialVersionUID = 873238321802804771L;
    private ObjectId id; //主键id
    private Long userId;
    private String text; //文字
    private List<String> medias; //媒体数据，图片或小视频 url
    private Integer seeType; //谁可以看：1-公开，2-私密，3-部分可见，4-不给谁看
    private List<Long> seeList; //部分可见的列表
    private List<Long> notSeeList; //不给谁看的列表
    private String longitude; //经度
    private String latitude; //纬度
    private String locationName; //位置名称
    private Long created; //发布时间
}
```

画面10：
```java
//校验publish对象
if (publish.getUserId() == null) {
    return false;
}
// ...... 其他的逻辑类似
Album album = new Album();
```

画面11：
```java
//保存动态信息
this.mongoTemplate.save(publish);
Album album = new Album();
album.setId(ObjectId.get());
album.setPublishId(publish.getId()); //动态id
album.setCreated(System.currentTimeMillis());
```

画面13：
```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
@Service(version = "1.0.0")
public class QuanzApiImpl implements QuanzApi {
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public boolean savePublish(Publish publish) {
        //校验publish对象
        if (publish.getUserId() == null) {
            return false;
        }
        // ...... 其他的逻辑类似
        publish.setId(ObjectId.get());
        publish.setCreated(System.currentTimeMillis()); //发布时间
        publish.setSeeType(1); //查看权限
        //保存动态信息
        this.mongoTemplate.save(publish);
        //写入到自己的相册表中
        Album album = new Album();
        album.setId(ObjectId.get());
        album.setPublishId(publish.getId()); //动态id
        album.setCreated(System.currentTimeMillis());
        //将相册对象写入到MongoDB中
        this.mongoTemplate.save(album, collectionName: "quanzi_album" + publish.getUserId());
        return false;
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

