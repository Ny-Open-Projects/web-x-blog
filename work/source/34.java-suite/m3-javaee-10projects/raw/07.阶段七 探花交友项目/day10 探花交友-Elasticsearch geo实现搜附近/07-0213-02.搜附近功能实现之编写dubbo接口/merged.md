# 02.搜附近功能实现之编写dubbo接口

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\02.搜附近功能实现之编写dubbo接口_【海量资源尽在 666java.com】.mp4
- 时长 15分11秒（音频 911s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下收附近啊这个功能那么在我们的首页中呢我们上面的去点击那个收附近啊就可以去看到下面这个界面啊它是这样的一个效果那么可以看到呢我们呢会去
[00:16] 按照我们当前的用户所在的地理位置然后呢去查询周边的一些用户这样的一些这个情况然后呢当然这个位置会有一个session那么它有两个条件一个就是我们的距离比如说我们会设置500米或者一公里或者是3000米三公里这样的一个条件那么另外一个条件呢就是我们的性别
[00:42] 是男性啊还是女性啊做这样的一个筛选啊所以说呢是这样的一个这个效果啊那么接下来呢我们就会要结合到前面啊我们所提到的用户的一个这个地理位置的个数据啊那么前面呢我们已经完成了每一个他这个用户的一个地理位置的一个上报就是上报给我们的服务端然后呢我们呢就给他存储起来了
[01:09] 那么存储起来之后啊那么接下来呢我们就需要去查询那么我们在mongodb中又该如何去做一个地理位置的一个查询呢那么这个就是我们接下来要讲的重点内容了好那么下面呢我们来看一下下面的内容啊那么首先呢我们来定义我们的double的接口那么在前面呢我们这个叫做UraLocation API中啊是不是只定义了一个更新用户地理位置的这个方法啊那么接下来呢我们还需要去
[01:38] 定义两个方法那么第一个呢就是根据什么呢用户ID去查询他自己的一个地理位置那么第二个呢是我们根据一个用户的一个地理位置来查询他的一些在一定范围内的
[01:54] 这个run的范围对吧一定范围内的这个用户那么也就是所谓的什么呢我们查附近啊查附近比方说传递他啊1000米那就是在1000米这个范围内的一些这个用户那我们要实现这两个方法那么细心的同学呢会发现那么我们的在这个位置所使用的对象啊返回对象呢是叫UrlocationVO
[02:18] 而我们之前呢所定义的对象叫做Urelocation这个对象那么我们为什么不直接使用这个对象而去使用这个VO这个对象呢原因是啊原因是什么呢原因是我们这个Urelocation这个对象它呢不能用来直接做来直接做序列化那么有同学觉得会比较奇怪就是说在这个位置我们明明是不是已经实现了我们序列化的接口
[02:47] 但是它依然是不能够序列化的为什么呢原因就是在这那么原因我们使用了我们的一个叫做geo jsonport这样的一个对象它呢不能被这个序列化序列化呢会出错所以说呢导致我们这个类呢就不能够序列化了那么大家可以去测试一下我这个呢就不测了那么如果我们直接将这个unlocation对象
[03:14] 去做序列化的话会报错所以说呢我们只能去换一个思路来做了用一个新的对象去取代它所以我们称为叫什么呢Ura Location VO下面呢我们就来看一下我们这个VO这个对象那么叫做Ura Location VO它呢也是需要去实现我们这个序列化接口然后呢设置几个这个属性那么当然这个里面呢跟我们前面所定的Ura Location呢
[03:42] 是非常的相似只是呢我们这个location这个位置呢通过这个经纬度呢去做了一个替换那么去用这个double类型的一个经纬度然后呢下面呢我们写了两个方法并且是一个两个静态的方法那么叫做format方法就是我们通过your location能够转化得到我们的一个your location vo那么这个里面其实就是做一些
[04:09] 自断的值的一些拷贝那么只是呢我们把这个我们的经纬度的以之前的location去转化为它的经纬度啊去做这样的一个值的一个复制就可以了而下面呢这个叫做format to list那么就是把我们的这个location的一个集合
[04:29] 去转化成一个locationVO的这样的一个集合当然了它还是调用这个format的这个方法去做一个转化好那么接下来呢我们就把这个U的locationVO这个对象呢我们来拷贝到我们的这个就是server下面我们再来创建一个包就叫VO这个包VO是不是已经存在了看一下啊之前已经有那我们就直接把它拷贝过来
[04:57] 叫UrLocationVo这样的一个对象那么接下来我们在实现我们这个接口的过程中就可以使用这个对象以及下面所定义的这两个方法了那么下面的我们就在我们的这个我们来看一下那么这个API是不是我们还没有拷贝过来那我们来拷贝一下就在上面的我们定义两个这个方法两个查询的方法好那我们往这一丢
[05:26] 好来看一下有没有问题没有问题吧那么接下来呢我们就来找到我们的一个Url Location API的一个实现内容那我们来实现啊这两个方法那么我们把这两个方法呢写出来然后呢我们分别的来做一个实现那么首先呢我们先来实现的就是我们这个根据用户ID呢去做一个我们这Url Location的一个查询
[05:54] 那么这个其实就比较简单了对吧那么我们只需要根据我们user id是一个条件就可以了那么我们就通过我们这个this.mongo.template然后呢调用它的find什么的one肯定只有一条数据对不对那么query呢先设置为none然后呢第二个这个参数我们设置user location.class要注意这个位置我们所设置的是user location而并不是
[06:22] 这个location vo所以说我们还需要把这个对象去转一下那么我们来看一下那么我们就会拿到我们这个yourlocation这样的一个对象那么接下来呢我们来给它设置这个query这个对象query等于query.query这个方法然后呢我们去通过criteria去做一个条件那么这个yourlocation中啊有个叫做yourid
[06:51] 我们就把它呢作为我们的一个这个条件啊放到这儿然后呢依谁呢就是我们这个UID啊就是他这个就是我们的一个查询条件然后呢我们把这个query呢给它丢到这个位置来然后呢我们就拿到一个UID location啊这样的一个对象那么接下来呢我们做一个判断如果我们空不等于这个UID location的话
[07:19] 那我们是不是就可以return所以是不是我们有一个叫做uselocationVO因为这个方法的反为者是不是要求是VO点有一个format这个方法那么把这个uselocation传递过去这样的话我们是不是得到一个VO这个对象了
[07:38] 那么通过这个format这个方法做一个这个数据的一个拷贝那么最后呢就可以啊返回了那么这个呢就是我们啊最简单的一个查询如果这个U location等于空的话那我们这个VO呢也只能去返回空了所以说这个位置return了啊好那么这个就是根据用户ID呢去做一个查询那么接下来我们来看这个啊这个是我们实现的一个关键了那么接下来呢我们来画一个图啊我们来分析一下啊
[08:07] 那么我们把这个简单的画一个示意图啊那么大家这个呢就理解了好那我们来看一下那么你比如说呢我们就画一个这个圆啊假设这是我们的这个地球然后呢我们每一个人呢在上面其实都是有什么呢都是有我们的一些这个坐标的对吧或者说我们所在的位置啊它都是有个坐标的那比如说我们就随便点一些这个点啊比如说
[08:34] 在这啊在这我随便点一些啊随便点一些这个呃用户啊有很多的这些这种点啊随便我点一点啊那么这个就是我们的用户的这个数据了对不对那么我们如何去做一个查询呢他的一个逻辑呢是这样的一个逻辑啊就是说首先我们肯定要找到一个中心点啊比如说呢我们是以这个用户啊以这个用户为中心比如说呃我当前这个用户张三啊这个用户
[09:04] 它呢是在这个位置假设是在红点的这个位置啊那么它呢要去查找它周边的啊附近的一些这个用户那么我们就会以谁呢以这个点为中心然后呢我们再去设置它的一个什么呢距离你比如说它的距离设置是一公里比如说一公里呢哎那么我们这个细一点那么一公里呢假设啊假设这个一公里呢就假设一公里啊
[09:34] 放大一点啊那么假设我们这个一公里啊一公里呢它就这么大啊这么大啊比如说一公里呢就这么大然后呢我们呢就会干嘛呢我们会基于我们的这个呃这个什么呢半径去画圆是吧画一个圆那么我们大致吧画一个这个圆啊大致能够去呃描述这个意思大家就能够理解了啊那么我们来画一个圆啊比如说呢这个就是我们去画了一个圆
[10:04] 那么所有啊落到我们这个圈里面的这个用户那么就是我们要去查询的一个这个用户了所以说我们接下来编码的逻辑啊也是这样的一个逻辑那么首先呢我们需要做什么事情啊首先呢我们就需要根据啊根据什么呢传入的这个坐标啊进行什么呢进行我们的确定确定我们的一个中心点
[10:32] 确信我们的中心点那么我们就需要定义一个叫做geo jsonport这样的一个对象叫做geo jsonport对象然后呢new一个geo jsonport这样的一个对象然后呢我们传递两个参数一个呢就是基因度一个呢就是纬度这个数据那么这样的话呢我们这个红色这个点是不是就确定了那么接下来呢我们需要设置它的一个
[11:01] 这个半径啊这个半径我们接下来来看一下传入的我们这个run它呢是我们的一个这个距离单位啊距离单位而我们的数据存储到我们的这个mongodb中啊它其实是一个什么呢这是一个球面上的这样的一个这个位置所以说呢我们需要去转化一下它啊那我们把它转成什么呢转成一个dishtest啊这样的一个对象
[11:30] 那我们就去new一个叫做distest这样的一个对象啊啊你啊你有一个他然后呢我们传递啊两个参数那么第一个参数就是我们的值那我们这个用者是单位是米那我们除以1000啊除以1000然后呢我们设置他的一个这个呃设置一个这个matrix这个呢就是我一个单位啊我们设置他是一个这个千米啊
[11:58] 来看一下就是我们的一个这个公里对吧就千米啊设置它啊然后呢我们就会得到一个我们的一个distance那么这个呢其实就是我们的一个那个半径啊就是我们的一个这个半径或者说是一个距离了这个画圈的啊画圈啊呃画圈的一个半径啊半径啊半径好那么这是两个参数啊那么可以看到这个是我们的中心点
[12:28] 那么下面这个呢是半径那么接下来呢我们是不是就该画什么呢是不是画一个圆了那么下面呢我们去new一个这个circle对象就是圆对吧然后呢CLE对吧我看啊这个叫什么呢C啊写错了CIR啊CLE然后呢传递两个参数那么第一个参数叫做GEO就是我们的中心点第二个呢就是我们这个半径啊这个距离
[12:57] 那我们这样的话就画了一个什么呢画了一个这个圆圈对吧那么我们来看啊这个就是我们画了啊画了一个啊圆啊画了一个圆呃圆圈啊好那么这个呢是不是就确定了我们的一个范围了那么接下来呢我们就会根据我们这个圆圈呢我们去做一个这个查询那我们定义一个这个query这个对象啊query它等于我们的一个
[13:25] 这个query然后呢设置一个条件啊creator然后呢vailvail谁呢就是我们的这个叫做usernamelocation中的一个对象啊叫location啊这个对象呃然后呢我把这个对象拿过来啊拿到他然后呢我们设置一个viz啊viz啊in sphere然后呢我们把这个呃这个圈给他对吧啊把这个圈给他
[13:54] 那么它的一个值呢就是在这个圈内圈内的值然后呢这个就是我们的一个query条件那么接下来呢我们就通过我们的mongo templatefed什么呢我们设置一个fedfed一个那就是fed了对吧两个条件两个参数一个呢就是我们的一个这个query那么第二个呢就是yourlocation.class
[14:20] 那么他所拿到的是一个叫做Urallocations的一个集合那么最后呢我们要求返回的是一个VO的这个集合那我们就通过这个VO他有一个叫什么呢Format to List这个方法把这个Urallocations传递过去这样的话呢是不是就OK了那么大家要理解这个代码那么其实跟我们刚刚画的图的原理是不是一样的那么就是说我们先要确定我们这个中心点
[14:49] 然后呢去设置一个我们的一个这个半径啊就是大小然后呢我们去画一个这个圆圈设置我们查询的一个条件然后呢做查询然后呢最后做一个return啊这样的话呢就可以了好那么关于我们这个呃double接口的一个服务的一个实现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在基于 Dubbo 的服务中，使用 MongoDB 实现根据用户 ID 查询附近好友的地理位置功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示“搜附近”功能的 UI 效果，提示“您附近有25个好友”。
画面2：展示代码编辑器中 UserLocationVo 类的定义，注释说明“由于UserLocation不能序列化，所以要再定义UserLocationVo进行返回数据”，并列出导入的包。
画面3：展示 UserLocationVo 类的 format 方法，用于将 UserLocation 对象转换为 UserLocationVo 对象。
画面4：展示 UserLocationVo 类的 format 方法，与画面3内容一致。
画面5：展示 UserLocationApiImpl 类中的 save 方法和 queryById 方法，其中 queryById 方法返回 null。
画面6：在 queryById 方法中，使用 CriteriaDefinition 构建查询条件。
画面7：在 queryById 方法中，调用 format 方法转换返回值。
画面8：展示一个绘图软件界面，用于演示地理围栏的圆形区域。
画面9：在 queryUserFromLocation 方法中，创建 GeoJsonPoint 对象。
画面10：在 queryUserFromLocation 方法中，创建 Distance 对象。
画面11：在 queryUserFromLocation 方法中，创建 Circle 对象。
画面12：在 queryUserFromLocation 方法中，使用 Query.query(Criteria.where()) 构建查询。
画面13：在 queryUserFromLocation 方法中，使用 this.mongoTemplate.find(d) 执行查询。
画面14：在 queryUserFromLocation 方法中，返回 UserLocationVo.formatToList(userLocations)。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
package com.tanhua.dubbo.server.pojo;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
```

画面3：
```java
public static final UserLocationVo format(UserLocation userLocation) {
    UserLocationVo userLocationVo = new UserLocationVo();
    userLocationVo.setAddress(userLocation.getAddress());
    userLocationVo.setCreated(userLocation.getCreated());
    userLocationVo.setUpdated(userLocation.getUpdated());
    userLocationVo.setUserId(userLocation.getUserId());
    userLocationVo.setLongitude(userLocation.getLocation().getX());
    userLocationVo.setLatitude(userLocation.getLocation().getY());
    return userLocationVo;
}

public static List<UserLocationVo> formatToList(List<UserLocation> userLocations) {
    List<UserLocationVo> list = new ArrayList<>();
    for (UserLocation userLocation : userLocations) {
        list.add(format(userLocation));
    }
    return list;
}
```

画面5：
```java
userLocation.setCreated(System.currentTimeMillis());
userLocation.setUpdated(userLocation.getCreated());
this.mongoTemplate.save(userLocation);
return userLocation.getId().toHexString();
```

画面6：
```java
CriteriaDefinition criteriaDefinition
```

画面7：
```java
return UserLocationVo.format(userLocation);
```

画面9：
```java
GeoJsonPoint geoJsonPoint = new GeoJsonPoint(longitude, latitude);
```

画面10：
```java
Distance distance = new Distance(value / 1000, Metrics.KILOMETERS);
```

画面11：
```java
Circle circle = new Circle(geoJsonPoint, distance);
```

画面12：
```java
Query query = Query.query(Criteria.where(...));
```

画面13：
```java
this.mongoTemplate.find(d)
```

画面14：
```java
return UserLocationVo.formatToList(userLocations);
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面8：展示一个绘图软件界面，用于演示地理围栏的圆形区域，没有标题或表格数据。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

