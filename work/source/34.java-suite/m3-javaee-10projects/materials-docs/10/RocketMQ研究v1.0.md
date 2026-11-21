# RocketMQ研究v1.0

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\day09 支付结果获取 RocketMQ\讲义-pdf\RocketMQ研究v1.0【海量资源尽在 666java.com】.pdf
- 页数：23
- 抽取：pypdf 文本层



<!-- page 1 -->
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
 
1
 
R
o
c
k
e
t
M
Q
介
绍
 
1
.
1
 
M
Q
的
应
用
场
景
 
M
Q
全
称
为
M
e
s
s
a
g
e
 
Q
u
e
u
e
，
即
消
息
队
列
，
 
开
发
中
消
息
队
列
通
常
有
如
下
应
用
场
景
：
1
、
任
务
异
步
处
理
。
将
不
需
要
同
步
处
理
的
并
且
耗
时
长
的
操
作
由
消
息
队
列
通
知
消
息
接
收
方
进
行
异
步
处
理
。
提
高
了
应
用
程
序
的
响
应
时
间
。
传
统
方
式
：
改
造
后
方
式
:
交
互
流
程
如
下
：
1
、
订
单
服
务
发
消
息
到
消
息
队
列
。
2
、
消
息
队
列
将
消
息
发
给
仓
储
服
务
和
物
流
服
务
。
3
、
仓
储
服
务
和
物
流
服
务
接
收
到
消
息
进
行
业
务
处
理
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
2
、
应
用
程
序
解
耦
合
M
Q
相
当
于
一
个
中
介
，
生
产
方
通
过
M
Q
与
消
费
方
交
互
，
它
将
应
用
程
序
进
行
解
耦
合
。
举
例
：
上
图
中
，
消
息
队
列
将
订
单
服
务
和
仓
储
服
务
进
行
解
耦
合
，
将
订
单
服
务
和
物
流
服
务
进
行
解
耦
合
。
3
）
日
志
收
集
：
 
 
进
行
统
一
业
务
日
志
收
集
，
供
分
析
系
统
进
行
数
据
分
析
，
消
息
队
列
作
为
日
志
数
据
的
中
转
站
。
交
互
流
程
如
下
：
1
、
采
集
系
统
从
l
o
g
日
志
文
件
采
集
数
据
，
发
送
至
消
息
队
列
 
。
2
、
各
日
志
需
求
服
务
从
消
息
队
列
 
接
收
消
息
进
行
日
志
处
理
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
1
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
介
绍
 
R
o
c
k
e
t
M
Q
是
阿
里
开
源
的
一
款
非
常
优
秀
中
间
件
产
品
，
脱
胎
于
阿
里
的
另
一
款
队
列
技
术
M
e
t
a
Q
，
后
捐
赠
给
A
p
a
c
h
e
基
金
会
作
为
一
款
孵
化
技
术
，
仅
仅
经
历
了
一
年
多
的
时
间
就
成
为
A
p
a
c
h
e
基
金
会
的
顶
级
项
目
。
并
且
它
现
在
已
经
在
阿
里
内
部
被
广
泛
的
应
用
，
并
且
经
受
住
了
多
次
双
十
一
的
这
种
极
致
场
景
的
压
力
。
（
2
0
1
7
年
的
双
十
一
，
R
o
c
k
e
t
M
Q
流
转
的
消
息
量
达
到
了
万
亿
级
，
峰
值
T
P
S
达
到
5
6
0
0
万
）
。
并
且
其
内
部
通
过
J
a
v
a
语
言
开
发
，
便
于
阅
读
与
修
改
。
h
t
t
p
:
/
/
r
o
c
k
e
t
m
q
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
 
1
.
3
 
消
息
队
列
技
术
选
型
对
比
 
市
场
上
还
有
哪
些
消
息
队
列
？
A
c
t
i
v
e
M
Q
，
R
a
b
b
i
t
M
Q
，
Z
e
r
o
M
Q
，
K
a
f
k
a
，
M
e
t
a
M
Q
，
R
e
d
i
s
。
本
项
目
选
用
R
o
c
k
e
t
M
Q
的
一
个
主
要
原
因
如
下
 
：
1
、
支
持
事
务
消
息
2
、
支
持
延
迟
消
息
3
、
天
然
支
持
集
群
、
负
载
均
衡
4
、
支
持
指
定
次
数
和
时
间
间
隔
的
失
败
消
息
重
发
详
细
的
技
术
选
型
对
比
如
下
：
 
R
a
b
b
i
t
M
Q
:
优
点
:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
1
.
支
持
A
M
Q
P
协
议
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
2
.
基
于
e
r
l
a
n
g
语
言
开
发
，
高
并
发
性
能
较
好
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
3
.
工
作
模
式
较
为
灵
活
 
 
 
 
 
 
 
 
 
 
4
.
支
持
延
迟
消
息
5
.
提
供
较
为
友
好
的
后
台
管
理
页
面
 
 
 
 
6
.
单
机
部
署
，
1
~
2
W
T
P
S
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
2
 
R
o
c
k
e
t
M
Q
基
础
 
2
.
1
组
成
结
构
 
R
o
c
k
e
t
M
Q
组
成
结
构
图
如
下
 
：
6
.
单
机
部
署
，
1
~
2
W
T
P
S
 
 
 
 
缺
点
：
1
.
不
支
持
水
平
扩
容
 
 
 
 
2
.
不
支
持
事
务
 
 
 
 
3
.
消
息
吞
吐
量
三
者
最
差
 
 
 
 
4
.
当
产
生
消
息
堆
积
，
性
能
下
降
明
显
 
 
 
 
5
.
消
息
重
发
机
制
需
要
手
动
设
置
 
 
 
 
6
.
不
支
持
消
息
重
复
消
费
 
 
 
 
R
o
c
k
e
t
M
Q
:
优
点
：
1
.
高
可
用
，
高
吞
吐
量
，
海
量
消
息
堆
积
，
低
延
迟
性
能
上
，
都
表
现
出
色
 
 
 
 
2
.
a
p
i
与
架
构
设
计
更
加
贴
切
业
务
场
景
 
 
 
 
3
.
支
持
顺
序
消
息
 
 
 
 
4
.
支
持
事
务
消
息
 
 
 
 
5
.
支
持
消
息
过
滤
 
 
 
 
6
.
支
持
重
复
消
费
 
 
 
 
7
.
支
持
延
迟
消
息
 
 
 
 
8
.
支
持
消
息
跟
踪
 
 
 
 
9
.
天
然
支
持
集
群
、
负
载
均
衡
 
 
 
 
1
0
.
支
持
指
定
次
数
和
时
间
间
隔
的
失
败
消
息
重
发
 
 
 
 
1
1
.
单
机
部
署
，
5
~
1
0
W
T
P
S
 
 
 
 
缺
点
：
1
.
生
态
圈
相
较
K
a
f
k
a
有
所
不
如
 
 
 
 
2
.
消
息
吞
吐
量
与
消
息
堆
积
能
力
也
不
如
K
a
f
k
a
 
 
 
 
3
.
不
支
持
主
从
自
动
切
换
 
 
 
 
4
.
只
支
持
J
a
v
a
 
 
 
 
K
a
f
k
a
:
优
点
：
1
.
高
可
用
，
高
吞
吐
量
，
低
延
迟
性
能
上
，
都
表
现
出
色
 
 
 
 
2
.
使
用
人
数
多
，
技
术
生
态
圈
完
善
 
 
 
 
3
.
支
持
顺
序
消
息
 
 
 
 
4
.
支
持
多
种
客
户
端
 
 
 
 
5
.
支
持
重
复
消
费
 
 
 
 
缺
点
：
1
.
依
赖
分
区
，
消
费
者
数
量
受
限
于
分
区
数
 
 
 
 
2
.
单
机
消
息
过
多
时
，
性
能
下
降
明
显
 
 
 
 
3
.
不
支
持
事
务
消
息
 
 
 
 
4
.
不
支
持
指
定
次
数
和
时
间
间
隔
的
失
败
消
息
重
发
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
交
互
过
程
如
下
：
1
）
B
r
o
k
d
e
r
定
时
发
送
自
身
状
态
 
到
N
a
m
e
S
e
r
v
e
r
。
2
）
P
r
o
d
u
c
e
r
 
请
求
N
a
m
e
S
e
r
v
e
r
获
取
B
r
o
k
e
r
的
地
址
。
3
）
P
r
o
d
u
c
e
r
 
将
消
息
发
送
到
B
r
o
k
e
r
中
的
消
息
队
列
。
4
）
C
o
n
s
u
m
e
r
订
阅
B
r
o
k
e
r
中
的
消
息
队
列
，
通
过
拉
取
消
息
，
或
由
B
r
o
k
e
r
将
消
息
推
送
至
C
o
n
s
u
m
e
r
。
1
）
P
r
o
d
u
c
e
r
 
C
l
u
s
t
e
r
 
消
息
生
产
者
群
负
责
发
送
消
息
，
一
般
由
业
务
系
统
负
责
产
生
消
息
。
2
）
C
o
n
s
u
m
e
r
 
C
l
u
s
t
e
r
 
消
息
费
群
负
责
消
费
消
息
，
一
般
是
后
台
系
统
负
责
异
步
消
费
。
两
种
消
费
模
式
：
P
u
s
h
 
C
o
n
s
u
m
e
r
，
服
务
端
向
消
费
者
端
推
送
消
息
P
u
l
l
 
C
o
n
s
u
m
e
r
，
消
费
者
端
向
服
务
定
时
拉
取
消
息
3
）
N
a
m
e
S
e
r
v
e
r
 
名
称
服
务
器
集
群
架
构
中
的
组
织
协
调
员
，
相
当
于
注
册
中
心
，
收
集
b
r
o
k
e
r
的
工
作
情
况
，
不
负
责
消
息
的
处
理
4
）
B
r
o
k
e
r
 
消
息
服
务
器
是
R
o
c
k
e
t
M
Q
的
核
心
，
负
责
消
息
的
接
受
，
存
储
，
发
送
等
。
需
要
定
时
发
送
自
身
状
态
 
到
N
a
m
e
S
e
r
v
e
r
，
默
认
1
0
秒
发
送
一
次
，
超
时
2
分
钟
会
认
为
该
b
r
o
k
e
r
失
效
。
 
2
.
2
 
安
装
R
o
c
k
e
t
M
Q
 
2
.
2
.
1
 
环
境
要
求
 
1
.
 
6
4
位
J
D
K
 
1
.
8
+
;
2
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
;
3
.
 
6
4
位
操
作
系
统
系
统
，
本
文
档
在
W
i
n
d
o
w
s
上
安
装
。
2
.
2
.
2
 
下
载
 
下
载
地
址
：
h
t
t
p
:
/
/
a
r
c
h
i
v
e
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
d
i
s
t
/
r
o
c
k
e
t
m
q
/
4
.
5
.
0
/
r
o
c
k
e
t
m
q
-
a
l
l
-
4
.
5
.
0
-
b
i
n
-
r
e
l
e
a
s
e
.
z
i
p
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
版
本
使
用
：
4
.
5
.
0
下
载
后
解
压
到
一
个
没
有
空
格
和
中
文
的
目
录
。
2
.
2
.
3
 
启
动
 
1
）
配
置
开
发
环
境
不
需
要
太
多
的
内
存
,
这
里
调
小
一
点
.
B
r
o
k
e
r
默
认
磁
盘
空
间
利
用
率
达
到
8
5
%
就
不
再
接
收
，
这
里
在
开
发
环
境
可
以
提
高
磁
盘
空
间
利
用
率
报
警
阀
值
为
9
8
%
。
 
2
）
启
动
N
a
m
e
S
e
r
v
e
r
进
入
c
m
d
命
令
窗
口
，
执
行
b
i
n
/
m
q
n
a
m
e
s
r
v
.
c
m
d
 
3
）
启
动
b
r
o
k
e
r
进
入
c
m
d
命
令
窗
口
，
执
行
b
i
n
/
m
q
b
r
o
k
e
r
.
c
m
d
 
-
n
 
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
调
整
默
认
的
内
存
大
小
参
数
 
c
d
 
b
i
n
/
 
v
i
m
 
r
u
n
s
e
r
v
e
r
.
c
m
d
 
s
e
t
 
"
J
A
V
A
_
O
P
T
=
%
J
A
V
A
_
O
P
T
%
 
‐
s
e
r
v
e
r
 
‐
X
m
s
5
1
2
m
 
‐
X
m
x
5
1
2
m
 
‐
X
m
n
5
1
2
m
 
‐
X
X
:
M
e
t
a
s
p
a
c
e
S
i
z
e
=
1
2
8
m
 
‐
X
X
:
M
a
x
M
e
t
a
s
p
a
c
e
S
i
z
e
=
3
2
0
m
"
 
c
d
 
b
i
n
/
 
v
i
m
 
r
u
n
b
r
o
k
e
r
.
c
m
d
 
s
e
t
 
"
J
A
V
A
_
O
P
T
=
%
J
A
V
A
_
O
P
T
%
 
‐
s
e
r
v
e
r
 
‐
D
r
o
c
k
e
t
m
q
.
b
r
o
k
e
r
.
d
i
s
k
S
p
a
c
e
W
a
r
n
i
n
g
L
e
v
e
l
R
a
t
i
o
=
0
.
9
8
 
‐
X
m
s
5
1
2
m
 
‐
X
m
x
5
1
2
m
 
‐
X
m
n
5
1
2
m
"
 
f
:
c
d
 
F
:
\
d
e
v
e
n
v
\
r
o
c
k
e
t
m
q
‐
a
l
l
‐
4
.
5
.
0
‐
b
i
n
‐
r
e
l
e
a
s
e
\
b
i
n
m
q
n
a
m
e
s
r
v
.
c
m
d
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
-
n
：
指
定
N
a
m
e
S
e
r
v
e
r
的
地
址
 
2
.
2
.
4
 
测
试
 
1
、
发
送
消
息
进
入
c
m
d
命
令
窗
口
，
执
行
：
 
 
2
、
接
送
消
息
进
入
c
m
d
命
令
窗
口
，
执
行
：
 
 
2
.
2
.
5
 
安
装
管
理
端
 
R
o
c
k
e
t
M
Q
提
供
了
U
I
管
理
工
具
，
名
为
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
，
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
p
a
c
h
e
/
r
o
c
k
e
t
m
q
-
e
x
t
e
r
n
a
l
s
/
t
r
e
e
/
m
a
s
t
e
r
/
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
1
）
下
载
源
代
码
见
资
料
文
件
夹
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
.
z
i
p
解
压
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
.
z
i
p
2
）
修
改
配
置
修
改
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
\
s
r
c
\
m
a
i
n
\
r
e
s
o
u
r
c
e
s
\
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
f
:
c
d
 
F
:
\
d
e
v
e
n
v
\
r
o
c
k
e
t
m
q
‐
a
l
l
‐
4
.
5
.
0
‐
b
i
n
‐
r
e
l
e
a
s
e
\
b
i
n
m
q
b
r
o
k
e
r
.
c
m
d
 
‐
n
 
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
s
e
t
 
N
A
M
E
S
R
V
_
A
D
D
R
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
9
8
7
6
c
d
 
F
:
\
d
e
v
e
n
v
\
r
o
c
k
e
t
m
q
‐
a
l
l
‐
4
.
5
.
0
‐
b
i
n
‐
r
e
l
e
a
s
e
\
b
i
n
t
o
o
l
s
.
c
m
d
 
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
e
x
a
m
p
l
e
.
q
u
i
c
k
s
t
a
r
t
.
P
r
o
d
u
c
e
r
s
e
t
 
N
A
M
E
S
R
V
_
A
D
D
R
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
9
8
7
6
t
o
o
l
s
.
c
m
d
 
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
e
x
a
m
p
l
e
.
q
u
i
c
k
s
t
a
r
t
.
C
o
n
s
u
m
e
r
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
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
8
7
7
 
/
/
 
服
务
端
口
号
 
r
o
c
k
e
t
m
q
.
c
o
n
ﬁ
g
.
n
a
m
e
s
r
v
A
d
d
r
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
9
8
7
6
 
/
/
 
名
称
服
务
地
址
r
o
c
k
e
t
m
q
.
c
o
n
ﬁ
g
.
d
a
t
a
P
a
t
h
=
/
t
m
p
/
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
/
d
a
t
a
 
/
/
 
m
q
数
据
路
径
3
）
打
包
进
入
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
目
录
下
c
m
d
下
执
行
：
 
4
）
启
动
 
进
入
/
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
/
t
a
r
g
e
t
j
a
v
a
 
-
j
a
r
 
r
o
c
k
e
t
m
q
-
c
o
n
s
o
l
e
-
n
g
-
1
.
0
.
1
.
j
a
r
 
-
-
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
8
7
7
 
-
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
c
o
n
ﬁ
g
.
n
a
m
e
s
r
v
A
d
d
r
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
9
8
7
6
5
)
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
9
8
7
7
 
2
.
3
 
快
速
入
门
 
2
.
3
.
1
 
三
种
消
息
发
送
方
式
 
R
o
c
k
e
t
M
Q
 
支
持
 
3
 
种
消
息
发
送
方
式
 
：
1
、
同
步
消
息
（
s
y
n
c
 
m
e
s
s
a
g
e
 
）
p
r
o
d
u
c
e
r
向
 
b
r
o
k
e
r
 
发
送
消
息
，
执
行
 
A
P
I
 
时
同
步
等
待
，
 
直
到
b
r
o
k
e
r
 
服
务
器
返
回
发
送
结
果
 
。
m
v
n
 
c
l
e
a
n
 
p
a
c
k
a
g
e
 
‐
D
m
a
v
e
n
.
t
e
s
t
.
s
k
i
p
=
t
r
u
e
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
2
、
异
步
消
息
（
a
s
y
n
c
 
m
e
s
s
a
g
e
）
p
r
o
d
u
c
e
r
向
 
b
r
o
k
e
r
 
发
送
消
息
时
指
定
消
息
发
送
成
功
及
发
送
异
常
的
回
调
方
法
，
调
用
 
A
P
I
 
后
立
即
返
回
，
p
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
线
程
不
阻
塞
 
，
消
息
发
送
成
功
或
失
败
的
回
调
任
务
在
一
个
新
的
线
程
中
执
行
 
。
3
、
单
向
消
息
（
o
n
e
w
a
y
 
m
e
s
s
a
g
e
）
p
r
o
d
u
c
e
r
向
 
b
r
o
k
e
r
 
发
送
消
息
，
执
行
 
A
P
I
 
时
直
接
返
回
，
不
等
待
b
r
o
k
e
r
 
服
务
器
的
结
果
 
。
 
2
.
3
.
2
 
消
息
结
构
 
R
o
c
k
e
t
M
Q
的
消
息
包
括
基
础
属
性
和
扩
展
属
性
两
部
分
：
1
、
基
础
属
性
1
）
t
o
p
i
c
 
：
 
主
题
相
当
于
消
息
的
一
级
分
类
，
具
有
相
同
t
o
p
i
c
的
消
息
将
发
送
至
该
t
o
p
i
c
下
的
消
息
队
列
中
，
比
方
说
一
个
电
商
系
统
可
以
分
为
商
品
消
息
、
订
单
消
息
、
物
流
消
息
等
，
就
可
以
在
b
r
o
k
e
r
中
创
建
商
品
主
题
、
订
单
主
题
等
，
所
有
商
品
的
消
息
发
送
至
该
主
题
下
的
消
息
队
列
中
。
2
）
消
息
体
：
即
消
息
的
内
容
 
，
可
以
的
字
符
串
、
对
象
等
类
型
（
可
系
列
化
）
。
消
息
的
最
大
长
度
 
是
4
M
。
3
）
 
消
息
 
F
l
a
g
：
消
息
的
一
个
标
记
，
R
o
c
k
e
t
M
Q
不
处
理
，
留
给
业
务
系
统
使
用
。
2
、
扩
展
属
性
1
）
t
a
g
 
：
相
当
于
消
息
的
二
级
分
类
，
用
于
消
费
消
息
时
进
行
过
滤
，
可
为
空
 
。
2
）
k
e
y
s
:
 
M
e
s
s
a
g
e
 
索
引
键
，
在
运
维
中
可
以
根
据
这
些
 
k
e
y
 
快
速
检
索
到
消
息
，
 
可
为
空
 
。
 
3
）
w
a
i
t
S
t
o
r
e
M
s
g
O
K
 
：
消
息
发
送
时
是
否
等
消
息
存
储
完
成
后
再
返
回
 
。
M
e
s
s
a
g
e
 
的
基
础
属
性
主
要
包
括
消
息
所
属
主
题
 
t
o
p
i
c
 
，
 
消
息
 
F
l
a
g
(
R
o
c
k
e
t
M
Q
 
不
做
处
理
）
、
 
扩
展
属
性
、
消
息
体
 
。
 
2
.
3
.
3
 
生
产
者
工
程
 
2
.
3
.
3
.
1
 
创
建
生
产
者
工
程
 
工
程
结
构
如
下
：
1
）
创
建
t
e
s
t
-
r
o
c
k
e
t
m
q
创
建
一
个
t
e
s
t
-
r
o
c
k
e
t
m
q
的
测
试
工
程
专
门
用
于
r
o
c
k
e
t
m
q
的
功
能
测
试
。
t
e
s
t
-
r
o
c
k
e
t
m
q
父
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
2
）
创
建
r
o
c
k
e
t
m
q
-
p
r
o
d
u
c
e
r
生
产
者
工
程
r
o
c
k
e
t
m
q
-
p
r
o
d
u
c
e
r
的
p
o
m
.
x
m
l
如
下
 
 
3
）
 
新
建
r
o
c
k
e
t
m
q
-
p
r
o
d
u
c
e
r
工
程
 
的
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
文
件
 
 
 
 
 
 
 
 
 
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
t
e
s
t
‐
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
t
e
s
t
‐
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
r
o
c
k
e
t
m
q
‐
p
r
o
d
u
c
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
p
r
o
j
e
c
t
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
4
）
新
建
启
动
类
 
 
2
.
3
.
3
.
2
 
发
送
同
步
消
息
 
 
 
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
 
8
1
8
1
 
#
服
务
端
口
 
 
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
r
o
c
k
e
t
m
q
‐
p
r
o
d
u
c
e
r
 
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
 
r
o
c
k
e
t
m
q
‐
p
r
o
d
u
c
e
r
 
#
指
定
服
务
名
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
 
d
e
m
o
‐
p
r
o
d
u
c
e
r
‐
g
r
o
u
p
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
 
P
r
o
d
u
c
e
r
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
P
r
o
d
u
c
e
r
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
e
s
t
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
 
/
*
*
 
*
 
r
o
c
k
e
t
m
q
发
送
消
息
类
 
*
 
@
a
u
t
h
o
r
 
A
d
m
i
n
i
s
t
r
a
t
o
r
 
*
 
@
v
e
r
s
i
o
n
 
1
.
0
 
*
*
/
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
r
o
d
u
c
e
r
S
i
m
p
l
e
 
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
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
发
送
同
步
消
息
 
 
 
 
 
*
 
@
p
a
r
a
m
 
t
o
p
i
c
 
 
 
 
 
*
 
@
p
a
r
a
m
 
m
s
g
 
 
 
 
 
*
/
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
2
.
3
.
3
.
3
 
测
试
 
1
、
在
t
e
s
t
下
编
写
测
试
类
，
发
送
同
步
消
息
。
 
2
、
启
动
N
a
m
e
S
e
r
v
e
r
、
B
r
o
k
e
r
、
管
理
端
3
、
执
行
t
e
s
t
S
e
n
d
S
y
n
c
M
s
g
方
法
4
、
观
察
控
制
台
和
管
理
端
控
制
台
出
现
e
n
d
.
.
.
 
表
示
消
息
发
送
成
功
。
进
入
管
理
端
，
查
询
消
息
。
 
 
 
 
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
 
s
e
n
d
S
y
n
c
M
s
g
(
S
t
r
i
n
g
 
t
o
p
i
c
,
 
S
t
r
i
n
g
 
m
s
g
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
s
y
n
c
S
e
n
d
(
t
o
p
i
c
,
m
s
g
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
e
s
t
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
 
/
*
*
 
*
 
@
a
u
t
h
o
r
 
A
d
m
i
n
i
s
t
r
a
t
o
r
 
*
 
@
v
e
r
s
i
o
n
 
1
.
0
 
*
*
/
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
 
P
r
o
d
u
c
e
r
S
i
m
p
l
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
 
 
 
 
p
r
i
v
a
t
e
 
P
r
o
d
u
c
e
r
S
i
m
p
l
e
 
p
r
o
d
u
c
e
r
S
i
m
p
l
e
;
 
 
 
 
 
/
/
测
试
发
送
同
步
消
息
 
 
 
 
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
n
d
S
y
n
c
M
s
g
(
)
{
 
 
 
 
 
 
 
 
t
h
i
s
.
p
r
o
d
u
c
e
r
S
i
m
p
l
e
.
s
e
n
d
S
y
n
c
M
s
g
(
"
m
y
‐
t
o
p
i
c
"
,
 
"
第
一
条
同
步
消
息
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
"
e
n
d
.
.
.
"
)
;
 
 
 
 
}
 
}
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
2
.
3
.
4
 
消
费
者
工
程
 
2
.
3
.
4
.
1
 
创
建
消
费
者
工
程
 
创
建
消
息
消
费
者
工
程
，
p
o
m
.
x
m
l
如
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
t
e
s
t
‐
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
r
o
c
k
e
t
m
q
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

<!-- page 14 -->
2
、
启
动
类
 
3
、
配
置
文
件
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
 
 
2
.
3
.
4
.
2
 
消
费
消
息
 
编
写
消
费
消
息
监
听
类
：
 
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
 
C
o
n
s
u
m
e
r
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
C
o
n
s
u
m
e
r
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
 
8
1
8
2
 
#
服
务
端
口
 
 
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
r
o
c
k
e
t
m
q
‐
c
o
n
s
u
m
e
r
 
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
 
r
o
c
k
e
t
m
q
‐
c
o
n
s
u
m
e
r
 
#
指
定
服
务
名
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
e
s
t
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
s
u
m
e
M
o
d
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
L
i
s
t
e
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
 
/
*
*
 
*
 
消
费
消
息
监
听
类
 
*
 
@
a
u
t
h
o
r
 
A
d
m
i
n
i
s
t
r
a
t
o
r
 
*
 
@
v
e
r
s
i
o
n
 
1
.
0
 
*
*
/
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
m
y
‐
t
o
p
i
c
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
d
e
m
o
‐
c
o
n
s
u
m
e
r
‐
g
r
o
u
p
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
 
C
o
n
s
u
m
e
r
S
i
m
p
l
e
 
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
S
t
r
i
n
g
>
 
{
 
 
 
 
 
/
/
接
手
到
消
息
调
用
此
方
法
 
 
 
 
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
S
t
r
i
n
g
 
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
s
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 15 -->
监
听
消
息
队
列
 
需
要
指
定
：
t
o
p
i
c
：
监
听
的
主
题
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
：
消
费
组
，
相
同
消
费
组
的
消
费
者
共
同
消
费
该
主
题
的
消
息
，
它
们
组
成
一
个
集
群
。
 
2
.
3
.
4
.
3
 
测
试
 
1
、
启
动
消
费
者
工
程
启
动
消
费
者
工
程
，
观
察
控
制
台
输
出
“
第
一
条
同
步
消
息
”
消
息
内
容
，
这
说
明
从
消
息
队
列
已
经
读
取
到
消
息
。
2
、
保
证
消
费
者
工
程
已
启
动
，
再
次
发
送
消
息
，
观
察
控
制
台
是
否
输
出
“
第
一
条
同
步
消
息
”
消
息
内
容
，
输
出
则
说
明
接
收
消
息
成
功
。
 
2
.
4
 
消
息
发
送
过
程
 
通
过
快
速
入
门
对
消
息
的
发
送
和
接
收
有
一
个
粗
略
的
认
识
，
下
边
分
析
具
体
的
消
息
发
送
过
程
，
如
下
图
：
消
息
发
送
流
程
如
下
：
1
、
P
r
o
d
u
c
e
r
从
N
a
m
e
S
e
r
v
e
r
中
获
取
主
题
路
由
信
息
B
r
o
k
e
r
将
自
己
的
状
态
上
报
给
N
a
m
e
S
e
r
v
e
r
，
N
a
m
e
S
e
r
v
e
r
中
存
储
了
每
个
B
r
o
k
e
r
及
主
题
、
消
息
队
列
的
信
息
。
P
r
o
d
u
c
e
r
根
据
 
t
o
p
i
c
从
N
a
m
e
S
e
r
v
e
r
查
询
所
有
消
息
队
列
，
查
询
到
的
结
果
例
如
：
 
 
 
 
}
}
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 16 -->
P
r
o
d
u
c
e
r
按
选
择
算
法
从
以
上
队
列
中
选
择
一
个
进
行
消
息
发
送
，
如
果
发
送
消
息
失
败
则
在
下
次
选
择
的
时
候
 
会
规
避
掉
失
败
的
b
r
o
k
e
r
。
2
、
构
建
消
息
，
发
送
消
息
发
送
消
息
前
进
行
校
验
，
比
如
消
息
的
内
容
长
度
不
能
为
0
、
消
息
最
大
长
度
、
消
息
必
要
的
属
性
是
否
具
备
等
（
t
o
p
i
c
、
消
息
体
，
生
产
组
等
）
。
如
果
该
t
o
p
i
c
下
还
没
有
队
列
则
自
动
创
建
，
默
认
一
个
t
o
p
i
c
下
自
动
创
建
4
个
写
队
列
，
4
个
读
队
列
 
。
为
什
么
要
多
个
队
列
 
？
1
）
高
可
用
当
某
个
队
列
不
可
用
时
其
它
队
列
顶
上
。
2
）
提
高
并
发
发
送
消
息
是
选
择
队
列
进
行
发
送
，
提
高
发
送
消
息
的
并
发
能
力
。
消
息
消
费
时
每
个
消
费
者
可
以
监
听
多
个
队
列
，
提
高
消
费
消
息
的
并
发
能
力
。
生
产
组
有
什
么
用
？
在
事
务
消
息
中
b
r
o
k
e
r
需
要
回
查
p
r
o
d
u
c
e
r
，
同
一
个
生
产
组
的
p
r
o
d
u
c
e
r
组
成
一
个
集
群
，
提
高
并
发
能
力
。
 
3
、
监
听
队
列
，
消
费
消
息
一
个
消
费
组
可
以
包
括
多
个
消
费
者
，
一
个
消
费
组
可
以
订
阅
多
个
主
题
。
一
个
队
列
同
时
只
允
许
一
个
消
费
者
消
费
，
一
个
消
费
者
可
以
消
费
多
个
队
列
中
的
消
息
。
消
费
组
有
两
种
消
费
模
式
：
1
）
集
群
模
式
一
个
消
费
组
内
的
消
费
者
组
成
一
个
集
群
，
主
题
下
的
一
条
消
息
只
能
被
一
个
消
费
者
消
费
。
2
）
广
播
模
式
主
题
下
的
一
条
消
息
能
被
消
费
组
下
的
所
有
消
费
者
消
费
。
消
费
者
和
b
r
o
k
e
r
之
间
通
过
推
模
式
和
拉
模
式
接
收
消
息
，
推
模
式
即
b
r
o
k
e
r
推
送
给
消
费
者
，
拉
模
式
是
消
费
者
主
动
从
b
r
o
k
e
r
查
询
消
息
。
 
 
2
.
5
 
三
种
消
息
发
送
方
式
 
[
 
 
{
"
b
r
o
k
e
r
N
a
m
e
"
:
"
B
r
o
k
e
r
‐
1
"
,
"
q
u
e
u
e
I
d
"
:
0
}
,
 
 
{
"
b
r
o
k
e
r
N
a
m
e
"
:
"
B
r
o
k
e
r
‐
1
"
,
"
q
u
e
u
e
I
d
"
:
1
}
,
 
 
{
"
b
r
o
k
e
r
N
a
m
e
"
:
"
B
r
o
k
e
r
‐
2
"
,
"
q
u
e
u
e
I
d
"
:
0
}
,
 
 
{
"
b
r
o
k
e
r
N
a
m
e
"
:
"
B
r
o
k
e
r
‐
2
"
,
"
q
u
e
u
e
I
d
"
:
1
}
]
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 17 -->
R
o
c
k
e
t
M
Q
 
支
持
 
3
 
种
消
息
发
送
方
式
 
，
即
同
 
步
消
息
（
s
y
n
c
 
m
e
s
s
a
g
e
 
）
 
、
异
步
消
息
（
a
s
y
n
c
 
m
e
s
s
a
g
e
）
、
单
向
消
息
（
o
n
e
w
a
y
 
m
e
s
s
a
g
e
）
 
。
2
.
5
.
1
 
同
步
消
息
 
参
见
快
速
入
门
的
测
试
程
序
。
2
.
5
.
2
 
异
步
消
息
 
p
r
o
d
u
c
e
r
向
 
b
r
o
k
e
r
 
发
送
消
息
时
指
定
消
息
发
送
成
功
及
发
送
异
常
的
回
调
方
法
，
调
用
 
A
P
I
 
后
立
即
返
回
，
p
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
线
程
不
阻
塞
 
，
消
息
发
送
成
功
或
失
败
的
回
调
任
务
在
一
个
新
的
线
程
中
执
行
 
。
在
P
r
o
d
u
c
e
r
S
i
m
p
l
e
中
编
写
发
送
异
步
消
息
的
方
法
 
测
试
：
 
2
.
5
.
3
 
单
向
消
息
 
p
r
o
d
u
c
e
r
向
 
b
r
o
k
e
r
 
发
送
消
息
，
执
行
 
A
P
I
 
时
直
接
返
回
，
不
等
待
b
r
o
k
e
r
 
服
务
器
的
结
果
 
。
/
*
*
 
*
 
发
送
异
步
消
息
 
*
 
@
p
a
r
a
m
 
t
o
p
i
c
 
*
 
@
p
a
r
a
m
 
m
s
g
 
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
 
s
e
n
d
A
S
y
n
c
M
s
g
(
S
t
r
i
n
g
 
t
o
p
i
c
,
 
S
t
r
i
n
g
 
m
s
g
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
a
s
y
n
c
S
e
n
d
(
t
o
p
i
c
,
m
s
g
,
n
e
w
 
S
e
n
d
C
a
l
l
b
a
c
k
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
 
v
o
i
d
 
o
n
S
u
c
c
e
s
s
(
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
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
成
功
回
调
 
 
 
 
 
 
 
 
 
 
 
 
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
.
g
e
t
S
e
n
d
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
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
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
T
h
r
o
w
a
b
l
e
 
e
)
 
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
异
常
回
调
 
 
 
 
 
 
 
 
 
 
 
 
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
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
)
;
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
S
e
n
d
A
S
y
n
c
M
s
g
(
)
 
t
h
r
o
w
s
 
I
n
t
e
r
r
u
p
t
e
d
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
 
 
 
 
t
h
i
s
.
p
r
o
d
u
c
e
r
S
i
m
p
l
e
.
s
e
n
d
A
S
y
n
c
M
s
g
(
"
m
y
‐
t
o
p
i
c
"
,
 
"
第
一
条
异
步
步
消
息
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
"
e
n
d
.
.
.
"
)
;
 
 
 
 
/
/
异
步
消
息
，
为
跟
踪
回
调
线
程
这
里
加
入
延
迟
 
 
 
 
T
h
r
e
a
d
.
s
l
e
e
p
(
3
0
0
0
)
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 18 -->
测
试
：
略
。
 
2
.
6
 
自
定
义
消
息
格
式
 
前
边
我
们
发
送
的
消
息
内
容
格
式
都
是
字
符
串
，
在
生
产
开
发
中
消
息
内
容
格
式
是
复
杂
的
，
本
小
节
介
绍
如
何
对
消
息
格
式
进
行
自
定
义
。
J
S
O
N
是
互
联
网
开
发
中
非
常
常
用
的
数
据
格
式
，
它
具
有
格
式
标
准
，
扩
展
方
便
的
特
点
，
将
消
息
的
格
式
使
用
J
S
O
N
进
行
定
义
可
以
提
高
消
息
内
容
的
扩
展
性
，
R
o
c
k
e
t
M
Q
支
持
传
递
J
S
O
N
数
据
格
式
。
在
生
产
端
和
消
费
端
定
义
模
型
类
：
 
生
产
端
：
/
*
*
 
*
 
发
送
单
向
消
息
 
*
 
@
p
a
r
a
m
 
t
o
p
i
c
 
*
 
@
p
a
r
a
m
 
m
s
g
 
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
 
s
e
n
d
O
n
e
W
a
y
M
s
g
(
S
t
r
i
n
g
 
t
o
p
i
c
,
 
S
t
r
i
n
g
 
m
s
g
)
{
 
 
 
 
t
h
i
s
.
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
e
n
d
O
n
e
W
a
y
(
t
o
p
i
c
,
m
s
g
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
t
e
s
t
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
m
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
 
l
o
m
b
o
k
.
T
o
S
t
r
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
 
j
a
v
a
.
i
o
.
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
D
a
t
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
T
o
S
t
r
i
n
g
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
E
x
t
 
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
 
S
t
r
i
n
g
 
i
d
;
 
 
 
 
 
p
r
i
v
a
t
e
 
D
a
t
e
 
c
r
e
a
t
e
T
i
m
e
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
 
m
o
n
e
y
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
 
t
i
t
l
e
;
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 19 -->
消
费
端
：
 
上
例
实
现
了
R
o
c
k
e
t
M
Q
传
输
J
S
O
N
消
息
的
过
程
，
消
费
端
在
接
收
到
J
S
O
N
手
动
将
J
S
O
N
转
成
对
象
，
也
可
以
自
动
转
换
成
对
象
，
代
码
如
下
：
定
义
新
的
监
听
类
，
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
泛
型
指
定
要
转
换
的
对
象
类
型
。
 
 
2
.
7
 
延
迟
消
息
 
2
.
7
.
1
 
延
迟
消
息
介
绍
 
/
*
*
 
*
 
消
息
内
容
为
j
s
o
n
格
式
 
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
 
s
e
n
d
M
s
g
B
y
J
s
o
n
(
S
t
r
i
n
g
 
t
o
p
i
c
,
 
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
t
)
{
 
 
 
 
/
/
发
送
同
步
消
息
，
消
息
内
容
将
o
r
d
e
r
E
x
t
转
为
j
s
o
n
 
 
 
 
t
h
i
s
.
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
t
o
p
i
c
,
o
r
d
e
r
E
x
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
f
(
"
s
e
n
d
 
m
s
g
 
:
 
%
s
"
,
o
r
d
e
r
E
x
t
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
m
y
‐
t
o
p
i
c
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
d
e
m
o
‐
c
o
n
s
u
m
e
r
‐
g
r
o
u
p
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
 
C
o
n
s
u
m
e
r
S
i
m
p
l
e
 
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
S
t
r
i
n
g
>
 
{
 
 
 
 
 
/
/
接
手
到
消
息
调
用
此
方
法
 
 
 
 
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
S
t
r
i
n
g
 
s
)
 
{
 
 
 
 
 
 
 
 
/
/
如
果
是
j
s
o
n
数
据
，
可
以
将
j
s
o
n
转
为
对
象
/
/
 
 
 
 
 
 
 
 
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
t
 
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
s
,
 
O
r
d
e
r
E
x
t
.
c
l
a
s
s
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
s
)
;
 
 
 
 
}
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
m
y
‐
t
o
p
i
c
‐
o
b
j
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
d
e
m
o
‐
c
o
n
s
u
m
e
r
‐
g
r
o
u
p
‐
o
b
j
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
 
C
o
n
s
u
m
e
r
S
i
m
p
l
e
O
b
j
 
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
O
r
d
e
r
E
x
t
>
 
{
 
 
 
 
 
/
/
接
手
到
消
息
调
用
此
方
法
 
 
 
 
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
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
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
o
r
d
e
r
E
x
t
)
;
 
 
 
 
}
}
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 20 -->
延
迟
消
息
也
叫
做
定
时
消
息
，
比
如
在
电
商
项
目
的
交
易
系
统
中
，
当
用
户
下
单
之
后
超
过
一
段
时
间
之
后
仍
然
没
有
支
付
，
此
时
就
需
要
将
该
订
单
关
l
闭
。
要
实
现
该
功
能
的
话
，
可
以
在
用
户
创
建
订
单
时
就
发
送
一
条
包
含
订
单
内
容
的
延
迟
消
息
，
该
消
息
在
一
段
时
间
之
后
投
递
给
消
息
消
费
者
，
当
消
息
消
费
者
接
收
到
该
消
息
后
，
判
断
该
订
单
的
支
付
状
态
，
如
果
处
于
未
支
付
状
态
，
则
将
该
订
单
关
闭
。
R
o
c
k
e
t
M
Q
的
延
迟
消
息
实
现
非
常
简
单
，
只
需
要
发
送
消
息
前
设
置
延
迟
的
时
间
，
延
迟
时
间
存
在
十
八
个
等
级
（
1
s
/
5
s
/
1
0
s
/
3
0
s
/
1
m
/
2
m
/
3
m
/
4
m
/
5
m
/
6
m
/
7
m
/
8
m
/
9
m
/
1
0
m
/
2
0
m
/
3
0
m
/
1
h
/
2
h
）
，
调
用
s
e
t
D
e
l
a
y
T
i
m
e
L
e
v
e
l
(
)
设
置
与
时
间
相
对
应
的
延
迟
级
别
即
可
。
2
.
7
.
2
 
同
步
消
息
延
迟
 
生
产
端
：
 
消
费
端
：
同
自
定
义
消
息
格
式
章
节
。
测
试
：
 
2
.
7
.
3
 
异
步
消
息
延
迟
（
自
学
）
 
生
产
端
：
 
/
*
*
 
*
 
发
送
延
迟
消
息
 
*
 
消
息
内
容
为
j
s
o
n
格
式
 
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
 
s
e
n
d
M
s
g
B
y
J
s
o
n
D
e
l
a
y
(
S
t
r
i
n
g
 
t
o
p
i
c
,
 
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
t
)
 
t
h
r
o
w
s
 
J
s
o
n
P
r
o
c
e
s
s
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
,
 
I
n
t
e
r
r
u
p
t
e
d
E
x
c
e
p
t
i
o
n
,
 
R
e
m
o
t
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
,
 
M
Q
C
l
i
e
n
t
E
x
c
e
p
t
i
o
n
,
 
M
Q
B
r
o
k
e
r
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
发
送
同
步
消
息
，
消
息
内
容
将
o
r
d
e
r
E
x
t
转
为
j
s
o
n
 
 
 
 
M
e
s
s
a
g
e
<
O
r
d
e
r
E
x
t
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
o
r
d
e
r
E
x
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
 
 
 
 
/
/
指
定
发
送
超
时
时
间
（
毫
秒
）
和
延
迟
等
级
 
 
 
 
t
h
i
s
.
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
t
o
p
i
c
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
f
(
"
s
e
n
d
 
m
s
g
 
:
 
%
s
"
,
o
r
d
e
r
E
x
t
)
;
}
/
/
测
试
发
送
同
步
消
息
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
n
d
M
s
g
B
y
J
s
o
n
D
e
l
a
y
(
)
 
t
h
r
o
w
s
 
J
s
o
n
P
r
o
c
e
s
s
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
,
 
I
n
t
e
r
r
u
p
t
e
d
E
x
c
e
p
t
i
o
n
,
 
R
e
m
o
t
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
,
 
M
Q
C
l
i
e
n
t
E
x
c
e
p
t
i
o
n
,
 
M
Q
B
r
o
k
e
r
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
 
 
 
 
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
t
 
=
 
n
e
w
 
O
r
d
e
r
E
x
t
(
)
;
 
 
 
 
o
r
d
e
r
E
x
t
.
s
e
t
I
d
(
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
 
 
 
 
o
r
d
e
r
E
x
t
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
n
e
w
 
D
a
t
e
(
)
)
;
 
 
 
 
o
r
d
e
r
E
x
t
.
s
e
t
M
o
n
e
y
(
1
6
8
L
)
;
 
 
 
 
o
r
d
e
r
E
x
t
.
s
e
t
T
i
t
l
e
(
"
测
试
订
单
"
)
;
 
 
 
 
t
h
i
s
.
p
r
o
d
u
c
e
r
S
i
m
p
l
e
.
s
e
n
d
M
s
g
B
y
J
s
o
n
D
e
l
a
y
(
"
m
y
‐
t
o
p
i
c
‐
o
b
j
"
,
o
r
d
e
r
E
x
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
"
e
n
d
.
.
.
"
)
;
}
/
*
*
 
*
 
发
送
异
步
延
迟
消
息
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 21 -->
消
费
端
：
同
自
定
义
消
息
格
式
章
节
。
测
试
/
/
测
试
发
送
异
步
消
息
 
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
n
d
A
s
y
n
c
M
s
g
B
y
J
s
o
n
D
e
l
a
y
(
)
 
t
h
r
o
w
s
 
J
s
o
n
P
r
o
c
e
s
s
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
,
 
I
n
t
e
r
r
u
p
t
e
d
E
x
c
e
p
t
i
o
n
,
 
R
e
m
o
t
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
,
 
M
Q
C
l
i
e
n
t
E
x
c
e
p
t
i
o
n
,
 
M
Q
B
r
o
k
e
r
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
 
 
 
 
 
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
t
 
=
 
n
e
w
 
O
r
d
e
r
E
x
t
(
)
;
 
 
 
 
 
o
r
d
e
r
E
x
t
.
s
e
t
I
d
(
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
 
 
 
 
 
o
r
d
e
r
E
x
t
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
n
e
w
 
D
a
t
e
(
)
)
;
 
 
 
 
 
o
r
d
e
r
E
x
t
.
s
e
t
M
o
n
e
y
(
1
6
8
L
)
;
 
 
 
 
 
o
r
d
e
r
E
x
t
.
s
e
t
T
i
t
l
e
(
"
测
试
订
单
"
)
;
 
 
 
 
 
t
h
i
s
.
p
r
o
d
u
c
e
r
S
i
m
p
l
e
.
s
e
n
d
A
s
y
n
c
M
s
g
B
y
J
s
o
n
D
e
l
a
y
(
"
m
y
‐
t
o
p
i
c
‐
o
b
j
"
,
o
r
d
e
r
E
x
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
"
e
n
d
.
.
.
"
)
;
 
 
 
 
 
T
h
r
e
a
d
.
s
l
e
e
p
(
2
0
0
0
0
)
;
 
}
 
2
.
8
 
消
费
重
试
 
2
.
8
.
1
 
什
么
是
消
费
重
试
 
 
*
 
消
息
内
容
为
j
s
o
n
格
式
 
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
 
s
e
n
d
A
s
y
n
c
M
s
g
B
y
J
s
o
n
D
e
l
a
y
(
S
t
r
i
n
g
 
t
o
p
i
c
,
 
O
r
d
e
r
E
x
t
 
o
r
d
e
r
E
x
t
)
 
t
h
r
o
w
s
 
J
s
o
n
P
r
o
c
e
s
s
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
,
 
I
n
t
e
r
r
u
p
t
e
d
E
x
c
e
p
t
i
o
n
,
 
R
e
m
o
t
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
,
 
M
Q
C
l
i
e
n
t
E
x
c
e
p
t
i
o
n
,
 
M
Q
B
r
o
k
e
r
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
消
息
内
容
将
o
r
d
e
r
E
x
t
转
为
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
 
j
s
o
n
 
=
 
t
h
i
s
.
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
g
e
t
O
b
j
e
c
t
M
a
p
p
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
V
a
l
u
e
A
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
E
x
t
)
;
 
 
 
 
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
c
o
m
m
o
n
.
m
e
s
s
a
g
e
.
M
e
s
s
a
g
e
 
m
e
s
s
a
g
e
 
=
 
n
e
w
 
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
c
o
m
m
o
n
.
m
e
s
s
a
g
e
.
M
e
s
s
a
g
e
(
t
o
p
i
c
,
j
s
o
n
.
g
e
t
B
y
t
e
s
(
C
h
a
r
s
e
t
.
f
o
r
N
a
m
e
(
"
u
t
f
‐
8
"
)
)
)
;
 
 
 
 
/
/
设
置
延
迟
等
级
 
 
 
 
m
e
s
s
a
g
e
.
s
e
t
D
e
l
a
y
T
i
m
e
L
e
v
e
l
(
3
)
;
 
 
 
 
/
/
发
送
异
步
消
息
 
 
 
 
t
h
i
s
.
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
g
e
t
P
r
o
d
u
c
e
r
(
)
.
s
e
n
d
(
m
e
s
s
a
g
e
,
n
e
w
 
S
e
n
d
C
a
l
l
b
a
c
k
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
 
v
o
i
d
 
o
n
S
u
c
c
e
s
s
(
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
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
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
t
h
r
o
w
a
b
l
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
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
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
f
(
"
s
e
n
d
 
m
s
g
 
:
 
%
s
"
,
o
r
d
e
r
E
x
t
)
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 22 -->
当
消
息
发
送
到
B
r
o
k
e
r
成
功
，
在
被
消
费
者
消
费
时
如
果
消
费
者
没
有
正
常
消
费
，
此
时
消
息
会
重
试
消
费
。
消
费
重
试
存
在
两
种
场
景
：
 
 
1
）
消
息
没
有
被
消
费
者
接
收
，
比
如
消
费
者
与
b
r
o
k
e
r
存
在
网
络
异
常
。
此
种
情
况
消
息
会
一
直
被
消
费
重
试
。
 
 
2
）
当
消
息
已
经
被
消
费
者
成
功
接
收
，
但
是
在
进
行
消
息
处
理
时
出
现
异
常
，
消
费
端
无
法
向
B
r
o
k
e
r
返
回
成
功
，
这
种
情
况
下
R
o
c
k
e
t
M
Q
会
不
断
重
试
。
本
小
节
重
点
讨
论
第
二
个
场
景
。
 
 
针
对
第
二
种
消
费
重
试
的
场
景
，
b
o
r
k
e
r
是
怎
么
知
道
重
试
呢
？
 
 
消
费
者
在
消
费
消
息
成
功
会
向
b
r
o
k
e
r
返
回
成
功
状
态
，
否
则
会
不
断
进
行
消
费
重
试
。
2
.
8
.
2
 
处
理
策
略
 
当
消
息
在
消
费
时
出
现
异
常
，
此
时
消
息
被
不
断
重
试
消
费
。
R
o
c
k
e
t
M
Q
会
一
直
重
试
消
费
吗
？
答
案
是
不
会
！
消
息
会
按
照
延
迟
消
息
的
延
迟
时
间
等
级
（
1
s
 
5
s
 
1
0
s
 
3
0
s
 
1
m
 
2
m
 
3
m
 
4
m
 
5
m
 
6
m
 
7
m
 
8
m
 
9
m
 
1
0
m
 
2
0
m
 
3
0
m
 
1
h
 
2
h
）
从
第
3
级
开
始
重
试
，
每
试
一
次
如
果
还
不
成
功
则
延
迟
等
级
加
1
。
比
如
：
一
条
消
息
消
费
失
败
，
等
待
1
0
s
(
第
3
级
)
进
行
重
试
，
如
果
还
没
有
被
成
功
消
费
则
延
迟
等
级
加
1
，
即
按
第
4
级
别
延
迟
等
待
，
等
3
0
s
继
续
进
行
重
试
，
如
此
进
行
下
去
，
直
到
重
试
1
6
次
。
当
重
试
了
1
6
次
还
未
被
成
功
消
费
将
会
投
递
到
死
信
队
列
，
到
达
死
信
队
列
的
消
息
将
不
再
被
消
费
。
实
际
生
产
中
的
处
理
策
略
是
什
么
呢
？
实
际
生
产
中
不
会
让
消
息
重
试
这
么
多
次
，
通
常
在
重
试
一
定
的
次
数
后
将
消
息
写
入
数
据
库
，
由
另
外
单
独
的
程
序
或
人
工
去
处
理
。
项
目
使
用
的
S
p
r
i
n
g
整
合
R
o
c
k
e
t
M
Q
的
方
式
，
消
费
者
实
现
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
的
o
n
M
e
s
s
a
g
e
方
法
，
在
此
方
法
中
实
现
处
理
策
略
的
示
例
代
码
如
下
：
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
 
C
o
n
s
u
m
e
r
S
i
m
p
l
e
 
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
 
 
 
 
 
 
 
 
 
/
/
取
出
当
前
重
试
次
数
 
 
 
 
 
 
 
 
 
i
n
t
 
r
e
c
o
n
s
u
m
e
T
i
m
e
s
 
=
 
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
R
e
c
o
n
s
u
m
e
T
i
m
e
s
(
)
;
 
 
 
 
 
 
 
 
 
/
/
当
大
于
一
定
的
次
数
后
将
消
息
写
入
数
据
库
，
由
单
独
的
程
序
或
人
工
去
处
理
 
 
 
 
 
 
 
 
i
f
(
r
e
c
o
n
s
u
m
e
T
i
m
e
s
 
>
=
2
)
{
 
 
 
 
 
 
 
 
 
 
 
 
/
/
将
消
息
写
入
数
据
库
，
之
后
正
常
返
回
 
 
 
 
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
;
 
 
 
 
 
 
 
 
}
 
 
 
 
 
 
 
 
 
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
第
%
s
次
处
理
失
败
.
.
"
,
r
e
c
o
n
s
u
m
e
T
i
m
e
s
)
)
;
 
 
 
 
 
}
 
}
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 23 -->
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
