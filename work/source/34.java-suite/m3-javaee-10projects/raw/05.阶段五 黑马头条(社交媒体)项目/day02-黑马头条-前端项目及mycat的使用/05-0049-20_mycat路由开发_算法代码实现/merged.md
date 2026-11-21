# 20_mycat路由开发_算法代码实现

- 阶段：05.阶段五 黑马头条（社交媒体）项目
- 章节：day02-黑马头条-前端项目及mycat的使用
- 源文件：05.阶段五 黑马头条（社交媒体）项目\day02-黑马头条-前端项目及mycat的使用\20_mycat路由开发_算法代码实现【海量资源尽在 666java.com】.mp4
- 时长 17分40秒（音频 1060s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好下面呢咱们就来去把这个算法给实现一下首先呢有个概念大家要先知道啊说啊这边有一个分片字段的规范命名为burst也就是说啊在你的某一个表上面应该加这么一个字段来去区分到底当前这个数据是在哪个分片上面那这个在哪里去设置呢其实
[00:23] 大家已经导入的表中已经存在了比如说咱们打开一个表啊这表的话咱们就打开这个behind entry当前的一个什么行为实体表打开打开完之后呢这里边是分了两部分好来看一看啊往前first这个呢其实就能去确定到底是哪一个分片啊那怎么去看这个东西呢来看啊首先呢第一个呢是前面这一列吧前面这一列是ID值你看跟这边的ID值是不是能对应上啊我给你啊这是ID值
[00:53] 然后后边这个呢刚后边这个呢是它的分片它的分片的它到底是存储到哪一个分片上面大家都知道咱们现在呢连接的是当前的一个mycat然后它连的时候呢它有可能会去查询多个分片上的数据对吧那你可以这样看啊比如说咱们可以打开咱们自己的本地的数据库好稍等啊咱们还是打开这个表这个表的话就是稍等还是打开这个表吧你看它是
[01:24] 一就是当前这点数据它是在哪个分片上呢在第一个分片上面然后下面三和四呢是在第二个分片上面OK啊那咱们就可以去找一找啊当前APP Hive里边好找到本地的库首先看第一个啊它应该是在这这里边是有两条数据对吧是不是两条吧是不是一和二啊OK啊咱们可以看一下当前实体
[01:50] 你看这里面是不是1和2是吧当然你也可以再看这个0里面有没有数据呢来看一看啊0里面应该是没有数据的没问题吧当然这里边还有一个东西那这个是不是3和4是在哪啊3和4是在第二个分片对吧所以说咱们可以找到第二个分片就是这块啊打开打开你看这个是不是3和4是不是都在第二个分片上面啊OK啊那这个咱们就解释明白了啊继续往下看啊
[02:20] 说它这个类型是死尊也就是说当前这一列的类型是一个死尊类型的它的格式就是当前的一个Date ID就是咱们的主件然后是分表ID是分表ID不是分片ID然后再往下看说Date ID咱们的主件是用于分组ID进行计算的分组ID进行计算为数据量提供扩展性那这句话是什么意思呢来看
[02:51] 目前的话呢目前的话咱们在配置的时候打开当前那个路了里边啊Skype里边啊比如说咱们还是拿这个举例当前这个路了里边是不是有一个分表的算法说咱们要去用主键去模拟40是吧那模拟40的话也就是说咱们需要去分40片那分40片最大的时候呢咱们能存多少数据啊能存4亿对吧因为一个表是不是存一个表是不是存1000万呢最多
[03:20] 所以说呢咱们是4亿那4亿的话呢比如说啊咱们现在这个数据啊是达不到4亿假如说这个4亿假如这个数据有一天超过了4亿那怎么办超过了4亿之后那这个数据是不是这个性能还是会降低啊所以说呢咱们要去自己去实现一个算法让他能够分组那分组的意思呢就是说现在是分了40片如果说这是第一组啊这是第一组如果说要是超过4亿的话我可以去分出来第二组
[03:50] 他就会干嘛呢再去加第二个40个分片第二组里边也是40个分片那这时候呢扩展性自然而然的就增强了咱们的算法呢就是这样首先呢你是拿到组然后最终的是拿到一个分辨ID除以mod是吧咱们那个是除以mod就可以了最终当前这个分辨ID是可以获取到当前是哪一组的分辨ID
[04:18] 当然你需要把这个组给加上你先拿出来组然后一般情况下咱们不超过4亿的话都是第一组如果超过4亿的话肯定是第二组然后最终是加上你的分辨ID就能去确定当前分辨ID了加上你的服务分辨ID是分辨ID除以MODE这里边是有三个值大家要注意一下三个值第一个是当前的STAND第二个是什么叫VOLUME是吧还有一个是MODE
[04:48] 那这三个值是干嘛用的这三个值其实都是在哪配置的都是在咱们的配置文件中去设置的在哪个配置文件中有个入了入了里边可以打开这个东西你看它里边就有三个值有三个值这是单组的容量单组的节点数单组数据的mode到底是模拟多少是吧如果说要是第一组是这样第二组的话它还是一样
[05:14] 只是组不一样每个组都是可以承受4亿当前的一个量好啊那行那咱们刚才这块咱们说了一下啊刚才这三个值咱们也说了这三个值是从当前的配置文件中去读的然后下面咱们就去用单板的方式去实现一下当前的这个算法那这算法其实呢也比较简单啊咱们一块来看一下啊首先呢是创建一个类啊然后呢是需要去继承它并且去实现当前的这个接口
[05:43] 它里边是有两个方法咱们需要去重写然后咱们在里边去定义这三个变量这三个变量对应的其实就是要读取当前这三个属性并且你要去提供啥呢SET的方法好再往下看然后分别咱们去实现两个方法第一个是计算分片是单值的如果说是一个范围差距的话咱们还要去再去计算一个范围的好了咱们就来去实现一下首先咱们去创建一个类
[06:11] 也就是说在咱们的当前的这个男啊都在这个Service里边啊去创建一个类Service mycat里边啊那是需要去继承谁呀继承来开这个文档啊继承一个类东西然后呢同时要去实现另外一个口有它然后呢去重写两个方法稍等啊这个包得小倒一下啊其实两个方法咱们再去写第二个方法啊
[06:49] 这方法的话其实跟它是差不多的这叫什么呢cat range这叫什么我看怎么写的它然后再加一个什么东西好就这个方法这个是直计算这个如果说你要传的是一个范围的话咱们用当前下面这个方法行那这个咱们就先说到这那具体该怎么去写呢刚才说了你需要去定义三个变量是吧三个变量分别是啥呢三个
[07:25] 下面这个名称你不能乱写首先咱们来写下private lang的形为什么要定义lang的形因为这个值有可能会比较这个单独的容量有可能会比较大所以说咱们第一个应该是lang的形好 跑啥呢跑它好然后再来第二个第二个是叫step这个咱们定义成integral就可以了这个数量一般会比较小一些最后一个是啥呢
[07:58] 也是integer类型的那这三个值你提供完之后你需要去提供一个set方法咱们就在下面提供了生成当前的set方法全选那这样的话咱们就做完了我现在咱们还要再去分析一下当前的这个算法到底该怎么写其实最主要的是当前这一个因为最终的咱们可以让当前的范围去一个一个去调用当前上面这个等值的那这个该怎么去做呢
[08:32] 首先这个参数是谁呢参数其实就是咱们的什么呢column其实就是咱们的boost那boost里面是什么存的呀可以看一下这里面是不是3个24个2是什么存的呀所以说这个值你要知道是啥有可能是这么存1个2比如说这个3是id这是存到了第二个分表的这种计算上面分辨上面这是这个id是1这个是啥这是2
[09:06] 二就是第二个分片对吧OK啊那没有问题那这时候我该怎么去算呢怎么去算出来当前的这种分片ID呢其实呢咱们刚才已经分析过了就是当前的这个算法我把它放到这啊放到下边行就放到这吧首先第一步要干嘛呢第一步的话呢咱们首先是要拿到当前一个对的ID是吧咱们先把这个数给算出来啊先把前面这部分给算出来首先是拿到当前的一个对的ID对的ID就是谁啊
[09:39] 就是前面这个3或者说前面这个1是吧也就是说你需要去拿到当前的一个什么这种主界ID好那这个值呢那这个值是怎么拿的呢这个值的话是不是就是从当前的配置文件中去读的呀所以说呢你要去拿到这个值的话呢刚才说了啊在在在这呢你就能拿得到行啊那这个Syp这个呢咱们也是可以从这拿得到所以说咱们这两个就不用动主要是拿当前的这个ID就可以那这个ID怎么拿呢
[10:09] 我们结局之前首先要去判断一下columnvolume然后是它运浪的时候然后咱们再去让它去调一个split然后是以什么杠然后是它分出来的一个数组咱们叫time好拿到它之后我们再去判断一下如果说它是等于等于第二个分出来之后肯定是2对吧
[10:41] 等于二的时候呢咱们才认得去操作要不然我们不操作好吧那这时候咱们首先是拿到当前这个DAT ID就是浪类型的DAT ID等于谁啊是不是就等于TAMP当前这个0啊OK啊这个0的话肯定它是错因为这个分出来之后它是啥呢它是当前的一个什么一个四五串是吧所以说这是个浪类型那怎么办呢那咱们就可以去转一下浪点offOK
[11:13] 把当前后边的东西直接装进去就完了这样转完了啊然后咱们再再拿第二个第二个就是当前的一个吗呃他这个怎么拿呀他这是一是吧这是一二我看这两个咱们都到了首先呢咱们要获取组我怎么拿刚才说了我是不是就前面的前面这个内容啊那就最后值那要拿呗吧现在怎么办呢这个的ID然后是投于谁呀投于当前的一个VOLUM
[11:48] 然后是扩起来扩解之后乘以step最终咱们这块就是一个int的一个globe好 不知道是什么 咱们就可以强转一下强转成int类型就可以了主的话不可能是有小数的所以说咱们就强转成int就可以了然后再往下再往下 那么那该拿谁的呢去拿了当前的一个分片ID来把它pulse
[12:25] 等于目前的一个什么组加上什么呢这东西是吧那组是不是有了group然后加上谁加上谁的话就是分低是boss id然后模拟谁呢推谁呢好那这样就完了最终他这应该会报错因为这个呢可能也也会是小数所以说咱们强转成嗯都可以最终呢你把这个目前的post返回这样
[12:55] 我们的算法就结束了那为了那个能够更完整完整啊咱们所以在这去打印一些东西啊咱们就跟那个那一样啊就跟咱们的笔记中是差不多的来看一看咱们打印这么一句话好呃第一个信息呢就是通行到calling586是吧第二个是pause好吧呃那当然这笔里笔记中啊还有一个就是加了一个catch那咱们也可以加一个啊加的东西也可以也很容易怎么办呢快然后是catch好吧一个savage
[13:33] exception把当前的这一类种呢直接往上挪然后呢咱们再把这个错误信息啊可以去打印一下好那这样的话就结束了啊如果这边呢是还是当前的错误信息是他具体的错误信息是你从这个exception里边去打印就可以了最终这个返回量不太合适咱们可以返回一个new什么呢integer中是一个0中咱们什么不返回会返回一个0可以了
[14:10] 行那这个咱们就做完了这个精确匹配的咱们就做完了然后下面还有一个按范围查询按范围查询其实更简单咱们主要是基于当前上面这个内容去做就可以了那这个怎么做呢首先它这边传的值肯定是两个一个是begin一个是end所以说咱们来去判断一下咱们先把它给删了别删了咱们直接去先删了一下
[14:39] 根据做判断啊是任何程序咱们都要去判断啊他不等于什么呢那并且n的value他也不等于呢然后呢咱们才去做操作然后咱们就就可以去通过当前的begin value和n的value去分别去获取他的精确的值因此值的话咱们就要用上面那个方法就可以了啊比如说begin value然后最终的是拿到他现在一个分辨ID我们叫begin嘛
[15:10] 好吧这是一个然后第二个呢一样呗想说第一项它是正义的然后这是正义的好那就拿到了当前的一个范围啊范围之后呢咱们就可以去做操作这时候咱们还可以做一步判断啊怎么判断呢如果说啊它呢是等于等于让或者是正义的等于等于让的话干嘛呢直接return一个new什么
[15:44] 直接返回一个空就可以了啊这里边是一个零OK那这样我们就算是设置完了啊设置完之后啊那下面呢咱们要真正的去计算返回一个数组对吧返回一个数组啊首先呢咱们要把这个数组啊给构建出来那构建的长度是谁呢其实就是当前那个范围对吧所以说呢咱们再往下做啊首先咱们还要再做一步判断啊什么判断呢应该干嘛呢大于等于谁啊
[16:13] 大于等于比例然后呢我们就可以做计算了啊首先是做出了一个integer的数组咱们它呢是要返回到21等于什么6一个integer它是不是需要一个长度啊那长度是谁呢长度的话其实干嘛说了就是当前比定和int的一个这种范围的长度是吧所以说呢咱们在这去拿到长度啊int等于什么呢等于int点去谁啊
[16:44] 是再加上1 ok那这个呢其实就是它的长度好然后呢咱们就可以往当前这个集合或者当前的数组中去放值了啊int i 等于0i 小于 l1然后是a 加中呢咱们就可以l1咱们可以往这边去加值那加什么值呢首先第一个值呢就是应该是1吧让谁啊1那这个呢就是它的一个比啊
[17:17] 这样的话就能去往这里边去不断的去装值最终装完之后你直接累称谁就可以了二可以了好那这样的话咱们就做完了啊那这个为了方式包错了咱们可以再去推一个什么呢跟前置一样可以了好吧成一个空可以了这个呢代码的实现呢咱们就说到这里啊

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何实现一个自定义的分库分表规则算法（HeMaBurstRuleAlgorithm），并展示其在数据库表结构和配置文件中的应用。

2) 按时间顺序列出每张画面的要点：
画面1: 显示 MySQL 数据库的表结构，包含多个以 "ap_" 和 "admin_" 开头的表，如 ap_article, ap_user, ap_user_identity 等，以及对应的触发器和存储过程。
画面2: 显示数据库中名为 "ap_behavior_entry" 的表结构，包含多个字段如 id, dataId, dataNode, type, createTime 等。
画面3: 显示一个 XML 配置文件，定义了多个表的分库分表规则，如 ap_article_content, ap_user, ap_user_identity 等，配置了 dataNode、autoincrement、primaryKey 和 rule。
画面4: 显示 IntelliJ IDEA 中的 Java 代码，定义了一个名为 HeMaBurstRuleAlgorithm 的类，它实现了 RuleAlgorithm 接口。
画面5: 显示一个 XML 配置文件，定义了多个分片规则，如 burst166, burst4040, burst5050, cron2slot, hash-int, rang-long 等，配置了 class、volume、step、mod 等属性。
画面6: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面7: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面8: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面9: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面10: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面11: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculate 方法，用于计算分片 ID。
画面12: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculateRange 方法，用于计算分片范围。
画面13: 显示 IntelliJ IDEA 中的 Java 代码，定义了 HeMaBurstRuleAlgorithm 类的 calculateRange 方法，用于计算分片范围。

3) 出现的代码、配置、命令、目录结构、SQL、XML/YAML 配置：
画面3:
<?xml version="1.0" encoding="UTF-8"?>
<rule>
    <table name="ADMIN_QRTZ_BLOB_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_CALENDARS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_CRON_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_FIRED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_LOCKS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_PAUSED_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_SCHEDULER_STATE" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_SIMPLE_TRIGGERS" dataNode="DNSQ" type="global"/>
    <table name="ADMIN_QRTZ_TRIGGERS" dataNode="DNSQ" type="global"/>
    <!-- --app_info-->
    <table name="ap_article" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_article_config" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_dynamic" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_identity" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_realname" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_follow" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_equipment" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>
    <table name="ap_user_article_list" dataNode="UNAP $0-39" autoincrement="true" primaryKey="id" rule="mod-long40"/>

画面5:
<?xml version="1.0" encoding="UTF-8"?>
<rule>
    <function name="burst166" class="com.heima.HeMaBurstRuleAlgorithm">
        <property name="volume">60000000</property><!-- 单组容量 -->
        <property name="step">66</property><!-- 单组节点数 -->
        <property name="mod">66</property><!-- 单组数据mod -->
    </function>
    <function name="burst4040" class="com.heima.HeMaBurstRuleAlgorithm">
        <property name="volume">40000000</property><!-- 单组容量 -->
        <property name="step">40</property><!-- 单组节点数 -->
        <property name="mod">40</property><!-- 单组数据mod -->
    </function>
    <function name="burst5050" class="com.heima.HeMaBurstRuleAlgorithm">
        <property name="volume">50000000</property><!-- 单组容量 -->
        <property name="step">50</property><!-- 单组节点数 -->
        <property name="mod">50</property><!-- 单组数据mod -->
    </function>
    <function name="cron2slot" class="io.mycat.route.function.PartitionByCRC32PreSlot">
        <property name="mount">2</property><!-- 一要分片的数据节点数量，必须指定，否则没法分片 -->
    </function>
    <function name="hash-int" class="io.mycat.route.function.PartitionByFileMap">
        <property name="mapFile">partition-hash-int.txt</property>
    </function>
    <function name="rang-long" class="io.mycat.route.function.PartitionByFileMap">
        <property name="mapFile">partition-hash-long.txt</property>
    </function>
</rule>

画面6:
public Integer calculate(String s) {
    return null;
}

@Override
public Integer[] calculateRange(String beginValue, String endValue) {
    return super.calculateRange(beginValue, endValue);
}

public void setVolume(Long volume) {
    this.volume = volume;
}

public void setStep(Integer step) {
    this.step = step;
}

public void setMod(Integer mod) {
    this.mod = mod;
}

画面7:
private Long volume;
private Integer step;
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    return null;
}

@Override
public Integer[] calculateRange(String beginValue, String endValue) {
    return super.calculateRange(beginValue, endValue);
}

画面8:
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    if (columnValue != null) {
        String[] temp = columnValue.split(regex);
        if (temp.length != 2) {
            long dataId = Long.valueOf(temp[0]);
            int pos = (int) (dataId / volume) * step + mod;
            return null;
        }
    }
    return null;
}

画面9:
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    if (columnValue != null) {
        String[] temp = columnValue.split(regex);
        if (temp.length != 2) {
            long dataId = Long.valueOf(temp[0]);
            long burstId = Long.valueOf(temp[1]);
            int group = (int) (dataId / volume) * step;
            int pos = group + (int) (burstId / mod);
            return null;
        }
    }
    return null;
}

画面10:
private Integer mod;

@Override
public Integer calculate(String columnValue) {
    if (columnValue != null) {
        String[] temp = columnValue.split(regex);
        if (temp.length != 2) {
            long dataId = Long.valueOf(temp[0]);
            long burstId = Long.valueOf(temp[1]);
            int group = (int) (dataId / volume) * step;
            int pos = group + (int) (burstId / mod);
            System.out.println("HEIMA RULE INFO [" + columnValue + "]-[[" + pos + "]]");
            return pos;
        }
    }

