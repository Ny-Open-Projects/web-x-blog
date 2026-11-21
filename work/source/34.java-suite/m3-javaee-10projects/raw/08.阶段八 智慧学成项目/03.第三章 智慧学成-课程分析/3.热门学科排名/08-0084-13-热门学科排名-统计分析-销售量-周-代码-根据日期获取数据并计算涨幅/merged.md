# 13-热门学科排名-统计分析-销售量-周-代码-根据日期获取数据并计算涨幅

- 阶段：08.阶段八 智慧学成项目
- 章节：03.第三章 智慧学成-课程分析/3.热门学科排名
- 源文件：08.阶段八 智慧学成项目\03.第三章 智慧学成-课程分析\3.热门学科排名\13-热门学科排名-统计分析-销售量-周-代码-根据日期获取数据并计算涨幅_【海量资源尽在 666java.com】.mp4
- 时长 14分32秒（音频 873s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好,咱们继续,接下来呢就根据咱们的日期,然后获取它本周的数据以及上周的数据,获取完数据之后呢,直接计算奖服,这里呢获取数据和计算奖服,咱们使用Spark Circle,这里呢Circle咱们还使用HUE编写,因为上面呢是有提示的,在上面测试完成之后呢,咱们再回到咱们的开发工具进行一个编写,咱们来切到HUE。
[00:29] 这里再强调一下咱们呢课程销量的数据就是销售量的数据呢是基于课程购买量的一个中间数据DWM层的数据进行一个数据清洗的进行一个数据统计的咱们呢直接获取这张表的数据就行这张表就是咱们课程购买量的中间表的数据咱们呢首先肯定是要先把它给查出来slot 行from咱们的是
[00:58] 这个没有库名咱们需要把库名给加上因为在咱们的Spark里边执行的时候如果没有库名它会出现一个情况就是说它找的是默认的库默认库里边是没有这个表的它就会报错这里呢数据查过来之后这是查询的所有数据咱们是不是要根据日期进行过滤咱们这里边的日期是谁本周的日期就是这个这个日期是相对的咱们是相对于11月11号
[01:27] 这个日期它这个本周日期的区间是这样的咱们是不是要根据这个区间进行一个取值但是这个地方和时间有关的数据是不是只有分区年月日咱们这里边条件是不是还要根据咱们的分区年月日进行一个连接之后进行一个条件的过滤这里边连接函数还是的concatws连接方式还是使用横杠的方式这样它就得到了
[01:58] 咱们yyymdd这种的日期格式得到这种日期格式之后咱们就可以直接使用btn按的使用btn按的进行这个日期的一个区间的一个查询这里呢有了它之后接下来按的这是这个区间区间有了之后咱们要计算的是啥呀咱们要计算的是课程的销售量课程的销售量的话咱们来看它这个
[02:32] 他这个数据这里呢他有一个查看的一个数据的一个窗口咱们呢直接就把它给弹出来课程销售量的数据这里你可以看得到他是不是已经通过轻度聚合然后得到的是一个就是当前那个课程他的销量是多少那这样的话咱们就不能使用counter这个方法了咱们就需要使用sum然后呢根据这个sum就进行一个求和
[03:00] 根据三部求核的时候它还有一个问题咱们这里是谁啊咱们这里是不是热门学科排名啊热门学科排名是不是要根据学科ID进行一个聚合啊咱们先把聚合给写出来这里你可以看到它是有学科的这个分类ID的这里通过学科分类ID进行一个聚合聚合完成之后呢它把学科ID给响应回来回来之后呢咱们是不是要对谁进行一个
[03:28] 求和是不是要根据咱们的销售量进行一个求和就是把当前学科里边所有的销售量全部给拿过来拿过来之后咱们就是每个学科的销售量就是在这个日期区间内的销售量就有了这是咱们本周的咱们来测试一下看结果咱们这个程序运行的就是这个circle运行的咱们把上周的也给编写一下
[04:00] 这里呢上读的区间咱们是不是只用改一下时间就行了写法都是一样的这里呢已经出来了这个分类下面是有这么多的一个销售量这么这个分类下面是有这么多的销售量销售量出来了之后咱们上周的销售量出来之后说明咱们这个src没有问题接下来呢是不是根据这个日期咱们修改一下日期来获取上上读的一个销售量啊由于刚才咱们这个src已经测试过src是没有问题的
[04:35] 上周的数据没有问题咱们只改了日期上上周的日期肯定也是没有问题两个周的日期获取完成之后接下来咱们是不是要计算涨幅了计算涨幅这个时候呢先把这个注释给删掉方便呢咱们就是代码结构的一个查看根据这两个数据计算涨幅的时候就需要使用到一个子磁团咱们呢先把它给
[05:03] 这两个表呢分别映射成什么映射成一个临时表映射成临时表之后它内部就算成一个自查群这个自查群呢再把这两个自查群使用left join连接起来之后呢就可以拿到咱们的销售量的数据这个时候就可以根据销售量的数据呢进行一个计算咱们呢这个地方还是select from这个时候from就有意思了咱们是不是要把它给变成一个
[05:34] 然后映射成一个临时表,这个时候就要加一个括号这个是中文括号,换成英文的,加个括号,这个的话咱们上周的话就叫A表吧,SA这是咱们上周的数据有了,然后呢还需要使用的谁啊,使用上上周的数据,这里呢咱们使用Live的教养教养的是谁啊,教养的是这张表,这张表也把它给扩起来,让它变成一个子插旋然后呢这个地方SB,SB表
[06:06] A表和B表有了是不是还要有他们的一个条件咱们的条件是啥是不是它课程认为学科分类的一个ID因为只有这个ID是公共的咱们这个地方条件就是on的条件就是A的分类ID等于B的分类ID课程分类ID这个分类ID有了之后接下来咱们是不是就是结果的一个输出以及
[06:35] 结果输出条件的一个编写以及咱们涨幅的一个计算呢这个地方把它给稍微推爆一下因为它是一个子插群方便咱们观看这个时候呢首先咱们课程分类ID肯定是要输的因为两个表都有你输出哪个表的都行然后呢写个别名还让它叫课程分类ID这是咱们第一个参数第二个呢是咱们最终输出的时候销售量是不是也要输出呀这个时候销售量咱们
[07:05] 要的是哪张表的呀肯定是要的是本周的呀这个时候你只能用输出A表的A表的销售量咱们呢这个地方的别名是S这个地方没有起别名没有起别名的话需要给它起一个别名不起别名的话它后边输出的时候它是找不着别名找不着值的就叫Solar Number这个呢相同也起一个别名这个呢别名使用一下
[07:36] 咱们输出的这个值就有了这个地方有了之后呢咱们接下来是不是要根据咱们的这个条件计算啥了计算涨幅了计算涨幅呢因为咱们是使用同比的方式同比的方式呢就是本周的减去上一周的再除以上一周的就得到的一个涨幅咱们来写一下本周的数据就是这个减去上周的sare number
[08:09] 这个地方没有少了一个逗号所以说它在报错这个地方还需要将括号把它给扩起来然后还要除余上读的这是咱们图比的一个计算方式这个时候再给它起一个别名咱们后边方便咱们使用就叫下方线直接使用横杠是不行的P12CEN7就叫这个涨幅
[08:42] 涨幅有了之后咱们就可以测试一下咱们这个代码写的时候OK咱们来跑一下这个呢它执行需要一定的时间咱们稍微等待一下还在运算中这个地方呢其实还有一个不完美这个不完美程序跑着给大家解释一下这个呢咱们本周和上周它肯定
[09:15] 不管你的这个数据是从哪天开始的,它总有一种情况是上周是没有数据的,上周没有数据的情况下,这个地方它就会出现一个控制人异常,这个呢,出现控制人异常,咱们既然出现了,肯定是要处理它的,这个地方呢,好,这里结果已经出来了,涨幅也计算出来了,有这种异常,就是可以遇到的异常,咱们呢,就把这个异常给解决了,这里呢,咱们使用if not这个函数,使用这个函数,
[09:48] 这个if-now在咱们Spark里边在咱们Spark里边有但是在咱们HOE里边是没有的这里先把它给写好写好之后咱们后边咱们直接用就行了这里if-now它接下来如果是now的话就是让它是1.01.0就是百分之百的增幅1.0是百分之百的增幅的情况下咱们这个就算写完成了
[10:19] 写完成之后咱们就把可以把它给放到Spark里边进行一个执行放到Spark里边执行看它是否是正常的这里呢咱们切到开发工具Spark circle这里呢就是咱们的代码由于是多行的这个地方要使用这个三个引号然后是多行的一个代码格式这个呢咱们直接把这个结果呢给输出出来看它的这个if now是否是好使的
[10:53] 走起这个的话这会儿因为这些变量还是硬编码等会儿呢咱们需要将那个变量变成咱们就是根据计算然后动态获取的一个日期这里程序在跑着咱们呢就来做一个计算就来一个就是取消硬编码的一个编写方式上周的日期这个地方呢上周日期它是不是还是一个字符串呢这结果出来了咱们接着改这个是一个字符串它的字符串方式
[11:29] 往上拉看日志还有没好日志这个地方还有它是用冒号进行分隔的其实呢这个地方咱们还可以接着进行一个分隔就是直接得到它这个什么呀上周和上周的开始和结束的一个日期这里呢也是得到上周开始和结束的日期这两个输出就先删掉咱们用的时候呢就可以这是上周的位置就可以呢使用咱们的变量进行一个直接的一个取值这是谁呀
[11:58] 它是上周这个地方那就是开始就是0这个就可以直接粘了它是结束结束呢这个地方就是1上上周是last这个地方呢咱们只用把它给改成last就行这是上周上上周开始接下来呢是上上周的结束这个咱们变成动态的之后呢咱们再运行一下代码走起看这个结果是否是正常的
[12:35] 这个想计算这个if now是否成功咱们呢需要将日期在咱们这个这个数据里边找到它一个最大的一个日期就是说不是最大的一个日期日期最早的一个日期找到最早的日期之后呢咱们就可以根据这个日期然后验证咱们的if now咱们呢来直接查看它的一个数据这个时候其实直接查看分区就行了因为分区的数据它是最大的数据和最小的数据是方便你查看的这里呢
[13:05] 最小的是2018年这个可能它时间比较久远了咱们呢就以这个为例它是9月22咱们呢往后再推个三天叫9月25使用9月25进行一个验证然后咱们来验证这个衣服闹是否是如果这个地方出现100%就是1.0就说明咱们这个衣服闹就OK了这是09这是25再测试一下只要出现1.0就说明
[13:40] 前面日期没有数据的情况下咱们呢程序通过这个逻辑判断就可以把它由于前面没有数据这边是新数据那涨幅肯定是100%这个地方就是一个一分掉的一个判断咱们来验证一下等程序计算一下这里呢还在计算中这里你可以看到前面数据是都是没有的这里咱们涨幅都是1.0通过这个计算呢咱们通过这个测试呢咱们
[14:09] 这个代码就是见状性还是可以的咱们对这个数据获取以及数据计算涨幅这一块呢已经写完咱们后边的还需要进行维度的关联以及保存结果交给下一个视频本视频呢主要内容就是获取数据并计算涨幅好视频呢就到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲如何通过Hive SQL和Spark SQL分别实现课程销售数据的周度销售金额及同比变化率计算，并对比两种技术方案的执行过程与结果。

2) 按时间顺序列出每张画面的要点：

画面1：
- 界面：Hue - Editor，连接到Hive。
- 状态：未输入任何SQL语句，提示“你没有保存任何查询”。
- 数据库列表：左侧显示Hive数据库，包括data_agency, data_course, data_dimen, data_platform, data_subject, default。

画面2：
- 界面：Hue - Editor，连接到Hive。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行结果：查询成功，返回14行数据，包含course_category_dim_id, sale_num, sale_percent。

画面3：
- 界面：Hue - Editor，连接到Hive。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行结果：查询成功，返回14行数据，包含course_category_dim_id, sale_num, sale_percent。

画面4：
- 界面：Hue - Editor，连接到Hive。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行结果：查询成功，返回14行数据，包含course_category_dim_id, sale_num, sale_percent。

画面5：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面6：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面7：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面8：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-11-04' and '2019-11-10'
    GROUP BY course_category_dim_id
  ) as a
  LEFT JOIN (
    SELECT course_category_dim_id, sum(salevolume) sale_num
    FROM data_course.course_buy_dim
    WHERE concat_ws('','years',months,days) BETWEEN '2019-10-28' and '2019-11-03'
    GROUP BY course_category_dim_id
  ) as b
  ON a.course_category_dim_id = b.course_category_dim_id
- 执行日志：显示Spark任务启动、初始化BlockManager、注册StoreCoordinator等信息。

画面9：
- 界面：IntelliJ IDEA，打开项目xc-analysis。
- 文件：SubjectSalesVolumeByWeek.scala。
- SQL语句：
  SELECT a.course_category_dim_id, course_category_dim_id, a.sale_num sale_num, (nullif((a.sale_num-b.sale_num)/b.sale_num, 1.0) sale_percent
  FROM (
    SELECT course_category

