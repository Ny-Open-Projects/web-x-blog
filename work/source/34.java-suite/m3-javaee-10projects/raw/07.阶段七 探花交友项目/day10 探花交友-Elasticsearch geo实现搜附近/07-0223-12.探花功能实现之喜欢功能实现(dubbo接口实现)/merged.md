# 12.探花功能实现之喜欢功能实现（dubbo接口实现）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\12.探花功能实现之喜欢功能实现（dubbo接口实现）_【海量资源尽在 666java.com】.mp4
- 时长 11分51秒（音频 711s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现我们的这个喜欢这个功能那么这个功能呢我们需要去从我们的这个double接口的一个定义呢去开发那么首先呢我们先来定义我们的一个这个usernike这样的一个对象那这个呢主要是用于存储我们的用户喜欢就喜欢这个某些人他的一些这种信息啊那么可以看到呢我们这个表呢叫usernike
[00:28] 然后呢下面有这么几个字段我们一起来看一下那么这个呢是ID啊下面这个是User ID这个就是自己啊自己这个ID然后呢这个是LikeUser ID就是你喜欢谁啊去记录对方然后呢这个还有个创建时间好那么我们把这个呢就来做一个拷贝啊然后呢丢到我们的这个Double服务的这个Interface中丢到我们这个里面来
[00:57] 那么OK好那么这个就丢进来了那么丢进来之后那么接下来我们就定义我们的一个double的一个接口那么我们来把这个接口拷贝到我们API这个里面来这个就是一个叫做Uderlike API那么这个包把它去掉然后我们来看一下在我们的接口中定义了这么几个方法那么第一个是叫做保存喜欢C5Uderlike
[01:22] 然后呢传递两个参数一个呢是用户ID一个就是like的UID然后呢还有的是相互喜欢就是是否是相互喜欢那么前面呢我们说到过一个逻辑就是说如果双方要是双向啊互相喜欢的话那么他们就会去注册为一个这个好友啊或者说加为一个好友那么我们所以说需要有个方法来判断这两个用户啊他是否是相互喜欢
[01:49] 然后还有就是删除用户喜欢就是用于不喜欢比如说用户不喜欢它就可以把它删除掉那么这个是我们简单的一个实现是可以这样去做一个实现的如果说我们要针对于用户不喜欢要做一些比如说像推荐上面的一些音质的一些操作的时候我们可能就需要去记录他的不喜欢的这种一些数据了然后用于我们的一个减分减分项
[02:16] 好嘞那么这个就是我们的一个接口那么接下来我们来看一下它的一个实现类那么我们就要进入到我们的Service下面去做一个实现然后我们在下面找到我们的API然后我们来写一个叫做imppl这样的一个实现它去实现的就是我们的这个接口实现它
[02:44] 好然后呢我们去实现它的三个方法好然后呢我们把它呢这个呢定义为是一个我们的一个double的一个Service然后呢这个版本呢同样的设置为是1.0.0然后在这个里面呢我们肯定会用到的是mongo的一个template对吧那么我们就把它呢就注入进来
[03:08] 好那么有了这个mongo的这个template之后呢然后呢我们就可以去做下面的一些这个实现了好那我们就分别来看一下这三个方法的一个实现那么首先呢我们是需要去判断一下对吧判断我们的这个就是喜欢的这样的一个关系啊是否存在那么我们需要先去做查询了那么就定一个这query应该叫query吧
[03:37] query点query然后creative然后呢creative然后呢点will设置一个谁呢就是我们这个user id他然后呢点一只他然后呢我们再设置一个我们的一个什么呢就是will他然后呢and是吧所以设置一个and条件然后呢还有一个就是like的user id然后呢他呢点
[04:06] 那么这个呢作为我们查询的一个这个条件啊然后呢我们这个就会得到一个query这个对象然后呢我们下面呢就做一个判断如果我们的这个template做一个count查询然后呢query给他然后呢设置为这是一个叫urlike.class然后呢如果他要大于0那就说明什么呢这个数据是不是已经存在了
[04:32] 直接转天档就可以了那么如果不存在我们就需要去给他设置一个urlike这样的一个对象我们设置一个urlike等于new一个urlike然后urlike.seturlike.setid那么这个显然就是我们的一个object id然后我们再继续set一个谁就是like的id
[05:00] like的UID那就是上面的它了然后呢我们再来一个set一个UID那么这个呢就是一个UID那么这俩然后呢还有还缺一个吧就是这个created这个呢要设置为是一个created就是我们当前的一个时间戳了当前时间戳好嘞那么这样的话呢我们就可以做一个save保存了点save一个操作然后呢我们把这个UID like传递过去
[05:30] 最后呢我们返回是我们的一个这个ID值对吧叫做userlike拿到ID然后呢拿到他的一个字符号好那么这样的话呢我们的这个C5是不是就搞定了那么下面呢我们来看其他两个方法啊那么我们先来看这个删除因为这个呢是比较简单的啊那么其实这个是就查询的比较会麻烦一点啊那我们来看一下这个删除吧那么删除呢我们就直接去调用谁呢
[06:00] 我们this.mongo-template然后做一个delete叫remote这个操作然后也是有两个参数query那么query同样的其实也是我们上面query对吧那就把它拷贝过来那么放到这然后这个就是query那么还有一个class那就是我们的一个yourlike class.class
[06:27] 然后呢他呢就会拿到一个我们的一个delete的一个result那我们就判断他的一个这个count数是不是等于1那么如果要是等于1的话那就说明删除成功了那么如果要是不等于1的话那就肯定删除失败了对不对好那么接下来呢我们就实现这个方法那么这个方法要实现的是什么呢就是我们的一个是否互相互相
[06:57] 喜欢是否互相喜欢那我们就需要给他设置一个较为复杂的一个查询条件了那我们来看一下这个应该怎么做那么我们肯定需要给他设置两个这个条件对吧那么首先呢我们来看一下啊Creator will设置一个叫做UID然后呢点一日他然后呢我们再去设置一个and这个
[07:26] 点按的然后呢我们再设置一个这个like user id点啊依日啊然后呢like user id然后呢点啊依日他那么这个条件跟我们刚刚的这个条件呢是一样的对吧那么我们这个呢就把它设置为是我们的character1啊character
[07:50] 这是我们第一个这个条件那我们来拷贝一下来给大家去生成我们第二个这个条件那么我们就改成什么呢对方对吧UID等于这个对方并且呢我们这个like UID呢等于他那我们就需要做这两个条件注意啊这两个条件之间是一个什么关系我们要把它设置为是一个all的关系就是或者的关系啊所以说呢我们还需要再定义一个我们的一个
[08:17] crate a new一个crate设置它的一个all的一个option一个操作然后呢我们把这两个呢crate给它啊服装进来然后呢这个两个服装进来啊然后呢它呢就会得到一个新的一个crate然后呢接下来呢我们就可以通过谁呢我们的mongotemplate然后呢做一个count查询那我们就直接在return这个位置吧那么大家可以想一下啊就是
[08:46] 那么我们根据这个条件查询那我们查询到他有几条数据的时候那么就是他相互喜欢呢他一定是什么等于什么两条数据的时候对不对啊那么只要保存了这有两条数据那就说明他们相互喜欢了然后呢我们来设这个count啊count呢两个参数那么一个呢叫做query.query把query传递给他第二个参数呢就是我们的yourlike.class
[09:13] 好那么这样的话呢我们是不是就已经啊完成了这个方法这个编写那么大家这个能够理解吗对吧只要我们把这个参数给他去颠倒的然后呢去查询一次只要能够查到两条数据啊那就说明什么呢那就说明啊这两个是相互喜欢了好那么接下来呢我们就来去写一下啊我们的一个呃这个单元测试啊
[09:37] 那么这个就实现了我们不看它了我们去看单元测试那我们就直接来使用它吧然后我们就把它拷贝到哪里我们的这个test目录下面来到这然后我们来看一下这个里面的测试就是把我们这个userlikeapn的注入进来然后我们做一些save操作我们save一个关系就是1 2就是用户1喜欢用户2然后用户1也喜欢用户3
[10:04] 用户二喜欢用户一所以说我们插入这三条数据然后我们下面的去做一个判断就说一和二是不是相互喜欢的那么二和一是不是相互喜欢一和三是不是相互喜欢然后再做一个删除这个就是可以测试我们刚刚写的几个方法了
[10:25] 那么我们测试之前需要保证两个操作第一个就是我看一下我们的这个数据那么我之前应该是有数据的那我把这个usrlike这个我给它drop掉把这个cool给它drop掉然后我要再把我这个double要停掉然后我们去来启动一下好我们先来去执行它好那么等待一下
[10:48] 好那么我们这个呢就执行结束了啊来看一下我们的数据啊那么可以看到下面的Uderlike呢是不是就有三条这个数据了对吧那么用户ID1呢喜欢2然后呢1呢喜欢3然后呢这个2呢喜欢啊1那么接下来呢我们来就来测试一下啊他的这个相互喜欢的这样的一个关系啊好那我们来等待一下好那么我们来看一下他的一个结果那么就是呃1和2呢是好友设置为处啊相互好友
[11:17] 那么二和一也是然后一和三就不是了所以返回FORCE那么所以说明这个方法也是OK的那么接下来我们就执行delete那么就会把这三条数据给它删除掉好那么可以看到我们打印了三个chew那就代表数据删除了那我们来测试一下看它到底有没有数据发现数据已经就被删除了好那么这个就是我们的一个喜欢的一个
[11:44] 这个double接口的一个实现好那么关于我们这个接口的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
实现用户点赞功能的 Java 代码，包括定义实体类、接口、实现类以及单元测试。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示 UserLike 实体类定义，包含 @Document 注解和字段。
画面 2: 展示 UserLikeApi 接口，定义了 saveUserLike、isMutualLike、deleteUserLike 三个方法。
画面 3: 展示 UserLikeApiImpl 类的初始结构，实现接口的三个方法。
画面 4: 在 UserLikeApiImpl 中注入 MongoTemplate。
画面 5: 在 saveUserLike 方法中构建查询条件，检查是否存在。
画面 6: 在 saveUserLike 方法中创建 UserLike 实例并设置属性。
画面 7: 在 saveUserLike 方法中调用 mongoTemplate.save 保存对象并返回 ID。
画面 8: 在 isMutualLike 方法中构建查询条件，检查是否为相互喜欢。
画面 9: 在 isMutualLike 方法中使用 Criteria.where 构建查询条件。
画面 10: 在 isMutualLike 方法中构建查询条件并调用 remove 方法。
画面 11: 展示 TestUserLikeApiImpl 类的初始结构，实现接口的三个方法。
画面 12: 在 TestUserLikeApiImpl 中编写 testSave、testIsMutualLike、testDeleteUserLike 三个测试方法。
画面 13: 在 testIsMutualLike 方法中打印相互喜欢的测试结果。
画面 14: 展示 TestUserLikeApiImpl 的完整代码，包含三个测试方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import org.bson.types.ObjectId;
import org.springframework.data.mongodb.core.index.Indexed;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@AllArgsConstructor
@Document(collection = "user_like")
public class UserLike implements java.io.Serializable {
    private static final long serialVersionUID = 673996663629466523L;
    private ObjectId id;
    private Long userId; //用户ID，自己
}
```

画面 2:
```java
/**
 * 保存喜欢
 * @param userId
 * @param likeUserId
 * @return
 */
String saveUserLike(Long userId, Long likeUserId);

/**
 * 相互喜欢
 * @param userId
 * @param likeUserId
 * @return
 */
Boolean isMutualLike(Long userId, Long likeUserId);

/**
 * 删除用户喜欢
 */
```

画面 3:
```java
package com.tanhua.dubbo.server.api;

public class UserLikeApiImpl implements UserLikeApi {
    @Override
    public String saveUserLike(Long userId, Long likeUserId) {
        return null;
    }

    @Override
    public Boolean isMutualLike(Long userId, Long likeUserId) {
        return null;
    }

    @Override
    public Boolean deleteUserLike(Long userId, Long likeUserId) {
        return null;
    }
}
```

画面 4:
```java
@Autowired
private MongoTemplate mongoTemplate;
```

画面 5:
```java
Query query = Query.query(Criteria.where("userId").is(userId)
        .and("likeUserId").is(likeUserId));
```

画面 6:
```java
UserLike userLike = new UserLike();
userLike.setId(ObjectId.get());
userLike.setLikeUserId(likeUserId);
userLike.setUserId(userId);
userLike.setCreated(System.currentTimeMillis());
```

画面 7:
```java
this.mongoTemplate.save(userLike);
return userLike.getId().toHexString();
```

画面 8:
```java
public Boolean isMutualLike(Long userId, Long likeUserId) {
    Query query = Query.query(Criteria.where("userId").is(userId)
            .and("likeUserId").is(likeUserId));
    this.mongoTemplate.remove(query, UserLike.class);
    return null;
}
```

画面 9:
```java
Criteria criteria = Criteria.where("userId").is(userId).and("likeUserId").is(likeUserId);
```

画面 10:
```java
Query query = Query.query(Criteria.where("userId").is(userId)
        .and("likeUserId").is(likeUserId));
DeleteResult deleteResult = this.mongoTemplate.remove(query, UserLike.class);
return deleteResult.getDeletedCount() == 1;
```

画面 11:
```java
package com.tanhua.dubbo.server.api;

@Service(version = "1.0.0")
public class UserLikeApiImpl implements UserLikeApi {
```

画面 12:
```java
@Test
public void testSave() {
    this.userLikeApi.saveUserLike(userId: 11, likeUserId: 21);
    this.userLikeApi.saveUserLike(userId: 11, likeUserId: 31);
    this.userLikeApi.saveUserLike(userId: 21, likeUserId: 11);
}

@Test
public void testIsMutualLike() {
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 21));
    System.out.println(this.userLikeApi.isMutualLike(userId: 21, likeUserId: 11));
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 31));
}

@Test
public void testDeleteUserLike() {
    System.out.println(this.userLikeApi.deleteUserLike(userId: 11, likeUserId: 21));
    System.out.println(this.userLikeApi.deleteUserLike(userId: 11, likeUserId: 31));
    System.out.println(this.userLikeApi.deleteUserLike(userId: 21, likeUserId: 11));
}
```

画面 13:
```java
@Test
public void testIsMutualLike() {
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 21));
    System.out.println(this.userLikeApi.isMutualLike(userId: 21, likeUserId: 11));
    System.out.println(this.userLikeApi.isMutualLike(userId: 11, likeUserId: 31));
}
```

画面 14:
```java
import org.junit.runner.RunWith;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;

@RunWith(SpringJUnit4ClassRunner.class)
@SpringBootTest
public class TestUserLikeApiImpl {
    @Autowired
    private UserLikeApi userLikeApi;

    @Test
    public void testSave() {
        this.userLikeApi.saveUserLike(11, 21);
        this.userLikeApi.saveUserLike(11, 31);
        this.userLikeApi.saveUserLike(21, 11);
    }

    @Test
    public void testIsMutualLike() {
        System.out.println(this.userLikeApi.isMutualLike(11, 21));
        System.out.println(this.userLikeApi.isMutualLike(21, 11));
        System.out.println(this.userLikeApi.isMutualLike(11, 31));
    }

    @Test
    public void testDeleteUserLike() {
        System.out.println(this.userLikeApi.deleteUserLike(11, 21));
        System.out.println(this.userLikeApi.deleteUserLike(11, 31));
        System.out.println(this.userLikeApi.deleteUserLike(21, 11));
    }
}
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

