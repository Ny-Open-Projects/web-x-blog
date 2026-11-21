# 08-SpringBoot配置-yaml数据格式

- 阶段：01.阶段一 微服务相关技术
- 章节：1.SpringBoot/1.SpringBoot 第一天
- 源文件：01.阶段一 微服务相关技术\1.SpringBoot\1.SpringBoot 第一天\08-SpringBoot配置-yaml数据格式_【海量资源尽在 ubkz.com】.mp4
- 时长 11分49秒（音频 710s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:01] 介绍完YAML的基本语法接下来我们来讲解YAML的数据格式在YAML文件中它可以允许有三种不同的数据格式第一种就是我们所最常用的对象就是见值对的这种集合的这种方式比如说在这个例子里边有一个personperson下边有一个namename的值是张三并且用这种缩进的关系表示了name
[00:30] 它是属于person的那么同样的我们也可以在person下面再定义比如说其他的属性age啊等等这些属性都是可以的那么这种箭直对的方式呢它也可以使用这种行内的写法比如说下边这个例子这样去写person 冒号然后呢空格写一对大括号箭直对里边又是箭直对name 冒号 空格 张三那么类似于这种类似于jason的这种写法但是要注意的是
[01:00] 在person和这个大括号之间这个地方有空格而name和张三这个值之间也是必须有空格的所以这个空格呢是很多同学容易忽略掉的但是这种行内写法它用的并没有这种缩进的写法用的这么多了解一下就可以了那么这种建制对的对象的方式我们map集合配置的时候也是这样去配置的待会我们可以来演示一下那么第二个呢就是竖组
[01:31] 数组在配置的时候它是以这种横杠和空格的方式来表示了这种数组的所属关系比如说addressaddress下边有两个值北京上海那么北京和上海组成了一个数组都是address这个数组下边的那么这个地方呢就使用横杠空格来表示那么同时呢数组也同样有行内的写法address 冒号空格中国号包裹起来
[01:59] 然后北京一个值上海一个值中间用逗号来做分割很类似Jason的这种写法那么最后一种叫做纯量纯量其实就是我们之前所理解的这种常量那么比如说我们写的什么20数字比如说true false这都是一些纯量那么我们介绍两个比较特殊的纯量单义和双义引起来的这种值那么我们有个例子message1
[02:28] Message2一个是单引引起来的一个是双引引起来的它们里边的内容都是一模一样的Hello, Word在Hello, Word中间呢有一个反斜杆N是一个转译字符那么这个转译字符表示了一个换行那么如果是单引号引起来的它会忽略这个转译字符也就是说Hello, Word中间这个反斜杆N会原样的被输出而如果是双引号的话它会识别这个转译字符
[02:56] 将来Hello World会分两行被输出那么当然这些值的输出我们肯定只能在获取这些数据值的时候才能演示这块我们只是先介绍一下那么介绍了这些数据格式之后接下来我们在代码里边来演示一下打开IDL打开IDL之后这个地方我们打开了这么一个Yammer的文件那么当然第一种这个呵呵
[03:25] 冒号ABC这个我们刚才写的写的呢我可以把它删掉没什么用我们可以在这里边写单个的属性比如说name冒号ABC吧单个的可以这样写那么同样呢我们也可以写这种对象的格式对象的格式那么对象呢比如说person冒号空格对吧这个地方呢其实不要加不加空格其实都无所谓因为person下面可能有一些其他的属性name冒号空格
[03:54] 比如张三然后呢再来ageage冒号20那么这个地方呢就表示了name和age属于person的他们一个值是张三一个值是20注意注意这个地方的空格一定要带有空格当然写一个空格和写三个空格没有什么任何的区别当然一般情况下我们都只写一个空格而这个person后边
[04:22] 没有对应的值这个地方可以不写空格好嘞要说明这个空格的问题我们必须来获取这个属性值现在我们又没有讲解怎么获取自定义的这些属性值那么这个地方Solver.part这个属性它是会被Tomcat插件自动识别的所以我们可以在这来演示比如说这个8082这个端口这块我们把这个空格给它删掉删掉之后你注意看
[04:50] idea这个编辑器还是比较强大的然后这个port这个高亮是不是就没见了颜色也没见了你看你加上空格注意加错了加这个地方你看这个高亮和蓝色是不是就变色了而你删除了这个空格之后它就不会变色了当然你加几个空格也是都OK的我们可以演示一下比如说现在我们把port给它干掉干掉之后我们重启一下服务properties里边没有
[05:19] 对应的Solver Port的配置YAML这个里边不识别那么就会识别这个YAML那么YAML里边配置的是8083那么启动的端口号就是8083了那么如果我把这个空格给它加上比如说我加好几个空格加上之后呢我们再来重启它就会识别这个YAML里边的8082这个配置你看识别了吧所以这个空格很重要
[05:47] 那么第一个对象我们就简单的说完了说完了之后呢接下来我们来说一下对象的行内的写法另外一种写法对象的行内写法行内写法呢我们person比如说叫做person2再叫person就不行了因为在同一个文件里边你不能配置两个键是一样的我们叫做person2冒号你注意看我这个冒号是不是就有点胖
[06:15] 对吧因为这个冒号呢其实是中文状态下的这个冒号我们要把它换成英文的冒号好换一下换一下之后呢你看这个冒号是不是就比较瘦一些然后加个空格大括号然后呢name冒号空格张三逗号age冒号空格20那么这是另外一种行内的写法OK那么对象说完了之后我们来说第二个数组
[06:45] 数组呢也比较简单address好,冒号下边呢就写横杠短的横杠空格北京注意这个横杠后边也需要加一个空格那么下来第二个呢我们再写一个上海吧上海OK那么就表示了address这个属性下边有两个值并且呢这两个值组成了一个数组第一个值呢是北京第二个值是上海
[07:13] 其实你可以看到Ardier对这个数组或者说对这个Yammer这个文件的支撑还是比较强大的你点到这个北京上面你可以看这个地方状态栏这一块你看这个addressitem1-2什么意思呢address是个数组一共有两个元素当前北京呢是第一个元素是第一个元素就是1-2那么上海呢就是2-2了对吧
[07:40] 那么接下来我们可以再来说一下这个数组的行内写法数组的行内写法同样呢address好注意不能叫同名叫2中国号然后呢北京逗号上海也是OK的那么最后呢我们来演示一下这个存量存量了解一下msg1好然后呢msg2
[08:10] 那么MSGE呢我们加个空格这个地方写单一号叫做Hello World中间呢加个-N吧那么这个地方呢我们就说了刚才说了说这个-N呢不会被识别这个转移字符会原样输出然后接下来我们加一个双一号双一号呢其实你现在看不出任何的区别因为待会我们来获取值之后才能看得出区别我们先把注释给它加上第一个呢会不会
[08:38] 识别这个转译字符会原样原样输出OK那么第二个呢双引号的话它会识别这个转译字符识别了之后呢Hello和What就会分两行来输出了OK那么这些基本的Yammer的这些数据格式这么三种对象啊
[09:07] 数组还有这种存量我们都介绍完了介绍完了之后我们再顺带讲一个小的知识点叫做参数引用参数引用什么意思呢比如说我们在这定义的一个name叫做李斯然后person下边也有个name这个name的值我想引用上面这个单独的这个name李斯的值我就可以用这种表达式的方式来引用上面这个k的值写一个dollar大括号把这个gen给它放这
[09:37] 那么这个将来获取Personal Name的值呢就会变成理似了就是参数引用演示一下比如说我们在这个地方配这个Name叫做ABC然后呢这个叫做张三我们把张三给他注释掉注释掉之后呢我们可以在这个地方写一个DollarDollarDollar大括号然后呢Name将来我一旦获取Personal Name的值它和这个Name的值就表示一样了叫做参数引用OK
[10:07] 那么介绍完至此我们就介绍完了所有的YAML的基本的一个语法我们来做一个简单的小节首先我们先介绍了YAML的配置文件就是Spring Boot里边配置文件的类型两种第一种就是Properties这个没有什么说的跟以前一模一样第二种就是YAMLYAML它有两种不同的后缀名一种是YML一种是YAML
[10:35] 这个地方一定要注意啊注意这个空格这个空格呢很多同学可能容易忽略掉那么接下来我们讲了一下YAML的一个特征它比较简洁并且呢它是以数据为中心的随后呢我们讲了它的基本的语法第一个呢大小显敏感第二个呢空格的问题数据值前面必须得有空格一个或多过空格都是可以的第三个呢使用空格来表示了层级关系
[11:04] 相同的缩进表示了同一级下来我们介绍了三种不同的数据格式对象的 数组的和存量的那么这个对象没有什么说的就是以这个缩进的关系或者说行列的写法来表示了一个对象的值然后数组我们使用这个横杠空格的方式来表示每个元素这个稍微会特殊一些OK最后我们简单的介绍了一下这个参数引用它的写法是这种表达式的方式
[11:34] 那么里边写一个KK呢就是你要引用的那个值的键OK那么至此呢我们Spring Boot配置文件里边这个压面我们就介绍完毕了

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲 Spring Boot 中 YAML 配置文件的语法、数据格式、参数引用及小结。

2) 按时间顺序列出每张画面的要点：
画面 1: PPT 页面，标题为“Spring Boot 配置”，子标题“YAML：数据格式”，内容包括对象（map）和数组（array）的 YAML 语法示例。
画面 2: IDEA 编辑器，显示项目结构，选中 `application.yml` 文件，内容为 `server: port: 8082`，光标在 `hehe` 后。
画面 3: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082`，`name: abc`，`person: name: zhangsan`。
画面 4: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082`，`name: abc`，`person: name: zhangsan age: 20`。
画面 5: IDEA 编辑器，切换到 `application.properties` 文件，内容为 `server.port=8082 name=abc`。
画面 6: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: zhangsan age: 20`。
画面 7: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: zhangsan age: 20`，光标在文件末尾。
画面 8: PPT 页面，标题为“Spring Boot 配置”，子标题“YAML：数据格式”，内容包括对象（map）、数组（array）和纯量（scalar）的 YAML 语法示例。
画面 9: PPT 页面，标题为“Spring Boot 配置”，子标题“YAML：参数引用”，内容为 `name: lisi person: name: ${name} # 引用上边定义的name值`。
画面 10: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: zhangsan age: 20 address: - beijing - shanghai msg1: 'hello \n world' # 不会识别转义字符，会原样输出 msg2: "hello \n world" # 双引号转义字符`。
画面 11: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: ${name} age: 20 address: - beijing - shanghai msg1: 'hello \n world' # 不会识别转义字符，会原样输出 msg2: "hello \n world" # 双引号转义字符`，光标在 `name: ${name}` 后，弹出系统属性提示框。
画面 12: IDEA 编辑器，`application.yml` 文件内容为 `server: port: 8082 name: abc person: name: ${name} age: 20 address: - beijing - shanghai msg1: 'hello \n world' # 不会识别转义字符，会原样输出 msg2: "hello \n world" # 双引号转义字符`，光标在 `name: ${name}` 后。
画面 13: PPT 页面，标题为“Spring Boot 配置”，子标题“YAML：参数引用”，内容为 `name: lisi person: name: ${name} # 引用上边定义的name值`。
画面 14: PPT 页面，标题为“Spring Boot 配置”，子标题“YAML：小结”，内容为“1) 配置文件类型：properties: 和以前一样 yaml/yaml: 注意空格 2) yaml: 简洁，以数据为核心 基本语法：大小写敏感 数据值前边必须有空格，作为分隔符 使用空格缩进表示层级关系，相同缩进表示同一级 数据格式：对象 数组：使用 “-” 表示数组每个元素 纯量 参数引用：${key}`。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面 1:
```
对象(map): 键值对的集合.
person:
  name: zhangsan
# 行内写法
person: {name: zhangsan}

数组: 一组按次序排列的值
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]
```

画面 2:
```
server:
  port: 8082
```

画面 3:
```
server:
  port: 8082
name: abc
# 对象
person:
  name: zhangsan
```

画面 4:
```
server:
  port: 8082
name: abc
# 对象
person:
  name: zhangsan
  age: 20
```

画面 5:
```
server.port=8082
name=abc
```

画面 6:
```
server:
  port: 8082
name: abc
person:
  name: zhangsan
  age: 20
```

画面 7:
```
server:
  port: 8082
name: abc
person:
  name: zhangsan
  age: 20
```

画面 8:
```
对象(map): 键值对的集合.
person:
  name: zhangsan
# 行内写法
person: {name: zhangsan}

数组: 一组按次序排列的值
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

纯量: 单个的、不可再分的值
msg1: 'hello \n world' # 单引号转义字符
msg2: "hello \n world" # 双引号转义字符
```

画面 9:
```
name: lisi
person:
  name: ${name} # 引用上边定义的name值
```

画面 10:
```
server:
  port: 8082
name: abc
person:
  name: zhangsan
  age: 20
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

# 纯量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 双引号转义字符
```

画面 11:
```
server:
  port: 8082
name: abc
person:
  name: ${name}
  age: 20
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

# 纯量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 双引号转义字符
```

画面 12:
```
server:
  port: 8082
name: abc
person:
  name: ${name}
  age: 20
address:
  - beijing
  - shanghai
# 行内写法
address: [beijing,shanghai]

# 纯量
msg1: 'hello \n world' # 不会识别转义字符，会原样输出
msg2: "hello \n world" # 双引号转义字符
```

画面 13:
```
name: lisi
person:
  name: ${name} # 引用上边定义的name值
```

画面 14:
```
1) 配置文件类型
  • properties: 和以前一样
  • yaml/yaml: 注意空格
2) yaml: 简洁，以数据为核心
  • 基本语法
    • 大小写敏感
    • 数据值前边必须有空格，作为分隔符
    • 使用空格缩进表示层级关系，相同缩进表示同一级
  • 数据格式
    • 对象
    • 数组: 使用 “-” 表示数组每个元素
    • 纯量
  • 参数引用
    • ${key}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面 1: 标题“Spring Boot 配置”，子标题“YAML：数据格式”，内容为 YAML 对象和数组的示例。
画面 8: 标题“Spring Boot 配置”，子标题“YAML：数据格式”，内容为 YAML 对象、数组和纯量的示例。
画面 9: 标题“Spring Boot 配置”，子标题“YAML：参数引用”，内容为 YAML 参数引用示

