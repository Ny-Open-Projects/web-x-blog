# 11.探花功能实现之卡片数据展现

- 阶段：07.阶段七 探花交友项目
- 章节：day10 探花交友-Elasticsearch geo实现搜附近
- 源文件：07.阶段七 探花交友项目\day10 探花交友-Elasticsearch geo实现搜附近\11.探花功能实现之卡片数据展现_【海量资源尽在 666java.com】.mp4
- 时长 17分53秒（音频 1073s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来看一下我们这个探花这个功能啊那么这个功能呢其实我们在首页呢我们的上面的第一个这个按钮呢就是进入这个探花那么这个功能的主要的这个作用呢其实就是将我们的一些推荐的好友呢然后随机的给他去展现出来并且呢是通过这种卡片式的这种方式的去做一个展现出来那么用户呢会通过一个非常快捷的一种方式
[00:29] 就是左滑和右滑来表示对这个推荐的好友是否喜欢那么做一个这个操作啊那么往左滑呢就是不喜欢往右滑呢就是喜欢那么就说我往这面滑哎那么比如说啊来画一下啊比如说往这面滑那代表的就喜欢那么如果说我往这面滑那代表就是不喜欢啊所以说有这样的一个操作啊那么要注意的是呢如果说对于这个喜欢这个操作而言啊那么如果我们双方呢
[00:59] 都喜欢那么就会成为这个好友啊互为这个好友了那么所以说呢我们需要有个逻辑呢是在这个里面那么如果说对于不喜欢呢我们暂时呢先不做处理但是大家可以想一下那么如果我们是有这个不喜欢的话那么我们在做一些好友推荐的时候是不是就可以去参考这个因素然后呢去降低它的一个分值那么这样的话是不是就不会去推荐出来了
[01:26] OK好那么这个呢就是我们的这个探花功能啊接下来呢我们就来做一个实现那么下面呢我们就来把我们的Controller的方法呢我们来拷贝一下啊那么这个呢我们要丢到我们这个todaybest这个Controller中那么我们来找一下啊是在我们的这个里面啊然后呢我们把它丢到最下面来那么这个呢就是我们探花这个功能那么接下来呢我们就在我们这个Service中啊来实现啊我们的这个方法
[01:55] 来看一下然后呢我们把这个方法来做一个实现下面我们来写一下这个方法那么前面说过呢我们是需要查询到我们的一些这个推荐数据然后呢我们去做一些随机的一些这个推荐对吧所以说呢我们就来写下这个代码那么首先呢我们肯定需要拿到我们当前的这个用户对吧等于谁呢叫做user seed local然后呢点get操作拿到我们当前这个user
[02:25] 然后呢下面呢我们就调用this.我们的这个recommend这个user Service然后呢有个叫query.recommend.user list然后这个方法那么这个方法呢需要传递三个参数那么第一个参数呢就是我们的一个用户ID那第二个参数呢就是配置那么第三个参数呢就是我们需要去获取的我们这个count数啊那么比如说呢我们要获取比如说50条啊这个推荐
[02:53] 然后呢它呢就会返回一个我们的一个PageInfo那么接下来我们是不是需要去做一个判断处理啊那么如果我们的这个应该用什么呢我们的一个ConnectedUtilsIsEmpty如果我们那个PageInfo.getRecode如果为空那么就代表着什么呢我们这个推荐的集合呢是为空的
[03:16] 就没有一些数据啊那么下面呢我们就应该去什么呢使用我们的一个默认的一个推荐列表那么这个默认的推荐列表呢上面我们是不是已经就写过这个逻辑了那我们来找一下啊那么上面的我们的呃找这个推荐啊是在这一块啊那么我们就把这个啊就拿过来然后呢我们啊网站丢啊网站丢然后呢拿到默认推荐列表呢然后呢我们用逗号去分割
[03:47] 然后拿到他的这个S那么就是我们的一个用户的一个ID然后去做这样的一个设置那么其实我们这一块没有必要去使用他的这个就是分子了因为我们在MOOC接口中是没有他的那么下面我们来可以看一下我们这个MOOC接口那么我们是在这个里面找到我们这个就是碳花这个左滑右滑
[04:13] 然后我们来看一下这个里面是不是只要返回三个字段就可以了对吧就是一个ID一个头像一个就是尼称所以说在这个位置就没有必要用score了就把它去掉然后我们把它加到record里面来我们就通过pageinf.getrecord然后做一个按的操作那么这样的话我们就完成了一个我们的一个集合的这样的一个
[04:41] 获取那么我们去第一是查询那么如果没有查询到就采用默认那么接下来我们就拿到我们的叫做pageinfo.getrecode那么拿到这个recode我们来看一下这个就是我们的recode我看一下我们定义到上面定义到这这种也可以好那我们就直接来使用它
[05:09] 然后呢下面我们来使用它那么下面呢我们就需要去做一个循环那么也就是我们需要去随机从我们这个50个这个中啊比如说我们随机10个啊出来那么随机10个选出来呢就可以去展现了但是大家要注意一下就是我随机我的目标呢是随机10个对不对但是我查询到的这个集合呢有可能呢小于
[05:35] 这个10那么如果我去直接拿10个的话肯定会这个速度下标越界的对吧肯定拿不到那么这个时候怎么办呢我们就定义一个叫一个show count它等于什么呢我们定义一个mess.me然后呢10和我们的一个recordrecord那么上面这个我们是不是写的有问题啊record怎么写了一个c呢对吧record应该用它啊
[06:05] 那么用它用它那么record它的一个size那么这这俩呢谁最小那就用谁啊也就是说我们可以保证我们最大呢就用到这个10然后呢我们接下来呢就可以去做一个我们的一个循环了对吧那么循环小于谁呢小于肯定我们这个so count对吧小于它然后呢我们去做一次我们的这个
[06:35] 随机去获取啊获取我们的这个值啊那么怎么样去获取这个值呢我们就需要写到一个新的一个这个集合中对不对啊那我们写一个list然后呢写一个recommend user然后呢我们写一个叫new啊然后呢recommend啊recommend user list那写个它吧等于new一个review list
[07:01] 然后呢我们就会往这个里面去做一个是不是丢一个对吧然后呢and去添加一个我们的一个这个数据啊而我们这个数据的它的来源呢其实就是我们去做一个我们的一个这个就是通过我们上面recode我们去随机去获取一个那就是getget一个谁呢那我们就需要去随机了那么通过random有tools.nextint
[07:30] 然后呢我们从零开始然后呢到谁呢我们的这个就是recommendrecommend那就是我们的这个recordsrecords它的size-1这个就它的一个取值范围那么我们随机通过我们这个集合呢去获取一个这个数据这个数据然后呢我们来看一下那么
[07:56] 如果啊那么我们随机拿到这个值呢就丢到这个里面来那么我们总共呢是循环的十次对吧循环十次当然了这个里面有个逻辑需要大家注意一下就是我们这个有可能会重复对不对有可能会重复所以说呢我们最好呢是去做一个排除这个重复的一个操作啊那么我们可以这么来判断一下对不对那么我们就可以这么来玩吧拿到它
[08:26] 然后呢我们就这么来写啊这么来写然后拿到一个recommend user然后呢我们去判断一下就说我们这个new一个recommend user list中是不是包含了我们这个recommend user那么如果没有包含的话那我们就做一个这个按键操作啊没有包含就把它加进来那么如果有包含的话那么这个时候怎么办呢
[08:55] 这个时候呢我们就要随机再生成一次但是这个时候呢有可能还是去重复对吧那么这个时候呢我们就要去写一个这个地归来做一个操作了这样的话才能够去保证我们这个不重复是不是那我们来看一下这个地归是怎么写那么我们在下面这个位置吧就写一个私有的一个方法就可以了小的一个地归的一个方法那么就是我们的一个
[09:24] 叫做create吧create我们的一个recommendrecommend user啊那么我们去产生啊这个他啊那这是一个地归方法我们去写一下啊地归随机生成生成我们的一个这个推荐好友啊这个要保证什么的不重复啊那么这个我们来看一下怎么玩那么首先呢肯定我们需要把我们这个
[09:53] 就是我们这个list是不是传递过来这是第一个传递过来第二个我们还需要把我们的叫什么呢Rickmonde是不是就是叫这个recodes这个也传递过来那么就是我们要从这个集合里面去拿到recodes然后我们去然后我们去做一个递归那么来看一下这个代码怎么样去做一个编写那么我们就要把我上面这个生成的这个逻辑
[10:22] 是吧那么我们是不是就要去把这块这个逻辑对吧我们就要拿到拿到这个里面来然后呢我们来看一下那么在这个里面呢我们那就应该是那这样啊应该是我们把这个什么呢把这个整个复迅环整个这个复迅环呢我们都给他拿过来那么我们这个其实不用拿这个复迅环了那么还是这样吧就在这个里面去生成就可以了
[10:51] 那么来看一下怎么样去做一个生成呢是不是我们去生成一个它那么如果是它已经包含的话如果不包含直接加就结这个方法就结束了那么如果要是包含的话那就开始什么呢开始我们的一个递归开始递归这个操作那我们就自己来调用自己了对吧叫create as a command user那么这个时候呢我们就把这个这两个集合呢我们再传递过来
[11:21] 把这个records也传递过来然后呢去开始去做一个递归直到它生成什么呢生成这个不相同的这个集合把它丢进来之后呢就结束所以说呢我们在这个位置啊那我们就调用循环去调用这个方法那就可以了然后呢我们传递我们的一个new recommend list还有一个records那么这样的话呢等到我们这个for循环结束那么这个递归方法执行结束之后呢
[11:51] 然后我们new recommend list集合是不是就填充就结束了那么接下来我们就需要去查询我们好友的一些信息那么我们还是需要定义一个我们的一个log然后来一个叫usrids等于new一个arrival list然后我们去做一个便利我们应该便利的是我们的上面的什么就是new recommend user
[12:20] 然后我们把这个Url 去点按的添加到添加这个recommend然后Url 点getUrl id然后下面我们是不是就去做查询了对吧我们就查询一下通过我们的一个Url info Service然后传递一个叫做什么query wrap对象Url info
[12:50] 然后呢这个叫queryrop等于new一个queryqueryrop对象然后呢我们去给它去做一个分装然后呢我们去设置一个in这个操作然后呢我们这个叫做url下滑性ID然后呢in一个我们的一个urlids然后呢我们就把它传递过去了这样的话就可以拿到我们这个url info一个list然后呢我们就可以进行做便利了
[13:19] 我们应该叫user info list好这样的话呢我们就开始去做两层便利对吧然后呢第一个便利这个recommend user然后呢我们再次便利的是我们user info list那么这两个这个操作就跟我们之前操作呢是基本上是不是就一样了对吧那我们就来看一下
[13:42] 那么其实这个呢我们不需要去循环它了对吧因为我们本身拿到的就是不重复的这个用户那么也就是我们只需要循环用户的这个集合就可以了那么我们上面这一堆去做一个推荐查询呢其实就是要拿到用户这个ID啊关键是这个下面呢我们在这个位置啊就去拗我们的一个这个响应数据就可以了
[14:04] 那么响应数据呢这个结构其实就是我们的一个今日佳人啊这个结构啊那么刚才呢我们是没有刷新啊刷新一些之后呢就会去下面这个数据啊之前没有显示全了这回就显示全了跟它是一样的所以说呢我们这个位置还是需要去new一个我们的一个叫做today of best然后呢写一个result等于new一个reveal list然后呢最后呢return它
[14:30] 那么这个里面是不是就去做分装了对吧那么这个分装呢我们其实可以来找一下前面的这个逻辑啊那我们就不去写这个逻辑了对吧那么找一下今日佳人的这个逻辑那么就在这对吧然后呢去给他去补全这个对吧那么或者我们去看找推荐吧这个这块是不是也是OK的对吧拿到他然后呢下面这个这个是一个分值这个就不需要去设置了因为我们
[14:58] 在展现的时候呢没有这个分值那我们就直接把上面这个拷贝过来吧然后呢我们就拷贝到啊这个里面来呃然后呢接下来呢我们给他加到我们的这个result中啊点按的去做一个添加啊去做一个添加好加到这来哎OK好那么这样的话呢我们这个逻辑呢是不是就已经啊完成了可以啊简单的去
[15:22] 检查一下啊应该是没有什么问题的对吧好那么这个逻辑呢是不是也就啊搞定了好那么接下来呢我们就来测试一下我们的这个展现啊那么我们代码呢是写完了啊那么需要注意的一下是
[15:37] 那么在我们的这个讲义中啊在这一块呢并没有去做一个地规那么也就是说这块没有考虑到一个去从的一个逻辑啊那么这个呢我们可以大家可以参考讲义啊也可以去参考我们的这个代码去做一个实现啊因为这个位置呢就是我们为了去做的更加真实一些就是去保证它的不重复我们做了一个地规啊那么如果是只是一个基本的一个实现呢我们随机啊去拿就可以了哎OK
[16:03] 好那么接下来呢我们就来把我们的服务呢就跑起来那么接下来呢我们来测试一下好那么现在呢我们就把服务呢都跑起来了那我们通过这个地址呢我们来测试一下我们的这个接口啊那么返回的数据呢其实可以看到是非常正常的这样的一个数据啊只是我们这个分子呢我们不需要就给他去没有去做一个设置
[16:26] 当然我们其实最好给它设置一个0以防我们的一个APP端爆错那我们可以试一下它会不会有问题如果有问题的话那么就把它设置为0然后这个就是我们的一个模拟器然后我也把它启动好了然后我们就打开我们的应用来测试一下我们的这个碳花这个功能
[16:46] 那么虽然我们并没有做左滑右滑之后的一个喜欢和不喜欢的这个接口但是我们现在可以先把这个数据呢是不是给它先展现出来啊那么这个地址没有问题然后呢我们去登录一下然后呢我们还是使用我们这个手机号啊6868啊然后呢我们去获取验证码然后呢验证码呢是123456
[17:13] 好那么他呢就会进入到我们的这个交友的主页的这个页面来然后呢上面这个位置是不是就会有一个探花啊我们点击啊这个探花然后呢他就会进入啊这样的一个页面那么可以看到数据呢是不是就已经显示出来了只是我们现在呢像这个左滑啊左滑这个功能还有右滑这个功能哎我们选中他按左滑但这个功能我们现在这个结果是不是还没做呀对不对哎还没有好那么但是呢我们现在是不是已经
[17:42] 先把这个数据呢是不是都展现出来了哎呀OK好那么关于我们这个探花的一个数据的一个展现呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
讲解“探花”功能的后端实现，包括推荐用户列表的生成、随机去重、用户信息聚合以及最终返回给前端的数据结构。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示 Typora 文档中“探花”功能的介绍，说明其通过卡片形式展示推荐用户，用户可选择“不喜欢”或“喜欢”。
画面2：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryCardsList` 方法的 `return null;` 语句被高亮，表示方法尚未完成。
画面3：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryCardsList` 方法内使用 `RestTemplate` 发起 HTTP 请求，将 `user` 信息作为参数。
画面4：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryCardsList` 方法内使用 `StringUtils.split` 解析默认推荐用户列表。
画面5：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryCardsList` 方法内定义 `showCount` 变量，限制返回用户数量。
画面6：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryCardsList` 方法内创建 `newRecommendUserList`，并使用 `RandomUtils.nextInt` 随机选择用户。
画面7：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryCardsList` 方法内调用 `createRecommendUser` 方法，传入新列表和原始列表。
画面8：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `createRecommendUser` 方法内使用 `RandomUtils.nextInt` 随机选择用户。
画面9：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `createRecommendUser` 方法内使用 `contains` 方法检查用户是否已存在。
画面10：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `createRecommendUser` 方法内创建 `QueryWrapper` 并调用 `queryUserInfoList` 查询用户信息。
画面11：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryTodayBest` 方法内初始化 `TodayBest` 对象并设置 `setId`。
画面12：在 IntelliJ IDEA 中展示 `TodayBestService.java` 文件，代码中 `queryTodayBest` 方法内将用户信息填充到 `TodayBest` 对象中。
画面13：在 Advanced REST Client 中展示 `queryTodayBest` 接口返回的 JSON 数据，包含用户头像、昵称、年龄、性别和标签等信息。
画面14：在 Typora 文档中展示“测试”部分，包含 HTTP 请求的 URL 和请求体，用于测试接口。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面2：
```java
public List<TodayBest> queryCardsList() {
    User user = UserThreadLocal.get();
    PageInfo<RecommendUser> pageInfo = this.recommendUserService.queryRecommendUserList(user.getId());
    List<RecommendUser> records = pageInfo.getRecords();
    if(CollectionUtils.isEmpty(records)) {
        return null;
    }
    String[] ss = StringUtils.split(defaultRecommendUsers, separatorChar: ',');
    for (String s : ss) {
        RecommendUser recommendUser = new RecommendUser();
        recommendUser.setUserId(Long.valueOf(s));
        recommendUser.setUserId(user.getId());
        records.add(recommendUser);
    }
    return null;
}
```

画面3：
```java
public BString megQuery(MAPITRowValueMap map) {
    User user = UserThreadLocal.get();
    String targetUrl = this.csuService.queryUserById(user.getId());
    HttpHeaders headers = new HttpHeaders();
    headers.setContentType(MediaType.APPLICATION_FORM_URL_ENCODED);
    headers.put("userId", user.getId().toString());
    msg.put("userId", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().toString());
    msg.put("user", user.getId().

