# 18.联系人列表实现之编码

- 阶段：07.阶段七 探花交友项目
- 章节：day05 探花交友-实现消息功能
- 源文件：07.阶段七 探花交友项目\day05 探花交友-实现消息功能\18.联系人列表实现之编码_【海量资源尽在 666java.com】.mp4
- 时长 16分39秒（音频 999s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们来实现我们的联系人啊查询的这个列表呃那么我们来看一下这个接口那么这个呢是对我们这个messagescontext然后呢去发起get请求呃然后他的请求参数呢有这么三个一个是page一个是page size还有一个keyword那么显然呢这块是需要去做搜索的对吧但是呢我们现在呢需要去
[00:27] 说明的一点是这个搜索啊那我们本身呢应该去走我们的这个全文检索比如说像elect search啊这样的一些这个搜索服务啊去做搜索但是呢我们目前呢基于我们
[00:40] 现在这个课程的一个设定的情况那我们就不去集成我们elite search了而是我们直接在数据库做搜索就可以了这样做其实是不是很专业的那么我们如果真正去做项目的话那么应该在这一块呢所使用的是elite search或者说我们使用这个solar来做一个完成这样都是可以的
[01:01] 好那么呃这两个呢就不说了一个就是当前页和呃这个页面大小然后下面这个是返回的数据结构也是我们标准的一个分页的这样的一个数据结构啊然后呢下面呢这是我们的一个数据啊数据的一个这样的一个结构啊呃然后呢我们就按照这个结构吧我们去分装我们的一个对象啊就叫context啊呃这个对象那我们把它呢拷贝一下然后呢来丢到我们的这个server的VO这个里面来
[01:30] 那么找到我们的这个server下面有一个VO网站一丢好那么这个就是我们的联系人啊这样的一个这样的一个对象了那么我们就最终我们返回的肯定是基于这个对象去做一个返回对吧好那么下面呢我们就先来去定义我们的double的这个接口那么首先呢在我们的这个us api中呢我们定义两个方法那么一个呢是根据用户id呢来查询他的这个所有的这个列表
[02:00] 那么第二个是做分页那么为什么会有两个我们简单来说一下就是说那么如果说我们是这个就是不是通过Keyword查询的话那我们就直接走MangoDB分页就可以了但是如果是说我们要去做我们的关键字查询的时候那么我们的MangoDB里面就没有保存Nikname所以说没有办法在MangoDB中去做一个分页
[02:29] 而必须要走数据库那么这个时候呢我们就需要把用户的所有的这个好友的全部都查询出来然后呢我们再去查询数据库做一个这样的一个这个排除然后呢我们才能拿到我们想要的数据啊那么大致呢是这样的一个逻辑我们解释一下那么一会儿呢我们在编码的时候呢再给大家去做一个详细的一个讲解然后呢我们先把这两个呢我们先定义出来
[02:55] 那么找到我们这个double的一个接口那么我们找到这个下面的会有一个叫做users应该先找到 interface我们先找上面它接口的一个定义叫做users API那我们把这两个就拷过来好嘞好那么定义好了那么接下来我们来看一下具体的一个实现那么这个实现我们也就直接来拷贝我们的
[03:22] 具体的实现了我们可以来看一下也是非常简单的一个实现好那么把相关的包他会自动的就引入进来了那我们来看一下那么我们去做一个queryall这个操作的话那我们就只要设置一个条件就可以了就是uid等于我们这个传入的uid就可以了那么返回是一个list那么这个是比较简单的那么下面的这个是
[03:47] 需要做一个分页做一个分页那么我们要定义一个配置result对象然后配置简易然后做一个排序我们根据创建时间做一个倒序的排序就是最新去增加的我们的好友我们就排到最前面来然后我们并且设置我们的一个条件然后去做一个分页那么就可以去拿到我们的list
[04:12] 然后去做一个这样的一个分页的数据的一个返回了那么返回就是个配置info好那么现在我们这个double是不是这个接口就搞定了对吧那么接下来我们就需要做的事情就是来编写我们的这个接口服务那么接下来我们来看一下Controller那么Controller是需要按照我们的这个
[04:33] 就是所传递的一个参数那么我们去做一个分装那么我们就把它拷贝过来拷贝到哪里拷贝到我们的server这个工程中有一个叫做imcontroller那么我们把它丢到这个里面来那么把具体的一些包它会导入进来然后我们在imservice中去创建这个方法创建它
[05:01] 然后呢我们来看一下这个里面的逻辑的一个编写那么首先呢我们先拿到我们当前的这个登录的这个用户那么我们把这个包呢导入进来它等于use3local.get好那么拿到这个use之后啊下面我们就可以使用它然后呢我们就做一个判断那么如果我们的这个.is not empty如果keyword我们不等于
[05:30] 空的话那我们就说明我们需要做搜索那么做搜索的话那我们就需要查询了我们就要用this.url.api然后呢叫queryall对吧这个urlist然后呢我们传递这个url.getid查询他的所有好友的列表就可以了那么这个呢我们要定一个list定一个list那么list中所存放的就是这个url
[05:57] 对吧urls然后我们定一个这个就叫什么呢urlslist等于好那么如果是他这个keyword不等于空的话我们就去做这样的一个查询那么else的话我们就做另外一种查询就是他点query做一个分页就可以了那么第一个参数叫做url.getid第二个参数就是我们的pager第三个参数叫pager sign
[06:25] 好这样的话就可以去分页查询那么他拿到的是一个叫做叫PageInfo这样的一个对象那么其实我们需要拿到就他的一个集合了那么就通过这个UrisList去做一个复制点get一个recode那么就拿到这个UrisList那么我们拿到这个还不行对吧因为最终我们需要响应的是一些这样的一些这个数据对吧那么同样的我们就需要去
[06:54] 查询我们的用户的这个列表了那么用户的列表呢我们肯定是需要去收集一下我们的一个用户的ID对吧那我们就叫这个那么就叫什么呢F user ID user IDS user IDSnew一个arrivailist然后呢我们去做一个便利便利谁呢去便利的是我们上面的
[07:22] 这个user list然后呢f userids.and去添加一个user.get什么fade id就是好友的这个id那么接下来呢我们就需要查询用户的这个信息这个大家这个用户呢其实我们就是这个好友了好友的一些这个信息了那么怎么样查询呢那我们是不是又需要通过我们的这个叫做userinfo
[07:52] user info Service去做一个查询把它就注入进来然后我们在这个位置就通过这个list点user info Service.queryuser info list然后传递一个query的一个wrap对象对吧那么我们去定一个它那么这个叫user info对象那么我们定一个querywrap等于new一个querywrap对象好那么我们把这个querywrap给它丢进去
[08:21] 那么接下来呢我们来给他做一个设置查询谁呢首先呢我们去设置一个我们的一个呃就是什么呢我们先去要做一个这个硬这个操作对吧那么呃硬谁呢就是我们要找到我们这个字段啊那么我们这个字段显然呢是叫什么来看一下啊就是叫优惠下滑线id啊那么就要优惠下滑线id啊硬谁呢是不是就上面的一个
[08:50] F有的ids好那么第一个这个参数那么第二个这个参数呢我们还是需要去做一个判断了判断我们的这个如果我们这个keyword不为空那就需要去做一个like查询了那么前面我们说过这块呢我们呢就去直接通过mycircle去做查询了那我们就不通过我们的这个一些这个全文搜索的一些框架来做实现了好那么我们就把这个keyword去传递过去做一个like这个查询
[09:19] 那么应该是叫什么呢我们去增加一个应该就是这样的然后呢缺少一个字段那么like谁呢就是我们的nickname来看一下这个nicknamenick下滑线name那我们就要设置一下nick下滑线name然后呢去like他那么这样的话呢我们就设置完我们这个条件了对吧那么他呢就会去拿到一个他呢就会拿到一个什么呢
[09:49] 拿到一个我们的这个那么这个这个直接提示不出来了那么就直接来写吧那我们就写到这个前面去那么他所拿到的其实就是一个我们这个list就叫url info list等于他好那么下面我们还是需要去做判断那么判断谁呢还是去判断我们这个keyword是不是等于空那我们还是通过steam有tools
[10:19] 2.1日empty那么如果 keyword等于空我们就直接去遍历遍历我们的遍历我们上面所写的叫做userslist就可以了然后我们还需要再去遍历谁我们 user info list然后去做一个判断
[10:46] 那么如果这个users.get那么fredid.longvalue如果等于等于谁呢这个userinfo.getid然后点longvalue如果相等OK那么这样的话你就找到这个user这个数据了对吧那么先做break的一个操作
[11:07] 然后呢上面呢我们需要去定义一个集合那么这个集合呢最终存的是我们这个叫什么呢就是刚刚我们所定义的context对吧然后呢这个对象那么我们就要context list那么去定义它然后呢在我们的这个里面呢就需要去定义这个context对象好那么去new一个context对象然后呢最后呢把这context
[11:34] list做一个&添加加进来好那么这样的话呢我们是不是就搞定了这样的话就搞定了然后呢我们去做一个set这个操作那么首先呢这个id其实我们这个id呢在我们这个前端这个位置告诉我们其实这个是非必须的其实没有什么实际意义所以呢我们就不做一个这个设置了点点set谁呢这个city城市
[12:02] 那么这个city呢是通过这个优热info是不是能够拿到呀那么就这个优热info点get city那么要注意了我们这个city呢我们可能是需要做一些这个处理那么比如说我们只显示这个上海或者是北京啊那么在我们之前的这个数据中啊那么它可能是这样的一个数据所以说我们需要去截取这个横杠前面的这个数据啊那么我们来截一下那么怎么去截呢那么应该这样来截一下
[12:32] 通过String.src.utils.substring然后它通过一个谁呢横杠去做一个截取这样的话我们就截到了我们在所需要的一个程式了点set我们再去设置userid那么这个userid那就是我们的这个userinfo点get什么呢userid然后这块它是需要一个支付券类型的我们就给它tostring一下
[13:02] 然后我们再继续设置然后还需要设置的是这个Nikoneme叫UseInfo.get什么呢Nikoneme这样这个没问题然后点Set谁呢就是我们的一个Gender一个性别UseInfo那么点Get一个Six点Name然后转成一个To一个小写对吧
[13:27] 然后呢还要去设置一个什么呢我们的一个这个就是头像youtubeinfo.get一个logo还有吗.set设置一个age那么我们还是通过youtubeinfo来get一个age好这样的话我们就设置完成了啊好那么这样设置完成之后呢最后呢我们是不是就拿到一个这个youtubeinfo的list那么最后呢我们就可以去做一个返回了啊那么一会儿我们来做最后这个返回
[13:56] 然后呢如果是这个else操作呢那代表着我们需要做一个这个就是关键字的一个搜索那么这个时候呢注意了我们就不能够去做这样的一个便利了如果我们便利它它的数据会非常多啊非常多那么我们肯定是要便利这个扫的这个数据对吧那肯定要先便利的是我们这个user info list便利它便利它呢这个才是我们真正需要返回的这个数据
[14:23] 这个大家能不能够去想明白我们要先遍历它先遍历它然后我们就直接来遍历遍历谁呢遍历我们上面的这个user info list那么遍历它就OK了然后这个里面的这个就是它的分装逻辑逻辑是一样的那我们把它拷贝一下拷到这来那我们来看一下它的分装逻辑是OK是一样的
[14:50] 那么有同学说那么既然我们只便利它那我们是不是就没有必要查询前面这个呢并不是因为这个呢也是一个我们查询的一个条件再加一个关键是是两个条件所以说我们需要这样做这样的一个分装然后呢最后呢我们就需要去定义我们的一个叫做page result对象了那我们来定义一个page result等于new一个page result
[15:17] 最后呢我们去返回返回它就可以了我们来给它设置一些内容那么首先呢我们来看一下set这个page size那就是page size那么我们来设置几个值set一个page那就是那么set一个page那就是我们当前的这个page还有个叫set pages那么这个是总页数那我们这个不提供那么这个我们也不需要它
[15:44] 然后呢Counts也设置为0然后呢我们还需要set一个就是iTerms这个呢我们就把我们上面这个context这个list去传进去这样的话呢就可以了最后做这样的一个返回啊OK好那么我们到这里呢我们这个查询逻辑呢就搞定了那么下面我们来看一下我们这个讲义中这个逻辑的这个查询逻辑啊
[16:09] 看一样不一样那么也是需要去做一个判断拿到我们的一个这个U的IDS然后去做条件查询那么有两个这个条件然后我们去做判断如果为空就做两层的一个循环便利如果不为空那就做一层就可以了最后去分装返回就OK了好那么关于我们这个联系人列表的一个实现那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示如何在 Java 项目中编写一个用于查询联系人列表的接口服务，涉及 Controller、Service 层的代码实现和数据组装。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了 Mock 服务的接口详情页面，接口名为“联系人列表”，路径为 GET /messages/contact，Mock 地址为 https://mock.boxuegu.com/mock/164/messages/contacts，请求头包含 Content-Type: application/json 和 Authorization: eyJ...（部分被遮挡）。
画面 2: 显示了 Typora 编辑器中的文档，标题为“day05 满足.md”，内容为“6.5、编写接口服务”章节的目录结构，其中包含“6.5.1、mock接口”、“6.5.2、定义dubbo服务”、“6.5.3、注册好友到环境”、“6.5.4、编写接口服务”等子项。
画面 3: 显示了 Typora 编辑器中的文档，标题为“day05 满足.md”，内容为“6.5、编写接口服务”章节，当前光标位于“6.5.4、dubbo接口”下方的“6.5.5、编写接口服务”标题处。
画面 4: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
if (responseEntity.getStatusCodeValue() == 200) {
    return true;
}
return false;
```
画面 5: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
public PageResult queryContactsList(Integer page, Integer pageSize, String keyword) {
    User user = UserThreadLocal.get();
    List<Users> usersList = null;
    if (StringUtils.isNotEmpty(keyword)) {
        usersList = this.usersApi.queryAllUsersList(user.getId());
    } else {
        PageInfo<User> pageInfo = this.usersApi.queryUsersList(user.getId(), page, pageSize);
        usersList = pageInfo.getRecords();
    }
    return null;
}
```
画面 6: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
List<Long> fUserIds = new ArrayList<>();
for (Users users : usersList) {
    fUserIds.add(users.getFriendId());
}
return null;
```
画面 7: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
QueryWrapper<UserInfo> queryWrapper = new QueryWrapper<>();
queryWrapper.in("column", fUserIds);
this.userInfoService.queryUserInfolist(queryWrapper);
return null;
```
画面 8: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
if (StringUtils.isEmpty(keyword)) {
    return null;
}
```
画面 9: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
List<UserInfo> userInfoList = this.userInfoService.queryUserInfolist(queryWrapper);
List<Contacts> contactList = new ArrayList<>();
if (StringUtils.isEmpty(keyword)) {
    for (UserInfo userInfo : userInfoList) {
        for (User user : usersList) {
            if (userInfo.getFriendId().longValue() == user.getId().longValue()) {
                Contacts contacts = new Contacts();
                contacts.setCity(StringUtils.substringBefore(userInfo.getCity(), "-"));
                contactList.add(contacts);
                break;
            }
        }
    }
}
return null;
```
画面 10: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
Contacts contacts = new Contacts();
contacts.setCity(StringUtils.substringBefore(userInfo.getCity(), "-"));
contacts.setUserId(userInfo.getUserId());
contacts.setNickname(userInfo.getNickName());
contacts.setGender(userInfo.getSex().name().toLowerCase());
contactList.add(contacts);
```
画面 11: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
contacts.setAge(userInfo.getAge());
contactList.add(contacts);
```
画面 12: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
PageResult pageResult = new PageResult();
pageResult.setPage(page);
pageResult.setPages(0);
pageResult.setCounts(0);
pageResult.setPageSize(pageSize);
pageResult.setItems(contactList);
return pageResult;
```
画面 13: 显示了 IntelliJ IDEA 编辑器中的 Java 代码，位于 `IMService.java` 文件中，代码片段为：
```java
pageResult.setItems(contactList);
return pageResult;
```
画面 14: 显示了 Typora 编辑器中的文档，标题为“day05 满足.md”，内容为“6.5、编写接口服务”章节，当前光标位于“6.5.5、编写接口服务”标题处。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号），这是最重要的部分：
画面 1: 无代码。
画面 2: 无代码。
画面 3: 无代码。
画面 4: 无代码。
画面 5: 无代码。
画面 6: 无代码。
画面 7: 无代码。
画面 8: 无代码。
画面 9: 无代码。
画面 10: 无代码。
画面 11: 无代码。
画面 12: 无代码。
画面 13: 无代码。
画面 14: 无代码。

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
无。

5) 不要评价画面美观，不要输出与课程无关的内容。
无。

