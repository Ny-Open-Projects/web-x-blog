# 14.地理位置之dubbo接口实现

- 阶段：07.阶段七 探花交友项目
- 章节：day09 探花交友-好友推荐、今日佳人
- 源文件：07.阶段七 探花交友项目\day09 探花交友-好友推荐、今日佳人\14.地理位置之dubbo接口实现_【海量资源尽在 666java.com】.mp4
- 时长 17分36秒（音频 1057s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,那么接下来呢,我们来看一下我们的地理位置这个功能那么这个功能呢,主要呢是我们要去搜集我们的用户的一些地理位置那么我们主要呢是要用于我们后面的我们这个搜附近这个功能就是我们要去搜索,比如说我在这个两公里范围之内
[00:22] 的一些好友有哪些那么要做这样的一个功能啊所以说呢我们必须要知道用户的一个这个地理位置那么我们基于这种移动端的啊这种它的一个特性那么用户有可能是在移动的过程对吧那么所以说呢我们就需要我们的这个客户端啊那么它呢是需要给我们去给服务端去上传或者说上报它的一个地理位置那么就是说如果它的这个就是
[00:51] 变化的一个大小大于500米或者是每隔五分钟的时候就向我们服务端去发送一次它的一个地理位置那么这样的话呢我们就可以基本上近视的实时的能够掌握到这个用户的一个位置所在然后呢我们是不是就可以根据这个位置来查询我们的一些附近的一些好友啊所以说我们是需要做这样的一件事情啊
[01:19] 那么我们如何去根据一个范围,比方说两公里这样的一个范围去做一个查找那么这个时候我们就需要借助于我们的MongoDB的一个GEO这样的一个功能来做一个实现它其实是我们在MongoDB中的一个关于我们地理位置的一个索引那么可以通过它来做一个查询那么我们今天先
[01:46] 去干嘛呢去保存我们的地理位置那么查询这个功能呢我们放到我们后面去实现我们的这个附近啊搜附近人的时候呢我们再去做一个讲解那么下面呢我们就来看一下我们的这个具体的内容的实现那么首先呢我们来定义我们的一个podio那么我们来看一下我们这个podio啊那么
[02:08] Poll中呢我们可以看到那么这个就不说了对吧这个是Lambook的一些读解然后呢这个是指定我们的这个就是表那么就是我们MongoDB中的一个表然后呢注意下面的这个呢是指定我们的这个实例中的这个所以
[02:29] 它指定哪个呢就是我们一个location啊location使用的是什么这种什么呢2D啊spell那么这样的一个所以那么就是代表了什么它是一个球面的对吧那么是一个地理位置的这样的一个所以这个所以的名字呢叫做location的一个index啊这样的一个配置然后呢下面呢这一块呢就是指定它的一些字段了有ID啊有这个url ID
[02:56] 并且呢UDID呢也设置了这个所以根据它查询的会速度比较快然后呢我们可以看到在这个位置呢我们就指定了一个这个GU JSON的一个point然后呢它是一个location然后呢这个GU JSON port中呢它呢主要是有两个这个属性那么一个呢是叫X一个呢是叫做Y那我们把这个X呢作为我们的一个精度
[03:23] 那么外呢作为一个纬度啊那么我们其实知道在地球上面啊它是有这个经纬度的对吧那么是去呃记录它的一个经度和纬度呃然后呢下面这个adj是它这个地呃位置的一个描述比如说北京啊上海啊这样的一个描述啊然后呢还有它的更新时间呃还有创建时间更新时间还有last update就是上一次更新的一个时间
[03:50] 那我们换有这个时间呢要去记录他这三个时间啊好嘞好那么呃我们就把这个puzzle呢我们去做一个创建那么我们要找到我们的这个谁呢找到我们这个呃double这个服务啊那么来看一下那么double的服务呢是在哪里呢我们来找一下啊是在这个位置啊找到interface然后呢这个里面呢我们找到一个我们的一个这个puzzle啊我们把它丢过来
[04:17] 那么这个呢就是我们的一个UraLocation这样的一个实体它所对应的表呢就是Ura下滑线这样的一个Location那么接下来呢我们来定义我们的这个Double的接口那么我们把这个接口呢定义出来叫做UraLocation的一个API那么我们可以看到现在呢定义了有一个方法叫做更新用户的一个地理位置那么就是Update然后呢Ura
[04:44] 然后location然后有这么几个参数那么第一个参数是user id第二个参数是它的精英度维度和地址总共是有四个参数那么接下来我们就来编写它的具体的实现类我们来找到我们的Service下面的API包然后我们去创建一个叫做user locationlocation的什么就是APIAPI AMP
[05:14] IMPL好那么我们去把它定义这是一个Service然后是一个Watson版本是1.0.0这样的一个版本的一个Service然后下面我们就来实现我们刚刚所写的这个接口那么我们去实现它就叫Urallocation API
[05:39] 然后呢我们去实现它的一些这个方法啊有一个叫更新的这个方法那我们先把谁呢先把我们这个mongo啊mongo template那么我们先注入进来啊先注入进来好嘞那么注入进来之后啊那么接下来呢我们就来编写啊我们的这个更新的这个逻辑啊那么在我们传入了这四个参数之后啊那我们就来构造一个叫做urlocation
[06:08] location的一个对象去new一个这个urlokation然后呢我们去来设置一下urlokation.set那么我们先设置它的一个地址然后呢我们再去set其他的一些内容那么我们再去set一个来看一下那么url那就是我们当前的这个传入的url那我们再来set一个location
[06:35] 那么location是需要我们去new一个geo的一个jsonpoint然后呢传入两个参数来看一下那么它分别是两个这个double类型那么一个是xx一个是y那我们就把这个我们的精度传入过来然后呢我们把我们的纬度传入过来作为我们的一个这个location然后呢我们来看一下还需要去设置什么吗
[07:01] 我们去设置我们的这个时间啊这个不需要了因为要好我们需要判断我们这个就是当前的这个用户的数据啊在我们库里面是否存在那么呃存在和不存在它的逻辑呢是不一样的啊那我们来看一下那么首先呢我们先来查询啊查询我们的这个就是这个用户的地理位置啊看他这个数据存在不存在那么我们根据this.mongo template
[07:27] 然后我们去做一个FindOne肯定是只有一条数据了那么query设置为None那么class设置为是什么就是UraLocation.class那么我们接下来来设置它的一个query那么设置它然后query等于query点query然后我们设置我们这个条件critter.vail设置谁呢
[07:59] 设置我们的usid好那么我们设置他usid然后我们点依日谁呢依日我们的usid去找这条数据看是否存在那么我们就可以把query是不是就丢给他了对吧然后我们就去拿到我们的usallocation我们就用 ul 吧就
[08:29] 然后我们去判断一下那么如果空等于这个UL的话那就说明什么这个位置数据在我们的mongo db中根本就不存在那么不存在就意味着什么呢新增我们的一个用户的一个位置数据位置的一个数据那么新增我们就需要给他去干嘛呢是不是设置这个urlocation.set一个id
[08:57] 那么就用object get去设置然后我们用了location.setAcrated就是我们当前的时间戳那么还有什么还有的就是我们set一个update那么也是当前这个时间戳但是我们最好是拿到相同的时间点get一个cated是相同的时间然后我们再去set一个lastset一个last update
[09:27] 那么同样的也是一个我们这个更新时间好嘞那么我们设置了这么几个值之后那么接下来我们就能够去做一个保存了叫用this.mongo-template.sale操作sale这个useLocation好嘞那么这个是不是我们就新增了对吧然后要注意我们的返回值返回值是一个这么串
[09:54] 那么也就是说我们返回要返回我们的一个ID那就是拿到这个 userlocation.get什么的ID然后呢去拿到他的一个这个字幕创好那么这是新增那么else呢那就代表着什么呢我们需要去更新了那么更新的话是需要更新哪些内容呢我们来看一下那我们去调用this.mongo.template做一个这个updateupdate first
[10:21] 就用上面的它就可以了那么同样的有三个参数第一个query我们先给它去设置为然后我们第二个update也设置为第三个就是我们的yourlocation.class我们先来做这样的一个设置我们这个query那么其实
[10:44] 他所更新的一个条件呢是谁呢啊就是说他不等于空那么我们是不是可以设置他的一个这个条件那么其实我们可以根据这个query是不是去做一个更新啊啊这样的话也是OK的对吧那么下面呢我们就需要给他设置一个什么呢就是我们的更新的一个对象啊那我们来设置一个谁呢updateupdate啊update那么我们来设置他update
[11:13] update等于什么update点update那么key那么我们要设置谁首先我们肯定需要给他去更新的是他的一个location对吧那么location那么我们放大这然后我们key是他然后我们这个value就是uo的location点get什么location这是第一个更新
[11:40] 那么第二个更新呢我们需要给他去set谁呢就是我们的一个update然后呢这个呢我们更新的是我们当前的一个时间出啊当前这个时间出这第二个更新那么第三个更新呢我们要更新我们的一个这个什么last update来就更新他啊那我更新我们这个last的一个update
[12:06] 那么这个值更新成谁呢就更新成我们当前所查询到的这个对象的什么呢这个update的时间就他上一次所更新的时间啊就是他那么我们把这个update呢给他传递过来这样的话呢我们是不是就完成了一个呃用户的这个更新啊对吧用户的这个地理位置更新然后呢最后这个return呢那我们就return我们拿到这个ul
[12:32] 拿到这个UL那么UL拿到他的一个ID啊好那么这样的话呢我们就完成了我们的一个这个更新了对吧这个是我们的一个实现的一个编写那么我们来看一下我们的讲义啊那么这个是接口的一个定义那么下面这个呢是我们的一个具体的一个实现那么下面呢我们来看一下当然我们这个是MOOC接口啊那么接下来呢我们可以先来去
[13:01] 测试一下我们这个方法测试我们的这个方法看是否是OK的那我们可以来编写一个测试用例我们来测一下那么我们就找到这个里面来吧那我们写一个叫做test叫userlocation然后呢我们去加一个注解那我们就来拷一下吧把这两个注解拷贝过来把它俩拷贝一下那么就是这个userlocation往这一丢
[13:33] 好嘞好那么把它呢导入进来然后呢我们接下来呢去测试我们的方法然后呢test然后呢做一个sale这个操作test应该是叫什么呢updateupdate然后呢我们设置一个test注解然后呢我们去把我们这个叫yourlocation API呢去注进来然后呢我们去做一个注入
[14:02] 然后呢我们去使用谁呢就是我们这个this.这个yourlocation.update啊传递四个参数那么第一个参数呢那我们就更新1这个用户吧然后呢第二个参数就是他的一个呃这个呃就是我们的坐标了那坐标的话我们需要去搜一下经纬度那么我们呃去去百度里面去搜一下吧搜一下就是我们的一个叫什么呢这个呃经纬度
[14:33] 查询应该叫金伟多查询看这个能不能找到啊然后呢我们这个好像不行那这个呢我们找一个那么这个他输一个地址对吧那我们就随便去写一个地址吧比如说北京市然后呢就是叫什么呢就输一个北京市吧解析这个地名那么解析的一个这个结果呢就是这个对吧那么前面这个116呢这个就是京都啊那我们来
[15:03] 拷贝一下那么这个是它的一个精度那第二个参数那么第三个参数呢就是后面这个纬度啊然后呢我们去传递一下然后呢第三个呢就是我们的名字啊北京好嘞好那么呃接下来呢我们就可以去呃拿到它的一个拿到谁呢是不是拿到我们的一个这个ID啊呃然后呢我们把它呢就打印出来ID
[15:29] 好那么接下来呢我们来刷新一下当然了我先来看一下我们这库里面有没有这个unlocation有我先把这个呢给它drop掉然后呢我们去做一个debug那么这个位置打一个断点然后呢我们去把这个之前的这个double呢给它停掉然后呢我们就直接来做一个debug一个启动好那我们来等待它的一个启动
[15:57] 好 那我们来跟踪一下它的一个执行走 那么进入走 走 设置一个我们的一个这个对象啊然后呢 我们去做一个查询现在肯定也没查到 是闹那么进入到我们的这个新增里面来走 做一个税务保存OK 走 是不是就打印出来我们的这个一个这个ID 对吧然后呢 我们就直接通过啊好嘞 那么这样的话呢我们就实现了我们的一个新增那么下面我们来看一下我们的
[16:25] 表里面啊库里面有没有这个数据啊是不是有了有了location有这样的一条这个数据啊那么我们location呢是这样的一个结构啊它的一个精微度的一个这样的一个值好那么呃接下来呢我们可以来查看一下它的一个就是这个表的什么呢就是一个索引啊get什么呢index啊index然后呢我们去做一个查询那么其实可以看到在我们这个当前这个表里面呢有三个索引
[16:55] 那么第一个索引呢就是我们的这个下滑线这个ID对吧然后第二个索引呢就是我们所设的这个location的这个索引那么它呢就是这个地理位置的这个索引那么第三个这个索引呢就是我们所设的UID的这个索引啊那么可以看到它的这个UID啊是我们的这个索引哎OK好那么我们这样的话呢是不是基本的也就啊实现了我们的这个
[17:24] double接口的一个编写对吧OK好那么关于我们这个就是地理位置更新的一个double接口的一个编写呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现一个用户地理位置服务，包括定义POJO、编写服务接口与实现、以及编写单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示课程文档“day09 讲义.md”中“5. 地理位置”章节的“6.1. 定义pojo”部分，代码中定义了UserLocation类，包含@Document、@CompoundIndex、@Data、@AllArgsConstructor等注解，以及id、userId、location、address、created、updated等字段。
画面2：在IDE中右键点击UserLocationApi.java文件，弹出菜单，显示“Delete”选项，准备删除该文件。
画面3：在UserLocationApiImpl.java中，使用@Autowired注入MongoTemplate，并定义了setLocation、setUserId、setAddress、setLastUpdated、setCreated、setUpdated、setId等方法。
画面4：在UserLocationApiImpl.java中，光标位于setCreated方法上，显示其方法签名。
画面5：在UserLocation.java中，定义了UserLocation类，包含@Document、@CompoundIndex、@Data、@AllArgsConstructor等注解，以及id、userId、location、address、created、updated等字段。
画面6：在UserLocationApiImpl.java中，编写了查询用户位置的代码，使用Query.query(Criteria.where("userId").is(userId))查询，并在查询结果为null时创建新对象并保存。
画面7：在UserLocationApiImpl.java中，光标位于this.mongoTemplate上，显示其类型为MongoTemplate。
画面8：在UserLocation.java中，再次展示UserLocation类的定义，包含@Document、@CompoundIndex、@Data、@AllArgsConstructor等注解，以及id、userId、location、address、created、updated等字段。
画面9：在UserLocationApiImpl.java中，编写了更新用户位置的代码，使用Update.update("location", userLocation.getLocation()).set("updated", System.currentTimeMillis()).set("lastUpdated", ul.getLastUpdated())更新，并使用this.mongoTemplate.updateFirst(query, update, UserLocation.class)执行更新。
画面10：在IDE中，弹出“Create New Class”对话框，准备创建新类。
画面11：在TestUserLocation.java中，使用@RunWith(SpringJUnit4ClassRunner.class)和@SpringBootTest注解，定义了测试类。
画面12：在网页中，显示了“map.yanue.net”网站，包含多个截图和地图。
画面13：在IDE中，调试器显示了UserLocationApiImpl类的updateUserLocation方法的执行过程，变量包括userId、longitude、latitude、userLocation等。
画面14：在课程文档“day09 讲义.md”中，展示“6.4. mock接口”部分，包含接口地址、请求参数、Headers和Body等信息。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
```java
package com.tanhu.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.mongodb.core.geo.GeoJsonPoint;
import org.springframework.data.mongodb.core.index.CompoundIndex;
import org.springframework.data.mongodb.core.mapping.Document;
import java.io.Serializable;
@Document(collection = "user_location")
@CompoundIndex(name = "location_index", def = "{ 'location' : '2dsphere' }")
public class UserLocation implements java.io.Serializable {
    private static final long serialVersionUID = 4508668382007529970L;
    @Id
    private ObjectId id;
    @Indexed
    private Long userId; //用户id
    private GeoJsonPoint location; //x:经度 y:纬度
    private String address; //位置描述
    private Long created; //创建时间
    private Long updated; //更新时间
    private Long lastUpdated; //上次更新时间
}
```

画面3：
```java
import com.alibaba.dubbo.config.annotation.Service;
import com.tanhu.dubbo.server.pojo.UserLocation;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.mongodb.core.MongoTemplate;
@Service(version = "1.0.0")
public class UserLocationApiImpl implements UserLocationApi {
    @Autowired
    private MongoTemplate mongoTemplate;
    @Override
    public String updateUserLocation(Long userId, Double longitude, Double latitude) {
        UserLocation userLocation = new UserLocation();
        userLocation.setAddress(address);
        userLocation.setUserId(userId);
        userLocation.setLocation(new GeoJsonPoint(longitude, latitude));
        // 查询用户的地理位置
        Query query = Query.query(Criteria.where("userId").is(userId));
        UserLocation ul = this.mongoTemplate.findOne(query, UserLocation.class);
        if(null == ul) {
            //新增用户位置数据
            userLocation.setId(ObjectId.get());
            userLocation.setCreated(System.currentTimeMillis());
            userLocation.setLastUpdated(userLocation.getCreated());
            this.mongoTemplate.save(userLocation);
            return userLocation.getId().toHexString();
        } else {
            //更新
            Update update = Update.update("location", userLocation.getLocation())
                    .set("updated", System.currentTimeMillis())
                    .set("lastUpdated", ul.getLastUpdated());
            this.mongoTemplate.updateFirst(query, update, UserLocation.class);
            return ul.getId().toHexString();
        }
    }
}
```

画面5：
```java
import ...
@Data
@NoArgsConstructor
@AllArgsConstructor
@Document(collection = "user_location")
@CompoundIndex(name = "location_index", def = "{ 'location' : '2dsphere' }")
public class UserLocation implements java.io.Serializable {
    private static final long serialVersionUID = 4508668382007529970L;
    @Id
    private ObjectId id;
    @Indexed
    private Long userId; //用户id
    private GeoJsonPoint location; //x:经度 y:纬度
    private String address; //位置描述
    private Long created; //创建时间
    private Long updated; //更新时间
    private Long lastUpdated; //上次更新时间
}
```

画面6：
```java
// 查询用户的地理位置
Query query = Query.query(Criteria.where("userId").is(userId));
UserLocation ul = this.mongoTemplate.findOne(query, UserLocation.class);
if(null == ul) {
    //新增用户位置数据
    userLocation.setId(ObjectId.get());
    userLocation.setCreated(System.currentTimeMillis());
    userLocation.setLastUpdated(userLocation.getCreated());
    this.mongoTemplate.save(userLocation);
    return userLocation.getId().toHexString();
} else {
    //更新
    Update update = Update.update("location", userLocation.getLocation())
            .set("updated", System.currentTimeMillis())
            .set("lastUpdated", ul.getLastUpdated());
    this.mongoTemplate.updateFirst(query, update, UserLocation.class);
    return ul.getId().toHexString();
}
```

画面9：
```java
// 更新
Update update = Update.update("location", userLocation.getLocation())
        .set("updated", System.currentTimeMillis())
        .set("lastUpdated", ul.getLastUpdated());
this.mongoTemplate.updateFirst(query, update, UserLocation.class);
return ul.getId().toHexString();
```

画面11：
```java
package com.tanhu.dubbo.server.api;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLocation {
    @Test
    public void test() {
        // 测试代码
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1：PPT标题为“5. 地理位置”，子标题为“6.1. 定义pojo”。
画面14：PPT标题为“6.4. mock接口”，包含接口地址、请求参数、Headers和Body等信息。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

