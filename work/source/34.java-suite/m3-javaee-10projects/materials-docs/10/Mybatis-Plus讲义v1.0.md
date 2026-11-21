# Mybatis-Plus讲义v1.0

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\day02 环境搭建 Mybatis-Plus Swagger\讲义-pdf\Mybatis-Plus讲义v1.0【海量资源尽在 666java.com】.pdf
- 页数：41
- 抽取：pypdf 文本层



<!-- page 1 -->
M
y
b
a
t
i
s
-
P
l
u
s
 
课
程
目
标
：
了
解
M
y
b
a
t
i
s
-
P
l
u
s
整
合
M
y
b
a
t
i
s
-
P
l
u
s
通
用
C
R
U
D
M
y
b
a
t
i
s
-
P
l
u
s
的
配
置
条
件
构
造
器
M
y
b
a
t
i
s
-
P
l
u
s
 
的
S
e
r
v
i
c
e
封
装
代
码
生
成
器
1
 
M
y
b
a
t
i
s
-
P
l
u
s
介
绍
 
1
.
1
 
M
y
b
a
t
i
s
-
P
l
u
s
介
绍
 
M
y
B
a
t
i
s
-
P
l
u
s
（
简
称
 
M
P
）
是
一
个
 
M
y
B
a
t
i
s
 
的
增
强
工
具
，
在
 
M
y
B
a
t
i
s
 
的
基
础
上
只
做
增
强
不
做
改
变
，
为
简
化
开
发
 
提
高
效
率
而
生
。
该
框
架
由
b
a
o
m
i
d
o
u
（
苞
米
豆
）
组
织
开
发
并
且
开
源
的
。
官
网
：
h
t
t
p
s
:
/
/
m
y
b
a
t
i
s
.
p
l
u
s
/
 
或
 
h
t
t
p
s
:
/
/
m
p
.
b
a
o
m
i
d
o
u
.
c
o
m
/
 
g
i
t
h
u
b
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
b
a
o
m
i
d
o
u
/
m
y
b
a
t
i
s
-
p
l
u
s
 
码
云
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
e
e
.
c
o
m
/
b
a
o
m
i
d
o
u
/
m
y
b
a
t
i
s
-
p
l
u
s
 
愿
景
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
我
们
的
愿
景
是
成
为
 
M
y
B
a
t
i
s
 
最
好
的
搭
档
，
就
像
 
魂
斗
罗
 
中
的
 
1
P
 
2
P
，
基
友
搭
配
，
效
率
翻
倍
。
1
.
2
 
支
持
的
数
据
库
 
M
y
B
a
t
i
s
P
l
u
s
支
持
如
下
数
据
库
：
m
y
s
q
l
 
 
 
m
a
r
i
a
d
b
 
 
 
o
r
a
c
l
e
 
 
 
d
b
2
 
 
 
h
2
 
 
 
h
s
q
l
 
 
 
s
q
l
i
t
e
 
 
 
p
o
s
t
g
r
e
s
q
l
 
 
 
s
q
l
s
e
r
v
e
r
达
梦
数
据
库
 
 
 
虚
谷
数
据
库
 
 
 
人
大
金
仓
数
据
库
1
.
3
 
特
性
 
无
侵
入
：
只
做
增
强
不
做
改
变
，
引
入
它
不
会
对
现
有
工
程
产
生
影
响
，
如
丝
般
顺
滑
损
耗
小
：
启
动
即
会
自
动
注
入
基
本
 
C
R
U
D
，
性
能
基
本
无
损
耗
，
直
接
面
向
对
象
操
作
强
大
的
 
C
R
U
D
 
操
作
：
内
置
通
用
 
M
a
p
p
e
r
 
通
用
 
S
e
r
v
i
c
e
，
仅
仅
通
过
少
量
配
置
即
可
实
现
单
表
大
部
分
 
C
R
U
D
 
操
作
，
更
有
强
大
的
条
件
构
造
器
，
满
足
各
类
使
用
需
求
支
持
 
L
a
m
b
d
a
 
形
式
调
用
：
通
过
 
L
a
m
b
d
a
 
表
达
式
，
方
便
的
编
写
各
类
查
询
条
件
，
无
需
再
担
心
字
段
写
错
支
持
多
种
数
据
库
：
支
持
 
M
y
S
Q
L
 
M
a
r
i
a
D
B
 
O
r
a
c
l
e
 
D
B
2
 
H
2
 
H
S
Q
L
 
S
Q
L
i
t
e
 
P
o
s
t
g
r
e
 
S
Q
L
S
e
r
v
e
r
2
0
0
5
 
S
Q
L
S
e
r
v
e
r
 
等
多
种
数
据
库
支
持
主
键
自
动
生
成
：
支
持
多
达
 
4
 
种
主
键
策
略
（
内
含
分
布
式
唯
一
 
I
D
 
生
成
器
 
-
 
S
e
q
u
e
n
c
e
）
，
可
自
由
配
置
，
完
美
解
决
主
键
问
题
1
支
持
 
X
M
L
 
热
加
载
：
M
a
p
p
e
r
 
对
应
的
 
X
M
L
 
支
持
热
加
载
，
对
于
简
单
的
 
C
R
U
D
 
操
作
，
甚
至
可
以
无
 
X
M
L
 
启
动
支
持
 
A
c
t
i
v
e
R
e
c
o
r
d
 
模
式
：
支
持
 
A
c
t
i
v
e
R
e
c
o
r
d
 
形
式
调
用
，
实
体
类
只
需
继
承
 
M
o
d
e
l
 
类
即
可
进
行
强
大
的
 
C
R
U
D
 
操
作
支
持
自
定
义
全
局
通
用
操
作
：
支
持
全
局
通
用
方
法
注
入
（
 
W
r
i
t
e
 
o
n
c
e
,
 
u
s
e
 
a
n
y
w
h
e
r
e
 
）
支
持
关
键
词
自
动
转
义
：
支
持
数
据
库
关
键
词
（
o
r
d
e
r
 
k
e
y
.
.
.
.
.
.
）
自
动
转
义
，
还
可
自
定
义
关
键
词
内
置
代
码
生
成
器
：
采
用
代
码
或
者
 
M
a
v
e
n
 
插
件
可
快
速
生
成
 
M
a
p
p
e
r
 
 
 
M
o
d
e
l
 
 
 
S
e
r
v
i
c
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
 
层
代
码
，
支
持
模
板
引
擎
，
更
有
超
多
自
定
义
配
置
等
您
来
使
用
内
置
分
页
插
件
：
基
于
 
M
y
B
a
t
i
s
 
物
理
分
页
，
开
发
者
无
需
关
心
具
体
操
作
，
配
置
好
插
件
之
后
，
写
分
页
等
同
于
普
通
 
L
i
s
t
 
查
询
内
置
性
能
分
析
插
件
：
可
输
出
 
S
q
l
 
语
句
以
及
其
执
行
时
间
，
建
议
开
发
测
试
时
启
用
该
功
能
，
能
快
速
揪
出
慢
查
询
内
置
全
局
拦
截
插
件
：
提
供
全
表
 
d
e
l
e
t
e
 
 
 
u
p
d
a
t
e
 
操
作
智
能
分
析
阻
断
，
也
可
自
定
义
拦
截
规
则
，
预
防
误
操
作
内
置
 
S
q
l
 
注
入
剥
离
器
：
支
持
 
S
q
l
 
注
入
剥
离
，
有
效
预
防
 
S
q
l
 
注
入
攻
击
1
.
4
 
架
构
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
M
y
b
a
t
i
s
主
要
包
含
以
下
模
块
：
核
心
功
能
(
c
o
r
e
)
，
基
于
M
y
b
a
t
i
s
的
封
装
，
提
供
了
M
y
b
a
t
i
s
 
P
l
u
s
的
基
础
配
置
类
与
核
心
功
能
，
如
内
置
通
用
 
M
a
p
p
e
r
，
L
a
m
b
d
a
 
表
达
式
查
询
等
。
注
解
(
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
)
，
提
供
了
M
y
b
a
t
i
s
 
P
l
u
s
中
注
解
的
定
义
。
扩
展
功
能
(
e
x
t
e
n
s
i
o
n
)
，
提
供
扩
展
及
插
件
功
能
，
包
括
分
页
插
件
 
通
用
 
S
e
r
v
i
c
e
扩
展
 
性
能
分
析
插
件
等
。
代
码
生
成
器
(
g
e
n
e
r
a
t
o
r
)
：
通
过
代
码
生
成
器
可
以
快
速
生
成
 
M
a
p
p
e
r
接
口
 
E
n
t
i
t
y
实
体
类
 
M
a
p
p
e
r
 
X
M
L
 
S
e
r
v
i
c
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
 
等
各
个
模
块
的
代
码
，
极
大
的
提
升
了
开
发
效
率
。
执
行
流
程
：
（
1
）
扫
描
注
解
E
n
t
i
t
y
，
反
射
提
取
注
解
信
息
如
：
表
名
称
 
字
段
名
称
等
信
息
。
（
2
）
分
析
注
解
信
息
并
基
于
c
o
m
.
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
e
n
u
m
s
的
S
Q
L
模
板
生
成
基
本
C
R
U
D
 
S
Q
L
。
（
3
）
最
后
将
这
些
S
Q
L
注
入
到
M
y
b
a
t
i
s
环
境
中
。
因
此
M
y
b
a
t
i
s
 
p
l
u
s
无
需
编
写
C
R
U
D
 
S
Q
L
语
句
，
只
需
继
承
B
a
s
e
M
a
p
p
e
r
，
魔
术
般
的
拥
有
了
C
R
U
D
功
能
(
通
用
C
R
U
D
)
。
 
2
 
快
速
入
门
 
2
.
1
 
准
备
环
境
 
J
D
K
 
8
+
M
a
v
e
n
 
3
.
3
.
9
I
D
E
A
 
2
0
1
8
.
2
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
M
y
S
Q
L
5
.
7
2
.
2
 
创
建
数
据
库
以
及
表
 
创
建
数
据
库
并
设
置
字
符
集
为
u
t
f
-
8
：
 
创
建
表
和
测
试
数
据
：
 
2
.
3
 
工
程
搭
建
 
2
.
3
.
1
 
创
建
工
程
 
创
建
m
a
v
e
n
工
程
，
分
别
填
写
G
r
o
u
p
I
d
 
A
r
t
i
f
a
c
t
I
d
和
V
e
r
s
i
o
n
，
如
下
：
 
2
.
3
.
2
 
导
入
依
赖
 
导
入
m
a
v
e
n
依
赖
，
由
于
本
例
采
用
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
，
使
用
m
y
b
a
t
i
s
-
p
l
u
s
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
能
与
其
便
捷
集
成
：
版
本
规
划
：
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
：
 
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
m
y
b
a
t
i
s
-
p
l
u
s
：
 
3
.
1
.
0
 
C
R
E
A
T
E
 
D
A
T
A
B
A
S
E
 
`
m
p
`
 
C
H
A
R
A
C
T
E
R
 
S
E
T
 
'
u
t
f
8
'
 
C
O
L
L
A
T
E
 
'
u
t
f
8
_
g
e
n
e
r
a
l
_
c
i
'
;
‐
‐
 
创
建
测
试
表
C
R
E
A
T
E
 
T
A
B
L
E
 
`
t
b
_
u
s
e
r
`
 
(
 
 
`
i
d
`
 
b
i
g
i
n
t
(
2
0
)
 
N
O
T
 
N
U
L
L
 
A
U
T
O
_
I
N
C
R
E
M
E
N
T
 
C
O
M
M
E
N
T
 
'
主
键
I
D
'
,
 
 
`
u
s
e
r
_
n
a
m
e
`
 
v
a
r
c
h
a
r
(
2
0
)
 
N
O
T
 
N
U
L
L
 
C
O
M
M
E
N
T
 
'
用
户
名
'
,
 
 
`
p
a
s
s
w
o
r
d
`
 
v
a
r
c
h
a
r
(
2
0
)
 
N
O
T
 
N
U
L
L
 
C
O
M
M
E
N
T
 
'
密
码
'
,
 
 
`
n
a
m
e
`
 
v
a
r
c
h
a
r
(
3
0
)
 
D
E
F
A
U
L
T
 
N
U
L
L
 
C
O
M
M
E
N
T
 
'
姓
名
'
,
 
 
`
a
g
e
`
 
i
n
t
(
1
1
)
 
D
E
F
A
U
L
T
 
N
U
L
L
 
C
O
M
M
E
N
T
 
'
年
龄
'
,
 
 
`
e
m
a
i
l
`
 
v
a
r
c
h
a
r
(
5
0
)
 
D
E
F
A
U
L
T
 
N
U
L
L
 
C
O
M
M
E
N
T
 
'
邮
箱
'
,
 
 
`
b
i
r
t
h
d
a
y
`
 
d
a
t
e
t
i
m
e
 
D
E
F
A
U
L
T
 
N
U
L
L
,
 
 
P
R
I
M
A
R
Y
 
K
E
Y
 
(
`
i
d
`
)
)
 
E
N
G
I
N
E
=
I
n
n
o
D
B
 
A
U
T
O
_
I
N
C
R
E
M
E
N
T
=
1
 
D
E
F
A
U
L
T
 
C
H
A
R
S
E
T
=
u
t
f
8
;
 
‐
‐
 
插
入
测
试
数
据
i
n
s
e
r
t
 
 
i
n
t
o
 
`
t
b
_
u
s
e
r
`
(
`
i
d
`
,
`
u
s
e
r
_
n
a
m
e
`
,
`
p
a
s
s
w
o
r
d
`
,
`
n
a
m
e
`
,
`
a
g
e
`
,
`
e
m
a
i
l
`
,
`
b
i
r
t
h
d
a
y
`
)
 
v
a
l
u
e
s
 
(
1
,
'
z
h
a
n
g
s
a
n
'
,
'
1
2
3
4
5
6
'
,
'
张
三
'
,
1
8
,
'
t
e
s
t
1
@
i
t
c
a
s
t
.
c
n
'
,
'
2
0
1
9
‐
0
9
‐
2
6
 
1
1
:
4
2
:
0
1
'
)
,
(
2
,
'
l
i
s
i
'
,
'
1
2
3
4
5
6
'
,
'
李
四
'
,
2
0
,
'
t
e
s
t
2
@
i
t
c
a
s
t
.
c
n
'
,
'
2
0
1
9
‐
1
0
‐
0
1
 
1
1
:
4
2
:
0
8
'
)
,
(
3
,
'
w
a
n
g
w
u
'
,
'
1
2
3
4
5
6
'
,
'
王
五
'
,
2
8
,
'
t
e
s
t
3
@
i
t
c
a
s
t
.
c
n
'
,
'
2
0
1
9
‐
1
0
‐
0
2
 
1
1
:
4
2
:
1
4
'
)
,
(
4
,
'
z
h
a
o
l
i
u
'
,
'
1
2
3
4
5
6
'
,
'
赵
六
'
,
2
1
,
'
t
e
s
t
4
@
i
t
c
a
s
t
.
c
n
'
,
'
2
0
1
9
‐
1
0
‐
0
5
 
1
1
:
4
2
:
1
8
'
)
,
(
5
,
'
s
u
n
q
i
'
,
'
1
2
3
4
5
6
'
,
'
孙
七
'
,
2
4
,
'
t
e
s
t
5
@
i
t
c
a
s
t
.
c
n
'
,
'
2
0
1
9
‐
1
0
‐
1
4
 
1
1
:
4
2
:
2
3
'
)
;
 
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
n
.
i
t
c
a
s
t
.
m
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
i
t
c
a
s
t
‐
m
p
‐
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

<!-- page 5 -->
2
.
3
.
3
 
编
写
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
n
.
i
t
c
a
s
t
.
m
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
i
t
c
a
s
t
‐
m
p
‐
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
t
e
s
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
s
c
o
p
e
>
t
e
s
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
!
‐
‐
简
化
代
码
的
工
具
包
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
p
r
o
j
e
c
t
l
o
m
b
o
k
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
l
o
m
b
o
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
o
p
t
i
o
n
a
l
>
t
r
u
e
<
/
o
p
t
i
o
n
a
l
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
!
‐
‐
m
y
b
a
t
i
s
‐
p
l
u
s
的
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
支
持
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
b
a
o
m
i
d
o
u
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
m
y
b
a
t
i
s
‐
p
l
u
s
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
3
.
1
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
 
 
 
 
 
 
 
 
<
!
‐
‐
m
y
s
q
l
驱
动
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
m
y
s
q
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
m
y
s
q
l
‐
c
o
n
n
e
c
t
o
r
‐
j
a
v
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
v
e
r
s
i
o
n
>
8
.
0
.
1
1
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

<!-- page 6 -->
2
.
3
.
4
 
编
写
p
o
j
o
 
 
@
D
a
t
a
：
l
o
m
b
o
k
的
注
解
，
使
用
它
可
以
省
略
g
e
t
t
e
r
/
s
e
t
t
e
r
方
法
。
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
：
 
生
成
无
参
构
造
 
方
法
@
A
l
l
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
：
生
成
所
有
参
数
构
造
 
方
法
，
参
数
顺
序
与
属
性
定
义
顺
序
一
致
。
@
T
a
b
l
e
N
a
m
e
：
指
定
表
名
@
T
a
b
l
e
I
d
：
指
定
主
键
名
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
 
i
t
c
a
s
t
‐
m
p
‐
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
d
r
i
v
e
r
‐
c
l
a
s
s
‐
n
a
m
e
=
c
o
m
.
m
y
s
q
l
.
c
j
.
j
d
b
c
.
D
r
i
v
e
r
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
u
r
l
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
2
7
.
0
.
0
.
1
:
3
3
0
6
/
m
p
?
u
s
e
U
n
i
c
o
d
e
=
t
r
u
e
&
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
U
T
F
‐
8
&
s
e
r
v
e
r
T
i
m
e
z
o
n
e
=
A
s
i
a
/
S
h
a
n
g
h
a
i
&
u
s
e
S
S
L
=
f
a
l
s
e
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
u
s
e
r
n
a
m
e
=
r
o
o
t
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
a
s
s
w
o
r
d
=
r
o
o
t
 
#
 
L
o
g
g
e
r
 
C
o
n
f
i
g
l
o
g
g
i
n
g
.
l
e
v
e
l
.
r
o
o
t
:
 
d
e
b
u
g
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
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
T
a
b
l
e
N
a
m
e
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
A
l
l
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
.
t
i
m
e
.
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
;
 
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
@
A
l
l
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
@
T
a
b
l
e
N
a
m
e
(
"
t
b
_
u
s
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
 
c
l
a
s
s
 
U
s
e
r
 
{
 
 
 
 
@
T
a
b
l
e
I
d
(
"
I
D
"
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
T
a
b
l
e
F
i
e
l
d
(
"
U
S
E
R
_
N
A
M
E
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
 
u
s
e
r
N
a
m
e
;
 
/
/
驼
峰
命
名
,
则
无
需
注
解
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
P
A
S
S
W
O
R
D
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
s
s
w
o
r
d
;
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
N
A
M
E
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
 
n
a
m
e
;
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
A
G
E
"
)
 
 
 
 
p
r
i
v
a
t
e
 
I
n
t
e
g
e
r
 
a
g
e
;
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
E
M
A
I
L
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
 
e
m
a
i
l
;
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
B
I
R
T
H
D
A
Y
"
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
 
b
i
r
t
h
d
a
y
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
@
T
a
b
l
e
F
i
e
l
d
：
指
定
列
名
 
2
.
3
.
5
 
编
写
m
a
p
p
e
r
 
 
2
.
3
.
6
 
编
写
启
动
类
 
 
2
.
3
.
7
 
编
写
测
试
用
例
 
编
写
U
s
e
r
M
a
p
p
e
r
的
测
试
用
例
 
，
使
用
U
s
e
r
M
a
p
p
e
r
查
询
用
户
列
表
。
在
t
e
s
t
下
创
建
测
试
类
，
包
名
为
 
c
n
.
i
t
c
a
s
t
.
m
p
。
 
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
m
a
p
p
e
r
.
B
a
s
e
M
a
p
p
e
r
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
 
U
s
e
r
M
a
p
p
e
r
 
e
x
t
e
n
d
s
 
B
a
s
e
M
a
p
p
e
r
<
U
s
e
r
>
 
{
}
 
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
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
m
y
b
a
t
i
s
.
s
p
r
i
n
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
M
a
p
p
e
r
S
c
a
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
W
e
b
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
T
y
p
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
b
u
i
l
d
e
r
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
B
u
i
l
d
e
r
;
 
@
M
a
p
p
e
r
S
c
a
n
(
"
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
"
)
 
/
/
设
置
m
a
p
p
e
r
接
口
的
扫
描
包
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
 
M
y
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
M
y
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
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
测
试
：
 
3
 
常
见
配
置
 
在
M
P
中
有
大
量
的
配
置
，
其
中
有
一
部
分
是
M
y
b
a
t
i
s
原
生
的
配
置
，
另
一
部
分
是
M
P
的
配
置
，
详
情
：
h
t
t
p
s
:
/
/
m
y
b
a
t
i
s
.
p
l
u
s
/
c
o
n
ﬁ
g
/
下
面
我
们
对
常
用
的
配
置
做
讲
解
。
3
.
1
 
c
o
n
ﬁ
g
L
o
c
a
t
i
o
n
s
 
c
o
n
ﬁ
g
L
o
c
a
t
i
o
n
s
即
M
y
B
a
t
i
s
 
配
置
文
件
位
置
，
如
果
您
有
单
独
的
 
M
y
B
a
t
i
s
 
配
置
，
请
将
其
路
径
配
置
到
 
c
o
n
ﬁ
g
L
o
c
a
t
i
o
n
中
。
 
M
y
B
a
t
i
s
 
C
o
n
ﬁ
g
u
r
a
t
i
o
n
 
的
具
体
内
容
请
参
考
M
y
B
a
t
i
s
 
官
方
文
档
示
例
：
1
 
在
r
e
s
o
u
r
c
e
s
下
创
建
m
y
b
a
t
i
s
-
c
o
n
ﬁ
g
.
x
m
l
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
e
l
e
c
t
(
)
 
{
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
L
i
s
t
 
=
 
u
s
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
L
i
s
t
(
n
u
l
l
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
L
i
s
t
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
L
i
s
t
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
L
i
s
t
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
L
i
s
t
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
5
[
m
a
i
n
]
 
[
o
r
g
.
m
y
b
a
t
i
s
.
s
p
r
i
n
g
.
S
q
l
S
e
s
s
i
o
n
U
t
i
l
s
]
‐
[
D
E
B
U
G
]
 
C
l
o
s
i
n
g
 
n
o
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
a
l
 
S
q
l
S
e
s
s
i
o
n
 
[
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
i
b
a
t
i
s
.
s
e
s
s
i
o
n
.
d
e
f
a
u
l
t
s
.
D
e
f
a
u
l
t
S
q
l
S
e
s
s
i
o
n
@
1
4
f
a
a
3
8
c
]
U
s
e
r
(
i
d
=
1
,
 
u
s
e
r
N
a
m
e
=
z
h
a
n
g
s
a
n
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
张
三
,
 
a
g
e
=
1
8
,
 
e
m
a
i
l
=
t
e
s
t
1
@
i
t
c
a
s
t
.
c
n
,
 
b
i
r
t
h
d
a
y
=
2
0
1
9
‐
0
9
‐
2
6
T
1
1
:
4
2
:
0
1
)
U
s
e
r
(
i
d
=
2
,
 
u
s
e
r
N
a
m
e
=
l
i
s
i
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
李
四
,
 
a
g
e
=
2
0
,
 
e
m
a
i
l
=
t
e
s
t
2
@
i
t
c
a
s
t
.
c
n
,
 
b
i
r
t
h
d
a
y
=
2
0
1
9
‐
1
0
‐
0
1
T
1
1
:
4
2
:
0
8
)
U
s
e
r
(
i
d
=
3
,
 
u
s
e
r
N
a
m
e
=
w
a
n
g
w
u
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
王
五
,
 
a
g
e
=
2
8
,
 
e
m
a
i
l
=
t
e
s
t
3
@
i
t
c
a
s
t
.
c
n
,
 
b
i
r
t
h
d
a
y
=
2
0
1
9
‐
1
0
‐
0
2
T
1
1
:
4
2
:
1
4
)
U
s
e
r
(
i
d
=
4
,
 
u
s
e
r
N
a
m
e
=
z
h
a
o
l
i
u
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
赵
六
,
 
a
g
e
=
2
1
,
 
e
m
a
i
l
=
t
e
s
t
4
@
i
t
c
a
s
t
.
c
n
,
 
b
i
r
t
h
d
a
y
=
2
0
1
9
‐
1
0
‐
0
5
T
1
1
:
4
2
:
1
8
)
U
s
e
r
(
i
d
=
5
,
 
u
s
e
r
N
a
m
e
=
s
u
n
q
i
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
孙
七
,
 
a
g
e
=
2
4
,
 
e
m
a
i
l
=
t
e
s
t
5
@
i
t
c
a
s
t
.
c
n
,
 
b
i
r
t
h
d
a
y
=
2
0
1
9
‐
1
0
‐
1
4
T
1
1
:
4
2
:
2
3
)
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
2
 
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
下
配
置
c
o
n
ﬁ
g
L
o
c
a
t
i
o
n
s
，
如
下
：
 
3
.
2
 
m
a
p
p
e
r
L
o
c
a
t
i
o
n
s
 
m
a
p
p
e
r
L
o
c
a
t
i
o
n
s
即
M
y
B
a
t
i
s
 
M
a
p
p
e
r
 
所
对
应
的
 
m
a
p
p
e
r
配
置
 
文
件
位
置
，
如
果
您
在
 
M
a
p
p
e
r
 
中
有
自
定
义
方
法
（
X
M
L
 
中
有
自
定
义
实
现
）
，
需
要
进
行
该
配
置
，
告
诉
 
M
a
p
p
e
r
 
所
对
应
的
 
X
M
L
 
文
件
位
置
。
如
果
不
配
置
m
a
p
p
e
r
L
o
c
a
t
i
o
n
s
时
，
m
a
p
p
e
r
的
x
m
l
文
件
存
放
路
径
需
要
和
m
a
p
p
e
r
 
c
l
a
s
s
文
件
保
持
一
致
，
文
件
名
保
持
 
一
致
，
如
下
：
测
试
：
新
建
U
s
e
r
M
a
p
p
e
r
.
x
m
l
：
将
此
文
件
放
在
r
e
s
o
u
r
c
e
s
/
c
n
/
i
t
c
a
s
t
/
m
p
/
m
a
p
p
e
r
下
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
!
D
O
C
T
Y
P
E
 
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
 
 
 
 
 
 
 
 
P
U
B
L
I
C
 
"
‐
/
/
m
y
b
a
t
i
s
.
o
r
g
/
/
D
T
D
 
C
o
n
f
i
g
 
3
.
0
/
/
E
N
"
 
 
 
 
 
 
 
 
"
h
t
t
p
:
/
/
m
y
b
a
t
i
s
.
o
r
g
/
d
t
d
/
m
y
b
a
t
i
s
‐
3
‐
c
o
n
f
i
g
.
d
t
d
"
>
<
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
>
 
 
 
 
 
 
 
 
<
!
‐
‐
<
p
l
u
g
i
n
s
>
‐
‐
>
 
 
 
 
 
 
 
 
<
!
‐
‐
<
p
l
u
g
i
n
 
i
n
t
e
r
c
e
p
t
o
r
=
"
c
o
m
.
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
e
x
t
e
n
s
i
o
n
.
p
l
u
g
i
n
s
.
P
a
g
i
n
a
t
i
o
n
I
n
t
e
r
c
e
p
t
o
r
"
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
‐
‐
>
 
 
 
 
<
!
‐
‐
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
‐
‐
>
 
<
/
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
>
m
y
b
a
t
i
s
‐
p
l
u
s
.
c
o
n
f
i
g
‐
l
o
c
a
t
i
o
n
 
=
 
c
l
a
s
s
p
a
t
h
:
m
y
b
a
t
i
s
‐
c
o
n
f
i
g
.
x
m
l
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
测
试
用
例
：
 
运
行
结
果
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
!
D
O
C
T
Y
P
E
 
m
a
p
p
e
r
 
 
 
 
 
 
 
 
P
U
B
L
I
C
 
"
‐
/
/
m
y
b
a
t
i
s
.
o
r
g
/
/
D
T
D
 
M
a
p
p
e
r
 
3
.
0
/
/
E
N
"
 
 
 
 
 
 
 
 
"
h
t
t
p
:
/
/
m
y
b
a
t
i
s
.
o
r
g
/
d
t
d
/
m
y
b
a
t
i
s
‐
3
‐
m
a
p
p
e
r
.
d
t
d
"
>
<
m
a
p
p
e
r
 
n
a
m
e
s
p
a
c
e
=
"
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
"
>
 
 
 
 
 
<
s
e
l
e
c
t
 
i
d
=
"
f
i
n
d
B
y
I
d
"
 
r
e
s
u
l
t
T
y
p
e
=
"
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
"
 
p
a
r
a
m
e
t
e
r
T
y
p
e
=
"
j
a
v
a
.
l
a
n
g
.
L
o
n
g
"
>
 
 
 
 
 
 
s
e
l
e
c
t
 
*
 
f
r
o
m
 
t
b
_
u
s
e
r
 
w
h
e
r
e
 
i
d
 
=
 
#
{
i
d
}
 
 
 
 
<
/
s
e
l
e
c
t
>
 
<
/
m
a
p
p
e
r
>
/
/
在
U
s
e
r
M
a
p
p
e
r
接
口
类
中
新
增
f
i
n
d
B
y
I
d
方
法
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
m
a
p
p
e
r
.
B
a
s
e
M
a
p
p
e
r
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
 
U
s
e
r
M
a
p
p
e
r
 
e
x
t
e
n
d
s
 
B
a
s
e
M
a
p
p
e
r
<
U
s
e
r
>
 
{
 
 
 
 
 
U
s
e
r
 
f
i
n
d
B
y
I
d
(
L
o
n
g
 
i
d
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
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
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
)
 
{
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
t
h
i
s
.
u
s
e
r
M
a
p
p
e
r
.
f
i
n
d
B
y
I
d
(
2
L
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
u
s
e
r
)
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
也
可
以
给
m
a
p
p
e
r
 
X
M
L
文
件
定
义
一
个
和
m
a
p
p
e
r
接
口
不
同
的
存
放
路
径
 
，
如
下
：
 
M
a
v
e
n
 
多
模
块
项
目
的
扫
描
路
径
需
以
 
c
l
a
s
s
p
a
t
h
*
:
 
开
头
 
（
即
加
载
多
个
 
j
a
r
 
包
下
的
 
X
M
L
 
文
件
）
 
3
.
3
 
t
y
p
e
A
l
i
a
s
e
s
P
a
c
k
a
g
e
 
设
置
M
y
B
a
i
t
s
 
别
名
包
扫
描
路
径
，
通
过
该
属
性
可
以
给
包
中
的
类
注
册
别
名
，
注
册
后
在
 
M
a
p
p
e
r
 
对
应
的
 
X
M
L
 
文
件
中
可
以
直
接
使
用
类
名
，
而
不
用
使
用
全
限
定
的
类
名
（
即
 
X
M
L
 
中
调
用
的
时
候
不
用
包
含
包
名
）
。
示
例
：
 
3
.
4
 
m
a
p
U
n
d
e
r
s
c
o
r
e
T
o
C
a
m
e
l
C
a
s
e
 
类
型
：
b
o
o
l
e
a
n
默
认
值
：
t
r
u
e
是
否
开
启
自
动
驼
峰
命
名
规
则
（
c
a
m
e
l
 
c
a
s
e
）
映
射
，
即
从
经
典
数
据
库
列
名
 
A
_
C
O
L
U
M
N
（
下
划
线
命
名
）
 
到
经
典
 
J
a
v
a
属
性
名
 
a
C
o
l
u
m
n
（
驼
峰
命
名
）
 
的
类
似
映
射
。
注
意
：
在
 
M
y
B
a
t
i
s
-
P
l
u
s
 
中
此
属
性
默
认
值
为
t
r
u
e
，
用
于
生
成
最
终
的
 
S
Q
L
 
语
句
如
果
您
的
数
据
库
命
名
符
合
规
则
无
需
使
用
 
@
T
a
b
l
e
F
i
e
l
d
 
注
解
指
定
数
据
库
字
段
名
测
试
：
 
 
1
 
屏
蔽
@
T
a
b
l
e
F
i
e
l
d
 
m
y
b
a
t
i
s
‐
p
l
u
s
.
m
a
p
p
e
r
‐
l
o
c
a
t
i
o
n
s
 
=
 
c
l
a
s
s
p
a
t
h
*
:
m
y
b
a
t
i
s
/
m
a
p
p
e
r
/
*
.
x
m
l
m
y
b
a
t
i
s
‐
p
l
u
s
.
t
y
p
e
‐
a
l
i
a
s
e
s
‐
p
a
c
k
a
g
e
 
=
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
#
开
启
自
动
驼
峰
映
射
，
注
意
：
配
置
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
.
m
a
p
‐
u
n
d
e
r
s
c
o
r
e
‐
t
o
‐
c
a
m
e
l
‐
c
a
s
e
则
不
能
配
置
c
o
n
f
i
g
‐
l
o
c
a
t
i
o
n
m
y
b
a
t
i
s
‐
p
l
u
s
.
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
.
m
a
p
‐
u
n
d
e
r
s
c
o
r
e
‐
t
o
‐
c
a
m
e
l
‐
c
a
s
e
=
t
r
u
e
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
@
A
l
l
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
@
T
a
b
l
e
N
a
m
e
(
"
t
b
_
u
s
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
 
c
l
a
s
s
 
U
s
e
r
 
{
 
 
 
 
@
T
a
b
l
e
I
d
(
"
I
D
"
)
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
2
 
测
试
u
s
e
r
M
a
p
p
e
r
.
ﬁ
n
d
B
y
I
d
方
法
跟
踪
发
现
u
s
e
r
N
a
m
e
可
以
映
射
成
功
。
如
果
项
目
中
有
符
合
驼
峰
规
则
的
定
义
也
有
不
符
合
的
，
此
时
建
议
统
一
使
用
@
T
a
b
l
e
F
i
e
l
d
。
3
.
如
果
使
用
m
y
b
a
t
i
s
-
c
o
n
ﬁ
g
.
x
m
l
的
同
时
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
配
置
m
y
b
a
t
i
s
-
p
l
u
s
.
c
o
n
ﬁ
g
u
r
a
t
i
o
n
则
报
错
P
r
o
p
e
r
t
y
 
'
c
o
n
ﬁ
g
u
r
a
t
i
o
n
'
 
a
n
d
 
'
c
o
n
ﬁ
g
L
o
c
a
t
i
o
n
'
 
c
a
n
 
n
o
t
 
s
p
e
c
i
ﬁ
e
d
 
w
i
t
h
 
t
o
g
e
t
h
e
r
解
决
方
法
：
只
使
用
一
种
配
置
方
法
。
本
案
例
屏
蔽
m
y
b
a
t
i
s
-
p
l
u
s
.
c
o
n
ﬁ
g
u
r
a
t
i
o
n
.
m
a
p
-
u
n
d
e
r
s
c
o
r
e
-
t
o
-
c
a
m
e
l
-
c
a
s
e
=
t
r
u
e
，
在
m
y
b
a
t
i
s
-
c
o
n
ﬁ
g
.
x
m
l
中
配
置
s
e
t
t
i
n
g
s
。
 
 
4
 
通
用
C
R
U
D
 
通
过
前
面
的
学
习
，
我
们
了
解
到
通
过
继
承
B
a
s
e
M
a
p
p
e
r
就
可
以
获
取
到
各
种
各
样
的
单
表
操
作
，
接
下
来
我
们
将
详
细
讲
解
这
些
操
作
，
下
图
是
B
a
s
e
M
a
p
p
e
r
的
各
各
方
法
：
 
 
 
 
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
/
/
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
U
S
E
R
_
N
A
M
E
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
 
u
s
e
r
N
a
m
e
;
 
/
/
驼
峰
命
名
,
则
无
需
注
解
/
/
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
P
A
S
S
W
O
R
D
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
s
s
w
o
r
d
;
/
/
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
N
A
M
E
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
 
n
a
m
e
;
/
/
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
A
G
E
"
)
 
 
 
 
p
r
i
v
a
t
e
 
I
n
t
e
g
e
r
 
a
g
e
;
/
/
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
E
M
A
I
L
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
 
e
m
a
i
l
;
/
/
 
 
 
 
@
T
a
b
l
e
F
i
e
l
d
(
"
B
I
R
T
H
D
A
Y
"
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
 
b
i
r
t
h
d
a
y
;
}
<
s
e
t
t
i
n
g
s
>
 
 
 
 
<
s
e
t
t
i
n
g
 
n
a
m
e
=
"
m
a
p
U
n
d
e
r
s
c
o
r
e
T
o
C
a
m
e
l
C
a
s
e
"
 
v
a
l
u
e
=
"
t
r
u
e
"
/
>
<
/
s
e
t
t
i
n
g
s
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
4
.
1
 
插
入
操
作
 
4
.
1
.
1
 
方
法
定
义
 
 
4
.
1
.
2
 
测
试
用
例
 
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
插
入
一
条
记
录
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
e
n
t
i
t
y
 
实
体
对
象
 
 
 
 
 
*
/
 
 
 
 
i
n
t
 
i
n
s
e
r
t
(
T
 
e
n
t
i
t
y
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
T
e
s
t
 
{
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 14 -->
4
.
1
.
3
 
M
P
主
键
生
成
策
略
 
上
例
中
M
y
b
a
t
i
s
-
p
l
u
s
自
动
生
成
I
D
，
如
何
设
置
i
d
的
生
成
策
略
呢
？
M
P
支
持
的
i
d
策
略
如
下
：
 
 
 
 
 
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
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
I
n
s
e
r
t
(
)
{
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
n
e
w
 
U
s
e
r
(
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
A
g
e
(
2
0
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
E
m
a
i
l
(
"
t
e
s
t
@
i
t
c
a
s
t
.
c
n
"
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
N
a
m
e
(
"
曹
操
"
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
U
s
e
r
N
a
m
e
(
"
c
a
o
c
a
o
"
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
P
a
s
s
w
o
r
d
(
"
1
2
3
4
5
6
"
)
;
 
 
 
 
 
 
 
 
D
a
t
e
T
i
m
e
F
o
r
m
a
t
t
e
r
 
d
f
 
=
 
D
a
t
e
T
i
m
e
F
o
r
m
a
t
t
e
r
.
o
f
P
a
t
t
e
r
n
(
"
y
y
y
y
‐
M
M
‐
d
d
 
H
H
:
m
m
:
s
s
"
)
;
 
 
 
 
 
 
 
 
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
 
l
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
 
=
 
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
p
a
r
s
e
(
"
1
9
9
0
‐
0
1
‐
0
1
 
0
0
:
0
0
:
0
0
"
,
 
d
f
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
B
i
r
t
h
d
a
y
(
l
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
)
;
 
 
 
 
 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
t
h
i
s
.
u
s
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
u
s
e
r
)
;
 
/
/
返
回
的
r
e
s
u
l
t
是
受
影
响
的
行
数
，
并
不
是
自
增
后
的
i
d
 
 
 
 
 
 
 
 
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
r
e
s
u
l
t
 
=
 
"
 
+
 
r
e
s
u
l
t
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
u
s
e
r
.
g
e
t
I
d
(
)
)
;
 
/
/
自
增
后
的
i
d
会
回
填
到
对
象
中
 
 
 
 
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
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
G
e
t
t
e
r
;
 
/
*
*
 
*
 
生
成
I
D
类
型
枚
举
类
 
*
 
*
 
@
a
u
t
h
o
r
 
h
u
b
i
n
 
*
 
@
s
i
n
c
e
 
2
0
1
5
‐
1
1
‐
1
0
 
*
/
@
G
e
t
t
e
r
p
u
b
l
i
c
 
e
n
u
m
 
I
d
T
y
p
e
 
{
 
 
 
 
/
*
*
 
 
 
 
 
*
 
数
据
库
I
D
自
增
 
 
 
 
 
*
/
 
 
 
 
A
U
T
O
(
0
)
,
 
 
 
 
/
*
*
 
 
 
 
 
*
 
该
类
型
为
未
设
置
主
键
类
型
 
 
 
 
 
*
/
 
 
 
 
N
O
N
E
(
1
)
,
 
 
 
 
/
*
*
 
 
 
 
 
*
 
用
户
输
入
I
D
 
 
 
 
 
*
 
<
p
>
该
类
型
可
以
通
过
自
己
注
册
自
动
填
充
插
件
进
行
填
充
<
/
p
>
 
 
 
 
 
*
/
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 15 -->
1
 
自
增
主
键
：
完
全
采
用
数
据
库
自
增
主
键
方
式
。
1
）
设
置
m
y
s
q
l
数
据
库
主
键
为
自
增
2
）
修
改
U
s
e
r
对
象
：
 
3
）
程
序
中
不
用
设
置
主
键
 
2
 
输
入
主
键
：
手
动
设
置
主
键
值
。
1
）
m
y
s
q
l
数
据
库
主
键
为
自
增
或
不
是
自
增
都
可
以
2
）
修
改
U
s
e
r
对
象
：
 
3
）
程
序
中
需
要
设
置
主
键
 
 
 
 
 
I
N
P
U
T
(
2
)
,
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
全
局
唯
一
I
D
 
(
i
d
W
o
r
k
e
r
)
 
 
 
 
 
*
/
 
 
 
 
I
D
_
W
O
R
K
E
R
(
3
)
,
 
 
 
 
/
*
*
 
 
 
 
 
*
 
全
局
唯
一
I
D
 
(
U
U
I
D
)
 
 
 
 
 
*
/
 
 
 
 
U
U
I
D
(
4
)
,
 
 
 
 
/
*
*
 
 
 
 
 
*
 
字
符
串
全
局
唯
一
I
D
 
(
i
d
W
o
r
k
e
r
 
的
字
符
串
表
示
)
 
 
 
 
 
*
/
 
 
 
 
I
D
_
W
O
R
K
E
R
_
S
T
R
(
5
)
;
 
 
 
 
 
p
r
i
v
a
t
e
 
f
i
n
a
l
 
i
n
t
 
k
e
y
;
 
 
 
 
 
I
d
T
y
p
e
(
i
n
t
 
k
e
y
)
 
{
 
 
 
 
 
 
 
 
t
h
i
s
.
k
e
y
 
=
 
k
e
y
;
 
 
 
 
}
}
 
 
 
 
 
@
T
a
b
l
e
I
d
(
v
a
l
u
e
 
=
 
"
I
D
"
,
 
t
y
p
e
 
=
 
I
d
T
y
p
e
.
A
U
T
O
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
或
:
 
 
 
 
@
T
a
b
l
e
I
d
(
v
a
l
u
e
 
=
 
"
I
D
"
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
T
a
b
l
e
I
d
(
v
a
l
u
e
 
=
 
"
I
D
"
,
t
y
p
e
 
=
 
I
d
T
y
p
e
.
I
N
P
U
T
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 16 -->
3
 
U
U
I
D
：
生
成
全
局
唯
一
I
D
。
1
）
m
y
s
q
l
数
据
库
主
键
为
字
符
串
类
型
，
不
是
自
增
类
型
。
2
）
修
改
U
s
e
r
对
象
。
 
3
）
程
序
中
不
用
设
置
主
键
 
4
 
I
D
_
W
O
R
K
E
R
_
S
T
R
：
采
用
雪
花
片
算
法
（
雪
花
算
法
生
成
的
I
D
是
纯
数
字
且
具
有
时
间
顺
序
，
适
合
分
布
式
场
景
）
生
成
全
局
唯
一
I
D
，
字
符
串
类
型
。
 
1
）
m
y
s
q
l
数
据
库
主
键
为
字
符
串
类
型
，
不
是
自
增
类
型
。
2
）
修
改
U
s
e
r
对
象
。
 
3
）
程
序
中
不
用
设
置
主
键
 
5
 
I
D
_
W
O
R
K
E
R
：
采
用
雪
花
片
算
法
生
成
全
局
唯
一
I
D
，
数
值
类
型
。
1
）
m
y
s
q
l
数
据
库
主
键
为
数
值
类
型
，
不
是
自
增
类
型
。
2
）
修
改
U
s
e
r
对
象
。
 
3
）
程
序
中
不
用
设
置
主
键
 
4
.
2
 
更
新
操
作
 
4
.
2
.
1
 
根
据
i
d
更
新
 
方
法
定
义
：
@
T
a
b
l
e
I
d
(
v
a
l
u
e
 
=
 
"
I
D
"
,
t
y
p
e
 
=
 
I
d
T
y
p
e
.
U
U
I
D
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
 
i
d
;
@
T
a
b
l
e
I
d
(
v
a
l
u
e
 
=
 
"
I
D
"
,
t
y
p
e
 
=
 
I
d
T
y
p
e
.
I
D
_
W
O
R
K
E
R
_
S
T
R
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
 
i
d
;
@
T
a
b
l
e
I
d
(
v
a
l
u
e
 
=
 
"
I
D
"
,
t
y
p
e
 
=
 
I
d
T
y
p
e
.
I
D
_
W
O
R
K
E
R
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 17 -->
根
据
i
d
更
新
操
作
步
骤
：
1
 
首
先
需
要
设
置
对
象
的
主
键
属
性
值
。
2
 
再
设
置
要
更
新
的
属
性
值
。
3
 
根
据
主
键
找
到
对
象
，
更
新
设
置
属
性
值
。
4
 
返
回
影
响
的
记
录
数
。
注
意
：
只
能
将
对
象
中
不
为
N
U
L
L
的
属
性
更
新
到
表
中
。
测
试
：
 
结
果
：
 
4
.
2
.
2
 
根
据
条
件
更
新
 
方
法
定
义
：
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
 
I
D
 
修
改
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
e
n
t
i
t
y
 
实
体
对
象
 
 
 
 
 
*
/
 
 
 
 
i
n
t
 
u
p
d
a
t
e
B
y
I
d
(
@
P
a
r
a
m
(
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
E
N
T
I
T
Y
)
 
T
 
e
n
t
i
t
y
)
;
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
U
p
d
a
t
e
B
y
I
d
(
)
 
{
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
n
e
w
 
U
s
e
r
(
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
I
d
(
6
L
)
;
 
/
/
主
键
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
A
g
e
(
2
1
)
;
 
/
/
更
新
的
字
段
 
 
 
 
 
 
 
 
 
/
/
根
据
i
d
更
新
，
更
新
不
为
n
u
l
l
的
字
段
 
 
 
 
 
 
 
 
t
h
i
s
.
u
s
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
B
y
I
d
(
u
s
e
r
)
;
 
 
 
 
}
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
U
P
D
A
T
E
 
t
b
_
u
s
e
r
 
S
E
T
 
a
g
e
=
?
 
W
H
E
R
E
 
i
d
=
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
1
(
I
n
t
e
g
e
r
)
,
 
6
(
L
o
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
U
p
d
a
t
e
s
:
 
1
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 18 -->
根
据
I
D
更
新
一
次
只
能
更
新
一
条
记
录
，
根
据
条
件
更
新
可
实
现
批
量
更
新
。
根
据
条
件
更
新
步
骤
：
1
 
在
对
象
中
设
置
要
更
新
的
属
性
值
。
2
 
设
置
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
，
设
置
更
新
条
件
，
可
以
设
置
多
个
。
3
 
返
回
影
响
的
记
录
数
。
注
意
：
只
能
将
对
象
中
不
为
N
U
L
L
的
属
性
更
新
到
表
中
。
测
试
用
例
：
下
次
将
n
a
m
e
等
于
“
曹
操
”
的
记
录
全
部
更
新
。
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
 
w
h
e
r
e
E
n
t
i
t
y
 
条
件
，
更
新
记
录
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
e
n
t
i
t
y
 
 
 
 
 
 
 
 
实
体
对
象
 
(
s
e
t
 
条
件
值
,
可
以
为
 
n
u
l
l
)
 
 
 
 
 
*
 
@
p
a
r
a
m
 
u
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
 
实
体
对
象
封
装
操
作
类
（
可
以
为
 
n
u
l
l
,
里
面
的
 
e
n
t
i
t
y
 
用
于
生
成
 
w
h
e
r
e
 
语
句
）
 
 
 
 
 
*
/
 
 
 
 
i
n
t
 
u
p
d
a
t
e
(
@
P
a
r
a
m
(
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
E
N
T
I
T
Y
)
 
T
 
e
n
t
i
t
y
,
 
@
P
a
r
a
m
(
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
R
A
P
P
E
R
)
 
W
r
a
p
p
e
r
<
T
>
 
u
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
)
;
 
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
W
r
a
p
p
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
u
p
d
a
t
e
.
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
;
i
m
p
o
r
t
 
n
e
t
.
m
i
n
i
d
e
v
.
j
s
o
n
.
w
r
i
t
e
r
.
U
p
d
a
t
e
r
M
a
p
p
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
U
p
d
a
t
e
(
)
 
{
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
n
e
w
 
U
s
e
r
(
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
A
g
e
(
2
2
)
;
 
/
/
更
新
的
字
段
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 19 -->
上
边
根
据
i
d
更
新
 
根
据
条
件
更
新
的
方
法
只
能
将
对
象
中
不
为
N
U
L
L
的
属
性
更
新
到
表
中
，
下
边
通
过
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
进
行
更
新
，
将
b
i
r
t
h
d
a
y
字
段
更
新
为
N
U
L
L
.
 
 
 
4
.
3
 
删
除
操
作
 
4
.
3
.
1
 
d
e
l
e
t
e
B
y
I
d
 
方
法
定
义
：
 
操
作
步
骤
：
1
 
指
定
要
删
除
记
录
的
主
键
值
。
2
 
调
用
d
e
l
e
t
e
B
y
I
d
方
法
执
行
删
除
。
测
试
用
例
：
 
 
 
 
 
 
 
 
/
/
更
新
的
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
n
a
m
e
"
,
 
"
曹
操
"
)
;
 
 
 
 
 
 
 
 
/
/
可
以
设
置
多
个
条
件
.
.
.
 
 
 
 
 
 
 
 
 
/
/
执
行
更
新
操
作
 
 
 
 
 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
t
h
i
s
.
u
s
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
u
s
e
r
,
 
w
r
a
p
p
e
r
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
"
r
e
s
u
l
t
 
=
 
"
 
+
 
r
e
s
u
l
t
)
;
 
 
 
 
}
 
}
 
 
 
 
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
U
p
d
a
t
e
2
(
)
 
{
 
 
 
 
 
 
 
 
/
/
更
新
的
条
件
以
及
字
段
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
>
(
)
;
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
i
d
"
,
 
6
)
.
s
e
t
(
"
a
g
e
"
,
 
2
3
)
.
s
e
t
(
"
b
i
r
t
h
d
a
y
"
,
n
u
l
l
)
;
 
 
 
 
 
 
 
 
 
/
/
执
行
更
新
操
作
 
 
 
 
 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
t
h
i
s
.
u
s
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
 
w
r
a
p
p
e
r
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
"
r
e
s
u
l
t
 
=
 
"
 
+
 
r
e
s
u
l
t
)
;
 
 
 
 
}
/
*
*
 
*
 
根
据
 
I
D
 
删
除
 
*
 
*
 
@
p
a
r
a
m
 
i
d
 
主
键
I
D
 
*
/
i
n
t
 
d
e
l
e
t
e
B
y
I
d
(
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
 
i
d
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 20 -->
结
果
：
 
4
.
3
.
2
 
d
e
l
e
t
e
 
方
法
定
义
：
 
根
据
条
件
删
除
步
骤
：
1
 
定
义
对
象
，
设
置
属
性
值
，
指
定
删
除
条
件
 
，
可
指
定
多
个
删
除
条
件
注
意
：
删
除
条
件
只
匹
配
对
象
中
不
为
N
U
L
L
的
属
性
值
2
 
设
置
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
3
 
执
行
删
除
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
D
e
l
e
t
e
B
y
I
d
(
)
 
{
 
 
 
 
 
 
 
 
/
/
执
行
删
除
操
作
 
 
 
 
 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
t
h
i
s
.
u
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
y
I
d
(
6
L
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
"
r
e
s
u
l
t
 
=
 
"
 
+
 
r
e
s
u
l
t
)
;
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
D
E
L
E
T
E
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
i
d
=
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
6
(
L
o
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
U
p
d
a
t
e
s
:
 
1
/
*
*
 
*
 
根
据
 
e
n
t
i
t
y
 
条
件
，
删
除
记
录
 
*
 
*
 
@
p
a
r
a
m
 
w
r
a
p
p
e
r
 
实
体
对
象
封
装
操
作
类
（
可
以
为
 
n
u
l
l
）
 
*
/
i
n
t
 
d
e
l
e
t
e
(
@
P
a
r
a
m
(
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
R
A
P
P
E
R
)
 
W
r
a
p
p
e
r
<
T
>
 
w
r
a
p
p
e
r
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 21 -->
测
试
用
例
：
 
结
果
：
 
注
意
：
定
义
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
可
以
不
包
装
模
型
对
象
，
手
动
设
置
条
件
，
如
下
：
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
H
a
s
h
M
a
p
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
.
u
t
i
l
.
M
a
p
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
D
e
l
e
t
e
B
y
M
a
p
(
)
 
{
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
n
e
w
 
U
s
e
r
(
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
A
g
e
(
2
0
)
;
 
 
 
 
 
 
 
 
u
s
e
r
.
s
e
t
N
a
m
e
(
"
张
三
"
)
;
 
 
 
 
 
 
 
 
 
/
/
将
实
体
对
象
进
行
包
装
，
包
装
为
操
作
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
u
s
e
r
)
;
 
 
 
 
 
 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
t
h
i
s
.
u
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
(
w
r
a
p
p
e
r
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
"
r
e
s
u
l
t
 
=
 
"
 
+
 
r
e
s
u
l
t
)
;
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
D
E
L
E
T
E
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
n
a
m
e
=
?
 
A
N
D
 
a
g
e
=
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
张
三
(
S
t
r
i
n
g
)
,
 
2
0
(
I
n
t
e
g
e
r
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
U
p
d
a
t
e
s
:
 
0
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 22 -->
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
w
r
a
p
p
e
r
.
e
q
(
"
a
g
e
"
,
2
0
)
;
 
w
r
a
p
p
e
r
.
e
q
(
"
n
a
m
e
"
,
"
张
三
"
)
;
 
4
.
3
.
3
 
d
e
l
e
t
e
B
a
t
c
h
I
d
s
 
方
法
定
义
：
 
批
量
删
除
操
作
步
骤
：
1
 
指
定
 
i
d
列
表
2
 
执
行
删
除
测
试
用
例
：
 
结
果
：
 
 
 
 
/
*
*
 
 
 
 
 
*
 
删
除
（
根
据
I
D
 
批
量
删
除
）
 
 
 
 
 
*
 
 
 
 
 
*
 
@
p
a
r
a
m
 
i
d
L
i
s
t
 
主
键
I
D
列
表
(
不
能
为
 
n
u
l
l
 
以
及
 
e
m
p
t
y
)
 
 
 
 
 
*
/
 
 
 
 
i
n
t
 
d
e
l
e
t
e
B
a
t
c
h
I
d
s
(
@
P
a
r
a
m
(
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
C
O
L
L
E
C
T
I
O
N
)
 
C
o
l
l
e
c
t
i
o
n
<
?
 
e
x
t
e
n
d
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
>
 
i
d
L
i
s
t
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
A
r
r
a
y
s
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
D
e
l
e
t
e
B
y
M
a
p
(
)
 
{
 
 
 
 
 
 
 
 
/
/
根
据
i
d
集
合
批
量
删
除
 
 
 
 
 
 
 
 
i
n
t
 
r
e
s
u
l
t
 
=
 
t
h
i
s
.
u
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
a
t
c
h
I
d
s
(
A
r
r
a
y
s
.
a
s
L
i
s
t
(
1
L
,
1
0
L
,
2
0
L
)
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
"
r
e
s
u
l
t
 
=
 
"
 
+
 
r
e
s
u
l
t
)
;
 
 
 
 
}
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 23 -->
4
.
4
 
查
询
操
作
 
M
P
提
供
了
多
种
查
询
操
作
，
包
括
根
据
i
d
查
询
 
批
量
查
询
 
查
询
单
条
数
据
 
查
询
列
表
 
分
页
查
询
等
操
作
。
4
.
4
.
1
 
s
e
l
e
c
t
B
y
I
d
 
方
法
定
义
：
 
根
据
i
d
查
询
步
骤
：
1
 
设
置
查
询
记
录
的
主
键
值
。
2
 
执
行
查
询
。
3
 
查
询
结
果
返
回
一
个
对
象
。
 
测
试
用
例
：
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
a
t
c
h
I
d
s
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
D
E
L
E
T
E
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
i
d
 
I
N
 
(
 
?
 
,
 
?
 
,
 
?
 
)
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
a
t
c
h
I
d
s
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
1
(
L
o
n
g
)
,
 
1
0
(
L
o
n
g
)
,
 
2
0
(
L
o
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
.
d
e
l
e
t
e
B
a
t
c
h
I
d
s
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
U
p
d
a
t
e
s
:
 
1
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
 
I
D
 
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
 
i
d
 
主
键
I
D
 
 
 
 
 
*
/
 
 
 
 
T
 
s
e
l
e
c
t
B
y
I
d
(
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
 
i
d
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
e
l
e
c
t
B
y
I
d
(
)
 
{
 
 
 
 
 
 
 
 
/
/
根
据
i
d
查
询
数
据
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 24 -->
结
果
：
 
4
.
4
.
2
 
s
e
l
e
c
t
B
a
t
c
h
I
d
s
 
方
法
定
义
：
 
根
据
i
d
列
表
查
询
：
1
 
设
置
i
d
列
表
2
 
执
行
查
询
3
 
查
询
对
象
返
回
L
i
s
t
测
试
用
例
：
 
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
t
h
i
s
.
u
s
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
B
y
I
d
(
2
L
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
"
r
e
s
u
l
t
 
=
 
"
 
+
 
u
s
e
r
)
;
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
i
d
=
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
(
L
o
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
y
I
d
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
1
 
r
e
s
u
l
t
 
=
 
U
s
e
r
(
i
d
=
2
,
 
u
s
e
r
N
a
m
e
=
l
i
s
i
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
李
四
,
 
a
g
e
=
2
0
,
 
e
m
a
i
l
=
t
e
s
t
2
@
i
t
c
a
s
t
.
c
n
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
/
*
*
 
*
 
查
询
（
根
据
I
D
 
批
量
查
询
）
 
*
 
*
 
@
p
a
r
a
m
 
i
d
L
i
s
t
 
主
键
I
D
列
表
(
不
能
为
 
n
u
l
l
 
以
及
 
e
m
p
t
y
)
 
*
/
L
i
s
t
<
T
>
 
s
e
l
e
c
t
B
a
t
c
h
I
d
s
(
@
P
a
r
a
m
(
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
C
O
L
L
E
C
T
I
O
N
)
 
C
o
l
l
e
c
t
i
o
n
<
?
 
e
x
t
e
n
d
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
>
 
i
d
L
i
s
t
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
A
r
r
a
y
s
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
T
e
s
t
 
{
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 25 -->
结
果
：
 
4
.
4
.
3
 
s
e
l
e
c
t
O
n
e
 
方
法
定
义
：
 
查
询
步
骤
：
1
 
设
置
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
对
象
，
设
置
查
询
条
件
，
可
以
设
置
多
个
条
件
2
 
执
行
查
询
注
意
：
如
果
查
询
结
果
为
多
条
记
录
则
报
错
（
T
o
o
M
a
n
y
R
e
s
u
l
t
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
）
。
 
测
试
用
例
：
 
 
 
 
 
 
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
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
e
l
e
c
t
B
a
t
c
h
I
d
s
(
)
 
{
 
 
 
 
 
 
 
 
/
/
根
据
i
d
集
合
批
量
查
询
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
B
a
t
c
h
I
d
s
(
A
r
r
a
y
s
.
a
s
L
i
s
t
(
2
L
,
 
3
L
,
 
1
0
L
)
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
a
t
c
h
I
d
s
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
i
d
 
I
N
 
(
 
?
 
,
 
?
 
,
 
?
 
)
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
a
t
c
h
I
d
s
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
(
L
o
n
g
)
,
 
3
(
L
o
n
g
)
,
 
1
0
(
L
o
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
B
a
t
c
h
I
d
s
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
2
 
U
s
e
r
(
i
d
=
2
,
 
u
s
e
r
N
a
m
e
=
l
i
s
i
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
李
四
,
 
a
g
e
=
2
0
,
 
e
m
a
i
l
=
t
e
s
t
2
@
i
t
c
a
s
t
.
c
n
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
U
s
e
r
(
i
d
=
3
,
 
u
s
e
r
N
a
m
e
=
w
a
n
g
w
u
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
王
五
,
 
a
g
e
=
2
8
,
 
e
m
a
i
l
=
t
e
s
t
3
@
i
t
c
a
s
t
.
c
n
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
/
*
*
 
*
 
根
据
 
e
n
t
i
t
y
 
条
件
，
查
询
一
条
记
录
 
*
 
*
 
@
p
a
r
a
m
 
q
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
 
实
体
对
象
封
装
操
作
类
（
可
以
为
 
n
u
l
l
）
 
*
/
T
 
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
@
P
a
r
a
m
(
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
R
A
P
P
E
R
)
 
W
r
a
p
p
e
r
<
T
>
 
q
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
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 26 -->
结
果
：
 
4
.
4
.
4
 
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
 
方
法
定
义
：
 
测
试
用
例
：
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
e
l
e
c
t
O
n
e
(
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
U
s
e
r
>
(
)
;
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
n
a
m
e
"
,
 
"
李
四
"
)
;
 
 
 
 
 
 
 
 
 
/
/
根
据
条
件
查
询
一
条
数
据
，
如
果
结
果
超
过
一
条
会
报
错
 
 
 
 
 
 
 
 
U
s
e
r
 
u
s
e
r
 
=
 
t
h
i
s
.
u
s
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
w
r
a
p
p
e
r
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
u
s
e
r
)
;
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
n
a
m
e
 
=
 
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
李
四
(
S
t
r
i
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
1
 
U
s
e
r
(
i
d
=
2
,
 
u
s
e
r
N
a
m
e
=
l
i
s
i
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
李
四
,
 
a
g
e
=
2
0
,
 
e
m
a
i
l
=
t
e
s
t
2
@
i
t
c
a
s
t
.
c
n
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
/
*
*
 
*
 
根
据
 
W
r
a
p
p
e
r
 
条
件
，
查
询
总
记
录
数
 
*
 
*
 
@
p
a
r
a
m
 
q
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
 
实
体
对
象
封
装
操
作
类
（
可
以
为
 
n
u
l
l
）
 
*
/
I
n
t
e
g
e
r
 
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
@
P
a
r
a
m
(
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
R
A
P
P
E
R
)
 
W
r
a
p
p
e
r
<
T
>
 
q
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
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 27 -->
结
果
：
 
4
.
4
.
5
 
s
e
l
e
c
t
L
i
s
t
 
方
法
定
义
：
 
测
试
用
例
：
 
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
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
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
U
s
e
r
>
(
)
;
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
g
t
(
"
a
g
e
"
,
 
2
3
)
;
 
/
/
年
龄
大
于
2
3
岁
 
 
 
 
 
 
 
 
 
/
/
根
据
条
件
查
询
数
据
条
数
 
 
 
 
 
 
 
 
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
 
t
h
i
s
.
u
s
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
C
o
u
n
t
(
w
r
a
p
p
e
r
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
"
c
o
u
n
t
 
=
 
"
 
+
 
c
o
u
n
t
)
;
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
C
o
u
n
t
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
C
O
U
N
T
(
 
1
 
)
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
a
g
e
 
>
 
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
C
o
u
n
t
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
3
(
I
n
t
e
g
e
r
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
C
o
u
n
t
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
1
 
c
o
u
n
t
 
=
 
2
/
*
*
 
*
 
根
据
 
e
n
t
i
t
y
 
条
件
，
查
询
全
部
记
录
 
*
 
*
 
@
p
a
r
a
m
 
q
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
 
实
体
对
象
封
装
操
作
类
（
可
以
为
 
n
u
l
l
）
 
*
/
L
i
s
t
<
T
>
 
s
e
l
e
c
t
L
i
s
t
(
@
P
a
r
a
m
(
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
R
A
P
P
E
R
)
 
W
r
a
p
p
e
r
<
T
>
 
q
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
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 28 -->
结
果
：
 
4
.
4
.
6
 
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
 
方
法
定
义
：
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
e
l
e
c
t
L
i
s
t
(
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
U
s
e
r
>
(
)
;
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
g
t
(
"
a
g
e
"
,
 
2
3
)
;
 
/
/
年
龄
大
于
2
3
岁
 
 
 
 
 
 
 
 
 
/
/
根
据
条
件
查
询
数
据
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
 
=
 
"
 
+
 
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
L
i
s
t
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
a
g
e
 
>
 
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
L
i
s
t
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
3
(
I
n
t
e
g
e
r
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
L
i
s
t
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
2
 
u
s
e
r
 
=
 
U
s
e
r
(
i
d
=
3
,
 
u
s
e
r
N
a
m
e
=
w
a
n
g
w
u
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
王
五
,
 
a
g
e
=
2
8
,
 
e
m
a
i
l
=
t
e
s
t
3
@
i
t
c
a
s
t
.
c
n
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
u
s
e
r
 
=
 
U
s
e
r
(
i
d
=
5
,
 
u
s
e
r
N
a
m
e
=
s
u
n
q
i
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
孙
七
,
 
a
g
e
=
2
4
,
 
e
m
a
i
l
=
t
e
s
t
5
@
i
t
c
a
s
t
.
c
n
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 29 -->
配
置
分
页
插
件
：
 
测
试
用
例
：
 
/
*
*
 
*
 
根
据
 
e
n
t
i
t
y
 
条
件
，
查
询
全
部
记
录
（
并
翻
页
）
 
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
g
e
 
 
 
 
 
 
 
 
 
分
页
查
询
条
件
（
可
以
为
 
R
o
w
B
o
u
n
d
s
.
D
E
F
A
U
L
T
）
 
*
 
@
p
a
r
a
m
 
q
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
 
实
体
对
象
封
装
操
作
类
（
可
以
为
 
n
u
l
l
）
 
*
/
I
P
a
g
e
<
T
>
 
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
I
P
a
g
e
<
T
>
 
p
a
g
e
,
 
@
P
a
r
a
m
(
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
R
A
P
P
E
R
)
 
W
r
a
p
p
e
r
<
T
>
 
q
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
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
e
x
t
e
n
s
i
o
n
.
p
l
u
g
i
n
s
.
P
a
g
i
n
a
t
i
o
n
I
n
t
e
r
c
e
p
t
o
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
m
y
b
a
t
i
s
.
s
p
r
i
n
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
M
a
p
p
e
r
S
c
a
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
c
o
n
t
e
x
t
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
B
e
a
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
c
o
n
t
e
x
t
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
;
 
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
@
M
a
p
p
e
r
S
c
a
n
(
"
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
"
)
 
/
/
设
置
m
a
p
p
e
r
接
口
的
扫
描
包
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
 
M
y
b
a
t
i
s
P
l
u
s
C
o
n
f
i
g
 
{
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
分
页
插
件
 
 
 
 
 
*
/
 
 
 
 
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
 
P
a
g
i
n
a
t
i
o
n
I
n
t
e
r
c
e
p
t
o
r
 
p
a
g
i
n
a
t
i
o
n
I
n
t
e
r
c
e
p
t
o
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
 
P
a
g
i
n
a
t
i
o
n
I
n
t
e
r
c
e
p
t
o
r
(
)
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
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
m
e
t
a
d
a
t
a
.
I
P
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
e
x
t
e
n
s
i
o
n
.
p
l
u
g
i
n
s
.
p
a
g
i
n
a
t
i
o
n
.
P
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
 
o
r
g
.
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 30 -->
结
果
：
 
 
5
 
条
件
构
造
器
 
在
M
P
中
，
W
r
a
p
p
e
r
接
口
的
实
现
类
关
系
如
下
：
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
S
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
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
U
s
e
r
>
(
)
;
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
g
t
(
"
a
g
e
"
,
 
2
0
)
;
 
/
/
年
龄
大
于
2
0
岁
 
 
 
 
 
 
 
 
 
/
/
参
数
1
：
当
前
页
码
，
小
于
1
的
按
1
算
 
 
 
 
 
 
 
 
/
/
参
数
2
：
每
页
记
录
数
 
 
 
 
 
 
 
 
P
a
g
e
<
U
s
e
r
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
1
,
1
)
;
 
 
 
 
 
 
 
 
 
/
/
根
据
条
件
查
询
数
据
 
 
 
 
 
 
 
 
I
P
a
g
e
<
U
s
e
r
>
 
i
P
a
g
e
 
=
 
t
h
i
s
.
u
s
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
 
w
r
a
p
p
e
r
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
"
数
据
总
条
数
：
"
 
+
 
i
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
"
总
页
数
：
"
 
+
 
i
P
a
g
e
.
g
e
t
P
a
g
e
s
(
)
)
;
 
/
/
取
出
分
页
记
录
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
i
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
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
 
=
 
"
 
+
 
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
 
}
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
P
a
g
e
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
C
O
U
N
T
(
1
)
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
a
g
e
 
>
 
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
P
a
g
e
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
0
(
I
n
t
e
g
e
r
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
P
a
g
e
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
 
P
r
e
p
a
r
i
n
g
:
 
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
a
g
e
 
>
 
?
 
L
I
M
I
T
 
?
,
?
 
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
P
a
g
e
]
‐
[
D
E
B
U
G
]
 
=
=
>
 
P
a
r
a
m
e
t
e
r
s
:
 
2
0
(
I
n
t
e
g
e
r
)
,
 
0
(
L
o
n
g
)
,
 
1
(
L
o
n
g
)
[
m
a
i
n
]
 
[
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
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
P
a
g
e
]
‐
[
D
E
B
U
G
]
 
<
=
=
 
 
 
 
 
 
T
o
t
a
l
:
 
1
[
m
a
i
n
]
 
[
o
r
g
.
m
y
b
a
t
i
s
.
s
p
r
i
n
g
.
S
q
l
S
e
s
s
i
o
n
U
t
i
l
s
]
‐
[
D
E
B
U
G
]
 
C
l
o
s
i
n
g
 
n
o
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
a
l
 
S
q
l
S
e
s
s
i
o
n
 
[
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
i
b
a
t
i
s
.
s
e
s
s
i
o
n
.
d
e
f
a
u
l
t
s
.
D
e
f
a
u
l
t
S
q
l
S
e
s
s
i
o
n
@
6
e
c
d
6
6
5
]
数
据
总
条
数
：
3
总
页
数
：
3
u
s
e
r
 
=
 
U
s
e
r
(
i
d
=
3
,
 
u
s
e
r
N
a
m
e
=
w
a
n
g
w
u
,
 
p
a
s
s
w
o
r
d
=
1
2
3
4
5
6
,
 
n
a
m
e
=
王
五
,
 
a
g
e
=
2
8
,
 
e
m
a
i
l
=
t
e
s
t
3
@
i
t
c
a
s
t
.
c
n
,
 
b
i
r
t
h
d
a
y
=
2
0
1
9
‐
1
0
‐
0
2
T
1
1
:
4
2
:
1
4
,
 
a
d
d
r
e
s
s
=
n
u
l
l
)
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 31 -->
在
M
P
查
询
中
，
还
可
以
使
用
l
a
m
b
d
a
方
式
查
询
，
降
低
数
据
库
列
表
写
错
的
风
险
。
5
.
1
 
基
本
比
较
操
作
 
e
q
等
于
 
=
n
e
不
等
于
 
<
>
g
t
大
于
 
>
g
e
大
于
等
于
 
>
=
l
t
小
于
 
<
l
e
小
于
等
于
 
<
=
b
e
t
w
e
e
n
B
E
T
W
E
E
N
 
值
1
 
A
N
D
 
值
2
n
o
t
B
e
t
w
e
e
n
N
O
T
 
B
E
T
W
E
E
N
 
值
1
 
A
N
D
 
值
2
i
n
字
段
 
I
N
 
(
v
a
l
u
e
.
g
e
t
(
0
)
,
 
v
a
l
u
e
.
g
e
t
(
1
)
,
 
.
.
.
)
n
o
t
I
n
字
段
 
N
O
T
 
I
N
 
(
v
0
,
 
v
1
,
 
.
.
.
)
测
试
用
例
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 32 -->
L
a
m
b
d
a
方
式
构
造
条
件
：
 
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
E
q
(
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
 
 
 
 
 
 
 
 
/
/
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
p
a
s
s
w
o
r
d
 
=
 
?
 
A
N
D
 
a
g
e
 
>
=
 
?
 
A
N
D
 
n
a
m
e
 
I
N
 
(
?
,
?
,
?
)
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
p
a
s
s
w
o
r
d
"
,
 
"
1
2
3
4
5
6
"
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
g
e
(
"
a
g
e
"
,
 
2
0
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
i
n
(
"
n
a
m
e
"
,
 
"
李
四
"
,
 
"
王
五
"
,
 
"
赵
六
"
)
;
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
}
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
=
 
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
>
(
)
;
 
 
 
 
 
 
 
 
 
/
/
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
p
a
s
s
w
o
r
d
 
=
 
?
 
A
N
D
 
a
g
e
 
>
=
 
?
 
A
N
D
 
n
a
m
e
 
I
N
 
(
?
,
?
,
?
)
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
U
s
e
r
:
:
g
e
t
P
a
s
s
w
o
r
d
,
 
"
1
2
3
4
5
6
"
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
g
e
(
U
s
e
r
:
:
g
e
t
A
g
e
,
 
2
0
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
i
n
(
U
s
e
r
:
:
g
e
t
N
a
m
e
,
 
"
李
四
"
,
 
"
王
五
"
,
 
"
赵
六
"
)
;
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 33 -->
通
常
在
开
发
中
要
根
据
表
达
式
进
行
判
断
，
表
达
式
为
t
r
u
e
则
拼
接
条
件
，
如
下
：
e
q
(
b
o
o
l
e
a
n
 
c
o
n
d
i
t
i
o
n
,
 
R
 
c
o
l
u
m
n
,
 
O
b
j
e
c
t
 
v
a
l
)
 
i
n
(
b
o
o
l
e
a
n
 
c
o
n
d
i
t
i
o
n
,
 
R
 
c
o
l
u
m
n
,
 
O
b
j
e
c
t
.
.
.
 
v
a
l
u
e
s
)
 
 
.
.
.
 
一
个
例
子
：
/
/
比
如
根
据
n
a
m
e
来
判
断
，
如
果
n
a
m
e
不
为
空
则
拼
接
条
件
 
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
 
n
u
l
l
;
 
w
r
a
p
p
e
r
.
e
q
(
U
s
e
r
:
:
g
e
t
P
a
s
s
w
o
r
d
,
 
"
1
2
3
4
5
6
"
)
 
 
 
 
 
 
 
 
 
.
g
e
(
U
s
e
r
:
:
g
e
t
A
g
e
,
 
2
0
)
 
 
 
 
 
 
 
 
 
.
i
n
(
n
a
m
e
!
=
n
u
l
l
,
U
s
e
r
:
:
g
e
t
N
a
m
e
,
 
"
李
四
"
,
 
"
王
五
"
,
 
"
赵
六
"
)
;
 
 
5
.
2
 
模
糊
查
询
 
l
i
k
e
L
I
K
E
 
'
%
值
%
'
例
:
 
l
i
k
e
(
"
n
a
m
e
"
,
 
"
王
"
)
-
-
-
>
n
a
m
e
 
l
i
k
e
 
'
%
王
%
'
n
o
t
L
i
k
e
N
O
T
 
L
I
K
E
 
'
%
值
%
'
例
:
 
n
o
t
L
i
k
e
(
"
n
a
m
e
"
,
 
"
王
"
)
-
-
-
>
n
a
m
e
 
n
o
t
 
l
i
k
e
 
'
%
王
%
'
l
i
k
e
L
e
f
t
L
I
K
E
 
'
%
值
'
例
:
 
l
i
k
e
L
e
f
t
(
"
n
a
m
e
"
,
 
"
王
"
)
-
-
-
>
n
a
m
e
 
l
i
k
e
 
'
%
王
'
l
i
k
e
R
i
g
h
t
L
I
K
E
 
'
值
%
'
例
:
 
l
i
k
e
R
i
g
h
t
(
"
n
a
m
e
"
,
 
"
王
"
)
-
-
-
>
n
a
m
e
 
l
i
k
e
 
'
王
%
'
测
试
用
例
：
 
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 34 -->
L
a
m
b
d
a
方
式
构
造
条
件
：
 
 
5
.
3
 
逻
辑
查
询
 
o
r
拼
接
 
O
R
主
动
调
用
o
r
表
示
紧
接
着
下
一
个
方
法
不
是
用
a
n
d
连
接
!
(
不
调
用
o
r
则
默
认
为
使
用
a
n
d
连
接
)
a
n
d
A
N
D
 
嵌
套
例
:
 
a
n
d
(
i
 
-
>
 
i
.
e
q
(
"
n
a
m
e
"
,
 
"
李
白
"
)
.
n
e
(
"
s
t
a
t
u
s
"
,
 
"
活
着
"
)
)
-
-
-
>
a
n
d
 
(
n
a
m
e
 
=
 
'
李
白
'
 
a
n
d
 
s
t
a
t
u
s
 
<
>
 
'
活
着
'
)
测
试
用
例
：
 
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
W
r
a
p
p
e
r
(
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
 
 
 
 
 
 
 
 
/
/
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
n
a
m
e
 
L
I
K
E
 
?
 
 
 
 
 
 
 
 
/
/
P
a
r
a
m
e
t
e
r
s
:
 
%
五
%
(
S
t
r
i
n
g
)
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
l
i
k
e
(
"
n
a
m
e
"
,
 
"
五
"
)
;
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
}
 
}
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
=
 
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
>
(
)
;
w
r
a
p
p
e
r
.
l
i
k
e
(
U
s
e
r
:
:
g
e
t
N
a
m
e
,
 
"
五
"
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 35 -->
L
a
m
b
d
a
方
式
构
造
条
件
：
 
5
.
4
 
s
e
l
e
c
t
 
在
M
P
查
询
中
，
默
认
查
询
所
有
的
字
段
，
如
果
有
需
要
也
可
以
通
过
s
e
l
e
c
t
方
法
进
行
指
定
字
段
。
 
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
W
r
a
p
p
e
r
(
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
 
 
 
 
 
 
 
 
/
/
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
n
a
m
e
 
=
 
?
 
O
R
 
a
g
e
 
=
 
?
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
n
a
m
e
"
,
"
李
四
"
)
.
o
r
(
)
.
e
q
(
"
a
g
e
"
,
 
2
4
)
;
 
 
 
 
 
 
 
 
/
/
变
为
a
n
d
方
式
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
n
a
m
e
"
,
"
李
四
"
)
.
e
q
(
"
a
g
e
"
,
 
2
4
)
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
}
 
}
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
=
 
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
>
(
)
;
w
r
a
p
p
e
r
.
e
q
(
U
s
e
r
:
:
g
e
t
N
a
m
e
,
"
李
四
"
)
.
o
r
(
)
.
e
q
(
U
s
e
r
:
:
g
e
t
A
g
e
,
 
2
4
)
;
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 36 -->
L
a
m
b
d
a
方
式
构
造
条
件
：
 
5
.
5
 
排
序
 
o
r
d
e
r
B
y
A
s
c
升
序
排
序
参
数
：
变
长
数
组
，
设
置
多
个
字
段
名
例
:
 
o
r
d
e
r
B
y
A
s
c
(
"
i
d
"
,
 
"
n
a
m
e
"
)
-
-
-
>
o
r
d
e
r
 
b
y
 
i
d
 
A
S
C
,
n
a
m
e
 
A
S
C
o
r
d
e
r
B
y
D
e
s
c
降
序
排
序
参
数
：
变
长
数
组
，
设
置
多
个
字
段
名
例
:
 
o
r
d
e
r
B
y
D
e
s
c
(
"
i
d
"
,
 
"
n
a
m
e
"
)
-
-
-
>
o
r
d
e
r
 
b
y
 
i
d
 
D
E
S
C
,
n
a
m
e
 
D
E
S
C
o
r
d
e
r
B
y
o
r
d
e
r
B
y
(
b
o
o
l
e
a
n
 
c
o
n
d
i
t
i
o
n
,
 
b
o
o
l
e
a
n
 
i
s
A
s
c
,
 
R
.
.
.
 
c
o
l
u
m
n
s
)
 
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
W
r
a
p
p
e
r
(
)
 
{
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
 
 
 
 
 
 
 
 
/
/
S
E
L
E
C
T
 
i
d
,
n
a
m
e
,
a
g
e
 
F
R
O
M
 
t
b
_
u
s
e
r
 
W
H
E
R
E
 
n
a
m
e
 
=
 
?
 
O
R
 
a
g
e
 
=
 
?
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
e
q
(
"
n
a
m
e
"
,
 
"
李
四
"
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
o
r
(
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
e
q
(
"
a
g
e
"
,
 
2
4
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
s
e
l
e
c
t
(
"
i
d
"
,
 
"
n
a
m
e
"
,
 
"
a
g
e
"
)
;
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
}
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
=
 
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
>
(
)
;
w
r
a
p
p
e
r
.
e
q
(
U
s
e
r
:
:
g
e
t
N
a
m
e
,
 
"
李
四
"
)
 
 
 
 
 
 
 
 
.
o
r
(
)
 
 
 
 
 
 
 
 
.
e
q
(
U
s
e
r
:
:
g
e
t
A
g
e
,
 
2
4
)
 
 
 
 
 
 
 
 
.
s
e
l
e
c
t
(
U
s
e
r
:
:
g
e
t
I
d
,
 
U
s
e
r
:
:
g
e
t
N
a
m
e
,
 
U
s
e
r
:
:
g
e
t
A
g
e
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 37 -->
‐
 
自
定
义
排
序
规
则
 
 
 
 
‐
 
参
数
1
：
t
r
u
e
有
效
，
f
a
l
s
e
无
效
 
，
参
数
2
：
是
否
升
序
，
参
数
3
.
.
设
置
多
个
字
段
 
 
 
 
‐
 
例
:
 
`
o
r
d
e
r
B
y
(
t
r
u
e
,
 
t
r
u
e
,
 
"
i
d
"
,
 
"
n
a
m
e
"
)
`
‐
‐
‐
>
`
o
r
d
e
r
 
b
y
 
i
d
 
A
S
C
,
n
a
m
e
 
A
S
C
`
 
 
 
 
‐
 
也
可
以
多
个
o
r
d
e
r
B
y
拼
装
，
如
下
：
 
 
 
 
 
 
o
r
d
e
r
B
y
(
t
r
u
e
,
 
t
r
u
e
,
 
"
i
d
"
)
.
o
r
d
e
r
B
y
(
t
r
u
e
,
 
t
r
u
e
,
 
 
"
n
a
m
e
"
)
 
 
效
果
同
上
 
 
例
子
：
 
 
`
`
`
j
a
v
a
 
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
;
 
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
m
a
p
p
e
r
.
U
s
e
r
M
a
p
p
e
r
;
 
i
m
p
o
r
t
 
c
n
.
i
t
c
a
s
t
.
m
p
.
p
o
j
o
.
U
s
e
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
c
o
n
d
i
t
i
o
n
s
.
q
u
e
r
y
.
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
j
u
n
i
t
.
T
e
s
t
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
j
u
n
i
t
.
r
u
n
n
e
r
.
R
u
n
W
i
t
h
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
o
o
t
.
t
e
s
t
.
c
o
n
t
e
x
t
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
T
e
s
t
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
t
e
s
t
.
c
o
n
t
e
x
t
.
j
u
n
i
t
4
.
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
.
u
t
i
l
.
L
i
s
t
;
 
 
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
 
U
s
e
r
M
a
p
p
e
r
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
 
 
 
 
 
p
r
i
v
a
t
e
 
U
s
e
r
M
a
p
p
e
r
 
u
s
e
r
M
a
p
p
e
r
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
W
r
a
p
p
e
r
(
)
 
{
 
 
 
 
 
 
 
 
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
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
<
>
(
)
;
 
 
 
 
 
 
 
 
 
 
/
/
S
E
L
E
C
T
 
i
d
,
u
s
e
r
_
n
a
m
e
,
p
a
s
s
w
o
r
d
,
n
a
m
e
,
a
g
e
,
e
m
a
i
l
 
F
R
O
M
 
t
b
_
u
s
e
r
 
O
R
D
E
R
 
B
Y
 
a
g
e
 
D
E
S
C
 
 
 
 
 
 
 
 
 
w
r
a
p
p
e
r
.
o
r
d
e
r
B
y
D
e
s
c
(
"
a
g
e
"
)
;
 
 
 
 
 
 
 
 
 
 
L
i
s
t
<
U
s
e
r
>
 
u
s
e
r
s
 
=
 
t
h
i
s
.
u
s
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
L
i
s
t
(
w
r
a
p
p
e
r
)
;
 
 
 
 
 
 
 
 
 
f
o
r
 
(
U
s
e
r
 
u
s
e
r
 
:
 
u
s
e
r
s
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
u
s
e
r
)
;
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
}
 
 
}
 
L
a
m
b
d
a
方
式
构
造
条
件
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 38 -->
6
 
代
码
生
成
器
 
A
u
t
o
G
e
n
e
r
a
t
o
r
 
是
 
M
y
B
a
t
i
s
-
P
l
u
s
 
的
代
码
生
成
器
，
通
过
 
A
u
t
o
G
e
n
e
r
a
t
o
r
 
可
以
快
速
生
成
 
M
a
p
p
e
r
接
口
、
 
E
n
t
i
t
y
实
体
类
及
M
a
p
p
e
r
 
X
M
L
文
件
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
o
n
t
r
o
l
l
e
r
 
等
各
个
模
块
的
代
码
，
极
大
的
提
升
了
开
发
效
率
。
 
1
）
在
p
o
m
文
件
中
引
入
依
赖
 
2
）
获
取
官
方
案
例
 
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
U
s
e
r
>
 
w
r
a
p
p
e
r
 
=
 
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
>
(
)
;
w
r
a
p
p
e
r
.
o
r
d
e
r
B
y
D
e
s
c
(
U
s
e
r
:
:
g
e
t
A
g
e
)
;
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
b
a
o
m
i
d
o
u
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
m
y
b
a
t
i
s
‐
p
l
u
s
‐
g
e
n
e
r
a
t
o
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
3
.
1
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
p
a
c
k
a
g
e
 
c
n
.
i
t
c
a
s
t
.
m
p
.
g
e
n
e
r
a
t
o
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
e
x
c
e
p
t
i
o
n
s
.
M
y
b
a
t
i
s
P
l
u
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
t
o
o
l
k
i
t
.
S
t
r
i
n
g
P
o
o
l
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
c
o
r
e
.
t
o
o
l
k
i
t
.
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
g
e
n
e
r
a
t
o
r
.
A
u
t
o
G
e
n
e
r
a
t
o
r
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
g
e
n
e
r
a
t
o
r
.
I
n
j
e
c
t
i
o
n
C
o
n
f
i
g
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
g
e
n
e
r
a
t
o
r
.
c
o
n
f
i
g
.
*
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
g
e
n
e
r
a
t
o
r
.
c
o
n
f
i
g
.
p
o
.
T
a
b
l
e
I
n
f
o
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
b
a
o
m
i
d
o
u
.
m
y
b
a
t
i
s
p
l
u
s
.
g
e
n
e
r
a
t
o
r
.
c
o
n
f
i
g
.
r
u
l
e
s
.
N
a
m
i
n
g
S
t
r
a
t
e
g
y
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
.
u
t
i
l
.
A
r
r
a
y
L
i
s
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
.
u
t
i
l
.
L
i
s
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
.
u
t
i
l
.
S
c
a
n
n
e
r
;
 
/
*
*
 
*
 
<
p
>
 
*
 
代
码
生
成
器
演
示
例
子
 
*
 
<
/
p
>
 
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
 
M
p
G
e
n
e
r
a
t
o
r
 
{
 
/
/
 
T
O
D
O
 
修
改
服
务
名
以
及
数
据
表
名
 
 
 
 
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
 
S
E
R
V
I
C
E
_
N
A
M
E
 
=
 
"
c
o
n
t
e
n
t
"
;
 
 
 
 
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
[
]
 
T
A
B
L
E
_
N
A
M
E
S
 
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
[
]
{
 
 
 
 
"
t
b
_
u
s
e
r
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
t
_
u
s
e
r
"
 
 
 
 
 
 
 
 
 
 
 
 
}
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 39 -->
}
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
 
 
 
 
/
/
 
代
码
生
成
器
 
 
 
 
 
 
 
 
A
u
t
o
G
e
n
e
r
a
t
o
r
 
m
p
g
 
=
 
n
e
w
 
A
u
t
o
G
e
n
e
r
a
t
o
r
(
)
;
 
 
 
 
 
 
 
 
/
/
 
选
择
 
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
 
引
擎
，
默
认
 
V
e
l
o
c
i
t
y
 
 
 
 
 
 
 
 
m
p
g
.
s
e
t
T
e
m
p
l
a
t
e
E
n
g
i
n
e
(
n
e
w
 
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
T
e
m
p
l
a
t
e
E
n
g
i
n
e
(
)
)
;
 
 
 
 
 
 
 
 
/
/
 
全
局
配
置
 
 
 
 
 
 
 
 
G
l
o
b
a
l
C
o
n
f
i
g
 
g
c
 
=
 
n
e
w
 
G
l
o
b
a
l
C
o
n
f
i
g
(
)
;
 
 
 
 
 
 
 
 
g
c
.
s
e
t
F
i
l
e
O
v
e
r
r
i
d
e
(
t
r
u
e
)
;
/
/
是
否
覆
盖
文
件
 
 
 
 
 
 
 
 
g
c
.
s
e
t
O
u
t
p
u
t
D
i
r
(
S
y
s
t
e
m
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
u
s
e
r
.
d
i
r
"
)
 
+
 
"
/
s
r
c
/
m
a
i
n
/
j
a
v
a
"
)
;
/
/
输
出
路
径
 
 
 
 
 
 
 
 
g
c
.
s
e
t
A
u
t
h
o
r
(
"
i
t
c
a
s
t
"
)
;
/
/
作
者
名
称
 
 
 
 
 
 
 
 
g
c
.
s
e
t
O
p
e
n
(
f
a
l
s
e
)
;
/
/
生
成
后
是
否
自
动
打
开
文
件
 
 
 
 
 
 
 
 
g
c
.
s
e
t
S
w
a
g
g
e
r
2
(
f
a
l
s
e
)
;
/
/
是
否
使
用
s
w
a
g
g
e
r
2
 
 
 
 
 
 
 
 
g
c
.
s
e
t
S
e
r
v
i
c
e
N
a
m
e
(
"
%
s
S
e
r
v
i
c
e
"
)
;
/
/
生
成
的
s
e
r
v
i
c
e
接
口
名
称
 
 
 
 
 
 
 
 
g
c
.
s
e
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
N
a
m
e
(
"
%
s
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
"
)
;
 
 
 
 
 
 
 
 
g
c
.
s
e
t
B
a
s
e
R
e
s
u
l
t
M
a
p
(
t
r
u
e
)
;
/
/
m
a
p
p
e
r
.
x
m
l
中
生
成
基
础
r
e
s
u
l
t
M
a
p
 
 
 
 
 
 
 
 
g
c
.
s
e
t
B
a
s
e
C
o
l
u
m
n
L
i
s
t
(
t
r
u
e
)
;
/
/
m
a
p
p
e
r
.
x
m
l
中
生
成
基
础
c
o
l
u
m
n
L
i
s
t
 
 
 
 
 
 
 
 
 
m
p
g
.
s
e
t
G
l
o
b
a
l
C
o
n
f
i
g
(
g
c
)
;
 
 
 
 
 
 
 
 
 
/
/
 
数
据
库
配
置
 
 
 
 
 
 
 
 
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
C
o
n
f
i
g
 
d
s
c
 
=
 
n
e
w
 
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
C
o
n
f
i
g
(
)
;
 
 
 
 
 
 
 
 
d
s
c
.
s
e
t
D
b
T
y
p
e
(
D
b
T
y
p
e
.
M
Y
S
Q
L
)
;
/
/
数
据
类
型
 
 
 
 
 
 
 
 
d
s
c
.
s
e
t
U
r
l
(
"
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
2
7
.
0
.
0
.
1
:
3
3
0
6
/
a
c
c
o
u
n
t
?
u
s
e
U
n
i
c
o
d
e
=
t
r
u
e
&
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
U
T
F
‐
8
&
s
e
r
v
e
r
T
i
m
e
z
o
n
e
=
U
T
C
&
u
s
e
S
S
L
=
f
a
l
s
e
"
)
;
 
 
 
 
 
 
 
 
d
s
c
.
s
e
t
D
r
i
v
e
r
N
a
m
e
(
"
c
o
m
.
m
y
s
q
l
.
c
j
.
j
d
b
c
.
D
r
i
v
e
r
"
)
;
 
 
 
 
 
 
 
 
d
s
c
.
s
e
t
U
s
e
r
n
a
m
e
(
"
r
o
o
t
"
)
;
 
 
 
 
 
 
 
 
d
s
c
.
s
e
t
P
a
s
s
w
o
r
d
(
"
m
y
s
q
l
"
)
;
 
 
 
 
 
 
 
 
m
p
g
.
s
e
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
(
d
s
c
)
;
 
 
 
 
 
 
 
 
 
/
/
 
包
配
置
 
 
 
 
 
 
 
 
P
a
c
k
a
g
e
C
o
n
f
i
g
 
p
c
 
=
 
n
e
w
 
P
a
c
k
a
g
e
C
o
n
f
i
g
(
)
;
 
 
 
 
 
 
 
 
p
c
.
s
e
t
M
o
d
u
l
e
N
a
m
e
(
S
E
R
V
I
C
E
_
N
A
M
E
)
;
 
 
 
 
 
 
 
 
p
c
.
s
e
t
P
a
r
e
n
t
(
"
c
n
.
i
t
c
a
s
t
"
)
;
 
 
 
 
 
 
 
 
p
c
.
s
e
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
;
 
 
 
 
 
 
 
 
p
c
.
s
e
t
X
m
l
(
"
m
a
p
p
e
r
"
)
;
 
 
 
 
 
 
 
 
m
p
g
.
s
e
t
P
a
c
k
a
g
e
I
n
f
o
(
p
c
)
;
 
 
 
 
 
 
 
 
 
/
/
 
设
置
模
板
 
 
 
 
 
 
 
 
T
e
m
p
l
a
t
e
C
o
n
f
i
g
 
t
c
 
=
 
n
e
w
 
T
e
m
p
l
a
t
e
C
o
n
f
i
g
(
)
;
 
 
 
 
 
 
 
 
m
p
g
.
s
e
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
t
c
)
;
 
 
 
 
 
 
 
 
 
/
/
 
策
略
配
置
 
 
 
 
 
 
 
 
S
t
r
a
t
e
g
y
C
o
n
f
i
g
 
s
t
r
a
t
e
g
y
 
=
 
n
e
w
 
S
t
r
a
t
e
g
y
C
o
n
f
i
g
(
)
;
 
 
 
 
 
 
 
 
s
t
r
a
t
e
g
y
.
s
e
t
N
a
m
i
n
g
(
N
a
m
i
n
g
S
t
r
a
t
e
g
y
.
u
n
d
e
r
l
i
n
e
_
t
o
_
c
a
m
e
l
)
;
/
/
表
名
映
射
到
实
体
策
略
，
带
下
划
线
的
转
成
驼
峰
 
 
 
 
 
 
 
 
s
t
r
a
t
e
g
y
.
s
e
t
C
o
l
u
m
n
N
a
m
i
n
g
(
N
a
m
i
n
g
S
t
r
a
t
e
g
y
.
u
n
d
e
r
l
i
n
e
_
t
o
_
c
a
m
e
l
)
;
/
/
列
名
映
射
到
类
型
属
性
策
略
，
带
下
划
线
的
转
成
驼
峰
 
 
 
 
 
 
 
 
s
t
r
a
t
e
g
y
.
s
e
t
E
n
t
i
t
y
L
o
m
b
o
k
M
o
d
e
l
(
t
r
u
e
)
;
/
/
实
体
类
使
用
l
o
m
b
o
k
 
 
 
 
 
 
 
 
/
/
s
t
r
a
t
e
g
y
.
s
e
t
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
S
t
y
l
e
(
t
r
u
e
)
;
/
/
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
使
用
r
e
s
t
接
口
模
式
 
 
 
 
 
 
s
t
r
a
t
e
g
y
.
s
e
t
I
n
c
l
u
d
e
(
T
A
B
L
E
_
N
A
M
E
S
)
;
/
/
设
置
表
名
 
 
 
 
 
 
 
 
/
/
s
t
r
a
t
e
g
y
.
s
e
t
T
a
b
l
e
P
r
e
f
i
x
(
"
t
b
_
"
)
;
/
/
表
名
映
射
到
实
体
名
称
去
掉
前
缀
 
 
 
 
 
 
s
t
r
a
t
e
g
y
.
s
e
t
E
n
t
i
t
y
B
o
o
l
e
a
n
C
o
l
u
m
n
R
e
m
o
v
e
I
s
P
r
e
f
i
x
(
t
r
u
e
)
;
/
/
 
B
o
o
l
e
a
n
类
型
字
段
是
否
移
除
i
s
前
缀
处
理
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 40 -->
3
）
测
试
这
里
使
用
提
供
的
生
成
器
工
程
，
解
压
g
e
n
e
r
a
t
o
r
.
z
i
p
，
并
导
入
I
D
E
A
。
运
行
M
y
B
a
t
i
s
P
l
u
s
G
e
n
e
r
a
t
o
r
的
m
a
i
n
方
法
。
输
入
模
块
名
：
注
意
：
模
块
名
匹
配
表
名
前
缀
会
自
动
去
掉
，
否
则
生
成
的
模
型
类
保
留
前
缀
。
生
成
的
文
件
包
括
e
n
t
i
t
y
、
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
、
s
e
r
v
i
c
e
、
m
a
p
p
e
r
，
如
下
：
s
t
r
a
t
e
g
y
.
s
e
t
E
n
t
i
t
y
B
o
o
l
e
a
n
C
o
l
u
m
n
R
e
m
o
v
e
I
s
P
r
e
f
i
x
(
t
r
u
e
)
;
/
/
 
B
o
o
l
e
a
n
类
型
字
段
是
否
移
除
i
s
前
缀
处
理
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
m
p
g
.
s
e
t
S
t
r
a
t
e
g
y
(
s
t
r
a
t
e
g
y
)
;
 
 
 
 
 
 
 
 
 
m
p
g
.
e
x
e
c
u
t
e
(
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 41 -->
4
）
自
定
义
模
板
上
边
的
自
动
生
成
代
码
是
通
过
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
 
引
擎
生
成
代
码
，
可
以
通
过
自
定
义
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
对
生
成
代
码
进
行
个
性
化
定
义
。
在
r
e
s
o
u
r
c
e
s
下
创
建
t
e
m
p
l
a
t
e
s
目
录
，
目
录
下
放
入
要
个
性
化
定
义
模
板
即
可
。
具
体
模
板
参
考
资
料
文
件
夹
下
的
t
e
m
p
l
a
t
e
s
目
录
 
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
