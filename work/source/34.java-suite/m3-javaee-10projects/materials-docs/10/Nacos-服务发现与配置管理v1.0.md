# Nacos-服务发现与配置管理v1.0

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\day01 项目介绍 Nacos Spring Cloud Alibaba\讲义-pdf\Nacos-服务发现与配置管理v1.0【海量资源尽在 666java.com】.pdf
- 页数：43
- 抽取：pypdf 文本层



<!-- page 1 -->
N
a
c
o
s
 
-
 
服
务
发
现
和
配
置
管
理
 
教
学
目
标
 
1
）
能
够
理
解
微
服
务
架
构
的
特
点
2
）
能
够
理
解
服
务
发
现
的
流
程
3
）
能
够
说
出
N
a
c
o
s
的
功
能
4
）
掌
握
N
a
c
o
s
的
安
装
方
法
5
）
掌
握
R
E
S
T
f
u
l
服
务
发
现
开
发
方
法
6
）
掌
握
D
u
b
b
o
服
务
发
现
开
发
方
法
7
）
理
解
N
a
c
o
s
服
务
发
现
的
数
据
模
型
8
）
能
够
掌
握
N
a
c
o
s
配
置
管
理
方
法
9
）
掌
握
N
a
c
o
s
扩
展
配
置
方
法
 
1
 
理
解
服
务
发
现
 
1
.
1
 
微
服
务
架
构
 
 
 
为
适
应
企
业
的
业
务
发
展
，
提
高
软
件
研
发
的
生
产
力
，
降
低
软
件
研
发
的
成
本
，
软
件
架
构
也
作
了
升
级
和
优
化
，
将
一
个
独
立
的
系
统
拆
分
成
若
干
小
的
服
务
，
每
个
小
服
务
运
行
在
不
同
的
进
程
中
，
服
务
与
服
务
之
间
采
用
R
E
S
T
f
u
l
、
R
P
C
等
协
议
传
输
数
据
，
每
个
服
务
所
拥
有
的
功
能
具
有
独
立
性
强
的
特
点
，
这
样
的
设
计
就
实
现
了
单
个
服
务
的
高
内
聚
，
服
务
与
服
务
之
间
的
低
耦
合
效
果
，
这
些
小
服
务
就
是
微
服
务
，
基
于
这
种
方
法
设
计
的
系
统
架
构
即
微
服
务
架
构
。
下
图
是
基
于
微
服
务
架
构
的
电
商
系
统
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
特
点
：
1
、
服
务
层
按
业
务
拆
分
为
一
个
一
个
的
微
服
务
。
2
、
微
服
务
的
职
责
单
一
。
3
、
微
服
务
之
间
采
用
R
E
S
T
f
u
l
、
R
P
C
等
轻
量
级
协
议
传
输
。
4
、
有
利
于
采
用
前
后
端
分
离
架
构
。
 
1
.
2
 
理
解
服
务
发
现
 
1
.
2
.
1
 
测
试
环
境
 
 
 
在
微
服
务
架
构
中
，
整
个
系
统
会
按
职
责
能
力
划
分
为
多
个
服
务
，
通
过
服
务
之
间
协
作
来
实
现
业
务
目
标
。
这
样
在
我
们
的
代
码
中
免
不
了
要
进
行
服
务
间
的
远
程
调
用
，
服
务
的
消
费
方
要
调
用
服
务
的
生
产
方
，
为
了
完
成
一
次
请
求
，
消
费
方
需
要
知
道
服
务
生
产
方
的
网
络
位
置
(
I
P
地
址
和
端
口
号
)
。
 
 
我
们
的
代
码
可
以
通
过
读
取
配
置
文
件
的
方
式
读
取
服
务
生
产
方
网
络
位
置
，
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
我
们
通
过
S
p
r
i
n
g
 
b
o
o
t
技
术
很
容
易
实
现
：
1
、
创
建
n
a
c
o
s
-
d
i
s
c
o
v
e
r
y
父
工
程
p
o
m
.
x
m
l
如
下
：
 
2
、
S
e
r
v
i
c
e
 
B
（
服
务
生
产
者
）
创
建
服
务
提
供
者
 
n
a
c
o
s
-
r
e
s
t
f
u
l
-
p
r
o
v
i
d
e
r
。
p
o
m
.
x
m
l
如
下
：
 
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
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
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
0
‐
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
‐
b
o
o
t
‐
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
/
p
r
o
j
e
c
t
>
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
S
e
r
v
i
c
e
 
B
是
服
务
的
生
产
方
，
暴
露
/
s
e
r
v
i
c
e
服
务
地
址
，
实
现
代
码
如
下
：
1
、
创
建
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
 
2
、
创
建
启
动
类
 
配
置
文
件
：
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
n
a
c
o
s
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
‐
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
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
p
r
o
v
i
d
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
‐
b
o
o
t
‐
s
t
a
r
t
e
r
‐
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
p
r
o
j
e
c
t
>
p
a
c
k
a
g
e
 
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
n
a
c
o
s
.
p
r
o
v
i
d
e
r
.
c
o
n
t
r
o
l
l
e
r
;
 
i
m
p
o
r
t
 
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
w
e
b
.
b
i
n
d
.
a
n
n
o
t
a
t
i
o
n
.
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
;
i
m
p
o
r
t
 
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
w
e
b
.
b
i
n
d
.
a
n
n
o
t
a
t
i
o
n
.
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
;
 
 
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
 
R
e
s
t
P
r
o
v
i
d
e
r
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
v
a
l
u
e
 
=
 
"
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
 
/
/
暴
露
服
务
 
 
 
 
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
y
s
t
e
m
.
o
u
t
.
p
r
i
n
t
l
n
(
"
p
r
o
v
i
d
e
r
 
i
n
v
o
k
e
"
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
p
r
o
v
i
d
e
r
 
i
n
v
o
k
e
"
;
 
 
 
 
}
}
 
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
p
r
i
n
g
R
e
s
t
P
r
o
v
i
d
e
r
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
p
r
i
n
g
R
e
s
t
P
r
o
v
i
d
e
r
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
创
建
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
y
m
l
，
内
容
如
下
：
 
3
、
S
e
r
v
i
c
e
 
A
（
服
务
消
费
者
）
创
建
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
 
服
务
消
费
工
程
。
p
o
m
.
x
m
l
如
下
：
 
实
现
代
码
：
1
、
创
建
c
o
n
t
r
o
l
l
e
r
 
s
e
r
v
e
r
：
p
o
r
t
：
5
6
0
1
0
 
 
 
 
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
n
a
c
o
s
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
‐
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
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
c
o
n
s
u
m
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
‐
b
o
o
t
‐
s
t
a
r
t
e
r
‐
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
p
r
o
j
e
c
t
>
p
a
c
k
a
g
e
 
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
n
a
c
o
s
.
c
o
n
s
u
m
e
r
.
c
o
n
t
r
o
l
l
e
r
;
 
i
m
p
o
r
t
 
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
e
a
n
s
.
f
a
c
t
o
r
y
.
a
n
n
o
t
a
t
i
o
n
.
A
u
t
o
w
i
r
e
d
;
i
m
p
o
r
t
 
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
e
a
n
s
.
f
a
c
t
o
r
y
.
a
n
n
o
t
a
t
i
o
n
.
V
a
l
u
e
;
i
m
p
o
r
t
 
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
w
e
b
.
b
i
n
d
.
a
n
n
o
t
a
t
i
o
n
.
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
;
i
m
p
o
r
t
 
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
w
e
b
.
b
i
n
d
.
a
n
n
o
t
a
t
i
o
n
.
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
;
i
m
p
o
r
t
 
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
w
e
b
.
c
l
i
e
n
t
.
R
e
s
t
T
e
m
p
l
a
t
e
;
 
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
 
R
e
s
t
C
o
n
s
u
m
e
r
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
V
a
l
u
e
(
"
$
{
p
r
o
v
i
d
e
r
.
a
d
d
r
e
s
s
}
"
)
 
 
 
 
p
r
i
v
a
t
e
 
S
t
r
i
n
g
 
p
r
o
v
i
d
e
r
A
d
d
r
e
s
s
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
v
a
l
u
e
 
=
 
"
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
2
、
创
建
启
动
类
 
配
置
文
件
：
创
建
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
y
m
l
，
内
容
如
下
：
 
访
问
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
5
6
0
2
0
/
s
e
r
v
i
c
e
，
输
出
以
下
内
容
：
 
1
.
2
.
2
 
服
务
发
现
流
程
 
 
 
上
边
的
例
子
看
上
去
很
完
美
，
但
是
，
仔
细
考
虑
以
下
，
此
方
案
对
于
微
服
务
应
用
而
言
行
不
通
。
首
先
，
微
服
务
可
能
是
部
署
在
云
环
境
的
，
服
务
实
例
的
网
络
位
置
或
许
是
动
态
分
配
的
。
另
外
，
每
一
个
服
务
一
般
会
有
多
个
实
例
来
做
负
载
均
衡
，
由
于
宕
机
或
升
级
，
服
务
实
例
网
络
地
址
会
经
常
动
态
改
变
。
再
者
，
每
一
个
服
务
也
可
能
应
对
临
时
访
问
压
力
增
加
新
的
服
务
节
点
。
正
如
下
图
所
示
：
 
 
 
 
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
 
 
 
 
 
 
 
 
R
e
s
t
T
e
m
p
l
a
t
e
 
r
e
s
t
T
e
m
p
l
a
t
e
 
=
 
n
e
w
 
R
e
s
t
T
e
m
p
l
a
t
e
(
)
;
 
 
 
 
 
 
 
 
/
/
调
用
服
务
S
t
r
i
n
g
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
 
=
 
r
e
s
t
T
e
m
p
l
a
t
e
.
g
e
t
F
o
r
O
b
j
e
c
t
(
"
h
t
t
p
:
/
/
"
 
+
 
p
r
o
v
i
d
e
r
A
d
d
r
e
s
s
 
+
 
"
/
s
e
r
v
i
c
e
"
,
S
t
r
i
n
g
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
c
o
n
s
u
m
e
r
 
i
n
v
o
k
e
 
|
 
"
 
+
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
;
 
 
 
 
}
 
 
}
 
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
p
r
i
n
g
R
e
s
t
C
o
n
s
u
m
e
r
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
p
r
i
n
g
R
e
s
t
C
o
n
s
u
m
e
r
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
6
0
2
0
#
 
服
务
生
产
方
地
址
p
r
o
v
i
d
e
r
.
a
d
d
r
e
s
s
 
=
 
1
2
7
.
0
.
0
.
1
:
5
6
0
1
0
 
c
o
n
s
u
m
e
r
 
i
n
v
o
k
e
 
|
 
p
r
o
v
i
d
e
r
 
i
n
v
o
k
e
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
基
于
以
上
的
问
题
，
服
务
之
间
如
何
相
互
发
现
？
服
务
如
何
管
理
？
这
就
是
服
务
发
现
的
问
题
了
。
 
 
服
务
发
现
就
是
服
务
消
费
方
通
过
服
务
发
现
中
心
智
能
发
现
服
务
提
供
方
，
从
而
进
行
远
程
调
用
的
过
程
。
 
 
如
下
图
：
 
 
 
上
图
中
服
务
实
例
本
身
并
不
记
录
服
务
生
产
方
的
网
络
地
址
，
所
有
服
务
实
例
内
部
都
会
包
含
服
务
发
现
客
户
端
。
 
 
（
1
）
在
每
个
服
务
启
动
时
会
向
服
务
发
现
中
心
上
报
自
己
的
网
络
位
置
。
这
样
，
在
服
务
发
现
中
心
内
部
会
形
成
一
个
服
务
注
册
表
，
服
务
注
册
表
是
服
务
发
现
的
核
心
部
分
，
是
包
含
所
有
服
务
实
例
的
网
络
地
址
的
数
据
库
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
对
比
项
目
N
a
c
o
s
E
u
r
e
k
a
C
o
n
s
u
l
Z
o
o
k
e
e
p
e
r
一
致
性
协
议
支
持
A
P
和
C
P
模
型
A
P
模
型
C
P
模
型
C
P
模
型
健
康
检
查
T
C
P
/
H
T
T
P
/
M
Y
S
Q
L
/
C
l
i
e
n
t
 
B
e
a
t
C
l
i
e
n
t
 
B
e
a
t
T
C
P
/
H
T
T
P
/
g
R
P
C
/
C
m
d
K
e
e
p
 
A
l
i
v
e
负
载
均
衡
策
略
权
重
/
m
e
t
a
d
a
t
a
/
S
e
l
e
c
t
o
r
R
i
b
b
o
n
F
a
b
i
o
-
雪
崩
保
护
有
有
无
无
自
动
注
销
实
例
支
持
支
持
不
支
持
支
持
访
问
协
议
H
T
T
P
/
D
N
S
H
T
T
P
H
T
T
P
/
D
N
S
T
C
P
监
听
支
持
支
持
支
持
支
持
支
持
多
数
据
中
心
支
持
支
持
支
持
不
支
持
跨
注
册
中
心
同
步
支
持
不
支
持
支
持
不
支
持
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
集
成
支
持
支
持
支
持
不
支
持
D
u
b
b
o
集
成
支
持
不
支
持
不
支
持
支
持
k
8
s
集
成
支
持
不
支
持
支
持
不
支
持
 
 
（
2
）
服
务
发
现
客
户
端
会
定
期
从
服
务
发
现
中
心
同
步
服
务
注
册
表
 
，
并
缓
存
在
客
户
端
。
 
 
（
3
）
当
需
要
对
某
服
务
进
行
请
求
时
，
服
务
实
例
通
过
该
注
册
表
，
定
位
目
标
服
务
网
络
地
址
。
若
目
标
服
务
存
在
多
个
网
络
地
址
，
则
使
用
负
载
均
衡
算
法
从
多
个
服
务
实
例
中
选
择
出
一
个
，
然
后
发
出
请
求
。
 
 
总
结
，
在
微
服
务
环
境
中
，
由
于
服
务
运
行
实
例
的
网
络
地
址
是
不
断
动
态
变
化
的
，
服
务
实
例
数
量
的
动
态
变
化
 
，
因
此
无
法
使
用
固
定
的
配
置
文
件
来
记
录
服
务
提
供
方
的
网
络
地
址
，
必
须
使
用
动
态
的
服
务
发
现
机
制
用
于
实
现
微
服
务
间
的
相
互
感
知
。
各
服
务
实
例
会
上
报
自
己
的
网
络
地
址
，
这
样
服
务
中
心
就
形
成
了
一
个
完
整
的
服
务
注
册
表
，
各
服
务
实
例
会
通
过
服
务
发
现
中
心
来
获
取
访
问
目
标
服
务
的
网
络
地
址
，
从
而
实
现
服
务
发
现
的
机
制
。
 
2
 
N
a
c
o
s
 
服
务
发
现
 
2
.
1
 
N
a
c
o
s
简
介
 
2
.
1
.
1
 
服
务
发
现
产
品
对
比
 
目
前
市
面
上
用
的
比
较
多
的
服
务
发
现
中
心
有
：
N
a
c
o
s
、
E
u
r
e
k
a
、
C
o
n
s
u
l
和
Z
o
o
k
e
e
p
e
r
。
 
 
从
上
面
对
比
可
以
了
解
到
，
N
a
c
o
s
作
为
服
务
发
现
中
心
，
具
备
更
多
的
功
能
支
持
项
，
且
从
长
远
来
看
N
a
c
o
s
在
以
后
的
版
本
会
支
持
S
p
r
i
n
g
C
L
o
u
d
+
K
u
b
e
r
n
e
t
e
s
的
组
合
，
填
补
 
2
 
者
的
鸿
沟
，
在
两
套
体
系
下
可
以
采
用
同
一
套
服
务
发
现
和
配
置
管
理
的
解
决
方
案
，
这
将
大
大
的
简
化
使
用
和
维
护
的
成
本
。
另
外
，
N
a
c
o
s
 
计
划
实
现
 
S
e
r
v
i
c
e
 
M
e
s
h
，
也
是
未
来
微
服
务
发
展
的
趋
势
。
 
2
.
1
.
2
 
N
a
c
o
s
简
介
 
N
a
c
o
s
是
阿
里
的
一
个
开
源
产
品
，
它
是
针
对
微
服
务
架
构
中
的
服
务
发
现
、
配
置
管
理
、
服
务
治
理
的
综
合
型
解
决
方
案
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
官
方
介
绍
是
这
样
的
：
N
a
c
o
s
 
致
力
于
帮
助
您
发
现
、
配
置
和
管
理
微
服
务
。
N
a
c
o
s
 
提
供
了
一
组
简
单
易
用
的
特
性
集
，
帮
助
您
实
现
动
态
服
务
发
现
、
服
务
配
置
管
理
、
服
务
及
流
量
管
理
。
 
N
a
c
o
s
 
帮
助
您
更
敏
捷
和
容
易
地
构
建
、
交
付
和
管
理
微
服
务
平
台
。
N
a
c
o
s
 
是
构
建
以
“
服
务
”
为
中
心
的
现
代
应
用
架
构
的
服
务
基
础
设
施
。
官
网
地
址
：
h
t
t
p
s
:
/
/
n
a
c
o
s
.
i
o
2
.
1
.
3
 
N
a
c
o
s
特
性
 
N
a
c
o
s
主
要
提
供
以
下
四
大
功
能
：
1
.
 
服
务
发
现
与
服
务
健
康
检
查
N
a
c
o
s
使
服
务
更
容
易
注
册
，
并
通
过
D
N
S
或
H
T
T
P
接
口
发
现
其
他
服
务
，
N
a
c
o
s
还
提
供
服
务
的
实
时
健
康
检
查
，
以
防
止
向
不
健
康
的
主
机
或
服
务
实
例
发
送
请
求
。
2
.
 
动
态
配
置
管
理
动
态
配
置
服
务
允
许
您
在
所
有
环
境
中
以
集
中
和
动
态
的
方
式
管
理
所
有
服
务
的
配
置
。
N
a
c
o
s
消
除
了
在
更
新
配
置
时
重
新
部
署
应
用
程
序
，
这
使
配
置
的
更
改
更
加
高
效
和
灵
活
。
3
.
 
动
态
D
N
S
服
务
N
a
c
o
s
提
供
基
于
D
N
S
 
协
议
的
服
务
发
现
能
力
，
旨
在
支
持
异
构
语
言
的
服
务
发
现
，
支
持
将
注
册
在
N
a
c
o
s
上
的
服
务
以
域
名
的
方
式
暴
露
端
点
，
让
三
方
应
用
方
便
的
查
阅
及
发
现
。
4
.
 
服
务
和
元
数
据
管
理
N
a
c
o
s
 
能
让
您
从
微
服
务
平
台
建
设
的
视
角
管
理
数
据
中
心
的
所
有
服
务
及
元
数
据
，
包
括
管
理
服
务
的
描
述
、
生
命
周
期
、
服
务
的
静
态
依
赖
分
析
、
服
务
的
健
康
状
态
、
服
务
的
流
量
管
理
、
路
由
及
安
全
策
略
。
这
里
1
、
3
、
4
说
明
了
服
务
发
现
的
功
能
特
性
。
2
.
2
 
安
装
N
a
c
o
s
 
S
e
r
v
e
r
 
2
.
2
.
1
 
预
备
环
境
准
备
 
N
a
c
o
s
 
依
赖
 
J
a
v
a
 
环
境
来
运
行
。
如
果
您
是
从
代
码
开
始
构
建
并
运
行
N
a
c
o
s
，
还
需
要
为
此
配
置
 
M
a
v
e
n
环
境
，
请
确
保
是
在
以
下
版
本
环
境
中
安
装
使
用
:
1
.
 
6
4
 
b
i
t
 
O
S
，
支
持
 
L
i
n
u
x
/
U
n
i
x
/
M
a
c
/
W
i
n
d
o
w
s
，
推
荐
选
用
 
L
i
n
u
x
/
U
n
i
x
/
M
a
c
。
2
.
 
6
4
 
b
i
t
 
J
D
K
 
1
.
8
+
；
下
载
 
&
 
配
置
。
3
.
 
M
a
v
e
n
 
3
.
2
.
x
+
；
下
载
 
&
 
配
置
。
2
.
2
.
2
 
下
载
源
码
或
者
安
装
包
 
你
可
以
通
过
源
码
和
发
行
包
两
种
方
式
来
获
取
 
N
a
c
o
s
。
从
 
G
i
t
h
u
b
 
上
下
载
源
码
方
式
 
g
i
t
 
c
l
o
n
e
 
h
t
t
p
s
:
/
/
g
i
t
h
u
b
.
c
o
m
/
a
l
i
b
a
b
a
/
n
a
c
o
s
.
g
i
t
c
d
 
n
a
c
o
s
/
m
v
n
 
‐
P
r
e
l
e
a
s
e
‐
n
a
c
o
s
 
c
l
e
a
n
 
i
n
s
t
a
l
l
 
‐
U
 
 
l
s
 
‐
a
l
 
d
i
s
t
r
i
b
u
t
i
o
n
/
t
a
r
g
e
t
/
 
/
/
 
c
h
a
n
g
e
 
t
h
e
 
$
v
e
r
s
i
o
n
 
t
o
 
y
o
u
r
 
a
c
t
u
a
l
 
p
a
t
h
c
d
 
d
i
s
t
r
i
b
u
t
i
o
n
/
t
a
r
g
e
t
/
n
a
c
o
s
‐
s
e
r
v
e
r
‐
$
v
e
r
s
i
o
n
/
n
a
c
o
s
/
b
i
n
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
下
载
编
译
后
压
缩
包
方
式
您
可
以
从
 
最
新
稳
定
版
本
 
下
载
 
n
a
c
o
s
-
s
e
r
v
e
r
-
$
v
e
r
s
i
o
n
.
z
i
p
 
包
，
本
教
程
使
用
n
a
c
o
s
-
s
e
r
v
e
r
-
1
.
1
.
3
版
本
。
下
载
地
址
：
h
t
t
p
s
:
/
/
g
i
t
h
u
b
.
c
o
m
/
a
l
i
b
a
b
a
/
n
a
c
o
s
/
r
e
l
e
a
s
e
s
下
载
后
解
压
：
 
2
.
2
.
3
 
启
动
服
务
器
 
n
a
c
o
s
的
默
认
端
口
是
8
8
4
8
，
需
要
保
证
8
8
4
8
默
认
端
口
没
有
被
其
他
进
程
占
用
。
进
入
安
装
程
序
的
b
i
n
目
录
：
L
i
n
u
x
/
U
n
i
x
/
M
a
c
启
动
方
式
：
启
动
命
令
(
s
t
a
n
d
a
l
o
n
e
代
表
着
单
机
模
式
运
行
，
非
集
群
模
式
)
:
s
h
 
s
t
a
r
t
u
p
.
s
h
 
-
m
 
s
t
a
n
d
a
l
o
n
e
如
果
您
使
用
的
是
u
b
u
n
t
u
系
统
，
或
者
运
行
脚
本
报
错
提
示
[
[
符
号
找
不
到
，
可
尝
试
如
下
运
行
：
b
a
s
h
 
s
t
a
r
t
u
p
.
s
h
 
-
m
 
s
t
a
n
d
a
l
o
n
e
W
i
n
d
o
w
s
启
动
方
式
：
启
动
命
令
：
c
m
d
 
s
t
a
r
t
u
p
.
c
m
d
或
者
双
击
s
t
a
r
t
u
p
.
c
m
d
运
行
文
件
。
 
启
动
成
功
，
可
通
过
浏
览
器
访
问
 
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
8
8
4
8
/
n
a
c
o
s
 
，
打
开
如
下
n
a
c
o
s
控
制
台
登
录
页
面
：
使
用
默
认
用
户
名
：
n
a
c
o
s
，
默
认
密
码
：
n
a
c
o
s
 
登
录
即
可
打
开
主
页
面
。
 
 
u
n
z
i
p
 
n
a
c
o
s
‐
s
e
r
v
e
r
‐
$
v
e
r
s
i
o
n
.
z
i
p
 
或
者
 
t
a
r
 
‐
x
v
f
 
n
a
c
o
s
‐
s
e
r
v
e
r
‐
$
v
e
r
s
i
o
n
.
t
a
r
.
g
z
 
 
c
d
 
n
a
c
o
s
/
b
i
n
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
2
.
2
.
4
 
外
部
m
y
s
q
l
数
据
库
支
持
 
 
 
单
机
模
式
时
n
a
c
o
s
默
认
使
用
嵌
入
式
数
据
库
实
现
数
据
的
存
储
，
若
想
使
用
外
部
m
y
s
q
l
存
储
n
a
c
o
s
数
据
，
需
要
进
行
以
下
步
骤
：
1
.
安
装
数
据
库
，
版
本
要
求
：
5
.
6
.
5
+
 
，
m
y
s
q
l
 
8
 
以
下
2
.
初
始
化
m
y
s
q
l
数
据
库
，
新
建
数
据
库
n
a
c
o
s
_
c
o
n
ﬁ
g
，
数
据
库
初
始
化
文
件
：
$
{
n
a
c
o
s
h
o
m
e
}
/
c
o
n
f
/
n
a
c
o
s
-
m
y
s
q
l
.
s
q
l
3
.
修
改
$
{
n
a
c
o
s
h
o
m
e
}
/
c
o
n
f
/
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
文
件
，
增
加
支
持
m
y
s
q
l
数
据
源
配
置
（
目
前
只
支
持
m
y
s
q
l
）
，
添
加
m
y
s
q
l
数
据
源
的
u
r
l
、
用
户
名
和
密
码
。
 
2
.
3
 
R
E
S
T
f
u
l
服
务
发
现
 
2
.
3
.
1
 
测
试
环
境
 
 
 
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
是
一
套
微
服
务
开
发
框
架
集
合
，
包
括
微
服
务
开
发
的
方
方
页
面
，
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
是
一
套
微
服
务
开
发
的
标
准
，
集
成
了
很
多
优
秀
的
开
源
框
架
，
比
如
有
名
的
N
e
t
ﬂ
i
x
公
司
的
众
多
项
目
。
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
 
项
目
地
址
：
h
t
t
p
s
:
/
/
s
p
r
i
n
g
.
i
o
/
p
r
o
j
e
c
t
s
/
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
 
 
本
测
试
环
境
采
用
阿
里
开
源
的
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
 
A
l
i
b
a
b
a
微
服
务
开
发
框
架
，
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
 
A
l
i
b
a
b
a
是
阿
里
巴
巴
公
司
基
于
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
标
准
实
现
一
套
微
服
务
开
发
框
架
集
合
，
它
和
N
e
t
ﬂ
i
x
一
样
都
是
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
微
服
务
开
发
实
现
方
案
。
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
 
A
l
i
b
a
b
a
项
目
地
址
：
h
t
t
p
s
:
/
/
g
i
t
h
u
b
.
c
o
m
/
a
l
i
b
a
b
a
/
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
a
l
i
b
a
b
a
通
过
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
 
A
l
i
b
a
b
a
实
现
解
决
：
1
、
服
务
发
现
客
户
端
从
服
务
发
现
中
心
获
取
服
务
列
表
2
、
服
务
消
费
方
通
过
负
载
均
衡
获
取
服
务
地
址
 
在
n
a
c
o
s
-
d
i
s
c
o
v
e
r
y
父
工
程
中
添
加
依
赖
管
理
s
p
r
i
n
g
.
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
.
p
l
a
t
f
o
r
m
=
m
y
s
q
l
 
d
b
.
n
u
m
=
1
d
b
.
u
r
l
.
0
=
j
d
b
c
:
m
y
s
q
l
:
/
/
1
1
.
1
6
2
.
1
9
6
.
1
6
:
3
3
0
6
/
n
a
c
o
s
_
c
o
n
f
i
g
?
c
h
a
r
a
c
t
e
r
E
n
c
o
d
i
n
g
=
u
t
f
8
&
c
o
n
n
e
c
t
T
i
m
e
o
u
t
=
1
0
0
0
&
s
o
c
k
e
t
T
i
m
e
o
u
t
=
3
0
0
0
&
a
u
t
o
R
e
c
o
n
n
e
c
t
=
t
r
u
e
d
b
.
u
s
e
r
=
n
a
c
o
s
_
d
e
v
t
e
s
t
d
b
.
p
a
s
s
w
o
r
d
=
y
o
u
d
o
n
t
k
n
o
w
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
分
别
在
服
务
提
供
及
服
务
消
费
工
程
中
添
加
依
赖
，
此
依
赖
的
作
用
是
服
务
发
现
 
2
.
3
.
2
 
服
务
注
册
 
在
服
务
提
供
工
程
中
配
置
n
a
c
o
s
服
务
发
现
相
关
的
配
置
：
服
务
提
供
：
 
启
动
n
a
c
o
s
启
动
服
务
提
供
观
察
n
a
c
o
s
服
务
列
表
，
n
a
c
o
s
-
r
e
s
t
f
u
l
-
p
r
o
v
i
d
e
r
注
册
成
功
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
‐
b
o
o
t
‐
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
‐
c
l
o
u
d
‐
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
‐
c
l
o
u
d
‐
a
l
i
b
a
b
a
‐
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
a
l
i
b
a
b
a
‐
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
s
p
r
i
n
g
:
 
 
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
:
 
 
 
 
n
a
m
e
:
 
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
p
r
o
v
i
d
e
r
 
 
c
l
o
u
d
:
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
d
i
s
c
o
v
e
r
y
:
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
服
务
名
称
：
每
个
服
务
在
服
务
注
册
中
心
的
标
识
，
相
当
于
J
a
v
a
中
的
类
名
。
服
务
实
例
：
网
络
中
提
供
服
务
的
实
例
，
具
有
I
P
和
端
口
，
相
当
于
J
a
v
a
中
的
对
象
，
一
个
实
例
即
为
运
行
在
服
务
器
上
的
一
个
进
程
。
2
.
3
.
3
 
服
务
发
现
 
在
服
务
消
费
工
程
中
配
置
n
a
c
o
s
服
务
发
现
相
关
的
配
置
：
服
务
消
费
：
 
修
改
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
中
远
程
调
用
的
代
码
：
 
执
行
流
程
：
1
、
服
务
提
供
方
将
自
己
注
册
到
服
务
注
册
中
心
2
、
服
务
消
费
方
从
注
册
中
心
获
取
服
务
地
址
s
p
r
i
n
g
:
 
 
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
:
 
 
 
 
n
a
m
e
:
 
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
c
o
n
s
u
m
e
r
 
 
c
l
o
u
d
:
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
d
i
s
c
o
v
e
r
y
:
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
/
/
服
务
i
d
即
注
册
中
心
的
中
的
服
务
名
 
 
 
 
 
 
 
 
p
r
i
v
a
t
e
 
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
I
d
=
"
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
p
r
o
v
i
d
e
r
"
;
 
 
 
 
 
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
 
 
 
 
L
o
a
d
B
a
l
a
n
c
e
r
C
l
i
e
n
t
 
l
o
a
d
B
a
l
a
n
c
e
r
C
l
i
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
v
a
l
u
e
 
=
 
"
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
 
 
 
 
 
 
 
 
R
e
s
t
T
e
m
p
l
a
t
e
 
r
e
s
t
T
e
m
p
l
a
t
e
 
=
 
n
e
w
 
R
e
s
t
T
e
m
p
l
a
t
e
(
)
;
 
 
 
 
 
 
 
 
/
/
调
用
服
务
/
/
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
 
=
 
r
e
s
t
T
e
m
p
l
a
t
e
.
g
e
t
F
o
r
O
b
j
e
c
t
(
"
h
t
t
p
:
/
/
"
 
+
 
p
r
o
v
i
d
e
r
A
d
d
r
e
s
s
 
+
 
"
/
s
e
r
v
i
c
e
"
,
S
t
r
i
n
g
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
 
S
e
r
v
i
c
e
I
n
s
t
a
n
c
e
 
s
e
r
v
i
c
e
I
n
s
t
a
n
c
e
 
=
 
l
o
a
d
B
a
l
a
n
c
e
r
C
l
i
e
n
t
.
c
h
o
o
s
e
(
s
e
r
v
i
c
e
I
d
)
;
 
 
 
 
 
 
 
 
U
R
I
 
u
r
i
 
=
 
s
e
r
v
i
c
e
I
n
s
t
a
n
c
e
.
g
e
t
U
r
i
(
)
;
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
 
=
 
r
e
s
t
T
e
m
p
l
a
t
e
.
g
e
t
F
o
r
O
b
j
e
c
t
(
u
r
i
+
"
/
s
e
r
v
i
c
e
"
,
S
t
r
i
n
g
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
c
o
n
s
u
m
e
r
 
i
n
v
o
k
e
 
|
 
"
 
+
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
;
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 14 -->
3
、
进
行
远
程
调
用
2
.
3
.
4
 
负
载
均
衡
 
 
 
在
R
E
S
T
f
u
l
服
务
发
现
的
流
程
中
，
S
e
r
v
i
c
e
A
通
过
负
载
均
衡
调
用
S
e
r
v
i
c
e
B
，
下
边
来
了
解
一
下
负
载
均
衡
：
 
 
负
载
均
衡
就
是
将
用
户
请
求
（
流
量
）
通
过
一
定
的
策
略
，
分
摊
在
多
个
服
务
实
例
上
执
行
，
它
是
系
统
处
理
高
并
发
、
缓
解
网
络
压
力
和
进
行
服
务
端
扩
容
的
重
要
手
段
之
一
。
它
分
为
服
务
端
负
载
均
衡
和
客
户
端
负
载
均
衡
。
 
 
服
务
器
端
负
载
均
衡
：
 
 
在
负
载
均
衡
器
中
维
护
一
个
可
用
的
服
务
实
例
清
单
，
当
客
户
端
请
求
来
临
时
，
负
载
均
衡
服
务
器
按
照
某
种
配
置
好
的
规
则
(
负
载
均
衡
算
法
)
从
可
用
服
务
实
例
清
单
中
选
取
其
一
去
处
理
客
户
端
的
请
求
。
这
就
是
服
务
端
负
载
均
衡
。
例
如
N
g
i
n
x
，
通
过
N
g
i
n
x
进
行
负
载
均
衡
，
客
户
端
发
送
请
求
至
N
g
i
n
x
，
N
g
i
n
x
通
过
负
载
均
衡
算
法
，
在
多
个
服
务
器
之
间
选
择
一
个
进
行
访
问
。
即
在
服
务
器
端
再
进
行
负
载
均
衡
算
法
分
配
。
客
户
端
服
务
负
载
均
衡
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 15 -->
上
边
使
用
的
L
o
a
d
B
a
l
a
n
c
e
r
C
l
i
e
n
t
就
是
一
个
客
户
端
负
载
均
衡
器
，
具
体
使
用
的
是
R
i
b
b
o
n
客
户
端
负
载
均
衡
器
。
R
i
b
b
o
n
在
发
送
请
求
前
通
过
负
载
均
衡
算
法
选
择
一
个
服
务
实
例
，
然
后
进
行
访
问
，
这
是
客
户
端
负
载
均
衡
。
即
在
客
户
端
就
进
行
负
载
均
衡
的
分
配
。
 
 
R
i
b
b
o
n
是
一
个
客
户
端
负
载
均
衡
器
，
它
的
责
任
是
从
一
组
实
例
列
表
中
挑
选
合
适
的
实
例
，
如
何
挑
选
？
取
决
于
负
载
均
衡
策
略
 
。
R
i
b
b
o
n
核
心
组
件
I
R
u
l
e
是
负
载
均
衡
策
略
接
口
，
它
有
如
下
实
现
，
大
家
仅
做
了
解
：
R
o
u
n
d
R
o
b
i
n
R
u
l
e
(
默
认
)
:
轮
询
，
即
按
一
定
的
顺
序
轮
换
获
取
实
例
的
地
址
。
R
a
n
d
o
m
R
u
l
e
:
随
机
，
即
以
随
机
的
方
式
获
取
实
例
的
地
址
。
A
v
a
i
l
a
b
i
l
i
t
y
F
i
l
t
e
r
i
n
g
R
u
l
e
:
 
会
先
过
滤
掉
由
于
多
次
访
问
故
障
而
处
于
断
路
器
跳
闸
状
态
的
服
务
,
以
及
并
发
的
连
接
数
量
超
过
阈
值
的
服
务
,
然
后
对
剩
余
的
服
务
列
表
按
照
轮
询
策
略
进
行
访
问
;
W
e
i
g
h
t
e
d
R
e
s
p
o
n
s
e
T
i
m
e
R
u
l
e
:
 
根
据
平
均
响
应
时
间
计
算
所
有
服
务
的
权
重
,
响
应
时
间
越
快
,
服
务
权
重
越
大
,
被
选
中
的
机
率
越
高
;
 
刚
启
动
时
,
如
果
统
计
信
息
不
足
,
则
使
用
R
o
u
n
d
R
o
b
i
n
R
u
l
e
策
略
,
等
统
计
信
息
足
够
时
,
会
切
换
到
W
e
i
g
h
t
e
d
R
e
s
p
o
n
s
e
T
i
m
e
R
u
l
e
R
e
t
r
y
R
u
l
e
:
 
先
按
照
R
o
u
n
d
R
o
b
i
n
R
u
l
e
的
策
略
获
取
服
务
,
如
果
获
取
服
务
失
败
,
则
在
指
定
时
间
内
会
进
行
重
试
,
获
取
可
用
的
服
务
;
B
e
s
t
A
v
a
i
l
a
b
l
e
R
u
l
e
:
 
会
先
过
滤
掉
由
于
多
次
访
问
故
障
而
处
于
断
路
器
跳
闸
状
态
的
服
务
,
然
后
选
择
一
个
并
发
量
最
小
的
服
务
;
Z
o
n
e
A
v
o
i
d
a
n
c
e
R
u
l
e
:
 
默
认
规
则
,
复
合
判
断
s
e
r
v
e
r
所
在
区
域
的
性
能
和
s
e
r
v
e
r
的
可
用
性
选
择
服
务
器
;
准
备
测
试
环
境
：
启
动
多
个
服
务
提
供
方
进
程
，
为
保
证
端
口
不
冲
突
，
通
过
启
动
参
数
配
置
端
口
，
并
启
动
这
两
个
进
程
。
 
可
通
过
下
面
方
式
在
服
务
消
费
方
的
 
配
置
文
件
中
修
改
默
认
的
负
载
均
衡
策
略
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 16 -->
n
a
c
o
s
-
r
e
s
t
f
u
l
-
p
r
o
v
i
d
e
r
即
服
务
提
供
方
的
服
务
名
称
。
c
o
m
.
n
e
t
ﬂ
i
x
.
l
o
a
d
b
a
l
a
n
c
e
r
.
R
a
n
d
o
m
R
u
l
e
：
负
载
均
衡
类
路
径
。
 
2
.
3
.
5
 
小
结
 
服
务
注
册
与
发
现
流
程
：
1
、
服
务
提
供
方
将
自
己
注
册
到
服
务
注
册
中
心
2
、
服
务
消
费
方
从
注
册
中
心
获
取
服
务
地
址
3
、
通
过
客
户
端
负
载
均
衡
器
进
行
远
程
调
用
 
2
.
4
 
D
u
b
b
o
服
务
发
现
 
 
 
D
u
b
b
o
是
阿
里
巴
巴
公
司
开
源
的
R
P
C
框
架
，
在
国
内
有
着
非
常
大
的
用
户
群
体
，
但
是
其
微
服
务
开
发
组
件
相
对
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
来
说
并
不
那
么
完
善
。
 
 
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
 
A
l
i
b
a
b
a
微
服
务
开
发
框
架
集
成
了
D
u
b
b
o
，
可
实
现
微
服
务
对
外
暴
露
D
u
b
b
o
协
议
的
接
口
，
D
u
b
b
o
协
议
相
比
R
E
S
T
f
u
l
协
议
速
度
更
快
。
R
P
C
：
R
P
C
是
远
程
过
程
调
用
（
R
e
m
o
t
e
 
P
r
o
c
e
d
u
r
e
 
C
a
l
l
）
的
缩
写
形
式
，
调
用
R
P
C
远
程
方
法
就
像
调
用
本
地
方
法
一
样
，
非
常
方
便
，
后
边
案
例
讲
解
具
体
过
程
。
2
.
4
.
1
 
D
u
b
b
o
服
务
架
构
 
下
图
是
微
服
务
采
用
D
u
b
b
o
协
议
的
系
统
架
构
图
：
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
p
r
o
v
i
d
e
r
:
 
 
r
i
b
b
o
n
:
 
 
 
 
N
F
L
o
a
d
B
a
l
a
n
c
e
r
R
u
l
e
C
l
a
s
s
N
a
m
e
:
 
c
o
m
.
n
e
t
f
l
i
x
.
l
o
a
d
b
a
l
a
n
c
e
r
.
R
a
n
d
o
m
R
u
l
e
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 17 -->
组
件
说
明
：
1
、
客
户
端
：
前
端
或
外
部
系
统
2
、
A
P
I
网
关
：
系
统
唯
一
入
口
，
路
由
转
发
3
、
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
-
1
 
：
应
用
1
，
前
端
提
供
H
t
t
p
接
口
，
接
收
用
户
的
交
互
请
求
4
、
s
e
r
v
i
c
e
-
1
 
：
微
服
务
1
，
提
供
业
务
逻
辑
处
理
服
务
5
、
s
e
r
v
i
c
e
-
2
：
微
服
务
2
，
提
供
业
务
逻
辑
处
理
服
务
交
互
流
程
：
1
、
网
关
负
责
客
户
端
请
求
的
统
一
入
口
，
路
由
转
发
，
前
端
通
过
网
关
请
求
后
端
服
务
。
2
、
网
关
收
到
前
端
请
求
，
转
发
请
求
给
应
用
。
3
、
应
用
接
收
前
端
请
求
，
调
用
微
服
务
进
行
业
务
逻
辑
处
理
4
、
微
服
务
为
应
用
提
供
业
务
逻
辑
处
理
的
支
撑
，
为
应
用
提
供
D
u
b
b
o
协
议
接
口
 
优
势
分
析
：
 
 
此
架
构
同
时
提
供
R
E
S
T
f
u
l
和
D
u
b
b
o
接
口
服
务
，
应
用
层
对
前
端
提
供
R
E
S
T
f
u
l
接
口
，
R
E
S
T
f
u
l
是
互
联
网
通
用
的
轻
量
级
交
互
协
议
，
方
便
前
端
接
入
系
统
；
微
服
务
层
向
应
用
层
提
供
D
u
b
b
o
接
口
，
D
u
b
b
o
接
口
基
于
R
P
C
通
信
协
议
速
度
更
快
。
 
 
本
架
构
采
用
阿
里
开
源
的
N
a
c
o
s
，
集
服
务
发
现
和
配
置
中
心
于
一
身
，
支
持
R
E
S
T
f
u
l
及
D
u
b
b
o
服
务
的
注
册
。
2
.
4
.
2
 
测
试
环
境
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 18 -->
父
工
程
：
仍
然
使
用
n
a
c
o
s
-
d
i
c
o
v
e
r
y
。
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
1
：
使
用
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
。
s
e
r
v
i
c
e
1
微
服
务
：
需
要
新
建
s
e
r
v
i
c
e
2
微
服
务
：
需
要
新
建
a
p
i
网
关
：
后
边
的
课
程
内
容
讲
解
。
 
2
.
4
.
3
 
s
e
r
v
i
c
e
2
微
服
务
 
s
e
r
v
i
c
e
2
对
外
暴
露
d
u
b
b
o
协
议
的
接
口
，
考
虑
远
程
接
口
可
能
 
会
被
其
它
多
个
服
务
调
用
，
这
里
将
s
e
r
v
i
c
e
2
的
接
口
单
独
抽
取
出
a
p
i
工
程
，
s
e
r
v
i
c
e
2
微
服
务
工
程
的
结
构
如
下
：
s
e
r
v
i
c
e
2
-
a
p
i
：
存
放
接
口
，
独
立
成
一
个
工
程
方
便
被
其
它
服
务
工
程
依
赖
。
s
e
r
v
i
c
e
2
-
s
e
r
v
e
r
：
存
放
接
口
实
现
，
即
d
u
b
b
o
服
务
的
实
现
部
分
。
2
.
4
.
3
.
1
 
定
义
s
e
r
v
i
c
e
2
-
a
p
i
 
1
、
创
建
s
e
r
v
i
c
e
2
工
程
 
2
、
创
建
s
e
r
v
i
c
e
2
-
a
p
i
工
程
 
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
n
a
c
o
s
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
‐
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
n
a
c
o
s
‐
d
u
b
b
o
‐
s
e
r
v
i
c
e
2
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
/
p
r
o
j
e
c
t
>
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 19 -->
3
、
定
义
接
口
 
2
.
4
.
3
.
2
 
定
义
s
e
r
v
i
c
e
2
-
s
e
r
v
e
r
 
1
、
创
建
s
e
r
v
i
c
e
2
-
s
e
r
v
e
r
工
程
 
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
u
b
b
o
‐
s
e
r
v
i
c
e
1
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
n
a
c
o
s
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
‐
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
2
‐
a
p
i
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
r
o
j
e
c
t
>
p
a
c
k
a
g
e
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
2
.
a
p
i
;
 
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
2
A
p
i
 
{
 
 
 
 
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
 
d
u
b
b
o
S
e
r
v
i
c
e
2
(
)
;
}
 
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
u
b
b
o
‐
s
e
r
v
i
c
e
1
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
n
a
c
o
s
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
‐
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
2
‐
s
e
r
v
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
n
a
c
o
s
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
r
v
i
c
e
2
‐
a
p
i
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
0
‐
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
a
l
i
b
a
b
a
‐
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 20 -->
2
、
定
义
接
口
实
现
注
意
：
使
用
@
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
ﬁ
g
.
a
n
n
o
t
a
t
i
o
n
.
S
e
r
v
i
c
e
标
记
d
u
b
b
o
服
务
 
3
、
定
义
启
动
类
 
4
、
定
义
配
置
文
件
b
o
o
t
s
t
r
a
p
.
y
m
l
 
 
 
 
 
 
 
 
 
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
d
u
b
b
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
p
r
o
j
e
c
t
>
p
a
c
k
a
g
e
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
2
.
s
e
r
v
i
c
e
;
 
i
m
p
o
r
t
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
2
.
a
p
i
.
S
e
r
v
i
c
e
2
A
p
i
;
 
@
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
f
i
g
.
a
n
n
o
t
a
t
i
o
n
.
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
 
S
e
r
v
i
c
e
2
A
p
i
I
m
p
l
 
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
 
S
e
r
v
i
c
e
2
A
p
i
 
{
 
 
 
 
 
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
 
d
u
b
b
o
S
e
r
v
i
c
e
2
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
d
u
b
b
o
S
e
r
v
i
c
e
2
"
;
 
 
 
 
}
}
 
 
p
a
c
k
a
g
e
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
2
;
 
i
m
p
o
r
t
 
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
.
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
;
i
m
p
o
r
t
 
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
.
a
u
t
o
c
o
n
f
i
g
u
r
e
.
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
;
 
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
2
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
2
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
s
e
r
v
e
r
:
 
 
p
o
r
t
:
 
5
6
0
4
0
 
#
启
动
端
口
 
命
令
行
注
入
 
s
p
r
i
n
g
:
 
 
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
:
 
 
 
 
n
a
m
e
:
 
d
u
b
b
o
‐
s
e
r
v
i
c
e
2
 
 
m
a
i
n
:
 
 
 
 
a
l
l
o
w
‐
b
e
a
n
‐
d
e
f
i
n
i
t
i
o
n
‐
o
v
e
r
r
i
d
i
n
g
:
 
t
r
u
e
 
#
 
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
 
2
.
1
 
需
要
设
定
 
 
c
l
o
u
d
:
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
d
i
s
c
o
v
e
r
y
:
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 21 -->
5
、
启
动
s
e
r
v
i
c
e
2
-
s
e
r
v
e
r
启
动
成
功
观
察
n
a
c
o
s
的
服
务
列
表
6
、
b
o
o
t
s
t
r
a
p
.
y
m
l
配
置
说
明
b
o
o
t
s
t
r
a
p
.
y
m
l
内
容
中
以
d
u
b
b
o
开
头
的
为
d
u
b
b
o
服
务
 
的
配
置
：
d
u
b
b
o
.
s
c
a
n
.
b
a
s
e
-
p
a
c
k
a
g
e
s
 
:
 
指
定
 
D
u
b
b
o
 
服
务
实
现
类
的
扫
描
基
准
包
，
将
@
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
ﬁ
g
.
a
n
n
o
t
a
t
i
o
n
.
S
e
r
v
i
c
e
注
解
标
注
的
s
e
r
v
i
c
e
暴
露
为
d
u
b
b
o
服
务
。
d
u
b
b
o
.
p
r
o
t
o
c
o
l
 
:
 
D
u
b
b
o
 
服
务
暴
露
的
协
议
配
置
，
其
中
子
属
性
 
n
a
m
e
 
为
协
议
名
称
，
p
o
r
t
 
为
d
u
b
b
o
协
议
端
口
可
以
指
定
多
协
议
，
如
：
d
u
b
b
o
.
p
r
o
t
o
c
o
l
.
r
m
i
.
p
o
r
t
=
1
0
9
9
d
u
b
b
o
.
r
e
g
i
s
t
r
y
 
:
 
D
u
b
b
o
 
服
务
注
册
中
心
配
置
，
其
中
子
属
性
 
a
d
d
r
e
s
s
 
的
值
 
"
n
a
c
o
s
:
/
/
1
2
7
.
0
.
0
.
1
:
8
8
4
8
"
，
说
明
d
u
b
b
o
服
务
注
册
到
n
a
c
o
s
相
当
于
原
生
d
u
b
b
o
的
x
m
l
配
置
中
的
 
<
d
u
b
b
o
:
r
e
g
i
s
t
r
y
 
a
d
d
r
e
s
s
=
"
1
0
.
2
0
.
1
5
3
.
1
0
:
9
0
9
0
"
 
/
>
 
b
o
o
t
s
t
r
a
p
.
y
m
l
内
容
的
上
半
部
分
为
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
的
相
关
配
置
：
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
 
:
 
S
p
r
i
n
g
 
应
用
名
称
，
用
于
 
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
 
服
务
注
册
和
发
现
。
该
值
在
 
D
u
b
b
o
 
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
 
加
持
下
被
视
作
 
d
u
b
b
o
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
，
因
此
，
无
需
再
显
示
地
配
置
d
u
b
b
o
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
n
a
c
o
s
.
d
i
s
c
o
v
e
r
y
 
:
 
N
a
c
o
s
 
服
务
发
现
与
注
册
配
置
，
其
中
子
属
性
 
s
e
r
v
e
r
-
a
d
d
r
 
指
定
 
N
a
c
o
s
 
服
务
器
主
机
和
端
口
 
 
2
.
4
.
4
 
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
1
调
用
s
e
r
v
i
c
e
2
 
根
据
d
u
b
b
o
服
务
的
架
构
图
，
本
章
节
将
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
作
为
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
1
，
实
现
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
1
调
用
s
e
r
v
i
c
e
2
。
2
.
4
.
4
.
1
 
引
用
s
e
r
v
i
c
e
2
 
d
u
b
b
o
:
 
 
s
c
a
n
:
 
 
 
 
#
 
d
u
b
b
o
 
服
务
扫
描
基
准
包
 
 
 
 
b
a
s
e
‐
p
a
c
k
a
g
e
s
:
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
2
.
s
e
r
v
i
c
e
 
 
p
r
o
t
o
c
o
l
:
 
 
 
 
#
 
d
u
b
b
o
 
协
议
 
 
 
 
n
a
m
e
:
 
d
u
b
b
o
 
 
 
 
#
 
d
u
b
b
o
 
协
议
端
口
 
 
 
 
p
o
r
t
:
 
2
0
8
9
1
 
 
r
e
g
i
s
t
r
y
:
 
 
 
 
a
d
d
r
e
s
s
:
 
n
a
c
o
s
:
/
/
1
2
7
.
0
.
0
.
1
:
8
8
4
8
 
 
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
:
 
 
 
 
q
o
s
‐
e
n
a
b
l
e
:
 
f
a
l
s
e
 
#
d
u
b
b
o
运
维
服
务
是
否
开
启
 
 
c
o
n
s
u
m
e
r
:
 
 
 
 
c
h
e
c
k
:
 
f
a
l
s
e
 
 
#
启
动
时
就
否
检
查
依
赖
的
服
务
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 22 -->
在
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
工
程
中
引
用
s
e
r
v
i
c
e
2
依
赖
在
p
o
m
.
x
m
l
中
引
入
s
e
r
v
i
c
e
2
-
a
p
i
的
依
赖
 
引
入
 
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
d
u
b
b
o
依
赖
，
它
会
根
据
接
口
生
成
代
理
对
象
 
2
.
4
.
4
.
2
 
实
现
远
程
调
用
 
修
改
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
工
程
的
R
e
s
t
C
o
n
s
u
m
e
r
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
：
 
N
o
t
e
：
注
意
：
这
里
的
@
R
e
f
e
r
e
n
c
e
注
解
是
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
f
i
g
.
a
n
n
o
t
a
t
i
o
n
.
R
e
f
e
r
e
n
c
e
测
试
：
请
求
：
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
5
6
0
2
0
/
s
e
r
v
i
c
e
2
显
示
：
c
o
n
s
u
m
e
r
 
d
u
b
b
o
 
i
n
v
o
k
e
 
|
 
d
u
b
b
o
S
e
r
v
i
c
e
2
 
表
明
s
e
r
v
i
c
e
2
调
用
成
功
。
 
2
.
4
.
5
 
s
e
r
v
i
c
e
1
微
服
务
 
s
e
r
v
i
c
e
1
采
用
和
s
e
r
v
i
c
e
2
相
同
的
工
程
结
构
。
本
节
实
现
s
e
r
v
i
c
e
1
对
外
暴
露
d
u
b
b
o
接
口
，
并
用
实
现
s
e
r
v
i
c
e
1
调
用
s
e
r
v
i
c
e
2
。
2
.
4
.
5
.
1
 
定
义
s
e
r
v
i
c
e
1
-
a
p
i
 
1
、
创
建
s
e
r
v
i
c
e
1
工
程
 
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
i
t
h
e
i
m
a
.
n
a
c
o
s
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
r
v
i
c
e
2
‐
a
p
i
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
0
‐
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
d
u
b
b
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
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
f
i
g
.
a
n
n
o
t
a
t
i
o
n
.
R
e
f
e
r
e
n
c
e
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
2
A
p
i
 
s
e
r
v
i
c
e
2
A
p
i
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
v
a
l
u
e
 
=
 
"
/
s
e
r
v
i
c
e
2
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
2
(
)
{
/
/
远
程
调
用
s
e
r
v
i
c
e
2
 
 
 
 
S
t
r
i
n
g
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
 
=
 
s
e
r
v
i
c
e
2
A
p
i
.
d
u
b
b
o
S
e
r
v
i
c
e
2
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
c
o
n
s
u
m
e
r
 
d
u
b
b
o
 
i
n
v
o
k
e
 
|
 
"
 
+
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
;
 
 
 
 
}
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 23 -->
2
、
创
建
s
e
r
v
i
c
e
1
-
a
p
i
工
程
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
 
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
u
b
b
o
‐
s
e
r
v
i
c
e
1
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
n
a
c
o
s
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
‐
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
1
‐
a
p
i
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
r
o
j
e
c
t
>
 
3
、
定
义
接
口
p
a
c
k
a
g
e
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
1
.
a
p
i
;
 
 
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
1
A
p
i
 
{
 
 
 
 
 
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
 
d
u
b
b
o
S
e
r
v
i
c
e
1
(
)
;
 
}
 
 
 
2
.
4
.
5
.
2
 
定
义
s
e
r
v
i
c
e
1
-
s
e
r
v
e
r
 
1
、
创
建
s
e
r
v
i
c
e
1
-
s
e
r
v
e
r
工
程
由
于
实
现
s
e
r
v
i
c
e
1
调
用
s
e
r
v
i
c
e
2
，
这
里
需
要
引
入
 
s
e
r
v
i
c
e
2
依
赖
。
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
n
a
c
o
s
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
‐
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
n
a
c
o
s
‐
d
u
b
b
o
‐
s
e
r
v
i
c
e
1
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
/
p
r
o
j
e
c
t
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 24 -->
<
?
x
m
l
 
v
e
r
s
i
o
n
=
"
1
.
0
"
 
e
n
c
o
d
i
n
g
=
"
U
T
F
‐
8
"
?
>
 
<
p
r
o
j
e
c
t
 
x
m
l
n
s
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
"
 
 
 
 
 
 
 
 
 
 
x
m
l
n
s
:
x
s
i
=
"
h
t
t
p
:
/
/
w
w
w
.
w
3
.
o
r
g
/
2
0
0
1
/
X
M
L
S
c
h
e
m
a
‐
i
n
s
t
a
n
c
e
"
 
 
 
 
 
 
 
 
 
 
x
s
i
:
s
c
h
e
m
a
L
o
c
a
t
i
o
n
=
"
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
P
O
M
/
4
.
0
.
0
 
h
t
t
p
:
/
/
m
a
v
e
n
.
a
p
a
c
h
e
.
o
r
g
/
x
s
d
/
m
a
v
e
n
‐
4
.
0
.
0
.
x
s
d
"
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
n
a
c
o
s
‐
d
u
b
b
o
‐
s
e
r
v
i
c
e
1
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
n
a
c
o
s
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
‐
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
1
‐
s
e
r
v
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
n
a
c
o
s
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
r
v
i
c
e
1
‐
a
p
i
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
0
‐
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
i
t
h
e
i
m
a
.
n
a
c
o
s
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
r
v
i
c
e
2
‐
a
p
i
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
0
‐
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
a
l
i
b
a
b
a
‐
n
a
c
o
s
‐
d
i
s
c
o
v
e
r
y
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
d
u
b
b
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
p
r
o
j
e
c
t
>
 
2
、
定
义
接
口
实
现
p
a
c
k
a
g
e
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
1
.
s
e
r
v
i
c
e
;
 
 
i
m
p
o
r
t
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
1
.
a
p
i
.
S
e
r
v
i
c
e
1
A
p
i
;
 
i
m
p
o
r
t
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
2
.
a
p
i
.
S
e
r
v
i
c
e
2
A
p
i
;
 
i
m
p
o
r
t
 
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
f
i
g
.
a
n
n
o
t
a
t
i
o
n
.
R
e
f
e
r
e
n
c
e
;
 
 
@
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
f
i
g
.
a
n
n
o
t
a
t
i
o
n
.
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
 
S
e
r
v
i
c
e
1
A
p
i
I
m
p
l
 
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
 
S
e
r
v
i
c
e
1
A
p
i
 
{
 
 
 
 
 
 
@
R
e
f
e
r
e
n
c
e
 
 
 
 
 
S
e
r
v
i
c
e
2
A
p
i
 
s
e
r
v
i
c
e
2
A
p
i
;
 
 
 
 
 
 
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
 
d
u
b
b
o
S
e
r
v
i
c
e
1
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
 
=
 
s
e
r
v
i
c
e
2
A
p
i
.
d
u
b
b
o
S
e
r
v
i
c
e
2
(
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 25 -->
r
e
t
u
r
n
 
"
d
u
b
b
o
S
e
r
v
i
c
e
1
|
"
+
s
;
 
 
 
 
 
}
 
}
 
 
3
、
定
义
启
动
类
p
a
c
k
a
g
e
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
1
;
 
 
i
m
p
o
r
t
 
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
.
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
;
 
i
m
p
o
r
t
 
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
.
a
u
t
o
c
o
n
f
i
g
u
r
e
.
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
;
 
 
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
1
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
1
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
 
4
、
定
义
配
置
文
件
b
o
o
t
s
t
r
a
p
.
y
m
l
s
e
r
v
e
r
:
 
 
 
p
o
r
t
:
 
5
6
0
3
0
 
#
启
动
端
口
 
命
令
行
注
入
 
 
s
p
r
i
n
g
:
 
 
 
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
:
 
 
 
 
 
n
a
m
e
:
 
d
u
b
b
o
‐
s
e
r
v
i
c
e
1
 
 
 
m
a
i
n
:
 
 
 
 
 
a
l
l
o
w
‐
b
e
a
n
‐
d
e
f
i
n
i
t
i
o
n
‐
o
v
e
r
r
i
d
i
n
g
:
 
t
r
u
e
 
#
 
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
 
2
.
1
 
需
要
设
定
 
 
 
c
l
o
u
d
:
 
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
 
d
i
s
c
o
v
e
r
y
:
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
 
d
u
b
b
o
:
 
 
 
s
c
a
n
:
 
 
 
 
 
#
 
d
u
b
b
o
 
服
务
扫
描
基
准
包
 
 
 
 
 
b
a
s
e
‐
p
a
c
k
a
g
e
s
:
 
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
i
c
r
o
s
e
r
v
i
c
e
.
s
e
r
v
i
c
e
1
.
s
e
r
v
i
c
e
 
 
 
p
r
o
t
o
c
o
l
:
 
 
 
 
 
#
 
d
u
b
b
o
 
协
议
 
 
 
 
 
n
a
m
e
:
 
d
u
b
b
o
 
 
 
 
 
#
 
d
u
b
b
o
 
协
议
端
口
 
 
 
 
 
p
o
r
t
:
 
2
0
8
8
1
 
 
 
r
e
g
i
s
t
r
y
:
 
 
 
 
 
a
d
d
r
e
s
s
:
 
n
a
c
o
s
:
/
/
1
2
7
.
0
.
0
.
1
:
8
8
4
8
 
 
 
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
:
 
 
 
 
 
q
o
s
‐
e
n
a
b
l
e
:
 
f
a
l
s
e
 
#
d
u
b
b
o
运
维
服
务
是
否
开
启
 
 
 
c
o
n
s
u
m
e
r
:
 
 
 
 
 
c
h
e
c
k
:
 
f
a
l
s
e
 
 
#
启
动
时
就
否
检
查
依
赖
的
服
务
 
5
、
启
动
s
e
r
v
i
c
e
1
-
s
e
r
v
e
r
启
动
成
功
观
察
n
a
c
o
s
的
服
务
列
表
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 26 -->
2
.
4
.
5
.
3
 
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
1
调
用
s
e
r
v
i
c
e
1
 
参
考
 
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
1
调
用
s
e
r
v
i
c
e
2
的
方
法
实
现
。
1
、
在
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
1
引
入
 
s
e
r
v
i
c
e
1
-
a
p
i
的
依
赖
略
2
、
在
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
1
的
c
o
n
t
r
o
l
l
e
r
中
调
用
s
e
r
v
i
c
e
1
接
口
@
R
e
f
e
r
e
n
c
e
 
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
1
A
p
i
 
s
e
r
v
i
c
e
1
A
p
i
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
v
a
l
u
e
 
=
 
"
/
s
e
r
v
i
c
e
3
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
1
(
)
{
 
 
 
 
 
S
t
r
i
n
g
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
 
=
 
s
e
r
v
i
c
e
1
A
p
i
.
d
u
b
b
o
S
e
r
v
i
c
e
1
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
c
o
n
s
u
m
e
r
 
d
u
b
b
o
 
i
n
v
o
k
e
 
|
 
"
 
+
 
p
r
o
v
i
d
e
r
R
e
s
u
l
t
;
 
}
 
3
、
测
试
，
请
求
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
5
6
0
2
0
/
s
e
r
v
i
c
e
3
显
示
 
：
c
o
n
s
u
m
e
r
 
d
u
b
b
o
 
i
n
v
o
k
e
 
|
 
d
u
b
b
o
S
e
r
v
i
c
e
1
|
d
u
b
b
o
S
e
r
v
i
c
e
2
，
表
明
调
用
s
e
r
v
i
c
e
1
成
功
，
s
e
r
v
i
c
e
1
调
用
s
e
r
v
i
c
e
2
成
功
。
 
2
.
5
 
服
务
发
现
数
据
模
型
 
2
.
5
.
1
N
a
m
e
s
p
a
c
e
 
隔
离
设
计
 
命
名
空
间
(
N
a
m
e
s
p
a
c
e
)
用
于
进
行
租
户
粒
度
的
隔
离
，
N
a
m
e
s
p
a
c
e
 
的
常
用
场
景
之
一
是
不
同
环
境
的
隔
离
，
例
如
开
发
测
试
环
境
和
生
产
环
境
的
资
源
（
如
配
置
、
服
务
）
隔
离
等
。
从
一
个
租
户
(
用
户
)
的
角
度
来
看
，
如
果
有
多
套
不
同
的
环
境
，
那
么
这
个
时
候
可
以
根
据
指
定
的
环
境
来
创
建
不
同
的
 
n
a
m
e
s
p
c
e
，
以
此
来
实
现
多
环
境
的
隔
离
。
例
如
，
你
可
能
有
开
发
，
测
试
和
生
产
三
个
不
同
的
环
境
，
那
么
使
用
一
套
 
n
a
c
o
s
 
集
群
可
以
分
别
建
以
下
三
个
不
同
的
 
n
a
m
e
s
p
a
c
e
。
如
下
图
所
示
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 27 -->
从
多
个
租
户
(
用
户
)
的
角
度
来
看
，
每
个
租
户
(
用
户
)
可
能
会
有
自
己
的
 
n
a
m
e
s
p
a
c
e
,
每
个
租
户
(
用
户
)
的
配
置
数
据
以
及
注
册
的
服
务
数
据
都
会
归
属
到
自
己
的
 
n
a
m
e
s
p
a
c
e
 
下
，
以
此
来
实
现
多
租
户
间
的
数
据
隔
离
。
例
如
超
级
管
理
员
分
配
了
三
个
租
户
，
分
别
为
张
三
、
李
四
和
王
五
。
分
配
好
了
之
后
，
各
租
户
用
自
己
的
账
户
名
和
密
码
登
录
后
，
创
建
自
己
的
命
名
空
间
。
如
下
图
所
示
：
注
意
:
 
在
此
教
程
编
写
之
时
，
n
a
c
o
s
多
租
户
(
用
户
)
功
能
还
在
规
划
中
。
 
2
.
5
.
2
 
命
名
空
间
管
理
 
 
 
前
面
已
经
介
绍
过
，
命
名
空
间
(
N
a
m
e
s
p
a
c
e
)
是
用
于
隔
离
多
个
环
境
的
（
如
开
发
、
测
试
、
生
产
）
，
而
每
个
应
用
在
不
同
环
境
的
同
一
个
配
置
（
如
数
据
库
数
据
源
）
的
值
是
不
一
样
的
。
因
此
，
我
们
应
针
对
企
业
项
目
实
际
研
发
流
程
、
环
境
进
行
规
划
。
如
某
软
件
公
司
拥
有
开
发
、
测
试
、
生
产
三
套
环
境
，
那
么
我
们
应
该
针
对
这
三
个
环
境
分
别
建
立
三
个
n
a
m
e
s
p
a
c
e
。
建
立
好
所
有
n
a
m
e
s
p
a
c
e
后
，
在
配
置
管
理
与
服
务
管
理
模
块
下
所
有
页
面
，
都
会
包
含
用
于
切
换
n
a
m
e
s
p
a
c
e
(
环
境
)
的
t
a
b
按
钮
，
如
下
图
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 28 -->
N
o
t
e
:
 
n
a
m
e
s
a
c
e
 
为
 
p
u
b
l
i
c
 
是
 
n
a
c
o
s
 
的
一
个
保
留
空
间
，
如
果
您
需
要
创
建
自
己
的
 
n
a
m
e
s
p
a
c
e
，
不
要
和
 
p
u
b
l
i
c
重
名
，
以
一
个
实
际
业
务
场
景
有
具
体
语
义
的
名
字
来
命
名
，
以
免
带
来
字
面
上
不
容
易
区
分
自
己
是
哪
一
个
n
a
m
e
s
p
a
c
e
。
N
o
t
e
：
在
编
写
程
序
获
取
配
置
集
时
，
指
定
的
n
a
m
e
s
p
a
c
e
参
数
一
定
要
填
写
命
名
空
间
I
D
，
而
不
是
名
称
 
2
.
5
.
3
 
数
据
模
型
 
 
 
N
a
c
o
s
在
经
过
阿
里
内
部
多
年
生
产
经
验
后
提
炼
出
的
数
据
模
型
，
则
是
一
种
服
务
-
集
群
-
实
例
的
三
层
模
型
，
这
样
基
本
可
以
满
足
服
务
在
所
有
场
景
下
的
数
据
存
储
和
管
理
。
n
a
c
o
s
服
务
发
现
的
数
据
模
型
如
下
：
服
务
对
外
提
供
的
软
件
功
能
，
通
过
网
络
访
问
预
定
义
的
接
口
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 29 -->
服
务
名
服
务
提
供
的
标
识
，
通
过
该
标
识
可
以
唯
一
确
定
要
访
问
的
服
务
。
实
例
提
供
一
个
或
多
个
服
务
的
具
有
可
访
问
网
络
地
址
（
I
P
:
P
o
r
t
）
的
进
程
，
启
动
一
个
服
务
，
就
产
生
了
一
个
服
务
实
例
。
元
信
息
N
a
c
o
s
数
据
（
如
配
置
和
服
务
）
描
述
信
息
，
如
服
务
版
本
、
权
重
、
容
灾
策
略
、
负
载
均
衡
策
略
、
鉴
权
配
置
、
各
种
自
定
义
标
签
 
(
l
a
b
e
l
)
，
从
作
用
范
围
来
看
，
分
为
服
务
级
别
的
元
信
息
、
集
群
的
元
信
息
及
实
例
的
元
信
息
。
集
群
服
务
实
例
的
集
合
，
服
务
实
例
组
成
一
个
默
认
集
群
,
 
集
群
可
以
被
进
一
步
按
需
求
划
分
，
划
分
的
单
位
可
以
是
虚
拟
集
群
，
相
同
集
群
下
的
实
例
才
能
相
互
感
知
。
通
过
数
据
模
型
可
知
：
应
用
通
过
N
a
m
e
s
p
a
c
e
、
S
e
r
v
i
c
e
、
C
l
u
s
t
e
r
(
D
E
F
A
U
L
T
)
的
配
置
，
描
述
了
该
服
务
向
哪
个
环
境
（
如
开
发
环
境
）
的
哪
个
集
群
注
册
实
例
。
例
子
如
下
：
指
定
n
a
m
e
s
p
a
c
e
的
i
d
：
a
1
f
8
e
8
6
3
-
3
1
1
7
-
4
8
c
4
-
9
d
d
3
-
e
9
d
d
c
2
a
f
9
0
a
8
（
注
意
根
据
自
己
环
境
设
置
n
a
m
e
s
p
a
c
e
的
i
d
）
指
定
集
群
名
称
：
D
E
F
A
U
L
T
表
示
默
认
集
群
，
可
不
填
写
 
N
o
t
e
:
 
集
群
作
为
实
例
的
隔
离
，
相
同
集
群
的
实
例
才
能
相
互
感
知
。
N
o
t
e
:
 
n
a
m
e
s
p
a
c
e
、
c
l
u
s
t
e
r
-
n
a
m
e
若
不
填
写
都
将
采
取
默
认
值
，
n
a
m
e
s
p
a
c
e
的
默
认
是
p
u
b
l
i
c
命
名
空
间
，
c
l
u
s
t
e
r
-
n
a
m
e
的
默
认
值
为
D
E
F
A
U
L
T
集
群
。
 
3
 
N
a
c
o
s
配
置
管
理
 
3
.
1
 
理
解
配
置
中
心
 
3
.
1
.
1
 
什
么
是
配
置
 
 
 
应
用
程
序
在
启
动
和
运
行
的
时
候
往
往
需
要
读
取
一
些
配
置
信
息
，
配
置
基
本
上
伴
随
着
应
用
程
序
的
整
个
生
命
周
期
，
比
如
：
数
据
库
连
接
参
数
、
启
动
参
数
等
。
配
置
主
要
有
以
下
几
个
特
点
：
s
p
r
i
n
g
:
 
 
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
:
 
 
 
 
n
a
m
e
:
 
t
r
a
n
s
a
c
t
i
o
n
‐
s
e
r
v
i
c
e
 
 
c
l
o
u
d
:
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
d
i
s
c
o
v
e
r
y
:
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
7
2
8
3
 
 
#
 
注
册
中
心
地
址
 
 
 
 
 
 
 
 
n
a
m
e
s
p
a
c
e
:
 
a
1
f
8
e
8
6
3
‐
3
1
1
7
‐
4
8
c
4
‐
9
d
d
3
‐
e
9
d
d
c
2
a
f
9
0
a
8
 
 
#
 
开
发
环
境
 
 
 
 
 
 
 
 
c
l
u
s
t
e
r
‐
n
a
m
e
:
 
D
E
F
A
U
L
T
 
#
 
默
认
集
群
，
可
不
填
写
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 30 -->
配
置
是
独
立
于
程
序
的
只
读
变
量
配
置
对
于
程
序
是
只
读
的
，
程
序
通
过
读
取
配
置
来
改
变
自
己
的
行
为
，
但
是
程
序
不
应
该
去
改
变
配
置
配
置
伴
随
应
用
的
整
个
生
命
周
期
配
置
贯
穿
于
应
用
的
整
个
生
命
周
期
，
应
用
在
启
动
时
通
过
读
取
配
置
来
初
始
化
，
在
运
行
时
根
据
配
置
调
整
行
为
。
比
如
：
启
动
时
需
要
读
取
服
务
的
端
口
号
、
系
统
在
运
行
过
程
中
需
要
读
取
定
时
策
略
执
行
定
时
任
务
等
。
配
置
可
以
有
多
种
加
载
方
式
常
见
的
有
程
序
内
部
h
a
r
d
 
c
o
d
e
，
配
置
文
件
，
环
境
变
量
，
启
动
参
数
，
基
于
数
据
库
等
配
置
需
要
治
理
同
一
份
程
序
在
不
同
的
环
境
（
开
发
，
测
试
，
生
产
）
、
不
同
的
集
群
（
如
不
同
的
数
据
中
心
）
经
常
需
要
有
不
同
的
配
置
，
所
以
需
要
有
完
善
的
环
境
、
集
群
配
置
管
理
3
.
1
.
2
 
什
么
是
配
置
中
心
 
 
 
在
微
服
务
架
构
中
，
当
系
统
从
一
个
单
体
应
用
，
被
拆
分
成
分
布
式
系
统
上
一
个
个
服
务
节
点
后
，
配
置
文
件
也
必
须
跟
着
迁
移
（
分
割
）
，
这
样
配
置
就
分
散
了
，
不
仅
如
此
，
分
散
中
还
包
含
着
冗
余
，
如
下
图
：
下
图
显
示
了
配
置
中
心
的
功
能
，
配
置
中
心
将
配
置
从
各
应
用
中
剥
离
出
来
，
对
配
置
进
行
统
一
管
理
，
应
用
自
身
不
需
要
自
己
去
管
理
配
置
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 31 -->
配
置
中
心
的
服
务
流
程
如
下
：
1
、
用
户
在
配
置
中
心
更
新
配
置
信
息
。
2
、
服
务
A
和
服
务
B
及
时
得
到
配
置
更
新
通
知
，
从
配
置
中
心
获
取
配
置
。
总
得
来
说
，
配
置
中
心
就
是
一
种
统
一
管
理
各
种
应
用
配
置
的
基
础
服
务
组
件
。
 
 
在
系
统
架
构
中
，
配
置
中
心
是
整
个
微
服
务
基
础
架
构
体
系
中
的
一
个
组
件
，
如
下
图
，
它
的
功
能
看
上
去
并
不
起
眼
，
无
非
就
是
配
置
的
管
理
和
存
取
，
但
它
是
整
个
微
服
务
架
构
中
不
可
或
缺
的
一
环
。
 
 
 
总
结
一
下
，
在
传
统
巨
型
单
体
应
用
纷
纷
转
向
细
粒
度
微
服
务
架
构
的
历
史
进
程
中
，
配
置
中
心
是
微
服
务
化
不
可
缺
少
的
一
个
系
统
组
件
，
在
这
种
背
景
下
中
心
化
的
配
置
服
务
即
配
置
中
心
应
运
而
生
，
一
个
合
格
的
配
置
中
心
需
要
满
足
如
下
特
性
：
配
置
项
容
易
读
取
和
修
改
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 32 -->
对
比
项
目
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
 
C
o
n
ﬁ
g
A
p
o
l
l
o
N
a
c
o
s
配
置
实
时
推
送
支
持
(
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
 
B
u
s
)
支
持
(
H
T
T
P
长
轮
询
1
s
内
)
支
持
(
H
T
T
P
长
轮
询
1
s
内
)
版
本
管
理
支
持
(
G
i
t
)
支
持
支
持
配
置
回
滚
支
持
(
G
i
t
)
支
持
支
持
灰
度
发
布
支
持
支
持
不
支
持
权
限
管
理
支
持
(
依
赖
G
i
t
)
支
持
不
支
持
多
集
群
支
持
支
持
支
持
多
环
境
支
持
支
持
支
持
监
听
查
询
支
持
支
持
支
持
多
语
言
只
支
持
J
a
v
a
主
流
语
言
，
提
供
了
O
p
e
n
 
A
P
I
主
流
语
言
，
提
供
了
O
p
e
n
 
A
P
I
配
置
格
式
校
验
不
支
持
支
持
支
持
单
机
读
(
Q
P
S
)
7
(
限
流
所
致
)
9
0
0
0
1
5
0
0
0
单
击
写
(
Q
P
S
)
5
(
限
流
所
致
)
1
1
0
0
1
8
0
0
3
节
点
读
(
Q
P
S
)
2
1
(
限
流
所
致
)
2
7
0
0
0
4
5
0
0
0
3
节
点
写
(
Q
P
S
)
5
(
限
流
所
致
)
3
3
0
0
5
6
0
0
分
布
式
环
境
下
应
用
配
置
的
可
管
理
性
，
即
提
供
远
程
管
理
配
置
的
能
力
支
持
对
配
置
的
修
改
的
检
视
以
把
控
风
险
可
以
查
看
配
置
修
改
的
历
史
记
录
不
同
部
署
环
境
下
应
用
配
置
的
隔
离
性
3
.
1
.
3
 
主
流
配
置
中
心
对
比
 
目
前
市
面
上
用
的
比
较
多
的
配
置
中
心
有
：
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
 
C
o
n
ﬁ
g
、
A
p
o
l
l
o
、
N
a
c
o
s
和
D
i
s
c
o
n
f
等
。
由
于
D
i
s
c
o
n
f
不
再
维
护
，
下
面
主
要
对
比
一
下
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
 
C
o
n
ﬁ
g
、
A
p
o
l
l
o
和
N
a
c
o
s
。
 
 
从
配
置
中
心
角
度
来
看
，
性
能
方
面
N
a
c
o
s
的
读
写
性
能
最
高
，
A
p
o
l
l
o
次
之
，
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
 
C
o
n
ﬁ
g
依
赖
G
i
t
场
景
不
适
合
开
放
的
大
规
模
自
动
化
运
维
A
P
I
。
功
能
方
面
A
p
o
l
l
o
最
为
完
善
，
n
a
c
o
s
具
有
A
p
o
l
l
o
大
部
分
配
置
管
理
功
能
，
而
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
C
o
n
ﬁ
g
不
带
运
维
管
理
界
面
，
需
要
自
行
开
发
。
N
a
c
o
s
的
一
大
优
势
是
整
合
了
注
册
中
心
、
配
置
中
心
功
能
，
部
署
和
操
作
相
比
A
p
o
l
l
o
都
要
直
观
简
单
，
因
此
它
简
化
了
架
构
复
杂
度
，
并
减
轻
运
维
及
部
署
工
作
。
 
 
综
合
来
看
，
N
a
c
o
s
的
特
点
和
优
势
还
是
比
较
明
显
的
，
下
面
我
们
一
起
进
入
N
a
c
o
s
的
世
界
。
3
.
2
 
N
a
c
o
s
配
置
管
理
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 33 -->
3
.
2
.
1
 
发
布
配
置
 
首
先
在
n
a
c
o
s
发
布
配
置
，
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
服
务
从
n
a
c
o
s
读
取
配
置
。
浏
览
器
访
问
 
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
8
8
4
8
/
n
a
c
o
s
 
，
打
开
n
a
c
o
s
控
制
台
，
并
点
击
菜
单
配
置
管
理
-
>
配
置
列
表
：
在
N
a
c
o
s
添
加
如
下
的
配
置
：
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
:
N
a
m
e
s
p
a
c
e
:
 
p
u
b
l
i
c
 
D
a
t
a
 
I
D
:
 
 
 
 
n
a
c
o
s
‐
r
e
s
t
f
u
l
‐
c
o
n
s
u
m
e
r
.
y
a
m
l
 
G
r
o
u
p
 
 
:
 
 
 
 
D
E
F
A
U
L
T
_
G
R
O
U
P
 
配
置
格
式
:
 
 
 
 
Y
A
M
L
 
配
置
内
容
：
 
 
 
c
o
m
m
o
n
:
 
 
 
 
 
 
 
 
n
a
m
e
:
 
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
1
 
c
o
n
f
i
g
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 34 -->
3
.
2
.
2
 
获
取
配
置
 
要
想
从
配
置
中
心
获
取
配
置
添
加
n
a
c
o
s
-
c
o
n
ﬁ
g
的
依
赖
：
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
‐
c
l
o
u
d
‐
s
t
a
r
t
e
r
‐
a
l
i
b
a
b
a
‐
n
a
c
o
s
‐
c
o
n
f
i
g
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
 
在
b
o
o
t
s
t
r
a
p
.
y
m
l
添
加
配
置
：
s
p
r
i
n
g
:
 
 
 
c
l
o
u
d
:
 
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
 
c
o
n
f
i
g
:
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
 
#
 
配
置
中
心
地
址
 
 
 
 
 
 
 
 
 
f
i
l
e
‐
e
x
t
e
n
s
i
o
n
:
 
y
a
m
l
 
 
 
 
 
 
 
 
 
g
r
o
u
p
:
 
D
E
F
A
U
L
T
_
G
R
O
U
P
 
注
意
：
要
使
用
配
置
中
心
就
要
在
b
o
o
t
s
t
r
a
p
.
y
m
l
中
来
配
置
，
b
o
o
t
s
t
r
a
p
.
y
m
l
配
置
文
件
的
加
载
顺
序
要
比
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
y
m
l
要
优
先
。
 
在
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
工
程
的
c
o
n
t
r
o
l
l
e
r
中
增
加
获
取
配
置
的
w
e
b
访
问
端
点
/
c
o
n
ﬁ
g
s
，
通
过
标
准
的
s
p
r
i
n
g
 
@
V
a
l
u
e
方
式
。
 
 
 
 
@
V
a
l
u
e
(
"
$
{
c
o
m
m
o
n
.
n
a
m
e
}
"
)
 
 
 
 
 
p
r
i
v
a
t
e
 
S
t
r
i
n
g
 
c
o
m
m
o
n
_
n
a
m
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
v
a
l
u
e
 
=
 
"
/
c
o
n
f
i
g
s
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
 
g
e
t
v
a
l
u
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
 
c
o
m
m
o
n
_
n
a
m
e
;
 
 
 
 
 
}
 
基
于
上
面
的
例
子
，
若
要
实
现
配
置
的
动
态
更
新
，
只
需
要
进
行
如
下
改
造
：
 
 
 
我
们
通
过
n
a
c
o
s
控
制
台
更
新
c
o
m
m
o
n
.
n
a
m
e
的
配
置
值
，
再
次
访
问
w
e
b
端
点
/
c
o
n
ﬁ
g
s
，
发
现
应
用
程
序
能
够
获
取
到
最
新
的
配
置
值
，
说
明
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
n
a
c
o
s
-
c
o
n
ﬁ
g
 
支
持
配
置
的
动
态
更
新
。
N
o
t
e
 
可
以
通
过
配
置
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
n
a
c
o
s
.
c
o
n
ﬁ
g
.
r
e
f
r
e
s
h
.
e
n
a
b
l
e
d
=
f
a
l
s
e
来
关
闭
动
态
刷
新
 
/
/
 
注
入
配
置
文
件
上
下
文
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
 
C
o
n
f
i
g
u
r
a
b
l
e
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
C
o
n
t
e
x
t
 
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
C
o
n
t
e
x
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
v
a
l
u
e
 
=
 
"
/
c
o
n
f
i
g
s
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
 
g
e
t
C
o
n
f
i
g
s
(
)
{
 
 
 
 
r
e
t
u
r
n
 
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
C
o
n
t
e
x
t
.
g
e
t
E
n
v
i
r
o
n
m
e
n
t
(
)
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
"
c
o
m
m
o
n
.
n
a
m
e
"
)
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 35 -->
3
.
2
.
3
 
配
置
管
理
模
型
 
对
于
N
a
c
o
s
配
置
管
理
，
通
过
N
a
m
e
s
p
a
c
e
、
g
r
o
u
p
、
D
a
t
a
 
I
D
能
够
定
位
到
一
个
配
置
集
。
 
配
置
集
(
D
a
t
a
 
I
D
)
 
 
在
系
统
中
，
一
个
配
置
文
件
通
常
就
是
一
个
配
置
集
，
一
个
配
置
集
可
以
包
含
了
系
统
的
各
种
配
置
信
息
，
例
如
，
一
个
配
置
集
可
能
包
含
了
数
据
源
、
线
程
池
、
日
志
级
别
等
配
置
项
。
每
个
配
置
集
都
可
以
定
义
一
个
有
意
义
的
名
称
，
就
是
配
置
集
的
I
D
即
D
a
t
a
I
D
。
配
置
项
 
 
配
置
集
中
包
含
的
一
个
个
配
置
内
容
就
是
配
置
项
。
它
代
表
一
个
具
体
的
可
配
置
的
参
数
与
其
值
域
，
通
常
以
 
k
e
y
=
v
a
l
u
e
 
的
形
式
存
在
。
例
如
我
们
常
配
置
系
统
的
日
志
输
出
级
别
（
l
o
g
L
e
v
e
l
=
I
N
F
O
|
W
A
R
N
|
E
R
R
O
R
）
 
就
是
一
个
配
置
项
。
配
置
分
组
(
G
r
o
u
p
)
 
 
配
置
分
组
是
对
配
置
集
进
行
分
组
，
通
过
一
个
有
意
义
的
字
符
串
（
如
 
B
u
y
 
或
 
T
r
a
d
e
 
）
来
表
示
，
不
同
的
配
置
分
组
下
可
以
有
相
同
的
配
置
集
（
D
a
t
a
 
I
D
）
。
当
您
在
 
N
a
c
o
s
 
上
创
建
一
个
配
置
时
，
如
果
未
填
写
配
置
分
组
的
名
称
，
则
配
置
分
组
的
名
称
默
认
采
用
 
D
E
F
A
U
L
T
_
G
R
O
U
P
 
。
配
置
分
组
的
常
见
场
景
：
可
用
于
区
分
不
同
的
项
目
或
应
用
，
例
如
：
学
生
管
理
系
统
的
配
置
集
可
以
定
义
一
个
g
r
o
u
p
为
：
S
T
U
D
E
N
T
_
G
R
O
U
P
。
 
命
名
空
间
(
N
a
m
e
s
p
a
c
e
)
 
 
命
名
空
间
（
n
a
m
e
s
p
a
c
e
）
可
用
于
进
行
不
同
环
境
的
配
置
隔
离
。
例
如
可
以
隔
离
开
发
环
境
、
测
试
环
境
和
生
产
环
境
，
因
为
它
们
的
配
置
可
能
各
不
相
同
，
或
者
是
隔
离
不
同
的
用
户
，
不
同
的
开
发
人
员
使
用
同
一
个
n
a
c
o
s
管
理
各
自
的
配
置
，
可
通
过
n
a
m
e
s
p
a
c
e
隔
离
。
不
同
的
命
名
空
间
下
，
可
以
存
在
相
同
名
称
的
配
置
分
组
(
G
r
o
u
p
)
 
或
 
配
置
集
。
最
佳
实
践
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 36 -->
N
a
c
o
s
抽
象
定
义
了
N
a
m
e
s
p
a
c
e
、
G
r
o
u
p
、
D
a
t
a
 
I
D
的
概
念
，
具
体
这
几
个
概
念
代
表
什
么
，
取
决
于
我
们
把
它
们
看
成
什
么
，
这
里
推
荐
给
大
家
一
种
用
法
，
如
下
图
：
N
a
m
e
s
p
a
c
e
：
代
表
不
同
环
境
，
如
开
发
、
测
试
、
生
产
环
境
。
G
r
o
u
p
：
代
表
某
项
目
，
如
X
X
医
疗
项
目
、
X
X
电
商
项
目
D
a
t
a
I
d
：
每
个
项
目
下
往
往
有
若
干
个
工
程
，
每
个
配
置
集
(
D
a
t
a
I
d
)
是
一
个
工
程
的
主
配
置
文
件
 
 
获
取
某
配
置
集
的
代
码
：
获
取
配
置
集
需
要
指
定
：
1
、
n
a
c
o
s
服
务
地
址
，
必
须
指
定
2
、
n
a
m
e
s
p
a
c
e
，
如
不
指
定
默
认
p
u
b
l
i
c
在
c
o
n
ﬁ
g
中
指
定
n
a
m
e
s
p
a
c
e
，
例
子
如
下
：
c
o
n
f
i
g
:
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
 
#
 
配
置
中
心
地
址
 
 
 
f
i
l
e
‐
e
x
t
e
n
s
i
o
n
:
 
y
a
m
l
 
 
 
n
a
m
e
s
p
a
c
e
:
 
a
1
f
8
e
8
6
3
‐
3
1
1
7
‐
4
8
c
4
‐
9
d
d
3
‐
e
9
d
d
c
2
a
f
9
0
a
8
 
#
 
开
发
环
境
 
 
 
g
r
o
u
p
:
 
D
E
F
A
U
L
T
_
G
R
O
U
P
 
#
 
x
x
业
务
组
 
3
、
g
r
o
u
p
，
如
不
指
定
默
认
 
D
E
F
A
U
L
T
_
G
R
O
U
P
见
上
边
第
2
点
的
例
子
。
4
、
d
a
t
a
I
d
，
必
须
指
定
，
名
称
为
应
用
名
称
+
配
置
文
件
扩
展
名
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 37 -->
3
.
3
 
自
定
义
扩
展
的
 
D
a
t
a
 
I
d
 
配
置
 
3
.
3
.
1
 
e
x
t
-
c
o
n
ﬁ
g
扩
展
配
置
 
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
 
A
l
i
b
a
b
a
 
N
a
c
o
s
 
C
o
n
ﬁ
g
可
支
持
自
定
义
 
D
a
t
a
 
I
d
 
的
配
置
。
 
一
个
完
整
的
配
置
案
例
如
下
所
示
：
 
可
以
看
到
:
通
过
 
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
n
a
c
o
s
.
c
o
n
f
i
g
.
e
x
t
-
c
o
n
f
i
g
[
n
]
.
d
a
t
a
-
i
d
 
的
配
置
方
式
来
支
持
多
个
 
D
a
t
a
 
I
d
 
的
配
置
。
通
过
 
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
n
a
c
o
s
.
c
o
n
f
i
g
.
e
x
t
-
c
o
n
f
i
g
[
n
]
.
g
r
o
u
p
 
的
配
置
方
式
自
定
义
 
D
a
t
a
 
I
d
 
所
在
的
组
，
不
明
确
配
置
的
话
，
默
认
是
 
D
E
F
A
U
L
T
_
G
R
O
U
P
。
s
p
r
i
n
g
:
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
:
 
 
 
 
n
a
m
e
:
 
s
e
r
v
i
c
e
2
 
 
 
 
 
 
 
 
c
l
o
u
d
:
 
 
 
 
n
a
c
o
s
:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
o
n
f
i
g
:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
e
r
v
e
r
‐
a
d
d
r
:
 
1
2
7
.
0
.
0
.
1
:
8
8
4
8
 
#
 
配
置
中
心
地
址
 
 
 
 
 
 
 
 
 
 
 
 
 
 
f
i
l
e
‐
e
x
t
e
n
s
i
o
n
:
 
y
a
m
l
 
 
 
 
 
 
#
 
 
 
 
 
 
 
 
n
a
m
e
s
p
a
c
e
:
 
a
1
f
8
e
8
6
3
‐
3
1
1
7
‐
4
8
c
4
‐
9
d
d
3
‐
e
9
d
d
c
2
a
f
9
0
a
8
 
#
 
开
发
环
境
 
 
 
 
 
 
 
 
 
 
 
 
 
 
g
r
o
u
p
:
 
D
E
F
A
U
L
T
_
G
R
O
U
P
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
c
o
n
f
i
g
 
e
x
t
e
r
n
a
l
 
c
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
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#
 
1
、
D
a
t
a
 
I
d
 
g
r
o
u
p
：
组
名
,
r
e
f
r
e
s
h
：
动
态
刷
新
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
t
‐
c
o
n
f
i
g
[
0
]
:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
‐
i
d
:
 
e
x
t
‐
c
o
n
f
i
g
‐
c
o
m
m
o
n
0
1
.
y
a
m
l
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
g
r
o
u
p
:
 
C
O
M
M
O
N
_
G
R
O
U
P
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
f
r
e
s
h
:
 
t
r
u
e
 
 
 
 
 
 
 
 
 
 
 
 
 
 
e
x
t
‐
c
o
n
f
i
g
[
1
]
:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
‐
i
d
:
 
e
x
t
‐
c
o
n
f
i
g
‐
c
o
m
m
o
n
0
2
.
y
a
m
l
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
g
r
o
u
p
:
 
C
O
M
M
O
N
_
G
R
O
U
P
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
f
r
e
s
h
:
 
t
r
u
e
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 38 -->
通
过
 
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
n
a
c
o
s
.
c
o
n
f
i
g
.
e
x
t
-
c
o
n
f
i
g
[
n
]
.
r
e
f
r
e
s
h
 
的
配
置
方
式
来
控
制
该
 
D
a
t
a
 
I
d
 
在
配
置
变
更
时
，
是
否
支
持
应
用
中
可
动
态
刷
新
，
 
感
知
到
最
新
的
配
置
值
。
默
认
是
不
支
持
的
。
N
o
t
e
 
：
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
n
a
c
o
s
.
c
o
n
f
i
g
.
e
x
t
-
c
o
n
f
i
g
[
n
]
.
d
a
t
a
-
i
d
 
的
值
必
须
带
文
件
扩
展
名
，
文
件
扩
展
名
既
可
支
持
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
，
又
可
以
支
持
 
y
a
m
l
/
y
m
l
。
 
此
时
 
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
n
a
c
o
s
.
c
o
n
f
i
g
.
f
i
l
e
-
e
x
t
e
n
s
i
o
n
 
的
配
置
对
自
定
义
扩
展
配
置
的
 
D
a
t
a
 
I
d
 
文
件
扩
展
名
没
有
影
响
。
 
测
试
：
配
置
e
x
t
-
c
o
n
ﬁ
g
-
c
o
m
m
o
n
0
1
.
y
a
m
l
：
配
置
e
x
t
-
c
o
n
ﬁ
g
-
c
o
m
m
o
n
0
2
.
y
a
m
l
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 39 -->
编
写
测
试
代
码
：
 
 
 
 
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
v
a
l
u
e
 
=
 
"
/
c
o
n
f
i
g
s
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
 
g
e
t
v
a
l
u
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
 
n
a
m
e
 
=
 
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
C
o
n
t
e
x
t
.
g
e
t
E
n
v
i
r
o
n
m
e
n
t
(
)
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
"
c
o
m
m
o
n
.
n
a
m
e
"
)
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
a
d
d
r
e
s
s
 
=
 
 
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
C
o
n
t
e
x
t
.
g
e
t
E
n
v
i
r
o
n
m
e
n
t
(
)
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
"
c
o
m
m
o
n
.
a
d
d
r
"
)
;
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
 
n
a
m
e
+
a
d
d
r
e
s
s
;
 
 
 
 
 
}
 
重
启
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
工
程
访
问
：
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
5
6
0
2
0
/
c
o
n
ﬁ
g
s
通
过
测
试
发
现
：
扩
展
配
置
优
先
级
是
 
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
n
a
c
o
s
.
c
o
n
f
i
g
.
e
x
t
-
c
o
n
f
i
g
[
n
]
.
d
a
t
a
-
i
d
 
其
中
 
n
 
的
值
越
大
，
优
先
级
越
高
。
通
过
内
部
相
关
规
则
(
应
用
名
、
扩
展
名
 
)
自
动
生
成
相
关
的
 
D
a
t
a
 
I
d
 
配
置
的
优
先
级
最
大
。
3
.
3
.
2
 
案
例
 
案
例
需
求
如
下
：
1
、
抽
取
s
e
r
v
l
e
t
公
用
的
配
置
到
独
立
的
配
置
文
件
，
配
置
文
件
内
容
如
下
：
#
H
T
T
P
格
式
配
置
 
s
p
r
i
n
g
:
 
 
 
h
t
t
p
:
 
 
 
 
 
e
n
c
o
d
i
n
g
:
 
 
 
 
 
 
 
c
h
a
r
s
e
t
:
 
U
T
F
‐
8
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 40 -->
f
o
r
c
e
:
 
t
r
u
e
 
 
 
 
 
 
 
e
n
a
b
l
e
d
:
 
t
r
u
e
 
 
 
m
e
s
s
a
g
e
s
:
 
 
 
 
 
e
n
c
o
d
i
n
g
:
 
U
T
F
‐
8
 
 
 
 
 
 
 
 
#
t
o
m
c
a
t
头
信
息
和
访
问
路
径
配
置
 
s
e
r
v
e
r
:
 
 
 
t
o
m
c
a
t
:
 
 
 
 
 
r
e
m
o
t
e
_
i
p
_
h
e
a
d
e
r
:
 
x
‐
f
o
r
w
a
r
d
e
d
‐
f
o
r
 
 
 
 
 
p
r
o
t
o
c
o
l
_
h
e
a
d
e
r
:
 
x
‐
f
o
r
w
a
r
d
e
d
‐
p
r
o
t
o
 
 
 
s
e
r
v
l
e
t
:
 
 
 
 
 
c
o
n
t
e
x
t
‐
p
a
t
h
:
 
/
a
 
 
 
u
s
e
‐
f
o
r
w
a
r
d
‐
h
e
a
d
e
r
s
:
 
t
r
u
e
 
2
、
如
果
有
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
的
个
性
配
置
可
以
单
独
设
置
实
现
如
下
：
1
、
抽
取
s
e
r
v
l
e
t
公
用
的
配
置
到
独
立
的
配
置
文
件
在
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
中
添
加
扩
展
配
置
文
件
，
下
图
中
红
色
框
内
为
指
定
的
配
置
文
件
名
称
：
在
n
a
c
o
s
中
添
加
扩
展
配
置
文
件
，
下
图
中
红
色
框
内
是
s
e
r
v
l
e
t
公
用
的
配
置
内
容
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 41 -->
发
布
配
置
，
重
启
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
访
问
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
5
6
0
2
0
/
a
/
c
o
n
ﬁ
g
s
验
证
配
置
是
否
生
效
2
、
如
果
有
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
的
个
性
配
置
可
以
单
独
设
置
这
里
我
们
需
要
对
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
的
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
设
置
为
根
路
径
，
如
何
实
现
？
方
案
1
：
修
改
e
x
t
-
c
o
n
ﬁ
g
-
h
t
t
p
.
y
a
m
l
中
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
为
根
路
径
，
但
是
此
文
件
定
义
为
公
用
配
置
文
件
，
其
它
服
务
可
使
用
了
，
此
方
案
不
可
行
。
方
案
2
：
在
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
.
y
a
m
l
中
定
义
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
为
根
路
径
，
因
为
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
.
y
a
m
l
单
独
属
于
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
工
程
，
且
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
.
y
a
m
l
的
优
先
级
比
e
x
t
-
c
o
n
ﬁ
g
-
h
t
t
p
.
y
a
m
l
高
，
所
以
此
方
案
可
行
。
在
n
a
c
o
s
中
配
置
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
.
y
a
m
l
，
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 42 -->
重
启
n
a
c
o
s
-
r
e
s
t
f
u
l
-
c
o
n
s
u
m
e
r
工
程
。
测
试
，
请
求
：
h
t
t
p
:
/
/
1
2
7
.
0
.
0
.
1
:
5
6
0
2
0
/
c
o
n
ﬁ
g
s
 
 
4
 
总
结
 
N
a
c
o
s
用
来
干
什
么
？
N
a
c
o
s
是
阿
里
巴
巴
公
司
开
源
的
项
目
，
它
用
来
实
现
配
置
中
心
和
服
务
注
册
中
心
。
什
么
是
服
务
发
现
？
在
微
服
务
架
构
中
一
个
业
务
流
程
需
要
多
个
微
服
务
通
过
网
络
接
口
调
用
完
成
业
务
处
理
，
服
务
消
费
方
从
服
务
注
册
中
心
获
取
服
务
提
供
方
的
地
址
，
从
而
进
行
远
程
调
用
，
这
个
过
程
叫
做
服
务
发
现
。
服
务
发
现
的
流
程
是
什
么
？
1
、
服
务
发
现
的
客
户
端
从
服
务
注
册
中
心
获
取
服
务
列
表
2
、
服
务
消
费
方
通
过
客
户
端
负
载
均
衡
获
取
服
务
实
例
地
址
，
进
行
远
程
调
用
。
什
么
是
配
置
中
心
？
在
微
服
务
架
构
中
为
了
统
一
管
理
各
各
微
服
务
的
配
置
信
息
专
门
设
置
配
置
中
心
，
配
置
中
心
就
是
一
种
统
一
管
理
各
种
应
用
配
置
的
基
础
服
务
组
件
。
配
置
中
心
的
应
用
流
程
是
什
么
？
1
、
发
布
配
置
，
将
配
置
信
息
发
布
到
配
置
中
心
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 43 -->
2
、
获
取
配
置
，
配
置
中
心
客
户
端
得
到
配
置
中
心
的
通
知
，
从
配
置
中
心
获
取
配
置
。
 
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
是
什
么
？
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
是
一
套
微
服
务
开
发
框
架
集
合
，
包
括
微
服
务
开
发
的
方
方
页
面
，
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
是
一
套
微
服
务
开
发
的
标
准
，
集
成
了
很
多
优
秀
的
开
源
框
架
，
比
如
有
名
的
N
e
t
ﬂ
i
x
公
司
的
众
多
项
目
。
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
 
A
l
i
b
a
b
a
是
什
么
？
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
 
A
l
i
b
a
b
a
是
阿
里
巴
巴
公
司
基
于
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
标
准
实
现
一
套
微
服
务
开
发
框
架
集
合
，
它
和
N
e
t
ﬂ
i
x
一
样
都
是
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
微
服
务
开
发
实
现
方
案
。
D
u
b
b
o
服
务
开
发
流
程
是
什
么
？
1
、
定
义
a
p
i
工
程
。
方
便
其
它
服
务
原
来
a
p
i
工
程
，
远
程
调
用
d
u
b
b
o
服
务
。
2
、
定
义
a
p
i
实
现
工
程
。
s
e
r
v
i
c
e
实
现
类
使
用
 
@
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
ﬁ
g
.
a
n
n
o
t
a
t
i
o
n
.
S
e
r
v
i
c
e
注
解
标
记
为
d
u
b
b
o
服
务
。
3
、
服
务
消
费
方
开
发
引
入
a
p
i
工
程
依
赖
使
用
o
r
g
.
a
p
a
c
h
e
.
d
u
b
b
o
.
c
o
n
ﬁ
g
.
a
n
n
o
t
a
t
i
o
n
.
R
e
f
e
r
e
n
c
e
注
解
注
入
s
e
r
v
i
c
e
，
发
起
远
程
调
用
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
