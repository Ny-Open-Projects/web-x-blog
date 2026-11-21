# SpringCloud Hystrix服务熔断

- 来源：JavaEE中级进修课资料（新版）\10.基于P2P的万信金融项目课程\微服务高级\讲义\SpringCloud Hystrix服务熔断\SpringCloud Hystrix服务熔断【海量资源尽在 666java.com】.pdf
- 页数：11
- 抽取：pypdf 文本层



<!-- page 1 -->
SpringCloud Hystrix 
服务熔断
 
教学目标
 
1
）能够说出服务熔断的概念以及使用场景
2
）了解
Hystrix
是什么
3
）理解
Hystrix
的三种状态
4
）掌握
Hystrix
的快速入门
5
）掌握
Spring Cloud Feign + Hystrix
的集成方式
6
）了解
Hystrix Dashboar
d
基本使用
1 
什么是服务熔断
 
在微服务架构的应用系统中，为了完成一次业务请求，往往需要多个服务协作完成，每次调用都会产生
一个调用链。
 
而且微服务之间进行
r
p
c
或者
h
t
t
p
调用时，我们一般都会设置
调
用
超
时
，
失
败
重
试
等机
制来确保服务的成功执行，看上去很完善，实际上却暗藏隐患。
假设我们有两个访问量比较大的服务
A
和
B
，这两个服务分别依赖
C
和
D , C
和
D
服务都依赖
E
，如下图所
示：
A
和
B
不断的调用
C,D
处理客户请求和返回需要的数据。当
E
不能供服务的时候，
C
和
D
的
超
时
和
重
试
机
制会被执行，如下图所示：
由于新的调用不断的产生，会导致
C
和
D
对
E
服务的调用大量的积压，产生大量的调用等待和重试调用，
慢慢会耗尽
C
和
D
的资源，比如内存或
CPU
，然后挂掉，如下图所示：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
接下来
A
和
B
服务会重复
C
和
D
的操作，资源耗尽，然后挂掉，最终一堆服务都不可访问，如下图所示：
像这种调用链路的连锁故障，叫做雪崩
 
。我们正在开发的万信金融
P2P
项目也会碰到类似场景，例如：
开户业务，满标放款业务等
(
可以查看业务流程图
)
。
如何解决呢？我们想到了现实生活中的
“
保险丝
”
。一个小区家家户户的电路中都会安装有保险丝，它起
什么作用呢？当电路发生故障或异常时，伴随着电流不断升高，并且升高的电流有可能损坏电路中的某
些重要器件，也有可能烧毁电路甚至造成火灾。若电路中正确地安装了保险丝，那么保险丝就会在电流
异常升高到一定的高度和热度的时候，自身熔断切断电流，从而起到保护电路安全运行的作用。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
通过这个案例，我们自然就想到，在分布式架构中，我们也可以为每个微服务加装
“
保险丝
”
，即：熔断
器，也叫断路器。当发现依赖的服务在一段时间内持续出现错误，熔断器就会自动断开，后续的请求不
会再真正访问依赖的服务，而是快速返回错误或缓存的数据，从而避免程序不断的尝试执行可能失败的
操作，降低资源消耗。
熔断这一概念来源于电子工程中的断路器（
Cir
cuit Br
eak
er
）。在互联网系统中，当下游服务因访问压
力过大而响应变慢或失败，上游服务为了保护系统整体的可用性，可以暂时切断对下游服务的调用。这
种牺牲局部，保全整体的措施就叫做
服务熔断
。
当进入
熔断
状态后，服务消费方将不会发出远程调用，直接返回失败。这样的情况用户体验显然不好，
针对这种情况，服务消费方可以在本地准备一个
备用
的
降级
方法进行用户体验改善处理。比如，查询接
口可准备默认值或缓存；秒杀业务可提示用户稍后再试。这种因服务处理能力退化而优雅返回错误的能
力，叫做
服务降级
。
 
熔断器是系统稳定性的最后一重保障。
2 Hystrix
 
上面已经介绍过
服务熔断
的基本概念，
 
而若实现它则需要有非常丰富的多线程开发经验
 
。不过
Netﬂix
的
Hystrix
库已经帮我们实现，可以使用它来让我们的应用变得更加健壮。
2.1 Hystrix
简介
 
Spring Cloud
中的断路器组件就是
Hystrix
，它也是
Netﬂix
套件的一部分。
hystrix
对应的中文名字是
“
豪
猪
”
，豪猪周身长满了刺，能保护自己不受天敌的伤害，代表了一种防御机制，这与
hystrix
本身的功能
不谋而合，因此
Netﬂix
团队将该框架命名为
Hystrix
，并使用了对应的卡通形象做作为
logo
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
2.2 
工作原理
 
当对某个服务的调用在一定的时间内
(
默认
10s)
，有超过一定次数
(
默认
20
次
)
并且失败率超过一定值
(
默认
50%)
，
Hystrix
断路器会切换到开路状态
(Open)
，这时所有请求会直接失败而不会发送到后端服务，断
路器保持开路状态一段时间后
(
默认
5
秒
), 
自动切换到半开路状态
(HALF-OPEN)
，这时会判断下一次请求
的返回情况
, 
如果请求成功
, 
断路器切回闭路状态
(CL
OSED), 
否则重新切换到开路状态
(OPEN)
，也就是说
断路器有自我检测并恢复的能力。
 
2.3 
降级回退
 
降级回退指的是某些服务熔断后，执行备用逻辑从故障服务中快速失败或快速返回，以保障主体业务不
受影响。
Hystrix
提供的降级主要是为了容错，保证当前服务不受依赖服务故障的影响，从而提高服务的
健壮性。
fallback
的方式包括：
返回空值。
返回默认值。
访问缓存。
执行某些逻辑。
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
3 
Feign&Hystrix
入门
 
Feign
和
Hystrix
都属于
SpringCloud
的组件，它们两个经常会一起使用。在通过
Feign
组件发起远程调用
时，可以通过
Hystrix
对此次调用实施熔断、降级处理。下面将通过一个例子来演示
Feign 
和
 Hystrix
的
集成方式。
3.1 
父工程
 
创建一个名为
FeignHystrix
的
maven
工程作为父工程，
pom.xm
如下所示：
 
 
 
 
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
m
o
d
e
l
V
e
r
s
i
o
n
>
4
.
0
.
0
<
/
m
o
d
e
l
V
e
r
s
i
o
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
h
y
s
t
r
i
x
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
f
e
i
g
n
-
h
y
s
t
r
i
x
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
p
a
c
k
a
g
i
n
g
>
p
o
m
<
/
p
a
c
k
a
g
i
n
g
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
0
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
m
o
d
u
l
e
s
>
 
 
 
 
 
 
 
 
<
m
o
d
u
l
e
>
d
i
s
c
o
v
e
r
y
-
s
e
r
v
e
r
<
/
m
o
d
u
l
e
>
 
 
 
 
 
 
 
 
<
m
o
d
u
l
e
>
s
e
r
v
i
c
e
-
a
<
/
m
o
d
u
l
e
>
 
 
 
 
 
 
 
 
<
m
o
d
u
l
e
>
s
e
r
v
i
c
e
-
b
<
/
m
o
d
u
l
e
>
 
 
 
 
<
/
m
o
d
u
l
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
3.2 
服务注册中心
 
仍然使用
Eur
eka
作为注册中心，不再多说，自己搭建或直接拿着之前的工程使用即可
3.3 
微服务
B
 
1
. 
创建一个名字为
service-b
的微服务工程，将来被
service-a
服务通过
Feign
进行远程调用
2
. 
引入依赖
3
. 
application.pr
operties
4
. 
启动类
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
p
a
r
e
n
t
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
f
e
i
g
n
-
h
y
s
t
r
i
x
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
h
y
s
t
r
i
x
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
0
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
/
p
a
r
e
n
t
>
 
 
 
 
<
m
o
d
e
l
V
e
r
s
i
o
n
>
4
.
0
.
0
<
/
m
o
d
e
l
V
e
r
s
i
o
n
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
r
v
i
c
e
-
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
-
n
e
t
f
l
i
x
-
e
u
r
e
k
a
-
c
l
i
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
-
o
p
e
n
f
e
i
g
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
-
n
e
t
f
l
i
x
-
h
y
s
t
r
i
x
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
f
e
i
g
n
-
h
y
s
t
r
i
x
-
s
e
r
v
i
c
e
-
b
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
2
2
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
r
v
i
c
e
-
b
e
u
r
e
k
a
.
c
l
i
e
n
t
.
s
e
r
v
i
c
e
U
r
l
.
d
e
f
a
u
l
t
Z
o
n
e
 
=
 
h
t
t
p
:
/
/
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
5
9
0
2
0
/
e
u
r
e
k
a
/
#
 
启
用
h
y
s
t
r
i
x
f
e
i
g
n
.
h
y
s
t
r
i
x
.
e
n
a
b
l
e
d
 
=
 
t
r
u
e
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
5
. 
Contr
oller
 
3.4 
微服务
A
 
1
. 
创建一个名为
service-a
的微服务工程
2
. 
引入依赖
3
. 
application.pr
operties
@
S
p
r
i
n
g
B
o
o
t
A
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
@
E
n
a
b
l
e
F
e
i
g
n
C
l
i
e
n
t
s
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
 
S
e
r
v
i
c
e
B
B
o
o
t
s
t
r
a
p
 
{
 
 
 
 
p
u
b
l
i
c
 
s
t
a
t
i
c
 
v
o
i
d
 
m
a
i
n
(
S
t
r
i
n
g
[
]
 
a
r
g
s
)
 
{
 
 
 
 
 
 
 
 
S
p
r
i
n
g
A
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
r
u
n
(
S
e
r
v
i
c
e
B
B
o
o
t
s
t
r
a
p
.
c
l
a
s
s
,
 
a
r
g
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
 
S
e
r
v
i
c
e
B
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
s
e
r
v
i
c
e
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
 
s
e
r
v
i
c
e
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
S
e
r
v
i
c
e
 
B
 
i
s
 
r
u
n
n
i
n
g
"
;
 
 
 
 
}
}
 
 
 
 
<
p
a
r
e
n
t
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
f
e
i
g
n
-
h
y
s
t
r
i
x
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
h
y
s
t
r
i
x
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
0
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
/
p
a
r
e
n
t
>
 
 
 
 
<
m
o
d
e
l
V
e
r
s
i
o
n
>
4
.
0
.
0
<
/
m
o
d
e
l
V
e
r
s
i
o
n
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
r
v
i
c
e
-
a
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
-
n
e
t
f
l
i
x
-
e
u
r
e
k
a
-
c
l
i
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
-
o
p
e
n
f
e
i
g
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
-
n
e
t
f
l
i
x
-
h
y
s
t
r
i
x
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
4
. 
启动类
5
. 
Feign
代理
@FeignClient
中的
fallbackFactory
对应降级处理工厂，在这里我们实现了
ServiceB
AgentHystrix
，其
中
cr
eate()
方法用于产出一个降级实现对象。而降级实现对象恰恰实现了
Feign
远程代理接口，这样，实
际的远程调用与本地降级方法的参数与返回就保持一致了。
6
. 
Contr
oller
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
f
e
i
g
n
-
h
y
s
t
r
i
x
-
s
e
r
v
i
c
e
-
a
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
2
1
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
r
v
i
c
e
-
a
e
u
r
e
k
a
.
c
l
i
e
n
t
.
s
e
r
v
i
c
e
U
r
l
.
d
e
f
a
u
l
t
Z
o
n
e
 
=
 
h
t
t
p
:
/
/
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
5
9
0
2
0
/
e
u
r
e
k
a
/
#
 
开
启
h
y
s
t
r
i
x
f
e
i
g
n
.
h
y
s
t
r
i
x
.
e
n
a
b
l
e
d
=
t
r
u
e
@
S
p
r
i
n
g
B
o
o
t
A
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
@
E
n
a
b
l
e
F
e
i
g
n
C
l
i
e
n
t
s
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
 
S
e
r
v
i
c
e
A
B
o
o
t
s
t
r
a
p
 
{
 
 
 
 
p
u
b
l
i
c
 
s
t
a
t
i
c
 
v
o
i
d
 
m
a
i
n
(
S
t
r
i
n
g
[
]
 
a
r
g
s
)
 
{
 
 
 
 
 
 
 
 
S
p
r
i
n
g
A
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
r
u
n
(
S
e
r
v
i
c
e
A
B
o
o
t
s
t
r
a
p
.
c
l
a
s
s
,
 
a
r
g
s
)
;
 
 
 
 
}
}
@
F
e
i
g
n
C
l
i
e
n
t
(
n
a
m
e
 
=
 
"
f
e
i
g
n
-
h
y
s
t
r
i
x
-
s
e
r
v
i
c
e
-
b
"
,
f
a
l
l
b
a
c
k
F
a
c
t
o
r
y
 
=
 
S
e
r
v
i
c
e
B
A
g
e
n
t
H
y
s
t
r
i
x
.
c
l
a
s
s
)
p
u
b
l
i
c
 
i
n
t
e
r
f
a
c
e
 
S
e
r
v
i
c
e
B
A
g
e
n
t
 
{
 
 
 
 
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
/
s
e
r
v
i
c
e
-
b
/
s
e
r
v
i
c
e
"
)
 
 
 
 
S
t
r
i
n
g
 
s
e
r
v
i
c
e
(
)
;
}
@
C
o
m
p
o
n
e
n
t
c
l
a
s
s
 
S
e
r
v
i
c
e
B
A
g
e
n
t
H
y
s
t
r
i
x
 
 
i
m
p
l
e
m
e
n
t
s
 
F
a
l
l
b
a
c
k
F
a
c
t
o
r
y
<
S
e
r
v
i
c
e
B
A
g
e
n
t
>
 
{
 
 
 
 
@
O
v
e
r
r
i
d
e
 
 
 
 
p
u
b
l
i
c
 
S
e
r
v
i
c
e
B
A
g
e
n
t
 
c
r
e
a
t
e
(
T
h
r
o
w
a
b
l
e
 
t
h
r
o
w
a
b
l
e
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
r
v
i
c
e
B
A
g
e
n
t
(
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
@
O
v
e
r
r
i
d
e
 
 
 
 
 
 
 
 
 
 
 
 
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
 
s
e
r
v
i
c
e
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
s
e
r
v
i
c
e
-
b
熔
断
.
.
.
"
;
 
 
 
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
}
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
3.5 
功能测试
 
启动所有微服务，通过浏览器访问
http://localhost:59021/service-a/service
，效果如下所示：
故意把微服务
B
关掉，再次访问
http://localhost:59021/service-a/service
，效果如下所示：
 
4 
万信金融
P2P
项目服务熔断
 
在万信金融
P2P
项目中，会有很多地方都需要通过
Hystrix
加入熔断机制，这里只以登录功能为例进行演
示。
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
 
S
e
r
v
i
c
e
A
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
 
S
e
r
v
i
c
e
B
A
g
e
n
t
 
s
e
r
v
i
c
e
B
A
g
e
n
t
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
s
e
r
v
i
c
e
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
 
s
e
r
v
i
c
e
(
)
{
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
s
e
r
v
i
c
e
b
 
=
 
s
e
r
v
i
c
e
B
A
g
e
n
t
.
s
e
r
v
i
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
 
s
e
r
v
i
c
e
b
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
1
. 
在统一账户
(account-service)
和
U
AA
微服务中引入依赖
2
. 
在
Apollo
的
common-template
项目中新建
micr
o_service.feign-hystrix
名称空间，并增加如下
配置：
3
. 
在
Apollo
的其他项目中
(
例如：
account-service
、
uaa...)
去关联
micr
o_service.feign-hystrix
名称
空间
4
. 
在相关微服务的
application.yml
中引入
micr
o_service.feign-hystrix
名称空间
5
. 
修改
U
AA
微服务中的
Feign
代理
(AccountApiAgent.java)
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
-
n
e
t
f
l
i
x
-
h
y
s
t
r
i
x
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
f
e
i
g
n
.
h
y
s
t
r
i
x
.
e
n
a
b
l
e
d
 
=
 
t
r
u
e
@
F
e
i
g
n
C
l
i
e
n
t
(
v
a
l
u
e
 
=
 
"
a
c
c
o
u
n
t
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
f
a
l
l
b
a
c
k
F
a
c
t
o
r
y
 
=
 
A
c
c
o
u
n
t
F
a
l
l
b
a
c
k
F
a
c
t
o
r
y
.
c
l
a
s
s
)
p
u
b
l
i
c
 
i
n
t
e
r
f
a
c
e
 
A
c
c
o
u
n
t
A
p
i
A
g
e
n
t
 
{
 
 
 
 
@
P
o
s
t
M
a
p
p
i
n
g
(
v
a
l
u
e
 
=
 
"
/
a
c
c
o
u
n
t
/
l
/
a
c
c
o
u
n
t
s
/
s
e
s
s
i
o
n
"
)
 
 
 
 
R
e
s
t
R
e
s
p
o
n
s
e
<
A
c
c
o
u
n
t
D
T
O
>
 
l
o
g
i
n
(
@
R
e
q
u
e
s
t
B
o
d
y
 
A
c
c
o
u
n
t
L
o
g
i
n
D
T
O
 
a
c
c
o
u
n
t
L
o
g
i
n
D
T
O
)
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
4
. 
启动相关微服务，进行功能测试
@
C
o
m
p
o
n
e
n
t
@
S
l
f
4
j
c
l
a
s
s
 
A
c
c
o
u
n
t
F
a
l
l
b
a
c
k
F
a
c
t
o
r
y
 
i
m
p
l
e
m
e
n
t
s
 
F
a
l
l
b
a
c
k
F
a
c
t
o
r
y
<
A
c
c
o
u
n
t
A
p
i
A
g
e
n
t
>
 
{
 
 
 
 
@
O
v
e
r
r
i
d
e
 
 
 
 
p
u
b
l
i
c
 
A
c
c
o
u
n
t
A
p
i
A
g
e
n
t
 
c
r
e
a
t
e
(
T
h
r
o
w
a
b
l
e
 
c
a
u
s
e
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
 
A
c
c
o
u
n
t
A
p
i
A
g
e
n
t
(
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
@
O
v
e
r
r
i
d
e
 
 
 
 
 
 
 
 
 
 
 
 
p
u
b
l
i
c
 
R
e
s
t
R
e
s
p
o
n
s
e
<
A
c
c
o
u
n
t
D
T
O
>
 
l
o
g
i
n
(
A
c
c
o
u
n
t
L
o
g
i
n
D
T
O
 
a
c
c
o
u
n
t
L
o
g
i
n
D
T
O
)
{
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
/
/
记
录
错
误
原
因
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
l
o
g
.
i
n
f
o
(
"
f
a
l
l
b
a
c
k
;
 
r
e
a
s
o
n
 
w
a
s
:
"
,
 
c
a
u
s
e
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
/
/
降
级
回
退
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
 
R
e
s
t
R
e
s
p
o
n
s
e
<
>
(
C
o
m
m
o
n
E
r
r
o
r
C
o
d
e
.
E
_
9
9
9
9
9
5
.
g
e
t
C
o
d
e
(
)
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
C
o
m
m
o
n
E
r
r
o
r
C
o
d
e
.
E
_
9
9
9
9
9
5
.
g
e
t
D
e
s
c
(
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
}
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
