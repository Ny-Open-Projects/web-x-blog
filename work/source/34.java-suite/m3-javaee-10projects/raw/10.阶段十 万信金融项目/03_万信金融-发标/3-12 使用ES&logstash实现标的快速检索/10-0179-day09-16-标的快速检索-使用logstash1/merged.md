# day09-16-标的快速检索-使用logstash1

- 阶段：10.阶段十 万信金融项目
- 章节：03_万信金融-发标/3-12 使用ES&logstash实现标的快速检索
- 源文件：10.阶段十 万信金融项目\03_万信金融-发标\3-12 使用ES&logstash实现标的快速检索\day09-16-标的快速检索-使用logstash1_【海量资源尽在 666java.com】.mp4
- 时长 15分49秒（音频 949s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 刚才我们在本机已经把logs-给安装过了相关的环境也搭建好接下来咱就开始学习如何使用logs-先问大家一个问题再回顾一下我们在这里使用logs-是干嘛的是让它干嘛的对我们是让它从mycircle数据库中干什么采集数据也叫读取数据然后把这些数据在向es当中写入
[00:30] 这个过程当中它会自动创建所以这是我们使用logstash的目的就是数据采集和数据同步那咱接下来呢主要就是学习一下logstash是如何进行数据采集如何进行数据同步的我们需要大概了解一下让大家看一下这张图那么这个图里边让大家看到我们很清晰的表明了logstash要从mycircle数据库采集数据是吧还要干什么呀
[01:00] 他把数据呢写入到ES索引库里边那这两个功能他怎么办到呢主要是靠两个配置文件两个配置文件啊我们接下来主要是讲这两个配置文件也就是说呢数据采集数据同步这两个功能是由logstash搞定的你不用管我们不用管但是我们需要给他提供两个配置文件在这里边你想啊你最最起码我们想到的是你要告诉他告诉谁啊告诉logstash你要连接哪个数据库
[01:30] 对吧数据库里边那么多表你要采集哪个表的数据啊大家想是不是然后你还要告诉他我这个采集的数据我要写入到yes的哪个库里边这个库里边这个字段哪些是需要进行分辨哪些不需要分辨你是不是都得告诉他刚才说的这些信息对不对所以你不告诉这些信息他也不知道从哪采数据对吧也不知道数据呢我要图不到哪里所以说呢我们玩logstash其实说到最后主要就是玩什么呀玩配置
[02:00] 两个配置那在图里边也告诉大家了啊一个是模板文件一个是我们起了一个名字叫my circle-什么es.configure这样一个配置文件那这两个配置文件分别是干啥呢在讲义里边也告诉大家你看模板文件主要就是配置映射信息就我刚才说的所有库里边它都有哪些字段字段都是什么类型哪些字段分词哪些字段不分词对不对
[02:26] 这个映射大家应该有印象吧其实映射不就是相当于咱们数据库里边的表结构吗对不对表结构那么另外一个配友链它的作用就是我们刚才说的你要告诉他从哪个数据库哪个表里边采集数据啊对吧你还要告诉他这些数据我要写入到ES的哪个锁定库里边对不对这信息通通是在这个配友链里边进行配置所以这是我们得大概知道logs-它是如何工作那咱接下来
[02:54] 按照顺序吧咱先搞定这个模板文件那咱先看这个模板文件长什么样吧其实就是一个json你看扩展名这个模板文件的快门就是什么呀json这里边都有啥呢咱先了解了解你看东西还挺多这个mapping大家以前见过就是映射的意思吗properties其实就是属性说白了就是都有哪些字段对不对这个映射我们刚才说了其实相当于咱数据库当中的表结构你看这里边这都是字段名是不是字段名然后type是什么呀大家还有印象吗
[03:27] 是不是字段的类型当然它这个类型呢跟咱数据库的不太一样啊不太一样但你看这个名字大概能能看出来它是什么意思啊因为这些咱之前学过特别是这里边你要注意这些地方analizer还有印象吗这是设置这个字段要分词以及采用的这个分词策略是不是你看我们还有哪个字段分词呀name标底的名称是不是也进行分词等等等等哎这个就是我们说的这个模板文件它里边配置的这个什么映射信息
[03:58] 然后最下边我们还起了一个模板名模板名字可以自定义我起的名字叫万星p2p下线project这是模板名这就是咱说的模板文件它里边这个内容这个模板文件放到什么地方大家注意了非常重要我们可以把模板文件放到logs-config目录下面咱接下来把这个事做一下在资料文件夹里边这个模板文件我在这其实都给大家准备好了你可以ctrl c
[04:28] 然后直接找到你电脑上logstash对吧找到哪个目录configure然后给它粘过来放到这就OK了这是我们说的这个谁模板文件模板文件搞定之后既然还有另外一个配置文件这个配置文件是至关重要的非常非常重要就是mysock也是configure那这个配置文件它里边东西比较多而且呢我们在使用这个配置文件之前我们还要做一个准备工作什么准备工作咱一起看一下我们要执行
[05:00] 一块搜索语句这个搜索语句是干嘛呢我们大家看一下你看alert table是不是修改表的结构对吧修改哪些表呢你看我们是不是把标底信息呢那两个库当中的四个表全部都要进行修改是吧我们当时是不是进行分库分表的两个库里边有四张表是不是修改什么内容呢我们是不是添加了一个字段叫add column对不对添加了一个字段叫modify data
[05:29] 然后这是字段的类型是不是然后什么呀允许为空这个字段表是修改时间数据的修改时间数据的修改时间就是标底信息它的一个修改时间我们要记录下来你看是不是四个表里边都增加了一个字段对吧增加这个字段是干嘛呢你先不用管你先不用管一会儿我们用到的时候自然就会给大家讲所以说呢你需要拷贝这个东西拷贝这个
[06:00] 几条搜索语句你放到这个谁搜索项里边这样一执行就完事了我这就不再给大家执行了因为我这个提前已经执行过就是每个表里边增加了一个字段标题清明这是一个准备工作这个准备工作做完之后我们接下来就看看这个谁mycircle-es.config这个配偶念我们刚才说了它是不是非常重要对不对我们的logs-主要就是根据这个配偶念来进行数据采集和数据同步
[06:29] 当然这个配偶链里边的代码有点多我们看一看这个配偶链呢其实整体分成两大块有个学生老师我怎么看出来这不止两大块呢来咱一起看一看啊你看哪两大块你看首先这是一个什么呀input是不是一直到哪结束啊到这到这结束这是第一大块然后接下来第二大块叫output一直到最后哎你看是两大块吗
[06:59] 然后你再想想哎他一个叫input一个叫output哎你再看这个图你能想到这个input output分别是配置啥的吗input output能猜出来吧对input就是配置数据库这一块的数据input其实就是告诉logstash你要从哪采取数据嘛对不对那么output就是针对哪一块进行配置的对yes这边哎output指的就是logstash要把采取的数据写
[07:29] 写到什么地方或者输出到什么地方是不是所以你看这个还是挺清晰的啊两大块配置啊我们先看第一大块配置input里input里边我们说了是跟数据库相关的一些配置这些代码有些你基本上是能看懂看不懂的我这里边也有主示啊你看看吧这我不用解释吧是不是数据库连接信息哎你要告诉他你要连接哪个服务器上的哪个名字的什么呀数据库对不对然后呢这是账号和什么呀密码
[07:59] 你要连接数据库你肯定得告诉他账号密码没有账号密码他怎么可能连接得上然后接下来这是啥这是MySQL的那个GDBC驱动包嘛那看到这个大家也能猜法logger-底层也是通过GDBC干什么呀对连接数据库然后读取数据的所以你在你的电脑上你要找一个这个驱动包你放到任何路径都行但是这个路径你别写错了在这你可不要照着我的抄这个路径咱们可不一定都一样
[08:29] 这驱动类不再说了这是分页的信息不用管它然后下边是一个时区设置这个至关重要时区设置一定得设置你不设置的话它就是国外的那个格林尼日时间它跟咱们这个咱们这儿的采用的这个时区是有差别的时间上是不一样的所以你这儿一定要设置这个时区然后呢这个地方是用来设置这个执行的搜狗语句的这个搜狗语句是干嘛的大家能想到吗
[09:02] 你看这是一个搜索链搜索链你我一会儿会打开让你看但我现在告诉你这个搜索链里边其实就是一条搜索语句而且是查询语句你觉得他是干嘛他是干嘛大家想一下你看我们这是不是只是告诉他你要从哪个数据库里边采取数据但是只告诉这个信息够吗不够啊数据是不是在具体某个表里边那你想想这个地方应该是我刚才你说的是一条查询语句你觉得那个查询语句是干嘛
[09:32] 对这个查询语句就是用来告诉logstash你要从哪个什么呀表里边你要从哪个表里边查什么样的数据查什么样的数据只有这样的数据我们才让logstash给采集出来了是不是这里边的数据我们一会儿搜索语句我们一会儿打开看然后这大家注意看这是一个表达式的一个写法这个什么意思我告诉你每隔10秒执行一次
[10:05] 也就是说呢我们前面说过这个log slash是不是自动化的一个工作我们不用管而且它会设置什么样这个工作的这个间隔你看我这就是每隔10秒它这个表还是这样的你看它是不是中间用空格拆分这个几部分对不对第一部分这是第一部分是用来设置秒的这是分这是小时这是什么呀日月年对不对那我们这呢就是为了便于大家观察效果
[10:33] 我是每隔10秒钟执行一次但在切当时一看的时候不一定是每隔10秒这个这个你要看距离情况然后呢下面这两个地方是用来设置这个要不要记录这个logstash最后一次运行的时间我们说了它每隔10秒执行一次嘛那它执行的那个时间就最后一次执行的这个时间我们要不要记录数据表要记录而且你要设置这个时间要记录到哪个地方我们是记录到
[11:02] 这样一个文件当中这个文件没有困难名啊但是他也是一个文件记录到这里边为什么要记录这个时间呢哎这个时候大家注意这个时间跟我们这里边的搜寇语句是密切相关来咱接下来就要看这个搜寇语句了啊这个搜寇文件呢我在客栈里边提供的有那么你将来用的时候可以把它拷贝到硬盘的任何地方但是这个路径别写错了啊那这个搜寇语句呢咱就打开看一看吧这俩其实一样你打开
[11:33] 一个我们看看你瞅吧是不是一条长语语句slack一堆字段你可以这样可以当成就是相当于slack星吧然后是不是从我们的标题信息表里边进行查了然后但是带了一个条件带了什么条件呢只是你要注意了啊我们这是不是加了一个字段刚才叫modify data有印象吗我们刚才在在这个地方告诉大家一个准备工作是modify datamodify data是干啥的来我给大家说一说再强调一下
[12:07] 你看我们现在这个表里边是不是有很多标底数据对吧我们在这是不是加了一个字段叫modify data这个字段的值是这样子这个表里边的任何一行数据只要发生变化它的值这个值也会发生变化而且这个值就是当时你修改这个这条数据的时候那个时间当前的那个时间它会记录到这我再次给大家说一下啊比如说举个例子比如说呢这个这个是什么呀这个是不是那个标底的应该是
[12:37] 借款的那个金额吧是不是我们看一下啊应该是那个借款金额你比如说举个例子吧比如说这个字段值我改了一下我进行了修改那么当时修改的时候那个日期就会记录到这个里这个字段里如果你将来又改了别的字段比如这个字段我改改的时候改的时候当前那个日期又会记录到这那么也就是说这个字段就是数据修改的那个日期我们会记录到这然后呢你看看啊它有什么用呢你看
[13:09] 他要大于等于哎这是个啥玩意儿呢对不对这不是在搜狗鱼当中的东西这你可以认为这是一个站位服务这个站位服务是干嘛的呢既然他是站位服务他将来一定得有值这个值从哪来呢对不对这时候你要注意了这时候要注意一定要注意了啊这个值是从这来大家看这那个地方的值其实就是我们的logs在是最后一次运行的这个时间我们刚才说这个时间是不是记录到这里边对不对
[13:41] 记录到这个文件里边而这个站位符它的值就是从这个文件里边来获取到了那个谁啊对最后一次运行时间他把这个时间拿到手然后放到这那也就是说呢我们的modify data其实是跟谁做一次比较跟logger-最后一次运行的那个时间做比较为什么要这么比一会儿再说你先大概知道啊他们之间这个这个有什么关系这个代码都是什么意思先搞明白
[14:12] 具体它能起到什么作用一会儿再说这是咱们把这个配置给大家说了然后呢下面你看是不是还有几块还有三块加起来一共几块对 input 里边一共有四块配置为啥有四块而且你会发现这些配置长的基本上是什么一样的为啥会有四块配置呢而且长的一样呢这时候大家注意了我们的标底信息这块是不是进行了分库分辨分成了几个库啊两个库然后一共会产生几个表啊标底信息你看这一个两个
[14:41] 三个四个现在明白咋回事吗四张表我们要从四张表里边采取数据是不是对你你你不能这个少掉一张表那那数据采集这个就不完整了是不是所以我们有四张表因此你看我这配了几个几块GDPC4块里边的代码几乎是一样的不一样的地方给大家强调一下这地方自然是不一样的数据库你看这就变成几来一是不是然后还有哪个地方不一样还有这不一样
[15:12] 这个scroll脚本不一样啊有的是执行0有的是执行什么呀10和1表是啥你注意了它是跟这两张表对应的你看咱有个表叫project0有的表叫project什么呀1嘛所以我提供了两个scroll文件这个1的就是查询那个project1那个表的数据的0就是查询那个project0那个表里的数据说这个这个你要区分开啊写到时候不要错其他的配置都是一样其他配置全是一样的啊
[15:42] 所以说这是我先把input这一块的配置给大家介绍一下

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何使用 Logstash 从 MySQL 数据库同步数据到 Elasticsearch，并配置相应的模板文件和连接配置。

2) 按时间顺序列出每张画面的要点：
画面 1: 展示了课程文档中“4.4.2 使用Logstash”章节，图示说明 Logstash 从 MySQL 数据库读取数据并写入 Elasticsearch 索引库，需要两个配置文件：mysql-es.conf 和模板文件。
画面 2: 展示了“4.4.2.1 创建模板文件”部分，显示了模板文件内容，包含字段 "isAssignment"、"amount"、"period" 的类型定义。
画面 3: 展示了“4.4.2.1 创建模板文件”部分，显示了模板文件内容，包含字段 "repaymentway"、"consumerId"、"userName"、"description"、"annualRate" 的类型定义。
画面 4: 展示了“4.4.2.2 配置mysql-es.conf”部分，说明需要执行 SQL 语句在目标表中增加字段，并提到在 Logstash 的 config 目录下创建 mysql-es.conf 配置文件。
画面 5: 展示了 mysql-es.conf 配置文件的 input 部分，包含 jdbc 连接字符串、用户名、密码、驱动库、分页设置、时区等配置。
画面 6: 展示了 mysql-es.conf 配置文件的 output 部分，配置了 Elasticsearch 的 hosts、index、template 等信息。
画面 7: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。
画面 8: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。
画面 9: 展示了 IntelliJ IDEA 中的项目结构，项目名为 "wanxing2p_apollo"。
画面 10: 展示了 MySQL Workbench 中的 "p2p_transaction_0" 表数据，包含字段如 PERIOD、ANNUAL_RATE、BORROWER_ANNUAL_RATE、REPAYMENT_WAY、AMOUNT、PROJECT_STATUS、CREATE_DATE、IS_ASSIGNMENT。
画面 11: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。
画面 12: 展示了 MySQL Workbench 中的 "p2p_transaction_1" 表数据，包含字段如 BORROWER_ANNUAL_RATE、COMMISSION_ANNUAL_RATE、REPAYMENT_WAY、AMOUNT、PROJECT_STATUS、CREATE_DATE、IS_ASSIGNMENT。
画面 13: 展示了 mysql-es.conf 配置文件的 output 部分，配置了 Elasticsearch 的 hosts、index、template 等信息。
画面 14: 展示了 mysql-es.conf 配置文件的 input 部分，与画面 5 内容相同。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面 1:
```
4.4.2 使用Logstash
Logstash的工作是从MySQL中读取数据，然后向ES中写入数据从而创建索引。因此它需要知道数据库相关的表和ES相关的配置文件：
1.mysql-es.conf：配置从哪个数据库和表读取数据，配置把读取到的数据写入到哪个ES索引库中
2.模板文件：索引库的映射配置
```

画面 2:
```
4.4.2.1 创建模板文件
在logstash的config目录中创建wanxing2p_project_template.json作为模板文件，配置索引库映射，内容如下：
{
  "mappings":{
    "properties":{
      "isAssignment":{
        "type":"keyword"
      },
      "amount":{
        "type":"double"
      },
      "period":{
        "type":"integer"
      }
    }
  }
}
```

画面 3:
```
4.4.2.1 创建模板文件
在logstash的config目录中创建wanxing2p_project_template.json作为模板文件，配置索引库映射，内容如下：
{
  "mappings":{
    "properties":{
      "isAssignment":{
        "type":"keyword"
      },
      "amount":{
        "type":"double"
      },
      "period":{
        "type":"integer"
      }
    }
  }
}
```

画面 4:
```
4.4.2.2 配置mysql-es.conf
1. 我们需要执行如下SQL语句，在目标的表中增加一个字段：
ALTER TABLE p2p_transaction_0.`project_0` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
ALTER TABLE p2p_transaction_0.`project_1` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
ALTER TABLE p2p_transaction_1.`project_0` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
ALTER TABLE p2p_transaction_1.`project_1` ADD COLUMN MODIFY_DATE datetime(0)
NULL DEFAULT NULL COMMENT '修改时间' AFTER CREATE_DATE;
2. 在Logstash的config目录下创建mysql-es.conf配置文件，Logstash会根据该配置文件从MySQL中读取数据并同步到ES中。
```

画面 5:
```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://localhost:3306/p2p_transaction_0?"
    useUnicode=true&characterEncoding=utf-8&useSSL=false
    jdbc_user => "root"
    jdbc_password => "123"
    jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_paging_enabled => true
    jdbc_page_size => "50000"
    jdbc_default_timezone => "Asia/Shanghai"
    #要执行的sql
    statement_filepath => "e:/wanxing2p-project_0.sql"
    #每隔10秒执行一次
    schedule => "*/10 * * * *"
    #是否记录最后一次的运行时间
    record_last_run => true
    #记录最后一次运行时间的位置
    last_run_metadata_path => "./logstash_metadata"
  }
}
```

画面 6:
```
output {
  Elasticsearch {
    #es服务地址
    hosts => "localhost:9200"
    #索引库名称
    index => "wanxing2p-project"
    #关联表主键作为文档ID
    document_id => "%{id}"
    #模板文件地址
    template => "C:/Users/apple/Desktop/logstash-7.3.1/config/wanxing2p_project_template.json"
    #模板文件名
    template_name => "wanxing2p_project"
    #覆盖模板
    template_overwrite => true
  }
}
```

画面 7:
```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://localhost:3306/p2p_transaction_0?"
    useUnicode=true&characterEncoding=utf-8&useSSL=false
    jdbc_user => "root"
    jdbc_password => "123"
    jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_paging_enabled => true
    jdbc_page_size => "50000"
    jdbc_default_timezone => "Asia/Shanghai"
    #要执行的sql
    statement_filepath => "e:/wanxing2p-project_0.sql"
    #每隔10秒执行一次
    schedule => "*/10 * * * *"
    #是否记录最后一次的运行时间
    record_last_run => true
    #记录最后一次运行时间的位置
    last_run_metadata_path => "./logstash_metadata"
  }
}
```

画面 8:
```
input {
  jdbc {
    jdbc_connection_string => "jdbc:mysql://localhost:3306/p2p_transaction_0?"
    useUnicode=true&characterEncoding=utf-8&useSSL=false
    jdbc_user => "root"
    jdbc_password => "123"
    jdbc_driver_library => "e:/mysql-connector-java-8.0.11.jar"
    jdbc_driver_class => "com.mysql.cj.jdbc.Driver"
    jdbc_paging_enabled => true
    jdbc_page_size => "50000"
    jdbc_default_timezone => "Asia/Shanghai"
    #要执行的sql
    statement_filepath => "e:/wanxing2p-project_0.sql"
    #每隔10秒执行一次
    schedule => "*/10 * * * *"
    #是否记录最后一次的运行时间
    record_last_run => true
    #记录最后一次运行时间的位置
    last_run_metadata_path => "./logstash_metadata"
  }
}
```

画面 9:
```
Project: wanxing2p_apollo
├── idea
├── logs
├── wanxing2p-account-Service
├── wanxing2p-apl
├── wanxing2p-common
├── wanxing2p-consumer-Service
├── wanxing2p-depository-agent-Service
├── wanxing2p-discover-server
├── wanxing2p-g

