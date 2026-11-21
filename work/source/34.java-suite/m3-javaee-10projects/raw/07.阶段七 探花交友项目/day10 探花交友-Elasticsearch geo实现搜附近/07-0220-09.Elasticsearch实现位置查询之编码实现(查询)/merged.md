# 09.Elasticsearch实现位置查询之编码实现（查询）

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\09.Elasticsearch实现位置查询之编码实现（查询）_【海量资源尽在 666java.com】.mp4
- 时长 20分8秒（音频 1208s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们继续来实现啊其他两个方法那么首先呢我们先来查询用户的一个地理位置就是根据用户ID啊去做一个查询然后呢我们就把这个拷贝过来啊然后呢我们就把它丢到我们的Controller中啊找到我们这个Controller然后呢我们放到下面的这个位置吧然后呢我们来看一下那么去创建啊这个方法啊
[00:27] 然后这个方法呢返回呢就是返回我们的这个UrLocationES对象了那么这个呢其实就是比较简单了我们直接去根据我们的一个Query去做一个查询啊就可以了那么前面呢我们这个代码是不是也写过对吧那我们就把这个就拷贝过来我们就把它丢到哪里呢是不是丢到下面的这个位置来然后呢去做一个查询然后呢那我们就直接ReturnReturn它就OK了
[00:57] 这个是最简单的一个这个查询了好那么其实这个查询呢是不是我们就啊搞定了好那么下面呢我们就通过我们的那个测试用力啊那我们来测试一下那我们下面来写一个test方法然后呢返回值呢是word然后呢testquerybyuserbyuser id啊然后呢我们去写一个test这个方法然后呢我们去
[01:26] 调用调用下面的上面的我们这个Service.querybyuid这个方法比如说我们查询1这个用户的一个地理位置的这样的一个数据那么拿到它然后我们就把它就打印出来好那么这样的话是不是就OK了好那我们执行这个操作走好那么来看一下查询到的这个数据那么这个数据就查询到了
[01:54] 那么基本上呢是没有任何问题的啊哎呀好嘞好那么呃我们的这个查询呢就搞定了那么接下来呢我们来看一下啊最为关键的一个查询就是查询附近的人那我们把这个Controller这个方法我们也拷贝过来啊然后呢我们把它丢到我们的这个Controller中啊那我们来看一下这个方法的一个编写呃那么我们来看一下哎啊好嘞那么只需要去创建呃这个方法就ok啊那我们先来看一下这个Controller的方法啊
[02:24] 那么搜索这个附近的人然后呢他的这个参数呢有这么几个参数啊有五个啊这个参数那么第一个呢就是我们的一个精度还有纬度啊还有我们的一个距离啊距离然后呢还有什么呢呃配置就是我们的一个分页啊然后呢如果他为none的话就设置为1如果不是的话就把它设置为他的值啊然后呢配置size也是这样的
[02:50] 默认的是返回100个这样的一个这个数据然后呢下面呢就去做一个查询那么关键是不是就在Service中他的这个方法的一个实现啊好那么哎那么我们去把这个嗯然后呢我们去看一下啊去做一个这个创建然后呢最后就return啊先return到啊好那么我们来写一下这个方法的一个注释啊把这个参数呢给大家注释清楚那么这个就是我们
[03:21] 查询查询什么呢附近的人然后呢这个呢就是什么呢精度然后这个是纬度然后呢我们的这个叫什么呢我们的距离也就是我们那个半径对吧距离然后呢这个是我们的一个页数那么要注意这个距离我们还是单位要设置这个单位为什么的米啊这个然后呢这个就是这个页面大小好嘞这样的话就比较清楚了
[03:51] 然后这个维是不是写的不对叫维度然后是这个好那我们来看一下这个的一个实现那么这个怎么去实现就是在elag search中这个就是根据位置查询稍微复杂那么一点点那么我们一点一点来写一下大家应该能够去理解那么首先我们需要去new一个我们一个叫nativenative的一个search query
[04:21] 然后呢当然我们需要去定他的一个build然后呢通过这个build呢我们去做一个构建啊那么我们就设置设置他吧然后呢注意这个native然后呢search query build呢他呢是实现了我们的这个来看一下啊那么我们是应该看的是谁呢叫这个嗯就是
[04:48] 这个我们最终啊注意啊那我们最终其实要拿到的是一个native query这个对象那么我们最终是要通过来看一下它会有一个build的这个方法啊那么最终我们肯定是需要拿到这个query就这个对象它呢其实是实现了我们那个search query那么我们要去查询数据啊那么肯定要通过这个search query去做一个实现就是说这个呢是实现了啊来写一下啊实现了我们这个
[05:18] 这个接口然后就是我们这个叫做native的一个sysquare它呢实现了这个接口那我们就可以去通过它呢去做一个这个构建了然后呢通过它去构建什么呢首先我们肯定是需要去构建我们的一个这个viz pageable那么就是我们的分页的这个信息那我们下面要设置我们的一个分页分页好那么分页怎么设置呢我们通过定一个page request
[05:49] 这个对象那么这个我们其实并不陌生了通过一个page request点off然后呢设置一个page-1这个-1呢别忘记然后那个pagepage-size那我们把这个page request呢丢到这个里面来好那么这样的话呢我们就设置完成这个分页了那么接下来呢我们就来设置什么呢设置我们的一个
[06:16] 查询啊设置查询那么这个查询呢我们其实要设置一个布尔查询啊所以说呢我们在elan设置中啊有很多的查询啊下面呢我们需要定义一个什么呢定义我们那个布尔啊布尔查询那么这个布尔查询呢我们要通过new一个布尔然后呢query啊query build那么要定义一个定义它啊这个别搞错然后呢来一个这个
[06:45] 这个build对吧叫bool的一个querybuild然后呢我们去给他去做一个这个我们这个是这个好像我们定义的不对吧这个包是不是引用的不对呢这个是不对的这个是lucen里面的那我们这个定义错了叫queryquerybuild应该是这个我们刚刚引入那个类是不对的应该是他这个bool没写全的这个bool那么这个
[07:14] 定义它然后呢有了这个bootquery build之后啊然后呢我们就设置我们的一个查询下面呢我们就通过我们的这个geo啊geo做一个查询那么同样呢我们需要去定义一个中心点对吧中心点然后呢并指定中心点然后呢并且指定它的一个查询范围也就是我们那个画圈的那个半径啊
[07:42] 那我们需要定义一个什么呢new一个geo然后呢disdisdisdisdis然后呢这个query一个builder啊然后呢我们去做一个这个设置啊那么这个builder中呢需要传递一个stream它呢其实就是我们一个字段啊field name那我们就来指定一个这个
[08:05] field name那么我们就指定到这个位置来field name等于谁呢它就等于我们的一个location这个字段对吧那我们来看一下是不是就是我们这个里面的location这个字段那我们把这个字段呢就拿过来往这一写然后呢就拿到field name往这一传然后呢我们就会得到一个我们的一个geo的一个distance一个query一个build然后呢我们再给它去指定我们的一个中心点
[08:35] 然后呢设置一个port那然后呢去指定什么呢我们的一个这个经纬度一个对象对吧然后呢设置一个经纬度然后呢设置一个经度来看一下对不对啊设置一个是我们的一个纬度一个是经度好那么设置完成之后啊那么接下来呢我们就需要去设置我们的查询然后设置什么呢设置我们这个还需要设置它的一个distance范围啊
[09:03] 那么我们给他设置谁呢String那么就这样我们还是去给他设置一个我们的一个这个我看啊传入的是一个double类型那就是double了然后呢他呢要除以多少呢1000因为我们单位呢是米然后呢并且呢我们去指定他的一个这个单位对吧叫dstins
[09:29] 然后呢我们设置它的一个这个单位呢是千米就是我们的一个公里啊一千米啊就是设置设置它了设置一个这个单位那么这个呢就指定了我们一个这个查询了这个GU的这个查询然后呢我们把这个我们指定的这个查询啊我们把它丢到我们这个布尔查询里面就是我们去做一个must啊must必须必须要满足我们这个条件啊把它呢
[09:58] 丢进来然后接下来我们把我们的布尔查询然后丢到我们的就是我们上面所我们来看一下那么就上面的我们native search这个build中然后我们去设置一个位置一个什么query把我们就是我们布尔查询给它丢进来
[10:24] 不好查询丢进来这样的话呢我们就构造完成这个查询啊然后呢我们还是需要给让他去给我们按照距离呢去设置一个排序啊那么我们去按照什么呢来看一下啊按照按照我们的一个距离啊做一个排序啊这个我们就去做一个生序吧就是生序
[10:46] 就是从小到大然后做一个这个声序或者说从近到远这样的一个声序那么我们就需要去设置一个我们的一个new一个geogeo的一个distance然后呢它会有一个叫sort那an c esort然后呢我们呢有一个叫做sortbuild有个这个对象
[11:15] 然后我们去设置它有两个参数我们来看一下那么第一个参数就是我们的一个字符串那么第二个就设置我们的经纬度那我们就来看一下那么这个字符串其实是需要指定我们的一个字段名的那么指定它然后我们设置我们的一个纬度然后再设置我们的一个经度好那么来看一下有没有问题它需要的是一个字段
[11:42] 还有一个是我们的纬度和精度啊然后呢我们就会拿到一个谁呢拿到我们的一个这个build的这个对象啊然后呢build的对象然后呢我们再给他去设置什么呢设置我们的一个这个单位啊这个他单位呢是一个千米对吧刚才跟我们刚才所设置的是一样的这个是我们的一个距离的一个单位然后呢接下来我们要设置他的一个排序
[12:12] 就是设置他点什么呢这个有个叫order做一个排序啊然后呢我们定义一个set order asc然后呢做一个什么呢做一个我正序的一个排序也就是我们的一个生序啊生序然后呢有了这个之后啊那么下面呢我们来那么我们就需要把我们这个geo的this sort build呢丢到我们这个native里面来native里面来那么到这啊
[12:40] 然后呢,为一个sort,为一个sort,那么我们把这个给它再丢进来,所以这个呢稍微有一点点复杂,那么丢到这个里面来,丢到这儿,丢到这个里面来,那么这个就是我们,就相当于现在我们是不是已经把我们的这个整个查询构造完成了,你看这个位置是构造分页,下面这个呢是构造我们的一个这个查询,查询呢所采用的是一个boll这个查询,
[13:07] 然后呢下面的这个呢是设置我们的一个距离的一个生序就是一个排序啊做一个这个sort然后呢我们就可以去做一个查询了那么通过race.elagsetterplay然后呢我们就设置一个query for什么呢
[13:25] 然后我们来看一下传递这么几个参数第一个参数就是我们这个native search query对象通过这个build对象去得到一个query对象那么第二个就是我们的一个class叫yield location yes class好那么这样的话就会得到谁的得到我们的一个这个配置对象那么最后给它返回去那这样吧我们就直接return吧到这里我们就直接return就好了
[13:55] 好下面就不需要它了这个代码就写完了这个代码稍微有一点点复杂不过呢好在还是比较容易理解的那么接下来呢我们就按照刚才所写的测试用力那我们来测试一下看它是否有问题那么下面我们来看这个测试用力呢是这样的就是我们传递一个经纬度这个经纬度呢还是我们的那个就是用户ID为1的
[14:21] 这个用户的一个近纬度查询一公里范围内的一些这个用户然后呢Page Size设置100然后呢我们去查询查询到之后啊我们做一个4Each循环然后呢我们把它打印出来并且呢我们通过这个GEO的一个Distance来计算它的一个这个距离那么我们设置一个这个是这个是这个中心的一个距离啊然后呢去设置它的一些这个单位就可以计算出
[14:49] 它和我距离我的一个距离是多少米大家最后看这个这个设置的单位这个设置单位呢是米所以说呢就会拿到是多少米OK好那我们就来执行一下好那么这个执行结果呢就出来了那么总共呢查到有这是一条两条三条四条数据但是第一条呢是自己本身是不是所以可以看到距离我的距离呢就是零米
[15:17] 然后呢下面一条呢是在上海中心大厦然后它距离我的这个距离呢是196米然后呢还有就是陆家嘴地铁站呢是459米然后呢东方明珠呢这个是725米所以可以看到呢这个数据是按照我们距离的一个生讯呢去做一个排序的那么并且呢也能够看出它的一个距离我的一个距离多米啊哎OK那么其实由此可见呢我们是不是已经就
[15:45] 把我们的这个服务呢是这个代码是不是就写好了对吧那么接下来呢我们就可以把我们这个服务就跑起来然后我们再来测试一下看他有没有问题了好那我们来启动一下我们这个服务那么就是我们的elac search的这个服务找到他找到是在是在这个里面对吧这个启动之前我们这个是不是有问题我们需要把它丢到这个里面来那么刚才我们这个包呢放的是有问题的
[16:14] 那么所有的这个它会自动去做一个修改这个时候就没有问题了那么这个里面呢应该也是没有问题吧看一下啊没有问题那么这个ES这个包是不是就导入进来了检查一下那然后呢是在这里啊没有问题的好那我们把这个我们的应用呢就跑起来来看一下效果好那么我们这个服务呢跑起来了接下来呢我们就可以来测试一下啊到了测试之前呢我们需要先去修改一个东西啊什么呢
[16:40] 就是我们的NJAX啊那么NJAX呢我们之前的一个配置我们来看一下啊那么之前的我们是不是去设置了我们这个User然后进入的是18080然后呢这个呃我们的这个就是这个呃其他的进入这个18081啊但是呢我们现在所请求的这个呢它是一个什么呢以这个ES是不是开头的这个服务对吧然后呢我们所以要添加一个
[17:09] 他添加一个他然后呢指向的18082这个端口那么这个大家的把上面这个拷贝一下然后拿下来之后呢去改一下改一下这个位置就可以了好嘞那么这样的话呢我们就可以去请求他了那么接下来呢我们就来实际的来测试一下然后呢我们来找到谁呢找到我们的这个ES这个地址那我们就测试其中一个就可以了那么我们去来测试一下测试他
[17:38] 然后呢发起的是一个来看一下啊那么下面这个呢是发起的是一个get请求那么就写一个这个附近的人哎这个是一个post请求对吧然后呢后面有一个下面有一个list然后呢在我们的这个请求题里面呢有这么几个参数啊当然至少你是有三个这个参数的啊那我们就来构造一下那么他的请求呢这个头其实不需要了你加也无所谓啊然后呢我们就设置一个这个json
[18:07] 然后呢我们去添加一个这个参数啊然后呢这个呢是我们的一个精度那精度是多少呢我们这样我们先把这个写好再来写下面内容然后呢这个是纬度啊然后呢我们再去写一个这个distance距离然后呢我们来看距离我就直接确定那么就是这个1000米然后呢上面的是我们的这个纬度啊经纬度的数据那我们就抄一下这个
[18:37] 我们测试用力中的这个数据啊那么把这个拿过来这个是我们的一个精度那么精度呢放到这然后呢记得打一个逗号然后呢下面这个是纬度那么把这个呢也拷贝一下然后呢也去打一个这个逗号然后呢这个距离是一切去做一个查询看一下这个结果那么这个结果是不是跟我们刚才看到的结果呢是一样的金光大厦啊然后呢上海中心大厦然后呢还有就是陆家嘴啊等等的啊
[19:06] 然后呢要注意的是呢在我们想运回的这个location这个对象啊那么它呢是有四个这个字段的其实我们只需要两个就可以了对吧但这个你返回这俩也无所谓那我们要这俩就可以了啊这个你根据需求自己去拿这个值呢就可以了好那么其实我们去测一个就可以了其他的也就非常的类似了你比如说你想去测这个control的话这个查询的话那直接就传递一个get请求对吧把list改成1
[19:35] 我查询这个1的这个用户的地址是不是就查到了OK好那么关于我们这个查询的这个编写是不是我们就已经搞定了那么这样的话我们是不是就已经
[19:47] 通使用这个elac search来实现了我们地理位置的一个查询了对吧那么接下来呢我们是不是就应该在我们double服务中呢去调用我们的这个所编写的这个服务然后呢去实现我们的这个就是ES版的这样的一个double服务了OK好那么关于这个呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Spring Boot 项目中使用 Elasticsearch 的 NativeSearchQueryBuilder 构建基于地理位置的查询和排序功能。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 UserLocationController 中的 @GetMapping 查询用户位置的接口，以及 @PostMapping 更新用户位置的接口。代码中包含参数解析和异常处理。
画面 2: 展示了 TestLocationService 中的 testQueryById 方法，用于测试根据用户 ID 查询位置信息，并计算与给定经纬度的距离。
画面 3: 展示了 UserLocationController 中的 @PostMapping 更新用户位置的接口，以及对应的目录结构，包括 Controller、Service、resources 等包。
画面 4: 展示了 UserLocationService 中的 NativeSearchQueryBuilder 的 build() 方法，用于构建 NativeSearchQuery。
画面 5: 展示了 UserLocationService 中的 queryUserFromLocation 方法，开始构建 NativeSearchQueryBuilder。
画面 6: 展示了在 queryUserFromLocation 方法中，创建 GeoDistanceQueryBuilder 并设置中心点和距离范围。
画面 7: 展示了在 queryUserFromLocation 方法中，创建 BoolQueryBuilder 并将 GeoDistanceQueryBuilder 添加到其中。
画面 8: 展示了在 queryUserFromLocation 方法中，创建 GeoDistanceSortBuilder 并设置排序字段和单位。
画面 9: 展示了在 queryUserFromLocation 方法中，将 GeoDistanceSortBuilder 设置到 nativeSearchQueryBuilder 中。
画面 10: 展示了 DistanceUnit 类的源码，定义了距离单位，如 MILES 和 METERS。
画面 11: 展示了 TestLocationService 类的测试方法 testUpdateUserLocation，用于测试更新用户位置功能。
画面 12: 展示了 application.properties 文件中的配置，包括 location 路由和 proxy 相关的设置。
画面 13: 展示了 UserLocationController 中的 queryUserFromLocation 方法，包含参数解析和异常处理。
画面 14: 展示了 day10 课程笔记中关于 RestTemplate 的配置和使用，以及 UserLocationController 中的 queryUserFromLocation 方法。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
```java
@GetMapping("userId")
public ResponseEntity<UserLocationES> queryUserLocation(@PathVariable("userId") Long userId) {
    try {
        this.userLocationService.queryUserById(userId);
        if (null == userLocationES) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
        }
        return ResponseEntity.ok(userLocationES);
    } catch (Exception e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
}

/**
 * 更新用户的地址位置
 */
@PutMapping("update")
public ResponseEntity<UserLocationES> updateUserLocation(@RequestBody Map<String, Object> param) {
    Long userId = Long.valueOf(param.get("userId").toString());
    Double longitude = Double.valueOf(param.get("longitude").toString());
    Double latitude = Double.valueOf(param.get("latitude").toString());
    String address = param.get("address").toString();
    boolean result = this.userLocationService.updateUserLocation(userId, longitude, latitude, address);
    if (result) {
        return ResponseEntity.ok(null);
    } catch (NumberFormatException e) {
        e.printStackTrace();
    }
    return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
}
```

画面 2:
```java
public void testQueryById() {
    this.userLocationService.updateUserLocation(userId: 301, longitude: 121.462452, latitude: 31.253463);
    this.userLocationService.updateUserLocation(userId: 321, longitude: 121.815478, latitude: 31.157478);
    this.userLocationService.updateUserLocation(userId: 341, longitude: 121.327908, latitude: 31.20033);
    this.userLocationService.updateUserLocation(userId: 361, longitude: 121.490155, latitude: 31.277876);
    this.userLocationService.updateUserLocation(userId: 431, longitude: 121.594194, latitude: 31.207761);
}

@Test
public void testQuery() {
    Page<UserLocationES> userLocationPage = this.userLocationService.queryUserFromLocation(121.512253, 31.24094, 1000);
    userLocationPage.forEach(userLocationES -> {
        System.out.println(userLocationES.getLoca);
        double distance = GeoDistance.ARC.calculate(31.24094, 121.512253, userLocationES.getLoca);
        System.out.println("距离实：" + distance + "米");
    });
}
```

画面 3:
```java
@GetMapping("list")
public ResponseEntity<List<UserLocationES>> queryUserFromLocation(@RequestParam Map<String, Object> param) {
    Double longitude = Double.valueOf(param.get("longitude").toString());
    Double latitude = Double.valueOf(param.get("latitude").toString());
    Double distance = Double.valueOf(param.get("distance").toString());
    Integer page = param.get("page") == null ? 1 : Integer.valueOf(param.get("page").toString());
    Integer pageSize = param.get("pageSize") == null ? 100 : Integer.valueOf(param.get("pageSize").toString());
    Page<UserLocationES> userLocationES = this.userLocationService.queryUserFromLocation(longitude, latitude, distance, page, pageSize);
    return ResponseEntity.ok(userLocationES.getContent());
} catch (NumberFormatException e) {
    e.printStackTrace();
}
return ResponseEntity.status(HttpStatus.INSUFFICIENT_STORAGE).build();
```

画面 4:
```java
public NativeSearchQueryBuilder withIndicesOptions(IndicesOptions indicesOptions) {
    this.indicesOptions = indicesOptions;
    return this;
}

public NativeSearchQueryBuilder build() {
    NativeSearchQuery nativeSearchQuery = new NativeSearchQuery(queryBuilder, filterBuilder, sortBuilder, highlightBuilder, highlightFields);
    nativeSearchQuery.setPageable(pageable);
    nativeSearchQuery.setTrackScores(trackScores);
    if (indices != null) {
        nativeSearchQuery.addIndices(indices);
    }
    if (types != null) {
        nativeSearchQuery.addTypes(types);
    }
    return nativeSearchQuery;
}
```

画面 5:
```java
public Page<UserLocationES> queryUserFromLocation(Double longitude, Double latitude, Double distance, Integer page, Integer pageSize) {
    // NativeSearchQueryBuilder nativeSearchQueryBuilder = new NativeSearchQueryBuilder();
    PageRequest pageRequest = PageRequest.of(page - 1, pageSize);
    nativeSearchQueryBuilder.withPageable(pageRequest);
    // 定义bool查询
    BoolQueryBuilder boolQueryBuilder = new BoolQueryBuilder();
    return null;
}
```

画面 6:
```java
// geo查询，定义中心点，指定查询范围
GeoDistanceQueryBuilder geoDistanceQueryBuilder = new GeoDistanceQueryBuilder(fieldName);
geoDistanceQueryBuilder.point(latitude, longitude);
geoDistanceQueryBuilder.distance(distance);
```

画面 7:
```java
// geo查询，定义中心点，指定查询范围
GeoDistanceQueryBuilder geoDistanceQueryBuilder = new GeoDistanceQueryBuilder(fieldName);
geoDistanceQueryBuilder.point(latitude, longitude);
geoDistanceQueryBuilder.distance(distance / 1000, DistanceUnit.KILOMETERS);
```

画面 8:
```java
// 按照距离排序
GeoDistanceSortBuilder geoDistanceSortBuilder = new GeoDistanceSortBuilder(fieldName, latitude, longitude);
geoDistanceSortBuilder.unit(DistanceUnit.KILOMETERS); // 距离单位
```

画面 9:
```java
// 按照距离排序
GeoDistanceSortBuilder geoDistanceSortBuilder = new GeoDistanceSortBuilder(fieldName, latitude, longitude);
geoDistanceSortBuilder.unit(DistanceUnit.KILOMETERS); // 距离单位
nativeSearchQueryBuilder.sort(geoDistanceSortBuilder);
```

画面 10:
```java
// 'm' is a suffix of 'nm' so it must follow 'nm'
MILES(1609.344, "mi", "miles"),
// since 'm' is suffix of other unit
// it must be the last entry of unit
// otherwise parsing would fail
METERS(1, "m", "meters");
public static final DistanceUnit DEFAULT = METERS;
DistanceUnit(double meters, String... names) {
    this.meters = meters;
    this.names = names;
}
```

画面 11:
```java
package com.tanhua.es.Service;

import com.tanhua.es.pojo.UserLocationES;
import org.Elasticsearch.common.unit.DistanceUnit;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.context.junit4

