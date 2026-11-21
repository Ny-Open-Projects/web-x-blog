# Sentinel实现限流

- 来源：JavaEE中级进修课资料（新版）\10.基于P2P的万信金融项目课程\微服务高级\讲义\Sentinel实现限流\Sentinel实现限流【海量资源尽在 666java.com】.pdf
- 页数：12
- 抽取：pypdf 文本层



<!-- page 1 -->
Sentinel
实现限流
 
学习目标
 
1
）能够说出限流的使用场景
2
）掌握
Sentinel
的快速入门
3
）理解
Sentinel
对资源的定义
4
）理解
Sentinel
对限流规则
5
）掌握
Sentinel
针对
Zuul
网关限流的实现方法
1 
限流概述
 
1.1 
问题分析
 
举个生活中的例子，一些热门的旅游景点，一般会对每日的景点入场人数有着严格的限制，比如北京的
故宫，每天只会卖出固定数目的门票，如果当天的票卖完了，当天就无法进入景点。
为什么旅游景点要做这样的人流限制呢？是因为它们的服务资源有限，景点的面积、服务人员数量、卫
生情况等各方面的承载能力都是有限的。景点入场人数一旦超出其承载能力，各种服务得不到保障，安
全会也出现隐患，密集人群也会给游客带来很不好的游玩体验。因此，景区只好做出限制每日入场人数
的举措。
同理，在软件系统中也存在这样的问题。如果一个系统每天可服务
100
万用户，突然有一天来了
500
万，如果不加以限流，很有可能导致这
500
万用户一下子就压垮系统，导致实际完成服务的用户寥寥无
几。因此为了保证系统至少还能为这
100
万用户提供正常服务，我们需要对系统进行限流设计。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
限流的定义：就是限制系统的输入和输出流量，达到保护系统的目的
。
一般来说系统的吞吐量是可以被测算的，为了保证系统的稳定运行，一旦达到的需要限制的阈值，就需
要采取一些措施以完成限制流量的目的。比如：延迟处理，拒绝处理，或者部分拒绝处理等等。
1.2 Sentinel
简介
 
怎么实现限流呢？目前比较流行的就是通过限流算法，常见的有计数器算法、令牌桶算法、漏桶算法和
滑动窗口算法。这些算法我们暂时不用管它，我们直接使用行业中成熟的框架去实现限流即可，这些框
架内部会采用一些限流算法。
随着微服务的流行，服务和服务之间的稳定性变得越来越重要。
Sentinel
是阿里巴巴开源的面向分布式
服务架构的
轻量级
流量控制框架，主要以流量为切入点，从流量控制、熔断降级、系统负载保护等多个
维度来保护服务的稳定性，
这里主要介绍流量控制
。
Sentinel
译为
“
哨兵
”
，发展历史如下：
2012 
年，
Sentinel 
诞生，主要功能为入口流量控制。
2013-2017 
年，
Sentinel 
在阿里巴巴集团内部迅速发展，成为基础技术模块，覆盖了所有的核心
场景。
Sentinel 
也因此积累了大量的流量归整场景以及生产实践。
2018 
年，
Sentinel 
开源。
Sentinel 
具有以下特征
:
丰富的应用场景
：
S
e
n
t
i
n
e
l
 
承接了阿里巴巴近
 10 
年的双十一大促流量的核心场景，例如秒杀
（即突发流量控制在系统容量可以承受的范围）、消息削峰填谷、实时熔断下游不可用应用等。
完备的实时监控
：
S
e
n
t
i
n
e
l
 
同时提供实时的监控功能。您可以在控制台中看到接入应用的单台
机器秒级数据，甚至
 500 
台以下规模的集群的汇总运行情况。
广泛的开源生态
：
S
e
n
t
i
n
e
l
 
提供开箱即用的与其它开源框架
/
库的整合模块，例如与
 
S
p
r
i
n
g
C
l
o
u
d
、
D
u
b
b
o
、
g
R
P
C
 
的整合。您只需要引入相应的依赖并进行简单的配置即可快速地接入
S
e
n
t
i
n
e
l
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
完善的
 SPI 
扩展点
：
S
e
n
t
i
n
e
l
 
提供简单易用、完善的
 
S
P
I
 
扩展点。您可以通过实现扩展点，快
速的定制逻辑。例如定制规则管理、适配数据源等。
Sentinel
分为两部分：
核心库（
Java 
客户端）不依赖任何框架
/
库，能够运行于所有
 Java 
运行时环境，同时对
 Dubbo /
Spring Cloud 
等框架也有较好的支持。
控制台（
Dashboar
d
）基于
 Spring Boot 
开发，打包后可以直接运行，不需要额外的
 T
omcat 
等
应用容器。
2 
快速入门
 
使用
 Sentinel 
来实现限流，主要分为几个步骤
:
1
. 
定义资源，这里的资源可以是任何东西，例如某个服务，某个服务里的方法，甚至是一段代码。
2
. 
定义规则，指的是流量控制规则
3
. 
检验规则是否生效
先把可能需要保护的资源定义好，之后再配置规则。也可以理解为，只要有了资源，我们就可以在任何
时候灵活地定义各种流量控制规则。在编码的时候，只需要考虑这个代码是否需要保护，如果需要保
护，就将之定义为一个资源。
对于主流框架，
Sentinel
都提供了适配，只需要按照适配中的说明配置，
Sentinel 
就会默认定义提供的
服务，方法等为资源。
Sentinel
支持的主流框架适配列表如下：
W
eb Servlet
Dubbo
Spring Boot / Spring Cloud
Spring W
ebFlux
gRPC
Reactive 
适配
Reactor
API Gate
way 
适配
Spring Cloud Gate
way
Netﬂix Zuul 1.x
Netﬂix Zuul 1.x
Apache Rock
etMQ
2.1 
入门案例
 
1
. 
创建名为
SentinelDemo
的
maven
工程
2
. 
引入依赖
 
 
 
 
<
p
a
r
e
n
t
>
 
 
 
 
 
 
 
 
<
g
r
o
u
p
I
d
>
o
r
g
.
s
p
r
i
n
g
f
r
a
m
e
w
o
r
k
.
b
o
o
t
<
/
g
r
o
u
p
I
d
>
 
 
 
 
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
p
r
i
n
g
-
b
o
o
t
-
s
t
a
r
t
e
r
-
p
a
r
e
n
t
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
 
 
 
 
<
v
e
r
s
i
o
n
>
2
.
1
.
3
.
R
E
L
E
A
S
E
<
/
v
e
r
s
i
o
n
>
 
 
 
 
<
/
p
a
r
e
n
t
>
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
i
t
h
e
i
m
a
.
m
s
a
.
s
e
n
t
i
n
e
l
<
/
g
r
o
u
p
I
d
>
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
e
n
t
i
n
e
l
d
e
m
o
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
<
v
e
r
s
i
o
n
>
0
.
0
.
1
-
S
N
A
P
S
H
O
T
<
/
v
e
r
s
i
o
n
>
 
 
 
 
<
n
a
m
e
>
s
e
n
t
i
n
e
l
-
d
e
m
o
<
/
n
a
m
e
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
3
. 
application.pr
operties
4
. 
Service
 
 
 
 
<
p
r
o
p
e
r
t
i
e
s
>
 
 
 
 
 
 
 
 
<
j
a
v
a
.
v
e
r
s
i
o
n
>
1
.
8
<
/
j
a
v
a
.
v
e
r
s
i
o
n
>
 
 
 
 
 
 
 
 
<
p
r
o
j
e
c
t
.
b
u
i
l
d
.
s
o
u
r
c
e
E
n
c
o
d
i
n
g
>
U
T
F
-
8
<
/
p
r
o
j
e
c
t
.
b
u
i
l
d
.
s
o
u
r
c
e
E
n
c
o
d
i
n
g
>
 
 
 
 
 
 
 
 
<
p
r
o
j
e
c
t
.
r
e
p
o
r
t
i
n
g
.
o
u
t
p
u
t
E
n
c
o
d
i
n
g
>
U
T
F
-
8
<
/
p
r
o
j
e
c
t
.
r
e
p
o
r
t
i
n
g
.
o
u
t
p
u
t
E
n
c
o
d
i
n
g
>
 
 
 
 
<
/
p
r
o
p
e
r
t
i
e
s
>
 
 
 
 
<
d
e
p
e
n
d
e
n
c
i
e
s
>
 
 
 
 
 
 
 
 
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
 
 
 
 
<
g
r
o
u
p
I
d
>
o
r
g
.
s
p
r
i
n
g
f
r
a
m
e
w
o
r
k
.
b
o
o
t
<
/
g
r
o
u
p
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
p
r
i
n
g
-
b
o
o
t
-
s
t
a
r
t
e
r
-
w
e
b
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
 
 
 
 
<
g
r
o
u
p
I
d
>
o
r
g
.
s
p
r
i
n
g
f
r
a
m
e
w
o
r
k
.
c
l
o
u
d
<
/
g
r
o
u
p
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
p
r
i
n
g
-
c
l
o
u
d
-
s
t
a
r
t
e
r
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
a
l
i
b
a
b
a
.
c
l
o
u
d
<
/
g
r
o
u
p
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
p
r
i
n
g
-
c
l
o
u
d
-
s
t
a
r
t
e
r
-
a
l
i
b
a
b
a
-
s
e
n
t
i
n
e
l
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
v
e
r
s
i
o
n
>
2
.
1
.
0
.
R
E
L
E
A
S
E
<
/
v
e
r
s
i
o
n
>
 
 
 
 
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
i
e
s
>
 
 
 
 
<
d
e
p
e
n
d
e
n
c
y
M
a
n
a
g
e
m
e
n
t
>
 
 
 
 
 
 
 
 
<
d
e
p
e
n
d
e
n
c
i
e
s
>
 
 
 
 
 
 
 
 
 
 
 
 
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
g
r
o
u
p
I
d
>
o
r
g
.
s
p
r
i
n
g
f
r
a
m
e
w
o
r
k
.
c
l
o
u
d
<
/
g
r
o
u
p
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
p
r
i
n
g
-
c
l
o
u
d
-
d
e
p
e
n
d
e
n
c
i
e
s
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
v
e
r
s
i
o
n
>
G
r
e
e
n
w
i
c
h
.
R
E
L
E
A
S
E
<
/
v
e
r
s
i
o
n
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
t
y
p
e
>
p
o
m
<
/
t
y
p
e
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
s
c
o
p
e
>
i
m
p
o
r
t
<
/
s
c
o
p
e
>
 
 
 
 
 
 
 
 
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
i
e
s
>
 
 
 
 
<
/
d
e
p
e
n
d
e
n
c
y
M
a
n
a
g
e
m
e
n
t
>
 
 
 
 
<
b
u
i
l
d
>
 
 
 
 
 
 
 
 
<
p
l
u
g
i
n
s
>
 
 
 
 
 
 
 
 
 
 
 
 
<
p
l
u
g
i
n
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
g
r
o
u
p
I
d
>
o
r
g
.
s
p
r
i
n
g
f
r
a
m
e
w
o
r
k
.
b
o
o
t
<
/
g
r
o
u
p
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
p
r
i
n
g
-
b
o
o
t
-
m
a
v
e
n
-
p
l
u
g
i
n
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
/
p
l
u
g
i
n
>
 
 
 
 
 
 
 
 
<
/
p
l
u
g
i
n
s
>
 
 
 
 
<
/
b
u
i
l
d
>
s
p
r
i
n
g
.
a
p
p
l
i
c
a
t
i
o
n
.
n
a
m
e
=
S
e
n
t
i
n
e
l
D
e
m
o
s
e
r
v
e
r
.
p
o
r
t
=
5
9
0
0
0
s
e
r
v
e
r
.
s
e
r
v
l
e
t
.
c
o
n
t
e
x
t
-
p
a
t
h
=
/
s
e
n
t
i
n
e
l
@
S
e
r
v
i
c
e
p
u
b
l
i
c
 
c
l
a
s
s
 
T
e
s
t
S
e
r
v
i
c
e
 
{
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
@SentinelResour
ce 
注解用来标识资源是否被限流、降级。上述例子中该注解的属性
 'hello
' 
表示
资源名。
@SentinelResour
ce 
还提供了其它额外的属性如
 
b
l
o
c
k
H
a
n
d
l
e
r
来指定被限流后的操作。
initFlo
wRules
方法内定义了限流资源和限流规则，在构造方法执行完毕后会自动运行
5
. 
Contr
oller
类
6
. 
功能测试
通过浏览器访问
http://localhost:59000/sentinel/hello
，慢速刷新，则持续显示
H
e
l
l
o
 
S
e
n
t
i
n
e
l
；快
速刷新则会交替出现
H
e
l
l
o
 
S
e
n
t
i
n
e
l
与
系
统
繁
忙
，
请
稍
候
。这说明对
h
e
l
l
o
资源限流成功。我们还可
以通过查看日志获取限流详情，日志文件的位置可以在控制台找到
(
图中红框处
)
。
 
 
 
 
@
S
e
n
t
i
n
e
l
R
e
s
o
u
r
c
e
(
v
a
l
u
e
 
=
 
"
h
e
l
l
o
"
,
b
l
o
c
k
H
a
n
d
l
e
r
 
=
 
"
e
x
c
e
p
t
i
o
n
H
a
n
d
l
e
r
"
)
 
 
 
 
p
u
b
l
i
c
 
S
t
r
i
n
g
 
h
e
l
l
o
(
)
{
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
H
e
l
l
o
 
S
e
n
t
i
n
e
l
"
;
 
 
 
 
}
 
 
 
 
p
u
b
l
i
c
 
S
t
r
i
n
g
 
e
x
c
e
p
t
i
o
n
H
a
n
d
l
e
r
(
B
l
o
c
k
E
x
c
e
p
t
i
o
n
 
e
x
)
{
 
 
 
 
 
 
 
 
e
x
.
p
r
i
n
t
S
t
a
c
k
T
r
a
c
e
(
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
系
统
繁
忙
，
请
稍
候
"
;
 
 
 
 
}
 
 
 
 
@
P
o
s
t
C
o
n
s
t
r
u
c
t
 
 
 
 
p
u
b
l
i
c
 
v
o
i
d
 
i
n
i
t
F
l
o
w
R
u
l
e
s
(
)
{
 
 
 
 
 
 
 
 
L
i
s
t
<
F
l
o
w
R
u
l
e
>
 
r
u
l
e
s
=
n
e
w
 
A
r
r
a
y
L
i
s
t
<
>
(
)
;
 
 
 
 
 
 
 
 
/
/
创
建
F
l
o
w
R
u
l
e
对
象
封
装
限
流
规
则
 
 
 
 
 
 
 
 
F
l
o
w
R
u
l
e
 
r
u
l
e
=
n
e
w
 
F
l
o
w
R
u
l
e
(
)
;
 
 
 
 
 
 
 
 
r
u
l
e
.
s
e
t
R
e
s
o
u
r
c
e
(
"
h
e
l
l
o
"
)
;
 
 
 
 
 
 
 
 
r
u
l
e
.
s
e
t
G
r
a
d
e
(
R
u
l
e
C
o
n
s
t
a
n
t
.
F
L
O
W
_
G
R
A
D
E
_
Q
P
S
)
;
 
 
 
 
 
 
 
 
r
u
l
e
.
s
e
t
C
o
u
n
t
(
2
)
;
 
 
 
 
 
 
 
 
r
u
l
e
s
.
a
d
d
(
r
u
l
e
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
/
/
加
载
或
启
用
限
流
规
则
 
 
 
 
 
 
 
 
F
l
o
w
R
u
l
e
M
a
n
a
g
e
r
.
l
o
a
d
R
u
l
e
s
(
r
u
l
e
s
)
;
 
 
 
 
}
}
@
R
e
s
t
C
o
n
t
r
o
l
l
e
r
p
u
b
l
i
c
 
c
l
a
s
s
 
T
e
s
t
C
o
n
t
r
o
l
l
e
r
 
{
 
 
 
 
@
A
u
t
o
w
i
r
e
d
 
 
 
 
p
r
i
v
a
t
e
 
T
e
s
t
S
e
r
v
i
c
e
 
t
e
s
t
S
e
r
v
i
c
e
;
 
 
 
 
@
G
e
t
M
a
p
p
i
n
g
(
"
h
e
l
l
o
"
)
 
 
 
 
p
u
b
l
i
c
 
S
t
r
i
n
g
 
h
e
l
l
o
(
)
 
{
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
t
e
s
t
S
e
r
v
i
c
e
.
h
e
l
l
o
(
)
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
在该目录下找到
S
e
n
t
i
n
e
l
D
e
m
o
-
m
e
t
r
i
c
s
.
l
o
g
.
y
y
y
y
-
M
M
-
d
d
文件，查看该文件内容如下所示：
2.2 Sentinel-Dashboar
d
图形化控制台
 
我们可以通过
Dashboar
d
更直观的查看这些日志信息，通过如下命令启动
Dashboar
d
：
注意：需要
 JDK 
版本为
 1.8 
及以上版本
然后通过浏览器打开
http://localhost:9999
即可访问
Dashboar
d
，默认用户名和密码都是
s
e
n
t
i
n
e
l
1
5
7
2
8
6
2
7
2
6
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
6
|
h
e
l
l
o
|
1
|
0
|
1
|
0
|
4
|
0
|
0
|
1
1
5
7
2
8
6
2
7
2
6
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
6
|
_
_
t
o
t
a
l
_
i
n
b
o
u
n
d
_
t
r
a
f
f
i
c
_
_
|
1
|
0
|
1
|
0
|
4
|
0
|
0
|
0
1
5
7
2
8
6
2
7
2
7
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
7
|
h
e
l
l
o
|
1
|
0
|
1
|
0
|
4
|
0
|
0
|
1
1
5
7
2
8
6
2
7
2
7
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
7
|
_
_
t
o
t
a
l
_
i
n
b
o
u
n
d
_
t
r
a
f
f
i
c
_
_
|
1
|
0
|
1
|
0
|
4
|
0
|
0
|
0
1
5
7
2
8
6
2
7
2
8
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
8
|
h
e
l
l
o
|
1
|
0
|
1
|
0
|
5
|
0
|
0
|
1
1
5
7
2
8
6
2
7
2
8
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
8
|
_
_
t
o
t
a
l
_
i
n
b
o
u
n
d
_
t
r
a
f
f
i
c
_
_
|
1
|
0
|
1
|
0
|
5
|
0
|
0
|
0
1
5
7
2
8
6
2
7
2
9
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
9
|
h
e
l
l
o
|
3
|
0
|
3
|
0
|
2
|
0
|
0
|
1
1
5
7
2
8
6
2
7
2
9
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
4
9
|
_
_
t
o
t
a
l
_
i
n
b
o
u
n
d
_
t
r
a
f
f
i
c
_
_
|
3
|
0
|
3
|
0
|
2
|
0
|
0
|
0
1
5
7
2
8
6
2
7
3
0
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
5
0
|
h
e
l
l
o
|
3
|
0
|
3
|
0
|
3
|
0
|
0
|
1
1
5
7
2
8
6
2
7
3
0
0
0
0
|
2
0
1
9
-
1
1
-
0
4
 
1
8
:
1
8
:
5
0
|
_
_
t
o
t
a
l
_
i
n
b
o
u
n
d
_
t
r
a
f
f
i
c
_
_
|
3
|
0
|
3
|
0
|
3
|
0
|
0
|
0
j
a
v
a
 
-
D
s
e
r
v
e
r
.
p
o
r
t
=
9
9
9
9
 
-
j
a
r
 
s
e
n
t
i
n
e
l
-
d
a
s
h
b
o
a
r
d
.
j
a
r
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
在
application.pr
operties
中增加如下配置：
重启微服务并重新通过浏览器访问
http://localhost:59000/sentinel/hello
，快慢速刷新几次。
2.3 
限流规则详解
 
2.3.1 
限流规则参数
 
一条限流规则主要由下面几个元素组成，我们可以组合这些元素来实现不同的限流效果：
1
. 
r
e
s
o
u
r
c
e
：资源名，即限流规则的作用对象
2
. 
g
r
a
d
e
: 
限流阈值类型（
QPS 
或并发线程数）
3
. 
c
o
u
n
t
: 
限流阈值
4
. 
l
i
m
i
t
A
p
p
: 
流控针对的调用来源，若为
 
d
e
f
a
u
l
t
 
则不区分调用来源
5
. 
c
o
n
t
r
o
l
B
e
h
a
v
i
o
r
: 
流量控制效果（直接拒绝、
W
arm Up
、匀速排队等待）
s
p
r
i
n
g
.
c
l
o
u
d
.
s
e
n
t
i
n
e
l
.
t
r
a
n
s
p
o
r
t
.
d
a
s
h
b
o
a
r
d
=
l
o
c
a
l
h
o
s
t
:
9
9
9
9
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
直接拒绝
（
R
u
l
e
C
o
n
s
t
a
n
t
.
C
O
N
T
R
O
L
_
B
E
H
A
V
I
O
R
_
D
E
F
A
U
L
T
）方式是默认的流量控制方式，当
QPS
超过任意规则的阈值后，新的请求就会被立即拒绝，拒绝方式为抛出
F
l
o
w
E
x
c
e
p
t
i
o
n
。
这种方式适用于对系统处理能力确切已知的情况下，比如通过压测确定了系统的准确水位
时。
W
arm Up
（
R
u
l
e
C
o
n
s
t
a
n
t
.
C
O
N
T
R
O
L
_
B
E
H
A
V
I
O
R
_
W
A
R
M
_
U
P
）方式，即预热
/
冷启动方式。当
系统长期处于低水位的情况下，当流量突然增加时，直接把系统拉升到高水位可能瞬间把系
统压垮。通过
"
冷启动
"
，让通过的流量缓慢增加，在一定时间内逐渐增加到阈值上限，给冷
系统一个预热的时间，避免冷系统被压垮。
排队等待
（
R
u
l
e
C
o
n
s
t
a
n
t
.
C
O
N
T
R
O
L
_
B
E
H
A
V
I
O
R
_
R
A
T
E
_
L
I
M
I
T
E
R
）方式会严格控制请求通过
的间隔时间，也即是让请求以均匀的速度通过，对应的是漏桶算法。
前面我们是通过
Java
代码来设置限流规则，同时
Sentinel
也支持通过
Dashboar
d
图形化控制台来设
置限流规则，如下图所示：
 
2.3.3 
动态规则
 
前面不管是通过
Java
代码还是通过
Dashboar
d
的方式去设置限流规则，都属于手动方式，不够灵活。这
种方式一般仅用于测试和演示，生产环境上一般通过动态规则源的方式来动态管理限流规则。也就是
说，很多时候限流规则会被存储在文件、数据库或者配置中心当中。
Sentinel
的
D
a
t
a
S
o
u
r
c
e
 
接口给我
们提供了对接任意配置源的能力。
官方推荐
通过控制台设置规则后将规则推送到统一的规则中心，客户端实现
 
R
e
a
d
a
b
l
e
D
a
t
a
S
o
u
r
c
e
 
接
口端监听规则中心实时获取变更
，流程如下：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
常见的实现方式有
:
拉取式
：客户端主动向某个规则管理中心定期轮询拉取规则，这个规则中心可以是
 RDBMS
、文
件，甚至是
 V
CS 
等。这样做的方式是简单，缺点是无法及时获取变更；实现拉模式的数据源最简
单的方式是继承
 
A
u
t
o
R
e
f
r
e
s
h
D
a
t
a
S
o
u
r
c
e
 
抽象类，然后实现
 
r
e
a
d
S
o
u
r
c
e
(
)
方法，在该方法里
从指定数据源读取字符串格式的配置数据。
推送式
：规则中心统一推送，客户端通过注册监听器的方式时刻监听变化，比如使用
 
Nacos
、
Zook
eeper 
、
Apollo
等配置中心。这种方式有更好的实时性和一致性保证。实现推模式的数据源
最简单的方式是继承
 
A
b
s
t
r
a
c
t
D
a
t
a
S
o
u
r
c
e
抽象类，在其构造方法中添加监听器，并实现
r
e
a
d
S
o
u
r
c
e
(
)
 
从指定数据源读取字符串格式的配置数据。
这里演示如何使用
 Apollo 
配置规则
Sentinel 
针对携程
Apollo
作了相应适配，底层可以采用
 Apollo 
作为规则配置数据源。使用时只需添加
以下依赖：
然后创建
 
A
p
o
l
l
o
D
a
t
a
S
o
u
r
c
e
 
并将其注册至对应的
 RuleManager 
上即可。例如：
3 
实现万信金融
P2P
网关限流
 
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
a
l
i
b
a
b
a
.
c
s
p
<
/
g
r
o
u
p
I
d
>
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
e
n
t
i
n
e
l
-
d
a
t
a
s
o
u
r
c
e
-
a
p
o
l
l
o
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
<
v
e
r
s
i
o
n
>
1
.
6
.
2
<
/
v
e
r
s
i
o
n
>
<
/
d
e
p
e
n
d
e
n
c
y
>
/
/
 
n
a
m
e
s
p
a
c
e
N
a
m
e
 
对
应
A
p
o
l
l
o
的
命
名
空
间
名
称
/
/
 
r
u
l
e
K
e
y
 
对
应
规
则
存
储
的
k
e
y
/
/
 
d
e
f
a
u
l
t
R
u
l
e
s
 
对
应
连
接
不
上
A
p
o
l
l
o
时
的
默
认
规
则
R
e
a
d
a
b
l
e
D
a
t
a
S
o
u
r
c
e
<
S
t
r
i
n
g
,
 
L
i
s
t
<
F
l
o
w
R
u
l
e
>
>
 
f
l
o
w
R
u
l
e
D
a
t
a
S
o
u
r
c
e
 
=
 
n
e
w
 
A
p
o
l
l
o
D
a
t
a
S
o
u
r
c
e
<
>
(
n
a
m
e
s
p
a
c
e
N
a
m
e
,
 
r
u
l
e
K
e
y
,
 
d
e
f
a
u
l
t
R
u
l
e
s
,
 
s
o
u
r
c
e
 
-
>
 
J
S
O
N
.
p
a
r
s
e
O
b
j
e
c
t
(
s
o
u
r
c
e
,
 
n
e
w
 
T
y
p
e
R
e
f
e
r
e
n
c
e
<
L
i
s
t
<
F
l
o
w
R
u
l
e
>
>
(
)
 
{
}
)
)
;
F
l
o
w
R
u
l
e
M
a
n
a
g
e
r
.
r
e
g
i
s
t
e
r
2
P
r
o
p
e
r
t
y
(
f
l
o
w
R
u
l
e
D
a
t
a
S
o
u
r
c
e
.
g
e
t
P
r
o
p
e
r
t
y
(
)
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
万信金融
P2P
平台在发展过程中，吞吐量也会与日俱增，为了保证系统稳定性，需要考虑使用
Sentinel
进行限流。由于该平台使用
HT
TP
网关作为系统的唯一入口，因此我们使用
Sentinel 
的网关限流模式。
3.1 
网关限流概述
 
Sentinel 
支持整合
 Spring Cloud Gate
way
、
Zuul 
等主流的网关进行限流。
Sentinel 1.6.0 
引入了
Sentinel API Gate
way Adapter Common 
模块，此模块中包含网关限流的规则和自定义
 API
。整体架
构如下图所示：
 
3.2 
功能实现
 
万信金融
p2p
项目采用
spring cloud zuul
作为网关，采用携程
apollo
作为配置中心。因此可以使用
Sentinel
集成
Zuul
，并采用
apollo
作为限流规则数据源。
1
. 
增加依赖
在父工程
pom
文件中
(wanxinp2p/pom.xml)
增加如下依赖管理：
在网关工程的
pom
文件中
(wanxinp2p-gate
way-server/pom.xml)
增加如下依赖：
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
a
l
i
b
a
b
a
.
c
s
p
<
/
g
r
o
u
p
I
d
>
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
e
n
t
i
n
e
l
-
z
u
u
l
-
a
d
a
p
t
e
r
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
<
v
e
r
s
i
o
n
>
1
.
6
.
2
<
/
v
e
r
s
i
o
n
>
<
/
d
e
p
e
n
d
e
n
c
y
>
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
a
l
i
b
a
b
a
.
c
s
p
<
/
g
r
o
u
p
I
d
>
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
e
n
t
i
n
e
l
-
d
a
t
a
s
o
u
r
c
e
-
a
p
o
l
l
o
<
/
a
r
t
i
f
a
c
t
I
d
>
 
 
 
 
<
v
e
r
s
i
o
n
>
1
.
6
.
2
<
/
v
e
r
s
i
o
n
>
<
/
d
e
p
e
n
d
e
n
c
y
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
3
. 
集成
Sentine
和
Zuul
找到
cn.itcast.wanxinp2p.gate
way
.conﬁg.ZuulConﬁg
类，创建限流过滤器
SentinelZuulXxxFilter
，作
为
Zuul
与
Sentinel
的集成点：
4
. 
设置动态规则，在
Apollo
中找到网关项目
(
gate
way-server
)
，在
application
命名空间中新增配
置，
k
e
y
为
sentinel.rule.gate
way-ﬂo
w-rule
，
value
如下：
5
. 
在
ZuulConﬁg
中增加限流规则配置，采用
apollo
作为
Sentinel
的动态规则数据源
(
前提是该项目已正
确配置
apollo
并能够成功连接
)
。
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
a
l
i
b
a
b
a
.
c
s
p
<
/
g
r
o
u
p
I
d
>
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
e
n
t
i
n
e
l
-
z
u
u
l
-
a
d
a
p
t
e
r
<
/
a
r
t
i
f
a
c
t
I
d
>
<
/
d
e
p
e
n
d
e
n
c
y
>
<
d
e
p
e
n
d
e
n
c
y
>
 
 
 
 
<
g
r
o
u
p
I
d
>
c
o
m
.
a
l
i
b
a
b
a
.
c
s
p
<
/
g
r
o
u
p
I
d
>
 
 
 
 
<
a
r
t
i
f
a
c
t
I
d
>
s
e
n
t
i
n
e
l
-
d
a
t
a
s
o
u
r
c
e
-
a
p
o
l
l
o
<
/
a
r
t
i
f
a
c
t
I
d
>
<
/
d
e
p
e
n
d
e
n
c
y
>
@
C
o
n
f
i
g
u
r
a
t
i
o
n
p
u
b
l
i
c
 
c
l
a
s
s
 
Z
u
u
l
C
o
n
f
i
g
 
{
 
 
 
 
/
/
其
他
代
码
.
.
.
 
 
 
 
 
 
 
 
@
B
e
a
n
 
 
 
 
/
/
p
r
e
过
滤
器
，
在
请
求
路
由
之
前
进
行
限
流
操
作
 
 
 
 
p
u
b
l
i
c
 
Z
u
u
l
F
i
l
t
e
r
 
s
e
n
t
i
n
e
l
Z
u
u
l
P
r
e
F
i
l
t
e
r
(
)
 
{
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
 
S
e
n
t
i
n
e
l
Z
u
u
l
P
r
e
F
i
l
t
e
r
(
)
;
 
 
 
 
}
 
 
 
 
@
B
e
a
n
 
 
 
/
/
p
o
s
t
过
滤
器
，
路
由
之
后
恢
复
资
源
 
 
 
 
p
u
b
l
i
c
 
Z
u
u
l
F
i
l
t
e
r
 
s
e
n
t
i
n
e
l
Z
u
u
l
P
o
s
t
F
i
l
t
e
r
(
)
 
{
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
 
S
e
n
t
i
n
e
l
Z
u
u
l
P
o
s
t
F
i
l
t
e
r
(
)
;
 
 
 
 
}
 
 
 
 
@
B
e
a
n
 
 
/
/
e
r
r
o
r
过
滤
器
，
异
常
后
的
处
理
 
 
 
 
p
u
b
l
i
c
 
Z
u
u
l
F
i
l
t
e
r
 
s
e
n
t
i
n
e
l
Z
u
u
l
E
r
r
o
r
F
i
l
t
e
r
(
)
 
{
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
 
S
e
n
t
i
n
e
l
Z
u
u
l
E
r
r
o
r
F
i
l
t
e
r
(
)
;
 
 
 
 
}
}
[
 
{
 
 
 
 
"
r
e
s
o
u
r
c
e
"
:
 
"
u
a
a
-
s
e
r
v
i
c
e
"
,
 
/
/
对
应
z
u
u
l
的
r
o
u
t
e
s
，
这
里
的
资
源
指
的
是
统
一
认
证
服
务
 
 
 
 
"
r
e
s
o
u
r
c
e
M
o
d
e
"
:
0
,
 
/
/
网
关
模
式
 
 
 
 
"
g
r
a
d
e
"
:
 
1
,
 
/
/
Q
P
S
限
流
模
式
 
 
 
 
"
c
o
u
n
t
"
:
 
2
,
 
/
/
 
上
限
值
 
 
 
 
"
i
n
t
e
r
v
a
l
S
e
c
"
:
 
1
,
 
/
/
统
计
时
间
窗
口
，
单
位
是
秒
，
默
认
是
1
秒
 
 
 
 
"
c
o
n
t
r
o
l
B
e
h
a
v
i
o
r
"
:
 
0
,
 
/
/
流
量
控
制
效
果
（
直
接
拒
绝
、
W
a
r
m
 
U
p
、
匀
速
排
队
等
待
）
 
 
 
 
"
b
u
r
s
t
"
:
 
0
,
 
/
/
应
对
突
发
请
求
时
额
外
允
许
的
请
求
数
目
 
 
 
 
"
m
a
x
Q
u
e
u
e
i
n
g
T
i
m
e
o
u
t
M
s
"
:
 
5
0
0
,
 
/
/
匀
速
排
队
模
式
下
的
最
长
排
队
时
间
，
单
位
是
毫
秒
，
仅
在
匀
速
排
队
模
式
下
生
效
 
 
 
 
"
p
a
r
a
m
I
t
e
m
"
:
 
{
 
/
/
动
态
参
数
，
目
前
不
需
要
 
 
 
 
}
 
 
}
]
/
*
*
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
3.3 
功能测试
 
由于登录业务中涉及到
uaa-service
，所以这里就以登录功能为例进行测试。为了测试方便，我们通过
Postman
频繁发送登录请求，如果一秒内的访问次数超过两次，将会得到如下信息：
大家也可以结合
Dashboar
d
图形化控制台观察效果，这里不再演示。
 
*
 
从
A
p
o
l
l
o
上
获
取
限
流
规
则
并
进
行
配
置
 
*
/
@
P
o
s
t
C
o
n
s
t
r
u
c
t
p
r
i
v
a
t
e
 
v
o
i
d
 
i
n
i
t
G
a
t
e
w
a
y
R
u
l
e
s
(
)
 
{
 
 
 
 
S
t
r
i
n
g
 
n
a
m
e
s
p
a
c
e
N
a
m
e
 
=
 
"
a
p
p
l
i
c
a
t
i
o
n
"
;
 
/
/
 
对
应
A
p
o
l
l
o
的
命
名
空
间
名
称
 
 
 
 
S
t
r
i
n
g
 
r
u
l
e
K
e
y
 
=
 
"
s
e
n
t
i
n
e
l
.
r
u
l
e
.
g
a
t
e
w
a
y
-
f
l
o
w
-
r
u
l
e
"
;
 
/
/
限
流
规
则
的
k
e
y
 
 
 
 
S
t
r
i
n
g
 
d
e
f
a
u
l
t
R
u
l
e
s
 
=
 
"
"
;
 
 
 
 
/
/
从
A
p
o
l
l
o
上
获
取
限
流
规
则
并
封
装
到
A
p
o
l
l
o
D
a
t
a
S
o
u
r
c
e
 
 
 
 
A
p
o
l
l
o
D
a
t
a
S
o
u
r
c
e
 
g
a
t
e
w
a
y
R
u
l
e
D
a
t
a
S
o
u
r
c
e
 
=
 
n
e
w
 
A
p
o
l
l
o
D
a
t
a
S
o
u
r
c
e
<
>
(
n
a
m
e
s
p
a
c
e
N
a
m
e
,
r
u
l
e
K
e
y
,
d
e
f
a
u
l
t
R
u
l
e
s
,
s
o
u
r
c
e
-
>
 
 
 
 
 
 
 
 
J
S
O
N
.
p
a
r
s
e
O
b
j
e
c
t
(
s
o
u
r
c
e
,
n
e
w
 
T
y
p
e
R
e
f
e
r
e
n
c
e
<
S
e
t
<
G
a
t
e
w
a
y
F
l
o
w
R
u
l
e
>
>
(
)
 
{
}
)
)
;
 
 
 
 
/
/
注
册
限
流
规
则
使
其
生
效
 
 
 
 
G
a
t
e
w
a
y
R
u
l
e
M
a
n
a
g
e
r
.
r
e
g
i
s
t
e
r
2
P
r
o
p
e
r
t
y
(
g
a
t
e
w
a
y
R
u
l
e
D
a
t
a
S
o
u
r
c
e
.
g
e
t
P
r
o
p
e
r
t
y
(
)
)
;
{
 
 
 
 
"
c
o
d
e
"
:
 
4
2
9
,
 
 
 
 
"
m
e
s
s
a
g
e
"
:
 
"
S
e
n
t
i
n
e
l
 
b
l
o
c
k
 
e
x
c
e
p
t
i
o
n
"
,
 
 
 
 
"
r
o
u
t
e
"
:
 
"
u
a
a
-
s
e
r
v
i
c
e
"
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
