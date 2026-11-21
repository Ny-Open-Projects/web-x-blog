# 20-Hive的基本操作-内置函数

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day05-Hive
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day05-Hive\20-Hive的基本操作-内置函数【海量资源尽在 ubkz.com】.mp4
- 时长 8分48秒（音频 529s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 接下来我们来学习Hive中的函数Hive中的函数有两种一种是内置函数一种叫自定义函数这个内置函数是Hive自带的而自定义函数是需要我们自己定义的我们来先学内置函数这个内置函数Hive中特别多这里有个文档你可以去查看还有它提供了一些命令我们可以查看相关的函数第一个叫输入方生色
[00:30] 它可以查看Hive中所有的内置函数来我们来演示一下好在这里呢我设个命令叫show functions走你看这里边列出来全是它的内置函数我们可以从上到下呢我们看一下好上面这些符号呢运算符呢也认为是它的内置函数比如说这个abs是求什么呢是求绝对值对吧还有呢这个地方avg是不是一个聚合函数求平均值
[01:00] 还有sill向上曲整还有什么cosine还有呢一些flower向下曲整等等OK这是一些内置函数那如果说你想看每一个函数怎么用呢它还有一个meaning我们回到讲义这里有一个叫dsc function upper这个地方呢是查看upper这个函数呢它的一个用法我们来看一下好dsc
[01:30] function upperupvr注意upper是一个函数的名字我们来看一下好这个地方呢它说呢这个upper啊它是return一个字幕串所有字符呢变成一个大写OK这样子那还有一个命令这个命令叫dse function extended upper加个extended呢表示啊我们查看的是它一些详细的一个信息来我们来用一下在这里呢我们来加一个
[01:59] extended好你看这个时候呢它的输出的信息呢更丰富一点它在这里呢还有一个example它呢给你列出来这个函数怎么去用那接下来呢我们就用一下你看我要去用这个函数呢我们先用个selectselect的意思就是说把函数的结果给它输出我们upper然后呢这里边呢需要一个字幕串比如说我来一个hello走
[02:29] 你看这个位置它就把你这个小写的hello是变成大写的hello了当然了还有其他的一些函数你比如说呢我们可以求这个求这个abs求绝对值我们写个比如说我们写个-5-5走它的绝对值是5等等这些呢都比较简单那在这里呢我还给大家列了一些我们后期呢会用的一些内置函数来咱们一起来看一下第一个呢
[02:58] 叫字部串连接函数叫concat它呢可以将多个字部串合成一个我们来用一下在这里呢我们把这个呢写一下比如说select叫什么concat里边呢你可以跟多个字部串比如说我写个hello逗号word然后再逗号比如说呢我们写个这个Hive回车好你看
[03:27] 它是将这个多个组串进行了合并这个有时候呢在我们写这个Hive一些指令的时候呢有时候会用到OK这是这个组串合并来再回到讲义还有一个呢叫concate ws这个什么意思呢这个是在合并的时候啊我们可以指定一个分隔幅你看这里边呢这个select concate ws表示第一个参数表示我的分隔幅是逗号那也就是说
[03:56] 我在将这些字幕串合并的时候我可以给它们指定一个逗号分割符来我们来试一下好在这里呢我们在concat后面加个ws然后呢第一个参数呢我们写个逗号好走一下回撤哎你看在合并的时候那么它们是不是中间有逗号分割呀ok这是这个ws的一个特点那接下来呢我们再看其他的还有一个叫
[04:26] cast这个叫类型转换这个函数也很常用这个cast怎么用呢它可以将一个类型转成另外一个类型我们来看这个cast1.5那么我可以把它变成整形一变成整形呢就相当于把小数点给去掉了我们来试一下好在这里呢我们来select然后cast这地方我写个数字1.5as把它转成什么类型呢int类型走你看
[04:56] 1.5变成int类型是不是变成1了把小数点去掉了这个有时候做类型转换它是有意义的这叫cast好也可以认为是一个类型的强转好再看下一个还有一个叫getJsonObject这个我们可以使用这个函数来去解析一个Json串你看这里一个Json串我们可以解析这个Json串后面这个表示我要获取这个Json串中的某个值你看
[05:25] $Float.Name就相当于根据这个Name这个键来获取Jack这个值来我们把这句话呢直接拿过来好站在这里好站在这里之后呢你看前边是一个Jason串那这个函数就能识别后面呢是从这个Jason对象中呢这是一个Jason对象这是Jason对象里边的一个键OK根据这个名字根据这个Name来获取对应的Value来我们来回来走好你看
[05:56] 这个内母对应的值是不是jack那假如说我要获取这个ag的值是20呢那大家说怎么做是不是只需要把这个$v内母变成什么$vag好就可以了那这里面就获取20了这个也很常用OK这是这个内容函数那接下来回到讲义我们再看下一个还有一个叫url解析函数这个函数也很常用这个函数叫pasul这个pasul呢
[06:26] 它是将我们URL进行解析然后根据后面这个参数来获取这个URL中不同的一些值什么意思呢我们来看把这句话直接拿过来来我们来看一下好站在这里这里的话我想干嘛呢我想从这个URL这个地址里边获取一个主机主机信息这个主机信息是什么呢我们来回车走你看到没有
[06:54] 他拿到的是一个facebook.com也就是说他从这个URL这个地址里边呢把这个facebook.com提取出来了这个不就是那个网址吗这个域名OK那我不仅可以提取这个host也就是我们的网域名我还提取其他部分比如说呢我还在这里边呢再写个叫pass我们来看一下好我写了一个pass之后呢他把这个域名后面的这个也就是把这个主机
[07:24] 这个网址后面这个部分是不是给我取出来了OK这是一个请求的路径对吧把这个路径给我取出来了那还有呢比如说呢我想获取后面这些参数怎么做呢我们还有一个参数这个参数叫queryquery我们看一下走一下你看这个时候它把后面写的参数这些箭指对给我取出来k1等于v1k2等于v2那假如说我想获取这个箭指对的某一个
[07:55] 值怎么办呢比如说我想获取V1那这个怎么写呢我们这样写我们在后面再加个逗号你可以在这里呢写一个写一个K1就可以了走你看前面要写query后面写上你要取的这个键的名字K1我拿的是V1那如果我要想去获取V2呢那这个地方呢我们来写K2是不是就可以了好这是这么一个叫pass ur
[08:24] 来进行UR的一个解析这个在网络日志一些数据的分析中呢非常常用好那么这个呢就是我给大家介绍的几个内置函数当然了它还有其他的一些内置函数大家呢可以下去再去自己呢再去看一下别的一些东西好那么关于呢Hive的内置函数呢我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示Hive内置函数的查看、描述和实际调用方法。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面1：展示Hive内置函数章节的PPT内容，列出查看系统函数、显示函数用法、详细描述函数和调用函数四个步骤，并给出对应命令示例。
画面2：与画面1内容相同，为同一PPT页面的重复展示。
画面3：在SecureCRT终端中执行`Hive desc function upper;`命令，输出函数说明，随后执行`Hive desc function extended upper;`命令，输出更详细的函数信息。
画面4：在SecureCRT终端中执行`SELECT upper('Facebook') FROM src LIMIT 1;`查询语句，输出结果为'FACEBOOK'，并显示函数类和类型信息。
画面5：展示PPT页面，重点在“4. 常用内置函数”部分，列出concat、concat_ws、cast等函数的示例代码。
画面6：在SecureCRT终端中执行`select upper('hello');`、`select abs(-5);`和`select concat('hello','world','Hive');`命令，分别输出结果“HELLO”、“5”和“helloworldhive”。
画面7：在SecureCRT终端中执行`select concat_ws(',', 'hello', 'world', 'Hive');`命令，输出结果“hello,world,Hive”。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面1：
https://cwiki.apache.org/confluence/display/Hive/LanguageManualUDF
1. 查看系统自带的函数
Hive show functions;
2. 显示自带的函数的用法
Hive desc function upper;
3. 详细显示自带的函数的用法
Hive desc function extended upper;
4. 常用内置函数
#字符串连接函数： concat
select concat('abc','def','gh');
#字符串拼接函数： concat_ws
select concat_ws(',', 'abc', 'def', 'gh');
#类型转换函数： cast
select cast(1.5 as int);

画面3：
xpath
xpath_boolean
xpath_double
xpath_float
xpath_int
xpath_long
xpath_number
xpath_short
xpath_string
year
Time taken: 0.028 seconds, Fetched: 289 row(s)
Hive> desc function upper;
OK
upper(str) - Returns str with all characters changed to uppercase
Time taken: 0.055 seconds, Fetched: 1 row(s)
Hive>

画面4：
upper(str) - Returns str with all characters changed to uppercase
Synonyms: ucase
Example:
> SELECT upper('Facebook') FROM src LIMIT 1;
'FACEBOOK'
Function class:org.apache.Hadoop.Hive.q1.udf.generic.GenericUDFUpper
Function type:BUILTIN
Time taken: 0.024 seconds, Fetched: 7 row(s)
Hive>

画面6：
Hive> select upper('hello');
HELLO
Time taken: 0.158 seconds, Fetched: 1 row(s)
Hive> select abs(-5);
5
Time taken: 0.157 seconds, Fetched: 1 row(s)
Hive> select concat('hello','world','Hive');
helloworldhive
Time taken: 0.153 seconds, Fetched: 1 row(s)

画面7：
Hive> select concat_ws(',', 'hello', 'world', 'Hive');
hello,world,Hive
Time taken: 0.153 seconds, Fetched: 1 row(s)

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面1和画面5：PPT标题为“3.1. 内置函数”，子标题“内容较多，见《Hive官方文档》”，并列出四个步骤：
1. 查看系统自带的函数
2. 显示自带的函数的用法
3. 详细显示自带的函数的用法
4. 常用内置函数
画面5中在“4. 常用内置函数”部分下方有“email”字样，但无明确结构指向。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

