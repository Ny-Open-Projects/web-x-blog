# 闪聚支付-第3章-C扫Bv1.1

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\day09 支付结果获取 RocketMQ\讲义-pdf\闪聚支付-第3章-C扫Bv1.1【海量资源尽在 666java.com】.pdf
- 页数：68
- 抽取：pypdf 文本层



<!-- page 1 -->
闪
聚
支
付
 
第
3
章
讲
义
-
C
扫
B
支
付
 
1
 
需
求
分
析
 
1
.
1
 
C
扫
B
的
概
念
 
 
 
C
扫
B
，
即
顾
客
(
C
u
s
t
o
m
e
r
)
扫
描
商
户
(
B
u
s
i
n
e
s
s
)
提
供
的
二
维
码
来
完
成
支
付
。
下
图
是
支
付
宝
提
供
的
C
扫
B
业
务
流
程
：
1
、
商
家
出
示
付
款
二
维
码
2
、
客
户
打
开
支
付
宝
或
微
信
的
扫
一
扫
，
扫
描
二
维
码
3
、
确
认
支
付
，
完
成
支
付
。
 
C
扫
B
支
付
分
为
两
种
方
式
：
一
是
固
定
金
额
支
付
，
顾
客
扫
描
后
无
需
输
入
金
额
直
接
确
认
支
付
即
可
；
另
外
一
种
是
输
入
金
额
，
顾
客
扫
描
后
需
自
己
输
入
待
支
付
的
金
额
，
然
后
完
成
支
付
。
什
么
是
固
定
金
额
支
付
？
C
扫
B
固
定
金
额
比
较
常
见
的
就
是
在
自
动
售
货
机
购
买
饮
料
时
，
当
你
选
择
一
个
饮
料
后
屏
幕
会
显
示
一
个
二
维
码
，
咱
们
扫
描
后
只
需
确
认
支
付
即
可
，
无
需
自
己
输
入
饮
料
的
价
格
，
这
种
情
况
大
家
可
以
根
据
下
面
的
交
互
流
程
图
来
自
行
实
现
。
什
么
是
输
入
金
额
支
付
？
C
扫
B
输
入
金
额
支
付
方
式
可
以
让
买
方
自
由
输
入
金
额
，
商
户
提
前
生
成
一
个
二
维
码
，
将
二
维
码
张
贴
在
结
账
处
，
买
方
扫
描
二
维
码
，
输
入
当
前
消
费
的
金
额
，
完
成
支
付
。
 
1
.
2
 
业
务
流
程
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
1
.
2
 
业
务
流
程
 
本
章
节
实
现
C
扫
B
输
入
金
额
支
付
，
业
务
流
程
如
下
：
1
.
 
商
户
点
击
组
织
管
理
-
》
门
店
管
理
-
》
打
开
门
店
列
表
页
面
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
2
.
 
选
择
应
用
3
.
 
点
击
指
定
门
店
的
生
成
二
维
码
按
钮
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
4
.
 
顾
客
扫
描
生
成
的
二
维
码
，
进
入
支
付
页
面
，
输
入
金
额
来
完
成
支
付
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
1
.
3
 
需
求
列
表
 
根
据
业
务
流
程
的
分
析
，
闪
聚
支
付
平
台
实
现
C
扫
B
输
入
金
额
支
付
功
能
，
需
要
完
成
以
下
需
求
：
1
、
为
门
店
生
成
统
一
的
支
付
二
维
码
，
用
户
扫
一
下
二
维
码
即
可
使
用
微
信
支
付
也
可
使
用
支
付
宝
完
成
支
付
。
2
、
闪
聚
支
付
平
台
与
微
信
、
支
付
宝
对
接
，
闪
聚
支
付
作
为
中
介
，
最
终
的
支
付
动
作
（
银
行
交
易
）
仍
通
过
微
信
、
支
付
宝
进
行
。
3
、
闪
聚
平
台
作
为
中
介
调
用
微
信
、
支
付
宝
的
下
单
接
口
，
完
成
支
付
。
 
2
 
支
付
接
口
技
术
预
研
 
根
据
前
边
的
需
求
分
析
，
最
重
要
的
是
闪
聚
支
付
平
台
作
为
中
介
，
将
用
户
的
支
付
请
求
通
过
接
口
与
微
信
、
支
付
宝
等
第
三
方
支
付
渠
道
进
行
对
接
，
完
成
支
付
通
道
的
聚
合
，
所
以
首
先
需
要
调
研
微
信
、
支
付
宝
等
第
三
方
支
付
渠
道
的
对
接
方
式
。
本
项
目
首
期
上
线
要
求
集
成
微
信
和
支
付
宝
，
下
边
对
微
信
和
支
付
宝
的
支
付
接
口
进
行
技
术
预
研
，
包
括
：
对
接
的
流
程
，
接
口
协
议
、
接
口
测
试
等
。
参
考
：
闪
聚
支
付
-
第
3
章
-
支
付
宝
支
付
接
入
指
南
.
p
d
f
、
闪
聚
支
付
-
第
3
章
-
微
信
支
付
接
入
指
南
.
p
d
f
。
 
3
 
生
成
门
店
二
维
码
 
3
.
1
 
业
务
流
程
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
3
.
1
 
业
务
流
程
 
1
.
 
商
户
点
击
组
织
管
理
-
》
门
店
管
理
-
》
打
开
门
店
列
表
页
面
2
.
 
选
择
应
用
3
.
 
点
击
指
定
门
店
的
生
成
二
维
码
按
钮
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
3
.
2
 
生
成
二
维
码
技
术
预
研
 
Z
X
i
n
g
是
一
个
开
源
的
，
用
J
a
v
a
编
写
的
多
格
式
的
1
D
 
/
 
2
D
条
码
图
像
处
理
库
，
使
用
Z
X
i
n
g
可
以
生
成
、
识
别
Q
R
 
C
o
d
e
（
二
维
码
）
。
常
用
的
二
维
码
处
理
库
还
有
z
b
a
r
，
近
几
年
已
经
不
再
更
新
代
码
，
下
边
介
绍
Z
X
i
n
g
生
成
二
维
码
的
方
法
。
1
）
引
入
依
赖
在
s
h
a
n
j
u
p
a
y
-
c
o
m
m
o
n
工
程
p
o
m
.
x
m
l
中
添
加
依
赖
：
 
2
）
生
成
二
维
码
方
法
复
制
二
维
码
工
具
类
Q
R
C
o
d
e
U
t
i
l
.
j
a
v
a
到
项
目
中
测
试
根
据
内
容
生
成
二
维
码
方
法
，
在
Q
R
C
o
d
e
U
t
i
l
中
添
加
m
a
i
n
方
法
如
下
：
 
 
 
 
 
 
 
 
 
<
!
‐
‐
 
二
维
码
生
成
&
识
别
组
件
 
‐
‐
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
g
o
o
g
l
e
.
z
x
i
n
g
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
c
o
r
e
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
3
.
3
.
3
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
g
o
o
g
l
e
.
z
x
i
n
g
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
j
a
v
a
s
e
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
3
.
3
.
3
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
 
t
h
r
o
w
s
 
I
O
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
Q
R
C
o
d
e
U
t
i
l
 
q
r
C
o
d
e
U
t
i
l
 
=
 
n
e
w
 
Q
R
C
o
d
e
U
t
i
l
(
)
;
 
 
 
 
 
 
 
 
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
q
r
C
o
d
e
U
t
i
l
.
c
r
e
a
t
e
Q
R
C
o
d
e
(
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
i
t
c
a
s
t
.
c
n
/
"
,
 
2
0
0
,
 
2
0
0
)
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
运
行
m
a
i
n
方
法
，
将
输
出
的
内
容
复
制
到
浏
览
器
地
址
后
回
车
 
使
用
手
机
扫
描
二
维
码
，
即
可
自
动
打
开
传
智
播
客
官
网
 
3
.
3
 
门
店
列
表
 
3
.
3
.
1
 
商
户
服
务
查
询
门
店
列
表
 
3
.
3
.
1
.
1
 
接
口
定
义
 
1
、
接
口
描
述
1
）
根
据
商
户
i
d
和
分
页
信
息
查
询
门
店
列
表
2
、
接
口
定
义
如
下
：
M
e
r
c
h
a
n
t
S
e
r
v
i
c
e
d
a
t
a
:
i
m
a
g
e
/
p
n
g
;
b
a
s
e
6
4
,
i
V
B
O
R
w
0
K
G
g
o
A
A
A
A
N
S
U
h
E
U
g
A
A
A
M
g
A
A
A
D
I
A
Q
A
A
A
A
C
F
I
5
M
z
A
A
A
B
Q
E
l
E
Q
V
R
4
2
u
2
Y
P
Z
K
D
M
A
y
F
5
a
F
I
u
U
f
I
U
T
h
a
f
D
S
O
w
h
E
o
U
z
C
8
f
Z
K
M
y
S
S
b
r
V
I
8
Z
u
I
C
B
X
8
u
I
v
t
Z
P
x
j
e
D
f
u
S
f
8
l
i
P
i
7
L
F
S
g
r
z
R
T
v
V
3
X
C
K
a
w
X
Y
L
p
t
F
o
b
v
i
z
6
Z
z
B
2
x
E
f
T
j
h
y
S
9
O
w
X
B
3
A
7
j
b
M
S
n
g
L
O
Q
0
I
4
v
2
A
Z
f
9
6
w
q
T
W
J
9
+
9
/
d
Y
E
H
S
x
2
R
Y
q
f
g
/
o
q
U
g
i
X
3
n
F
B
V
f
c
C
e
p
c
S
b
i
J
P
6
7
i
w
Z
1
G
+
5
+
A
m
7
k
y
T
z
W
9
O
c
W
/
k
R
A
X
+
Q
J
9
5
3
+
u
C
l
8
z
O
5
P
V
5
U
s
a
f
f
U
p
8
r
q
P
5
+
j
i
y
S
J
U
8
j
t
N
x
c
N
r
y
s
e
t
C
N
K
6
A
/
V
4
l
E
Q
e
U
+
x
a
0
e
Z
R
E
E
1
t
O
T
p
F
Y
o
d
0
V
K
X
s
K
C
q
v
R
q
M
k
W
5
p
k
z
a
8
G
g
y
3
W
g
E
u
T
v
Z
c
z
0
d
c
U
B
c
+
9
M
n
e
L
1
D
q
k
X
j
Q
z
0
e
a
Z
A
1
L
q
V
t
m
z
c
M
f
f
T
K
P
i
P
w
z
1
m
h
2
z
k
G
y
N
w
t
T
9
k
g
u
T
V
I
7
L
W
v
6
u
l
7
D
C
p
O
j
X
9
i
a
G
V
6
6
H
D
n
y
/
Z
L
1
W
f
I
L
f
c
/
h
M
H
L
U
p
e
k
A
A
A
A
A
S
U
V
O
R
K
5
C
Y
I
I
=
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
3
.
3
.
1
.
2
 
接
口
实
现
 
3
、
在
M
e
r
c
h
a
n
t
S
e
r
v
i
c
e
I
m
p
l
中
实
现
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
方
法
：
 
 
3
.
3
.
2
 
商
户
平
台
应
用
查
询
门
店
列
表
 
3
.
3
.
2
.
1
 
接
口
定
义
 
1
、
接
口
描
述
1
）
请
求
商
户
服
务
查
询
门
店
列
表
 
2
、
接
口
定
义
如
下
：
S
t
o
r
e
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
 
/
*
*
 
*
 
分
页
条
件
查
询
商
户
下
门
店
 
*
 
@
p
a
r
a
m
 
s
t
o
r
e
D
T
O
 
*
 
@
p
a
r
a
m
 
p
a
g
e
N
o
 
*
 
@
p
a
r
a
m
 
p
a
g
e
S
i
z
e
 
*
 
@
r
e
t
u
r
n
 
*
/
P
a
g
e
V
O
<
S
t
o
r
e
D
T
O
>
 
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
(
S
t
o
r
e
D
T
O
 
s
t
o
r
e
D
T
O
,
 
I
n
t
e
g
e
r
 
p
a
g
e
N
o
,
 
I
n
t
e
g
e
r
 
p
a
g
e
S
i
z
e
)
;
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
 
P
a
g
e
V
O
<
S
t
o
r
e
D
T
O
>
 
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
(
S
t
o
r
e
D
T
O
 
s
t
o
r
e
D
T
O
,
 
I
n
t
e
g
e
r
 
p
a
g
e
N
o
,
 
I
n
t
e
g
e
r
 
p
a
g
e
S
i
z
e
)
 
{
 
 
 
/
/
 
创
建
分
页
 
 
 
P
a
g
e
<
S
t
o
r
e
>
 
p
a
g
e
 
=
 
n
e
w
 
P
a
g
e
<
>
(
p
a
g
e
N
o
,
 
p
a
g
e
S
i
z
e
)
;
 
 
 
/
/
 
构
造
查
询
条
件
 
 
 
Q
u
e
r
y
W
r
a
p
p
e
r
<
S
t
o
r
e
>
 
q
w
 
=
 
n
e
w
 
Q
u
e
r
y
W
r
a
p
p
e
r
(
)
;
 
 
 
i
f
 
(
n
u
l
l
 
!
=
 
s
t
o
r
e
D
T
O
 
&
&
 
n
u
l
l
 
!
=
 
s
t
o
r
e
D
T
O
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
)
 
{
 
 
 
 
 
 
q
w
.
l
a
m
b
d
a
(
)
.
e
q
(
S
t
o
r
e
:
:
g
e
t
M
e
r
c
h
a
n
t
I
d
,
 
s
t
o
r
e
D
T
O
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
)
;
 
 
 
}
 
 
 
/
/
 
执
行
查
询
 
 
 
I
P
a
g
e
<
S
t
o
r
e
>
 
s
t
o
r
e
I
P
a
g
e
 
=
 
s
t
o
r
e
M
a
p
p
e
r
.
s
e
l
e
c
t
P
a
g
e
(
p
a
g
e
,
 
q
w
)
;
 
 
 
/
/
 
e
n
t
i
t
y
 
L
i
s
t
转
D
T
O
 
L
i
s
t
 
 
 
L
i
s
t
<
S
t
o
r
e
D
T
O
>
 
s
t
o
r
e
L
i
s
t
 
=
 
S
t
o
r
e
C
o
n
v
e
r
t
.
I
N
S
T
A
N
C
E
.
l
i
s
t
e
n
t
i
t
y
2
d
t
o
(
s
t
o
r
e
I
P
a
g
e
.
g
e
t
R
e
c
o
r
d
s
(
)
)
;
 
 
 
/
/
 
封
装
结
果
集
 
 
 
r
e
t
u
r
n
 
n
e
w
 
P
a
g
e
V
O
<
>
(
s
t
o
r
e
L
i
s
t
,
 
s
t
o
r
e
I
P
a
g
e
.
g
e
t
T
o
t
a
l
(
)
,
 
p
a
g
e
N
o
,
 
p
a
g
e
S
i
z
e
)
;
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
s
h
a
n
j
u
p
a
y
.
m
e
r
c
h
a
n
t
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
 
@
A
p
i
(
v
a
l
u
e
 
=
 
"
商
户
平
台
‐
门
店
管
理
"
,
 
t
a
g
s
 
=
 
"
商
户
平
台
‐
门
店
管
理
"
,
 
d
e
s
c
r
i
p
t
i
o
n
 
=
 
"
商
户
平
台
‐
门
店
的
增
删
改
查
"
)
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
t
o
r
e
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
p
i
O
p
e
r
a
t
i
o
n
(
"
分
页
条
件
查
询
商
户
下
门
店
"
)
 
 
 
@
A
p
i
I
m
p
l
i
c
i
t
P
a
r
a
m
s
(
{
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
3
.
3
.
2
.
2
 
接
口
实
现
 
前
端
J
S
在
L
o
n
g
长
度
大
于
1
7
位
时
会
出
现
精
度
丢
失
的
问
题
，
由
于
项
目
中
门
店
I
D
的
长
度
会
超
过
1
7
位
，
所
以
在
此
处
添
加
注
解
将
返
回
给
前
端
的
门
店
I
D
自
动
转
为
s
t
r
i
n
g
类
型
1
）
使
用
j
a
c
k
s
o
n
来
完
成
自
动
转
换
，
在
s
h
a
n
j
u
p
a
y
-
m
e
r
c
h
a
n
t
-
a
p
i
工
程
中
添
加
依
赖
：
 
2
）
在
S
t
o
r
e
D
T
O
中
添
加
注
解
：
 
 
2
、
在
S
t
o
r
e
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
实
现
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
方
法
：
 
2
.
3
.
4
.
3
 
接
口
测
试
 
由
于
已
经
接
入
S
a
a
S
，
请
求
统
一
走
网
关
的
端
口
5
6
0
1
0
。
 
 
 
 
 
 
 
 
 
@
A
p
i
I
m
p
l
i
c
i
t
P
a
r
a
m
(
n
a
m
e
 
=
 
"
p
a
g
e
N
o
"
,
 
v
a
l
u
e
 
=
 
"
页
码
"
,
 
r
e
q
u
i
r
e
d
 
=
 
t
r
u
e
,
 
d
a
t
a
T
y
p
e
 
=
 
"
i
n
t
"
,
 
p
a
r
a
m
T
y
p
e
 
=
 
"
q
u
e
r
y
"
)
,
 
 
 
 
 
 
 
 
 
@
A
p
i
I
m
p
l
i
c
i
t
P
a
r
a
m
(
n
a
m
e
 
=
 
"
p
a
g
e
S
i
z
e
"
,
 
v
a
l
u
e
 
=
 
"
每
页
记
录
数
"
,
 
r
e
q
u
i
r
e
d
 
=
 
t
r
u
e
,
 
d
a
t
a
T
y
p
e
 
=
 
"
i
n
t
"
,
 
p
a
r
a
m
T
y
p
e
 
=
 
"
q
u
e
r
y
"
)
}
)
 
 
 
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
"
/
m
y
/
s
t
o
r
e
s
/
m
e
r
c
h
a
n
t
s
/
p
a
g
e
"
)
 
 
 
p
u
b
l
i
c
 
P
a
g
e
V
O
<
S
t
o
r
e
D
T
O
>
 
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
(
@
R
e
q
u
e
s
t
P
a
r
a
m
 
I
n
t
e
g
e
r
 
p
a
g
e
N
o
,
 
@
R
e
q
u
e
s
t
P
a
r
a
m
 
I
n
t
e
g
e
r
 
p
a
g
e
S
i
z
e
)
{
 
 
 
}
}
 
 
 
 
 
 
 
 
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
f
a
s
t
e
r
x
m
l
.
j
a
c
k
s
o
n
.
c
o
r
e
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
j
a
c
k
s
o
n
‐
d
a
t
a
b
i
n
d
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
9
.
9
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
s
c
o
p
e
>
c
o
m
p
i
l
e
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
@
A
p
i
M
o
d
e
l
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
门
店
I
d
"
)
@
J
s
o
n
S
e
r
i
a
l
i
z
e
(
u
s
i
n
g
=
 
T
o
S
t
r
i
n
g
S
e
r
i
a
l
i
z
e
r
.
c
l
a
s
s
)
p
r
i
v
a
t
e
 
L
o
n
g
 
i
d
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
/
m
y
/
s
t
o
r
e
s
/
m
e
r
c
h
a
n
t
s
/
p
a
g
e
"
)
p
u
b
l
i
c
 
P
a
g
e
V
O
<
S
t
o
r
e
D
T
O
>
 
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
(
@
R
e
q
u
e
s
t
P
a
r
a
m
 
I
n
t
e
g
e
r
 
p
a
g
e
N
o
,
 
@
R
e
q
u
e
s
t
P
a
r
a
m
 
I
n
t
e
g
e
r
 
p
a
g
e
S
i
z
e
)
{
 
 
 
/
/
获
取
商
户
i
d
 
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
 
=
 
S
e
c
u
r
i
t
y
U
t
i
l
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
;
 
 
S
t
o
r
e
D
T
O
 
s
t
o
r
e
D
T
O
 
=
 
n
e
w
 
S
t
o
r
e
D
T
O
(
)
;
 
 
s
t
o
r
e
D
T
O
.
s
e
t
M
e
r
c
h
a
n
t
I
d
(
m
e
r
c
h
a
n
t
I
d
)
;
 
 
/
/
分
页
查
询
 
 
P
a
g
e
V
O
<
S
t
o
r
e
D
T
O
>
 
s
t
o
r
e
s
 
=
 
m
e
r
c
h
a
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
S
t
o
r
e
B
y
P
a
g
e
(
s
t
o
r
e
D
T
O
,
 
p
a
g
e
N
o
,
 
p
a
g
e
S
i
z
e
)
;
 
 
r
e
t
u
r
n
 
s
t
o
r
e
s
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
1
首
先
请
求
认
证
获
取
t
o
k
e
n
，
及
租
户
的
i
d
1
)
启
动
三
个
S
a
a
S
服
务
2
)
使
用
账
号
申
请
t
o
k
e
n
 
2
使
用
P
o
s
t
m
a
n
：
P
O
S
T
 
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
6
0
1
0
/
m
e
r
c
h
a
n
t
/
m
y
/
s
t
o
r
e
s
/
m
e
r
c
h
a
n
t
s
/
p
a
g
e
?
p
a
g
e
N
o
=
1
&
p
a
g
e
S
i
z
e
=
2
0
 
查
询
门
店
列
表
注
意
在
h
e
a
d
e
r
中
添
加
 
A
u
t
h
o
r
i
z
a
t
i
o
n
及
t
e
n
a
n
t
I
d
。
 
 
3
.
4
 
生
成
二
维
码
 
3
.
4
.
1
 
系
统
交
互
流
程
 
生
成
二
维
码
的
系
统
交
互
 
流
程
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
1
、
商
户
登
录
商
户
应
用
平
台
 
，
查
询
门
店
列
表
2
、
商
户
平
台
 
请
求
交
易
 
服
务
获
取
门
店
二
维
码
U
R
L
3
、
商
户
平
台
 
根
据
 
U
R
L
生
成
二
维
码
 
 
3
.
4
.
2
交
易
服
务
生
成
二
维
码
U
R
L
 
3
.
4
.
2
.
1
 
接
口
定
义
 
接
口
描
述
：
生
成
门
店
的
c
扫
b
二
维
码
接
口
参
数
：
输
入
：
商
户
i
d
、
应
用
i
d
、
门
店
i
d
、
标
题
，
内
容
输
出
：
支
付
入
口
1
、
在
交
易
服
务
的
a
p
i
工
程
 
创
建
d
t
o
 
2
、
接
口
定
义
如
下
@
D
a
t
a
@
N
o
A
r
g
s
C
o
n
s
t
r
u
c
t
o
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
 
Q
R
C
o
d
e
D
t
o
 
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
i
a
l
i
z
a
b
l
e
 
{
 
 
 
 
 
p
r
i
v
a
t
e
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
;
 
 
 
 
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
 
a
p
p
I
d
;
 
 
 
 
p
r
i
v
a
t
e
 
L
o
n
g
 
s
t
o
r
e
I
d
;
 
 
 
 
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
u
b
j
e
c
t
;
/
/
商
品
标
题
 
 
 
 
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
 
b
o
d
y
;
/
/
订
单
描
述
 
}
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
3
.
4
.
2
.
2
 
商
户
服
务
应
用
合
法
校
验
接
口
 
商
户
生
成
二
维
码
需
要
根
据
门
店
、
应
用
来
生
成
，
设
计
接
口
需
要
对
应
用
和
门
店
的
合
法
性
来
校
验
。
1
、
校
验
该
应
用
是
否
属
于
该
商
户
。
2
、
校
验
该
门
店
是
否
属
于
该
商
户
1
、
接
口
描
述
1
）
根
据
商
户
i
d
和
应
用
i
d
查
询
应
用
信
息
，
查
询
到
则
说
明
合
法
。
2
、
在
A
p
p
S
e
r
v
i
c
e
下
定
义
接
口
如
下
 
3
、
接
口
实
现
如
下
在
A
p
p
S
e
r
v
i
c
e
I
m
p
l
中
实
现
q
u
e
r
y
A
p
p
I
n
M
e
r
c
h
a
n
t
接
口
/
*
*
 
*
 
交
易
订
单
相
关
服
务
接
口
 
*
/
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
 
T
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
S
e
r
v
i
c
e
 
{
 
 
 
 
/
*
*
 
 
 
 
 
*
 
生
成
门
店
二
维
码
 
 
 
 
 
*
 
@
p
a
r
a
m
 
q
r
C
o
d
e
D
t
o
，
传
入
m
e
r
c
h
a
n
t
I
d
,
a
p
p
I
d
、
s
t
o
r
e
i
d
、
c
h
a
n
n
e
l
、
s
u
b
j
e
c
t
、
b
o
d
y
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
支
付
入
口
U
R
L
，
将
二
维
码
的
参
数
组
成
j
s
o
n
并
用
b
a
s
e
6
4
编
码
 
 
 
 
 
*
 
@
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
 
 
 
 
*
/
 
 
 
 
S
t
r
i
n
g
 
c
r
e
a
t
e
S
t
o
r
e
Q
R
C
o
d
e
(
Q
R
C
o
d
e
D
t
o
 
q
r
C
o
d
e
D
t
o
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
;
 
}
/
*
*
 
*
 
查
询
应
用
是
否
属
于
某
个
商
户
 
*
 
@
p
a
r
a
m
 
a
p
p
I
d
 
*
 
@
p
a
r
a
m
 
m
e
r
c
h
a
n
t
I
d
 
*
 
@
r
e
t
u
r
n
 
*
/
B
o
o
l
e
a
n
 
q
u
e
r
y
A
p
p
I
n
M
e
r
c
h
a
n
t
(
S
t
r
i
n
g
 
a
p
p
I
d
,
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 14 -->
3
.
4
.
2
.
3
 
商
户
服
务
门
店
合
法
校
验
接
口
 
1
、
接
口
描
述
1
）
根
据
商
户
i
d
和
门
店
i
d
查
询
门
店
，
查
询
到
则
说
明
合
法
。
 
2
、
在
M
e
r
c
h
a
n
t
S
e
r
v
i
c
e
中
定
义
接
口
：
 
3
、
接
口
实
现
如
下
在
M
e
r
c
h
a
n
t
S
e
r
v
i
c
e
I
m
p
l
中
实
现
q
u
e
r
y
S
t
o
r
e
I
n
M
e
r
c
h
a
n
t
接
口
 
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
查
询
应
用
是
否
属
于
某
个
商
户
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
p
p
I
d
 
 
 
 
 
*
 
@
p
a
r
a
m
 
m
e
r
c
h
a
n
t
I
d
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
 
 
 
 
*
/
 
 
 
 
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
 
B
o
o
l
e
a
n
 
q
u
e
r
y
A
p
p
I
n
M
e
r
c
h
a
n
t
(
S
t
r
i
n
g
 
a
p
p
I
d
,
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
)
 
{
 
 
 
 
 
 
 
 
I
n
t
e
g
e
r
 
c
o
u
n
t
 
=
 
a
p
p
M
a
p
p
e
r
.
s
e
l
e
c
t
C
o
u
n
t
(
n
e
w
 
L
a
m
b
d
a
Q
u
e
r
y
W
r
a
p
p
e
r
<
A
p
p
>
(
)
.
e
q
(
A
p
p
:
:
g
e
t
A
p
p
I
d
,
 
a
p
p
I
d
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
e
q
(
A
p
p
:
:
g
e
t
M
e
r
c
h
a
n
t
I
d
,
 
m
e
r
c
h
a
n
t
I
d
)
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t
>
0
;
 
 
 
 
}
/
*
*
 
*
 
查
询
门
店
是
否
属
于
某
商
户
 
*
 
@
p
a
r
a
m
 
s
t
o
r
e
I
d
 
*
 
@
p
a
r
a
m
 
m
e
r
c
h
a
n
t
I
d
 
*
 
@
r
e
t
u
r
n
 
*
/
B
o
o
l
e
a
n
 
q
u
e
r
y
S
t
o
r
e
I
n
M
e
r
c
h
a
n
t
(
L
o
n
g
 
s
t
o
r
e
I
d
,
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
)
;
/
*
*
 
 
 
 
 
*
 
查
询
门
店
是
否
属
于
某
商
户
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
s
t
o
r
e
I
d
 
 
 
 
 
*
 
@
p
a
r
a
m
 
m
e
r
c
h
a
n
t
I
d
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
 
 
 
 
*
/
 
 
 
 
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
 
B
o
o
l
e
a
n
 
q
u
e
r
y
S
t
o
r
e
I
n
M
e
r
c
h
a
n
t
(
L
o
n
g
 
s
t
o
r
e
I
d
,
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
)
 
{
 
 
 
 
 
 
 
 
I
n
t
e
g
e
r
 
c
o
u
n
t
 
=
 
s
t
o
r
e
M
a
p
p
e
r
.
s
e
l
e
c
t
C
o
u
n
t
(
n
e
w
 
L
a
m
b
d
a
Q
u
e
r
y
W
r
a
p
p
e
r
<
S
t
o
r
e
>
(
)
.
e
q
(
S
t
o
r
e
:
:
g
e
t
I
d
,
 
s
t
o
r
e
I
d
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
e
q
(
S
t
o
r
e
:
:
g
e
t
M
e
r
c
h
a
n
t
I
d
,
 
m
e
r
c
h
a
n
t
I
d
)
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
c
o
u
n
t
>
0
;
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 15 -->
3
.
4
.
2
.
4
 
接
口
实
现
 
在
N
a
c
o
s
中
添
加
支
付
入
口
配
置
：
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
-
s
e
r
v
i
c
e
.
y
a
m
l
支
付
入
口
是
扫
码
支
付
的
统
一
入
口
。
 
实
现
c
r
e
a
t
e
S
t
o
r
e
Q
R
C
o
d
e
接
口
：
 
#
支
付
入
口
u
r
l
s
h
a
n
j
u
p
a
y
:
 
 
p
a
y
u
r
l
:
 
"
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
1
0
/
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
/
p
a
y
‐
e
n
t
r
y
/
"
@
S
l
f
4
j
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
 
T
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
S
e
r
v
i
c
e
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
 
T
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
S
e
r
v
i
c
e
 
{
 
 
 
 
/
*
*
 
 
 
 
 
*
 
支
付
入
口
u
r
l
 
 
 
 
 
*
/
 
 
 
 
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
s
h
a
n
j
u
p
a
y
.
p
a
y
u
r
l
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
a
y
u
r
l
;
 
 
 
 
 
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
 
 
 
 
M
e
r
c
h
a
n
t
S
e
r
v
i
c
e
 
m
e
r
c
h
a
n
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
R
e
f
e
r
e
n
c
e
 
 
 
 
A
p
p
S
e
r
v
i
c
e
 
a
p
p
S
e
r
v
i
c
e
;
 
 
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
 
生
成
门
店
二
维
码
 
 
 
 
 
*
 
@
p
a
r
a
m
 
q
r
C
o
d
e
D
t
o
 
商
户
i
d
、
应
用
i
d
、
门
店
i
d
、
标
题
、
内
容
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
 
 
 
 
*
 
@
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
 
 
 
 
*
/
 
 
 
 
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
 
c
r
e
a
t
e
S
t
o
r
e
Q
R
C
o
d
e
(
Q
R
C
o
d
e
D
t
o
 
q
r
C
o
d
e
D
t
o
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
 
 
 
 
/
/
校
验
应
用
和
门
店
 
 
 
 
 
 
 
 
v
e
r
i
f
y
A
p
p
A
n
d
S
t
o
r
e
(
q
r
C
o
d
e
D
t
o
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
,
q
r
C
o
d
e
D
t
o
.
g
e
t
A
p
p
I
d
(
)
,
q
r
C
o
d
e
D
t
o
.
g
e
t
S
t
o
r
e
I
d
(
)
)
;
 
 
 
 
 
 
 
 
/
/
1
.
 
生
成
支
付
信
息
 
 
 
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
n
e
w
 
P
a
y
O
r
d
e
r
D
T
O
(
)
;
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
M
e
r
c
h
a
n
t
I
d
(
q
r
C
o
d
e
D
t
o
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
)
;
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
A
p
p
I
d
(
q
r
C
o
d
e
D
t
o
.
g
e
t
A
p
p
I
d
(
)
)
;
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
S
t
o
r
e
I
d
(
q
r
C
o
d
e
D
t
o
.
g
e
t
S
t
o
r
e
I
d
(
)
)
;
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
S
u
b
j
e
c
t
(
q
r
C
o
d
e
D
t
o
.
g
e
t
S
u
b
j
e
c
t
(
)
)
;
/
/
显
示
订
单
标
题
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
C
h
a
n
n
e
l
(
"
s
h
a
n
j
u
_
c
2
b
"
)
;
/
/
服
务
类
型
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
B
o
d
y
(
q
r
C
o
d
e
D
t
o
.
g
e
t
B
o
d
y
(
)
)
;
/
/
订
单
内
容
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
j
s
o
n
S
t
r
i
n
g
 
=
 
J
S
O
N
.
t
o
J
S
O
N
S
t
r
i
n
g
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
 
 
 
 
 
 
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
 
s
e
r
v
i
c
e
 
c
r
e
a
t
e
S
t
o
r
e
Q
R
C
o
d
e
,
J
s
o
n
S
t
r
i
n
g
 
i
s
 
{
}
"
,
j
s
o
n
S
t
r
i
n
g
)
;
 
 
 
 
 
 
 
 
/
/
将
支
付
信
息
保
存
到
票
据
中
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 16 -->
3
.
4
.
3
 
商
户
平
台
应
用
生
成
二
维
码
 
3
.
4
.
3
.
1
 
接
口
实
现
 
1
、
配
置
参
数
定
义
c
扫
b
二
维
码
的
标
题
和
内
容
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
t
i
c
k
e
t
 
=
 
E
n
c
r
y
p
t
U
t
i
l
.
e
n
c
o
d
e
U
T
F
8
S
t
r
i
n
g
B
a
s
e
6
4
(
j
s
o
n
S
t
r
i
n
g
)
;
 
 
 
 
 
 
 
 
/
/
支
付
入
口
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
p
a
y
E
n
t
r
y
U
r
l
 
=
 
p
a
y
u
r
l
 
+
t
i
c
k
e
t
;
 
 
 
 
 
 
 
 
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
 
s
e
r
v
i
c
e
 
c
r
e
a
t
e
S
t
o
r
e
Q
R
C
o
d
e
,
p
a
y
‐
e
n
t
r
y
 
i
s
 
{
}
"
,
p
a
y
E
n
t
r
y
U
r
l
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
p
a
y
E
n
t
r
y
U
r
l
;
 
 
 
 
}
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
校
验
应
用
和
门
店
是
否
属
于
当
前
登
录
商
户
 
 
 
 
 
*
 
@
p
a
r
a
m
 
m
e
r
c
h
a
n
t
I
d
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
p
p
I
d
 
 
 
 
 
*
 
@
p
a
r
a
m
 
s
t
o
r
e
I
d
 
 
 
 
 
*
/
 
 
 
 
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
 
v
e
r
i
f
y
A
p
p
A
n
d
S
t
o
r
e
(
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
,
S
t
r
i
n
g
 
a
p
p
I
d
,
L
o
n
g
 
s
t
o
r
e
I
d
)
 
{
 
 
 
 
 
 
 
 
/
/
判
断
应
用
是
否
属
于
当
前
商
户
 
 
 
 
 
 
 
 
B
o
o
l
e
a
n
 
c
o
n
t
a
i
n
s
 
=
 
a
p
p
S
e
r
v
i
c
e
.
q
u
e
r
y
A
p
p
I
n
M
e
r
c
h
a
n
t
(
a
p
p
I
d
,
 
m
e
r
c
h
a
n
t
I
d
)
;
 
 
 
 
 
 
 
 
i
f
 
(
!
c
o
n
t
a
i
n
s
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
2
0
0
0
0
5
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
判
断
门
店
是
否
属
于
当
前
商
户
 
 
 
 
 
 
 
 
B
o
o
l
e
a
n
 
c
o
n
t
a
i
n
s
S
t
o
r
e
 
=
 
m
e
r
c
h
a
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
S
t
o
r
e
I
n
M
e
r
c
h
a
n
t
(
s
t
o
r
e
I
d
,
 
m
e
r
c
h
a
n
t
I
d
)
;
 
 
 
 
 
 
 
 
i
f
 
(
!
c
o
n
t
a
i
n
s
S
t
o
r
e
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
2
0
0
0
0
6
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 17 -->
内
容
 
如
下
：
 
2
、
定
义
接
口
 
s
h
a
n
j
u
p
a
y
:
 
 
c
2
b
:
 
 
 
 
s
u
b
j
e
c
t
:
 
"
%
s
商
品
"
 
 
 
 
b
o
d
y
:
 
"
向
%
s
付
款
"
/
*
*
*
 
门
店
二
维
码
订
单
标
题
*
/
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
s
h
a
n
j
u
p
a
y
.
c
2
b
.
s
u
b
j
e
c
t
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
 
s
u
b
j
e
c
t
;
 
/
*
*
*
 
门
店
二
维
码
订
单
内
容
*
/
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
s
h
a
n
j
u
p
a
y
.
c
2
b
.
b
o
d
y
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
 
b
o
d
y
;
 
@
A
p
i
O
p
e
r
a
t
i
o
n
(
"
生
成
商
户
应
用
门
店
二
维
码
"
)
 
 
 
 
 
 
 
 
@
A
p
i
I
m
p
l
i
c
i
t
P
a
r
a
m
s
(
{
 
 
 
 
 
 
 
 
 
 
 
 
@
A
p
i
I
m
p
l
i
c
i
t
P
a
r
a
m
(
n
a
m
e
 
=
 
"
a
p
p
I
d
"
,
 
v
a
l
u
e
 
=
 
"
商
户
应
用
i
d
"
,
 
r
e
q
u
i
r
e
d
 
=
 
t
r
u
e
,
 
d
a
t
a
T
y
p
e
 
=
 
"
S
t
r
i
n
g
"
,
 
p
a
r
a
m
T
y
p
e
 
=
 
"
p
a
t
h
"
)
,
 
 
 
 
 
 
 
 
 
 
 
 
@
A
p
i
I
m
p
l
i
c
i
t
P
a
r
a
m
(
n
a
m
e
 
=
 
"
s
t
o
r
e
I
d
"
,
 
v
a
l
u
e
 
=
 
"
商
户
门
店
i
d
"
,
 
r
e
q
u
i
r
e
d
 
=
 
t
r
u
e
,
 
d
a
t
a
T
y
p
e
 
=
 
"
S
t
r
i
n
g
"
,
 
p
a
r
a
m
T
y
p
e
 
=
 
"
p
a
t
h
"
)
,
 
 
 
 
}
)
 
 
 
 
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
m
y
/
a
p
p
s
/
{
a
p
p
I
d
}
/
s
t
o
r
e
s
/
{
s
t
o
r
e
I
d
}
/
a
p
p
‐
s
t
o
r
e
‐
q
r
c
o
d
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
 
c
r
e
a
t
e
C
S
c
a
n
B
S
t
o
r
e
Q
R
C
o
d
e
(
@
P
a
t
h
V
a
r
i
a
b
l
e
 
S
t
r
i
n
g
 
a
p
p
I
d
,
 
@
P
a
t
h
V
a
r
i
a
b
l
e
 
L
o
n
g
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 18 -->
3
.
4
.
3
.
2
 
 
测
试
 
1
、
请
求
认
证
，
获
取
t
o
k
e
n
及
租
户
i
d
2
、
请
求
获
取
二
维
码
注
意
：
应
用
及
门
店
的
合
法
性
 
4
 
支
付
入
口
 
s
t
o
r
e
I
d
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
 
 
 
/
/
商
户
i
d
 
 
 
 
 
 
 
 
L
o
n
g
 
m
e
r
c
h
a
n
t
I
d
 
=
 
S
e
c
u
r
i
t
y
U
t
i
l
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
;
 
 
 
 
 
 
 
 
/
/
生
成
二
维
码
链
接
 
 
 
 
 
 
 
 
Q
R
C
o
d
e
D
t
o
 
q
r
C
o
d
e
D
t
o
 
=
 
n
e
w
 
Q
R
C
o
d
e
D
t
o
(
)
;
 
 
 
 
 
 
 
 
q
r
C
o
d
e
D
t
o
.
s
e
t
M
e
r
c
h
a
n
t
I
d
(
m
e
r
c
h
a
n
t
I
d
)
;
 
 
 
 
 
 
 
 
q
r
C
o
d
e
D
t
o
.
s
e
t
A
p
p
I
d
(
a
p
p
I
d
)
;
 
 
 
 
 
 
 
 
q
r
C
o
d
e
D
t
o
.
s
e
t
S
t
o
r
e
I
d
(
s
t
o
r
e
I
d
)
;
 
 
 
 
 
 
 
 
/
/
标
题
 
 
 
 
 
 
 
 
M
e
r
c
h
a
n
t
D
T
O
 
m
e
r
c
h
a
n
t
D
T
O
 
=
 
m
e
r
c
h
a
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
M
e
r
c
h
a
n
t
B
y
I
d
(
m
e
r
c
h
a
n
t
I
d
)
;
 
 
 
 
 
 
 
 
/
/
"
%
s
 
商
品
"
 
 
 
 
 
 
 
 
q
r
C
o
d
e
D
t
o
.
s
e
t
S
u
b
j
e
c
t
(
S
t
r
i
n
g
.
f
o
r
m
a
t
(
s
u
b
j
e
c
t
,
m
e
r
c
h
a
n
t
D
T
O
.
g
e
t
M
e
r
c
h
a
n
t
N
a
m
e
(
)
)
)
;
 
 
 
 
 
 
 
 
/
/
内
容
,
格
式
：
"
向
%
s
 
付
款
"
 
 
 
 
 
 
 
 
q
r
C
o
d
e
D
t
o
.
s
e
t
B
o
d
y
(
S
t
r
i
n
g
.
f
o
r
m
a
t
(
b
o
d
y
,
m
e
r
c
h
a
n
t
D
T
O
.
g
e
t
M
e
r
c
h
a
n
t
N
a
m
e
(
)
)
)
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
s
t
o
r
e
Q
R
C
o
d
e
U
r
l
 
=
 
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
S
e
r
v
i
c
e
.
c
r
e
a
t
e
S
t
o
r
e
Q
R
C
o
d
e
(
q
r
C
o
d
e
D
t
o
)
;
 
 
 
 
 
 
 
 
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
[
m
e
r
c
h
a
n
t
I
d
:
{
}
,
a
p
p
I
d
:
{
}
,
s
t
o
r
e
I
d
:
{
}
]
c
r
e
a
t
e
C
S
c
a
n
B
S
t
o
r
e
Q
R
C
o
d
e
 
i
s
 
{
}
"
,
m
e
r
c
h
a
n
t
I
d
,
a
p
p
I
d
,
s
t
o
r
e
I
d
,
s
t
o
r
e
Q
R
C
o
d
e
U
r
l
)
;
 
 
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
根
据
返
回
u
r
l
，
调
用
生
成
二
维
码
工
具
类
，
生
成
二
维
码
b
a
s
e
6
4
返
回
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
Q
R
C
o
d
e
U
t
i
l
.
c
r
e
a
t
e
Q
R
C
o
d
e
(
s
t
o
r
e
Q
R
C
o
d
e
U
r
l
,
 
2
0
0
,
 
2
0
0
)
;
 
 
 
 
 
 
 
 
}
 
c
a
t
c
h
 
(
I
O
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
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
2
0
0
0
0
7
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 19 -->
4
 
支
付
入
口
 
4
.
1
 
需
求
分
析
 
买
方
扫
描
门
店
二
维
码
，
进
入
支
付
入
口
 
即
进
入
订
单
确
认
页
面
，
流
程
如
下
：
1
）
顾
客
扫
描
二
维
码
2
）
进
入
订
单
确
认
页
面
 
 
4
.
2
 
F
r
e
e
m
a
r
k
e
r
技
术
预
研
 
支
付
确
认
页
面
由
服
务
端
渲
染
生
成
，
常
用
的
技
术
有
j
s
p
、
f
r
e
e
m
a
r
k
e
r
 
v
e
l
o
c
i
t
y
 
T
h
y
m
e
l
e
a
f
等
。
本
项
目
采
用
f
r
e
e
m
a
r
k
e
r
模
板
引
擎
，
参
考
f
r
e
e
m
a
r
k
e
r
基
础
v
1
.
1
.
p
d
f
。
 
4
.
3
 
交
易
服
务
支
付
入
口
 
交
互
流
程
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 20 -->
1
、
顾
客
扫
描
二
维
码
，
请
求
交
易
服
务
支
付
入
口
2
、
交
易
服
务
解
析
请
求
，
生
成
支
付
确
认
页
面
3
、
交
易
服
务
向
服
务
响
应
支
付
确
认
页
面
4
.
3
.
1
 
支
付
确
认
页
面
 
1
、
从
资
料
-
>
代
码
拷
贝
p
a
y
.
h
t
m
l
、
p
a
y
_
e
r
r
o
r
.
h
t
m
l
到
交
易
服
务
工
程
下
。
 
2
、
在
交
易
服
务
接
口
实
现
工
程
的
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
依
赖
 
3
、
在
N
a
c
o
s
中
配
置
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
f
r
e
e
m
a
r
k
e
r
.
y
a
m
l
，
G
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
 
 
 
 
 
 
 
 
 
<
!
‐
‐
 
f
r
e
e
m
a
r
k
e
r
依
赖
 
‐
‐
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
f
r
e
e
m
a
r
k
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
#
f
r
e
e
m
a
r
k
e
r
基
本
配
置
s
p
r
i
n
g
:
 
 
f
r
e
e
m
a
r
k
e
r
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
 
 
 
 
r
e
q
u
e
s
t
‐
c
o
n
t
e
x
t
‐
a
t
t
r
i
b
u
t
e
:
 
r
c
 
 
 
 
c
o
n
t
e
n
t
‐
t
y
p
e
:
 
t
e
x
t
/
h
t
m
l
 
 
 
 
s
u
f
f
i
x
:
 
.
h
t
m
l
 
 
 
 
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
 
 
r
e
s
o
u
r
c
e
s
:
 
 
 
 
a
d
d
‐
m
a
p
p
i
n
g
s
:
 
f
a
l
s
e
 
#
关
闭
工
程
中
默
认
的
资
源
处
理
 
 
m
v
c
:
 
 
 
 
t
h
r
o
w
‐
e
x
c
e
p
t
i
o
n
‐
i
f
‐
n
o
‐
h
a
n
d
l
e
r
‐
f
o
u
n
d
:
 
t
r
u
e
 
#
出
现
错
误
时
直
接
抛
出
异
常
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 21 -->
在
s
h
a
n
j
u
p
a
y
-
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
-
s
e
r
v
i
c
e
工
程
的
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
引
入
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
f
r
e
e
m
a
r
k
e
r
.
y
a
m
l
 
4
、
新
建
W
e
b
M
v
c
C
o
n
ﬁ
g
配
置
确
认
支
付
页
面
视
图
名
：
 
5
、
定
义
支
付
入
口
接
口
注
意
：
P
a
y
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
要
向
前
端
响
应
页
面
，
使
用
@
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
注
解
。
 
 
 
 
 
 
 
 
 
 
 
‐
 
 
 
 
 
 
 
 
 
 
 
 
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
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
‐
i
d
:
 
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
f
r
e
e
m
a
r
k
e
r
.
y
a
m
l
 
#
 
s
p
r
i
n
g
 
b
o
o
t
 
f
r
e
e
m
a
r
k
e
r
配
置
 
 
 
 
 
 
 
 
 
 
 
 
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
 
#
 
通
用
配
置
组
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
s
h
a
n
j
u
p
a
y
.
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
.
c
o
n
f
i
g
;
 
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
 
W
e
b
M
v
c
C
o
n
f
i
g
 
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
 
W
e
b
M
v
c
C
o
n
f
i
g
u
r
e
r
 
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
 
v
o
i
d
 
a
d
d
V
i
e
w
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
s
(
V
i
e
w
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
R
e
g
i
s
t
r
y
 
r
e
g
i
s
t
r
y
)
 
{
 
 
 
 
 
 
 
 
r
e
g
i
s
t
r
y
.
a
d
d
V
i
e
w
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
(
"
/
p
a
y
‐
p
a
g
e
"
)
.
s
e
t
V
i
e
w
N
a
m
e
(
"
p
a
y
"
)
;
 
 
 
 
}
}
@
S
l
f
4
j
@
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
 
P
a
y
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
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
支
付
入
口
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 22 -->
6
、
测
试
页
面
渲
染
1
）
在
n
a
c
o
s
配
置
网
关
转
发
到
交
易
服
务
的
路
由
2
）
用
c
h
r
o
m
e
浏
览
器
访
问
（
用
手
机
视
图
模
式
）
二
维
码
的
统
一
入
口
地
址
。
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
1
0
/
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
/
p
a
y
-
e
n
t
r
y
/
.
.
.
注
意
：
由
于
没
有
数
据
，
订
单
信
息
均
为
空
。
 
 
 
 
 
*
 
@
p
a
r
a
m
 
t
i
c
k
e
t
 
 
 
 
 
*
 
@
p
a
r
a
m
 
t
y
p
e
 
 
 
 
 
*
 
@
p
a
r
a
m
 
r
e
q
u
e
s
t
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
 
 
 
 
*
/
 
 
 
 
@
R
e
q
u
e
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
p
a
y
‐
e
n
t
r
y
/
{
t
i
c
k
e
t
}
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
 
p
a
y
E
n
t
r
y
(
@
P
a
t
h
V
a
r
i
a
b
l
e
(
"
t
i
c
k
e
t
"
)
 
S
t
r
i
n
g
 
t
i
c
k
e
t
,
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
)
 
{
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
"
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 23 -->
4
.
3
.
2
 
页
面
完
善
 
前
边
测
试
的
支
付
确
认
页
面
由
于
没
有
数
据
所
以
显
示
为
空
，
下
边
对
页
面
进
行
完
善
。
1
、
页
面
完
善
需
求
如
下
：
1
）
进
入
支
付
入
口
，
传
入
t
i
c
k
e
t
，
需
要
解
析
t
i
c
k
e
t
得
到
订
单
信
息
，
在
支
付
确
认
页
面
显
示
。
2
）
解
析
出
客
户
端
类
型
，
目
前
支
付
微
信
、
支
付
宝
两
种
。
4
.
3
.
2
.
1
 
解
析
t
i
c
k
e
t
 
拷
贝
资
料
-
-
>
代
码
下
的
P
a
y
O
r
d
e
r
D
T
O
.
j
a
v
a
、
P
a
y
O
r
d
e
r
C
o
n
v
e
r
t
.
j
a
v
a
到
交
易
服
务
工
程
。
解
析
t
i
c
k
e
t
代
码
如
下
：
 
4
.
3
.
2
.
2
 
解
析
客
户
端
类
型
 
1
、
拷
贝
到
资
料
-
-
>
代
码
下
的
B
r
o
w
s
e
r
T
y
p
e
.
j
a
v
a
到
交
易
服
务
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
包
下
，
此
类
是
系
统
定
义
的
客
户
端
配
置
类
型
。
2
、
修
改
支
付
入
口
代
码
：
@
R
e
q
u
e
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
p
a
y
‐
e
n
t
r
y
/
{
t
i
c
k
e
t
}
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
 
p
a
y
E
n
t
r
y
(
@
P
a
t
h
V
a
r
i
a
b
l
e
(
"
t
i
c
k
e
t
"
)
 
S
t
r
i
n
g
 
t
i
c
k
e
t
,
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
)
 
{
 
 
 
 
/
/
将
t
i
c
k
e
t
的
b
a
s
e
6
4
还
原
 
 
 
 
S
t
r
i
n
g
 
t
i
c
k
e
t
S
t
r
 
=
 
E
n
c
r
y
p
t
U
t
i
l
.
d
e
c
o
d
e
U
T
F
8
S
t
r
i
n
g
B
a
s
e
6
4
(
t
i
c
k
e
t
)
;
 
 
 
 
/
/
将
t
i
c
k
e
t
（
j
s
o
n
）
转
成
对
象
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
o
r
d
e
r
 
=
 
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
t
i
c
k
e
t
S
t
r
,
 
P
a
y
O
r
d
e
r
D
T
O
.
c
l
a
s
s
)
;
 
 
 
 
/
/
将
对
象
转
成
u
r
l
格
式
 
 
 
 
S
t
r
i
n
g
 
p
a
r
a
m
s
 
=
 
P
a
r
s
e
U
R
L
P
a
i
r
U
t
i
l
.
p
a
r
s
e
U
R
L
P
a
i
r
(
o
r
d
e
r
)
;
 
 
 
 
r
e
t
u
r
n
 
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
?
"
 
+
 
p
a
r
a
m
s
;
}
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 24 -->
4
.
3
.
3
 
接
口
测
试
 
由
于
添
加
上
了
客
户
端
类
型
的
解
析
，
使
用
微
信
或
支
付
宝
扫
码
方
可
进
入
支
付
入
口
，
需
要
使
用
模
拟
器
进
行
测
试
。
1
、
修
改
支
付
入
口
地
址
修
改
为
模
拟
器
可
以
访
问
到
的
地
址
，
模
拟
器
安
装
在
开
发
电
脑
上
，
支
付
入
口
地
址
修
改
为
开
发
电
脑
局
域
网
的
地
址
。
@
R
e
q
u
e
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
p
a
y
‐
e
n
t
r
y
/
{
t
i
c
k
e
t
}
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
 
p
a
y
E
n
t
r
y
(
@
P
a
t
h
V
a
r
i
a
b
l
e
(
"
t
i
c
k
e
t
"
)
 
S
t
r
i
n
g
 
t
i
c
k
e
t
,
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
)
 
{
 
 
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
将
t
i
c
k
e
t
的
b
a
s
e
6
4
还
原
 
 
 
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
t
i
c
k
e
t
S
t
r
 
=
 
E
n
c
r
y
p
t
U
t
i
l
.
d
e
c
o
d
e
U
T
F
8
S
t
r
i
n
g
B
a
s
e
6
4
(
t
i
c
k
e
t
)
;
 
 
 
 
 
 
 
 
 
 
 
 
/
/
将
t
i
c
k
e
t
（
j
s
o
n
）
转
成
对
象
 
 
 
 
 
 
 
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
o
r
d
e
r
 
=
 
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
t
i
c
k
e
t
S
t
r
,
 
P
a
y
O
r
d
e
r
D
T
O
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
 
 
 
 
 
/
/
将
对
象
转
成
u
r
l
格
式
/
/
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
u
r
l
 
=
 
t
o
P
a
r
a
m
s
S
t
r
i
n
g
(
o
r
d
e
r
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
B
r
o
w
s
e
r
T
y
p
e
 
b
r
o
w
s
e
r
T
y
p
e
 
=
 
B
r
o
w
s
e
r
T
y
p
e
.
v
a
l
u
e
O
f
U
s
e
r
A
g
e
n
t
(
r
e
q
u
e
s
t
.
g
e
t
H
e
a
d
e
r
(
"
u
s
e
r
‐
a
g
e
n
t
"
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
s
w
i
t
c
h
 
(
b
r
o
w
s
e
r
T
y
p
e
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
s
e
 
A
L
I
P
A
Y
:
 
/
/
直
接
跳
转
收
银
台
p
a
y
.
h
t
m
l
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
?
"
 
+
 
P
a
r
s
e
U
R
L
P
a
i
r
U
t
i
l
.
p
a
r
s
e
U
R
L
P
a
i
r
(
o
r
d
e
r
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
s
e
 
W
E
C
H
A
T
:
 
/
/
获
取
授
权
码
(
待
实
现
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
?
"
 
+
 
P
a
r
s
e
U
R
L
P
a
i
r
U
t
i
l
.
p
a
r
s
e
U
R
L
P
a
i
r
(
o
r
d
e
r
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
:
 
 
 
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
}
c
a
t
c
h
 
(
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
)
{
 
 
 
 
 
 
 
 
 
 
 
 
e
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
 
 
 
 
 
 
 
 
 
 
 
 
l
o
g
.
e
r
r
o
r
(
e
.
g
e
t
M
e
s
s
a
g
e
(
)
,
e
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
‐
e
r
r
o
r
"
;
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 25 -->
2
、
生
成
门
店
二
维
码
3
、
使
用
模
拟
器
运
行
支
付
宝
沙
箱
A
P
P
，
扫
描
二
维
码
查
看
支
付
确
认
页
面
5
 
立
即
支
付
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 26 -->
5
 
立
即
支
付
 
5
.
1
 
需
求
分
析
 
顾
客
扫
码
进
入
支
付
确
认
页
面
，
输
入
金
额
，
点
击
立
即
支
付
，
打
开
支
付
客
户
端
（
微
信
或
支
付
宝
）
，
输
入
支
付
密
码
完
成
支
付
。
立
即
支
付
需
要
调
用
第
三
方
支
付
渠
道
的
统
一
下
单
接
口
，
本
章
节
完
成
支
付
宝
统
一
下
单
接
口
对
接
。
交
互
流
程
如
下
：
支
付
渠
道
代
理
服
务
介
绍
：
有
支
付
需
求
的
微
服
务
统
一
通
过
支
付
渠
道
代
理
服
务
调
用
“
第
三
方
支
付
服
务
”
提
供
的
接
口
，
这
样
做
的
好
处
由
支
付
渠
道
代
理
服
务
将
第
三
方
支
付
系
统
和
闪
聚
支
付
内
部
服
务
进
行
解
耦
合
。
整
体
执
行
流
程
如
下
：
1
、
顾
客
输
入
金
额
，
点
击
立
即
支
付
2
、
请
求
交
易
服
务
，
交
易
服
务
保
存
订
单
3
、
交
易
服
务
调
用
支
付
渠
道
代
理
服
务
的
支
付
宝
下
单
接
口
4
、
支
付
渠
道
代
理
服
务
调
用
支
付
宝
的
统
一
下
单
接
口
。
5
、
支
付
凭
证
返
回
 
5
.
2
 
搭
建
支
付
渠
道
代
理
工
程
 
支
付
渠
道
代
理
服
务
包
括
如
下
工
程
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 27 -->
服
务
名
职
责
支
付
渠
道
代
理
服
务
A
P
I
(
s
h
a
n
j
u
p
a
y
-
p
a
y
m
e
n
t
-
a
g
e
n
t
-
a
p
i
)
定
义
支
付
渠
道
代
理
服
务
提
供
的
接
口
支
付
渠
道
代
理
服
务
(
s
h
a
n
j
u
p
a
y
-
p
a
y
m
e
n
t
-
a
g
e
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
)
实
现
支
付
渠
道
代
理
服
务
的
所
有
接
口
1
.
 
复
制
提
供
的
s
h
a
n
j
u
p
a
y
-
p
a
y
m
e
n
t
-
a
g
e
n
t
目
录
到
s
h
a
n
j
u
p
a
y
根
目
录
2
.
 
添
加
M
o
d
u
l
e
到
I
D
E
A
中
3
.
 
在
N
a
c
o
s
中
添
加
p
a
y
m
e
n
t
-
a
g
e
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
.
y
a
m
l
配
置
，
G
r
o
u
p
:
 
S
H
A
N
J
U
P
A
Y
_
G
R
O
U
P
 
4
.
 
打
开
s
h
a
n
j
u
p
a
y
-
p
a
y
m
e
n
t
-
a
g
e
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
工
程
的
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
，
将
其
中
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
替
换
为
自
己
创
建
的
d
e
v
命
名
空
间
I
D
5
.
 
启
动
P
a
y
m
e
n
t
A
g
e
n
t
B
o
o
t
s
t
r
a
p
测
试
：
s
e
r
v
e
r
:
 
 
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
p
a
y
m
e
n
t
‐
r
e
c
e
i
v
e
r
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 28 -->
5
.
3
 
支
付
渠
道
代
理
服
务
支
付
宝
下
单
 
5
.
3
.
1
 
接
口
定
义
 
5
.
3
.
1
.
1
 
支
付
宝
接
口
参
数
 
支
付
渠
道
代
理
服
务
调
用
支
付
宝
手
机
网
站
下
单
接
口
，
下
边
梳
理
接
口
的
参
数
：
公
共
参
数
如
下
：
标
记
蓝
色
的
由
s
d
k
设
置
、
标
记
红
色
的
已
在
支
付
渠
道
参
数
配
置
中
（
需
要
支
付
渠
道
代
理
服
务
接
口
处
理
）
，
标
记
绿
色
的
需
支
付
渠
道
代
理
服
务
接
口
处
理
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 29 -->
业
务
参
数
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 30 -->
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 31 -->
5
.
3
.
1
.
2
 
接
口
定
义
 
1
、
接
口
描
述
：
调
用
支
付
宝
手
机
w
a
p
下
单
接
口
2
、
接
口
定
义
在
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
中
定
义
接
口
：
 
5
.
3
.
2
 
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
s
h
a
n
j
u
p
a
y
.
p
a
y
m
e
n
t
a
g
e
n
t
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
 
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
 
{
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
调
用
支
付
宝
手
机
W
A
P
下
单
接
口
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
支
付
渠
道
参
数
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
l
i
p
a
y
B
e
a
n
 
请
求
支
付
参
数
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
 
 
 
 
*
 
@
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
 
 
 
 
*
/
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
A
l
i
W
A
P
(
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
A
l
i
p
a
y
B
e
a
n
 
a
l
i
p
a
y
B
e
a
n
)
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
;
}
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
@
S
l
f
4
j
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
 
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
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
 
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
 
{
 
 
 
 
/
*
*
 
 
 
 
 
*
 
调
用
支
付
宝
手
机
W
A
P
下
单
接
口
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
支
付
渠
道
参
数
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
l
i
p
a
y
B
e
a
n
 
 
 
 
 
请
求
支
付
参
数
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 32 -->
*
 
@
r
e
t
u
r
n
 
 
 
 
 
*
 
@
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
 
 
 
 
*
/
 
 
 
 
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
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
A
l
i
W
A
P
(
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
A
l
i
p
a
y
B
e
a
n
 
a
l
i
p
a
y
B
e
a
n
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
 
 
 
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
支
付
宝
请
求
参
数
"
,
 
a
l
i
p
a
y
B
e
a
n
.
t
o
S
t
r
i
n
g
(
)
)
;
 
 
 
 
 
 
 
 
 
/
/
支
付
宝
渠
道
参
数
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
g
a
t
e
w
a
y
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
U
r
l
(
)
;
/
/
支
付
宝
下
单
接
口
地
址
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
I
d
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
p
p
I
d
(
)
;
/
/
a
p
p
i
d
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
r
s
a
P
r
i
v
a
t
e
K
e
y
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
R
s
a
P
r
i
v
a
t
e
K
e
y
(
)
;
/
/
私
钥
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
f
o
r
m
a
t
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
F
o
r
m
a
t
(
)
;
/
/
数
据
格
式
j
s
o
n
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
c
h
a
r
e
s
t
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
C
h
a
r
e
s
t
(
)
;
/
/
字
符
编
码
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
a
l
i
p
a
y
P
u
b
l
i
c
K
e
y
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
l
i
p
a
y
P
u
b
l
i
c
K
e
y
(
)
;
 
/
/
公
钥
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
s
i
g
n
t
y
p
e
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
S
i
g
n
t
y
p
e
(
)
;
/
/
签
名
算
法
类
型
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
n
o
t
i
f
y
U
r
l
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
N
o
t
i
f
y
U
r
l
(
)
;
/
/
支
付
结
果
通
知
地
址
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
r
e
t
u
r
n
U
r
l
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
R
e
t
u
r
n
U
r
l
(
)
;
/
/
支
付
完
成
返
回
商
户
地
址
 
 
 
 
 
 
 
 
 
/
/
支
付
宝
s
d
k
客
户
端
 
 
 
 
 
 
 
 
A
l
i
p
a
y
C
l
i
e
n
t
 
c
l
i
e
n
t
 
=
 
n
e
w
 
D
e
f
a
u
l
t
A
l
i
p
a
y
C
l
i
e
n
t
(
g
a
t
e
w
a
y
,
 
a
p
p
I
d
,
 
r
s
a
P
r
i
v
a
t
e
K
e
y
,
 
f
o
r
m
a
t
,
 
c
h
a
r
e
s
t
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
P
u
b
l
i
c
K
e
y
,
 
s
i
g
n
t
y
p
e
)
;
 
 
 
 
 
 
 
 
 
/
/
 
封
装
请
求
支
付
信
息
 
 
 
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
W
a
p
P
a
y
R
e
q
u
e
s
t
 
a
l
i
p
a
y
R
e
q
u
e
s
t
 
=
 
n
e
w
 
A
l
i
p
a
y
T
r
a
d
e
W
a
p
P
a
y
R
e
q
u
e
s
t
(
)
;
 
 
 
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
W
a
p
P
a
y
M
o
d
e
l
 
m
o
d
e
l
 
=
 
n
e
w
 
A
l
i
p
a
y
T
r
a
d
e
W
a
p
P
a
y
M
o
d
e
l
(
)
;
 
 
 
 
 
 
 
 
m
o
d
e
l
.
s
e
t
O
u
t
T
r
a
d
e
N
o
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
)
;
/
/
闪
聚
平
台
订
单
 
 
 
 
 
 
 
 
m
o
d
e
l
.
s
e
t
S
u
b
j
e
c
t
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
S
u
b
j
e
c
t
(
)
)
;
/
/
订
单
标
题
 
 
 
 
 
 
 
 
m
o
d
e
l
.
s
e
t
T
o
t
a
l
A
m
o
u
n
t
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
T
o
t
a
l
A
m
o
u
n
t
(
)
)
;
/
/
订
单
金
额
 
 
 
 
 
 
 
 
m
o
d
e
l
.
s
e
t
B
o
d
y
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
B
o
d
y
(
)
)
;
/
/
订
单
内
容
 
 
 
 
 
 
 
 
m
o
d
e
l
.
s
e
t
T
i
m
e
o
u
t
E
x
p
r
e
s
s
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
E
x
p
i
r
e
T
i
m
e
(
)
)
;
/
/
订
单
过
期
时
间
 
 
 
 
 
 
 
 
m
o
d
e
l
.
s
e
t
P
r
o
d
u
c
t
C
o
d
e
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
P
r
o
d
u
c
t
C
o
d
e
(
)
)
;
/
/
商
户
与
支
付
宝
签
定
的
产
品
码
，
固
定
为
Q
U
I
C
K
_
W
A
P
_
W
A
Y
 
 
 
 
 
 
 
 
a
l
i
p
a
y
R
e
q
u
e
s
t
.
s
e
t
B
i
z
M
o
d
e
l
(
m
o
d
e
l
)
;
/
/
请
求
参
数
集
合
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
j
s
o
n
S
t
r
i
n
g
 
=
 
J
S
O
N
.
t
o
J
S
O
N
S
t
r
i
n
g
(
a
l
i
p
a
y
B
e
a
n
)
;
 
 
 
 
 
 
 
 
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
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
A
l
i
W
A
P
.
.
a
l
i
p
a
y
R
e
q
u
e
s
t
:
{
}
"
,
j
s
o
n
S
t
r
i
n
g
)
;
 
 
 
 
 
 
 
 
/
/
 
设
置
异
步
通
知
地
址
 
 
 
 
 
 
 
 
a
l
i
p
a
y
R
e
q
u
e
s
t
.
s
e
t
N
o
t
i
f
y
U
r
l
(
n
o
t
i
f
y
U
r
l
)
;
 
 
 
 
 
 
 
 
/
/
 
设
置
同
步
地
址
 
 
 
 
 
 
 
 
a
l
i
p
a
y
R
e
q
u
e
s
t
.
s
e
t
R
e
t
u
r
n
U
r
l
(
r
e
t
u
r
n
U
r
l
)
;
 
 
 
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
 
调
用
S
D
K
提
交
表
单
 
 
 
 
 
 
 
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
W
a
p
P
a
y
R
e
s
p
o
n
s
e
 
r
e
s
p
o
n
s
e
 
=
 
c
l
i
e
n
t
.
p
a
g
e
E
x
e
c
u
t
e
(
a
l
i
p
a
y
R
e
q
u
e
s
t
)
;
 
 
 
 
 
 
 
 
 
 
 
 
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
支
付
宝
手
机
网
站
支
付
预
支
付
订
单
信
息
"
 
+
 
r
e
s
p
o
n
s
e
)
;
 
 
 
 
 
 
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
 
=
 
n
e
w
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
(
)
;
 
 
 
 
 
 
 
 
 
 
 
 
r
e
s
.
s
e
t
C
o
n
t
e
n
t
(
r
e
s
p
o
n
s
e
.
g
e
t
B
o
d
y
(
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
;
 
 
 
 
 
 
 
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
e
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
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
4
0
0
0
0
2
)
;
/
/
支
付
宝
确
认
支
付
失
败
 
 
 
 
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 33 -->
5
.
4
 
交
易
服
务
支
付
宝
下
单
 
5
.
4
.
1
 
接
口
定
义
 
交
易
服
务
支
付
宝
下
单
是
提
供
给
支
付
入
口
请
求
的
支
付
宝
付
款
接
口
，
当
用
户
用
支
付
宝
客
户
端
扫
描
二
维
码
进
入
确
认
支
付
页
面
，
点
击
确
认
支
付
即
将
请
求
此
接
口
。
1
、
接
口
描
述
1
）
接
收
前
端
支
付
请
求
2
）
保
存
订
单
信
息
到
闪
聚
支
付
平
台
3
）
调
用
支
付
渠
道
代
理
服
务
请
求
支
付
宝
下
单
接
口
4
）
将
支
付
宝
下
单
接
口
响
应
结
果
返
回
到
前
端
，
前
端
开
始
进
行
支
付
 
2
、
接
口
定
义
在
P
a
y
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
定
义
接
口
如
下
：
定
义
O
r
d
e
r
C
o
n
ﬁ
r
m
V
O
接
收
前
端
请
求
的
支
付
参
数
：
 
接
口
定
义
如
下
：
 
 
 
 
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
s
h
a
n
j
u
p
a
y
.
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
.
v
o
;
 
i
m
p
o
r
t
 
i
o
.
s
w
a
g
g
e
r
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
s
.
A
p
i
M
o
d
e
l
;
i
m
p
o
r
t
 
l
o
m
b
o
k
.
D
a
t
a
;
 
@
A
p
i
M
o
d
e
l
(
v
a
l
u
e
 
=
 
"
O
r
d
e
r
C
o
n
f
i
r
m
V
O
"
,
 
d
e
s
c
r
i
p
t
i
o
n
 
=
 
"
订
单
确
认
信
息
"
)
@
D
a
t
a
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
 
O
r
d
e
r
C
o
n
f
i
r
m
V
O
 
{
 
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
 
a
p
p
I
d
;
 
/
/
应
用
i
d
 
 
 
 
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
 
t
r
a
d
e
N
o
;
/
/
交
易
单
号
 
 
 
 
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
 
o
p
e
n
I
d
;
/
/
微
信
o
p
e
n
i
d
 
 
 
 
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
t
o
r
e
I
d
;
/
/
门
店
i
d
 
 
 
 
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
h
a
n
n
e
l
;
 
/
/
服
务
类
型
 
 
 
 
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
 
b
o
d
y
;
/
/
订
单
描
述
 
 
 
 
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
u
b
j
e
c
t
;
/
/
订
单
标
题
 
 
 
 
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
 
t
o
t
a
l
A
m
o
u
n
t
;
/
/
金
额
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 34 -->
@
A
p
i
O
p
e
r
a
t
i
o
n
(
"
支
付
宝
门
店
下
单
付
款
"
)
 
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
"
/
c
r
e
a
t
e
A
l
i
P
a
y
O
r
d
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
 
v
o
i
d
 
c
r
e
a
t
e
A
l
i
p
a
y
O
r
d
e
r
F
o
r
S
t
o
r
e
(
O
r
d
e
r
C
o
n
f
i
r
m
V
O
 
o
r
d
e
r
C
o
n
f
i
r
m
V
O
,
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
,
 
H
t
t
p
S
e
r
v
l
e
t
R
e
s
p
o
n
s
e
 
r
e
s
p
o
n
s
e
)
 
 
 
 
 
 
 
t
h
r
o
w
s
 
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
 
 
 
 
 
}
 
 
5
.
4
.
2
 
接
口
实
现
 
5
.
4
.
2
.
1
 
保
存
订
单
 
1
、
拷
贝
资
料
-
-
》
代
码
中
的
I
d
W
o
r
k
e
r
U
t
i
l
s
.
j
a
v
a
、
P
a
y
m
e
n
t
U
t
i
l
.
j
a
v
a
工
具
类
到
c
o
m
m
o
n
 
工
程
。
2
、
在
T
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
S
e
r
v
i
c
e
I
m
p
l
中
编
写
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
方
法
。
/
*
*
 
 
*
 
支
付
宝
订
单
保
存
 
 
*
 
 
*
 
@
p
a
r
a
m
 
p
a
y
O
r
d
e
r
D
T
O
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
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
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
(
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
)
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
/
/
保
存
订
单
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
P
a
y
C
h
a
n
n
e
l
(
"
A
L
I
P
A
Y
_
W
A
P
"
)
;
 
 
 
 
 
/
/
保
存
订
单
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
s
a
v
e
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
/
/
调
用
支
付
代
理
服
务
请
求
第
三
方
支
付
系
统
 
 
/
/
.
.
.
 
 
 
 
 
r
e
t
u
r
n
 
n
u
l
l
;
 
}
 
3
、
编
写
保
存
订
单
的
方
法
，
此
方
法
由
/
*
*
 
 
*
 
保
存
订
单
到
闪
聚
平
台
 
 
*
 
 
*
 
@
p
a
r
a
m
 
p
a
y
O
r
d
e
r
D
T
O
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
p
r
i
v
a
t
e
 
P
a
y
O
r
d
e
r
D
T
O
 
s
a
v
e
(
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
P
a
y
O
r
d
e
r
 
e
n
t
i
t
y
 
=
 
P
a
y
O
r
d
e
r
C
o
n
v
e
r
t
.
I
N
S
T
A
N
C
E
.
d
t
o
2
e
n
t
i
t
y
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
 
 
 
e
n
t
i
t
y
.
s
e
t
T
r
a
d
e
N
o
(
P
a
y
m
e
n
t
U
t
i
l
.
g
e
n
U
n
i
q
u
e
P
a
y
O
r
d
e
r
N
o
(
)
)
;
 
 
 
 
 
/
/
订
单
创
建
时
间
 
 
 
 
 
e
n
t
i
t
y
.
s
e
t
C
r
e
a
t
e
T
i
m
e
(
L
o
c
a
l
D
a
t
e
T
i
m
e
.
n
o
w
(
)
)
;
 
 
 
 
 
/
/
设
置
过
期
时
间
，
3
0
分
钟
 
 
 
 
 
e
n
t
i
t
y
.
s
e
t
E
x
p
i
r
e
T
i
m
e
(
L
o
c
a
l
D
a
t
e
T
i
m
e
.
n
o
w
(
)
.
p
l
u
s
(
3
0
,
 
C
h
r
o
n
o
U
n
i
t
.
M
I
N
U
T
E
S
)
)
;
 
 
 
 
 
e
n
t
i
t
y
.
s
e
t
C
u
r
r
e
n
c
y
(
"
C
N
Y
"
)
;
/
/
设
置
支
付
币
种
 
 
 
 
 
e
n
t
i
t
y
.
s
e
t
T
r
a
d
e
S
t
a
t
e
(
"
0
"
)
;
/
/
订
单
状
态
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 35 -->
i
n
t
 
i
n
s
e
r
t
 
=
 
p
a
y
O
r
d
e
r
M
a
p
p
e
r
.
i
n
s
e
r
t
(
e
n
t
i
t
y
)
;
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
O
r
d
e
r
C
o
n
v
e
r
t
.
I
N
S
T
A
N
C
E
.
e
n
t
i
t
y
2
d
t
o
(
e
n
t
i
t
y
)
;
 
}
 
 
 
5
.
4
.
2
.
2
 
请
求
代
理
服
务
调
用
支
付
宝
下
单
 
在
T
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
S
e
r
v
i
c
e
I
m
p
l
中
编
写
私
有
方
法
，
实
现
请
求
代
理
服
务
调
用
支
付
宝
下
单
接
口
。
此
私
有
方
法
被
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
方
法
调
用
。
 
/
/
调
用
支
付
宝
下
单
接
口
 
 
 
 
 
p
r
i
v
a
t
e
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
a
l
i
p
a
y
H
5
(
S
t
r
i
n
g
 
t
r
a
d
e
N
o
)
 
{
 
 
 
 
 
 
 
 
 
/
/
构
建
支
付
实
体
 
 
 
 
 
 
 
 
 
A
l
i
p
a
y
B
e
a
n
 
a
l
i
p
a
y
B
e
a
n
 
=
 
n
e
w
 
A
l
i
p
a
y
B
e
a
n
(
)
;
 
 
 
 
 
 
 
 
 
 
/
/
根
据
订
单
号
查
询
订
单
详
情
 
 
 
 
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
q
u
e
r
y
P
a
y
O
r
d
e
r
(
t
r
a
d
e
N
o
)
;
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
B
e
a
n
.
s
e
t
O
u
t
T
r
a
d
e
N
o
(
t
r
a
d
e
N
o
)
;
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
B
e
a
n
.
s
e
t
S
u
b
j
e
c
t
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
S
u
b
j
e
c
t
(
)
)
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
t
o
t
a
l
A
m
o
u
n
t
 
=
 
n
u
l
l
;
/
/
支
付
宝
那
边
入
参
是
元
 
 
 
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
 
/
/
将
分
转
成
元
 
 
 
 
 
 
 
 
 
 
 
 
 
t
o
t
a
l
A
m
o
u
n
t
 
=
 
A
m
o
u
n
t
U
t
i
l
.
c
h
a
n
g
e
F
2
Y
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
T
o
t
a
l
A
m
o
u
n
t
(
)
.
t
o
S
t
r
i
n
g
(
)
)
;
 
 
 
 
 
 
 
 
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
e
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
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
6
)
;
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
B
e
a
n
.
s
e
t
T
o
t
a
l
A
m
o
u
n
t
(
t
o
t
a
l
A
m
o
u
n
t
)
;
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
B
e
a
n
.
s
e
t
B
o
d
y
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
B
o
d
y
(
)
)
;
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
B
e
a
n
.
s
e
t
S
t
o
r
e
I
d
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
S
t
o
r
e
I
d
(
)
)
;
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
B
e
a
n
.
s
e
t
E
x
p
i
r
e
T
i
m
e
(
"
3
0
m
"
)
;
 
 
 
 
 
 
 
 
 
 
/
/
根
据
应
用
、
服
务
类
型
、
支
付
渠
道
查
询
支
付
渠
道
参
数
 
 
 
 
 
 
 
 
 
P
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
 
p
a
y
C
h
a
n
n
e
l
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
r
a
m
B
y
A
p
p
P
l
a
t
f
o
r
m
A
n
d
P
a
y
C
h
a
n
n
e
l
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
A
p
p
I
d
(
)
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
C
h
a
n
n
e
l
(
)
,
 
"
A
L
I
P
A
Y
_
W
A
P
"
)
;
 
 
 
 
 
 
 
 
 
i
f
(
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
=
 
n
u
l
l
)
{
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
7
)
;
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
/
/
支
付
宝
渠
道
参
数
 
 
 
 
 
 
 
 
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
.
g
e
t
P
a
r
a
m
(
)
,
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
 
 
/
/
字
符
编
码
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
C
h
a
r
e
s
t
(
"
u
t
f
‐
8
"
)
;
 
 
 
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
p
a
y
O
r
d
e
r
R
e
s
p
o
n
s
e
 
=
 
p
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
A
l
i
W
A
P
(
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
a
l
i
p
a
y
B
e
a
n
)
;
 
 
 
 
 
 
 
 
 
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
支
付
宝
H
5
支
付
响
应
C
o
n
t
e
n
t
:
"
 
+
 
p
a
y
O
r
d
e
r
R
e
s
p
o
n
s
e
.
g
e
t
C
o
n
t
e
n
t
(
)
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 36 -->
r
e
t
u
r
n
 
p
a
y
O
r
d
e
r
R
e
s
p
o
n
s
e
;
 
 
 
 
 
}
 
定
义
根
据
订
单
号
查
询
订
单
信
息
。
/
*
*
 
 
*
 
根
据
订
单
号
查
询
订
单
信
息
 
 
*
 
@
p
a
r
a
m
 
t
r
a
d
e
N
o
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
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
 
P
a
y
O
r
d
e
r
D
T
O
 
q
u
e
r
y
P
a
y
O
r
d
e
r
(
S
t
r
i
n
g
 
t
r
a
d
e
N
o
)
 
{
 
 
 
 
 
P
a
y
O
r
d
e
r
 
p
a
y
O
r
d
e
r
 
=
 
p
a
y
O
r
d
e
r
M
a
p
p
e
r
 
 
 
 
 
 
 
 
 
 
 
 
 
.
s
e
l
e
c
t
O
n
e
(
n
e
w
 
Q
u
e
r
y
W
r
a
p
p
e
r
<
P
a
y
O
r
d
e
r
>
(
)
.
l
a
m
b
d
a
(
)
.
e
q
(
P
a
y
O
r
d
e
r
:
:
g
e
t
T
r
a
d
e
N
o
,
 
t
r
a
d
e
N
o
)
)
;
 
 
 
 
r
e
t
u
r
n
 
P
a
y
O
r
d
e
r
C
o
n
v
e
r
t
.
I
N
S
T
A
N
C
E
.
e
n
t
i
t
y
2
d
t
o
(
p
a
y
O
r
d
e
r
)
;
 
}
 
完
善
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
方
法
，
调
用
a
l
i
p
a
y
H
5
方
法
：
p
u
b
l
i
c
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
(
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
)
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
/
/
保
存
订
单
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
P
a
y
C
h
a
n
n
e
l
(
"
A
L
I
P
A
Y
_
W
A
P
"
)
;
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
s
a
v
e
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
/
/
调
用
支
付
代
理
服
务
请
求
第
三
方
支
付
系
统
 
 
 
 
 
r
e
t
u
r
n
 
a
l
i
p
a
y
H
5
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
T
r
a
d
e
N
o
(
)
)
;
 
}
 
5
.
4
.
2
.
3
 
完
善
交
易
服
务
下
单
接
口
 
完
善
c
r
e
a
t
e
A
l
i
P
a
y
O
r
d
e
r
接
口
，
调
用
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
提
交
支
付
宝
订
单
。
@
A
p
i
O
p
e
r
a
t
i
o
n
(
"
支
付
宝
门
店
下
单
付
款
"
)
 
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
"
/
c
r
e
a
t
e
A
l
i
P
a
y
O
r
d
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
 
v
o
i
d
 
c
r
e
a
t
e
A
l
i
p
a
y
O
r
d
e
r
F
o
r
S
t
o
r
e
(
O
r
d
e
r
C
o
n
f
i
r
m
V
O
 
o
r
d
e
r
C
o
n
f
i
r
m
V
O
,
 
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
,
 
H
t
t
p
S
e
r
v
l
e
t
R
e
s
p
o
n
s
e
 
r
e
s
p
o
n
s
e
)
 
 
 
 
 
 
 
 
 
t
h
r
o
w
s
 
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
i
f
 
(
S
t
r
i
n
g
U
t
i
l
s
.
i
s
B
l
a
n
k
(
o
r
d
e
r
C
o
n
f
i
r
m
V
O
.
g
e
t
A
p
p
I
d
(
)
)
)
 
{
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
3
)
;
 
 
 
 
 
}
 
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
P
a
y
O
r
d
e
r
C
o
n
v
e
r
t
.
I
N
S
T
A
N
C
E
.
v
o
2
d
t
o
(
o
r
d
e
r
C
o
n
f
i
r
m
V
O
)
;
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
T
o
t
a
l
A
m
o
u
n
t
(
I
n
t
e
g
e
r
.
v
a
l
u
e
O
f
(
A
m
o
u
n
t
U
t
i
l
.
c
h
a
n
g
e
Y
2
F
(
o
r
d
e
r
C
o
n
f
i
r
m
V
O
.
g
e
t
T
o
t
a
l
A
m
o
u
n
t
(
)
)
)
)
;
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
C
l
i
e
n
t
I
p
(
I
P
U
t
i
l
.
g
e
t
I
p
A
d
d
r
(
r
e
q
u
e
s
t
)
)
;
 
 
 
 
 
/
/
获
取
下
单
应
用
信
息
 
 
 
 
 
A
p
p
D
T
O
 
a
p
p
 
=
 
a
p
p
S
e
r
v
i
c
e
.
g
e
t
A
p
p
B
y
I
d
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
A
p
p
I
d
(
)
)
;
 
 
 
 
 
/
/
设
置
所
属
商
户
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
M
e
r
c
h
a
n
t
I
d
(
a
p
p
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
)
;
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
p
a
y
O
r
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
S
e
r
v
i
c
e
.
s
u
b
m
i
t
O
r
d
e
r
B
y
A
l
i
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
 
 
 
 
S
t
r
i
n
g
 
c
o
n
t
e
n
t
 
=
 
S
t
r
i
n
g
.
v
a
l
u
e
O
f
(
p
a
y
O
r
d
e
r
R
e
s
u
l
t
.
g
e
t
C
o
n
t
e
n
t
(
)
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 37 -->
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
支
付
宝
H
5
支
付
响
应
的
结
果
：
"
 
+
 
c
o
n
t
e
n
t
)
;
 
 
 
 
 
r
e
s
p
o
n
s
e
.
s
e
t
C
o
n
t
e
n
t
T
y
p
e
(
"
t
e
x
t
/
h
t
m
l
;
c
h
a
r
s
e
t
=
U
T
F
‐
8
"
)
;
 
 
 
 
 
r
e
s
p
o
n
s
e
.
g
e
t
W
r
i
t
e
r
(
)
.
w
r
i
t
e
(
c
o
n
t
e
n
t
)
;
/
/
直
接
将
完
整
的
表
单
h
t
m
l
输
出
到
页
面
 
 
 
 
 
r
e
s
p
o
n
s
e
.
g
e
t
W
r
i
t
e
r
(
)
.
f
l
u
s
h
(
)
;
 
 
 
 
 
r
e
s
p
o
n
s
e
.
g
e
t
W
r
i
t
e
r
(
)
.
c
l
o
s
e
(
)
;
 
}
 
5
.
4
.
3
 
测
试
 
1
、
生
成
二
维
码
注
意
：
二
维
码
的
U
R
L
可
以
被
模
拟
器
访
问
。
2
、
扫
码
进
入
支
付
入
口
，
进
入
支
付
确
认
页
面
3
、
输
入
金
额
，
点
击
确
认
支
付
。
订
单
写
入
闪
聚
平
台
数
据
库
。
调
用
支
付
宝
下
单
接
口
是
否
成
功
。
 
 
6
 
获
取
支
付
结
果
 
6
.
1
 
需
求
分
析
 
获
取
支
付
结
果
的
需
求
包
括
如
下
几
个
方
面
：
1
、
服
务
间
异
步
通
信
顾
客
支
付
完
成
后
，
平
台
需
要
及
时
得
到
支
付
结
果
并
更
新
数
据
库
中
的
订
单
状
态
。
根
据
微
服
务
职
责
划
分
，
支
付
渠
道
代
理
服
务
负
责
与
支
付
宝
、
微
信
接
口
对
接
，
交
易
服
务
负
责
维
护
订
单
的
数
据
，
支
付
渠
道
代
理
服
务
如
何
把
查
询
到
的
订
单
结
果
通
知
给
交
易
服
务
呢
？
项
目
中
会
采
用
消
息
队
列
来
完
成
。
2
、
实
现
第
三
方
支
付
系
统
支
付
结
果
查
询
接
口
完
成
支
付
后
第
三
方
支
付
系
统
提
供
两
种
方
式
获
取
支
付
结
果
，
如
下
图
：
1
）
第
三
方
支
付
系
统
主
动
通
知
闪
聚
支
付
平
台
支
付
结
果
。
2
）
闪
聚
支
付
平
台
主
动
从
第
三
方
支
付
系
统
查
询
支
付
结
果
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 38 -->
以
上
两
种
方
法
在
实
际
项
目
中
可
以
都
用
，
其
中
第
二
种
是
必
须
用
的
，
因
为
第
一
种
是
由
第
三
方
支
付
系
统
主
动
通
知
闪
聚
支
付
平
台
，
当
调
用
闪
聚
平
台
接
口
无
法
通
信
达
到
一
定
的
次
数
后
第
三
方
支
付
系
统
将
不
再
通
知
。
本
项
目
支
付
渠
道
代
理
服
务
集
成
第
二
种
方
法
完
成
支
付
结
果
的
查
询
。
3
、
下
单
成
功
延
迟
向
第
三
方
支
付
系
统
查
询
支
付
结
果
在
调
用
第
三
方
支
付
下
单
接
口
之
后
此
时
用
户
正
在
支
付
中
，
所
以
需
要
延
迟
一
定
的
时
间
再
去
查
询
支
付
结
果
。
如
果
查
询
支
付
结
果
还
没
有
支
付
再
继
续
等
待
一
定
的
时
间
再
去
查
询
，
当
达
到
订
单
的
有
效
期
还
没
有
支
付
则
不
再
查
询
。
 
6
.
2
 
R
o
c
k
e
t
M
Q
技
术
预
研
 
参
考
：
R
o
c
k
e
t
M
Q
研
究
v
1
.
0
.
p
d
f
。
6
.
3
 
技
术
方
案
 
项
目
使
用
消
息
队
列
R
o
c
k
e
t
M
Q
完
成
支
付
渠
道
代
理
服
务
与
交
易
服
务
之
间
的
通
信
，
如
下
图
：
1
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 39 -->
0
、
支
付
渠
道
代
理
服
务
调
用
第
三
方
支
付
下
单
接
口
。
（
此
时
顾
客
开
始
输
入
密
码
进
行
支
付
）
1
、
支
付
渠
道
代
理
向
消
息
队
列
发
送
一
条
延
迟
消
息
（
查
询
支
付
结
果
）
，
消
费
方
仍
是
支
付
渠
道
代
理
服
务
。
2
、
支
付
渠
道
代
理
接
收
消
息
，
调
用
支
付
宝
接
口
查
询
支
付
结
果
3
、
支
付
渠
道
代
理
查
询
到
支
付
结
果
，
将
支
付
结
果
发
送
至
M
Q
，
消
费
方
是
交
易
服
务
。
4
、
交
易
服
务
接
收
到
支
付
结
果
消
息
，
更
新
订
单
状
态
。
 
6
.
4
 
支
付
渠
道
代
理
查
询
支
付
宝
交
易
状
态
 
6
.
4
.
1
 
支
付
宝
交
易
状
态
查
询
接
口
 
参
考
手
机
网
支
付
产
品
介
绍
文
档
（
h
t
t
p
s
:
/
/
d
o
c
s
.
o
p
e
n
.
a
l
i
p
a
y
.
c
o
m
/
2
0
3
）
，
查
看
a
l
i
p
a
y
.
t
r
a
d
e
.
q
u
e
r
y
交
易
状
态
查
询
接
口
文
档
。
6
.
4
.
1
.
1
 
请
求
参
数
 
公
共
请
求
参
数
基
本
都
是
支
付
渠
道
设
置
的
参
数
，
实
现
方
法
参
考
支
付
宝
下
单
接
口
即
可
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 40 -->
业
务
请
求
参
数
中
o
u
t
_
t
r
a
d
e
_
n
o
即
闪
聚
支
付
平
台
订
单
号
，
根
据
此
订
单
号
查
询
支
付
状
态
。
6
.
4
.
1
.
2
 
响
应
参
数
 
支
付
宝
交
易
状
态
查
询
接
口
的
响
应
参
数
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 41 -->
以
上
参
数
主
要
解
析
c
o
d
e
和
t
r
a
d
e
_
s
t
a
t
u
s
：
1
、
根
据
c
o
d
e
判
断
接
口
请
求
是
否
成
功
参
考
：
h
t
t
p
s
:
/
/
d
o
c
s
.
o
p
e
n
.
a
l
i
p
a
y
.
c
o
m
/
c
o
m
m
o
n
/
1
0
5
8
0
6
2
、
根
据
t
r
a
d
e
_
s
t
a
t
u
s
判
断
具
体
的
支
付
状
态
交
易
状
态
如
下
：
W
A
I
T
_
B
U
Y
E
R
_
P
A
Y
（
交
易
创
建
，
等
待
买
家
付
款
）
T
R
A
D
E
_
C
L
O
S
E
D
（
未
付
款
交
易
超
时
关
闭
，
或
支
付
完
成
后
全
额
退
款
）
T
R
A
D
E
_
S
U
C
C
E
S
S
（
交
易
支
付
成
功
）
T
R
A
D
E
_
F
I
N
I
S
H
E
D
（
交
易
结
束
，
不
可
退
款
）
 
6
.
4
.
2
 
支
付
渠
道
代
理
接
口
定
义
 
6
.
4
.
2
.
1
 
接
口
定
义
 
接
口
描
述
：
1
）
使
用
支
付
宝
S
D
K
发
起
支
付
结
果
查
询
请
求
 
2
）
返
回
查
询
结
果
在
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
定
义
如
下
接
口
：
/
*
*
 
 
*
 
支
付
宝
交
易
状
态
查
询
 
 
*
 
@
p
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
 
支
付
渠
道
参
数
 
 
*
 
@
p
a
r
a
m
 
o
u
t
T
r
a
d
e
N
o
 
闪
聚
平
台
订
单
号
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
(
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
S
t
r
i
n
g
 
o
u
t
T
r
a
d
e
N
o
)
;
 
6
.
4
.
2
.
2
 
接
口
实
现
 
参
考
支
付
宝
官
方
提
供
的
样
例
代
码
与
支
付
宝
通
信
。
h
t
t
p
s
:
/
/
d
o
c
s
.
o
p
e
n
.
a
l
i
p
a
y
.
c
o
m
/
a
p
i
_
1
/
a
l
i
p
a
y
.
t
r
a
d
e
.
q
u
e
r
y
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 42 -->
1
）
定
义
支
付
宝
查
询
返
回
状
态
码
常
量
类
：
A
l
i
C
o
d
e
C
o
n
s
t
a
n
t
s
 
2
）
s
d
k
示
例
如
下
参
考
s
d
k
示
例
：
h
t
t
p
s
:
/
/
d
o
c
s
.
o
p
e
n
.
a
l
i
p
a
y
.
c
o
m
/
a
p
i
_
1
/
a
l
i
p
a
y
.
t
r
a
d
e
.
q
u
e
r
y
/
A
l
i
p
a
y
C
l
i
e
n
t
 
a
l
i
p
a
y
C
l
i
e
n
t
 
=
 
n
e
w
 
D
e
f
a
u
l
t
A
l
i
p
a
y
C
l
i
e
n
t
(
"
h
t
t
p
s
:
/
/
o
p
e
n
a
p
i
.
a
l
i
p
a
y
.
c
o
m
/
g
a
t
e
w
a
y
.
d
o
"
,
"
a
p
p
_
i
d
"
,
"
y
o
u
r
 
p
r
i
v
a
t
e
_
k
e
y
"
,
"
j
s
o
n
"
,
"
G
B
K
"
,
"
a
l
i
p
a
y
_
p
u
b
l
i
c
_
k
e
y
"
,
"
R
S
A
2
"
)
;
 
A
l
i
p
a
y
T
r
a
d
e
Q
u
e
r
y
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
 
=
 
n
e
w
 
A
l
i
p
a
y
T
r
a
d
e
Q
u
e
r
y
R
e
q
u
e
s
t
(
)
;
 
r
e
q
u
e
s
t
.
s
e
t
B
i
z
C
o
n
t
e
n
t
(
"
{
"
 
+
 
"
\
"
o
u
t
_
t
r
a
d
e
_
n
o
\
"
:
\
"
2
0
1
5
0
3
2
0
0
1
0
1
0
1
0
0
1
\
"
,
"
 
+
 
"
\
"
t
r
a
d
e
_
n
o
\
"
:
\
"
2
0
1
4
1
1
2
6
1
1
0
0
1
0
0
4
6
8
0
 
0
7
3
9
5
6
7
0
7
\
"
,
"
 
+
 
"
\
"
o
r
g
_
p
i
d
\
"
:
\
"
2
0
8
8
1
0
1
1
1
7
9
5
2
2
2
2
\
"
,
"
 
+
 
"
 
 
 
 
 
 
\
"
q
u
e
r
y
_
o
p
t
i
o
n
s
\
"
:
[
"
 
+
 
"
 
 
 
 
 
 
 
 
\
"
T
R
A
D
E
_
S
E
T
T
L
E
_
I
N
F
O
\
"
"
 
+
 
"
 
 
 
 
 
 
]
"
 
+
 
"
 
 
}
"
)
;
 
A
l
i
p
a
y
T
r
a
d
e
Q
u
e
r
y
R
e
s
p
o
n
s
e
 
r
e
s
p
o
n
s
e
 
=
 
a
l
i
p
a
y
C
l
i
e
n
t
.
e
x
e
c
u
t
e
(
r
e
q
u
e
s
t
)
;
 
i
f
(
r
e
s
p
o
n
s
e
.
i
s
S
u
c
c
e
s
s
(
)
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
调
用
成
功
"
)
;
 
}
 
e
l
s
e
 
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
调
用
失
败
"
)
;
 
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
s
h
a
n
j
u
p
a
y
.
p
a
y
m
e
n
t
a
g
e
n
t
.
c
o
m
m
o
n
.
c
o
n
s
t
a
n
t
;
 
/
*
*
 
*
 
支
付
宝
查
询
返
回
状
态
码
常
量
类
 
*
/
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
 
A
l
i
C
o
d
e
C
o
n
s
t
a
n
t
s
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
S
U
C
C
E
S
S
C
O
D
E
 
=
 
"
1
0
0
0
0
"
;
 
/
/
 
支
付
成
功
或
接
口
调
用
成
功
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
P
A
Y
I
N
G
C
O
D
E
 
 
=
 
"
1
0
0
0
3
"
;
 
/
/
 
用
户
支
付
中
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
F
A
I
L
E
D
C
O
D
E
 
 
=
 
"
4
0
0
0
4
"
;
 
/
/
 
失
败
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
E
R
R
O
R
C
O
D
E
 
 
 
=
 
"
2
0
0
0
0
"
;
 
/
/
 
系
统
异
常
 
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
支
付
宝
交
易
状
态
 
 
 
 
 
*
 
 
 
 
 
 
W
A
I
T
_
B
U
Y
E
R
_
P
A
Y
（
交
易
创
建
，
等
待
买
家
付
款
）
 
 
 
 
 
*
 
 
 
 
 
T
R
A
D
E
_
C
L
O
S
E
D
（
未
付
款
交
易
超
时
关
闭
，
或
支
付
完
成
后
全
额
退
款
）
 
 
 
 
 
*
 
 
 
 
 
T
R
A
D
E
_
S
U
C
C
E
S
S
（
交
易
支
付
成
功
）
 
 
 
 
 
*
 
 
 
 
 
T
R
A
D
E
_
F
I
N
I
S
H
E
D
（
交
易
结
束
，
不
可
退
款
）
 
 
 
 
 
*
/
 
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
W
A
I
T
_
B
U
Y
E
R
_
P
A
Y
 
=
 
"
W
A
I
T
_
B
U
Y
E
R
_
P
A
Y
"
;
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
T
R
A
D
E
_
C
L
O
S
E
D
 
=
 
"
T
R
A
D
E
_
C
L
O
S
E
D
"
;
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
T
R
A
D
E
_
S
U
C
C
E
S
S
 
=
 
"
T
R
A
D
E
_
S
U
C
C
E
S
S
"
;
 
 
 
 
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
 
f
i
n
a
l
 
S
t
r
i
n
g
 
T
R
A
D
E
_
F
I
N
I
S
H
E
D
 
=
 
"
T
R
A
D
E
_
F
I
N
I
S
H
E
D
"
;
 
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 43 -->
3
）
接
口
实
现
如
下
支
付
宝
交
易
状
态
查
询
实
现
方
法
如
下
：
/
*
*
 
 
*
 
支
付
宝
交
易
状
态
查
询
 
 
*
 
 
*
 
@
p
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
 
*
 
@
p
a
r
a
m
 
o
u
t
T
r
a
d
e
N
o
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
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
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
(
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
S
t
r
i
n
g
 
o
u
t
T
r
a
d
e
N
o
)
 
{
 
 
 
 
S
t
r
i
n
g
 
g
a
t
e
w
a
y
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
U
r
l
(
)
;
/
/
支
付
接
口
网
关
地
址
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
I
d
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
p
p
I
d
(
)
;
/
/
a
p
p
i
d
 
 
 
 
 
S
t
r
i
n
g
 
r
s
a
P
r
i
v
a
t
e
K
e
y
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
R
s
a
P
r
i
v
a
t
e
K
e
y
(
)
;
 
/
/
私
钥
 
 
 
 
 
S
t
r
i
n
g
 
f
o
r
m
a
t
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
F
o
r
m
a
t
(
)
;
/
/
j
s
o
n
格
式
 
 
 
 
 
S
t
r
i
n
g
 
c
h
a
r
e
s
t
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
C
h
a
r
e
s
t
(
)
;
/
/
编
码
 
u
t
f
‐
8
 
 
 
 
 
S
t
r
i
n
g
 
a
l
i
p
a
y
P
u
b
l
i
c
K
e
y
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
l
i
p
a
y
P
u
b
l
i
c
K
e
y
(
)
;
 
/
/
公
钥
 
 
 
 
 
S
t
r
i
n
g
 
s
i
g
n
t
y
p
e
 
=
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
S
i
g
n
t
y
p
e
(
)
;
/
/
签
名
算
法
类
型
 
 
 
 
 
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
C
扫
B
请
求
支
付
宝
查
询
订
单
，
参
数
：
{
}
"
,
 
J
S
O
N
.
t
o
J
S
O
N
S
t
r
i
n
g
(
a
l
i
C
o
n
f
i
g
P
a
r
a
m
)
)
;
 
 
 
 
 
 
/
/
构
建
s
d
k
客
户
端
 
 
 
 
 
A
l
i
p
a
y
C
l
i
e
n
t
 
c
l
i
e
n
t
 
=
 
n
e
w
 
D
e
f
a
u
l
t
A
l
i
p
a
y
C
l
i
e
n
t
(
g
a
t
e
w
a
y
,
 
a
p
p
I
d
,
 
r
s
a
P
r
i
v
a
t
e
K
e
y
,
 
f
o
r
m
a
t
,
 
c
h
a
r
e
s
t
,
 
 
 
 
 
 
 
 
 
 
 
 
 
a
l
i
p
a
y
P
u
b
l
i
c
K
e
y
,
 
s
i
g
n
t
y
p
e
)
;
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
Q
u
e
r
y
R
e
q
u
e
s
t
 
q
u
e
r
y
R
e
q
u
e
s
t
 
=
 
n
e
w
 
A
l
i
p
a
y
T
r
a
d
e
Q
u
e
r
y
R
e
q
u
e
s
t
(
)
;
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
P
a
y
M
o
d
e
l
 
m
o
d
e
l
 
=
 
n
e
w
 
A
l
i
p
a
y
T
r
a
d
e
P
a
y
M
o
d
e
l
(
)
;
 
 
 
 
 
/
/
闪
聚
平
台
订
单
号
 
 
 
 
 
m
o
d
e
l
.
s
e
t
O
u
t
T
r
a
d
e
N
o
(
o
u
t
T
r
a
d
e
N
o
)
;
 
 
 
 
 
/
/
封
装
请
求
参
数
 
 
 
 
 
q
u
e
r
y
R
e
q
u
e
s
t
.
s
e
t
B
i
z
M
o
d
e
l
(
m
o
d
e
l
)
;
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
d
t
o
;
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
/
/
请
求
支
付
宝
接
口
 
 
 
 
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
Q
u
e
r
y
R
e
s
p
o
n
s
e
 
q
r
 
=
 
c
l
i
e
n
t
.
e
x
e
c
u
t
e
(
q
u
e
r
y
R
e
q
u
e
s
t
)
;
 
 
 
 
 
 
 
 
 
/
/
接
口
调
用
成
功
 
 
 
 
 
 
 
 
 
i
f
 
(
A
l
i
C
o
d
e
C
o
n
s
t
a
n
t
s
.
S
U
C
C
E
S
S
C
O
D
E
.
e
q
u
a
l
s
(
q
r
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
)
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
/
/
将
支
付
宝
响
应
的
状
态
转
换
为
闪
聚
平
台
的
状
态
 
 
 
 
 
 
 
 
 
 
 
 
 
T
r
a
d
e
S
t
a
t
u
s
 
t
r
a
d
e
S
t
a
t
u
s
 
=
 
c
o
v
e
r
t
A
l
i
T
r
a
d
e
S
t
a
t
u
s
T
o
S
h
a
n
j
u
C
o
d
e
(
q
r
.
g
e
t
T
r
a
d
e
S
t
a
t
u
s
(
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
d
t
o
 
=
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
s
u
c
c
e
s
s
(
q
r
.
g
e
t
T
r
a
d
e
N
o
(
)
,
 
q
r
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
,
 
t
r
a
d
e
S
t
a
t
u
s
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
q
r
.
g
e
t
M
s
g
(
)
 
+
 
"
 
"
 
+
 
q
r
.
g
e
t
S
u
b
M
s
g
(
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
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
‐
‐
‐
‐
查
询
支
付
宝
H
5
支
付
结
果
"
 
+
 
J
S
O
N
.
t
o
J
S
O
N
S
t
r
i
n
g
(
d
t
o
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
d
t
o
;
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
}
 
c
a
t
c
h
 
(
A
l
i
p
a
y
A
p
i
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
)
 
{
 
 
 
 
 
 
 
 
 
l
o
g
.
w
a
r
n
(
e
.
g
e
t
M
e
s
s
a
g
e
(
)
,
 
e
)
;
 
 
 
 
 
}
 
 
 
 
 
d
t
o
 
=
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
f
a
i
l
(
"
查
询
支
付
宝
支
付
结
果
异
常
"
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
U
N
K
N
O
W
N
)
;
 
 
 
 
 
r
e
t
u
r
n
 
d
t
o
;
 
}
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 44 -->
定
义
支
付
宝
响
应
状
态
与
闪
聚
平
台
的
转
换
方
法
：
/
*
*
 
 
*
 
将
支
付
宝
查
询
时
订
单
状
态
t
r
a
d
e
_
s
t
a
t
u
s
 
转
换
为
 
 
闪
聚
订
单
状
态
 
 
*
 
@
p
a
r
a
m
 
a
l
i
T
r
a
d
e
S
t
a
t
u
s
 
支
付
宝
交
易
状
态
 
 
*
 
 
 
 
 
 
W
A
I
T
_
B
U
Y
E
R
_
P
A
Y
（
交
易
创
建
，
等
待
买
家
付
款
）
 
 
*
 
 
 
 
 
 
T
R
A
D
E
_
C
L
O
S
E
D
（
未
付
款
交
易
超
时
关
闭
，
或
支
付
完
成
后
全
额
退
款
）
 
 
*
 
 
 
 
 
 
T
R
A
D
E
_
S
U
C
C
E
S
S
（
交
易
支
付
成
功
）
 
 
*
 
 
 
 
 
 
T
R
A
D
E
_
F
I
N
I
S
H
E
D
（
交
易
结
束
，
不
可
退
款
）
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
p
r
i
v
a
t
e
 
T
r
a
d
e
S
t
a
t
u
s
 
c
o
v
e
r
t
A
l
i
T
r
a
d
e
S
t
a
t
u
s
T
o
S
h
a
n
j
u
C
o
d
e
(
S
t
r
i
n
g
 
a
l
i
T
r
a
d
e
S
t
a
t
u
s
)
 
{
 
 
 
 
s
w
i
t
c
h
 
(
a
l
i
T
r
a
d
e
S
t
a
t
u
s
)
 
{
 
 
 
 
 
 
 
c
a
s
e
 
A
l
i
C
o
d
e
C
o
n
s
t
a
n
t
s
.
W
A
I
T
_
B
U
Y
E
R
_
P
A
Y
:
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
a
d
e
S
t
a
t
u
s
.
U
S
E
R
P
A
Y
I
N
G
;
 
 
 
 
 
 
 
c
a
s
e
 
A
l
i
C
o
d
e
C
o
n
s
t
a
n
t
s
.
T
R
A
D
E
_
S
U
C
C
E
S
S
:
 
 
 
 
 
 
 
c
a
s
e
 
A
l
i
C
o
d
e
C
o
n
s
t
a
n
t
s
.
T
R
A
D
E
_
F
I
N
I
S
H
E
D
:
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
a
d
e
S
t
a
t
u
s
.
S
U
C
C
E
S
S
;
 
 
 
 
 
 
 
d
e
f
a
u
l
t
:
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
T
r
a
d
e
S
t
a
t
u
s
.
F
A
I
L
E
D
;
 
 
 
 
}
 
}
 
6
.
4
.
2
.
3
 
接
口
测
试
 
对
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
方
法
进
行
单
元
测
试
：
1
、
通
过
C
扫
B
进
行
支
付
定
下
单
，
从
数
据
库
找
到
订
单
号
2
、
编
写
测
试
类
A
P
P
_
I
D
、
A
P
P
_
P
R
I
V
A
T
E
_
K
E
Y
、
A
L
I
P
A
Y
_
P
U
B
L
I
C
_
K
E
Y
使
用
自
己
申
请
的
支
付
宝
沙
箱
参
数
。
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
T
e
s
t
 
@
R
u
n
W
i
t
h
(
S
p
r
i
n
g
R
u
n
n
e
r
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
 
c
l
a
s
s
 
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
T
e
s
t
 
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
 
 
 
 
 
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
 
p
a
y
C
h
a
n
n
e
l
A
g
e
n
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
T
e
s
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
 
t
e
s
t
Q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
(
)
{
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
A
P
P
_
I
D
 
=
 
"
"
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
A
P
P
_
P
R
I
V
A
T
E
_
K
E
Y
 
=
 
"
"
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
A
L
I
P
A
Y
_
P
U
B
L
I
C
_
K
E
Y
 
=
 
"
"
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
C
H
A
R
S
E
T
 
=
 
"
U
T
F
‐
8
"
;
 
 
 
 
 
 
 
 
 
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
e
r
U
r
l
 
=
 
"
h
t
t
p
s
:
/
/
o
p
e
n
a
p
i
.
a
l
i
p
a
y
d
e
v
.
c
o
m
/
g
a
t
e
w
a
y
.
d
o
"
;
/
/
正
式
"
h
t
t
p
s
:
/
/
o
p
e
n
a
p
i
.
a
l
i
p
a
y
.
c
o
m
/
g
a
t
e
w
a
y
.
d
o
"
 
 
 
 
 
 
 
 
 
 
/
/
支
付
渠
道
参
数
 
 
 
 
 
 
 
 
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
=
 
n
e
w
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
(
)
;
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
U
r
l
(
s
e
r
v
e
r
U
r
l
)
;
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
C
h
a
r
e
s
t
(
C
H
A
R
S
E
T
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 45 -->
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
A
l
i
p
a
y
P
u
b
l
i
c
K
e
y
(
A
L
I
P
A
Y
_
P
U
B
L
I
C
_
K
E
Y
)
;
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
R
s
a
P
r
i
v
a
t
e
K
e
y
(
A
P
P
_
P
R
I
V
A
T
E
_
K
E
Y
)
;
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
A
p
p
I
d
(
A
P
P
_
I
D
)
;
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
F
o
r
m
a
t
(
"
j
s
o
n
"
)
;
 
 
 
 
 
 
 
 
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
S
i
g
n
t
y
p
e
(
"
R
S
A
2
"
)
;
 
 
 
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
p
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
=
 
p
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
(
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
"
S
J
1
2
1
6
3
2
5
1
6
2
3
7
0
3
8
3
8
7
3
"
)
;
 
 
 
 
 
 
 
 
 
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
p
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
)
;
 
 
 
 
 
 
}
 
}
 
6
.
5
 
支
付
结
果
查
询
 
6
.
5
.
1
 
交
互
流
程
 
根
据
技
术
方
案
的
分
析
，
交
互
流
程
如
下
：
1
、
支
付
渠
道
代
理
服
务
调
用
支
付
宝
下
单
接
口
完
成
后
向
M
Q
发
送
“
支
付
结
果
查
询
”
消
息
（
延
迟
消
息
）
，
消
费
方
为
支
付
渠
道
代
理
服
务
。
2
、
支
付
渠
道
代
理
服
务
监
听
消
息
队
列
，
接
收
“
支
付
结
果
查
询
”
消
息
。
3
、
支
付
渠
道
代
理
服
务
调
用
第
三
方
支
付
系
统
的
支
付
结
果
查
询
接
口
。
 
6
.
5
.
2
 
发
送
消
息
 
6
.
5
.
2
.
1
 
配
置
R
o
c
k
e
t
M
Q
 
1
）
在
支
付
渠
道
代
理
工
程
中
添
加
R
o
c
k
e
t
M
Q
依
赖
：
 
2
）
在
N
a
c
o
s
中
添
加
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
r
o
c
k
e
t
m
q
.
y
a
m
l
配
置
，
D
a
t
a
 
I
D
:
 
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
r
o
c
k
e
t
m
q
.
y
a
m
l
,
G
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
a
p
a
c
h
e
.
r
o
c
k
e
t
m
q
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
r
o
c
k
e
t
m
q
‐
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
0
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

<!-- page 46 -->
3
）
在
s
h
a
n
j
u
p
a
y
-
p
a
y
m
e
n
t
-
a
g
e
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
工
程
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
引
入
此
配
置
：
 
6
.
5
.
2
.
2
 
生
产
消
息
类
 
1
、
修
改
支
付
宝
下
单
调
用
方
法
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
A
l
i
W
A
P
，
调
用
P
a
y
P
r
o
d
u
c
e
r
发
送
消
息
。
发
送
支
付
结
果
查
询
延
迟
消
息
代
码
如
下
：
t
r
y
 
{
 
 
 
 
 
/
/
发
送
支
付
结
果
查
询
延
迟
消
息
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
<
A
l
i
C
o
n
f
i
g
P
a
r
a
m
>
 
n
o
t
i
c
e
 
=
 
n
e
w
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
<
A
l
i
C
o
n
f
i
g
P
a
r
a
m
>
(
)
;
 
 
 
 
 
n
o
t
i
c
e
.
s
e
t
O
u
t
T
r
a
d
e
N
o
(
a
l
i
p
a
y
B
e
a
n
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
)
;
 
 
 
 
 
n
o
t
i
c
e
.
s
e
t
C
o
n
t
e
n
t
(
a
l
i
C
o
n
f
i
g
P
a
r
a
m
)
;
 
 
 
 
 
n
o
t
i
c
e
.
s
e
t
M
s
g
(
"
A
L
I
P
A
Y
_
W
A
P
"
)
;
 
 
 
 
 
p
a
y
P
r
o
d
u
c
e
r
.
p
a
y
O
r
d
e
r
N
o
t
i
c
e
(
n
o
t
i
c
e
)
;
 
 
 
 
 
 
 
 
 
/
/
 
调
用
S
D
K
提
交
表
单
 
 
 
 
 
A
l
i
p
a
y
T
r
a
d
e
W
a
p
P
a
y
R
e
s
p
o
n
s
e
 
r
e
s
p
o
n
s
e
 
=
 
c
l
i
e
n
t
.
p
a
g
e
E
x
e
c
u
t
e
(
a
l
i
p
a
y
R
e
q
u
e
s
t
)
;
 
 
 
 
 
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
支
付
宝
手
机
网
站
支
付
预
支
付
订
单
信
息
"
 
+
 
r
e
s
p
o
n
s
e
)
;
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
 
=
 
n
e
w
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
(
)
;
 
 
 
 
 
r
e
s
.
s
e
t
C
o
n
t
e
n
t
(
r
e
s
p
o
n
s
e
.
g
e
t
B
o
d
y
(
)
)
;
 
 
 
 
 
 
r
e
t
u
r
n
 
r
e
s
;
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
e
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
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
4
0
0
0
0
2
)
;
/
/
支
付
宝
确
认
支
付
失
败
 
}
 
 
2
、
在
支
付
渠
道
代
理
服
务
中
编
写
生
产
消
息
类
P
a
y
P
r
o
d
u
c
e
r
 
r
o
c
k
e
t
m
q
:
 
 
n
a
m
e
S
e
r
v
e
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
9
8
7
6
 
 
p
r
o
d
u
c
e
r
:
 
 
 
 
g
r
o
u
p
:
 
P
I
D
_
P
A
Y
_
P
R
O
D
U
C
E
R
 
 
 
 
 
 
 
 
 
 
‐
 
 
 
 
 
 
 
 
 
 
 
 
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
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
‐
i
d
:
 
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
r
o
c
k
e
t
m
q
.
y
a
m
l
 
#
 
r
o
c
k
e
t
m
q
配
置
 
 
 
 
 
 
 
 
 
 
 
 
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
 
#
 
通
用
配
置
组
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
s
h
a
n
j
u
p
a
y
.
p
a
y
m
e
n
t
a
g
e
n
t
.
m
e
s
s
a
g
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
s
h
a
n
j
u
p
a
y
.
c
o
m
m
o
n
.
a
p
i
.
d
t
o
.
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
;
i
m
p
o
r
t
 
l
o
m
b
o
k
.
e
x
t
e
r
n
.
s
l
f
4
j
.
S
l
f
4
j
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
r
o
c
k
e
t
m
q
.
s
p
r
i
n
g
.
c
o
r
e
.
R
o
c
k
e
t
M
Q
T
e
m
p
l
a
t
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
s
t
e
r
e
o
t
y
p
e
.
C
o
m
p
o
n
e
n
t
;
 
i
m
p
o
r
t
 
j
a
v
a
x
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
o
u
r
c
e
;
 
@
S
l
f
4
j
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 47 -->
6
.
5
.
3
 
接
收
消
息
 
定
义
P
a
y
C
o
n
s
u
m
e
r
类
，
监
听
“
支
付
结
果
查
询
”
消
息
队
列
。
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
s
h
a
n
j
u
p
a
y
.
p
a
y
m
e
n
t
a
g
e
n
t
.
m
e
s
s
a
g
e
;
 
 
@
S
l
f
4
j
 
@
S
e
r
v
i
c
e
 
@
R
o
c
k
e
t
M
Q
M
e
s
s
a
g
e
L
i
s
t
e
n
e
r
(
t
o
p
i
c
 
=
 
"
T
P
_
P
A
Y
M
E
N
T
_
O
R
D
E
R
"
,
 
c
o
n
s
u
m
e
r
G
r
o
u
p
 
=
 
"
C
I
D
_
P
A
Y
M
E
N
T
_
C
O
N
S
U
M
E
R
"
)
 
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
 
P
a
y
C
o
n
s
u
m
e
r
 
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
 
R
o
c
k
e
t
M
Q
L
i
s
t
e
n
e
r
<
M
e
s
s
a
g
e
E
x
t
>
 
{
 
 
 
 
 
@
R
e
s
o
u
r
c
e
 
 
 
 
p
r
i
v
a
t
e
 
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
 
p
a
y
A
g
e
n
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
 
v
o
i
d
 
o
n
M
e
s
s
a
g
e
(
M
e
s
s
a
g
e
E
x
t
 
m
e
s
s
a
g
e
E
x
t
)
 
{
 
 
 
 
 
 
 
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
开
始
消
费
支
付
结
果
查
询
消
息
:
{
}
"
,
 
m
e
s
s
a
g
e
E
x
t
)
;
 
 
 
 
 
 
 
/
/
取
出
消
息
内
容
 
 
 
 
 
 
 
S
t
r
i
n
g
 
b
o
d
y
 
=
 
n
e
w
 
S
t
r
i
n
g
(
m
e
s
s
a
g
e
E
x
t
.
g
e
t
B
o
d
y
(
)
,
 
S
t
a
n
d
a
r
d
C
h
a
r
s
e
t
s
.
U
T
F
_
8
)
;
 
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
p
o
n
s
e
 
=
 
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
b
o
d
y
,
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
S
t
r
i
n
g
 
o
u
t
T
r
a
d
e
N
o
 
=
 
r
e
s
p
o
n
s
e
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
;
 
 
 
 
 
 
 
S
t
r
i
n
g
 
m
s
g
 
=
 
r
e
s
p
o
n
s
e
.
g
e
t
M
s
g
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
a
r
a
m
 
=
 
S
t
r
i
n
g
.
v
a
l
u
e
O
f
(
r
e
s
p
o
n
s
e
.
g
e
t
C
o
n
t
e
n
t
(
)
)
;
 
 
 
 
 
 
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
r
a
m
,
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
/
/
判
断
是
支
付
宝
还
是
微
信
 
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
u
l
t
 
=
 
n
e
w
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
(
)
;
 
 
 
 
 
 
 
i
f
 
(
"
A
L
I
P
A
Y
_
W
A
P
"
.
e
q
u
a
l
s
(
m
s
g
)
)
 
{
 
 
 
 
 
 
 
 
 
 
/
/
查
询
支
付
宝
支
付
结
果
 
 
 
 
 
 
 
 
 
 
r
e
s
u
l
t
 
=
 
p
a
y
A
g
e
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
(
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
o
u
t
T
r
a
d
e
N
o
)
;
 
 
 
 
 
 
 
}
 
e
l
s
e
 
i
f
 
(
"
W
X
_
J
S
A
P
I
"
.
e
q
u
a
l
s
(
m
s
g
)
)
 
{
 
 
 
 
 
 
 
 
 
 
/
/
查
询
微
信
支
付
结
果
 
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
 
P
a
y
P
r
o
d
u
c
e
r
 
{
 
 
 
 
/
/
消
息
T
o
p
i
c
 
 
 
 
p
r
i
v
a
t
e
 
s
t
a
t
i
c
 
f
i
n
a
l
 
S
t
r
i
n
g
 
T
O
P
I
C
_
O
R
D
E
R
 
=
 
"
T
P
_
P
A
Y
M
E
N
T
_
O
R
D
E
R
"
;
 
 
 
 
 
@
R
e
s
o
u
r
c
e
 
 
 
 
p
r
i
v
a
t
e
 
R
o
c
k
e
t
M
Q
T
e
m
p
l
a
t
e
 
r
o
c
k
e
t
M
Q
T
e
m
p
l
a
t
e
;
 
 
 
 
 
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
 
p
a
y
O
r
d
e
r
N
o
t
i
c
e
(
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
u
l
t
)
 
{
 
 
 
 
 
 
 
 
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
支
付
通
知
发
送
延
迟
消
息
:
{
}
"
,
 
r
e
s
u
l
t
)
;
 
 
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
处
理
消
息
存
储
格
式
 
 
 
 
 
 
 
 
 
 
 
 
M
e
s
s
a
g
e
<
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
>
 
m
e
s
s
a
g
e
 
=
 
M
e
s
s
a
g
e
B
u
i
l
d
e
r
.
w
i
t
h
P
a
y
l
o
a
d
(
r
e
s
u
l
t
)
.
b
u
i
l
d
(
)
;
 
 
 
 
 
 
 
 
 
 
 
 
S
e
n
d
R
e
s
u
l
t
 
s
e
n
d
R
e
s
u
l
t
 
=
 
r
o
c
k
e
t
M
Q
T
e
m
p
l
a
t
e
.
s
y
n
c
S
e
n
d
(
T
O
P
I
C
_
O
R
D
E
R
,
 
m
e
s
s
a
g
e
,
 
1
0
0
0
,
 
3
)
;
 
 
 
 
 
 
 
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
l
o
g
.
w
a
r
n
(
e
.
g
e
t
M
e
s
s
a
g
e
(
)
,
 
e
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 48 -->
}
 
 
 
 
 
 
 
 
/
/
返
回
查
询
获
得
的
支
付
状
态
 
 
 
 
 
 
 
i
f
 
(
T
r
a
d
e
S
t
a
t
u
s
.
U
N
K
N
O
W
N
.
e
q
u
a
l
s
(
r
e
s
u
l
t
.
g
e
t
T
r
a
d
e
S
t
a
t
e
(
)
)
 
|
|
 
T
r
a
d
e
S
t
a
t
u
s
.
U
S
E
R
P
A
Y
I
N
G
 
 
 
 
 
 
 
 
 
 
 
 
 
.
e
q
u
a
l
s
(
r
e
s
u
l
t
.
g
e
t
T
r
a
d
e
S
t
a
t
e
(
)
)
)
 
{
 
 
 
 
 
 
 
 
 
 
/
/
在
支
付
状
态
未
知
或
支
付
中
，
抛
出
异
常
会
重
新
消
息
此
消
息
 
 
 
 
 
 
 
 
 
 
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
支
付
代
理
‐
‐
‐
支
付
状
态
未
知
，
等
待
重
试
"
)
;
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
R
u
n
t
i
m
e
E
x
c
e
p
t
i
o
n
(
"
支
付
状
态
未
知
，
等
待
重
试
"
)
;
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
 
}
 
}
 
 
 
6
.
6
 
支
付
结
果
更
新
 
6
.
6
.
1
 
交
互
流
程
 
支
付
渠
道
代
理
服
务
查
询
到
支
付
结
果
，
将
支
付
结
果
更
新
消
息
发
送
给
交
易
服
务
，
实
现
订
单
状
态
更
新
，
流
程
如
下
：
1
、
支
付
渠
道
代
理
服
务
查
询
到
支
付
结
果
2
、
向
M
Q
发
送
“
支
付
结
果
更
新
”
消
息
3
、
交
易
服
务
监
听
“
支
付
结
果
更
新
”
消
息
队
列
4
、
交
易
服
务
接
收
到
“
支
付
结
果
更
新
”
消
息
，
更
新
订
单
状
态
 
6
.
6
.
2
 
发
送
消
息
 
在
支
付
渠
道
代
理
服
务
的
P
a
y
P
r
o
d
u
c
e
r
中
定
义
发
送
“
支
付
结
果
更
新
”
消
息
方
法
p
r
i
v
a
t
e
 
s
t
a
t
i
c
 
f
i
n
a
l
 
S
t
r
i
n
g
 
T
O
P
I
C
_
R
E
S
U
L
T
 
=
 
"
T
P
_
P
A
Y
M
E
N
T
_
R
E
S
U
L
T
"
;
 
 
 
/
*
*
 
 
*
 
发
送
支
付
结
果
消
息
 
 
*
 
@
p
a
r
a
m
 
r
e
s
u
l
t
 
 
*
/
 
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
 
p
a
y
R
e
s
u
l
t
N
o
t
i
c
e
(
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
u
l
t
)
{
 
 
 
 
r
o
c
k
e
t
M
Q
T
e
m
p
l
a
t
e
.
c
o
n
v
e
r
t
A
n
d
S
e
n
d
(
T
O
P
I
C
_
R
E
S
U
L
T
,
r
e
s
u
l
t
)
;
 
}
 
修
改
支
付
渠
道
代
理
服
务
的
P
a
y
C
o
n
s
u
m
e
r
，
在
查
询
到
支
付
结
果
后
调
用
p
a
y
R
e
s
u
l
t
N
o
t
i
c
e
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 49 -->
.
.
.
.
 
/
/
不
管
支
付
成
功
还
是
失
败
都
需
要
发
送
支
付
结
果
消
息
 
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
交
易
中
心
处
理
支
付
结
果
通
知
，
支
付
代
理
发
送
消
息
:
{
}
"
,
 
r
e
s
u
l
t
)
;
 
p
a
y
P
r
o
d
u
c
e
r
.
p
a
y
R
e
s
u
l
t
N
o
t
i
c
e
(
r
e
s
u
l
t
)
;
 
.
.
.
 
 
6
.
6
.
3
 
接
收
消
息
 
6
.
6
.
3
.
1
 
交
易
服
务
更
新
订
单
接
口
 
在
T
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
S
e
r
v
i
c
e
I
m
p
l
中
实
现
u
p
d
a
t
e
O
r
d
e
r
T
r
a
d
e
N
o
A
n
d
T
r
a
d
e
S
t
a
t
e
方
法
，
根
据
闪
聚
支
付
订
单
号
和
支
付
宝
订
单
号
更
新
订
单
状
态
：
 
6
.
6
.
3
.
2
 
交
易
服
务
接
收
消
息
 
1
）
在
交
易
服
务
工
程
中
添
加
R
o
c
k
e
t
M
Q
依
赖
：
 
2
）
在
s
h
a
n
j
u
p
a
y
-
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
-
s
e
r
v
i
c
e
的
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
引
入
此
配
置
：
 
 
 
 
/
*
*
 
 
 
 
 
*
 
更
新
订
单
支
付
状
态
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
t
r
a
d
e
N
o
 
 
 
 
 
 
 
 
 
 
 
闪
聚
平
台
订
单
号
 
 
 
 
 
*
 
@
p
a
r
a
m
 
p
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
 
支
付
宝
或
微
信
的
交
易
流
水
号
 
 
 
 
 
*
 
@
p
a
r
a
m
 
s
t
a
t
e
 
 
 
 
 
 
 
 
 
 
 
 
 
订
单
状
态
 
 
交
易
状
态
支
付
状
态
,
0
‐
订
单
生
成
,
1
‐
支
付
中
(
目
前
未
使
用
)
,
2
‐
支
付
成
功
,
4
‐
关
闭
 
5
‐
‐
失
败
 
 
 
 
 
*
/
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
 
v
o
i
d
 
u
p
d
a
t
e
O
r
d
e
r
T
r
a
d
e
N
o
A
n
d
T
r
a
d
e
S
t
a
t
e
(
S
t
r
i
n
g
 
t
r
a
d
e
N
o
,
 
S
t
r
i
n
g
 
p
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
,
 
S
t
r
i
n
g
 
s
t
a
t
e
)
 
{
 
 
 
f
i
n
a
l
 
L
a
m
b
d
a
U
p
d
a
t
e
W
r
a
p
p
e
r
<
P
a
y
O
r
d
e
r
>
 
l
a
m
b
d
a
 
=
 
n
e
w
 
U
p
d
a
t
e
W
r
a
p
p
e
r
<
P
a
y
O
r
d
e
r
>
(
)
.
l
a
m
b
d
a
(
)
;
 
 
 
l
a
m
b
d
a
.
e
q
(
P
a
y
O
r
d
e
r
:
:
g
e
t
T
r
a
d
e
N
o
,
 
t
r
a
d
e
N
o
)
.
s
e
t
(
P
a
y
O
r
d
e
r
:
:
g
e
t
P
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
,
 
p
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
)
 
 
 
 
 
 
 
 
 
.
s
e
t
(
P
a
y
O
r
d
e
r
:
:
g
e
t
T
r
a
d
e
S
t
a
t
e
,
 
s
t
a
t
e
)
;
 
 
 
i
f
 
(
s
t
a
t
e
 
!
=
 
n
u
l
l
 
&
&
 
"
2
"
.
e
q
u
a
l
s
(
s
t
a
t
e
)
)
 
{
 
 
 
 
 
 
l
a
m
b
d
a
.
s
e
t
(
P
a
y
O
r
d
e
r
:
:
g
e
t
P
a
y
S
u
c
c
e
s
s
T
i
m
e
,
 
L
o
c
a
l
D
a
t
e
T
i
m
e
.
n
o
w
(
)
)
;
 
 
 
}
 
 
 
p
a
y
O
r
d
e
r
M
a
p
p
e
r
.
u
p
d
a
t
e
(
n
u
l
l
,
 
l
a
m
b
d
a
)
;
}
 
 
 
 
 
 
 
 
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
a
p
a
c
h
e
.
r
o
c
k
e
t
m
q
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
r
o
c
k
e
t
m
q
‐
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
0
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

<!-- page 50 -->
3
）
在
交
易
服
务
定
义
“
支
付
结
果
消
息
”
消
费
类
。
@
S
l
f
4
j
 
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
R
o
c
k
e
t
M
Q
M
e
s
s
a
g
e
L
i
s
t
e
n
e
r
(
t
o
p
i
c
 
=
 
"
T
P
_
P
A
Y
M
E
N
T
_
R
E
S
U
L
T
"
,
 
c
o
n
s
u
m
e
r
G
r
o
u
p
 
=
 
"
C
I
D
_
O
R
D
E
R
_
C
O
N
S
U
M
E
R
"
)
 
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
P
a
y
C
o
n
s
u
m
e
r
 
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
 
R
o
c
k
e
t
M
Q
L
i
s
t
e
n
e
r
<
M
e
s
s
a
g
e
E
x
t
>
 
{
 
 
@
R
e
s
o
u
r
c
e
 
 
p
r
i
v
a
t
e
 
T
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
S
e
r
v
i
c
e
 
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
S
e
r
v
i
c
e
;
 
 
 
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
 
v
o
i
d
 
o
n
M
e
s
s
a
g
e
(
M
e
s
s
a
g
e
E
x
t
 
m
e
s
s
a
g
e
E
x
t
)
 
{
 
 
 
S
t
r
i
n
g
 
b
o
d
y
 
=
 
n
e
w
 
S
t
r
i
n
g
(
m
e
s
s
a
g
e
E
x
t
.
g
e
t
B
o
d
y
(
)
,
 
S
t
a
n
d
a
r
d
C
h
a
r
s
e
t
s
.
U
T
F
_
8
)
;
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
 
=
 
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
b
o
d
y
,
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
c
l
a
s
s
)
;
 
 
 
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
交
易
中
心
消
费
方
接
收
支
付
结
果
消
息
：
{
}
"
,
 
b
o
d
y
)
;
 
 
 
f
i
n
a
l
 
T
r
a
d
e
S
t
a
t
u
s
 
t
r
a
d
e
S
t
a
t
e
 
=
 
r
e
s
.
g
e
t
T
r
a
d
e
S
t
a
t
e
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
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
 
=
 
r
e
s
.
g
e
t
T
r
a
d
e
N
o
(
)
;
 
 
 
S
t
r
i
n
g
 
t
r
a
d
e
N
o
 
=
 
r
e
s
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
;
 
 
 
s
w
i
t
c
h
 
(
t
r
a
d
e
S
t
a
t
e
)
{
 
 
 
 
c
a
s
e
 
S
U
C
C
E
S
S
:
 
 
 
 
 
/
/
支
付
成
功
时
，
修
改
订
单
状
态
为
支
付
成
功
 
 
 
 
 
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
S
e
r
v
i
c
e
.
u
p
d
a
t
e
O
r
d
e
r
T
r
a
d
e
N
o
A
n
d
T
r
a
d
e
S
t
a
t
e
(
t
r
a
d
e
N
o
,
 
p
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
,
 
"
2
"
)
;
 
 
 
 
 
r
e
t
u
r
n
 
;
 
 
 
 
c
a
s
e
 
R
E
V
O
K
E
D
:
 
 
 
 
 
/
/
支
付
关
闭
时
，
修
改
订
单
状
态
为
关
闭
 
 
 
 
 
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
S
e
r
v
i
c
e
.
u
p
d
a
t
e
O
r
d
e
r
T
r
a
d
e
N
o
A
n
d
T
r
a
d
e
S
t
a
t
e
(
t
r
a
d
e
N
o
,
 
p
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
,
 
"
4
"
)
;
 
 
 
 
 
r
e
t
u
r
n
 
;
 
 
 
 
c
a
s
e
 
F
A
I
L
E
D
:
 
 
 
 
 
/
/
支
付
失
败
时
，
修
改
订
单
状
态
为
失
败
 
 
 
 
 
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
S
e
r
v
i
c
e
.
u
p
d
a
t
e
O
r
d
e
r
T
r
a
d
e
N
o
A
n
d
T
r
a
d
e
S
t
a
t
e
(
t
r
a
d
e
N
o
,
 
p
a
y
C
h
a
n
n
e
l
T
r
a
d
e
N
o
,
 
"
5
"
)
;
 
 
 
 
 
r
e
t
u
r
n
 
;
 
 
 
 
d
e
f
a
u
l
t
:
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
R
u
n
t
i
m
e
E
x
c
e
p
t
i
o
n
(
S
t
r
i
n
g
.
f
o
r
m
a
t
(
"
无
法
解
析
支
付
结
果
:
%
s
"
,
b
o
d
y
)
)
;
 
 
 
}
 
 
}
 
}
 
 
7
 
接
入
微
信
 
7
.
1
 
接
入
分
析
 
 
 
 
 
 
 
 
 
 
 
‐
 
 
 
 
 
 
 
 
 
 
 
 
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
 
 
 
 
 
 
 
 
 
 
 
 
d
a
t
a
‐
i
d
:
 
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
r
o
c
k
e
t
m
q
.
y
a
m
l
 
#
 
r
o
c
k
e
t
m
q
配
置
 
 
 
 
 
 
 
 
 
 
 
 
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
 
#
 
通
用
配
置
组
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 51 -->
闪
聚
支
付
平
台
是
将
各
各
常
用
的
第
三
方
支
付
渠
道
统
一
为
一
个
支
付
通
道
，
前
边
实
现
了
C
扫
B
支
付
宝
支
付
的
流
程
，
下
边
接
入
微
信
支
付
，
根
据
接
入
支
付
宝
的
流
程
分
析
接
入
微
信
需
要
实
现
的
如
下
：
1
、
支
付
入
口
顾
客
扫
码
进
入
支
付
入
口
，
根
据
客
户
端
类
型
判
断
是
微
信
还
是
支
付
宝
，
是
支
付
宝
则
直
接
进
入
收
银
台
，
如
果
是
微
信
则
需
要
首
先
获
取
o
p
e
n
i
d
，
再
进
入
收
银
台
。
2
、
立
即
支
付
点
击
立
即
支
付
调
用
微
信
的
统
一
下
单
接
口
，
若
下
单
成
功
则
唤
起
微
信
客
户
端
开
始
支
付
。
3
、
获
取
支
付
结
果
调
用
微
信
的
“
支
付
结
果
查
询
”
接
口
获
取
支
付
结
果
。
 
7
.
2
 
支
付
入
口
 
7
.
2
.
1
 
获
取
o
p
e
n
i
d
接
口
 
参
考
：
闪
聚
支
付
-
第
3
章
-
微
信
支
付
接
入
指
南
.
p
d
f
7
.
2
.
2
 
获
取
微
信
授
权
码
 
用
户
进
入
支
付
入
口
，
判
断
客
户
端
类
型
如
果
是
微
信
则
获
取
微
信
授
权
码
。
根
据
获
取
o
p
e
n
i
d
的
流
程
得
知
，
第
一
步
获
取
微
信
授
权
码
，
这
里
需
要
生
成
获
取
微
信
授
权
码
的
U
R
L
，
由
页
面
重
定
向
即
可
。
1
、
在
n
a
c
o
s
中
交
易
服
务
的
主
配
置
文
件
中
添
加
如
下
参
数
：
w
e
i
x
i
n
:
 
 
 
o
a
u
t
h
2
R
e
q
u
e
s
t
U
r
l
:
 
"
h
t
t
p
s
:
/
/
o
p
e
n
.
w
e
i
x
i
n
.
q
q
.
c
o
m
/
c
o
n
n
e
c
t
/
o
a
u
t
h
2
/
a
u
t
h
o
r
i
z
e
"
 
 
 
o
a
u
t
h
2
C
o
d
e
R
e
t
u
r
n
U
r
l
:
 
"
h
t
t
p
:
/
/
x
f
c
.
n
a
t
3
0
0
.
t
o
p
/
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
/
w
x
‐
o
a
u
t
h
‐
c
o
d
e
‐
r
e
t
u
r
n
"
 
 
 
o
a
u
t
h
2
T
o
k
e
n
:
 
"
h
t
t
p
s
:
/
/
a
p
i
.
w
e
i
x
i
n
.
q
q
.
c
o
m
/
s
n
s
/
o
a
u
t
h
2
/
a
c
c
e
s
s
_
t
o
k
e
n
"
 
 
2
、
在
交
易
服
务
P
a
y
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
添
加
获
取
微
信
授
权
码
方
法
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
w
e
i
x
i
n
.
o
a
u
t
h
2
R
e
q
u
e
s
t
U
r
l
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
 
w
x
O
A
u
t
h
2
R
e
q
u
e
s
t
U
r
l
;
 
 
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
w
e
i
x
i
n
.
o
a
u
t
h
2
C
o
d
e
R
e
t
u
r
n
U
r
l
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
 
w
x
O
A
u
t
h
2
C
o
d
e
R
e
t
u
r
n
U
r
l
;
 
 
/
*
*
 
 
*
 
获
取
微
信
授
权
码
 
 
*
 
 
*
 
@
p
a
r
a
m
 
o
r
d
e
r
 
订
单
对
象
 
 
*
 
@
r
e
t
u
r
n
 
 
*
 
@
t
h
r
o
w
s
 
E
x
c
e
p
t
i
o
n
 
 
*
/
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 52 -->
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
 
g
e
t
W
X
O
A
u
t
h
2
C
o
d
e
(
P
a
y
O
r
d
e
r
D
T
O
 
o
r
d
e
r
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
{
 
 
 
 
 
 
 
 
 
/
/
将
订
单
信
息
封
装
到
s
t
a
t
e
参
数
中
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
s
t
a
t
e
 
=
 
E
n
c
r
y
p
t
U
t
i
l
.
e
n
c
o
d
e
U
T
F
8
S
t
r
i
n
g
B
a
s
e
6
4
(
J
S
O
N
.
t
o
J
S
O
N
S
t
r
i
n
g
(
o
r
d
e
r
)
)
;
 
 
 
 
 
 
 
 
 
/
/
应
用
i
d
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
I
d
 
=
 
o
r
d
e
r
.
g
e
t
A
p
p
I
d
(
)
;
 
 
 
 
 
 
 
 
 
/
/
服
务
类
型
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
c
h
a
n
n
e
l
 
=
 
o
r
d
e
r
.
g
e
t
C
h
a
n
n
e
l
(
)
;
 
 
 
 
 
 
 
 
 
/
/
获
取
微
信
支
付
渠
道
参
数
，
根
据
应
用
、
服
务
类
型
、
支
付
渠
道
查
询
支
付
渠
道
参
数
 
 
 
 
 
 
 
 
 
P
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
 
p
a
y
C
h
a
n
n
e
l
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
r
a
m
B
y
A
p
p
P
l
a
t
f
o
r
m
A
n
d
P
a
y
C
h
a
n
n
e
l
(
a
p
p
I
d
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
h
a
n
n
e
l
,
 
"
W
X
_
J
S
A
P
I
"
)
;
 
 
 
 
 
 
 
 
 
i
f
(
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
=
 
n
u
l
l
)
{
 
 
 
 
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
7
)
;
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
/
/
支
付
渠
道
参
数
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
p
a
y
P
a
r
a
m
 
=
 
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
.
g
e
t
P
a
r
a
m
(
)
;
 
 
 
 
 
 
 
 
 
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
y
P
a
r
a
m
,
 
W
X
C
o
n
f
i
g
P
a
r
a
m
.
c
l
a
s
s
)
;
 
 
 
 
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
u
r
l
 
=
 
S
t
r
i
n
g
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
f
o
r
m
a
t
(
"
%
s
?
a
p
p
i
d
=
%
s
&
s
c
o
p
e
=
s
n
s
a
p
i
_
b
a
s
e
&
s
t
a
t
e
=
%
s
&
r
e
d
i
r
e
c
t
_
u
r
i
=
%
s
"
,
 
w
x
O
A
u
t
h
2
R
e
q
u
e
s
t
U
r
l
,
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
p
p
I
d
(
)
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
t
a
t
e
,
 
U
R
L
E
n
c
o
d
e
r
.
e
n
c
o
d
e
(
w
x
O
A
u
t
h
2
C
o
d
e
R
e
t
u
r
n
U
r
l
,
 
"
u
t
f
‐
8
"
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
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
微
信
生
成
授
权
码
u
r
l
:
{
}
"
,
u
r
l
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
r
e
d
i
r
e
c
t
:
"
 
+
 
u
r
l
;
 
 
 
 
 
 
 
 
 
}
 
c
a
t
c
h
 
(
U
n
s
u
p
p
o
r
t
e
d
E
n
c
o
d
i
n
g
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
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
e
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
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
‐
e
r
r
o
r
"
;
/
/
生
成
获
取
授
权
码
链
接
失
败
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
}
 
2
、
支
付
入
口
调
用
微
信
授
权
码
获
取
方
法
@
R
e
q
u
e
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
p
a
y
‐
e
n
t
r
y
/
{
t
i
c
k
e
t
}
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
 
p
a
y
E
n
t
r
y
(
@
P
a
t
h
V
a
r
i
a
b
l
e
(
"
t
i
c
k
e
t
"
)
 
S
t
r
i
n
g
 
t
i
c
k
e
t
,
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
)
 
{
 
.
.
.
 
 
 
B
r
o
w
s
e
r
T
y
p
e
 
b
r
o
w
s
e
r
T
y
p
e
 
=
 
B
r
o
w
s
e
r
T
y
p
e
.
v
a
l
u
e
O
f
U
s
e
r
A
g
e
n
t
(
r
e
q
u
e
s
t
.
g
e
t
H
e
a
d
e
r
(
"
u
s
e
r
‐
a
g
e
n
t
"
)
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
s
w
i
t
c
h
 
(
b
r
o
w
s
e
r
T
y
p
e
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
s
e
 
A
L
I
P
A
Y
:
 
/
/
直
接
跳
转
收
银
台
p
a
y
.
h
t
m
l
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
?
"
 
+
 
t
o
P
a
r
a
m
s
S
t
r
i
n
g
(
o
r
d
e
r
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
c
a
s
e
 
W
E
C
H
A
T
:
 
/
/
获
取
授
权
码
(
待
实
现
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
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
S
e
r
v
i
c
e
.
g
e
t
W
X
O
A
u
t
h
2
C
o
d
e
(
o
r
d
e
r
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
d
e
f
a
u
l
t
:
 
 
 
 
 
 
 
 
 
 
 
 
 
}
 
.
.
.
 
 
 
 
7
.
2
.
3
 
微
信
授
权
码
回
调
接
口
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 53 -->
授
权
码
获
取
成
功
后
微
信
会
将
授
权
码
传
入
授
权
码
回
调
U
R
L
，
在
授
权
码
回
调
接
口
中
实
现
获
取
o
p
e
n
i
d
。
7
.
2
.
3
.
1
 
接
口
定
义
 
1
、
在
P
a
y
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
定
义
微
信
授
权
码
回
调
接
口
@
A
p
i
O
p
e
r
a
t
i
o
n
(
"
微
信
授
权
码
回
调
"
)
 
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
w
x
‐
o
a
u
t
h
‐
c
o
d
e
‐
r
e
t
u
r
n
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
 
w
x
O
A
u
t
h
2
C
o
d
e
R
e
t
u
r
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
P
a
r
a
m
 
S
t
r
i
n
g
 
c
o
d
e
,
 
@
R
e
q
u
e
s
t
P
a
r
a
m
 
S
t
r
i
n
g
 
s
t
a
t
e
)
 
{
 
 
 
/
/
获
取
o
p
e
n
i
d
 
 
 
/
/
重
定
向
到
支
付
确
认
页
面
 
}
 
 
2
、
在
T
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
S
e
r
v
i
c
e
中
定
义
获
取
o
p
e
n
i
d
方
法
 
 
7
.
2
.
3
.
2
 
接
口
实
现
 
1
、
添
加
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
配
置
使
用
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
发
起
h
t
t
p
请
求
，
在
s
h
a
n
j
u
p
a
y
-
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
-
s
e
r
v
i
c
e
工
程
的
p
o
m
.
x
m
l
中
添
加
依
赖
：
 
在
T
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
B
o
o
t
s
t
r
a
p
中
注
入
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
 
2
、
添
加
获
取
o
p
e
n
i
d
地
址
配
置
在
n
a
c
o
s
中
向
交
易
服
务
添
加
获
取
o
p
e
n
i
d
地
址
配
置
，
如
下
：
 
 
 
 
/
*
*
 
 
 
 
 
*
 
获
取
微
信
o
p
e
n
i
d
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
c
o
d
e
 
授
权
i
d
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
p
p
I
d
 
应
用
i
d
，
用
于
获
取
微
信
支
付
的
参
数
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
o
p
e
n
i
d
 
 
 
 
 
*
/
 
 
 
 
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
W
X
O
A
u
t
h
O
p
e
n
I
d
(
S
t
r
i
n
g
 
c
o
d
e
,
 
S
t
r
i
n
g
 
a
p
p
I
d
)
;
<
!
‐
‐
 
o
k
h
t
t
p
3
 
‐
‐
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
s
q
u
a
r
e
u
p
.
o
k
h
t
t
p
3
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
o
k
h
t
t
p
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
B
e
a
n
 
 
 
 
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
n
e
w
 
O
k
H
t
t
p
3
C
l
i
e
n
t
H
t
t
p
R
e
q
u
e
s
t
F
a
c
t
o
r
y
(
)
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 54 -->
w
e
i
x
i
n
:
 
 
 
o
a
u
t
h
2
T
o
k
e
n
:
 
"
h
t
t
p
s
:
/
/
a
p
i
.
w
e
i
x
i
n
.
q
q
.
c
o
m
/
s
n
s
/
o
a
u
t
h
2
/
a
c
c
e
s
s
_
t
o
k
e
n
"
 
 
3
、
g
e
t
W
X
O
A
u
t
h
O
p
e
n
I
d
接
口
实
现
 
 
 
 
/
*
*
 
 
 
 
 
 
*
 
获
取
微
信
o
p
e
n
i
d
 
 
 
 
 
 
*
 
 
 
 
 
 
*
 
@
p
a
r
a
m
 
c
o
d
e
 
授
权
i
d
 
 
 
 
 
 
*
 
@
p
a
r
a
m
 
a
p
p
I
d
 
应
用
i
d
，
用
于
获
取
微
信
支
付
的
参
数
 
 
 
 
 
 
*
 
@
p
a
r
a
m
 
c
h
a
n
n
e
l
 
服
务
类
型
，
用
于
获
取
微
信
支
付
的
参
数
 
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
o
p
e
n
i
d
 
 
 
 
 
 
*
/
 
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
 
g
e
t
W
X
O
A
u
t
h
O
p
e
n
I
d
(
S
t
r
i
n
g
 
c
o
d
e
,
 
S
t
r
i
n
g
 
a
p
p
I
d
)
 
{
 
 
 
 
 
/
/
获
取
微
信
支
付
渠
道
参
数
，
根
据
应
用
、
服
务
类
型
、
支
付
渠
道
查
询
支
付
渠
道
参
数
 
 
 
 
 
P
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
 
p
a
y
C
h
a
n
n
e
l
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
r
a
m
B
y
A
p
p
P
l
a
t
f
o
r
m
A
n
d
P
a
y
C
h
a
n
n
e
l
(
a
p
p
I
d
,
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
h
a
n
j
u
_
c
2
b
"
,
 
"
W
X
_
J
S
A
P
I
"
)
;
 
 
 
 
 
i
f
(
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
=
 
n
u
l
l
)
{
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
7
)
;
 
 
 
 
 
}
 
 
 
 
 
/
/
支
付
渠
道
参
数
 
 
 
 
 
S
t
r
i
n
g
 
p
a
y
P
a
r
a
m
 
=
 
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
.
g
e
t
P
a
r
a
m
(
)
;
 
 
 
 
 
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
y
P
a
r
a
m
,
 
W
X
C
o
n
f
i
g
P
a
r
a
m
.
c
l
a
s
s
)
;
 
 
 
 
 
/
/
密
钥
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
S
e
c
r
e
t
 
=
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
p
p
S
e
c
r
e
t
(
)
;
 
 
 
 
 
/
/
获
取
o
p
e
n
i
d
地
址
 
 
 
 
 
S
t
r
i
n
g
 
u
r
l
 
=
 
S
t
r
i
n
g
.
f
o
r
m
a
t
(
"
%
s
?
a
p
p
i
d
=
%
s
&
s
e
c
r
e
t
=
%
s
&
c
o
d
e
=
%
s
&
g
r
a
n
t
_
t
y
p
e
=
a
u
t
h
o
r
i
z
a
t
i
o
n
_
c
o
d
e
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
o
a
u
t
h
2
T
o
k
e
n
,
w
x
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
p
p
I
d
(
)
,
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
A
p
p
S
e
c
r
e
t
(
)
,
 
c
o
d
e
)
;
 
 
 
 
 
R
e
s
p
o
n
s
e
E
n
t
i
t
y
<
S
t
r
i
n
g
>
 
e
x
c
h
a
n
g
e
 
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
e
x
c
h
a
n
g
e
(
t
o
k
e
n
U
r
l
,
 
H
t
t
p
M
e
t
h
o
d
.
G
E
T
,
 
n
u
l
l
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
t
r
i
n
g
 
r
e
s
p
o
n
s
e
 
=
 
e
x
c
h
a
n
g
e
.
g
e
t
B
o
d
y
(
)
;
 
 
 
 
 
r
e
t
u
r
n
 
J
S
O
N
O
b
j
e
c
t
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
r
e
s
p
o
n
s
e
)
.
g
e
t
S
t
r
i
n
g
(
"
o
p
e
n
i
d
"
)
;
 
}
 
4
、
微
信
授
权
码
回
调
接
口
实
现
@
A
p
i
O
p
e
r
a
t
i
o
n
(
"
微
信
授
权
码
回
调
"
)
 
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
w
x
‐
o
a
u
t
h
‐
c
o
d
e
‐
r
e
t
u
r
n
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
 
w
x
O
A
u
t
h
2
C
o
d
e
R
e
t
u
r
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
P
a
r
a
m
 
S
t
r
i
n
g
 
c
o
d
e
,
 
@
R
e
q
u
e
s
t
P
a
r
a
m
 
S
t
r
i
n
g
 
s
t
a
t
e
)
 
{
 
 
 
 
 
/
/
将
之
前
s
t
a
t
e
中
保
存
的
订
单
信
息
读
取
出
来
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
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
E
n
c
r
y
p
t
U
t
i
l
.
d
e
c
o
d
e
U
T
F
8
S
t
r
i
n
g
B
a
s
e
6
4
(
s
t
a
t
e
)
,
 
P
a
y
O
r
d
e
r
D
T
O
.
c
l
a
s
s
)
;
 
 
 
 
 
/
/
应
用
i
d
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
I
d
 
=
 
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
A
p
p
I
d
(
)
;
 
 
 
 
 
/
/
获
取
o
p
e
n
i
d
 
 
 
 
 
S
t
r
i
n
g
 
o
p
e
n
I
d
 
=
 
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
S
e
r
v
i
c
e
.
g
e
t
W
X
O
A
u
t
h
O
p
e
n
I
d
(
c
o
d
e
,
a
p
p
I
d
)
;
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
/
/
将
订
单
信
息
转
成
q
u
e
r
y
参
数
的
形
式
拼
接
起
来
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 55 -->
S
t
r
i
n
g
 
o
r
d
e
r
I
n
f
o
 
=
 
P
a
r
s
e
U
R
L
P
a
i
r
U
t
i
l
.
p
a
r
s
e
U
R
L
P
a
i
r
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
 
 
 
 
 
 
 
/
/
返
回
所
有
的
q
u
e
r
y
参
数
到
支
付
确
认
页
面
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
S
t
r
i
n
g
.
f
o
r
m
a
t
(
"
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
?
o
p
e
n
I
d
=
%
s
&
%
s
"
,
 
o
p
e
n
I
d
,
 
o
r
d
e
r
I
n
f
o
)
;
 
 
 
 
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
 
 
 
 
e
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
f
o
r
w
a
r
d
:
/
p
a
y
‐
p
a
g
e
‐
e
r
r
o
r
"
;
 
 
 
 
 
}
 
 
}
 
 
7
.
2
.
4
 
测
试
 
1
、
生
成
门
店
c
扫
b
的
二
维
码
2
、
打
开
内
网
穿
透
工
具
3
、
打
开
模
拟
器
，
使
用
微
信
扫
码
4
、
观
察
程
序
输
出
日
志
，
确
认
o
p
e
n
i
d
是
否
生
成
成
功
，
支
付
确
认
页
面
是
否
正
常
打
开
7
.
3
 
立
即
支
付
 
7
.
3
.
1
 
交
互
流
程
 
点
击
立
即
支
付
调
用
第
三
方
支
付
系
统
的
下
单
接
口
，
微
信
客
户
端
扫
码
进
入
确
认
页
面
，
点
击
立
即
支
付
则
由
渠
道
代
理
服
务
调
用
微
信
支
付
的
下
单
接
口
，
具
体
的
流
程
如
下
：
1
、
微
信
客
户
端
扫
码
进
入
确
认
页
面
，
点
击
立
即
支
付
请
求
交
易
服
务
微
信
下
单
接
口
2
、
交
易
服
务
通
过
支
付
渠
道
代
理
服
务
调
用
微
信
下
单
接
口
3
、
调
用
微
信
下
单
接
口
成
功
，
返
回
H
5
网
页
4
、
在
H
5
网
页
调
起
微
信
客
户
端
支
付
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 56 -->
7
.
3
.
1
 
支
付
渠
道
代
理
服
务
微
信
下
单
 
7
.
3
.
1
.
1
 
接
口
定
义
 
1
、
 
微
信
支
付
下
单
接
口
参
数
请
求
参
数
如
下
，
主
要
关
注
必
填
项
目
：
红
色
：
支
付
渠
道
参
数
配
置
的
内
容
蓝
色
：
微
信
s
d
k
自
动
配
置
绿
色
：
程
序
设
置
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 57 -->
响
应
参
数
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 58 -->
2
、
 
支
付
渠
道
代
理
服
务
下
单
接
口
定
义
1
）
接
口
描
述
：
调
用
微
信
j
s
a
p
i
下
单
接
口
2
）
接
口
定
义
在
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
中
定
义
接
口
：
/
*
*
 
 
*
 
微
信
j
s
a
p
i
下
单
接
口
请
求
 
 
*
 
@
p
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
 
*
 
@
p
a
r
a
m
 
w
e
C
h
a
t
B
e
a
n
 
 
*
 
@
r
e
t
u
r
n
 
h
5
页
面
所
需
要
的
数
据
 
 
*
/
 
p
u
b
l
i
c
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
J
S
A
P
I
(
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
W
e
C
h
a
t
B
e
a
n
 
w
e
C
h
a
t
B
e
a
n
)
;
 
7
.
3
.
1
.
2
 
接
口
实
现
 
将
资
料
-
-
>
代
码
下
的
W
X
S
D
K
C
o
n
ﬁ
g
.
j
a
v
a
工
具
类
拷
贝
至
支
付
渠
道
代
理
服
务
。
1
、
在
s
h
a
n
j
u
p
a
y
-
p
a
y
m
e
n
t
-
a
g
e
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
工
程
的
p
o
m
.
x
m
l
引
入
依
赖
：
 
2
、
在
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
中
实
现
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
J
S
A
P
I
方
法
<
!
‐
‐
 
微
信
支
付
S
D
K
 
‐
‐
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
g
i
t
h
u
b
.
t
e
d
z
h
d
z
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
w
x
p
a
y
‐
s
d
k
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
3
.
0
.
1
0
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
g
i
t
h
u
b
.
b
i
n
a
r
y
w
a
n
g
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
w
e
i
x
i
n
‐
j
a
v
a
‐
p
a
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
3
.
4
.
0
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

<!-- page 59 -->
/
*
*
 
 
*
 
微
信
j
s
a
p
i
下
单
接
口
请
求
 
 
*
 
 
*
 
@
p
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
 
*
 
@
p
a
r
a
m
 
w
e
C
h
a
t
B
e
a
n
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
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
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
J
S
A
P
I
(
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
W
e
C
h
a
t
B
e
a
n
 
w
e
C
h
a
t
B
e
a
n
)
 
{
 
 
 
 
 
W
X
S
D
K
C
o
n
f
i
g
 
c
o
n
f
i
g
 
=
 
n
e
w
 
W
X
S
D
K
C
o
n
f
i
g
(
w
x
C
o
n
f
i
g
P
a
r
a
m
)
;
/
/
通
过
实
际
支
付
参
数
匹
配
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
W
X
P
a
y
 
w
x
p
a
y
 
=
 
n
e
w
 
W
X
P
a
y
(
c
o
n
f
i
g
)
;
 
 
 
 
 
 
 
 
 
 
/
/
按
照
微
信
统
一
下
单
接
口
要
求
构
造
请
求
参
数
 
 
 
 
 
 
 
 
 
/
/
h
t
t
p
s
:
/
/
p
a
y
.
w
e
i
x
i
n
.
q
q
.
c
o
m
/
w
i
k
i
/
d
o
c
/
a
p
i
/
j
s
a
p
i
.
p
h
p
?
c
h
a
p
t
e
r
=
9
_
1
 
 
 
 
 
 
 
 
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
r
e
q
u
e
s
t
P
a
r
a
m
 
=
 
n
e
w
 
H
a
s
h
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
(
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
b
o
d
y
"
,
 
w
e
C
h
a
t
B
e
a
n
.
g
e
t
B
o
d
y
(
)
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
o
u
t
_
t
r
a
d
e
_
n
o
"
,
 
w
e
C
h
a
t
B
e
a
n
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
f
e
e
_
t
y
p
e
"
,
 
"
C
N
Y
"
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
t
o
t
a
l
_
f
e
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
v
a
l
u
e
O
f
(
w
e
C
h
a
t
B
e
a
n
.
g
e
t
T
o
t
a
l
F
e
e
(
)
)
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
s
p
b
i
l
l
_
c
r
e
a
t
e
_
i
p
"
,
 
w
e
C
h
a
t
B
e
a
n
.
g
e
t
S
p
b
i
l
l
C
r
e
a
t
e
I
p
(
)
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
n
o
t
i
f
y
_
u
r
l
"
,
 
w
e
C
h
a
t
B
e
a
n
.
g
e
t
N
o
t
i
f
y
U
r
l
(
)
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
t
r
a
d
e
_
t
y
p
e
"
,
 
"
J
S
A
P
I
"
)
;
 
 
 
 
 
 
 
 
 
r
e
q
u
e
s
t
P
a
r
a
m
.
p
u
t
(
"
o
p
e
n
i
d
"
,
 
w
e
C
h
a
t
B
e
a
n
.
g
e
t
O
p
e
n
I
d
(
)
)
;
 
 
 
 
 
 
 
 
 
 
/
/
调
用
微
信
统
一
下
单
A
P
I
 
 
 
 
 
 
 
 
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
r
e
s
p
 
=
 
w
x
p
a
y
.
u
n
i
f
i
e
d
O
r
d
e
r
(
r
e
q
u
e
s
t
P
a
r
a
m
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
/
/
返
回
h
5
网
页
需
要
的
数
据
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
t
i
m
e
s
t
a
m
p
 
=
 
S
t
r
i
n
g
.
v
a
l
u
e
O
f
(
S
y
s
t
e
m
.
c
u
r
r
e
n
t
T
i
m
e
M
i
l
l
i
s
(
)
 
/
 
1
0
0
0
)
;
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
k
e
y
 
=
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
g
e
t
K
e
y
(
)
;
 
 
 
 
 
 
 
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
j
s
a
p
i
P
a
y
P
a
r
a
m
 
=
 
n
e
w
 
H
a
s
h
M
a
p
<
>
(
)
;
 
 
 
 
 
 
 
 
j
s
a
p
i
P
a
y
P
a
r
a
m
.
p
u
t
(
"
a
p
p
I
d
"
,
 
r
e
s
p
.
g
e
t
(
"
a
p
p
i
d
"
)
)
;
 
 
 
 
 
 
 
 
j
s
a
p
i
P
a
y
P
a
r
a
m
.
p
u
t
(
"
p
a
c
k
a
g
e
"
,
 
"
p
r
e
p
a
y
_
i
d
=
"
 
+
 
r
e
s
p
.
g
e
t
(
"
p
r
e
p
a
y
_
i
d
"
)
)
;
 
 
 
 
 
 
 
 
j
s
a
p
i
P
a
y
P
a
r
a
m
.
p
u
t
(
"
t
i
m
e
S
t
a
m
p
"
,
 
t
i
m
e
s
t
a
m
p
)
;
 
 
 
 
 
 
 
 
j
s
a
p
i
P
a
y
P
a
r
a
m
.
p
u
t
(
"
n
o
n
c
e
S
t
r
"
,
 
U
U
I
D
.
r
a
n
d
o
m
U
U
I
D
(
)
.
t
o
S
t
r
i
n
g
(
)
)
;
 
 
 
 
 
 
 
 
j
s
a
p
i
P
a
y
P
a
r
a
m
.
p
u
t
(
"
s
i
g
n
T
y
p
e
"
,
 
"
H
M
A
C
‐
S
H
A
2
5
6
"
)
;
 
 
 
 
 
 
 
 
j
s
a
p
i
P
a
y
P
a
r
a
m
.
p
u
t
(
"
p
a
y
S
i
g
n
"
,
 
 
 
 
 
 
 
 
W
X
P
a
y
U
t
i
l
.
g
e
n
e
r
a
t
e
S
i
g
n
a
t
u
r
e
(
j
s
a
p
i
P
a
y
P
a
r
a
m
,
 
k
e
y
,
 
W
X
P
a
y
C
o
n
s
t
a
n
t
s
.
S
i
g
n
T
y
p
e
.
H
M
A
C
S
H
A
2
5
6
)
)
;
 
 
 
 
 
 
 
 
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
微
信
J
S
A
P
I
支
付
响
应
内
容
：
"
 
+
 
j
s
a
p
i
P
a
y
P
a
r
a
m
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
j
s
a
p
i
P
a
y
P
a
r
a
m
;
 
 
 
 
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
 
 
 
 
l
o
g
.
e
r
r
o
r
(
e
.
g
e
t
M
e
s
s
a
g
e
(
)
,
 
e
)
;
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
4
0
0
0
0
1
)
;
 
 
 
 
 
}
 
}
 
7
.
3
.
2
 
交
易
服
务
微
信
下
单
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 60 -->
交
易
服
务
微
信
下
单
是
提
供
给
支
付
入
口
请
求
的
微
信
付
款
的
接
口
，
当
用
户
用
微
信
客
户
端
扫
描
二
维
码
进
入
确
认
支
付
页
面
，
点
击
确
认
支
付
即
将
请
求
此
接
口
。
7
.
3
.
2
.
1
 
 
H
5
页
面
 
按
照
微
信
官
方
例
子
编
写
调
起
微
信
客
户
端
支
付
的
H
5
页
面
，
从
资
料
文
件
夹
拷
贝
“
w
x
p
a
y
.
h
t
m
l
”
到
交
易
服
务
下
7
.
3
.
2
.
2
 
接
口
定
义
 
1
、
接
口
描
述
1
）
接
收
前
端
支
付
请
求
2
）
保
存
订
单
信
息
到
闪
聚
支
付
平
台
3
）
调
用
支
付
渠
道
代
理
服
务
请
求
微
信
下
单
接
口
 
2
、
接
口
定
义
1
、
在
T
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
S
e
r
v
i
c
e
I
m
p
l
中
编
写
s
u
b
m
i
t
O
r
d
e
r
B
y
W
e
c
h
a
t
接
口
。
/
*
*
 
 
*
 
微
信
确
认
支
付
 
 
*
 
@
p
a
r
a
m
 
p
a
y
O
r
d
e
r
D
T
O
 
 
*
 
@
r
e
t
u
r
n
 
微
信
下
单
接
口
的
响
应
数
据
 
 
*
 
@
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
 
*
/
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
s
u
b
m
i
t
O
r
d
e
r
B
y
W
e
c
h
a
t
(
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
)
 
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
;
 
 
2
 
在
P
a
y
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
定
义
接
口
如
下
：
@
A
p
i
O
p
e
r
a
t
i
o
n
(
"
微
信
门
店
下
单
付
款
"
)
 
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
"
/
w
x
j
s
p
a
y
"
)
 
p
u
b
l
i
c
 
M
o
d
e
l
A
n
d
V
i
e
w
 
c
r
e
a
t
e
W
X
O
r
d
e
r
F
o
r
S
t
o
r
e
(
O
r
d
e
r
C
o
n
f
i
r
m
V
O
 
o
r
d
e
r
C
o
n
f
i
r
m
V
O
,
 
H
t
t
p
S
e
r
v
l
e
t
R
e
q
u
e
s
t
 
r
e
q
u
e
s
t
)
 
{
 
 
 
 
 
i
f
 
(
S
t
r
i
n
g
U
t
i
l
s
.
i
s
B
l
a
n
k
(
o
r
d
e
r
C
o
n
f
i
r
m
V
O
.
g
e
t
O
p
e
n
I
d
(
)
)
)
 
{
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
2
)
;
 
 
 
 
 
}
 
 
 
 
 
 
/
/
应
用
i
d
 
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
I
d
 
=
 
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
A
p
p
I
d
(
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 61 -->
A
p
p
D
T
O
 
a
p
p
 
=
 
a
p
p
S
e
r
v
i
c
e
.
g
e
t
A
p
p
B
y
I
d
(
a
p
p
I
d
)
;
 
 
 
 
 
 
/
/
商
户
i
d
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
M
e
r
c
h
a
n
t
I
d
(
a
p
p
.
g
e
t
M
e
r
c
h
a
n
t
I
d
(
)
)
;
 
 
 
 
 
 
/
/
客
户
端
i
p
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
C
l
i
e
n
t
I
p
(
I
P
U
t
i
l
.
g
e
t
I
p
A
d
d
r
(
r
e
q
u
e
s
t
)
)
;
 
 
 
 
 
 
/
/
将
前
端
输
入
的
元
转
成
分
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
T
o
t
a
l
A
m
o
u
n
t
(
I
n
t
e
g
e
r
.
p
a
r
s
e
I
n
t
(
A
m
o
u
n
t
U
t
i
l
.
c
h
a
n
g
e
Y
2
F
(
o
r
d
e
r
C
o
n
f
i
r
m
V
O
.
g
e
t
T
o
t
a
l
A
m
o
u
n
t
(
)
.
t
o
S
t
r
i
n
g
(
)
)
)
)
;
 
 
 
 
 
 
/
/
调
用
微
信
下
单
接
口
 
 
 
 
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
j
s
a
p
i
R
e
s
p
o
n
s
e
 
=
 
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
S
e
r
v
i
c
e
.
s
u
b
m
i
t
O
r
d
e
r
B
y
W
e
c
h
a
t
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
 
 
 
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
/
w
x
j
s
p
a
y
 
微
信
门
店
下
单
接
口
响
应
内
容
：
{
}
"
,
j
s
a
p
i
R
e
s
p
o
n
s
e
)
;
 
 
 
 
 
r
e
t
u
r
n
 
n
e
w
 
M
o
d
e
l
A
n
d
V
i
e
w
(
"
w
x
p
a
y
"
,
 
j
s
a
p
i
R
e
s
p
o
n
s
e
)
;
 
 
 
 
 
}
 
7
.
3
.
2
.
3
 
接
口
实
现
 
本
接
口
实
现
两
部
分
内
容
：
1
）
保
存
订
单
到
闪
聚
支
付
数
据
库
2
）
调
用
支
付
渠
道
代
理
服
务
请
求
微
信
下
单
接
口
 
1
、
保
存
订
单
实
现
方
法
同
支
付
宝
下
单
，
需
要
注
意
订
单
信
息
的
支
付
渠
道
标
识
为
W
X
_
J
S
A
P
I
：
/
*
*
 
 
*
 
微
信
确
认
支
付
 
 
*
 
 
*
 
@
p
a
r
a
m
 
p
a
y
O
r
d
e
r
D
T
O
 
 
*
 
@
r
e
t
u
r
n
 
微
信
下
单
接
口
的
响
应
数
据
 
 
*
 
@
t
h
r
o
w
s
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
 
 
*
/
 
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
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
s
u
b
m
i
t
O
r
d
e
r
B
y
W
e
c
h
a
t
(
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
)
 
{
 
 
 
 
 
 
/
/
微
信
o
p
e
n
i
d
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
o
p
e
n
I
d
 
=
 
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
O
p
e
n
I
d
(
)
;
 
 
 
 
 
 
 
 
 
p
a
y
O
r
d
e
r
D
T
O
.
s
e
t
P
a
y
C
h
a
n
n
e
l
(
"
W
X
_
J
S
A
P
I
"
)
;
 
 
 
 
 
 
 
 
 
/
/
保
存
订
单
 
 
 
 
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
s
a
v
e
 
=
 
s
a
v
e
(
p
a
y
O
r
d
e
r
D
T
O
)
;
 
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
t
r
a
d
e
N
o
 
=
 
s
a
v
e
.
g
e
t
T
r
a
d
e
N
o
(
)
;
 
 
 
 
 
 
 
 
 
/
/
微
信
统
一
下
单
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
w
e
C
h
a
t
J
s
a
p
i
(
o
p
e
n
I
d
,
t
r
a
d
e
N
o
)
;
 
 
 
 
 
}
 
2
、
请
求
支
付
渠
道
代
理
服
务
进
行
微
信
下
单
/
*
*
 
 
*
 
 
微
信
j
s
a
p
i
 
调
用
支
付
渠
道
代
理
 
 
*
 
@
p
a
r
a
m
 
o
r
d
e
r
R
e
s
u
l
t
 
下
单
请
求
 
 
*
 
@
r
e
t
u
r
n
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 62 -->
*
/
 
p
r
i
v
a
t
e
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
w
e
C
h
a
t
J
s
a
p
i
(
S
t
r
i
n
g
 
o
p
e
n
I
d
,
S
t
r
i
n
g
 
t
r
a
d
e
N
o
)
 
{
 
 
 
 
 
 
/
/
根
据
订
单
号
查
询
订
单
详
情
 
 
 
 
 
P
a
y
O
r
d
e
r
D
T
O
 
p
a
y
O
r
d
e
r
D
T
O
 
=
 
q
u
e
r
y
P
a
y
O
r
d
e
r
(
t
r
a
d
e
N
o
)
;
 
 
 
 
 
i
f
(
p
a
y
O
r
d
e
r
D
T
O
 
=
=
 
n
u
l
l
)
{
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
4
0
0
0
0
2
)
;
 
 
 
 
 
}
 
 
 
 
 
/
/
构
造
微
信
订
单
参
数
实
体
 
 
 
 
 
W
e
C
h
a
t
B
e
a
n
 
w
e
C
h
a
t
B
e
a
n
 
=
 
n
e
w
 
W
e
C
h
a
t
B
e
a
n
(
)
;
 
 
 
 
 
w
e
C
h
a
t
B
e
a
n
.
s
e
t
O
p
e
n
I
d
(
o
p
e
n
I
d
)
;
/
/
o
p
e
n
i
d
 
 
 
 
 
w
e
C
h
a
t
B
e
a
n
.
s
e
t
S
p
b
i
l
l
C
r
e
a
t
e
I
p
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
C
l
i
e
n
t
I
p
(
)
)
;
/
/
客
户
i
p
 
 
 
 
 
w
e
C
h
a
t
B
e
a
n
.
s
e
t
T
o
t
a
l
F
e
e
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
T
o
t
a
l
A
m
o
u
n
t
(
)
)
;
/
/
金
额
 
 
 
 
 
w
e
C
h
a
t
B
e
a
n
.
s
e
t
B
o
d
y
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
B
o
d
y
(
)
)
;
/
/
订
单
描
述
 
 
 
 
 
w
e
C
h
a
t
B
e
a
n
.
s
e
t
O
u
t
T
r
a
d
e
N
o
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
T
r
a
d
e
N
o
(
)
)
;
/
/
使
用
聚
合
平
台
的
订
单
号
 
 
t
r
a
d
e
N
o
 
 
 
 
 
w
e
C
h
a
t
B
e
a
n
.
s
e
t
N
o
t
i
f
y
U
r
l
(
"
n
o
n
e
"
)
;
/
/
异
步
接
收
微
信
通
知
支
付
结
果
的
地
址
(
暂
时
不
用
)
 
 
 
 
 
 
/
/
根
据
应
用
、
服
务
类
型
、
支
付
渠
道
查
询
支
付
渠
道
参
数
 
 
 
 
 
P
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
 
p
a
y
C
h
a
n
n
e
l
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
r
a
m
B
y
A
p
p
P
l
a
t
f
o
r
m
A
n
d
P
a
y
C
h
a
n
n
e
l
(
p
a
y
O
r
d
e
r
D
T
O
.
g
e
t
A
p
p
I
d
(
)
,
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
h
a
n
j
u
_
c
2
b
"
,
 
"
W
X
_
J
S
A
P
I
"
)
;
 
 
 
 
 
i
f
(
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
 
=
=
 
n
u
l
l
)
{
 
 
 
 
 
 
 
 
 
t
h
r
o
w
 
n
e
w
 
B
u
s
i
n
e
s
s
E
x
c
e
p
t
i
o
n
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
3
0
0
0
0
7
)
;
 
 
 
 
 
}
 
 
 
 
 
/
/
支
付
宝
渠
道
参
数
 
 
 
 
 
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
y
C
h
a
n
n
e
l
P
a
r
a
m
D
T
O
.
g
e
t
P
a
r
a
m
(
)
,
 
W
X
C
o
n
f
i
g
P
a
r
a
m
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
 
p
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
.
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
J
S
A
P
I
(
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
w
e
C
h
a
t
B
e
a
n
)
;
 
}
 
 
7
.
3
.
2
.
4
 
接
口
测
试
 
1
、
生
成
门
店
c
扫
b
的
二
维
码
2
、
打
开
模
拟
器
，
使
用
微
信
扫
码
，
进
入
支
付
确
认
页
面
3
、
输
入
金
额
，
点
击
立
即
支
付
4
、
观
察
控
制
台
日
志
，
最
终
订
单
写
入
闪
聚
平
台
数
据
库
5
、
调
起
微
信
支
付
客
户
端
，
输
入
密
码
支
付
成
功
 
 
7
.
4
 
获
取
支
付
结
果
 
7
.
4
.
1
 
微
信
支
付
结
果
查
询
接
口
 
根
据
获
取
支
付
结
果
的
技
术
方
案
，
接
入
微
信
需
要
请
求
微
信
查
询
支
付
结
果
，
接
口
参
数
如
下
：
请
求
参
数
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 63 -->
响
应
参
数
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 64 -->
以
下
字
段
在
r
e
t
u
r
n
_
c
o
d
e
 
、
r
e
s
u
l
t
_
c
o
d
e
、
t
r
a
d
e
_
s
t
a
t
e
都
为
S
U
C
C
E
S
S
时
有
返
回
 
，
如
t
r
a
d
e
_
s
t
a
t
e
不
为
 
S
U
C
C
E
S
S
，
则
只
返
回
o
u
t
_
t
r
a
d
e
_
n
o
（
必
传
）
和
a
t
t
a
c
h
（
选
传
）
。
支
付
结
果
：
S
U
C
C
E
S
S
—
支
付
成
功
R
E
F
U
N
D
—
转
入
退
款
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 65 -->
N
O
T
P
A
Y
—
未
支
付
C
L
O
S
E
D
—
已
关
闭
R
E
V
O
K
E
D
—
已
撤
销
（
付
款
码
支
付
）
U
S
E
R
P
A
Y
I
N
G
-
-
用
户
支
付
中
（
付
款
码
支
付
）
P
A
Y
E
R
R
O
R
-
-
支
付
失
败
(
其
他
原
因
，
如
银
行
返
回
失
败
)
 
7
.
4
.
2
 
支
付
渠
道
代
理
接
口
定
义
 
7
.
4
.
2
.
1
 
接
口
定
义
 
接
口
描
述
：
1
）
使
用
微
信
S
D
K
发
起
支
付
结
果
查
询
请
求
 
2
）
返
回
查
询
结
果
在
P
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
定
义
如
下
接
口
：
 
 
 
 
/
*
*
 
 
 
 
 
 
*
 
查
询
微
信
支
付
结
果
 
 
 
 
 
 
*
 
 
 
 
 
 
*
 
@
p
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
 
 
 
 
 
*
 
@
p
a
r
a
m
 
o
u
t
T
r
a
d
e
N
o
 
 
 
 
 
 
*
 
@
r
e
t
u
r
n
 
 
 
 
 
 
*
/
 
 
 
 
 
p
u
b
l
i
c
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
(
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
S
t
r
i
n
g
 
o
u
t
T
r
a
d
e
N
o
)
;
 
7
.
4
.
2
.
2
 
接
口
实
现
 
 
/
*
*
 
 
*
 
查
询
微
信
支
付
结
果
 
 
*
 
 
*
 
@
p
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
 
*
 
@
p
a
r
a
m
 
o
u
t
T
r
a
d
e
N
o
 
 
*
 
@
r
e
t
u
r
n
 
 
*
/
 
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
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
(
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
S
t
r
i
n
g
 
o
u
t
T
r
a
d
e
N
o
)
 
{
 
 
 
 
 
W
X
S
D
K
C
o
n
f
i
g
 
c
o
n
f
i
g
 
=
 
n
e
w
 
W
X
S
D
K
C
o
n
f
i
g
(
w
x
C
o
n
f
i
g
P
a
r
a
m
)
;
/
/
通
过
实
际
支
付
参
数
匹
配
 
 
 
 
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
r
e
s
p
 
=
 
n
u
l
l
;
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
W
X
P
a
y
 
w
x
p
a
y
 
=
 
n
e
w
 
W
X
P
a
y
(
c
o
n
f
i
g
)
;
 
 
 
 
 
 
 
 
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
d
a
t
a
 
=
 
n
e
w
 
H
a
s
h
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
(
)
;
 
 
 
 
 
 
 
 
 
d
a
t
a
.
p
u
t
(
"
o
u
t
_
t
r
a
d
e
_
n
o
"
,
 
o
u
t
T
r
a
d
e
N
o
)
;
 
 
 
 
 
 
 
 
 
r
e
s
p
 
=
 
w
x
p
a
y
.
o
r
d
e
r
Q
u
e
r
y
(
d
a
t
a
)
;
 
 
 
 
 
}
 
c
a
t
c
h
 
(
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
)
 
{
 
 
 
 
 
 
 
 
 
l
o
g
.
w
a
r
n
(
e
.
g
e
t
M
e
s
s
a
g
e
(
)
,
 
e
)
;
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
f
a
i
l
(
"
调
用
微
信
查
询
订
单
异
常
"
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
U
N
K
N
O
W
N
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 66 -->
}
 
 
 
 
 
S
t
r
i
n
g
 
r
e
t
u
r
n
C
o
d
e
 
=
 
r
e
s
p
.
g
e
t
(
"
r
e
t
u
r
n
_
c
o
d
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
 
r
e
s
u
l
t
C
o
d
e
 
=
 
r
e
s
p
.
g
e
t
(
"
r
e
s
u
l
t
_
c
o
d
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
 
t
r
a
d
e
S
t
a
t
e
 
=
 
r
e
s
p
.
g
e
t
(
"
t
r
a
d
e
_
s
t
a
t
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
I
d
 
=
 
r
e
s
p
.
g
e
t
(
"
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
_
i
d
"
)
;
 
 
 
 
 
S
t
r
i
n
g
 
t
r
a
d
e
T
y
p
e
 
=
 
r
e
s
p
.
g
e
t
(
"
t
r
a
d
e
_
t
y
p
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
 
r
e
t
u
r
n
M
s
g
 
=
 
r
e
s
p
.
g
e
t
(
"
r
e
t
u
r
n
_
m
s
g
"
)
;
 
 
 
 
i
f
 
(
"
S
U
C
C
E
S
S
"
.
e
q
u
a
l
s
(
r
e
t
u
r
n
C
o
d
e
)
 
&
&
 
"
S
U
C
C
E
S
S
"
.
e
q
u
a
l
s
(
r
e
s
u
l
t
C
o
d
e
)
)
 
{
 
/
/
 
接
口
调
用
成
功
 
 
 
 
 
 
 
 
 
 
 
 
 
i
f
 
(
"
S
U
C
C
E
S
S
"
.
e
q
u
a
l
s
(
t
r
a
d
e
S
t
a
t
e
)
)
 
{
 
/
/
交
易
成
功
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
s
u
c
c
e
s
s
(
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
I
d
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
S
U
C
C
E
S
S
,
 
"
"
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
}
 
e
l
s
e
 
i
f
 
(
"
U
S
E
R
P
A
Y
I
N
G
"
.
e
q
u
a
l
s
(
t
r
a
d
e
S
t
a
t
e
)
)
 
{
 
/
/
等
待
用
户
支
付
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
s
u
c
c
e
s
s
(
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
I
d
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
U
S
E
R
P
A
Y
I
N
G
,
 
"
"
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
}
 
e
l
s
e
 
i
f
 
(
"
P
A
Y
E
R
R
O
R
"
.
e
q
u
a
l
s
(
t
r
a
d
e
S
t
a
t
e
)
)
 
{
 
/
/
交
易
失
败
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
s
u
c
c
e
s
s
(
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
I
d
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
F
A
I
L
E
D
,
 
r
e
t
u
r
n
M
s
g
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
}
 
e
l
s
e
 
i
f
 
(
"
C
L
O
S
E
D
"
.
e
q
u
a
l
s
(
t
r
a
d
e
S
t
a
t
e
)
)
 
{
 
/
/
交
易
关
闭
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
s
u
c
c
e
s
s
(
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
I
d
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
R
E
V
O
K
E
D
,
 
r
e
t
u
r
n
M
s
g
)
;
 
 
 
 
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
r
e
t
u
r
n
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
s
u
c
c
e
s
s
(
"
暂
不
支
持
其
他
状
态
"
,
 
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
I
d
,
 
o
u
t
T
r
a
d
e
N
o
,
 
T
r
a
d
e
S
t
a
t
u
s
.
U
N
K
N
O
W
N
)
;
 
}
 
7
.
4
.
2
.
3
 
单
元
测
试
 
@
T
e
s
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
 
t
e
s
t
Q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
(
)
{
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
I
D
 
=
 
"
w
x
d
2
b
f
2
d
b
a
2
e
8
6
a
8
c
7
"
;
 
 
 
 
 
S
t
r
i
n
g
 
m
c
h
I
D
 
=
 
"
1
5
0
2
5
7
0
4
3
1
"
;
 
 
 
 
 
S
t
r
i
n
g
 
a
p
p
S
e
c
r
e
t
 
=
 
"
c
e
c
1
a
9
1
8
5
a
d
4
3
5
a
b
e
1
b
c
e
d
4
b
9
3
f
7
e
f
2
e
"
;
 
 
 
 
 
S
t
r
i
n
g
 
k
e
y
 
=
 
"
9
5
f
e
3
5
5
d
a
c
a
5
0
f
1
a
e
8
2
f
0
8
6
5
c
2
c
e
8
7
c
8
"
;
 
 
 
 
 
/
/
支
付
渠
道
参
数
 
 
 
 
 
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
=
 
n
e
w
 
W
X
C
o
n
f
i
g
P
a
r
a
m
(
)
;
 
 
 
 
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
A
p
p
I
d
(
a
p
p
I
D
)
;
 
 
 
 
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
M
c
h
I
d
(
m
c
h
I
D
)
;
 
 
 
 
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
A
p
p
S
e
c
r
e
t
(
a
p
p
S
e
c
r
e
t
)
;
 
 
 
 
 
w
x
C
o
n
f
i
g
P
a
r
a
m
.
s
e
t
K
e
y
(
k
e
y
)
;
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
p
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
=
 
p
a
y
C
h
a
n
n
e
l
A
g
e
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
(
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
"
S
J
1
2
1
6
5
8
0
9
3
0
6
3
3
5
0
6
8
1
7
"
)
;
 
 
 
 
 
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
p
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
)
;
 
 
}
 
7
.
4
.
3
 
支
付
查
询
 
7
.
4
.
3
.
1
 
发
送
支
付
结
果
查
询
消
息
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 67 -->
支
付
渠
道
代
理
服
务
完
成
微
信
下
单
接
口
的
调
用
即
向
M
Q
发
送
支
付
结
果
查
询
消
息
修
改
支
付
渠
道
代
理
服
务
的
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
J
S
A
P
I
方
法
：
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
 
M
a
p
<
S
t
r
i
n
g
,
 
S
t
r
i
n
g
>
 
c
r
e
a
t
e
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
J
S
A
P
I
(
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
W
e
C
h
a
t
B
e
a
n
 
w
e
C
h
a
t
B
e
a
n
)
 
{
 
 
 
 
 
W
X
S
D
K
C
o
n
f
i
g
 
c
o
n
f
i
g
 
=
 
n
e
w
 
W
X
S
D
K
C
o
n
f
i
g
(
w
x
C
o
n
f
i
g
P
a
r
a
m
)
;
/
/
通
过
实
际
支
付
参
数
匹
配
 
 
 
 
 
 
t
r
y
 
{
 
 
 
 
 
 
 
 
 
/
/
发
送
支
付
结
果
查
询
延
迟
消
息
 
 
 
 
 
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
<
W
X
C
o
n
f
i
g
P
a
r
a
m
>
 
n
o
t
i
c
e
 
=
 
n
e
w
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
<
W
X
C
o
n
f
i
g
P
a
r
a
m
>
(
)
;
 
 
 
 
 
 
 
 
 
n
o
t
i
c
e
.
s
e
t
O
u
t
T
r
a
d
e
N
o
(
w
e
C
h
a
t
B
e
a
n
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
)
;
 
 
 
 
 
 
 
 
 
n
o
t
i
c
e
.
s
e
t
C
o
n
t
e
n
t
(
w
x
C
o
n
f
i
g
P
a
r
a
m
)
;
 
 
 
 
 
 
 
 
 
n
o
t
i
c
e
.
s
e
t
M
s
g
(
"
A
L
I
P
A
Y
_
W
A
P
"
)
;
 
 
 
 
 
 
 
 
 
p
a
y
P
r
o
d
u
c
e
r
.
p
a
y
O
r
d
e
r
N
o
t
i
c
e
(
n
o
t
i
c
e
)
;
 
 
 
 
 
 
 
 
 
.
.
.
 
 
 
 
 
 
 
 
 
 
7
.
4
.
3
.
2
 
消
费
支
付
结
果
查
询
消
息
 
修
改
支
付
渠
道
代
理
服
务
的
P
a
y
C
o
n
s
u
m
e
r
.
.
.
 
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
 
v
o
i
d
 
o
n
M
e
s
s
a
g
e
(
M
e
s
s
a
g
e
E
x
t
 
m
e
s
s
a
g
e
E
x
t
)
 
{
 
 
 
 
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
开
始
消
费
支
付
结
果
查
询
消
息
:
{
}
"
,
 
m
e
s
s
a
g
e
E
x
t
)
;
 
 
 
 
/
/
取
出
消
息
内
容
 
 
 
 
S
t
r
i
n
g
 
b
o
d
y
 
=
 
n
e
w
 
S
t
r
i
n
g
(
m
e
s
s
a
g
e
E
x
t
.
g
e
t
B
o
d
y
(
)
,
 
S
t
a
n
d
a
r
d
C
h
a
r
s
e
t
s
.
U
T
F
_
8
)
;
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
p
o
n
s
e
 
=
 
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
b
o
d
y
,
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
.
c
l
a
s
s
)
;
 
 
 
 
S
t
r
i
n
g
 
o
u
t
T
r
a
d
e
N
o
 
=
 
r
e
s
p
o
n
s
e
.
g
e
t
O
u
t
T
r
a
d
e
N
o
(
)
;
 
 
 
 
S
t
r
i
n
g
 
m
s
g
 
=
 
r
e
s
p
o
n
s
e
.
g
e
t
M
s
g
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
a
r
a
m
 
=
 
S
t
r
i
n
g
.
v
a
l
u
e
O
f
(
r
e
s
p
o
n
s
e
.
g
e
t
C
o
n
t
e
n
t
(
)
)
;
 
 
 
 
 
/
/
判
断
是
支
付
宝
还
是
微
信
 
 
 
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
 
r
e
s
u
l
t
 
=
 
n
e
w
 
P
a
y
m
e
n
t
R
e
s
p
o
n
s
e
D
T
O
(
)
;
 
 
 
 
i
f
 
(
"
A
L
I
P
A
Y
_
W
A
P
"
.
e
q
u
a
l
s
(
m
s
g
)
)
 
{
 
 
 
 
 
 
 
/
/
查
询
支
付
宝
支
付
结
果
 
 
 
 
 
 
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
 
a
l
i
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
r
a
m
,
 
A
l
i
C
o
n
f
i
g
P
a
r
a
m
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
s
u
l
t
 
=
 
p
a
y
A
g
e
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
A
l
i
(
a
l
i
C
o
n
f
i
g
P
a
r
a
m
,
 
o
u
t
T
r
a
d
e
N
o
)
;
 
 
 
 
}
 
e
l
s
e
 
i
f
 
(
"
W
X
_
J
S
A
P
I
"
.
e
q
u
a
l
s
(
m
s
g
)
)
 
{
 
 
 
 
 
 
 
/
/
查
询
微
信
支
付
结
果
 
 
 
 
 
 
 
W
X
C
o
n
f
i
g
P
a
r
a
m
 
w
x
C
o
n
f
i
g
P
a
r
a
m
 
=
 
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
p
a
r
a
m
,
 
W
X
C
o
n
f
i
g
P
a
r
a
m
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
s
u
l
t
 
=
 
p
a
y
A
g
e
n
t
S
e
r
v
i
c
e
.
q
u
e
r
y
P
a
y
O
r
d
e
r
B
y
W
e
C
h
a
t
(
w
x
C
o
n
f
i
g
P
a
r
a
m
,
 
o
u
t
T
r
a
d
e
N
o
)
;
 
 
 
 
}
 
 
 
 
.
.
.
 
7
.
4
.
3
.
3
 
测
试
 
1
、
生
成
门
店
c
扫
b
的
二
维
码
2
、
打
开
模
拟
器
，
使
用
微
信
扫
码
，
进
入
支
付
确
认
页
面
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 68 -->
3
、
输
入
金
额
，
点
击
立
即
支
付
4
、
观
察
控
制
台
日
志
，
最
终
订
单
写
入
闪
聚
平
台
数
据
库
5
、
调
起
微
信
支
付
客
户
端
，
输
入
密
码
支
付
成
功
观
察
控
制
台
日
志
，
支
付
结
果
是
否
发
送
至
交
易
服
务
。
数
据
库
订
单
状
态
是
否
正
常
更
新
。
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
