# 闪聚支付-第2章-讲义-对接SaaSv1.0

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\day05 支付渠道参数配置 Redis\讲义-pdf\闪聚支付-第2章-讲义-对接SaaSv1.0【海量资源尽在 666java.com】.pdf
- 页数：34
- 抽取：pypdf 文本层



<!-- page 1 -->
闪
聚
支
付
 
第
2
章
 
讲
义
-
对
接
S
a
a
S
 
 
1
 
对
接
S
a
a
S
 
1
.
1
 
基
础
概
念
 
1
.
1
.
1
 
S
a
a
S
 
 
 
S
a
a
S
是
S
o
f
t
w
a
r
e
-
a
s
-
a
-
S
e
r
v
i
c
e
（
软
件
即
服
务
）
的
简
称
，
它
是
一
种
通
过
互
联
网
提
供
软
件
服
务
的
模
式
，
与
传
统
软
件
相
比
有
如
下
几
点
区
别
：
1
、
S
a
a
S
软
件
不
再
是
用
户
向
软
件
供
应
商
定
制
软
件
或
进
行
二
次
开
发
，
而
是
供
应
商
将
软
件
部
署
在
自
己
的
服
务
器
上
并
通
过
互
联
网
提
供
在
线
服
务
。
2
、
软
件
供
应
商
负
责
搭
建
一
切
网
络
设
备
、
软
硬
件
运
行
平
台
等
基
础
设
施
，
并
全
权
负
责
运
营
和
维
护
软
件
。
3
、
用
户
根
据
实
际
需
要
通
过
互
联
网
订
购
所
需
要
的
软
件
服
务
，
按
照
订
购
服
务
的
多
少
和
时
间
长
短
支
付
费
用
。
4
、
用
户
不
需
要
一
次
性
支
付
很
大
一
笔
软
件
定
制
费
，
只
需
支
付
一
些
租
用
费
用
就
可
以
使
用
软
件
，
风
险
非
常
低
，
当
发
现
软
件
不
满
足
需
求
或
不
适
合
公
司
管
理
模
式
可
以
停
止
续
租
。
 
 
对
于
许
多
中
小
型
企
业
来
说
，
S
a
a
S
模
式
是
采
用
先
进
技
术
的
最
好
途
径
，
它
减
少
了
企
业
购
买
、
构
建
和
维
护
基
础
设
施
和
应
用
程
序
的
成
本
，
大
大
降
低
了
软
件
费
用
。
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
云
计
算
的
三
种
模
式
：
 
 
云
计
算
的
发
展
至
今
有
十
几
年
的
历
史
，
如
今
云
计
算
得
到
了
广
泛
的
市
场
应
用
，
具
体
包
括
三
个
层
次
：
 
 
I
a
a
S
:
 
I
n
f
r
a
s
t
r
u
c
t
u
r
e
-
a
s
-
a
-
S
e
r
v
i
c
e
（
基
础
设
施
即
服
务
）
，
也
叫
H
a
r
d
w
a
r
e
-
a
s
-
a
-
S
e
r
v
i
c
e
，
将
计
算
机
硬
件
资
源
打
包
对
外
提
供
服
务
，
比
如
云
主
机
、
云
存
储
等
。
P
a
a
S
:
 
P
l
a
t
f
o
r
m
-
a
s
-
a
-
S
e
r
v
i
c
e
（
平
台
即
服
务
）
，
也
叫
中
间
件
服
务
，
比
如
：
M
y
S
Q
L
数
据
库
服
务
、
E
l
a
s
t
i
c
S
e
a
r
c
h
搜
索
服
务
等
。
 
S
a
a
S
:
 
S
o
f
t
w
a
r
e
-
a
s
-
a
-
S
e
r
v
i
c
e
（
软
件
即
服
务
）
 
，
提
供
具
体
应
用
软
件
服
务
，
比
如
：
C
R
M
系
统
，
电
商
平
台
等
。
下
图
是
一
个
云
平
台
的
架
构
图
，
每
层
列
出
了
比
较
典
型
的
服
务
内
容
：
 
1
.
1
.
2
 
多
租
户
 
 
 
当
一
个
使
用
S
a
a
S
模
式
部
署
的
软
件
同
时
有
多
个
企
业
用
户
租
用
时
，
每
一
个
企
业
都
是
独
立
的
租
用
者
，
我
们
通
常
称
他
为
：
租
户
(
t
e
n
a
n
t
)
；
同
时
有
多
个
租
用
者
，
那
就
是
多
租
户
(
m
u
l
t
i
-
t
e
n
a
n
t
)
。
多
租
户
（
M
u
l
t
i
-
t
e
n
a
n
t
)
是
S
a
a
S
最
重
要
的
核
心
概
念
和
关
键
技
术
。
什
么
是
租
户
？
 
 
一
个
“
组
织
”
在
某
软
件
平
台
上
购
买
了
部
分
软
件
服
务
(
权
限
集
合
)
，
这
个
“
组
织
”
就
是
这
个
软
件
平
台
的
“
租
户
”
。
“
组
织
”
就
是
指
人
们
为
实
现
一
定
的
目
标
，
互
相
协
作
结
合
而
成
的
集
体
或
团
体
，
如
某
企
业
、
某
学
校
、
某
机
构
、
某
商
户
、
甚
至
某
家
庭
。
什
么
是
租
户
类
型
？
 
 
闪
聚
支
付
平
台
作
为
一
个
S
a
a
S
平
台
，
提
供
多
租
户
管
理
，
具
有
相
同
业
务
的
为
同
一
类
租
户
，
比
如
：
“
商
户
”
是
一
类
租
户
，
“
X
X
超
市
”
则
是
一
个
具
体
的
商
户
（
租
户
）
。
什
么
是
用
户
？
 
 
“
用
户
”
是
“
组
织
”
(
租
户
)
内
成
员
，
是
软
件
平
台
的
实
际
使
用
者
，
使
用
者
凭
身
份
（
用
户
名
）
、
凭
证
(
密
码
)
登
入
平
台
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
“
用
户
”
可
以
在
其
所
在
“
租
户
”
内
新
建
其
它
用
户
，
并
在
“
租
户
”
购
买
的
权
限
集
合
范
围
内
对
其
它
用
户
授
权
，
称
之
为
用
户
、
权
限
“
自
管
理
”
。
整
个
软
件
平
台
被
很
多
个
租
户
共
同
使
用
，
引
入
“
多
租
户
”
的
用
户
架
构
是
为
了
让
组
织
得
到
用
户
、
权
限
“
自
管
理
”
的
支
持
，
并
与
其
它
“
租
户
”
的
数
据
隔
离
。
下
图
是
闪
聚
支
付
平
台
的
多
租
户
结
构
图
：
闪
聚
支
付
平
台
由
支
付
系
统
、
运
营
系
统
、
统
计
分
析
系
统
、
员
工
管
理
系
统
等
模
块
组
成
，
租
户
根
据
自
己
的
需
求
购
买
平
台
的
服
务
。
比
如
：
以
支
付
为
主
的
租
户
，
他
需
要
购
买
支
付
系
统
、
员
工
管
理
系
统
、
统
计
分
析
系
统
；
需
要
运
营
管
理
的
租
户
则
需
要
购
买
运
营
系
统
。
如
何
购
买
服
务
呢
？
闪
聚
支
付
平
台
将
平
台
的
系
统
功
能
集
合
作
成
一
个
一
个
的
套
餐
，
比
如
：
“
套
餐
A
”
 
包
括
支
付
系
统
、
员
工
管
理
系
统
、
统
计
分
析
系
统
，
以
支
付
为
主
的
租
户
购
买
套
餐
A
就
拥
有
了
支
付
系
统
、
员
工
管
理
系
统
、
统
计
分
析
系
统
的
使
用
权
限
。
 
 
 
1
.
2
 
对
接
S
a
a
S
步
骤
 
1
.
2
.
1
 
业
务
模
型
 
商
户
平
台
应
用
与
S
a
a
S
平
台
模
型
的
对
应
关
系
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
左
侧
为
商
户
平
台
，
右
侧
为
S
a
a
S
平
台
。
商
户
平
台
的
商
户
对
应
S
a
a
S
平
台
的
租
户
。
商
户
平
台
的
员
工
对
应
S
a
a
S
平
台
的
用
户
。
门
店
是
什
么
？
门
店
是
商
户
平
台
中
员
工
的
组
织
机
构
，
比
如
：
本
商
户
是
一
个
大
型
超
市
，
该
大
型
超
市
在
很
多
地
方
有
自
己
的
连
锁
店
，
这
个
连
锁
店
就
是
门
店
，
每
个
连
锁
店
都
有
自
己
的
员
工
。
门
店
和
S
a
a
S
平
台
有
对
应
的
模
型
吗
？
门
店
是
商
户
平
台
由
于
经
营
需
要
所
设
立
的
组
织
机
构
，
在
S
a
a
S
平
台
中
没
有
对
应
模
型
。
 
1
.
2
.
2
 
接
入
步
骤
 
一
个
商
户
注
册
相
当
于
一
个
租
户
在
S
a
a
S
平
台
注
册
，
下
图
展
示
了
商
户
注
册
时
商
户
服
务
与
S
a
a
S
的
交
互
流
程
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
商
户
注
册
，
调
用
S
a
a
S
平
台
的
新
增
租
户
与
用
户
接
口
，
每
个
步
骤
如
下
：
1
、
新
增
租
户
（
上
图
第
9
步
）
在
商
户
平
台
新
增
商
户
。
调
用
S
a
a
S
系
统
的
接
口
新
增
租
户
。
2
、
新
增
用
户
（
上
图
第
1
0
-
1
1
步
）
在
商
户
平
台
 
新
增
员
工
。
调
用
S
a
a
S
的
接
口
新
增
用
户
，
且
自
动
设
置
用
户
和
租
户
的
绑
定
关
系
，
并
将
该
用
户
设
置
为
该
租
户
的
管
理
员
。
3
、
初
始
化
租
户
权
限
（
上
图
第
1
2
步
）
商
户
注
册
成
功
为
该
租
户
设
置
默
认
权
限
。
4
、
更
新
管
理
员
的
权
限
（
上
图
第
1
3
步
）
为
第
2
步
新
增
的
账
号
分
配
管
理
员
权
限
，
管
理
员
权
限
即
是
租
户
的
权
限
。
 
商
户
平
台
 
实
际
接
入
S
a
a
S
开
发
步
骤
如
下
：
1
、
部
署
S
a
a
S
系
统
S
a
a
S
系
统
是
闪
聚
支
付
平
台
独
立
的
系
统
，
我
们
需
要
部
署
S
a
a
S
系
统
并
实
现
商
户
平
台
与
其
对
接
。
2
、
商
户
注
册
后
调
用
S
a
a
S
系
统
的
接
口
完
成
上
边
流
程
的
对
接
1
）
商
户
平
台
完
成
的
功
能
如
下
：
新
增
商
户
新
增
员
工
新
增
门
店
为
门
店
管
理
员
功
能
2
）
调
用
S
a
a
S
系
统
的
接
口
完
成
的
功
能
如
下
：
新
增
租
户
新
增
用
户
自
动
设
置
用
户
和
租
户
的
绑
定
关
系
，
并
将
该
用
户
设
置
为
该
租
户
的
管
理
员
为
该
租
户
设
置
默
认
权
限
分
配
管
理
员
权
限
1
.
3
 
部
署
S
a
a
S
系
统
 
1
.
3
.
1
 
初
始
化
数
据
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
执
行
“
资
料
”
下
的
 
“
s
h
a
n
j
u
p
a
y
_
s
a
a
s
.
s
q
l
”
 
脚
本
导
入
S
a
a
S
系
统
数
据
库
。
 
1
.
3
.
2
 
部
署
服
务
 
1
.
 
复
制
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
g
a
t
e
w
a
y
、
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
u
a
a
、
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
u
s
e
r
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
父
工
程
2
.
 
添
加
上
述
三
个
M
o
d
u
l
e
3
.
 
完
成
后
，
整
体
目
录
结
构
如
下
：
1
.
3
.
3
 
完
善
配
置
 
1
.
3
.
3
.
1
 
网
关
服
务
 
1
.
 
在
N
a
c
o
s
上
添
加
j
w
t
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
，
如
下
图
所
示
 
s
i
g
i
n
g
‐
k
e
y
:
 
s
h
a
n
j
u
1
2
3
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
2
.
 
将
授
课
资
料
中
的
g
a
t
e
w
a
y
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
添
加
到
N
a
c
o
s
上
，
G
r
o
u
p
：
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
配
置
内
容
参
考
“
资
料
”
文
件
夹
。
 
1
.
 
修
改
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
g
a
t
e
w
a
y
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
下
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
n
a
m
e
s
p
a
c
e
为
自
己
N
a
c
o
s
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
 
i
d
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
1
.
3
.
3
.
2
 
U
A
A
服
务
 
1
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
：
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
 
2
.
 
修
改
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
工
程
下
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
n
a
m
e
s
p
a
c
e
为
自
己
N
a
c
o
s
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
 
i
d
#
 
覆
盖
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
h
t
t
p
.
y
a
m
l
的
项
目
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
u
a
a
 
#
 
覆
盖
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
d
r
u
i
d
.
y
a
m
l
的
项
目
s
p
r
i
n
g
:
 
 
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
:
 
 
 
 
d
r
u
i
d
:
 
 
 
 
 
u
r
l
:
 
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
s
h
a
n
j
u
p
a
y
_
u
a
a
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
 
 
 
 
 
u
s
e
r
n
a
m
e
:
 
r
o
o
t
 
 
 
 
 
p
a
s
s
w
o
r
d
:
 
y
o
u
r
p
a
s
s
w
o
r
d
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
1
.
3
.
3
.
3
 
统
一
账
户
服
务
 
1
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
u
s
e
r
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
：
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
 
2
.
 
修
改
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
u
s
e
r
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
下
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
n
a
m
e
s
p
a
c
e
为
自
己
N
a
c
o
s
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
 
i
d
#
 
覆
盖
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
h
t
t
p
.
y
a
m
l
的
项
目
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
u
s
e
r
 
#
 
覆
盖
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
d
r
u
i
d
.
y
a
m
l
的
项
目
s
p
r
i
n
g
:
 
 
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
:
 
 
 
 
d
r
u
i
d
:
 
 
 
 
 
u
r
l
:
 
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
s
h
a
n
j
u
p
a
y
_
u
s
e
r
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
 
 
 
 
 
u
s
e
r
n
a
m
e
:
 
r
o
o
t
 
 
 
 
 
p
a
s
s
w
o
r
d
:
 
y
o
u
r
p
a
s
s
w
o
r
d
 
#
 
覆
盖
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
y
a
m
l
的
项
目
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
:
 
 
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
:
 
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
u
s
e
r
.
e
n
t
i
t
y
 
 
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
:
 
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
c
o
m
/
s
h
a
n
j
u
p
a
y
/
*
/
m
a
p
p
e
r
/
x
m
l
/
*
.
x
m
l
 
s
m
s
:
 
 
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
8
5
/
s
a
i
l
i
n
g
"
 
 
e
f
f
e
c
t
i
v
e
T
i
m
e
:
 
6
0
0
0
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
1
.
4
 
对
接
S
a
a
S
代
码
实
现
 
根
据
前
边
接
口
S
a
a
S
步
骤
 
的
分
析
，
需
要
在
商
户
平
台
 
完
成
新
增
员
工
、
新
增
门
店
、
设
置
门
店
管
理
员
等
功
能
。
1
.
4
.
1
 
商
户
服
务
新
增
门
店
接
口
 
1
.
4
.
1
.
1
 
接
口
定
义
 
在
商
户
服
务
定
义
新
增
门
店
接
口
1
、
接
口
描
述
如
下
：
1
）
商
户
注
册
的
同
时
新
增
默
认
门
店
 
2
、
接
口
定
义
如
下
：
生
成
S
t
o
r
e
D
T
O
类
。
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
接
口
类
中
定
义
如
下
接
口
：
 
 
1
.
4
.
1
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
 
商
户
下
新
增
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
/
 
 
 
 
S
t
o
r
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
S
t
o
r
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
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
编
写
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
。
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
类
中
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
方
法
。
 
1
.
4
.
2
 
商
户
服
务
新
增
员
工
接
口
 
1
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
 
在
商
户
服
务
定
义
新
增
员
工
接
口
1
、
接
口
描
述
如
下
：
1
）
接
收
商
户
填
写
的
员
工
数
据
2
）
请
求
商
户
服
务
进
行
新
增
员
工
员
工
的
账
号
和
手
机
号
需
要
保
持
唯
一
性
。
3
）
返
回
结
果
 
2
、
接
口
定
义
如
下
：
生
成
S
t
a
ﬀ
D
T
O
类
。
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
接
口
类
中
定
义
如
下
接
口
：
 
 
1
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
 
编
写
S
t
a
ﬀ
C
o
n
v
e
r
t
。
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
类
中
定
义
c
r
e
a
t
e
S
t
a
ﬀ
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
 
S
t
o
r
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
S
t
o
r
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
)
 
{
 
 
 
 
S
t
o
r
e
 
s
t
o
r
e
 
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
s
t
o
r
e
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
商
户
下
新
增
门
店
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
s
t
o
r
e
)
)
;
 
 
 
 
 
 
 
 
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
i
n
s
e
r
t
(
s
t
o
r
e
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
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
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
/
*
*
 
 
 
 
 
*
 
商
户
新
增
员
工
 
 
 
 
 
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
f
f
D
T
O
 
 
 
 
 
*
/
 
 
 
 
S
t
a
f
f
D
T
O
 
c
r
e
a
t
e
S
t
a
f
f
(
S
t
a
f
f
D
T
O
 
s
t
a
f
f
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
a
f
f
D
T
O
 
c
r
e
a
t
e
S
t
a
f
f
(
S
t
a
f
f
D
T
O
 
s
t
a
f
f
D
T
O
)
 
{
 
 
 
 
 
 
 
 
/
/
1
.
校
验
手
机
号
格
式
及
是
否
存
在
 
 
 
 
 
 
 
 
S
t
r
i
n
g
 
m
o
b
i
l
e
 
=
 
s
t
a
f
f
D
T
O
.
g
e
t
M
o
b
i
l
e
(
)
;
 
 
 
 
 
 
 
 
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
m
o
b
i
l
e
)
)
{
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
1
.
4
.
3
 
商
户
服
务
门
店
设
置
管
理
员
接
口
 
 
 
 
 
 
 
 
 
 
 
 
 
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
1
0
0
1
1
2
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
根
据
商
户
i
d
和
手
机
号
校
验
唯
一
性
 
 
 
 
 
 
 
 
i
f
(
i
s
E
x
i
s
t
S
t
a
f
f
B
y
M
o
b
i
l
e
(
m
o
b
i
l
e
,
 
s
t
a
f
f
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
1
0
0
1
1
3
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
2
.
校
验
用
户
名
是
否
为
空
 
 
 
 
 
 
 
 
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
n
a
m
e
 
=
 
s
t
a
f
f
D
T
O
.
g
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
)
;
 
 
 
 
 
 
 
 
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
u
s
e
r
n
a
m
e
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
1
0
0
1
1
0
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
根
据
商
户
i
d
和
账
号
校
验
唯
一
性
 
 
 
 
 
 
 
 
i
f
(
i
s
E
x
i
s
t
S
t
a
f
f
B
y
U
s
e
r
N
a
m
e
(
u
s
e
r
n
a
m
e
,
 
s
t
a
f
f
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
1
0
0
1
1
4
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
S
t
a
f
f
 
e
n
t
i
t
y
 
=
 
S
t
a
f
f
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
s
t
a
f
f
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
商
户
下
新
增
员
工
"
)
;
 
 
 
 
 
 
 
 
s
t
a
f
f
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
 
S
t
a
f
f
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
 
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
手
机
号
判
断
员
工
是
否
已
在
指
定
商
户
存
在
 
 
 
 
 
*
 
@
p
a
r
a
m
 
m
o
b
i
l
e
 
手
机
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
 
 
 
 
p
r
i
v
a
t
e
 
b
o
o
l
e
a
n
 
i
s
E
x
i
s
t
S
t
a
f
f
B
y
M
o
b
i
l
e
(
S
t
r
i
n
g
 
m
o
b
i
l
e
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
a
f
f
>
 
l
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
S
t
a
f
f
>
(
)
;
 
 
 
 
 
 
 
 
l
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
.
e
q
(
S
t
a
f
f
:
:
g
e
t
M
o
b
i
l
e
,
 
m
o
b
i
l
e
)
.
e
q
(
S
t
a
f
f
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
;
 
 
 
 
 
 
 
 
i
n
t
 
i
 
=
 
s
t
a
f
f
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
l
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
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
 
>
 
0
;
 
 
 
 
}
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
账
号
判
断
员
工
是
否
已
在
指
定
商
户
存
在
 
 
 
 
 
*
 
@
p
a
r
a
m
 
u
s
e
r
N
a
m
e
 
 
 
 
 
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
 
 
 
 
p
r
i
v
a
t
e
 
b
o
o
l
e
a
n
 
i
s
E
x
i
s
t
S
t
a
f
f
B
y
U
s
e
r
N
a
m
e
(
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
a
f
f
>
 
l
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
S
t
a
f
f
>
(
)
;
 
 
 
 
 
 
 
 
l
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
.
e
q
(
S
t
a
f
f
:
:
g
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
,
 
u
s
e
r
N
a
m
e
)
.
e
q
(
S
t
a
f
f
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
;
 
 
 
 
 
 
 
 
i
n
t
 
i
 
=
 
s
t
a
f
f
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
l
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
)
;
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
i
 
>
 
0
;
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
1
.
4
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
接
口
描
述
如
下
：
绑
定
门
店
和
员
工
对
应
关
系
2
、
接
口
定
义
如
下
：
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
接
口
类
中
定
义
如
下
接
口
：
 
1
.
4
.
3
.
2
 
接
口
实
现
 
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
实
现
b
i
n
d
S
t
a
ﬀ
T
o
S
t
o
r
e
。
 
1
.
4
.
4
 
商
户
服
务
商
户
注
册
接
口
修
改
 
1
.
4
.
4
.
1
 
接
口
说
明
 
S
a
a
S
系
统
的
用
户
服
务
提
供
注
册
租
户
的
接
口
，
如
下
 
：
 
接
口
参
数
：
1
、
手
机
号
2
、
账
号
3
、
密
码
/
*
*
 
 
 
 
 
*
 
为
门
店
设
置
管
理
员
 
 
 
 
 
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
 
s
t
a
f
f
I
d
 
 
 
 
 
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
 
 
 
 
v
o
i
d
 
b
i
n
d
S
t
a
f
f
T
o
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
 
s
t
a
f
f
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
 
b
i
n
d
S
t
a
f
f
T
o
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
 
s
t
a
f
f
I
d
)
 
{
 
 
 
 
S
t
o
r
e
S
t
a
f
f
 
s
t
o
r
e
S
t
a
f
f
 
=
 
n
e
w
 
S
t
o
r
e
S
t
a
f
f
(
)
;
 
 
 
 
 
 
 
 
s
t
o
r
e
S
t
a
f
f
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
 
 
 
 
 
 
 
 
s
t
o
r
e
S
t
a
f
f
.
s
e
t
S
t
a
f
f
I
d
(
s
t
a
f
f
I
d
)
;
 
 
 
 
 
 
 
 
s
t
o
r
e
S
t
a
f
f
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
s
t
o
r
e
S
t
a
f
f
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
创
建
租
户
如
果
已
存
在
租
户
则
返
回
租
户
信
息
，
否
则
新
增
租
户
、
新
增
租
户
管
理
员
，
同
时
初
始
化
权
限
 
 
 
 
 
*
 
1
.
若
管
理
员
用
户
名
已
存
在
，
禁
止
创
建
 
 
 
 
 
*
 
2
.
手
机
号
已
存
在
，
禁
止
创
建
 
 
 
 
 
*
 
3
.
创
建
根
租
户
对
应
账
号
时
，
需
要
手
机
号
，
账
号
的
用
户
名
密
码
 
 
 
 
 
*
 
@
p
a
r
a
m
 
c
r
e
a
t
e
T
e
n
a
n
t
R
e
q
u
e
s
t
 
创
建
租
户
请
求
信
息
 
 
 
 
 
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
 
 
 
 
T
e
n
a
n
t
D
T
O
 
c
r
e
a
t
e
T
e
n
a
n
t
A
n
d
A
c
c
o
u
n
t
(
C
r
e
a
t
e
T
e
n
a
n
t
R
e
q
u
e
s
t
D
T
O
 
c
r
e
a
t
e
T
e
n
a
n
t
R
e
q
u
e
s
t
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 14 -->
4
、
租
户
类
型
：
s
h
a
n
j
u
-
m
e
r
c
h
a
n
t
5
、
默
认
套
餐
：
s
h
a
n
j
u
-
m
e
r
c
h
a
n
t
6
、
租
户
名
称
，
同
账
号
名
 
1
.
4
.
4
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
S
a
a
S
的
用
户
服
务
A
P
I
依
赖
：
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
m
e
r
c
h
a
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
 
2
、
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
，
完
善
c
r
e
a
t
e
M
e
r
c
h
a
n
t
(
)
方
法
：
 
<
!
‐
‐
 
S
a
a
S
的
用
户
服
务
A
P
I
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
h
a
n
j
u
p
a
y
‐
u
s
e
r
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
@
O
v
e
r
r
i
d
e
 
 
 
 
@
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
a
l
 
 
 
 
 
 
 
 
p
u
b
l
i
c
 
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
 
c
r
e
a
t
e
M
e
r
c
h
a
n
t
(
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
 
1
.
校
验
 
 
 
 
 
 
 
 
i
f
 
(
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
1
0
0
1
0
8
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
手
机
号
非
空
校
验
 
 
 
 
 
 
 
 
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
o
b
i
l
e
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
1
0
0
1
1
2
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
校
验
手
机
号
的
合
法
性
 
 
 
 
 
 
 
 
i
f
 
(
!
P
h
o
n
e
U
t
i
l
.
i
s
M
a
t
c
h
e
s
(
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
o
b
i
l
e
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
1
0
0
1
0
9
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
联
系
人
非
空
校
验
 
 
 
 
 
 
 
 
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
U
s
e
r
n
a
m
e
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
1
0
0
1
1
0
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
密
码
非
空
校
验
 
 
 
 
 
 
 
 
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
P
a
s
s
w
o
r
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
1
0
0
1
1
1
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
/
/
校
验
商
户
手
机
号
的
唯
一
性
,
根
据
商
户
的
手
机
号
查
询
商
户
表
，
如
果
存
在
记
录
则
说
明
已
有
相
同
的
手
机
号
重
复
 
 
 
 
 
 
 
 
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
M
e
r
c
h
a
n
t
>
 
l
a
m
b
d
a
Q
r
y
W
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
M
e
r
c
h
a
n
t
>
(
)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
.
e
q
(
M
e
r
c
h
a
n
t
:
:
g
e
t
M
o
b
i
l
e
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
o
b
i
l
e
(
)
)
;
 
 
 
 
 
 
 
 
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
 
m
e
r
c
h
a
n
t
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
l
a
m
b
d
a
Q
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
 
 
 
 
 
 
 
 
i
f
(
c
o
u
n
t
>
0
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
1
0
0
1
1
3
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
/
/
2
.
添
加
租
户
 
和
账
号
 
并
绑
定
关
系
 
 
 
 
 
 
 
 
C
r
e
a
t
e
T
e
n
a
n
t
R
e
q
u
e
s
t
D
T
O
 
c
r
e
a
t
e
T
e
n
a
n
t
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
 
C
r
e
a
t
e
T
e
n
a
n
t
R
e
q
u
e
s
t
D
T
O
(
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 15 -->
c
r
e
a
t
e
T
e
n
a
n
t
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
M
o
b
i
l
e
(
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
o
b
i
l
e
(
)
)
;
 
 
 
 
 
 
 
 
/
/
表
示
该
租
户
类
型
是
商
户
 
 
 
 
 
 
 
 
c
r
e
a
t
e
T
e
n
a
n
t
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
T
e
n
a
n
t
T
y
p
e
C
o
d
e
(
"
s
h
a
n
j
u
‐
m
e
r
c
h
a
n
t
"
)
;
 
 
 
 
 
 
 
 
/
/
设
置
租
户
套
餐
为
初
始
化
套
餐
餐
 
 
 
 
 
 
 
 
c
r
e
a
t
e
T
e
n
a
n
t
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
u
n
d
l
e
C
o
d
e
(
"
s
h
a
n
j
u
‐
m
e
r
c
h
a
n
t
"
)
;
 
 
 
 
 
 
 
 
/
/
租
户
的
账
号
信
息
 
 
 
 
 
 
 
 
c
r
e
a
t
e
T
e
n
a
n
t
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
U
s
e
r
n
a
m
e
(
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
U
s
e
r
n
a
m
e
(
)
)
;
 
 
 
 
 
 
 
 
c
r
e
a
t
e
T
e
n
a
n
t
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
P
a
s
s
w
o
r
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
D
T
O
.
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
(
)
)
;
 
 
 
 
 
 
 
 
/
/
新
增
租
户
并
设
置
为
管
理
员
 
 
 
 
 
 
 
 
c
r
e
a
t
e
T
e
n
a
n
t
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
a
m
e
(
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
U
s
e
r
n
a
m
e
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
商
户
中
心
调
用
统
一
账
号
服
务
，
新
增
租
户
和
账
号
"
)
;
 
 
 
 
 
 
 
 
T
e
n
a
n
t
D
T
O
 
t
e
n
a
n
t
D
T
O
 
=
 
t
e
n
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
c
r
e
a
t
e
T
e
n
a
n
t
A
n
d
A
c
c
o
u
n
t
(
c
r
e
a
t
e
T
e
n
a
n
t
R
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
t
e
n
a
n
t
D
T
O
 
=
=
 
n
u
l
l
 
|
|
 
t
e
n
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
I
d
(
)
 
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
2
0
0
0
1
2
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
/
/
判
断
租
户
下
是
否
已
经
注
册
过
商
户
 
 
 
 
 
 
 
 
M
e
r
c
h
a
n
t
 
m
e
r
c
h
a
n
t
 
=
 
m
e
r
c
h
a
n
t
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
M
e
r
c
h
a
n
t
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
M
e
r
c
h
a
n
t
:
:
g
e
t
T
e
n
a
n
t
I
d
,
 
t
e
n
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
I
d
(
)
)
)
;
 
 
 
 
 
 
 
 
i
f
 
(
m
e
r
c
h
a
n
t
 
!
=
 
n
u
l
l
 
&
&
 
m
e
r
c
h
a
n
t
.
g
e
t
I
d
(
)
 
!
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
2
0
0
0
1
7
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
/
/
3
.
 
设
置
商
户
所
属
租
户
 
 
 
 
 
 
 
 
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
s
e
t
T
e
n
a
n
t
I
d
(
t
e
n
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
审
核
状
态
，
注
册
时
默
认
为
"
0
"
 
 
 
 
 
 
 
 
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
s
e
t
A
u
d
i
t
S
t
a
t
u
s
(
"
0
"
)
;
/
/
审
核
状
态
 
0
‐
未
申
请
,
1
‐
已
申
请
待
审
核
,
2
‐
审
核
通
过
,
3
‐
审
核
拒
绝
 
 
 
 
 
 
 
 
M
e
r
c
h
a
n
t
 
e
n
t
i
t
y
 
=
 
M
e
r
c
h
a
n
t
C
o
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
)
;
 
 
 
 
 
 
 
 
/
/
保
存
商
户
信
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
保
存
商
户
注
册
信
息
"
)
;
 
 
 
 
 
 
 
 
m
e
r
c
h
a
n
t
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
 
 
 
 
 
 
 
 
 
/
/
4
.
新
增
门
店
，
创
建
根
门
店
 
 
 
 
 
 
 
 
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
e
n
t
i
t
y
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
S
t
o
r
e
N
a
m
e
(
"
根
门
店
"
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
 
=
 
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
(
s
t
o
r
e
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
门
店
信
息
：
{
}
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
s
t
o
r
e
D
T
O
)
)
;
 
 
 
 
 
 
 
 
 
/
/
5
.
新
增
员
工
，
并
设
置
归
属
门
店
 
 
 
 
 
 
 
 
S
t
a
f
f
D
T
O
 
s
t
a
f
f
D
T
O
 
=
 
n
e
w
 
S
t
a
f
f
D
T
O
(
)
;
 
 
 
 
 
 
 
 
s
t
a
f
f
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
e
n
t
i
t
y
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
 
 
 
 
 
 
 
 
s
t
a
f
f
D
T
O
.
s
e
t
M
o
b
i
l
e
(
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
o
b
i
l
e
(
)
)
;
 
 
 
 
 
 
 
 
s
t
a
f
f
D
T
O
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
U
s
e
r
n
a
m
e
(
)
)
;
 
 
 
 
 
 
 
 
/
/
为
员
工
选
择
归
属
门
店
,
此
处
为
根
门
店
 
 
 
 
 
 
 
 
s
t
a
f
f
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
I
d
(
)
)
;
 
 
 
 
 
 
 
 
s
t
a
f
f
D
T
O
 
=
 
c
r
e
a
t
e
S
t
a
f
f
(
s
t
a
f
f
D
T
O
)
;
 
 
 
 
 
 
 
 
 
/
/
6
.
为
门
店
设
置
管
理
员
 
 
 
 
 
 
 
 
b
i
n
d
S
t
a
f
f
T
o
S
t
o
r
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
.
g
e
t
I
d
(
)
,
 
s
t
a
f
f
D
T
O
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
返
回
商
户
注
册
信
息
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 16 -->
1
.
4
.
4
.
2
 
测
试
 
使
用
P
o
s
t
m
a
n
进
行
商
户
注
册
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
7
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
e
r
c
h
a
n
t
s
/
r
e
g
i
s
t
e
r
注
册
成
功
后
观
察
s
h
a
n
j
u
p
a
y
_
u
s
e
r
数
据
库
下
的
a
c
c
o
u
n
t
、
t
e
n
a
n
t
、
t
e
n
a
n
t
_
a
c
c
o
u
n
t
表
是
否
有
新
注
册
的
账
号
、
租
户
信
息
。
 
 
2
 
用
户
认
证
 
S
a
a
S
平
台
提
供
统
一
认
证
的
服
务
，
本
章
节
学
习
S
a
a
S
平
台
的
认
证
功
能
。
2
.
1
 
基
本
概
念
 
2
.
1
.
1
 
什
么
是
认
证
 
 
 
进
入
移
动
互
联
网
时
代
，
大
家
每
天
都
在
刷
手
机
，
常
用
的
软
件
有
微
信
、
支
付
宝
、
头
条
等
，
下
边
拿
微
信
来
举
例
子
说
明
认
证
相
关
的
基
本
概
念
，
在
初
次
使
用
微
信
前
需
要
注
册
成
为
微
信
用
户
，
然
后
输
入
账
号
和
密
码
即
可
登
录
微
信
，
输
入
账
号
和
密
码
登
录
微
信
的
过
程
就
是
认
证
。
 
 
系
统
为
什
么
要
认
证
？
 
 
认
证
是
为
了
保
护
系
统
的
隐
私
数
据
与
资
源
，
用
户
的
身
份
合
法
方
可
访
问
该
系
统
的
资
源
。
 
 
认
证
 
：
用
户
认
证
就
是
判
断
一
个
用
户
的
身
份
是
否
合
法
的
过
程
，
用
户
去
访
问
系
统
资
源
时
系
统
要
求
验
证
用
户
的
身
份
信
息
，
身
份
合
法
方
可
继
续
访
问
，
不
合
法
则
拒
绝
访
问
。
常
见
的
用
户
身
份
认
证
方
式
有
：
用
户
名
密
码
登
录
，
二
维
码
登
录
，
手
机
短
信
登
录
，
指
纹
认
证
等
方
式
。
2
.
1
.
2
 
什
么
是
会
话
 
 
 
用
户
认
证
通
过
后
，
为
了
避
免
用
户
的
每
次
操
作
都
进
行
认
证
可
将
用
户
的
信
息
保
证
在
会
话
中
。
会
话
就
是
系
统
为
了
保
持
当
前
用
户
的
登
录
状
态
所
提
供
的
机
制
，
常
见
的
有
基
于
s
e
s
s
i
o
n
方
式
、
基
于
t
o
k
e
n
方
式
等
。
 
 
基
于
s
e
s
s
i
o
n
的
认
证
方
式
如
下
图
：
 
 
它
的
交
互
流
程
是
，
用
户
认
证
成
功
后
，
在
服
务
端
生
成
用
户
相
关
的
数
据
保
存
在
s
e
s
s
i
o
n
(
当
前
会
话
)
中
，
发
给
客
户
端
的
s
e
s
s
s
i
o
n
_
i
d
 
存
放
到
 
c
o
o
k
i
e
 
中
，
这
样
用
户
客
户
端
请
求
时
带
上
 
s
e
s
s
i
o
n
_
i
d
 
就
可
以
验
证
服
务
器
端
是
否
存
在
 
s
e
s
s
i
o
n
 
数
据
，
以
此
完
成
用
户
的
合
法
校
验
，
当
用
户
退
出
系
统
或
s
e
s
s
i
o
n
过
期
销
毁
时
,
客
户
端
的
s
e
s
s
i
o
n
_
i
d
也
就
无
效
了
。
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
M
e
r
c
h
a
n
t
C
o
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
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 17 -->
基
于
t
o
k
e
n
方
式
如
下
图
：
 
 
它
的
交
互
流
程
是
，
用
户
认
证
成
功
后
，
服
务
端
生
成
一
个
t
o
k
e
n
发
给
客
户
端
，
客
户
端
存
储
t
o
k
e
n
，
每
次
请
求
时
带
上
t
o
k
e
n
，
服
务
端
收
到
t
o
k
e
n
通
过
验
证
后
即
可
确
认
用
户
身
份
。
 
 
基
于
s
e
s
s
i
o
n
的
认
证
方
式
由
S
e
r
v
l
e
t
规
范
定
制
，
服
务
端
要
存
储
s
e
s
s
i
o
n
信
息
需
要
占
用
内
存
资
源
，
客
户
端
需
要
支
持
c
o
o
k
i
e
；
基
于
t
o
k
e
n
的
方
式
则
一
般
不
需
要
服
务
端
存
储
t
o
k
e
n
，
并
且
不
限
制
客
户
端
的
存
储
方
式
。
如
今
移
动
互
联
网
时
代
更
多
类
型
的
客
户
端
需
要
接
入
系
统
，
系
统
多
是
采
用
前
后
端
分
离
的
架
构
进
行
实
现
，
所
以
基
于
t
o
k
e
n
的
方
式
更
适
合
。
2
.
1
.
3
 
什
么
是
授
权
 
 
 
还
拿
微
信
来
举
例
子
，
微
信
登
录
成
功
后
用
户
即
可
使
用
微
信
的
功
能
，
比
如
，
发
红
包
、
发
朋
友
圈
、
添
加
好
友
等
，
没
有
绑
定
银
行
卡
的
用
户
是
无
法
发
送
红
包
的
，
绑
定
银
行
卡
的
用
户
才
可
以
发
红
包
，
发
红
包
功
能
、
发
朋
友
圈
功
能
都
是
微
信
的
资
源
即
功
能
资
源
，
用
户
拥
有
发
红
包
功
能
的
权
限
才
可
以
正
常
使
用
发
送
红
包
功
能
，
拥
有
发
朋
友
圈
功
能
的
权
限
才
可
以
使
用
发
朋
友
圈
功
能
，
这
个
根
据
用
户
的
权
限
来
控
制
用
户
使
用
资
源
的
过
程
就
是
授
权
。
 
 
为
什
么
要
授
权
？
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 18 -->
认
证
是
为
了
保
证
用
户
身
份
的
合
法
性
，
授
权
则
是
为
了
更
细
粒
度
的
对
隐
私
数
据
进
行
划
分
，
授
权
是
在
认
证
通
过
后
发
生
的
，
控
制
不
同
的
用
户
能
够
访
问
不
同
的
资
源
。
 
 
授
权
：
 
授
权
是
用
户
认
证
通
过
根
据
用
户
的
权
限
来
控
制
用
户
访
问
资
源
的
过
程
，
拥
有
资
源
的
访
问
权
限
则
正
常
访
问
，
没
有
权
限
则
拒
绝
访
问
。
2
.
2
.
分
布
式
系
统
认
证
方
案
 
2
.
2
.
1
 
分
布
式
认
证
需
求
 
1
、
统
一
认
证
授
权
 
 
分
布
式
系
统
的
每
个
服
务
（
系
统
）
都
会
有
认
证
、
授
权
的
需
求
，
如
果
每
个
服
务
都
实
现
一
套
认
证
授
权
逻
辑
会
非
常
冗
余
，
考
虑
分
布
式
系
统
共
享
性
的
特
点
，
需
要
由
独
立
的
认
证
服
务
来
处
理
系
统
认
证
授
权
的
请
求
；
如
下
图
，
闪
聚
支
付
平
台
包
括
：
商
户
平
台
应
用
、
运
营
平
台
应
用
、
门
户
应
用
，
每
个
应
用
都
需
要
身
份
认
证
，
闪
聚
支
付
平
台
统
一
由
U
A
A
认
证
服
务
完
成
认
证
。
1
、
前
端
请
求
U
A
A
认
证
服
务
请
求
认
证
，
认
证
通
过
获
取
 
T
o
k
e
n
2
、
前
端
携
带
T
o
k
e
n
访
问
各
各
应
用
。
 
2
、
开
放
认
证
体
系
 
 
考
虑
分
布
式
系
统
开
放
性
的
特
点
，
U
A
A
认
证
服
务
不
仅
服
务
于
平
台
自
身
，
并
且
对
第
三
方
系
统
也
要
提
供
认
证
，
平
台
应
提
供
扩
展
和
开
放
的
认
证
机
制
，
以
开
放
A
P
I
的
方
式
供
第
三
方
应
用
接
入
，
一
方
应
用
（
内
部
 
系
统
服
务
）
和
三
方
应
用
（
第
三
方
应
用
）
均
采
用
统
一
机
制
接
入
。
下
图
是
第
三
方
的
应
用
接
入
闪
聚
支
付
平
台
结
构
图
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 19 -->
1
、
第
三
方
应
用
请
求
U
A
A
认
证
服
务
请
求
认
证
，
认
证
通
过
获
取
T
o
k
e
n
。
2
、
第
三
方
应
用
携
带
T
o
k
e
n
访
问
A
P
I
代
理
（
专
门
针
对
第
三
方
应
用
接
入
开
发
的
微
服
务
）
。
3
、
A
P
I
代
理
访
问
平
台
微
服
务
向
第
三
方
应
用
返
回
业
务
数
据
。
 
2
.
2
.
2
 
分
布
式
认
证
方
案
 
2
.
2
.
2
.
1
 
选
型
分
析
 
1
、
基
于
s
e
s
s
i
o
n
的
认
证
方
式
在
分
布
式
的
环
境
下
，
基
于
s
e
s
s
i
o
n
的
认
证
会
出
现
一
个
问
题
，
每
个
应
用
服
务
都
需
要
在
s
e
s
s
i
o
n
中
存
储
用
户
身
份
信
息
，
通
过
负
载
均
衡
将
本
地
的
请
求
分
配
到
另
一
个
应
用
服
务
需
要
将
s
e
s
s
i
o
n
信
息
带
过
去
，
否
则
会
重
新
认
证
。
这
个
时
候
，
通
常
的
做
法
有
下
面
几
种
：
S
e
s
s
i
o
n
复
制
：
多
台
应
用
服
务
器
之
间
同
步
s
e
s
s
i
o
n
，
使
s
e
s
s
i
o
n
保
持
一
致
，
对
外
透
明
。
S
e
s
s
i
o
n
黏
贴
：
当
用
户
访
问
集
群
中
某
台
服
务
器
后
，
强
制
指
定
后
续
所
有
请
求
均
落
到
此
机
器
上
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 20 -->
S
e
s
s
i
o
n
集
中
存
储
：
将
S
e
s
s
i
o
n
存
入
分
布
式
缓
存
中
，
所
有
服
务
器
应
用
实
例
统
一
从
分
布
式
缓
存
中
存
取
S
e
s
s
i
o
n
。
 
 
总
体
来
讲
，
基
于
s
e
s
s
i
o
n
认
证
的
认
证
方
式
，
可
以
更
好
的
在
服
务
端
对
会
话
进
行
控
制
，
且
安
全
性
较
高
。
但
是
，
s
e
s
s
i
o
n
机
制
方
式
基
于
c
o
o
k
i
e
，
在
复
杂
多
样
的
移
动
客
户
端
上
不
能
有
效
的
使
用
，
并
且
无
法
跨
域
，
另
外
随
着
系
统
的
扩
展
需
提
高
s
e
s
s
i
o
n
的
复
制
、
黏
贴
及
存
储
的
容
错
性
。
 
2
、
基
于
t
o
k
e
n
的
认
证
方
式
 
 
基
于
t
o
k
e
n
的
认
证
方
式
，
服
务
端
不
用
存
储
认
证
数
据
，
易
维
护
扩
展
性
强
，
 
客
户
端
可
以
把
t
o
k
e
n
 
存
在
任
意
地
方
，
并
且
可
以
实
现
w
e
b
和
a
p
p
统
一
认
证
机
制
。
其
缺
点
也
很
明
显
，
t
o
k
e
n
由
于
自
包
含
信
息
，
因
此
一
般
数
据
量
较
大
，
而
且
每
次
请
求
都
需
要
传
递
，
因
此
比
较
占
带
宽
。
另
外
，
t
o
k
e
n
的
签
名
验
签
操
作
也
会
给
c
p
u
带
来
额
外
的
处
理
负
担
。
 
2
.
2
.
2
.
2
 
技
术
方
案
 
根
据
 
选
型
的
分
析
，
决
定
采
用
基
于
t
o
k
e
n
的
认
证
方
式
，
它
的
优
点
是
：
1
、
适
合
统
一
认
证
的
机
制
，
客
户
端
、
一
方
应
用
、
三
方
应
用
都
遵
循
一
致
的
认
证
机
制
。
2
、
t
o
k
e
n
认
证
方
式
对
第
三
方
应
用
接
入
更
适
合
，
因
为
它
更
开
放
，
使
用
当
前
有
流
行
的
开
放
协
议
O
a
u
t
h
2
.
0
、
J
W
T
。
3
、
一
般
情
况
服
务
端
无
需
存
储
会
话
信
息
，
减
轻
了
服
务
端
的
压
力
。
分
布
式
系
统
认
证
技
术
方
案
见
下
图
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 21 -->
流
程
描
述
：
（
1
）
接
入
方
（
需
要
使
用
平
台
资
源
的
统
称
为
接
入
方
）
采
取
O
A
u
t
h
2
.
0
方
式
请
求
统
一
认
证
服
务
(
U
A
A
)
进
行
认
证
。
（
2
）
认
证
服
务
(
U
A
A
)
调
用
统
一
账
号
服
务
去
查
询
该
用
户
信
息
及
其
权
限
信
息
。
（
第
三
方
应
用
接
入
不
需
要
该
步
骤
）
（
3
）
认
证
服
务
(
U
A
A
)
验
证
登
录
用
户
及
第
三
方
应
用
合
法
性
。
（
4
）
若
接
入
方
身
份
合
法
，
认
证
服
务
生
成
j
w
t
令
牌
返
回
给
接
入
方
，
其
中
j
w
t
中
包
含
了
权
限
信
息
。
（
5
）
接
入
方
携
带
j
w
t
令
牌
对
A
P
I
网
关
内
的
微
服
务
资
源
进
行
访
问
。
（
6
）
A
P
I
网
关
对
令
牌
解
析
、
并
验
证
接
入
方
的
权
限
是
否
能
够
访
问
本
次
请
求
的
微
服
务
。
（
7
）
如
果
接
入
方
的
权
限
没
问
题
，
A
P
I
网
关
将
T
o
k
e
n
转
发
至
微
服
务
。
（
8
）
微
服
务
收
到
请
求
，
明
文
t
o
k
e
n
中
包
含
登
录
用
户
的
身
份
和
权
限
信
息
，
后
续
微
服
务
使
用
用
户
身
份
及
权
限
信
息
。
流
程
所
涉
及
到
统
一
账
号
服
务
、
U
A
A
服
务
、
A
P
I
网
关
这
三
个
组
件
职
责
如
下
：
1
）
统
一
账
号
服
务
 
 
提
供
商
户
和
平
台
运
营
人
员
的
登
录
账
号
、
密
码
、
角
色
、
权
限
、
资
源
等
系
统
级
信
息
的
管
理
，
不
包
含
用
户
业
务
信
息
。
2
）
统
一
认
证
服
务
(
U
A
A
)
 
 
它
承
载
了
O
A
u
t
h
2
.
0
接
入
方
认
证
、
登
入
用
户
的
认
证
、
授
权
以
及
生
成
令
牌
的
职
责
，
完
成
实
际
的
用
户
认
证
、
授
权
功
能
。
3
）
A
P
I
网
关
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 22 -->
作
为
系
统
的
唯
一
入
口
，
A
P
I
网
关
为
接
入
方
提
供
定
制
的
A
P
I
集
合
，
它
可
能
还
具
有
其
它
职
责
，
如
身
份
验
证
、
监
控
、
负
载
均
衡
、
缓
存
等
。
A
P
I
网
关
方
式
的
核
心
要
点
是
，
所
有
的
接
入
方
和
消
费
端
都
通
过
统
一
的
网
关
接
入
微
服
务
，
在
网
关
层
处
理
所
有
的
非
业
务
功
能
。
 
2
.
3
 
O
A
u
t
h
2
.
0
 
2
.
3
.
1
 
O
A
u
t
h
2
.
0
介
绍
 
 
 
O
A
u
t
h
（
开
放
授
权
）
是
一
个
开
放
标
准
，
允
许
用
户
授
权
第
三
方
应
用
访
问
他
们
存
储
在
另
外
的
服
务
提
供
者
上
的
信
息
，
而
不
需
要
将
用
户
名
和
密
码
提
供
给
第
三
方
应
用
或
分
享
他
们
数
据
的
所
有
内
容
。
O
A
u
t
h
2
.
0
是
O
A
u
t
h
协
议
的
延
续
版
本
，
但
不
向
后
兼
容
O
A
u
t
h
 
1
.
0
即
完
全
废
止
了
O
A
u
t
h
1
.
0
。
很
多
大
公
司
如
G
o
o
g
l
e
，
Y
a
h
o
o
，
M
i
c
r
o
s
o
f
t
等
都
提
供
了
O
A
U
T
H
认
证
服
务
，
这
些
都
足
以
说
明
O
A
U
T
H
标
准
逐
渐
成
为
开
放
资
源
授
权
的
标
准
。
 
 
O
a
u
t
h
协
议
目
前
发
展
到
2
.
0
版
本
，
1
.
0
版
本
过
于
复
杂
，
2
.
0
版
本
已
得
到
广
泛
应
用
。
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
b
a
i
k
e
.
b
a
i
d
u
.
c
o
m
/
i
t
e
m
/
o
A
u
t
h
/
7
1
5
3
1
3
4
?
f
r
=
a
l
a
d
d
i
n
O
a
u
t
h
协
议
：
h
t
t
p
s
:
/
/
t
o
o
l
s
.
i
e
t
f
.
o
r
g
/
h
t
m
l
/
r
f
c
6
7
4
9
下
边
分
析
一
个
O
a
u
t
h
2
认
证
的
例
子
，
通
过
例
子
去
理
解
O
A
u
t
h
2
.
0
协
议
的
认
证
流
程
，
本
例
子
是
黑
马
程
序
员
网
站
使
用
微
信
认
证
的
过
程
，
这
个
过
程
的
简
要
描
述
如
下
：
用
户
借
助
微
信
认
证
登
录
黑
马
程
序
员
网
站
，
用
户
就
不
用
单
独
在
黑
马
程
序
员
注
册
用
户
，
怎
么
样
算
认
证
成
功
吗
？
黑
马
程
序
员
网
站
需
要
成
功
从
微
信
获
取
用
户
的
身
份
信
息
则
认
为
用
户
认
证
成
功
，
那
如
何
从
微
信
获
取
用
户
的
身
份
信
息
？
用
户
信
息
的
拥
有
者
是
用
户
本
人
，
微
信
需
要
经
过
用
户
的
同
意
方
可
为
黑
马
程
序
员
网
站
生
成
令
牌
，
黑
马
程
序
员
网
站
拿
此
令
牌
方
可
从
微
信
获
取
用
户
的
信
息
。
1
、
客
户
端
请
求
第
三
方
授
权
用
户
进
入
黑
马
程
序
的
登
录
页
面
，
点
击
微
信
的
图
标
以
微
信
账
号
登
录
系
统
，
用
户
是
自
己
在
微
信
里
信
息
的
资
源
拥
有
者
。
 
点
击
“
微
信
”
出
现
一
个
二
维
码
，
此
时
用
户
扫
描
二
维
码
，
开
始
给
黑
马
程
序
员
授
权
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 23 -->
2
、
资
源
拥
有
者
同
意
给
客
户
端
授
权
资
源
拥
有
者
扫
描
二
维
码
表
示
资
源
拥
有
者
同
意
给
客
户
端
授
权
，
微
信
会
对
资
源
拥
有
者
的
身
份
进
行
验
证
，
 
验
证
通
过
后
，
微
信
会
询
问
用
户
是
否
给
授
权
黑
马
程
序
员
访
问
自
己
的
微
信
数
据
，
用
户
点
击
“
确
认
登
录
”
表
示
同
意
授
权
，
微
信
认
证
服
务
器
会
颁
发
一
个
授
权
码
，
并
重
定
向
到
黑
马
程
序
员
的
网
站
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 24 -->
3
、
客
户
端
获
取
到
授
权
码
，
请
求
认
证
服
务
器
申
请
令
牌
此
过
程
用
户
看
不
到
，
客
户
端
应
用
程
序
请
求
认
证
服
务
器
，
请
求
携
带
授
权
码
。
4
、
认
证
服
务
器
向
客
户
端
响
应
令
牌
微
信
认
证
服
务
器
验
证
了
客
户
端
请
求
的
授
权
码
，
如
果
合
法
则
给
客
户
端
颁
发
令
牌
，
令
牌
是
客
户
端
访
问
资
源
的
通
行
证
。
此
交
互
过
程
用
户
看
不
到
，
当
客
户
端
拿
到
令
牌
后
，
用
户
在
黑
马
程
序
员
看
到
已
经
登
录
成
功
。
5
、
客
户
端
请
求
资
源
服
务
器
的
资
源
客
户
端
携
带
令
牌
访
问
资
源
服
务
器
的
资
源
。
黑
马
程
序
员
网
站
携
带
令
牌
请
求
访
问
微
信
服
务
器
获
取
用
户
的
基
本
信
息
。
6
、
资
源
服
务
器
返
回
受
保
护
资
源
资
源
服
务
器
校
验
令
牌
的
合
法
性
，
如
果
合
法
则
向
用
户
响
应
资
源
信
息
内
容
。
 
以
上
认
证
授
权
详
细
的
执
行
流
程
如
下
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 25 -->
通
过
上
边
的
例
子
我
们
大
概
了
解
了
O
A
a
u
t
h
2
.
0
的
认
证
过
程
，
下
边
我
们
看
O
A
u
t
h
2
.
0
认
证
流
程
：
引
自
O
A
a
u
t
h
2
.
0
协
议
r
f
c
6
7
4
9
 
h
t
t
p
s
:
/
/
t
o
o
l
s
.
i
e
t
f
.
o
r
g
/
h
t
m
l
/
r
f
c
6
7
4
9
O
A
a
u
t
h
2
.
0
包
括
以
下
角
色
：
1
、
客
户
端
本
身
不
存
储
资
源
，
需
要
通
过
资
源
拥
有
者
的
授
权
去
请
求
资
源
服
务
器
的
资
源
，
比
如
：
A
n
d
r
o
i
d
客
户
端
、
W
e
b
客
户
端
（
浏
览
器
端
）
、
微
信
客
户
端
等
。
2
、
资
源
拥
有
者
通
常
为
用
户
，
也
可
以
是
应
用
程
序
，
即
该
资
源
的
拥
有
者
。
3
、
授
权
服
务
器
（
也
称
认
证
服
务
器
）
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 26 -->
用
于
服
务
提
供
商
对
资
源
拥
有
的
身
份
进
行
认
证
、
对
访
问
资
源
进
行
授
权
，
认
证
成
功
后
会
给
客
户
端
发
放
令
牌
（
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
）
，
作
为
客
户
端
访
问
资
源
服
务
器
的
凭
据
。
本
例
为
微
信
的
认
证
服
务
器
。
4
、
资
源
服
务
器
存
储
资
源
的
服
务
器
，
本
例
子
为
微
信
存
储
的
用
户
信
息
。
现
在
还
有
一
个
问
题
，
服
务
提
供
商
能
允
许
随
便
一
个
客
户
端
就
接
入
到
它
的
授
权
服
务
器
吗
？
答
案
是
否
定
的
，
服
务
提
供
商
会
给
准
入
的
接
入
方
一
个
身
份
，
用
于
接
入
时
的
凭
据
:
c
l
i
e
n
t
_
i
d
：
客
户
端
标
识
 
c
l
i
e
n
t
_
s
e
c
r
e
t
：
客
户
端
秘
钥
因
此
，
准
确
来
说
，
授
权
服
务
器
对
两
种
O
A
u
t
h
2
.
0
中
的
两
个
角
色
进
行
认
证
授
权
，
分
别
是
资
源
拥
有
者
、
客
户
端
。
2
.
3
.
2
 
四
种
模
式
 
O
A
u
t
h
2
.
0
提
供
了
四
种
授
权
(
获
取
令
牌
)
方
式
，
四
种
方
式
均
采
用
不
同
的
执
行
流
程
，
让
我
们
适
应
不
同
的
场
景
。
2
.
3
.
2
.
1
.
授
权
码
模
式
 
授
权
码
模
式
流
程
如
下
 
：
 
 
（
1
）
资
源
拥
有
者
打
开
客
户
端
，
客
户
端
要
求
资
源
拥
有
者
给
予
授
权
，
它
将
浏
览
器
被
重
定
向
到
授
权
服
务
器
，
重
定
向
时
会
附
加
客
户
端
的
身
份
信
息
。
如
：
 
/
u
a
a
/
o
a
u
t
h
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
?
c
l
i
e
n
t
_
i
d
=
p
2
p
w
e
b
&
r
e
s
p
o
n
s
e
_
t
y
p
e
=
c
o
d
e
&
s
c
o
p
e
=
a
p
p
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
h
t
t
p
:
/
/
x
x
.
x
x
/
n
o
t
i
f
y
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 27 -->
参
数
列
表
如
下
：
c
l
i
e
n
t
_
i
d
：
客
户
端
接
入
标
识
。
r
e
s
p
o
n
s
e
_
t
y
p
e
：
授
权
码
模
式
固
定
为
c
o
d
e
。
s
c
o
p
e
：
客
户
端
权
限
。
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
：
跳
转
u
r
i
，
当
授
权
码
申
请
成
功
后
会
跳
转
到
此
地
址
，
并
在
后
边
带
上
c
o
d
e
参
数
（
授
权
码
）
。
（
2
）
浏
览
器
出
现
向
授
权
服
务
器
授
权
页
面
，
之
后
将
用
户
同
意
授
权
。
（
3
）
授
权
服
务
器
将
授
权
码
（
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
C
o
d
e
）
转
经
浏
览
器
发
送
给
c
l
i
e
n
t
(
通
过
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
)
。
（
4
）
客
户
端
拿
着
授
权
码
向
授
权
服
务
器
索
要
访
问
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
，
请
求
如
下
：
 
参
数
列
表
如
下
c
l
i
e
n
t
_
i
d
：
客
户
端
准
入
标
识
。
c
l
i
e
n
t
_
s
e
c
r
e
t
：
客
户
端
秘
钥
。
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
：
授
权
类
型
，
填
写
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
，
表
示
授
权
码
模
式
c
o
d
e
：
授
权
码
，
就
是
刚
刚
获
取
的
授
权
码
，
注
意
：
授
权
码
只
使
用
一
次
就
无
效
了
，
需
要
重
新
申
请
。
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
：
申
请
授
权
码
时
的
跳
转
u
r
l
，
一
定
和
申
请
授
权
码
时
用
的
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
一
致
。
（
4
）
授
权
服
务
器
返
回
令
牌
(
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
)
 
 
这
种
模
式
是
四
种
模
式
中
最
安
全
的
一
种
模
式
。
一
般
用
于
W
e
b
服
务
器
端
应
用
或
第
三
方
的
原
生
A
p
p
调
用
资
源
服
务
的
时
候
。
因
为
在
这
种
模
式
中
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
不
会
经
过
浏
览
器
或
移
动
端
的
A
p
p
，
而
是
直
接
从
服
务
端
去
交
换
，
这
样
就
最
大
限
度
的
减
小
了
令
牌
泄
漏
的
风
险
。
 
 
 
2
.
3
.
2
.
2
.
密
码
模
式
 
密
码
模
式
使
用
较
多
，
适
应
于
第
一
方
的
单
页
面
应
用
以
及
第
一
方
的
原
生
A
p
p
，
比
如
：
闪
聚
支
付
平
台
运
营
平
台
用
户
使
用
此
模
式
完
成
用
户
登
录
。
密
码
模
式
认
证
流
程
如
下
：
/
u
a
a
/
o
a
u
t
h
/
t
o
k
e
n
?
c
l
i
e
n
t
_
i
d
=
p
2
p
w
e
b
&
c
l
i
e
n
t
_
s
e
c
r
e
t
=
g
d
j
b
c
d
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
&
c
o
d
e
=
5
P
g
f
c
D
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
h
t
t
p
:
/
/
x
x
.
x
x
/
n
o
t
i
f
y
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 28 -->
（
1
）
资
源
拥
有
者
将
用
户
名
、
密
码
发
送
给
客
户
端
（
2
）
客
户
端
拿
着
资
源
拥
有
者
的
用
户
名
、
密
码
向
授
权
服
务
器
请
求
令
牌
（
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
）
，
请
求
如
下
：
 
参
数
列
表
如
下
：
c
l
i
e
n
t
_
i
d
：
客
户
端
准
入
标
识
。
c
l
i
e
n
t
_
s
e
c
r
e
t
：
客
户
端
秘
钥
。
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
：
授
权
类
型
，
填
写
p
a
s
s
w
o
r
d
表
示
密
码
模
式
u
s
e
r
n
a
m
e
：
资
源
拥
有
者
用
户
名
。
p
a
s
s
w
o
r
d
：
资
源
拥
有
者
密
码
。
（
3
）
授
权
服
务
器
将
令
牌
（
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
）
发
送
给
c
l
i
e
n
t
 
 
这
种
模
式
十
分
简
单
，
但
是
却
意
味
着
直
接
将
用
户
敏
感
信
息
泄
漏
给
了
c
l
i
e
n
t
，
因
此
这
就
说
明
这
种
模
式
只
能
用
于
c
l
i
e
n
t
是
我
们
自
己
开
发
的
情
况
下
。
因
此
密
码
模
式
一
般
用
于
我
们
自
己
开
发
的
，
第
一
方
原
生
A
p
p
或
第
一
方
单
页
面
应
用
。
2
.
3
.
2
.
3
.
客
户
端
模
式
 
 
（
1
）
客
户
端
向
授
权
服
务
器
发
送
自
己
的
身
份
信
息
，
并
请
求
令
牌
（
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
）
（
2
）
确
认
客
户
端
身
份
无
误
后
，
将
令
牌
（
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
）
发
送
给
c
l
i
e
n
t
，
请
求
如
下
：
 
参
数
列
表
如
下
:
/
u
a
a
/
o
a
u
t
h
/
t
o
k
e
n
?
c
l
i
e
n
t
_
i
d
=
p
2
p
w
e
b
&
c
l
i
e
n
t
_
s
e
c
r
e
t
=
f
g
s
d
g
r
f
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
p
a
s
s
w
o
r
d
&
u
s
e
r
n
a
m
e
=
s
h
a
n
g
s
a
n
&
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
/
u
a
a
/
o
a
u
t
h
/
t
o
k
e
n
?
c
l
i
e
n
t
_
i
d
=
p
2
p
w
e
b
&
c
l
i
e
n
t
_
s
e
c
r
e
t
=
f
d
a
f
d
a
g
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
c
l
i
e
n
t
_
c
r
e
d
e
n
t
i
a
l
s
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 29 -->
c
l
i
e
n
t
_
i
d
：
客
户
端
准
入
标
识
。
c
l
i
e
n
t
_
s
e
c
r
e
t
：
客
户
端
秘
钥
。
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
：
授
权
类
型
，
填
写
c
l
i
e
n
t
_
c
r
e
d
e
n
t
i
a
l
s
表
示
客
户
端
模
式
这
种
模
式
是
最
方
便
但
最
不
安
全
的
模
式
。
因
此
这
就
要
求
我
们
对
c
l
i
e
n
t
完
全
的
信
任
，
而
c
l
i
e
n
t
本
身
也
是
安
全
的
。
因
此
这
种
模
式
一
般
用
来
提
供
给
我
们
完
全
信
任
的
服
务
器
端
服
务
。
比
如
，
合
作
方
系
统
对
接
，
拉
取
一
组
用
户
信
息
。
客
户
端
模
式
适
应
于
没
有
用
户
参
与
的
，
完
全
信
任
的
一
方
或
合
作
方
服
务
器
端
程
序
接
入
。
2
.
3
.
2
.
4
.
简
化
模
式
 
（
1
）
资
源
拥
有
者
打
开
客
户
端
，
客
户
端
要
求
资
源
拥
有
者
给
予
授
权
，
它
将
浏
览
器
被
重
定
向
到
授
权
服
务
器
，
重
定
向
时
会
附
加
客
户
端
的
身
份
信
息
。
如
：
 
参
数
描
述
同
授
权
码
模
式
 
，
注
意
r
e
s
p
o
n
s
e
_
t
y
p
e
=
t
o
k
e
n
，
说
明
是
简
化
模
式
。
（
2
）
浏
览
器
出
现
向
授
权
服
务
器
授
权
页
面
，
之
后
将
用
户
同
意
授
权
。
（
3
）
授
权
服
务
器
将
授
权
码
将
令
牌
（
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
）
以
H
a
s
h
的
形
式
存
放
在
重
定
向
u
r
i
的
f
a
r
g
m
e
n
t
中
发
送
给
浏
览
器
。
注
：
f
r
a
g
m
e
n
t
 
主
要
是
用
来
标
识
 
U
R
I
 
所
标
识
资
源
里
的
某
个
资
源
，
在
 
U
R
I
 
的
末
尾
通
过
 
（
#
）
作
为
 
f
r
a
g
m
e
n
t
 
的
开
头
，
其
中
 
#
 
不
属
于
 
f
r
a
g
m
e
n
t
 
的
值
。
如
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
m
a
i
n
/
i
n
d
e
x
#
L
1
8
这
个
 
U
R
I
 
中
 
L
1
8
 
就
是
 
f
r
a
g
m
e
n
t
 
的
值
。
大
家
只
需
要
知
道
j
s
通
过
响
应
浏
览
器
地
址
栏
变
化
的
方
式
能
获
取
到
f
r
a
g
m
e
n
t
 
就
行
了
。
一
般
来
说
，
简
化
模
式
用
于
第
三
方
单
页
面
应
用
。
 
/
u
a
a
/
o
a
u
t
h
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
?
c
l
i
e
n
t
_
i
d
=
p
2
p
w
e
b
&
r
e
s
p
o
n
s
e
_
t
y
p
e
=
t
o
k
e
n
&
s
c
o
p
e
=
a
p
p
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
h
t
t
p
:
/
/
x
x
.
x
x
/
n
o
t
i
f
y
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 30 -->
2
.
4
.
统
一
认
证
测
试
 
2
.
4
.
1
.
认
证
接
口
说
明
 
2
.
4
.
1
.
1
.
登
录
 
功
能
说
明
：
 
用
户
登
录
并
返
回
令
牌
，
该
令
牌
用
于
访
问
闪
聚
支
付
平
台
内
受
保
护
资
源
。
访
问
路
径
：
[
授
权
服
务
地
址
]
/
o
a
u
t
h
/
t
o
k
e
n
请
求
参
数
：
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
：
 
授
权
类
型
，
可
以
是
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
,
i
m
p
l
i
c
i
t
,
c
l
i
e
n
t
_
c
r
e
d
e
n
t
i
a
l
s
,
p
a
s
s
w
o
r
d
c
l
i
e
n
t
_
i
d
：
接
入
客
户
端
i
d
c
l
i
e
n
t
_
s
e
c
r
e
t
：
接
入
客
户
端
密
钥
u
s
e
r
n
a
m
e
：
登
录
用
户
名
，
认
证
类
型
(
如
密
码
认
证
，
短
信
认
证
，
二
维
码
认
证
等
)
 
p
a
s
s
w
o
r
d
：
登
录
密
码
响
应
内
容
：
 
2
.
4
.
1
.
2
.
解
析
令
牌
 
功
能
说
明
：
返
回
令
牌
的
明
文
内
容
，
描
述
的
是
当
前
登
录
的
用
户
及
接
入
客
户
端
的
信
息
。
访
问
路
径
：
[
授
权
服
务
地
址
]
/
o
a
u
t
h
/
c
h
e
c
k
_
t
o
k
e
n
请
求
参
数
：
t
o
k
e
n
：
 
"
e
y
J
h
b
G
c
i
O
i
J
I
f
d
a
s
f
d
a
j
g
f
s
i
o
g
j
ﬁ
s
n
i
j
i
I
F
D
J
G
D
f
h
d
s
o
g
.
.
.
"
响
应
内
容
：
 
{
"
u
s
e
r
n
a
m
e
"
:
"
a
d
m
i
n
"
,
"
a
u
t
h
e
n
t
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
"
:
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
}
{
 
 
 
 
"
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
:
 
"
e
y
J
h
b
G
c
i
O
i
J
I
U
z
I
1
N
i
I
s
I
n
R
5
c
C
I
6
I
k
p
X
V
C
J
9
.
.
.
"
,
 
/
/
令
牌
 
 
 
 
"
t
o
k
e
n
_
t
y
p
e
"
:
 
"
b
e
a
r
e
r
"
,
 
 
 
 
"
r
e
f
r
e
s
h
_
t
o
k
e
n
"
:
 
"
e
y
J
h
b
G
c
i
O
i
J
I
U
z
I
1
N
i
I
s
I
n
R
5
c
C
I
6
I
k
p
X
V
C
J
9
.
.
.
"
,
 
/
/
刷
新
令
牌
 
 
 
 
"
e
x
p
i
r
e
s
_
i
n
"
:
 
3
1
5
3
5
9
9
9
,
 
/
/
有
效
期
 
 
 
 
"
s
c
o
p
e
"
:
 
"
r
e
a
d
"
,
 
 
 
 
"
j
t
i
"
:
 
"
d
f
c
6
f
3
0
a
‐
a
a
8
e
‐
4
0
2
8
‐
a
4
3
a
‐
1
4
8
7
e
6
4
a
2
c
f
b
"
}
{
 
 
 
 
"
a
u
d
"
:
 
[
 
 
 
 
 
 
 
 
"
s
h
a
n
j
u
‐
r
e
s
o
u
r
c
e
"
 
 
 
 
]
,
 
 
 
 
"
p
a
y
l
o
a
d
"
:
 
{
 
 
 
 
 
 
 
 
"
1
1
8
6
1
7
3
8
1
9
1
5
7
5
4
4
9
6
2
"
:
 
{
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 31 -->
2
.
4
.
2
.
接
口
测
试
 
 
 
分
别
启
动
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
g
a
t
e
w
a
y
、
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
u
s
e
r
、
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
u
a
a
三
个
工
程
，
测
试
过
程
若
有
不
清
楚
可
参
考
前
面
1
.
2
.
3
章
节
O
A
u
t
h
2
.
0
理
论
部
分
和
上
一
小
节
接
口
说
明
。
2
.
4
.
2
.
1
.
密
码
模
式
认
证
 
 
请
求
参
数
：
 
 
 
 
 
 
 
 
 
 
 
 
"
u
s
e
r
_
a
u
t
h
o
r
i
t
i
e
s
"
:
 
{
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
r
_
0
0
1
"
:
 
[
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
s
t
a
f
f
_
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
p
a
y
m
e
n
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
o
_
m
e
m
b
e
r
_
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
c
o
n
s
o
l
e
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
a
c
c
o
u
n
t
_
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
o
_
e
n
t
r
e
p
r
i
s
e
_
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
a
p
p
_
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
e
n
t
e
r
p
r
i
s
e
_
a
u
t
h
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
o
_
a
u
d
i
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
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
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
s
t
o
r
e
_
l
i
s
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
o
_
s
e
r
v
i
c
e
_
t
y
p
e
"
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
m
_
a
c
c
o
u
n
t
_
c
h
e
c
k
"
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
]
,
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
r
_
0
0
2
"
:
 
[
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
"
s
j
_
o
_
m
e
m
b
e
r
_
q
u
e
r
y
"
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
]
 
 
 
 
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
}
 
 
 
 
}
,
 
 
 
 
"
u
s
e
r
_
n
a
m
e
"
:
 
"
a
d
m
i
n
"
,
 
 
 
 
"
s
c
o
p
e
"
:
 
[
 
 
 
 
 
 
 
 
"
r
e
a
d
"
 
 
 
 
]
,
 
 
 
 
"
m
o
b
i
l
e
"
:
 
"
1
7
7
1
7
7
7
1
7
7
7
"
,
 
 
 
 
"
e
x
p
"
:
 
1
6
0
6
3
5
4
3
1
6
,
 
 
 
 
"
c
l
i
e
n
t
_
a
u
t
h
o
r
i
t
i
e
s
"
:
 
[
 
 
 
 
 
 
 
 
"
R
O
L
E
_
M
E
R
C
H
A
N
T
"
,
 
 
 
 
 
 
 
 
"
R
O
L
E
_
U
S
E
R
"
 
 
 
 
]
,
 
 
 
 
"
j
t
i
"
:
 
"
d
f
c
6
f
3
0
a
‐
a
a
8
e
‐
4
0
2
8
‐
a
4
3
a
‐
1
4
8
7
e
6
4
a
2
c
f
b
"
,
 
 
 
 
"
c
l
i
e
n
t
_
i
d
"
:
 
"
m
e
r
c
h
a
n
t
‐
p
l
a
t
f
o
r
m
"
}
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
2
0
/
u
a
a
/
o
a
u
t
h
/
t
o
k
e
n
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 32 -->
2
.
4
.
2
.
2
.
 
解
析
t
o
k
e
n
 
 
请
求
参
数
：
 
 
 
2
.
4
.
3
 
J
W
T
 
什
么
是
J
W
T
？
 
 
J
S
O
N
 
W
e
b
 
T
o
k
e
n
（
J
W
T
）
是
一
个
开
放
的
行
业
标
准
（
R
F
C
 
7
5
1
9
）
，
它
定
义
了
一
种
简
洁
的
、
自
包
含
的
协
议
格
式
，
用
于
在
通
信
双
方
传
递
j
s
o
n
对
象
，
传
递
的
信
息
经
过
数
字
签
名
可
以
被
验
证
和
信
任
。
J
W
T
可
以
使
用
H
M
A
C
算
法
或
使
用
R
S
A
的
公
钥
/
私
钥
对
来
签
名
，
防
止
被
篡
改
。
J
W
T
令
牌
的
优
点
：
 
1
、
j
w
t
基
于
j
s
o
n
，
非
常
方
便
解
析
。
 
2
、
可
以
在
令
牌
中
自
定
义
丰
富
的
内
容
，
易
扩
展
。
 
3
、
通
过
非
对
称
加
密
算
法
及
数
字
签
名
技
术
，
J
W
T
防
止
篡
改
，
安
全
性
高
。
J
W
T
令
牌
结
构
：
J
W
T
令
牌
由
H
e
a
d
e
r
、
P
a
y
l
o
a
d
、
S
i
g
n
a
t
u
r
e
三
部
分
组
成
，
每
部
分
中
间
使
用
点
（
.
）
分
隔
，
比
如
：
x
x
x
x
x
.
y
y
y
y
y
.
z
z
z
z
z
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
2
0
/
u
a
a
/
o
a
u
t
h
/
c
h
e
c
k
_
t
o
k
e
n
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 33 -->
1
）
H
e
a
d
e
r
头
部
包
括
令
牌
的
类
型
（
即
J
W
T
）
及
使
用
的
哈
希
算
法
（
如
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
或
R
S
A
）
。
一
个
例
子
：
 
将
上
边
的
内
容
使
用
B
a
s
e
6
4
U
r
l
编
码
，
得
到
一
个
字
符
串
就
是
J
W
T
令
牌
的
第
一
部
分
。
H
S
2
5
6
就
是
H
M
A
C
-
S
H
A
2
5
6
，
加
密
算
法
使
用
H
M
A
C
，
摘
要
算
法
使
用
S
H
A
2
5
6
。
测
试
：
将
生
成
的
j
w
t
令
牌
第
一
部
分
使
用
B
a
s
e
6
4
还
原
原
始
内
容
如
下
：
 
得
到
的
结
果
是
：
{
"
a
l
g
"
:
"
H
S
2
5
6
"
,
"
t
y
p
"
:
"
J
W
T
"
}
 
2
）
P
a
y
l
o
a
d
第
二
部
分
是
负
载
，
内
容
也
是
一
个
j
s
o
n
对
象
，
它
是
存
放
有
效
信
息
的
地
方
，
它
可
以
存
放
j
w
t
提
供
的
现
成
字
段
，
比
 
如
：
i
s
s
（
签
发
者
）
,
e
x
p
（
过
期
时
间
戳
）
,
 
s
u
b
（
面
向
的
用
户
）
等
，
也
可
自
定
义
字
段
。
 
此
部
分
不
建
议
存
放
敏
感
信
息
，
因
为
此
部
分
可
以
解
码
还
原
原
始
内
容
。
 
一
个
例
子
：
 
{
"
a
l
g
"
:
 
"
H
S
2
5
6
"
,
 
 
 
 
"
t
y
p
"
:
 
"
J
W
T
"
 
 
 
 
}
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
 
 
 
 
b
y
t
e
[
]
 
h
e
a
d
e
r
 
=
 
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
B
a
s
e
6
4
.
g
e
t
D
e
c
o
d
e
r
(
)
.
d
e
c
o
d
e
(
"
e
y
J
h
b
G
c
i
O
i
J
I
U
z
I
1
N
i
I
s
I
n
R
5
c
C
I
6
I
k
p
X
V
C
J
9
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
h
e
a
d
e
r
)
)
;
}
{
"
s
u
b
"
:
 
"
1
2
3
4
5
6
7
8
9
0
"
,
 
 
 
 
"
n
a
m
e
"
:
 
"
4
5
6
"
,
 
 
 
 
"
a
d
m
i
n
"
:
 
t
r
u
e
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 34 -->
最
后
将
第
二
部
分
负
载
使
用
B
a
s
e
6
4
U
r
l
编
码
，
得
到
一
个
字
符
串
就
是
J
W
T
令
牌
的
第
二
部
分
。
3
）
S
i
g
n
a
t
u
r
e
第
三
部
分
是
签
名
，
此
部
分
用
于
防
止
j
w
t
内
容
被
篡
改
。
 
这
个
部
分
使
用
b
a
s
e
6
4
u
r
l
将
前
两
部
分
进
行
编
码
，
编
码
后
使
用
点
（
.
）
连
接
组
成
字
符
串
，
最
后
使
用
h
e
a
d
e
r
中
声
明
 
签
名
算
法
进
行
签
名
。
 
一
个
例
子
：
 
b
a
s
e
6
4
U
r
l
E
n
c
o
d
e
(
h
e
a
d
e
r
)
：
j
w
t
令
牌
的
第
一
部
分
。
 
b
a
s
e
6
4
U
r
l
E
n
c
o
d
e
(
p
a
y
l
o
a
d
)
：
j
w
t
令
牌
的
第
二
部
分
。
 
s
e
c
r
e
t
：
签
名
所
使
用
的
密
钥
。
J
W
T
三
个
部
分
只
有
第
三
部
分
是
加
密
的
，
通
过
数
字
签
名
机
制
，
我
们
既
可
以
保
证
数
据
完
整
性
，
也
可
以
对
数
据
来
源
进
行
身
份
验
证
。
什
么
是
签
名
？
签
名
是
数
字
签
名
，
发
送
方
将
消
息
原
文
使
用
摘
要
算
法
生
成
摘
要
，
再
用
私
钥
对
摘
要
进
行
加
密
，
生
成
数
字
签
名
。
传
输
数
据
时
为
了
保
证
数
据
的
完
整
性
可
以
使
用
数
字
签
名
技
术
：
1
、
发
送
方
使
用
私
钥
对
内
容
进
行
数
字
签
名
2
、
将
内
容
附
带
数
字
签
名
发
送
给
对
方
3
、
对
方
收
到
内
容
和
数
字
签
名
，
使
用
公
钥
进
行
验
签
（
相
当
于
解
密
的
过
程
）
，
如
果
发
现
内
容
不
一
致
则
说
明
传
输
过
程
被
篡
改
。
 
 
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
(
b
a
s
e
6
4
U
r
l
E
n
c
o
d
e
(
h
e
a
d
e
r
)
 
+
 
"
.
"
 
+
b
a
s
e
6
4
U
r
l
E
n
c
o
d
e
(
p
a
y
l
o
a
d
)
,
s
e
c
r
e
t
)
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
