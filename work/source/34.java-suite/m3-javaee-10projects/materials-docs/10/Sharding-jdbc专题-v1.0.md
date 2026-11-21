# Sharding-jdbc专题-v1.0

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\扩展 分库分表\讲义-pdf\Sharding-jdbc专题-v1.0【海量资源尽在 666java.com】.pdf
- 页数：41
- 抽取：pypdf 文本层



<!-- page 1 -->
S
h
a
r
d
i
n
g
-
J
D
B
C
分
库
分
表
专
题
 
 
1
.
概
述
 
1
.
1
.
分
库
分
表
是
什
么
 
 
 
小
明
是
一
家
初
创
电
商
平
台
的
开
发
人
员
，
他
负
责
卖
家
模
块
的
功
能
开
发
，
其
中
涉
及
了
店
铺
、
商
品
的
相
关
业
务
，
设
计
如
下
数
据
库
：
 
 
 
通
过
以
下
S
Q
L
能
够
获
取
到
商
品
相
关
的
店
铺
信
息
、
地
理
区
域
信
息
：
 
形
成
类
似
以
下
列
表
展
示
：
S
E
L
E
C
T
 
p
.
*
,
r
.
[
地
理
区
域
名
称
]
,
s
.
[
店
铺
名
称
]
,
s
.
[
信
誉
]
F
R
O
M
 
[
商
品
信
息
]
 
p
 
L
E
F
T
 
J
O
I
N
 
[
地
理
区
域
]
 
r
 
O
N
 
p
.
[
产
地
]
 
=
 
r
.
[
地
理
区
域
编
码
]
L
E
F
T
 
J
O
I
N
 
[
店
铺
信
息
]
 
s
 
O
N
 
p
.
i
d
 
=
 
s
.
[
所
属
店
铺
]
W
H
E
R
E
 
p
.
i
d
 
=
 
?
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
随
着
公
司
业
务
快
速
发
展
，
数
据
库
中
的
数
据
量
猛
增
，
访
问
性
能
也
变
慢
了
，
优
化
迫
在
眉
睫
。
分
析
一
下
问
题
出
现
在
哪
儿
呢
？
 
关
系
型
数
据
库
本
身
比
较
容
易
成
为
系
统
瓶
颈
，
单
机
存
储
容
量
、
连
接
数
、
处
理
能
力
都
有
限
。
当
单
表
的
数
据
量
达
到
1
0
0
0
W
或
1
0
0
G
以
后
，
由
于
查
询
维
度
较
多
，
即
使
添
加
从
库
、
优
化
索
引
，
做
很
多
操
作
时
性
能
仍
下
降
严
重
。
 
 
方
案
1
：
 
 
通
过
提
升
服
务
器
硬
件
能
力
来
提
高
数
据
处
理
能
力
，
比
如
增
加
存
储
容
量
 
、
C
P
U
等
，
这
种
方
案
成
本
很
高
，
并
且
如
果
瓶
颈
在
M
y
S
Q
L
本
身
那
么
提
高
硬
件
也
是
有
很
的
。
 
 
方
案
2
：
 
 
把
数
据
分
散
在
不
同
的
数
据
库
中
，
使
得
单
一
数
据
库
的
数
据
量
变
小
来
缓
解
单
一
数
据
库
的
性
能
问
题
，
从
而
达
到
提
升
数
据
库
性
能
的
目
的
，
如
下
图
：
将
电
商
数
据
库
拆
分
为
若
干
独
立
的
数
据
库
，
并
且
对
于
大
表
也
拆
分
为
若
干
小
表
，
通
过
这
种
数
据
库
拆
分
的
方
法
来
解
决
数
据
库
的
性
能
问
题
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
分
库
分
表
就
是
为
了
解
决
由
于
数
据
量
过
大
而
导
致
数
据
库
性
能
降
低
的
问
题
，
将
原
来
独
立
的
数
据
库
拆
分
成
若
干
数
据
库
组
成
，
将
数
据
大
表
拆
分
成
若
干
数
据
表
组
成
，
使
得
单
一
数
据
库
、
单
一
数
据
表
的
数
据
量
变
小
，
从
而
达
到
提
升
数
据
库
性
能
的
目
的
。
 
1
.
2
.
分
库
分
表
的
方
式
 
 
 
分
库
分
表
包
括
分
库
和
分
表
两
个
部
分
，
在
生
产
中
通
常
包
括
：
垂
直
分
库
、
水
平
分
库
、
垂
直
分
表
、
水
平
分
表
四
种
方
式
。
1
.
2
.
1
.
垂
直
分
表
 
 
 
下
边
通
过
一
个
商
品
查
询
的
案
例
讲
解
垂
直
分
表
：
 
 
通
常
在
商
品
列
表
中
是
不
显
示
商
品
详
情
信
息
的
，
如
下
图
：
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
用
户
在
浏
览
商
品
列
表
时
，
只
有
对
某
商
品
感
兴
趣
时
才
会
查
看
该
商
品
的
详
细
描
述
。
因
此
，
商
品
信
息
中
商
品
描
述
字
段
访
问
频
次
较
低
，
且
该
字
段
存
储
占
用
空
间
较
大
，
访
问
单
个
数
据
I
O
时
间
较
长
；
商
品
信
息
中
商
品
名
称
、
商
品
图
片
、
商
品
价
格
等
其
他
字
段
数
据
访
问
频
次
较
高
。
 
 
由
于
这
两
种
数
据
的
特
性
不
一
样
，
因
此
他
考
虑
将
商
品
信
息
表
拆
分
如
下
：
 
 
将
访
问
频
次
低
的
商
品
描
述
信
息
单
独
存
放
在
一
张
表
中
，
访
问
频
次
较
高
的
商
品
基
本
信
息
单
独
放
在
一
张
表
中
。
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
商
品
列
表
可
采
用
以
下
s
q
l
：
 
需
要
获
取
商
品
描
述
时
，
再
通
过
以
下
s
q
l
获
取
：
 
小
明
进
行
的
这
一
步
优
化
，
就
叫
垂
直
分
表
。
垂
直
分
表
定
义
：
将
一
个
表
按
照
字
段
分
成
多
表
，
每
个
表
存
储
其
中
一
部
分
字
段
。
 
它
带
来
的
提
升
是
：
1
.
为
了
避
免
I
O
争
抢
并
减
少
锁
表
的
几
率
，
查
看
详
情
的
用
户
与
商
品
信
息
浏
览
互
不
影
响
2
.
充
分
发
挥
热
门
数
据
的
操
作
效
率
，
商
品
信
息
的
操
作
的
高
效
率
不
会
被
商
品
描
述
的
低
效
率
所
拖
累
。
 
 
一
般
来
说
，
某
业
务
实
体
中
的
各
个
数
据
项
的
访
问
频
次
是
不
一
样
的
，
部
分
数
据
项
可
能
是
占
用
存
储
空
间
比
较
大
的
B
L
O
B
或
是
T
E
X
T
。
例
如
上
例
中
的
商
品
描
述
。
所
以
，
当
表
数
据
量
很
大
时
，
可
以
将
表
按
字
段
切
开
，
将
热
门
字
段
、
冷
门
字
段
分
开
放
置
在
不
同
库
中
，
这
些
库
可
以
放
在
不
同
的
存
储
设
备
上
，
避
免
I
O
争
抢
。
垂
直
切
分
带
来
的
性
能
提
升
主
要
集
中
在
热
门
数
据
的
操
作
效
率
上
，
而
且
磁
盘
争
用
情
况
减
少
。
通
常
我
们
按
以
下
原
则
进
行
垂
直
拆
分
:
1
.
 
把
不
常
用
的
字
段
单
独
放
在
一
张
表
;
2
.
 
把
t
e
x
t
，
b
l
o
b
等
大
字
段
拆
分
出
来
放
在
附
表
中
;
3
.
 
经
常
组
合
查
询
的
列
放
在
一
张
表
中
;
 
1
.
2
.
2
.
垂
直
分
库
 
 
 
通
过
垂
直
分
表
性
能
得
到
了
一
定
程
度
的
提
升
，
但
是
还
没
有
达
到
要
求
，
并
且
磁
盘
空
间
也
快
不
够
了
，
因
为
数
据
还
是
始
终
限
制
在
一
台
服
务
器
，
库
内
垂
直
分
表
只
解
决
了
单
一
表
数
据
量
过
大
的
问
题
，
但
没
有
将
表
分
布
到
不
同
的
服
务
器
上
，
因
此
每
个
表
还
是
竞
争
同
一
个
物
理
机
的
C
P
U
、
内
存
、
网
络
I
O
、
磁
盘
。
 
 
经
过
思
考
，
他
把
原
有
的
S
E
L
L
E
R
_
D
B
(
卖
家
库
)
，
分
为
了
P
R
O
D
U
C
T
_
D
B
(
商
品
库
)
和
S
T
O
R
E
_
D
B
(
店
铺
库
)
，
并
把
这
两
个
库
分
散
到
不
同
服
务
器
，
如
下
图
：
 
S
E
L
E
C
T
 
p
.
*
,
r
.
[
地
理
区
域
名
称
]
,
s
.
[
店
铺
名
称
]
,
s
.
[
信
誉
]
F
R
O
M
 
[
商
品
信
息
]
 
p
 
L
E
F
T
 
J
O
I
N
 
[
地
理
区
域
]
 
r
 
O
N
 
p
.
[
产
地
]
 
=
 
r
.
[
地
理
区
域
编
码
]
L
E
F
T
 
J
O
I
N
 
[
店
铺
信
息
]
 
s
 
O
N
 
p
.
i
d
 
=
 
s
.
[
所
属
店
铺
]
W
H
E
R
E
.
.
.
O
R
D
E
R
 
B
Y
.
.
.
L
I
M
I
T
.
.
.
S
E
L
E
C
T
 
*
F
R
O
M
 
[
商
品
描
述
]
 
W
H
E
R
E
 
[
商
品
I
D
]
 
=
 
?
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
由
于
商
品
信
息
与
商
品
描
述
业
务
耦
合
度
较
高
，
因
此
一
起
被
存
放
在
P
R
O
D
U
C
T
_
D
B
(
商
品
库
)
；
而
店
铺
信
息
相
对
独
立
，
因
此
单
独
被
存
放
在
S
T
O
R
E
_
D
B
(
店
铺
库
)
。
 
 
小
明
进
行
的
这
一
步
优
化
，
就
叫
垂
直
分
库
。
 
 
垂
直
分
库
是
指
按
照
业
务
将
表
进
行
分
类
，
分
布
到
不
同
的
数
据
库
上
面
，
每
个
库
可
以
放
在
不
同
的
服
务
器
上
，
它
的
核
心
理
念
是
专
库
专
用
。
它
带
来
的
提
升
是
：
解
决
业
务
层
面
的
耦
合
，
业
务
清
晰
能
对
不
同
业
务
的
数
据
进
行
分
级
管
理
、
维
护
、
监
控
、
扩
展
等
高
并
发
场
景
下
，
垂
直
分
库
一
定
程
度
的
提
升
I
O
、
数
据
库
连
接
数
、
降
低
单
机
硬
件
资
源
的
瓶
颈
 
 
垂
直
分
库
通
过
将
表
按
业
务
分
类
，
然
后
分
布
在
不
同
数
据
库
，
并
且
可
以
将
这
些
数
据
库
部
署
在
不
同
服
务
器
上
，
从
而
达
到
多
个
服
务
器
共
同
分
摊
压
力
的
效
果
，
但
是
依
然
没
有
解
决
单
表
数
据
量
过
大
的
问
题
。
 
1
.
2
.
3
.
水
平
分
库
 
 
 
经
过
垂
直
分
库
后
，
数
据
库
性
能
问
题
得
到
一
定
程
度
的
解
决
，
但
是
随
着
业
务
量
的
增
长
，
P
R
O
D
U
C
T
_
D
B
(
商
品
库
)
单
库
存
储
数
据
已
经
超
出
预
估
。
粗
略
估
计
，
目
前
有
8
w
店
铺
，
每
个
店
铺
平
均
1
5
0
个
不
同
规
格
的
商
品
，
再
算
上
增
长
，
那
商
品
数
量
得
往
1
5
0
0
w
+
上
预
估
，
并
且
P
R
O
D
U
C
T
_
D
B
(
商
品
库
)
属
于
访
问
非
常
频
繁
的
资
源
，
单
台
服
务
器
已
经
无
法
支
撑
。
此
时
该
如
何
优
化
？
 
 
再
次
分
库
？
但
是
从
业
务
角
度
分
析
，
目
前
情
况
已
经
无
法
再
次
垂
直
分
库
。
 
 
尝
试
水
平
分
库
，
将
店
铺
I
D
为
单
数
的
和
店
铺
I
D
为
双
数
的
商
品
信
息
分
别
放
在
两
个
库
中
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
也
就
是
说
，
要
操
作
某
条
数
据
，
先
分
析
这
条
数
据
所
属
的
店
铺
I
D
。
如
果
店
铺
I
D
为
双
数
，
将
此
操
作
映
射
至
R
R
O
D
U
C
T
_
D
B
1
(
商
品
库
1
)
；
如
果
店
铺
I
D
为
单
数
，
将
操
作
映
射
至
R
R
O
D
U
C
T
_
D
B
2
(
商
品
库
2
)
。
此
操
作
要
访
问
数
据
库
名
称
的
表
达
式
为
R
R
O
D
U
C
T
_
D
B
[
店
铺
I
D
%
2
 
+
 
1
]
 
。
 
 
小
明
进
行
的
这
一
步
优
化
，
就
叫
水
平
分
库
。
 
 
水
平
分
库
是
把
同
一
个
表
的
数
据
按
一
定
规
则
拆
到
不
同
的
数
据
库
中
，
每
个
库
可
以
放
在
不
同
的
服
务
器
上
。
 
它
带
来
的
提
升
是
：
解
决
了
单
库
大
数
据
，
高
并
发
的
性
能
瓶
颈
。
提
高
了
系
统
的
稳
定
性
及
可
用
性
。
 
 
 
当
一
个
应
用
难
以
再
细
粒
度
的
垂
直
切
分
，
或
切
分
后
数
据
量
行
数
巨
大
，
存
在
单
库
读
写
、
存
储
性
能
瓶
颈
，
这
时
候
就
需
要
进
行
水
平
分
库
了
，
经
过
水
平
切
分
的
优
化
，
往
往
能
解
决
单
库
存
储
量
及
性
能
瓶
颈
。
但
由
于
同
一
个
表
被
分
配
在
不
同
的
数
据
库
，
需
要
额
外
进
行
数
据
操
作
的
路
由
工
作
，
因
此
大
大
提
升
了
系
统
复
杂
度
。
 
 
1
.
2
.
4
.
水
平
分
表
 
 
 
按
照
水
平
分
库
的
思
路
对
他
把
P
R
O
D
U
C
T
_
D
B
_
X
(
商
品
库
)
内
的
表
也
可
以
进
行
水
平
拆
分
，
其
目
的
也
是
为
解
决
单
表
数
据
量
大
的
问
题
，
如
下
图
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
与
水
平
分
库
的
思
路
类
似
，
不
过
这
次
操
作
的
目
标
是
表
，
商
品
信
息
及
商
品
描
述
被
分
成
了
两
套
表
。
如
果
商
品
I
D
为
双
数
，
将
此
操
作
映
射
至
商
品
信
息
1
表
；
如
果
商
品
I
D
为
单
数
，
将
操
作
映
射
至
商
品
信
息
2
表
。
此
操
作
要
访
问
表
名
称
的
表
达
式
为
商
品
信
息
[
商
品
I
D
%
2
 
+
 
1
]
 
。
 
 
小
明
进
行
的
这
一
步
优
化
，
就
叫
水
平
分
表
。
 
 
水
平
分
表
是
在
同
一
个
数
据
库
内
，
把
同
一
个
表
的
数
据
按
一
定
规
则
拆
到
多
个
表
中
。
 
它
带
来
的
提
升
是
：
优
化
单
一
表
数
据
量
过
大
而
产
生
的
性
能
问
题
避
免
I
O
争
抢
并
减
少
锁
表
的
几
率
 
 
库
内
的
水
平
分
表
，
解
决
了
单
一
表
数
据
量
过
大
的
问
题
，
分
出
来
的
小
表
中
只
包
含
一
部
分
数
据
，
从
而
使
得
单
个
表
的
数
据
量
变
小
，
提
高
检
索
性
能
。
1
.
2
.
5
 
小
结
 
本
章
介
绍
了
分
库
分
表
的
各
种
方
式
，
它
们
分
别
是
垂
直
分
表
、
垂
直
分
库
、
水
平
分
库
和
水
平
分
表
：
垂
直
分
表
：
可
以
把
一
个
宽
表
的
字
段
按
访
问
频
次
、
是
否
是
大
字
段
的
原
则
拆
分
为
多
个
表
，
这
样
既
能
使
业
务
清
晰
，
还
能
提
升
部
分
性
能
。
拆
分
后
，
尽
量
从
业
务
角
度
避
免
联
查
，
否
则
性
能
方
面
将
得
不
偿
失
。
垂
直
分
库
：
可
以
把
多
个
表
按
业
务
耦
合
松
紧
归
类
，
分
别
存
放
在
不
同
的
库
，
这
些
库
可
以
分
布
在
不
同
服
务
器
，
从
而
使
访
问
压
力
被
多
服
务
器
负
载
，
大
大
提
升
性
能
，
同
时
能
提
高
整
体
架
构
的
业
务
清
晰
度
，
不
同
的
业
务
库
可
根
据
自
身
情
况
定
制
优
化
方
案
。
但
是
它
需
要
解
决
跨
库
带
来
的
所
有
复
杂
问
题
。
水
平
分
库
：
可
以
把
一
个
表
的
数
据
(
按
数
据
行
)
分
到
多
个
不
同
的
库
，
每
个
库
只
有
这
个
表
的
部
分
数
据
，
这
些
库
可
以
分
布
在
不
同
服
务
器
，
从
而
使
访
问
压
力
被
多
服
务
器
负
载
，
大
大
提
升
性
能
。
它
不
仅
需
要
解
决
跨
库
带
来
的
所
有
复
杂
问
题
，
还
要
解
决
数
据
路
由
的
问
题
(
数
据
路
由
问
题
后
边
介
绍
)
。
水
平
分
表
：
可
以
把
一
个
表
的
数
据
(
按
数
据
行
)
分
到
多
个
同
一
个
数
据
库
的
多
张
表
中
，
每
个
表
只
有
这
个
表
的
部
分
数
据
，
这
样
做
能
小
幅
提
升
性
能
，
它
仅
仅
作
为
水
平
分
库
的
一
个
补
充
优
化
。
一
般
来
说
，
在
系
统
设
计
阶
段
就
应
该
根
据
业
务
耦
合
松
紧
来
确
定
垂
直
分
库
，
垂
直
分
表
方
案
，
在
数
据
量
及
访
问
压
力
不
是
特
别
大
的
情
况
，
首
先
考
虑
缓
存
、
读
写
分
离
、
索
引
技
术
等
方
案
。
若
数
据
量
极
大
，
且
持
续
增
长
，
再
考
虑
水
平
分
库
水
平
分
表
方
案
。
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
1
.
3
.
分
库
分
表
带
来
的
问
题
 
 
 
分
库
分
表
能
有
效
的
缓
解
了
单
机
和
单
库
带
来
的
性
能
瓶
颈
和
压
力
，
突
破
网
络
I
O
、
硬
件
资
源
、
连
接
数
的
瓶
颈
，
同
时
也
带
来
了
一
些
问
题
。
1
.
3
.
1
.
事
务
一
致
性
问
题
 
 
 
由
于
分
库
分
表
把
数
据
分
布
在
不
同
库
甚
至
不
同
服
务
器
，
不
可
避
免
会
带
来
分
布
式
事
务
问
题
。
1
.
3
.
2
.
跨
节
点
关
联
查
询
 
在
没
有
分
库
前
，
我
们
检
索
商
品
时
可
以
通
过
以
下
S
Q
L
对
店
铺
信
息
进
行
关
联
查
询
：
 
但
垂
直
分
库
后
[
商
品
信
息
]
和
[
店
铺
信
息
]
不
在
一
个
数
据
库
，
甚
至
不
在
一
台
服
务
器
，
无
法
进
行
关
联
查
询
。
可
将
原
关
联
查
询
分
为
两
次
查
询
，
第
一
次
查
询
的
结
果
集
中
找
出
关
联
数
据
i
d
，
然
后
根
据
i
d
发
起
第
二
次
请
求
得
到
关
联
数
据
，
最
后
将
获
得
到
的
数
据
进
行
拼
装
。
 
1
.
3
.
3
.
跨
节
点
分
页
、
排
序
函
数
 
 
 
跨
节
点
多
库
进
行
查
询
时
，
l
i
m
i
t
分
页
、
o
r
d
e
r
 
b
y
排
序
等
问
题
，
就
变
得
比
较
复
杂
了
。
需
要
先
在
不
同
的
分
片
节
点
中
将
数
据
进
行
排
序
并
返
回
，
然
后
将
不
同
分
片
返
回
的
结
果
集
进
行
汇
总
和
再
次
排
序
。
 
 
如
，
进
行
水
平
分
库
后
的
商
品
库
，
按
I
D
倒
序
排
序
分
页
，
取
第
一
页
：
S
E
L
E
C
T
 
p
.
*
,
r
.
[
地
理
区
域
名
称
]
,
s
.
[
店
铺
名
称
]
,
s
.
[
信
誉
]
F
R
O
M
 
[
商
品
信
息
]
 
p
 
L
E
F
T
 
J
O
I
N
 
[
地
理
区
域
]
 
r
 
O
N
 
p
.
[
产
地
]
 
=
 
r
.
[
地
理
区
域
编
码
]
L
E
F
T
 
J
O
I
N
 
[
店
铺
信
息
]
 
s
 
O
N
 
p
.
i
d
 
=
 
s
.
[
所
属
店
铺
]
W
H
E
R
E
.
.
.
O
R
D
E
R
 
B
Y
.
.
.
L
I
M
I
T
.
.
.
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
以
上
流
程
是
取
第
一
页
的
数
据
，
性
能
影
响
不
大
，
但
由
于
商
品
信
息
的
分
布
在
各
数
据
库
的
数
据
可
能
是
随
机
的
，
如
果
是
取
第
N
页
，
需
要
将
所
有
节
点
前
N
页
数
据
都
取
出
来
合
并
，
再
进
行
整
体
的
排
序
，
操
作
效
率
可
想
而
知
。
所
以
请
求
页
数
越
大
，
系
统
的
性
能
也
会
越
差
。
 
 
在
使
用
M
a
x
、
M
i
n
、
S
u
m
、
C
o
u
n
t
之
类
的
函
数
进
行
计
算
的
时
候
，
与
排
序
分
页
同
理
，
也
需
要
先
在
每
个
分
片
上
执
行
相
应
的
函
数
，
然
后
将
各
个
分
片
的
结
果
集
进
行
汇
总
和
再
次
计
算
，
最
终
将
结
果
返
回
。
 
1
.
3
.
4
.
主
键
避
重
 
 
 
在
分
库
分
表
环
境
中
，
由
于
表
中
数
据
同
时
存
在
不
同
数
据
库
中
，
主
键
值
平
时
使
用
的
自
增
长
将
无
用
武
之
地
，
某
个
分
区
数
据
库
生
成
的
I
D
无
法
保
证
全
局
唯
一
。
因
此
需
要
单
独
设
计
全
局
主
键
，
以
避
免
跨
库
主
键
重
复
问
题
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
1
.
3
.
5
.
公
共
表
 
 
 
实
际
的
应
用
场
景
中
，
参
数
表
、
数
据
字
典
表
等
都
是
数
据
量
较
小
，
变
动
少
，
而
且
属
于
高
频
联
合
查
询
的
依
赖
表
。
例
子
中
地
理
区
域
表
也
属
于
此
类
型
。
 
 
可
以
将
这
类
表
在
每
个
数
据
库
都
保
存
一
份
，
所
有
对
公
共
表
的
更
新
操
作
都
同
时
发
送
到
所
有
分
库
执
行
。
 
 
由
于
分
库
分
表
之
后
，
数
据
被
分
散
在
不
同
的
数
据
库
、
服
务
器
。
因
此
，
对
数
据
的
操
作
也
就
无
法
通
过
常
规
方
式
完
成
，
并
且
它
还
带
来
了
一
系
列
的
问
题
。
好
在
，
这
些
问
题
不
是
所
有
都
需
要
我
们
在
应
用
层
面
上
解
决
，
市
面
上
有
很
多
中
间
件
可
供
我
们
选
择
，
其
中
S
h
a
r
d
i
n
g
-
J
D
B
C
使
用
流
行
度
较
高
，
我
们
来
了
解
一
下
它
。
 
1
.
4
 
S
h
a
r
d
i
n
g
-
J
D
B
C
介
绍
 
1
.
4
.
1
 
S
h
a
r
d
i
n
g
-
J
D
B
C
介
绍
 
 
 
S
h
a
r
d
i
n
g
-
J
D
B
C
是
当
当
网
研
发
的
开
源
分
布
式
数
据
库
中
间
件
，
从
 
3
.
0
 
开
始
S
h
a
r
d
i
n
g
-
J
D
B
C
被
包
含
在
 
S
h
a
r
d
i
n
g
-
S
p
h
e
r
e
中
，
之
后
该
项
目
进
入
进
入
A
p
a
c
h
e
孵
化
器
，
4
.
0
版
本
之
后
的
版
本
为
A
p
a
c
h
e
版
本
。
 
 
S
h
a
r
d
i
n
g
S
p
h
e
r
e
是
一
套
开
源
的
分
布
式
数
据
库
中
间
件
解
决
方
案
组
成
的
生
态
圈
，
它
由
S
h
a
r
d
i
n
g
-
J
D
B
C
、
S
h
a
r
d
i
n
g
-
P
r
o
x
y
和
S
h
a
r
d
i
n
g
-
S
i
d
e
c
a
r
（
计
划
中
）
这
3
款
相
互
独
立
的
产
品
组
成
。
 
他
们
均
提
供
标
准
化
的
数
据
分
片
、
分
布
式
事
务
和
数
据
库
治
理
功
能
，
可
适
用
于
如
J
a
v
a
同
构
、
异
构
语
言
、
容
器
、
云
原
生
等
各
种
多
样
化
的
应
用
场
景
。
官
方
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
h
a
r
d
i
n
g
s
p
h
e
r
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
o
c
u
m
e
n
t
/
c
u
r
r
e
n
t
/
c
n
/
o
v
e
r
v
i
e
w
/
 
 
咱
们
目
前
只
需
关
注
S
h
a
r
d
i
n
g
-
J
D
B
C
，
它
定
位
为
轻
量
级
J
a
v
a
框
架
，
在
J
a
v
a
的
J
D
B
C
层
提
供
的
额
外
服
务
。
 
它
使
用
客
户
端
直
连
数
据
库
，
以
j
a
r
包
形
式
提
供
服
务
，
无
需
额
外
部
署
和
依
赖
，
可
理
解
为
增
强
版
的
J
D
B
C
驱
动
，
完
全
兼
容
J
D
B
C
和
各
种
O
R
M
框
架
。
 
 
S
h
a
r
d
i
n
g
-
J
D
B
C
的
核
心
功
能
为
数
据
分
片
和
读
写
分
离
，
通
过
S
h
a
r
d
i
n
g
-
J
D
B
C
，
应
用
可
以
透
明
的
使
用
j
d
b
c
访
问
已
经
分
库
分
表
、
读
写
分
离
的
多
个
数
据
源
，
而
不
用
关
心
数
据
源
的
数
量
以
及
数
据
如
何
分
布
。
适
用
于
任
何
基
于
J
a
v
a
的
O
R
M
框
架
，
如
：
 
H
i
b
e
r
n
a
t
e
,
 
M
y
b
a
t
i
s
,
 
S
p
r
i
n
g
 
J
D
B
C
 
T
e
m
p
l
a
t
e
或
直
接
使
用
J
D
B
C
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
基
于
任
何
第
三
方
的
数
据
库
连
接
池
，
如
：
D
B
C
P
,
 
C
3
P
0
,
 
B
o
n
e
C
P
,
 
D
r
u
i
d
,
 
H
i
k
a
r
i
C
P
等
。
支
持
任
意
实
现
J
D
B
C
规
范
的
数
据
库
。
目
前
支
持
M
y
S
Q
L
，
O
r
a
c
l
e
，
S
Q
L
S
e
r
v
e
r
和
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
。
上
图
展
示
了
S
h
a
r
d
i
n
g
-
J
d
b
c
的
工
作
方
式
，
使
用
S
h
a
r
d
i
n
g
-
J
d
b
c
前
需
要
人
工
对
数
据
库
进
行
分
库
分
表
，
在
应
用
程
序
中
加
入
S
h
a
r
d
i
n
g
-
J
d
b
c
的
J
a
r
包
，
应
用
程
序
通
过
S
h
a
r
d
i
n
g
-
J
d
b
c
操
作
分
库
分
表
后
的
数
据
库
和
数
据
表
，
由
于
S
h
a
r
d
i
n
g
-
J
d
b
c
是
对
J
d
b
c
驱
动
的
增
强
，
使
用
S
h
a
r
d
i
n
g
-
J
d
b
c
就
像
使
用
J
d
b
c
驱
动
一
样
，
在
应
用
程
序
中
是
无
需
指
定
具
体
要
操
作
的
分
库
和
分
表
的
。
1
.
4
.
2
 
与
j
d
b
c
性
能
对
比
 
1
.
 
性
能
损
耗
测
试
：
服
务
器
资
源
充
足
、
并
发
数
相
同
，
比
较
J
D
B
C
和
S
h
a
r
d
i
n
g
-
J
D
B
C
性
能
损
耗
，
S
h
a
r
d
i
n
g
-
J
D
B
C
相
对
J
D
B
C
损
耗
不
超
过
7
%
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
2
.
 
性
能
对
比
测
试
：
服
务
器
资
源
使
用
到
极
限
，
相
同
的
场
景
J
D
B
C
与
S
h
a
r
d
i
n
g
-
J
D
B
C
的
吞
吐
量
相
当
。
3
.
 
性
能
对
比
测
试
：
服
务
器
资
源
使
用
到
极
限
，
S
h
a
r
d
i
n
g
-
J
D
B
C
采
用
分
库
分
表
后
，
S
h
a
r
d
i
n
g
-
J
D
B
C
吞
吐
量
较
J
D
B
C
不
分
表
有
接
近
2
倍
的
提
升
。
 
2
.
S
h
a
r
d
i
n
g
-
J
D
B
C
快
速
入
门
 
2
.
1
 
需
求
说
明
 
本
章
节
使
用
S
h
a
r
d
i
n
g
-
J
D
B
C
完
成
对
订
单
表
的
水
平
分
表
，
通
过
快
速
入
门
程
序
的
开
发
，
快
速
体
验
S
h
a
r
d
i
n
g
-
J
D
B
C
的
使
用
方
法
。
人
工
创
建
两
张
表
，
t
_
o
r
d
e
r
_
1
和
t
_
o
r
d
e
r
_
2
，
这
两
张
表
是
订
单
表
拆
分
后
的
表
，
通
过
S
h
a
r
d
i
n
g
-
J
d
b
c
向
订
单
表
插
入
数
据
，
按
照
一
定
的
分
片
规
则
，
主
键
为
偶
数
的
进
入
t
_
o
r
d
e
r
_
1
，
另
一
部
分
数
据
进
入
t
_
o
r
d
e
r
_
2
，
通
过
S
h
a
r
d
i
n
g
-
J
d
b
c
 
查
询
数
据
，
根
据
 
S
Q
L
语
句
的
内
容
从
t
_
o
r
d
e
r
_
1
或
t
_
o
r
d
e
r
_
2
查
询
数
据
。
2
.
2
.
环
境
搭
建
 
2
.
2
.
1
 
环
境
说
明
 
操
作
系
统
：
W
i
n
1
0
数
据
库
：
M
y
S
Q
L
-
5
.
7
.
2
5
J
D
K
：
6
4
位
 
j
d
k
1
.
8
.
0
_
2
0
1
应
用
框
架
：
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
，
M
y
b
a
t
i
s
3
.
5
.
0
S
h
a
r
d
i
n
g
-
J
D
B
C
：
s
h
a
r
d
i
n
g
-
j
d
b
c
-
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
4
.
0
.
0
-
R
C
1
2
.
2
.
2
 
创
建
数
据
库
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 14 -->
创
建
订
单
库
o
r
d
e
r
_
d
b
 
在
o
r
d
e
r
_
d
b
中
创
建
t
_
o
r
d
e
r
_
1
、
t
_
o
r
d
e
r
_
2
表
 
2
.
2
.
3
.
引
入
m
a
v
e
n
依
赖
 
引
入
 
s
h
a
r
d
i
n
g
-
j
d
b
c
和
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
整
合
的
J
a
r
包
：
 
具
体
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
相
关
依
赖
及
配
置
请
参
考
资
料
中
d
b
s
h
a
r
d
i
n
g
/
s
h
a
r
d
i
n
g
-
j
d
b
c
-
s
i
m
p
l
e
工
程
，
本
指
引
只
说
明
与
S
h
a
r
d
i
n
g
-
J
D
B
C
相
关
的
内
容
。
 
2
.
3
 
编
写
程
序
 
2
.
3
.
1
 
分
片
规
则
配
置
 
分
片
规
则
配
置
是
s
h
a
r
d
i
n
g
-
j
d
b
c
进
行
对
分
库
分
表
操
作
的
重
要
依
据
，
配
置
内
容
包
括
：
数
据
源
、
主
键
生
成
策
略
、
分
片
策
略
等
。
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
中
配
置
 
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
o
r
d
e
r
_
d
b
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
D
R
O
P
 
T
A
B
L
E
 
I
F
 
E
X
I
S
T
S
 
`
t
_
o
r
d
e
r
_
1
`
;
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
_
o
r
d
e
r
_
1
`
 
 
(
 
 
`
o
r
d
e
r
_
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
 
C
O
M
M
E
N
T
 
'
订
单
i
d
'
,
 
 
`
p
r
i
c
e
`
 
d
e
c
i
m
a
l
(
1
0
,
 
2
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
订
单
价
格
'
,
 
 
`
u
s
e
r
_
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
 
C
O
M
M
E
N
T
 
'
下
单
用
户
i
d
'
,
 
 
`
s
t
a
t
u
s
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
 
u
t
f
8
 
C
O
L
L
A
T
E
 
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
订
单
状
态
'
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
o
r
d
e
r
_
i
d
`
)
 
U
S
I
N
G
 
B
T
R
E
E
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
 
=
 
u
t
f
8
 
C
O
L
L
A
T
E
 
=
 
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
 
R
O
W
_
F
O
R
M
A
T
 
=
 
D
y
n
a
m
i
c
;
 
D
R
O
P
 
T
A
B
L
E
 
I
F
 
E
X
I
S
T
S
 
`
t
_
o
r
d
e
r
_
2
`
;
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
_
o
r
d
e
r
_
2
`
 
 
(
 
 
`
o
r
d
e
r
_
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
 
C
O
M
M
E
N
T
 
'
订
单
i
d
'
,
 
 
`
p
r
i
c
e
`
 
d
e
c
i
m
a
l
(
1
0
,
 
2
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
订
单
价
格
'
,
 
 
`
u
s
e
r
_
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
 
C
O
M
M
E
N
T
 
'
下
单
用
户
i
d
'
,
 
 
`
s
t
a
t
u
s
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
 
u
t
f
8
 
C
O
L
L
A
T
E
 
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
订
单
状
态
'
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
o
r
d
e
r
_
i
d
`
)
 
U
S
I
N
G
 
B
T
R
E
E
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
 
=
 
u
t
f
8
 
C
O
L
L
A
T
E
 
=
 
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
 
R
O
W
_
F
O
R
M
A
T
 
=
 
D
y
n
a
m
i
c
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
s
h
a
r
d
i
n
g
s
p
h
e
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
s
h
a
r
d
i
n
g
‐
j
d
b
c
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
4
.
0
.
0
‐
R
C
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
8
1
 
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
 
s
h
a
r
d
i
n
g
‐
j
d
b
c
‐
s
i
m
p
l
e
‐
d
e
m
o
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 15 -->
1
.
首
先
定
义
数
据
源
m
1
，
并
对
m
1
进
行
实
际
的
参
数
配
置
。
2
.
指
定
t
_
o
r
d
e
r
表
的
数
据
分
布
情
况
，
他
分
布
在
m
1
.
t
_
o
r
d
e
r
_
1
，
m
1
.
t
_
o
r
d
e
r
_
2
3
.
指
定
t
_
o
r
d
e
r
表
的
主
键
生
成
策
略
为
S
N
O
W
F
L
A
K
E
，
S
N
O
W
F
L
A
K
E
是
一
种
分
布
式
自
增
算
法
，
保
证
i
d
全
局
唯
一
4
.
定
义
t
_
o
r
d
e
r
分
片
策
略
，
o
r
d
e
r
_
i
d
为
偶
数
的
数
据
落
在
t
_
o
r
d
e
r
_
1
，
为
奇
数
的
落
在
t
_
o
r
d
e
r
_
2
，
分
表
策
略
的
表
达
式
为
t
_
o
r
d
e
r
_
$
-
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
}
 
 
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
‐
p
a
t
h
 
=
 
/
s
h
a
r
d
i
n
g
‐
j
d
b
c
‐
s
i
m
p
l
e
‐
d
e
m
o
s
p
r
i
n
g
.
h
t
t
p
.
e
n
c
o
d
i
n
g
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
s
p
r
i
n
g
.
h
t
t
p
.
e
n
c
o
d
i
n
g
.
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
s
p
r
i
n
g
.
h
t
t
p
.
e
n
c
o
d
i
n
g
.
f
o
r
c
e
 
=
 
t
r
u
e
 
s
p
r
i
n
g
.
m
a
i
n
.
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
 
=
 
t
r
u
e
 
m
y
b
a
t
i
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
#
 
以
下
是
分
片
规
则
配
置
#
 
定
义
数
据
源
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
n
a
m
e
s
 
=
 
m
1
 
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
.
t
y
p
e
 
=
 
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
3
3
0
6
/
o
r
d
e
r
_
d
b
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
 
指
定
t
_
o
r
d
e
r
表
的
数
据
分
布
情
况
，
配
置
数
据
节
点
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
a
c
t
u
a
l
‐
d
a
t
a
‐
n
o
d
e
s
 
=
 
m
1
.
t
_
o
r
d
e
r
_
$
‐
>
{
1
.
.
2
}
 
#
 
指
定
t
_
o
r
d
e
r
表
的
主
键
生
成
策
略
为
S
N
O
W
F
L
A
K
E
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
k
e
y
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
.
c
o
l
u
m
n
=
o
r
d
e
r
_
i
d
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
k
e
y
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
.
t
y
p
e
=
S
N
O
W
F
L
A
K
E
 
 
 
#
 
指
定
t
_
o
r
d
e
r
表
的
分
片
策
略
，
分
片
策
略
包
括
分
片
键
和
分
片
算
法
 
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
s
h
a
r
d
i
n
g
‐
c
o
l
u
m
n
 
=
 
o
r
d
e
r
_
i
d
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
a
l
g
o
r
i
t
h
m
‐
e
x
p
r
e
s
s
i
o
n
 
=
 
t
_
o
r
d
e
r
_
$
‐
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
}
 
 
 
 
 
 
 
 
#
 
打
开
s
q
l
输
出
日
志
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
p
r
o
p
s
.
s
q
l
.
s
h
o
w
 
=
 
t
r
u
e
 
s
w
a
g
g
e
r
.
e
n
a
b
l
e
 
=
 
t
r
u
e
 
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
 
=
 
i
n
f
o
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
 
=
 
i
n
f
o
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
d
b
s
h
a
r
d
i
n
g
 
 
=
 
d
e
b
u
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
d
r
u
i
d
.
s
q
l
 
=
 
d
e
b
u
g
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 16 -->
2
.
3
.
2
.
数
据
操
作
 
 
 
2
.
3
.
3
.
测
试
 
编
写
单
元
测
试
：
 
@
M
a
p
p
e
r
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
 
i
n
t
e
r
f
a
c
e
 
O
r
d
e
r
D
a
o
 
{
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
新
增
订
单
 
 
 
 
 
*
 
@
p
a
r
a
m
 
p
r
i
c
e
 
订
单
价
格
 
 
 
 
 
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
I
d
 
用
户
i
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
t
u
s
 
订
单
状
态
 
 
 
 
 
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
I
n
s
e
r
t
(
"
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
 
t
_
o
r
d
e
r
(
p
r
i
c
e
,
u
s
e
r
_
i
d
,
s
t
a
t
u
s
)
 
v
a
l
u
e
(
#
{
p
r
i
c
e
}
,
#
{
u
s
e
r
I
d
}
,
#
{
s
t
a
t
u
s
}
)
"
)
 
 
 
 
i
n
t
 
i
n
s
e
r
t
O
r
d
e
r
(
@
P
a
r
a
m
(
"
p
r
i
c
e
"
)
 
B
i
g
D
e
c
i
m
a
l
 
p
r
i
c
e
,
 
@
P
a
r
a
m
(
"
u
s
e
r
I
d
"
)
L
o
n
g
 
u
s
e
r
I
d
,
 
@
P
a
r
a
m
(
"
s
t
a
t
u
s
"
)
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
u
s
)
;
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
i
d
列
表
查
询
多
个
订
单
 
 
 
 
 
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
I
d
s
 
订
单
i
d
列
表
 
 
 
 
 
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
S
e
l
e
c
t
(
{
"
<
s
c
r
i
p
t
>
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
s
e
l
e
c
t
 
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
 
*
 
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
 
f
r
o
m
 
t
_
o
r
d
e
r
 
t
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
 
w
h
e
r
e
 
t
.
o
r
d
e
r
_
i
d
 
i
n
 
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
<
f
o
r
e
a
c
h
 
c
o
l
l
e
c
t
i
o
n
=
'
o
r
d
e
r
I
d
s
'
 
i
t
e
m
=
'
i
d
'
 
o
p
e
n
=
'
(
'
 
s
e
p
a
r
a
t
o
r
=
'
,
'
 
c
l
o
s
e
=
'
)
'
>
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
 
#
{
i
d
}
 
"
 
+
 
 
 
 
 
 
 
 
 
 
 
 
"
<
/
f
o
r
e
a
c
h
>
"
+
 
 
 
 
 
 
 
 
 
 
 
 
"
<
/
s
c
r
i
p
t
>
"
}
)
 
 
 
 
L
i
s
t
<
M
a
p
>
 
s
e
l
e
c
t
O
r
d
e
r
b
y
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
"
o
r
d
e
r
I
d
s
"
)
L
i
s
t
<
L
o
n
g
>
 
o
r
d
e
r
I
d
s
)
;
 
}
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
(
c
l
a
s
s
e
s
 
=
 
{
S
h
a
r
d
i
n
g
J
d
b
c
S
i
m
p
l
e
D
e
m
o
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
}
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
 
O
r
d
e
r
D
a
o
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
 
O
r
d
e
r
D
a
o
 
o
r
d
e
r
D
a
o
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
O
r
d
e
r
(
)
{
 
 
 
 
 
 
 
 
f
o
r
 
(
i
n
t
 
i
 
=
 
0
 
;
 
i
<
1
0
;
 
i
+
+
)
{
 
 
 
 
 
 
 
 
 
 
 
 
o
r
d
e
r
D
a
o
.
i
n
s
e
r
t
O
r
d
e
r
(
n
e
w
 
B
i
g
D
e
c
i
m
a
l
(
(
i
+
1
)
*
5
)
,
1
L
,
"
W
A
I
T
_
P
A
Y
"
)
;
 
 
 
 
 
 
 
 
}
 
 
 
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 17 -->
执
行
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
O
r
d
e
r
：
通
过
日
志
可
以
发
现
o
r
d
e
r
_
i
d
为
奇
数
的
被
插
入
到
t
_
o
r
d
e
r
_
2
表
，
为
偶
数
的
被
插
入
到
t
_
o
r
d
e
r
_
1
表
，
达
到
预
期
目
标
。
执
行
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
r
d
e
r
b
y
I
d
s
：
通
过
日
志
可
以
发
现
，
根
据
传
入
o
r
d
e
r
_
i
d
的
奇
偶
不
同
，
s
h
a
r
d
i
n
g
-
j
d
b
c
分
别
去
不
同
的
表
检
索
数
据
，
达
到
预
期
目
标
。
 
2
.
4
.
流
程
分
析
 
通
过
日
志
分
析
，
S
h
a
r
d
i
n
g
-
J
D
B
C
在
拿
到
用
户
要
执
行
的
s
q
l
之
后
干
了
哪
些
事
儿
：
（
1
）
解
析
s
q
l
，
获
取
片
键
值
，
在
本
例
中
是
o
r
d
e
r
_
i
d
（
2
）
S
h
a
r
d
i
n
g
-
J
D
B
C
通
过
规
则
配
置
 
t
_
o
r
d
e
r
_
$
-
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
}
，
知
道
了
当
o
r
d
e
r
_
i
d
为
偶
数
时
，
应
该
往
t
_
o
r
d
e
r
_
1
表
插
数
据
，
为
奇
数
时
，
往
t
_
o
r
d
e
r
_
2
插
数
据
。
（
3
）
于
是
S
h
a
r
d
i
n
g
-
J
D
B
C
根
据
o
r
d
e
r
_
i
d
的
值
改
写
s
q
l
语
句
，
改
写
后
的
S
Q
L
语
句
是
真
实
所
要
执
行
的
S
Q
L
语
句
。
（
4
）
执
行
改
写
后
的
真
实
s
q
l
语
句
（
5
）
将
所
有
真
正
执
行
s
q
l
的
结
果
进
行
汇
总
合
并
，
返
回
。
 
 
 
 
 
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
r
d
e
r
b
y
I
d
s
(
)
{
 
 
 
 
 
 
 
 
L
i
s
t
<
L
o
n
g
>
 
i
d
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
 
 
 
 
 
 
 
 
i
d
s
.
a
d
d
(
3
7
3
7
7
1
6
3
6
0
8
5
6
2
0
7
3
6
L
)
;
 
 
 
 
 
 
 
 
i
d
s
.
a
d
d
(
3
7
3
7
7
1
6
3
5
8
0
4
6
0
2
3
6
9
L
)
;
 
 
 
 
 
 
 
 
L
i
s
t
<
M
a
p
>
 
m
a
p
s
 
=
 
o
r
d
e
r
D
a
o
.
s
e
l
e
c
t
O
r
d
e
r
b
y
I
d
s
(
i
d
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
m
a
p
s
)
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 18 -->
2
.
5
.
其
他
集
成
方
式
 
S
h
a
r
d
i
n
g
-
J
D
B
C
不
仅
可
以
与
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
良
好
集
成
，
它
还
支
持
其
他
配
置
方
式
，
共
支
持
以
下
四
种
集
成
方
式
。
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
 
Y
a
m
l
 
配
置
定
义
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
8
1
 
 
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
s
h
a
r
d
i
n
g
‐
j
d
b
c
‐
s
i
m
p
l
e
‐
d
e
m
o
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
h
a
r
d
i
n
g
‐
j
d
b
c
‐
s
i
m
p
l
e
‐
d
e
m
o
 
 
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
 
 
 
 
 
 
c
h
a
r
s
e
t
:
 
u
t
f
‐
8
 
 
 
 
 
 
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
 
 
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
 
 
 
 
 
 
n
a
m
e
s
:
 
m
1
 
 
 
 
 
 
m
1
:
 
 
 
 
 
 
 
 
t
y
p
e
:
 
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
 
 
 
 
 
 
 
 
d
r
i
v
e
r
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
m
y
s
q
l
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
3
3
0
6
/
o
r
d
e
r
_
d
b
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
 
m
y
s
q
l
 
 
 
 
s
h
a
r
d
i
n
g
:
 
 
 
 
 
 
t
a
b
l
e
s
:
 
 
 
 
 
 
 
 
t
_
o
r
d
e
r
:
 
 
 
 
 
 
 
 
 
 
a
c
t
u
a
l
D
a
t
a
N
o
d
e
s
:
 
m
1
.
t
_
o
r
d
e
r
_
$
‐
>
{
1
.
.
2
}
 
 
 
 
 
 
 
 
 
 
t
a
b
l
e
S
t
r
a
t
e
g
y
:
 
 
 
 
 
 
 
 
 
 
 
 
i
n
l
i
n
e
:
 
 
 
 
 
 
 
 
 
 
 
 
 
 
s
h
a
r
d
i
n
g
C
o
l
u
m
n
:
 
o
r
d
e
r
_
i
d
 
 
 
 
 
 
 
 
 
 
 
 
 
 
a
l
g
o
r
i
t
h
m
E
x
p
r
e
s
s
i
o
n
:
 
t
_
o
r
d
e
r
_
$
‐
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
}
 
 
 
 
 
 
 
 
 
 
k
e
y
G
e
n
e
r
a
t
o
r
:
 
 
 
 
 
 
 
 
 
 
 
 
t
y
p
e
:
 
S
N
O
W
F
L
A
K
E
 
 
 
 
 
 
 
 
 
 
 
 
c
o
l
u
m
n
:
 
o
r
d
e
r
_
i
d
 
 
 
 
p
r
o
p
s
:
 
 
 
 
 
 
s
q
l
:
 
 
 
 
 
 
 
 
s
h
o
w
:
 
t
r
u
e
m
y
b
a
t
i
s
:
 
 
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
:
 
 
 
 
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
:
 
t
r
u
e
s
w
a
g
g
e
r
:
 
 
e
n
a
b
l
e
:
 
t
r
u
e
l
o
g
g
i
n
g
:
 
 
l
e
v
e
l
:
 
 
 
 
r
o
o
t
:
 
i
n
f
o
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 19 -->
如
果
使
用
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
则
需
要
屏
蔽
原
来
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
。
 
J
a
v
a
 
配
置
添
加
配
置
类
：
 
 
 
 
 
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
:
 
i
n
f
o
 
 
 
 
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
d
b
s
h
a
r
d
i
n
g
:
 
d
e
b
u
g
 
 
 
 
d
r
u
i
d
.
s
q
l
:
 
d
e
b
u
g
 
 
 
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
 
S
h
a
r
d
i
n
g
J
d
b
c
C
o
n
f
i
g
 
{
 
 
 
 
 
/
/
 
定
义
数
据
源
 
 
 
 
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
>
 
c
r
e
a
t
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
M
a
p
(
)
 
{
 
 
 
 
 
 
 
 
D
r
u
i
d
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
 
d
a
t
a
S
o
u
r
c
e
1
 
=
 
n
e
w
 
D
r
u
i
d
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
)
;
 
 
 
 
 
 
 
 
d
a
t
a
S
o
u
r
c
e
1
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
C
l
a
s
s
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
a
t
a
S
o
u
r
c
e
1
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
3
3
0
6
/
o
r
d
e
r
_
d
b
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
"
)
;
 
 
 
 
 
 
 
 
d
a
t
a
S
o
u
r
c
e
1
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
a
t
a
S
o
u
r
c
e
1
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
r
o
o
t
"
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
>
 
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
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
p
u
t
(
"
m
1
"
,
 
d
a
t
a
S
o
u
r
c
e
1
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
u
l
t
;
 
 
 
 
}
 
 
 
 
/
/
 
定
义
主
键
生
成
策
略
 
 
 
 
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
 
K
e
y
G
e
n
e
r
a
t
o
r
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
 
g
e
t
K
e
y
G
e
n
e
r
a
t
o
r
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
(
)
 
{
 
 
 
 
 
 
 
 
K
e
y
G
e
n
e
r
a
t
o
r
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
 
K
e
y
G
e
n
e
r
a
t
o
r
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
(
"
S
N
O
W
F
L
A
K
E
"
,
"
o
r
d
e
r
_
i
d
"
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
u
l
t
;
 
 
 
 
}
 
 
 
 
 
/
/
 
定
义
t
_
o
r
d
e
r
表
的
分
片
策
略
 
 
 
 
T
a
b
l
e
R
u
l
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
t
i
o
n
 
g
e
t
O
r
d
e
r
T
a
b
l
e
R
u
l
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
t
i
o
n
(
)
 
{
 
 
 
 
 
 
 
 
T
a
b
l
e
R
u
l
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
t
i
o
n
 
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
 
T
a
b
l
e
R
u
l
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
t
i
o
n
(
"
t
_
o
r
d
e
r
"
,
"
m
1
.
t
_
o
r
d
e
r
_
$
‐
>
{
1
.
.
2
}
"
)
;
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
s
e
t
T
a
b
l
e
S
h
a
r
d
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
C
o
n
f
i
g
(
n
e
w
 
I
n
l
i
n
e
S
h
a
r
d
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
(
"
o
r
d
e
r
_
i
d
"
,
 
"
t
_
o
r
d
e
r
_
$
‐
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
}
"
)
)
;
 
 
 
 
 
 
 
 
r
e
s
u
l
t
.
s
e
t
K
e
y
G
e
n
e
r
a
t
o
r
C
o
n
f
i
g
(
g
e
t
K
e
y
G
e
n
e
r
a
t
o
r
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
u
l
t
;
 
 
 
 
}
 
 
 
 
/
/
 
定
义
s
h
a
r
d
i
n
g
‐
J
d
b
c
数
据
源
 
 
 
 
@
B
e
a
n
 
 
 
 
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
e
t
S
h
a
r
d
i
n
g
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
)
 
t
h
r
o
w
s
 
S
Q
L
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
 
 
 
 
 
 
 
 
S
h
a
r
d
i
n
g
R
u
l
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
t
i
o
n
 
s
h
a
r
d
i
n
g
R
u
l
e
C
o
n
f
i
g
 
=
 
n
e
w
 
S
h
a
r
d
i
n
g
R
u
l
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
t
i
o
n
(
)
;
 
 
 
 
 
 
 
 
s
h
a
r
d
i
n
g
R
u
l
e
C
o
n
f
i
g
.
g
e
t
T
a
b
l
e
R
u
l
e
C
o
n
f
i
g
s
(
)
.
a
d
d
(
g
e
t
O
r
d
e
r
T
a
b
l
e
R
u
l
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
t
i
o
n
(
)
)
;
 
 
 
 
 
 
 
 
/
/
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
p
r
o
p
s
.
s
q
l
.
s
h
o
w
 
=
 
t
r
u
e
 
 
 
 
 
 
 
 
P
r
o
p
e
r
t
i
e
s
 
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
 
=
 
n
e
w
 
P
r
o
p
e
r
t
i
e
s
(
)
;
 
 
 
 
 
 
 
 
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
.
p
u
t
(
"
s
q
l
.
s
h
o
w
"
,
"
t
r
u
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
 
S
h
a
r
d
i
n
g
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
F
a
c
t
o
r
y
.
c
r
e
a
t
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
(
c
r
e
a
t
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
M
a
p
(
)
,
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 20 -->
由
于
采
用
了
配
置
类
所
以
需
要
屏
蔽
原
来
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
中
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
开
头
的
配
置
信
息
。
还
需
要
在
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
启
动
类
中
屏
蔽
使
用
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
配
置
项
的
类
：
 
 
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
此
方
式
同
快
速
入
门
程
序
。
 
S
p
r
i
n
g
命
名
空
间
配
置
此
方
式
使
用
x
m
l
方
式
配
置
，
不
推
荐
使
用
。
 
s
h
a
r
d
i
n
g
R
u
l
e
C
o
n
f
i
g
,
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
)
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
(
e
x
c
l
u
d
e
 
=
 
{
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
.
c
l
a
s
s
}
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
 
S
h
a
r
d
i
n
g
J
d
b
c
S
i
m
p
l
e
D
e
m
o
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
.
.
.
.
}
#
 
定
义
数
据
源
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
n
a
m
e
s
 
=
 
m
1
 
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
.
t
y
p
e
 
=
 
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
3
3
0
6
/
o
r
d
e
r
_
d
b
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
 
指
定
t
_
o
r
d
e
r
表
的
主
键
生
成
策
略
为
S
N
O
W
F
L
A
K
E
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
k
e
y
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
.
c
o
l
u
m
n
=
o
r
d
e
r
_
i
d
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
k
e
y
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
.
t
y
p
e
=
S
N
O
W
F
L
A
K
E
 
#
 
指
定
t
_
o
r
d
e
r
表
的
数
据
分
布
情
况
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
a
c
t
u
a
l
‐
d
a
t
a
‐
n
o
d
e
s
 
=
 
m
1
.
t
_
o
r
d
e
r
_
$
‐
>
{
1
.
.
2
}
 
#
 
指
定
t
_
o
r
d
e
r
表
的
分
表
策
略
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
s
h
a
r
d
i
n
g
‐
c
o
l
u
m
n
 
=
 
o
r
d
e
r
_
i
d
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
a
l
g
o
r
i
t
h
m
‐
e
x
p
r
e
s
s
i
o
n
 
=
 
t
_
o
r
d
e
r
_
$
‐
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
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
b
e
a
n
s
 
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
w
w
w
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
o
r
g
/
s
c
h
e
m
a
/
b
e
a
n
s
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
m
l
n
s
:
p
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
o
r
g
/
s
c
h
e
m
a
/
p
"
 
 
 
 
 
 
 
x
m
l
n
s
:
c
o
n
t
e
x
t
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
o
r
g
/
s
c
h
e
m
a
/
c
o
n
t
e
x
t
"
 
 
 
 
 
 
 
x
m
l
n
s
:
t
x
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
o
r
g
/
s
c
h
e
m
a
/
t
x
"
 
 
 
 
 
 
 
x
m
l
n
s
:
s
h
a
r
d
i
n
g
=
"
h
t
t
p
:
/
/
s
h
a
r
d
i
n
g
s
p
h
e
r
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
s
c
h
e
m
a
/
s
h
a
r
d
i
n
g
s
p
h
e
r
e
/
s
h
a
r
d
i
n
g
"
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 21 -->
3
.
S
h
a
r
d
i
n
g
-
J
D
B
C
执
行
原
理
 
3
.
1
 
基
本
概
念
 
在
了
解
S
h
a
r
d
i
n
g
-
J
D
B
C
的
执
行
原
理
前
，
需
要
了
解
以
下
概
念
：
逻
辑
表
水
平
拆
分
的
数
据
表
的
总
称
。
例
：
订
单
数
据
表
根
据
主
键
尾
数
拆
分
为
1
0
张
表
，
分
别
是
t
_
o
r
d
e
r
_
0
、
t
_
o
r
d
e
r
_
1
到
t
_
o
r
d
e
r
_
9
，
他
们
的
逻
辑
表
名
为
t
_
o
r
d
e
r
。
真
实
表
在
分
片
的
数
据
库
中
真
实
存
在
的
物
理
表
。
即
上
个
示
例
中
的
t
_
o
r
d
e
r
_
0
到
t
_
o
r
d
e
r
_
9
。
 
 
 
 
 
 
 
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
w
w
w
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
o
r
g
/
s
c
h
e
m
a
/
b
e
a
n
s
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
o
r
g
/
s
c
h
e
m
a
/
b
e
a
n
s
/
s
p
r
i
n
g
‐
b
e
a
n
s
.
x
s
d
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
h
t
t
p
:
/
/
s
h
a
r
d
i
n
g
s
p
h
e
r
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
s
c
h
e
m
a
/
s
h
a
r
d
i
n
g
s
p
h
e
r
e
/
s
h
a
r
d
i
n
g
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
h
t
t
p
:
/
/
s
h
a
r
d
i
n
g
s
p
h
e
r
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
s
c
h
e
m
a
/
s
h
a
r
d
i
n
g
s
p
h
e
r
e
/
s
h
a
r
d
i
n
g
/
s
h
a
r
d
i
n
g
.
x
s
d
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
o
r
g
/
s
c
h
e
m
a
/
c
o
n
t
e
x
t
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
o
r
g
/
s
c
h
e
m
a
/
c
o
n
t
e
x
t
/
s
p
r
i
n
g
‐
c
o
n
t
e
x
t
.
x
s
d
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
o
r
g
/
s
c
h
e
m
a
/
t
x
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
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
o
r
g
/
s
c
h
e
m
a
/
t
x
/
s
p
r
i
n
g
‐
t
x
.
x
s
d
"
>
 
 
 
 
<
c
o
n
t
e
x
t
:
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
‐
c
o
n
f
i
g
 
/
>
 
 
 
 
 
 
 
 
<
!
‐
‐
定
义
多
个
数
据
源
‐
‐
>
 
 
 
 
<
b
e
a
n
 
i
d
=
"
m
1
"
 
c
l
a
s
s
=
"
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
"
 
d
e
s
t
r
o
y
‐
m
e
t
h
o
d
=
"
c
l
o
s
e
"
>
 
 
 
 
 
 
 
 
<
p
r
o
p
e
r
t
y
 
n
a
m
e
=
"
d
r
i
v
e
r
C
l
a
s
s
N
a
m
e
"
 
v
a
l
u
e
=
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
 
/
>
 
 
 
 
 
 
 
 
<
p
r
o
p
e
r
t
y
 
n
a
m
e
=
"
u
r
l
"
 
v
a
l
u
e
=
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
3
3
0
6
/
o
r
d
e
r
_
d
b
_
1
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
"
 
/
>
 
 
 
 
 
 
 
 
<
p
r
o
p
e
r
t
y
 
n
a
m
e
=
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
 
v
a
l
u
e
=
"
r
o
o
t
"
 
/
>
 
 
 
 
 
 
 
 
<
p
r
o
p
e
r
t
y
 
n
a
m
e
=
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
 
v
a
l
u
e
=
"
r
o
o
t
"
 
/
>
 
 
 
 
<
/
b
e
a
n
>
 
 
 
 
 
<
!
‐
‐
定
义
分
库
策
略
‐
‐
>
 
 
<
s
h
a
r
d
i
n
g
:
i
n
l
i
n
e
‐
s
t
r
a
t
e
g
y
 
i
d
=
"
t
a
b
l
e
S
h
a
r
d
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
"
 
s
h
a
r
d
i
n
g
‐
c
o
l
u
m
n
=
"
o
r
d
e
r
_
i
d
"
 
a
l
g
o
r
i
t
h
m
‐
e
x
p
r
e
s
s
i
o
n
=
"
t
_
o
r
d
e
r
_
$
‐
>
{
o
r
d
e
r
_
i
d
 
%
 
2
 
+
 
1
}
"
 
/
>
 
 
 
 
 
 
 
 
 
<
!
‐
‐
定
义
主
键
生
成
策
略
‐
‐
>
 
 
<
s
h
a
r
d
i
n
g
:
k
e
y
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
 
i
d
=
"
o
r
d
e
r
K
e
y
G
e
n
e
r
a
t
o
r
"
 
t
y
p
e
=
"
S
N
O
W
F
L
A
K
E
"
 
c
o
l
u
m
n
=
"
o
r
d
e
r
_
i
d
"
 
/
>
 
 
 
 
 
 
 
 
<
!
‐
‐
定
义
s
h
a
r
d
i
n
g
‐
J
d
b
c
数
据
源
‐
‐
>
 
 
 
 
<
s
h
a
r
d
i
n
g
:
d
a
t
a
‐
s
o
u
r
c
e
 
i
d
=
"
s
h
a
r
d
i
n
g
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
"
>
 
 
 
 
 
 
 
 
<
s
h
a
r
d
i
n
g
:
s
h
a
r
d
i
n
g
‐
r
u
l
e
 
d
a
t
a
‐
s
o
u
r
c
e
‐
n
a
m
e
s
=
"
m
1
"
>
 
 
 
 
 
 
 
 
 
 
 
 
<
s
h
a
r
d
i
n
g
:
t
a
b
l
e
‐
r
u
l
e
s
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
s
h
a
r
d
i
n
g
:
t
a
b
l
e
‐
r
u
l
e
 
l
o
g
i
c
‐
t
a
b
l
e
=
"
t
_
o
r
d
e
r
"
 
 
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
‐
r
e
f
=
"
t
a
b
l
e
S
h
a
r
d
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
"
 
k
e
y
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
‐
r
e
f
=
"
o
r
d
e
r
K
e
y
G
e
n
e
r
a
t
o
r
"
 
/
>
 
 
 
 
 
 
 
 
 
 
 
 
<
/
s
h
a
r
d
i
n
g
:
t
a
b
l
e
‐
r
u
l
e
s
>
 
 
 
 
 
 
 
 
<
/
s
h
a
r
d
i
n
g
:
s
h
a
r
d
i
n
g
‐
r
u
l
e
>
 
 
 
 
<
/
s
h
a
r
d
i
n
g
:
d
a
t
a
‐
s
o
u
r
c
e
>
<
/
b
e
a
n
s
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 22 -->
数
据
节
点
数
据
分
片
的
最
小
物
理
单
元
。
由
数
据
源
名
称
和
数
据
表
组
成
，
例
：
d
s
_
0
.
t
_
o
r
d
e
r
_
0
。
绑
定
表
指
分
片
规
则
一
致
的
主
表
和
子
表
。
例
如
：
t
_
o
r
d
e
r
表
和
t
_
o
r
d
e
r
_
i
t
e
m
表
，
均
按
照
o
r
d
e
r
_
i
d
分
片
,
绑
定
表
之
间
的
分
区
键
完
全
相
同
，
则
此
两
张
表
互
为
绑
定
表
关
系
。
绑
定
表
之
间
的
多
表
关
联
查
询
不
会
出
现
笛
卡
尔
积
关
联
，
关
联
查
询
效
率
将
大
大
提
升
。
举
例
说
明
，
如
果
S
Q
L
为
：
 
在
不
配
置
绑
定
表
关
系
时
，
假
设
分
片
键
o
r
d
e
r
_
i
d
将
数
值
1
0
路
由
至
第
0
片
，
将
数
值
1
1
路
由
至
第
1
片
，
那
么
路
由
后
的
S
Q
L
应
该
为
4
条
，
它
们
呈
现
为
笛
卡
尔
积
：
 
在
配
置
绑
定
表
关
系
后
，
路
由
的
S
Q
L
应
该
为
2
条
：
 
 
广
播
表
指
所
有
的
分
片
数
据
源
中
都
存
在
的
表
，
表
结
构
和
表
中
的
数
据
在
每
个
数
据
库
中
均
完
全
一
致
。
适
用
于
数
据
量
不
大
且
需
要
与
海
量
数
据
的
表
进
行
关
联
查
询
的
场
景
，
例
如
：
字
典
表
。
分
片
键
用
于
分
片
的
数
据
库
字
段
，
是
将
数
据
库
(
表
)
水
平
拆
分
的
关
键
字
段
。
例
：
将
订
单
表
中
的
订
单
主
键
的
尾
数
取
模
分
片
，
则
订
单
主
键
为
分
片
字
段
。
 
S
Q
L
中
如
果
无
分
片
字
段
，
将
执
行
全
路
由
，
性
能
较
差
。
 
除
了
对
单
分
片
字
段
的
支
持
，
S
h
a
r
d
i
n
g
-
J
d
b
c
也
支
持
根
据
多
个
字
段
进
行
分
片
。
分
片
算
法
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
0
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
1
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
0
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
1
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
0
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
S
E
L
E
C
T
 
i
.
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
1
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
W
H
E
R
E
 
o
.
o
r
d
e
r
_
i
d
 
i
n
 
(
1
0
,
 
1
1
)
;
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 23 -->
通
过
分
片
算
法
将
数
据
分
片
，
支
持
通
过
=
、
B
E
T
W
E
E
N
和
I
N
分
片
。
分
片
算
法
需
要
应
用
方
开
发
者
自
行
实
现
，
可
实
现
的
灵
活
度
非
常
高
。
包
括
：
精
确
分
片
算
法
 
、
范
围
分
片
算
法
 
，
复
合
分
片
算
法
 
等
。
例
如
：
w
h
e
r
e
 
o
r
d
e
r
_
i
d
 
=
 
?
 
将
采
用
精
确
分
片
算
法
，
w
h
e
r
e
 
o
r
d
e
r
_
i
d
 
i
n
 
(
?
,
?
,
?
)
将
采
用
精
确
分
片
算
法
，
w
h
e
r
e
 
o
r
d
e
r
_
i
d
 
B
E
T
W
E
E
N
 
?
 
a
n
d
 
?
 
将
采
用
范
围
分
片
算
法
，
复
合
分
片
算
法
用
于
分
片
键
有
多
个
复
杂
情
况
。
分
片
策
略
包
含
分
片
键
和
分
片
算
法
，
由
于
分
片
算
法
的
独
立
性
，
将
其
独
立
抽
离
。
真
正
可
用
于
分
片
操
作
的
是
分
片
键
 
+
 
分
片
算
法
，
也
就
是
分
片
策
略
。
内
置
的
分
片
策
略
大
致
可
分
为
尾
数
取
模
、
哈
希
、
范
围
、
标
签
、
时
间
等
。
由
用
户
方
配
置
的
分
片
策
略
则
更
加
灵
活
，
常
用
的
使
用
行
表
达
式
配
置
分
片
策
略
，
它
采
用
G
r
o
o
v
y
表
达
式
表
示
，
如
:
 
t
_
u
s
e
r
_
$
-
>
{
u
_
i
d
 
%
 
8
}
 
表
示
t
_
u
s
e
r
表
根
据
u
_
i
d
模
8
，
而
分
成
8
张
表
，
表
名
称
为
t
_
u
s
e
r
_
0
到
t
_
u
s
e
r
_
7
。
自
增
主
键
生
成
策
略
通
过
在
客
户
端
生
成
自
增
主
键
替
换
以
数
据
库
原
生
自
增
主
键
的
方
式
，
做
到
分
布
式
主
键
无
重
复
。
3
.
2
.
S
Q
L
解
析
 
 
 
当
S
h
a
r
d
i
n
g
-
J
D
B
C
接
受
到
一
条
S
Q
L
语
句
时
，
会
陆
续
执
行
S
Q
L
解
析
 
=
>
 
查
询
优
化
 
=
>
 
S
Q
L
路
由
 
=
>
 
S
Q
L
改
写
 
=
>
 
S
Q
L
执
行
=
>
 
结
果
归
并
，
最
终
返
回
执
行
结
果
。
 
 
 
S
Q
L
解
析
过
程
分
为
词
法
解
析
和
语
法
解
析
。
 
词
法
解
析
器
用
于
将
S
Q
L
拆
解
为
不
可
再
分
的
原
子
符
号
，
称
为
T
o
k
e
n
。
并
根
据
不
同
数
据
库
方
言
所
提
供
的
字
典
，
将
其
归
类
为
关
键
字
，
表
达
式
，
字
面
量
和
操
作
符
。
 
再
使
用
语
法
解
析
器
将
S
Q
L
转
换
为
抽
象
语
法
树
。
例
如
，
以
下
S
Q
L
：
 
解
析
之
后
的
为
抽
象
语
法
树
见
下
图
：
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
 
F
R
O
M
 
t
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
 
s
t
a
t
u
s
 
=
 
'
A
C
T
I
V
E
'
 
A
N
D
 
a
g
e
 
>
 
1
8
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 24 -->
为
了
便
于
理
解
，
抽
象
语
法
树
中
的
关
键
字
的
T
o
k
e
n
用
绿
色
表
示
，
变
量
的
T
o
k
e
n
用
红
色
表
示
，
灰
色
表
示
需
要
进
一
步
拆
分
。
 
 
最
后
，
通
过
对
抽
象
语
法
树
的
遍
历
去
提
炼
分
片
所
需
的
上
下
文
，
并
标
记
有
可
能
需
要
S
Q
L
改
写
(
后
边
介
绍
)
的
位
置
。
 
供
分
片
使
用
的
解
析
上
下
文
包
含
查
询
选
择
项
（
S
e
l
e
c
t
 
I
t
e
m
s
）
、
表
信
息
（
T
a
b
l
e
）
、
分
片
条
件
（
S
h
a
r
d
i
n
g
 
C
o
n
d
i
t
i
o
n
）
、
自
增
主
键
信
息
（
A
u
t
o
 
i
n
c
r
e
m
e
n
t
 
P
r
i
m
a
r
y
 
K
e
y
）
、
排
序
信
息
（
O
r
d
e
r
 
B
y
）
、
分
组
信
息
（
G
r
o
u
p
 
B
y
）
以
及
分
页
信
息
（
L
i
m
i
t
、
R
o
w
n
u
m
、
T
o
p
）
。
3
.
3
.
S
Q
L
路
由
 
 
 
S
Q
L
路
由
就
是
把
针
对
逻
辑
表
的
数
据
操
作
映
射
到
对
数
据
结
点
操
作
的
过
程
。
 
 
根
据
解
析
上
下
文
匹
配
数
据
库
和
表
的
分
片
策
略
，
并
生
成
路
由
路
径
。
 
对
于
携
带
分
片
键
的
S
Q
L
，
根
据
分
片
键
操
作
符
不
同
可
以
划
分
为
单
片
路
由
(
分
片
键
的
操
作
符
是
等
号
)
、
多
片
路
由
(
分
片
键
的
操
作
符
是
I
N
)
和
范
围
路
由
(
分
片
键
的
操
作
符
是
B
E
T
W
E
E
N
)
，
不
携
带
分
片
键
的
S
Q
L
则
采
用
广
播
路
由
。
根
据
分
片
键
进
行
路
由
的
场
景
可
分
为
直
接
路
由
、
标
准
路
由
、
笛
卡
尔
路
由
等
。
标
准
路
由
标
准
路
由
是
S
h
a
r
d
i
n
g
-
J
d
b
c
最
为
推
荐
使
用
的
分
片
方
式
，
它
的
适
用
范
围
是
不
包
含
关
联
查
询
或
仅
包
含
绑
定
表
之
间
关
联
查
询
的
S
Q
L
。
 
当
分
片
运
算
符
是
等
于
号
时
，
路
由
结
果
将
落
入
单
库
（
表
）
，
当
分
片
运
算
符
是
B
E
T
W
E
E
N
或
I
N
时
，
则
路
由
结
果
不
一
定
落
入
唯
一
的
库
（
表
）
，
因
此
一
条
逻
辑
S
Q
L
最
终
可
能
被
拆
分
为
多
条
用
于
执
行
的
真
实
S
Q
L
。
 
举
例
说
明
，
如
果
按
照
o
r
d
e
r
_
i
d
的
奇
数
和
偶
数
进
行
数
据
分
片
，
一
个
单
表
查
询
的
S
Q
L
如
下
：
 
那
么
路
由
的
结
果
应
为
：
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 25 -->
绑
定
表
的
关
联
查
询
与
单
表
查
询
复
杂
度
和
性
能
相
当
。
举
例
说
明
，
如
果
一
个
包
含
绑
定
表
的
关
联
查
询
的
S
Q
L
如
下
：
 
那
么
路
由
的
结
果
应
为
：
 
可
以
看
到
，
S
Q
L
拆
分
的
数
目
与
单
表
是
一
致
的
。
笛
卡
尔
路
由
笛
卡
尔
路
由
是
最
复
杂
的
情
况
，
它
无
法
根
据
绑
定
表
的
关
系
定
位
分
片
规
则
，
因
此
非
绑
定
表
之
间
的
关
联
查
询
需
要
拆
解
为
笛
卡
尔
积
组
合
执
行
。
 
如
果
上
个
示
例
中
的
S
Q
L
并
未
配
置
绑
定
表
关
系
，
那
么
路
由
的
结
果
应
为
：
 
笛
卡
尔
路
由
查
询
性
能
较
低
，
需
谨
慎
使
用
。
 
全
库
表
路
由
对
于
不
携
带
分
片
键
的
S
Q
L
，
则
采
取
广
播
路
由
的
方
式
。
根
据
S
Q
L
类
型
又
可
以
划
分
为
全
库
表
路
由
、
全
库
路
由
、
全
实
例
路
由
、
单
播
路
由
和
阻
断
路
由
这
5
种
类
型
。
其
中
全
库
表
路
由
用
于
处
理
对
数
据
库
中
与
其
逻
辑
表
相
关
的
所
有
真
实
表
的
操
作
，
主
要
包
括
不
带
分
片
键
的
D
Q
L
(
数
据
查
询
)
和
D
M
L
（
数
据
操
纵
）
，
以
及
D
D
L
（
数
据
定
义
）
等
。
例
如
：
 
则
会
遍
历
所
有
数
据
库
中
的
所
有
表
，
逐
一
匹
配
逻
辑
表
和
真
实
表
名
，
能
够
匹
配
得
上
则
执
行
。
路
由
后
成
为
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
0
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
1
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
0
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
1
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
0
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
o
 
J
O
I
N
 
t
_
o
r
d
e
r
_
i
t
e
m
_
1
 
i
 
O
N
 
o
.
o
r
d
e
r
_
i
d
=
i
.
o
r
d
e
r
_
i
d
 
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
 
I
N
 
(
1
,
 
2
)
;
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
 
W
H
E
R
E
 
g
o
o
d
_
p
r
o
r
i
t
y
 
I
N
 
(
1
,
 
1
0
)
;
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
0
 
W
H
E
R
E
 
g
o
o
d
_
p
r
o
r
i
t
y
 
I
N
 
(
1
,
 
1
0
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
W
H
E
R
E
 
g
o
o
d
_
p
r
o
r
i
t
y
 
I
N
 
(
1
,
 
1
0
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
2
 
W
H
E
R
E
 
g
o
o
d
_
p
r
o
r
i
t
y
 
I
N
 
(
1
,
 
1
0
)
;
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
_
o
r
d
e
r
_
3
 
W
H
E
R
E
 
g
o
o
d
_
p
r
o
r
i
t
y
 
I
N
 
(
1
,
 
1
0
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 26 -->
3
.
4
.
S
Q
L
改
写
 
工
程
师
面
向
逻
辑
表
书
写
的
S
Q
L
，
并
不
能
够
直
接
在
真
实
的
数
据
库
中
执
行
，
S
Q
L
改
写
用
于
将
逻
辑
S
Q
L
改
写
为
在
真
实
数
据
库
中
可
以
正
确
执
行
的
S
Q
L
。
如
一
个
简
单
的
例
子
，
若
逻
辑
S
Q
L
为
：
 
假
设
该
S
Q
L
配
置
分
片
键
o
r
d
e
r
_
i
d
，
并
且
o
r
d
e
r
_
i
d
=
1
的
情
况
，
将
路
由
至
分
片
表
1
。
那
么
改
写
之
后
的
S
Q
L
应
该
为
：
 
 
再
比
如
，
S
h
a
r
d
i
n
g
-
J
D
B
C
需
要
在
结
果
归
并
时
获
取
相
应
数
据
，
但
该
数
据
并
未
能
通
过
查
询
的
S
Q
L
返
回
。
 
这
种
情
况
主
要
是
针
对
G
R
O
U
P
 
B
Y
和
O
R
D
E
R
 
B
Y
。
结
果
归
并
时
，
需
要
根
据
G
R
O
U
P
 
B
Y
和
O
R
D
E
R
 
B
Y
的
字
段
项
进
行
分
组
和
排
序
，
但
如
果
原
始
S
Q
L
的
选
择
项
中
若
并
未
包
含
分
组
项
或
排
序
项
，
则
需
要
对
原
始
S
Q
L
进
行
改
写
。
 
先
看
一
下
原
始
S
Q
L
中
带
有
结
果
归
并
所
需
信
息
的
场
景
：
 
由
于
使
用
u
s
e
r
_
i
d
进
行
排
序
，
在
结
果
归
并
中
需
要
能
够
获
取
到
u
s
e
r
_
i
d
的
数
据
，
而
上
面
的
S
Q
L
是
能
够
获
取
到
u
s
e
r
_
i
d
数
据
的
，
因
此
无
需
补
列
。
如
果
选
择
项
中
不
包
含
结
果
归
并
时
所
需
的
列
，
则
需
要
进
行
补
列
，
如
以
下
S
Q
L
：
 
由
于
原
始
S
Q
L
中
并
不
包
含
需
要
在
结
果
归
并
中
需
要
获
取
的
u
s
e
r
_
i
d
，
因
此
需
要
对
S
Q
L
进
行
补
列
改
写
。
补
列
之
后
的
S
Q
L
是
：
 
 
 
3
.
5
.
S
Q
L
执
行
 
 
 
S
h
a
r
d
i
n
g
-
J
D
B
C
采
用
一
套
自
动
化
的
执
行
引
擎
，
负
责
将
路
由
和
改
写
完
成
之
后
的
真
实
S
Q
L
安
全
且
高
效
发
送
到
底
层
数
据
源
执
行
。
 
它
不
是
简
单
地
将
S
Q
L
通
过
J
D
B
C
直
接
发
送
至
数
据
源
执
行
；
也
并
非
直
接
将
执
行
请
求
放
入
线
程
池
去
并
发
执
行
。
它
更
关
注
平
衡
数
据
源
连
接
创
建
以
及
内
存
占
用
所
产
生
的
消
耗
，
以
及
最
大
限
度
地
合
理
利
用
并
发
等
问
题
。
 
执
行
引
擎
的
目
标
是
自
动
化
的
平
衡
资
源
控
制
与
执
行
效
率
，
他
能
在
以
下
两
种
模
式
自
适
应
切
换
：
内
存
限
制
模
式
S
E
L
E
C
T
 
o
r
d
e
r
_
i
d
 
F
R
O
M
 
t
_
o
r
d
e
r
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
=
1
;
S
E
L
E
C
T
 
o
r
d
e
r
_
i
d
 
F
R
O
M
 
t
_
o
r
d
e
r
_
1
 
W
H
E
R
E
 
o
r
d
e
r
_
i
d
=
1
;
S
E
L
E
C
T
 
o
r
d
e
r
_
i
d
,
 
u
s
e
r
_
i
d
 
F
R
O
M
 
t
_
o
r
d
e
r
 
O
R
D
E
R
 
B
Y
 
u
s
e
r
_
i
d
;
S
E
L
E
C
T
 
o
r
d
e
r
_
i
d
 
F
R
O
M
 
t
_
o
r
d
e
r
 
O
R
D
E
R
 
B
Y
 
u
s
e
r
_
i
d
;
 
S
E
L
E
C
T
 
o
r
d
e
r
_
i
d
,
 
u
s
e
r
_
i
d
 
A
S
 
O
R
D
E
R
_
B
Y
_
D
E
R
I
V
E
D
_
0
 
F
R
O
M
 
t
_
o
r
d
e
r
 
O
R
D
E
R
 
B
Y
 
u
s
e
r
_
i
d
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 27 -->
使
用
此
模
式
的
前
提
是
，
S
h
a
r
d
i
n
g
-
J
D
B
C
对
一
次
操
作
所
耗
费
的
数
据
库
连
接
数
量
不
做
限
制
。
 
如
果
实
际
执
行
的
S
Q
L
需
要
对
某
数
据
库
实
例
中
的
2
0
0
张
表
做
操
作
，
则
对
每
张
表
创
建
一
个
新
的
数
据
库
连
接
，
并
通
过
多
线
程
的
方
式
并
发
处
理
，
以
达
成
执
行
效
率
最
大
化
。
连
接
限
制
模
式
 
 
使
用
此
模
式
的
前
提
是
，
S
h
a
r
d
i
n
g
-
J
D
B
C
严
格
控
制
对
一
次
操
作
所
耗
费
的
数
据
库
连
接
数
量
。
 
如
果
实
际
执
行
的
S
Q
L
需
要
对
某
数
据
库
实
例
中
的
2
0
0
张
表
做
操
作
，
那
么
只
会
创
建
唯
一
的
数
据
库
连
接
，
并
对
其
2
0
0
张
表
串
行
处
理
。
 
如
果
一
次
操
作
中
的
分
片
散
落
在
不
同
的
数
据
库
，
仍
然
采
用
多
线
程
处
理
对
不
同
库
的
操
作
，
但
每
个
库
的
每
次
操
作
仍
然
只
创
建
一
个
唯
一
的
数
据
库
连
接
。
 
 
内
存
限
制
模
式
适
用
于
O
L
A
P
操
作
，
可
以
通
过
放
宽
对
数
据
库
连
接
的
限
制
提
升
系
统
吞
吐
量
；
 
连
接
限
制
模
式
适
用
于
O
L
T
P
操
作
，
O
L
T
P
通
常
带
有
分
片
键
，
会
路
由
到
单
一
的
分
片
，
因
此
严
格
控
制
数
据
库
连
接
，
以
保
证
在
线
系
统
数
据
库
资
源
能
够
被
更
多
的
应
用
所
使
用
，
是
明
智
的
选
择
。
 
3
.
6
.
结
果
归
并
 
 
 
将
从
各
个
数
据
节
点
获
取
的
多
数
据
结
果
集
，
组
合
成
为
一
个
结
果
集
并
正
确
的
返
回
至
请
求
客
户
端
，
称
为
结
果
归
并
。
 
 
S
h
a
r
d
i
n
g
-
J
D
B
C
支
持
的
结
果
归
并
从
功
能
上
可
分
为
遍
历
、
排
序
、
分
组
、
分
页
和
聚
合
5
种
类
型
，
它
们
是
组
合
而
非
互
斥
的
关
系
。
 
 
归
并
引
擎
的
整
体
结
构
划
分
如
下
图
。
 
 
结
果
归
并
从
结
构
划
分
可
分
为
流
式
归
并
、
内
存
归
并
和
装
饰
者
归
并
。
流
式
归
并
和
内
存
归
并
是
互
斥
的
，
装
饰
者
归
并
可
以
在
流
式
归
并
和
内
存
归
并
之
上
做
进
一
步
的
处
理
。
 
 
内
存
归
并
很
容
易
理
解
，
他
是
将
所
有
分
片
结
果
集
的
数
据
都
遍
历
并
存
储
在
内
存
中
，
再
通
过
统
一
的
分
组
、
排
序
以
及
聚
合
等
计
算
之
后
，
再
将
其
封
装
成
为
逐
条
访
问
的
数
据
结
果
集
返
回
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 28 -->
流
式
归
并
是
指
每
一
次
从
数
据
库
结
果
集
中
获
取
到
的
数
据
，
都
能
够
通
过
游
标
逐
条
获
取
的
方
式
返
回
正
确
的
单
条
数
据
，
它
与
数
据
库
原
生
的
返
回
结
果
集
的
方
式
最
为
契
合
。
 
 
下
边
举
例
说
明
排
序
归
并
的
过
程
，
如
下
图
是
一
个
通
过
分
数
进
行
排
序
的
示
例
图
，
它
采
用
流
式
归
并
方
式
。
 
图
中
展
示
了
3
张
表
返
回
的
数
据
结
果
集
，
每
个
数
据
结
果
集
已
经
根
据
分
数
排
序
完
毕
，
但
是
3
个
数
据
结
果
集
之
间
是
无
序
的
。
 
将
3
个
数
据
结
果
集
的
当
前
游
标
指
向
的
数
据
值
进
行
排
序
，
并
放
入
优
先
级
队
列
，
t
_
s
c
o
r
e
_
0
的
第
一
个
数
据
值
最
大
，
t
_
s
c
o
r
e
_
2
的
第
一
个
数
据
值
次
之
，
t
_
s
c
o
r
e
_
1
的
第
一
个
数
据
值
最
小
，
因
此
优
先
级
队
列
根
据
t
_
s
c
o
r
e
_
0
，
t
_
s
c
o
r
e
_
2
和
t
_
s
c
o
r
e
_
1
的
方
式
排
序
队
列
。
下
图
则
展
现
了
进
行
n
e
x
t
调
用
的
时
候
，
排
序
归
并
是
如
何
进
行
的
。
 
通
过
图
中
我
们
可
以
看
到
，
当
进
行
第
一
次
n
e
x
t
调
用
时
，
排
在
队
列
首
位
的
t
_
s
c
o
r
e
_
0
将
会
被
弹
出
队
列
，
并
且
将
当
前
游
标
指
向
的
数
据
值
（
也
就
是
1
0
0
）
返
回
至
查
询
客
户
端
，
并
且
将
游
标
下
移
一
位
之
后
，
重
新
放
入
优
先
级
队
列
。
 
而
优
先
级
队
列
也
会
根
据
t
_
s
c
o
r
e
_
0
的
当
前
数
据
结
果
集
指
向
游
标
的
数
据
值
（
这
里
是
9
0
）
进
行
排
序
，
根
据
当
前
数
值
，
t
_
s
c
o
r
e
_
0
排
列
在
队
列
的
最
后
一
位
。
 
之
前
队
列
中
排
名
第
二
的
t
_
s
c
o
r
e
_
2
的
数
据
结
果
集
则
自
动
排
在
了
队
列
首
位
。
在
进
行
第
二
次
n
e
x
t
时
，
只
需
要
将
目
前
排
列
在
队
列
首
位
的
t
_
s
c
o
r
e
_
2
弹
出
队
列
，
并
且
将
其
数
据
结
果
集
游
标
指
向
的
值
返
回
至
客
户
端
，
并
下
移
游
标
，
继
续
加
入
队
列
排
队
，
以
此
类
推
。
 
当
一
个
结
果
集
中
已
经
没
有
数
据
了
，
则
无
需
再
次
加
入
队
列
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 29 -->
可
以
看
到
，
对
于
每
个
数
据
结
果
集
中
的
数
据
有
序
，
而
多
数
据
结
果
集
整
体
无
序
的
情
况
下
，
S
h
a
r
d
i
n
g
-
J
D
B
C
无
需
将
所
有
的
数
据
都
加
载
至
内
存
即
可
排
序
。
 
它
使
用
的
是
流
式
归
并
的
方
式
，
每
次
n
e
x
t
仅
获
取
唯
一
正
确
的
一
条
数
据
，
极
大
的
节
省
了
内
存
的
消
耗
。
 
 
装
饰
者
归
并
是
对
所
有
的
结
果
集
归
并
进
行
统
一
的
功
能
增
强
，
比
如
归
并
时
需
要
聚
合
S
U
M
前
，
在
进
行
聚
合
计
算
前
，
都
会
通
过
内
存
归
并
或
流
式
归
并
查
询
出
结
果
集
。
因
此
，
聚
合
归
并
是
在
之
前
介
绍
的
归
并
类
型
之
上
追
加
的
归
并
能
力
，
即
装
饰
者
模
式
。
 
3
.
7
 
总
结
 
通
过
以
上
内
容
介
绍
，
相
信
大
家
已
经
了
解
到
S
h
a
r
d
i
n
g
-
J
D
B
C
基
础
概
念
、
核
心
功
能
以
及
执
行
原
理
。
基
础
概
念
：
逻
辑
表
，
真
实
表
，
数
据
节
点
，
绑
定
表
，
广
播
表
，
分
片
键
，
分
片
算
法
，
分
片
策
略
，
主
键
生
成
策
略
核
心
功
能
：
数
据
分
片
，
读
写
分
离
执
行
流
程
：
S
Q
L
解
析
 
=
>
 
查
询
优
化
 
=
>
 
S
Q
L
路
由
 
=
>
 
S
Q
L
改
写
 
=
>
 
S
Q
L
执
行
 
=
>
 
结
果
归
并
接
下
来
我
们
将
通
过
一
个
个
d
e
m
o
，
来
演
示
S
h
a
r
d
i
n
g
-
J
D
B
C
实
际
使
用
方
法
。
 
4
.
水
平
分
表
 
 
 
前
面
已
经
介
绍
过
，
水
平
分
表
是
在
同
一
个
数
据
库
内
，
把
同
一
个
表
的
数
据
按
一
定
规
则
拆
到
多
个
表
中
。
在
快
速
入
门
里
，
我
们
已
经
对
水
平
分
库
进
行
实
现
，
这
里
不
再
重
复
介
绍
。
 
5
.
水
平
分
库
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 30 -->
5
.
水
平
分
库
 
 
 
前
面
已
经
介
绍
过
，
水
平
分
库
是
把
同
一
个
表
的
数
据
按
一
定
规
则
拆
到
不
同
的
数
据
库
中
，
每
个
库
可
以
放
在
不
同
的
服
务
器
上
。
接
下
来
看
一
下
如
何
使
用
S
h
a
r
d
i
n
g
-
J
D
B
C
实
现
水
平
分
库
，
咱
们
继
续
对
快
速
入
门
中
的
例
子
进
行
完
善
。
(
1
)
将
原
有
o
r
d
e
r
_
d
b
库
拆
分
为
o
r
d
e
r
_
d
b
_
1
、
o
r
d
e
r
_
d
b
_
2
(
2
)
分
片
规
则
修
改
由
于
数
据
库
拆
分
了
两
个
，
这
里
需
要
配
置
两
个
数
据
源
。
分
库
需
要
配
置
分
库
的
策
略
，
和
分
表
策
略
的
意
义
类
似
，
通
过
分
库
策
略
实
现
数
据
操
作
针
对
分
库
的
数
据
库
进
行
操
作
。
 
分
库
策
略
定
义
方
式
如
下
：
#
 
定
义
多
个
数
据
源
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
n
a
m
e
s
 
=
 
m
1
,
m
2
 
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
.
t
y
p
e
 
=
 
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
3
3
0
6
/
o
r
d
e
r
_
d
b
_
1
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
1
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
 
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
2
.
t
y
p
e
 
=
 
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
2
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
2
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
3
3
0
6
/
o
r
d
e
r
_
d
b
_
2
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
2
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
2
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
.
.
.
#
 
分
库
策
略
，
以
u
s
e
r
_
i
d
为
分
片
键
，
分
片
策
略
为
u
s
e
r
_
i
d
 
%
 
2
 
+
 
1
，
u
s
e
r
_
i
d
为
偶
数
操
作
m
1
数
据
源
，
否
则
操
作
m
2
。
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
d
a
t
a
b
a
s
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
s
h
a
r
d
i
n
g
‐
c
o
l
u
m
n
 
=
 
u
s
e
r
_
i
d
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
o
r
d
e
r
.
d
a
t
a
b
a
s
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
a
l
g
o
r
i
t
h
m
‐
e
x
p
r
e
s
s
i
o
n
 
=
 
m
$
‐
>
{
u
s
e
r
_
i
d
 
%
 
2
 
+
 
1
}
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 31 -->
S
h
a
r
d
i
n
g
-
J
D
B
C
支
持
以
下
几
种
分
片
策
略
：
不
管
理
分
库
还
是
分
表
，
策
略
基
本
一
样
。
s
t
a
n
d
a
r
d
：
标
准
分
片
策
略
，
对
应
S
t
a
n
d
a
r
d
S
h
a
r
d
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
。
提
供
对
S
Q
L
语
句
中
的
=
,
 
I
N
和
B
E
T
W
E
E
N
 
A
N
D
的
分
片
操
作
支
持
。
S
t
a
n
d
a
r
d
S
h
a
r
d
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
只
支
持
单
分
片
键
，
提
供
P
r
e
c
i
s
e
S
h
a
r
d
i
n
g
A
l
g
o
r
i
t
h
m
和
R
a
n
g
e
S
h
a
r
d
i
n
g
A
l
g
o
r
i
t
h
m
两
个
分
片
算
法
。
P
r
e
c
i
s
e
S
h
a
r
d
i
n
g
A
l
g
o
r
i
t
h
m
是
必
选
的
，
用
于
处
理
=
和
I
N
的
分
片
。
R
a
n
g
e
S
h
a
r
d
i
n
g
A
l
g
o
r
i
t
h
m
是
可
选
的
，
用
于
处
理
B
E
T
W
E
E
N
 
A
N
D
分
片
，
如
果
不
配
置
R
a
n
g
e
S
h
a
r
d
i
n
g
A
l
g
o
r
i
t
h
m
，
S
Q
L
中
的
B
E
T
W
E
E
N
 
A
N
D
将
按
照
全
库
路
由
处
理
。
c
o
m
p
l
e
x
：
符
合
分
片
策
略
，
对
应
C
o
m
p
l
e
x
S
h
a
r
d
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
。
复
合
分
片
策
略
。
提
供
对
S
Q
L
语
句
中
的
=
,
 
I
N
和
B
E
T
W
E
E
N
 
A
N
D
的
分
片
操
作
支
持
。
C
o
m
p
l
e
x
S
h
a
r
d
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
支
持
多
分
片
键
，
由
于
多
分
片
键
之
间
的
关
系
复
杂
，
因
此
并
未
进
行
过
多
的
封
装
，
而
是
直
接
将
分
片
键
值
组
合
以
及
分
片
操
作
符
透
传
至
分
片
算
法
，
完
全
由
应
用
开
发
者
实
现
，
提
供
最
大
的
灵
活
度
。
i
n
l
i
n
e
：
行
表
达
式
分
片
策
略
，
对
应
I
n
l
i
n
e
S
h
a
r
d
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
。
使
用
G
r
o
o
v
y
的
表
达
式
，
提
供
对
S
Q
L
语
句
中
的
=
和
I
N
的
分
片
操
作
支
持
，
只
支
持
单
分
片
键
。
对
于
简
单
的
分
片
算
法
，
可
以
通
过
简
单
的
配
置
使
用
，
从
而
避
免
繁
琐
的
J
a
v
a
代
码
开
发
，
如
:
 
t
_
u
s
e
r
_
$
-
>
{
u
_
i
d
 
%
 
8
}
 
表
示
t
_
u
s
e
r
表
根
据
u
_
i
d
模
8
，
而
分
成
8
张
表
，
表
名
称
为
t
_
u
s
e
r
_
0
到
t
_
u
s
e
r
_
7
。
h
i
n
t
：
H
i
n
t
分
片
策
略
，
对
应
H
i
n
t
S
h
a
r
d
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
。
通
过
H
i
n
t
而
非
S
Q
L
解
析
的
方
式
分
片
的
策
略
。
对
于
分
片
字
段
非
S
Q
L
决
定
，
而
由
其
他
外
置
条
件
决
定
的
场
景
，
可
使
用
S
Q
L
 
H
i
n
t
灵
活
的
注
入
分
片
字
段
。
例
：
内
部
系
统
，
按
照
员
工
登
录
主
键
分
库
，
而
数
据
库
中
并
无
此
字
段
。
S
Q
L
 
H
i
n
t
支
持
通
过
J
a
v
a
 
A
P
I
和
S
Q
L
注
释
(
待
实
现
)
两
种
方
式
使
用
。
n
o
n
e
：
不
分
片
策
略
，
对
应
N
o
n
e
S
h
a
r
d
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
。
不
分
片
的
策
略
。
目
前
例
子
中
都
使
用
i
n
l
i
n
e
分
片
策
略
，
若
对
其
他
分
片
策
略
细
节
若
感
兴
趣
，
请
查
阅
官
方
文
档
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
h
a
r
d
i
n
g
s
p
h
e
r
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
(
3
)
插
入
测
试
修
改
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
O
r
d
e
r
方
法
，
插
入
数
据
中
包
含
不
同
的
u
s
e
r
_
i
d
 
执
行
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
O
r
d
e
r
:
 
#
分
库
策
略
，
如
何
将
一
个
逻
辑
表
映
射
到
多
个
数
据
源
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
<
逻
辑
表
名
称
>
.
d
a
t
a
b
a
s
e
‐
s
t
r
a
t
e
g
y
.
<
分
片
策
略
>
.
<
分
片
策
略
属
性
名
>
=
 
#
分
片
策
略
属
性
值
 
#
分
表
策
略
，
如
何
将
一
个
逻
辑
表
映
射
为
多
个
实
际
表
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
<
逻
辑
表
名
称
>
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
<
分
片
策
略
>
.
<
分
片
策
略
属
性
名
>
=
 
#
分
片
策
略
属
性
值
 
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
O
r
d
e
r
(
)
{
 
 
 
 
f
o
r
 
(
i
n
t
 
i
 
=
 
0
 
;
 
i
<
1
0
;
 
i
+
+
)
{
 
 
 
 
 
 
 
 
o
r
d
e
r
D
a
o
.
i
n
s
e
r
t
O
r
d
e
r
(
n
e
w
 
B
i
g
D
e
c
i
m
a
l
(
(
i
+
1
)
*
5
)
,
1
L
,
"
W
A
I
T
_
P
A
Y
"
)
;
 
 
 
 
}
 
 
 
 
f
o
r
 
(
i
n
t
 
i
 
=
 
0
 
;
 
i
<
1
0
;
 
i
+
+
)
{
 
 
 
 
 
 
 
 
o
r
d
e
r
D
a
o
.
i
n
s
e
r
t
O
r
d
e
r
(
n
e
w
 
B
i
g
D
e
c
i
m
a
l
(
(
i
+
1
)
*
1
0
)
,
2
L
,
"
W
A
I
T
_
P
A
Y
"
)
;
 
 
 
 
}
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 32 -->
通
过
日
志
可
以
看
出
，
根
据
u
s
e
r
_
i
d
的
奇
偶
不
同
，
数
据
分
别
落
在
了
不
同
数
据
源
，
达
到
目
标
。
 
（
4
）
查
询
测
试
调
用
快
速
入
门
的
查
询
接
口
进
行
测
试
：
L
i
s
t
<
M
a
p
>
 
s
e
l
e
c
t
O
r
d
e
r
b
y
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
"
o
r
d
e
r
I
d
s
"
)
L
i
s
t
<
L
o
n
g
>
 
o
r
d
e
r
I
d
s
)
;
 
通
过
日
志
发
现
，
s
h
a
r
d
i
n
g
-
j
d
b
c
将
s
q
l
路
由
到
m
1
和
m
2
：
问
题
分
析
：
由
于
查
询
语
句
中
并
没
有
使
用
分
片
键
u
s
e
r
_
i
d
，
所
以
s
h
a
r
d
i
n
g
-
j
d
b
c
将
广
播
路
由
到
每
个
数
据
结
点
。
下
边
我
们
在
s
q
l
中
添
加
分
片
键
进
行
查
询
。
在
O
r
d
e
r
D
a
o
中
定
义
接
口
：
@
S
e
l
e
c
t
(
{
"
<
s
c
r
i
p
t
>
"
,
 
 
 
 
 
 
 
 
 
"
 
s
e
l
e
c
t
"
,
 
 
 
 
 
 
 
 
 
"
 
*
 
"
,
 
 
 
 
 
 
 
 
 
"
 
f
r
o
m
 
t
_
o
r
d
e
r
 
t
 
"
,
 
 
 
 
 
 
 
 
 
"
w
h
e
r
e
 
t
.
o
r
d
e
r
_
i
d
 
i
n
"
,
 
 
 
 
 
 
 
 
 
"
<
f
o
r
e
a
c
h
 
c
o
l
l
e
c
t
i
o
n
=
'
o
r
d
e
r
I
d
s
'
 
i
t
e
m
=
'
i
d
'
 
o
p
e
n
=
'
(
'
 
s
e
p
a
r
a
t
o
r
=
'
,
'
 
c
l
o
s
e
=
'
)
'
>
"
,
 
 
 
 
 
 
 
 
 
"
#
{
i
d
}
"
,
 
 
 
 
 
 
 
 
 
"
<
/
f
o
r
e
a
c
h
>
"
,
 
 
 
 
 
 
 
 
 
"
 
a
n
d
 
t
.
u
s
e
r
_
i
d
 
=
 
#
{
u
s
e
r
I
d
}
 
"
,
 
 
 
 
 
 
 
 
 
"
<
/
s
c
r
i
p
t
>
"
 
}
)
 
L
i
s
t
<
M
a
p
>
 
s
e
l
e
c
t
O
r
d
e
r
b
y
U
s
e
r
A
n
d
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
"
u
s
e
r
I
d
"
)
 
I
n
t
e
g
e
r
 
u
s
e
r
I
d
,
@
P
a
r
a
m
(
"
o
r
d
e
r
I
d
s
"
)
L
i
s
t
<
L
o
n
g
>
 
o
r
d
e
r
I
d
s
)
;
 
 
编
写
测
试
方
法
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 33 -->
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
r
d
e
r
b
y
U
s
e
r
A
n
d
I
d
s
(
)
{
 
 
 
 
 
L
i
s
t
<
L
o
n
g
>
 
o
r
d
e
r
I
d
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
 
 
 
 
 
o
r
d
e
r
I
d
s
.
a
d
d
(
3
7
3
4
2
2
4
1
6
6
4
4
2
7
6
2
2
4
L
)
;
 
 
 
 
 
o
r
d
e
r
I
d
s
.
a
d
d
(
3
7
3
4
2
2
4
1
5
8
3
0
5
8
1
2
4
8
L
)
;
 
 
 
 
 
/
/
查
询
条
件
中
包
括
分
库
的
键
u
s
e
r
_
i
d
 
 
 
 
 
i
n
t
 
u
s
e
r
_
i
d
 
=
 
1
;
 
 
 
 
 
L
i
s
t
<
M
a
p
>
 
o
r
d
e
r
s
 
=
 
o
r
d
e
r
D
a
o
.
s
e
l
e
c
t
O
r
d
e
r
b
y
U
s
e
r
A
n
d
I
d
s
(
u
s
e
r
_
i
d
,
o
r
d
e
r
I
d
s
)
;
 
 
 
 
 
J
S
O
N
A
r
r
a
y
 
j
s
o
n
O
r
d
e
r
s
 
=
 
n
e
w
 
J
S
O
N
A
r
r
a
y
(
o
r
d
e
r
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
j
s
o
n
O
r
d
e
r
s
)
;
 
}
 
执
行
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
r
d
e
r
b
y
U
s
e
r
A
n
d
I
d
s
:
查
询
条
件
u
s
e
r
_
i
d
为
1
，
根
据
分
片
策
略
m
$
-
>
{
u
s
e
r
_
i
d
 
%
 
2
 
+
 
1
}
计
算
得
出
m
2
，
此
s
h
a
r
d
i
n
g
-
j
d
b
c
将
s
q
l
路
由
到
m
2
，
见
上
图
日
志
。
 
6
.
垂
直
分
库
 
 
 
前
面
已
经
介
绍
过
，
垂
直
分
库
是
指
按
照
业
务
将
表
进
行
分
类
，
分
布
到
不
同
的
数
据
库
上
面
，
每
个
库
可
以
放
在
不
同
的
服
务
器
上
，
它
的
核
心
理
念
是
专
库
专
用
。
接
下
来
看
一
下
如
何
使
用
S
h
a
r
d
i
n
g
-
J
D
B
C
实
现
垂
直
分
库
。
(
1
)
创
建
数
据
库
创
建
数
据
库
u
s
e
r
_
d
b
 
在
u
s
e
r
_
d
b
中
创
建
t
_
u
s
e
r
表
 
(
2
)
在
S
h
a
r
d
i
n
g
-
J
D
B
C
规
则
中
修
改
 
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
u
s
e
r
_
d
b
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
D
R
O
P
 
T
A
B
L
E
 
I
F
 
E
X
I
S
T
S
 
`
t
_
u
s
e
r
`
;
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
_
u
s
e
r
`
 
 
(
 
 
`
u
s
e
r
_
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
i
d
'
,
 
 
`
f
u
l
l
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
5
5
)
 
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
 
u
t
f
8
 
C
O
L
L
A
T
E
 
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
姓
名
'
,
 
 
`
u
s
e
r
_
t
y
p
e
`
 
c
h
a
r
(
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
用
户
类
型
'
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
u
s
e
r
_
i
d
`
)
 
U
S
I
N
G
 
B
T
R
E
E
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
 
=
 
u
t
f
8
 
C
O
L
L
A
T
E
 
=
 
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
 
R
O
W
_
F
O
R
M
A
T
 
=
 
D
y
n
a
m
i
c
;
#
 
新
增
m
0
数
据
源
，
对
应
u
s
e
r
_
d
b
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
n
a
m
e
s
 
=
 
m
0
,
m
1
,
m
2
.
.
.
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
0
.
t
y
p
e
 
=
 
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
d
r
u
i
d
.
p
o
o
l
.
D
r
u
i
d
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
0
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 34 -->
(
3
)
数
据
操
作
新
增
U
s
e
r
D
a
o
:
 
 
(
4
)
测
试
新
增
单
元
测
试
方
法
：
 
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
0
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
3
3
0
6
/
u
s
e
r
_
d
b
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
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
0
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
s
h
a
r
d
i
n
g
s
p
h
e
r
e
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
m
0
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
 
.
.
.
.
#
 
t
_
u
s
e
r
分
表
策
略
，
固
定
分
配
至
m
0
的
t
_
u
s
e
r
真
实
表
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
u
s
e
r
.
a
c
t
u
a
l
‐
d
a
t
a
‐
n
o
d
e
s
 
=
 
m
$
‐
>
{
0
}
.
t
_
u
s
e
r
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
u
s
e
r
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
s
h
a
r
d
i
n
g
‐
c
o
l
u
m
n
 
=
 
u
s
e
r
_
i
d
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
t
a
b
l
e
s
.
t
_
u
s
e
r
.
t
a
b
l
e
‐
s
t
r
a
t
e
g
y
.
i
n
l
i
n
e
.
a
l
g
o
r
i
t
h
m
‐
e
x
p
r
e
s
s
i
o
n
 
=
 
t
_
u
s
e
r
@
M
a
p
p
e
r
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
D
a
o
 
{
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
新
增
用
户
 
 
 
 
 
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
I
d
 
用
户
i
d
 
 
 
 
 
*
 
@
p
a
r
a
m
 
f
u
l
l
n
a
m
e
 
用
户
姓
名
 
 
 
 
 
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
I
n
s
e
r
t
(
"
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
 
t
_
u
s
e
r
(
u
s
e
r
_
i
d
,
 
f
u
l
l
n
a
m
e
)
 
v
a
l
u
e
(
#
{
u
s
e
r
I
d
}
,
#
{
f
u
l
l
n
a
m
e
}
)
"
)
 
 
 
 
i
n
t
 
i
n
s
e
r
t
U
s
e
r
(
@
P
a
r
a
m
(
"
u
s
e
r
I
d
"
)
L
o
n
g
 
u
s
e
r
I
d
,
@
P
a
r
a
m
(
"
f
u
l
l
n
a
m
e
"
)
S
t
r
i
n
g
 
f
u
l
l
n
a
m
e
)
;
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
根
据
i
d
列
表
查
询
多
个
用
户
 
 
 
 
 
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
I
d
s
 
用
户
i
d
列
表
 
 
 
 
 
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
S
e
l
e
c
t
(
{
"
<
s
c
r
i
p
t
>
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
 
s
e
l
e
c
t
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
 
*
 
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
 
f
r
o
m
 
t
_
u
s
e
r
 
t
 
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
 
w
h
e
r
e
 
t
.
u
s
e
r
_
i
d
 
i
n
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
<
f
o
r
e
a
c
h
 
c
o
l
l
e
c
t
i
o
n
=
'
u
s
e
r
I
d
s
'
 
i
t
e
m
=
'
i
d
'
 
o
p
e
n
=
'
(
'
 
s
e
p
a
r
a
t
o
r
=
'
,
'
 
c
l
o
s
e
=
'
)
'
>
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
#
{
i
d
}
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
<
/
f
o
r
e
a
c
h
>
"
,
 
 
 
 
 
 
 
 
 
 
 
 
"
<
/
s
c
r
i
p
t
>
"
 
 
 
 
}
)
 
 
 
 
L
i
s
t
<
M
a
p
>
 
s
e
l
e
c
t
U
s
e
r
b
y
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
"
u
s
e
r
I
d
s
"
)
L
i
s
t
<
L
o
n
g
>
 
u
s
e
r
I
d
s
)
;
 
}
@
T
e
s
t
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 35 -->
执
行
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
U
s
e
r
:
通
过
日
志
可
以
看
出
t
_
u
s
e
r
表
的
数
据
被
落
在
了
m
0
数
据
源
，
达
到
目
标
。
执
行
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
U
s
e
r
b
y
I
d
s
:
通
过
日
志
可
以
看
出
t
_
u
s
e
r
表
的
查
询
操
作
被
落
在
了
m
0
数
据
源
，
达
到
目
标
。
 
 
7
.
公
共
表
 
 
 
公
共
表
属
于
系
统
中
数
据
量
较
小
，
变
动
少
，
而
且
属
于
高
频
联
合
查
询
的
依
赖
表
。
参
数
表
、
数
据
字
典
表
等
属
于
此
类
型
。
可
以
将
这
类
表
在
每
个
数
据
库
都
保
存
一
份
，
所
有
更
新
操
作
都
同
时
发
送
到
所
有
分
库
执
行
。
接
下
来
看
一
下
如
何
使
用
S
h
a
r
d
i
n
g
-
J
D
B
C
实
现
公
共
表
。
(
1
)
创
建
数
据
库
分
别
在
u
s
e
r
_
d
b
、
o
r
d
e
r
_
d
b
_
1
、
o
r
d
e
r
_
d
b
_
2
中
创
建
t
_
d
i
c
t
表
：
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
U
s
e
r
(
)
{
 
 
 
 
f
o
r
 
(
i
n
t
 
i
 
=
 
0
 
;
 
i
<
1
0
;
 
i
+
+
)
{
 
 
 
 
 
 
 
 
L
o
n
g
 
i
d
 
=
 
i
 
+
 
1
L
;
 
 
 
 
 
 
 
 
u
s
e
r
D
a
o
.
i
n
s
e
r
t
U
s
e
r
(
i
d
,
"
姓
名
"
+
 
i
d
 
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
S
e
l
e
c
t
U
s
e
r
b
y
I
d
s
(
)
{
 
 
 
 
L
i
s
t
<
L
o
n
g
>
 
u
s
e
r
I
d
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
 
 
 
 
u
s
e
r
I
d
s
.
a
d
d
(
1
L
)
;
 
 
 
 
u
s
e
r
I
d
s
.
a
d
d
(
2
L
)
;
 
 
 
 
L
i
s
t
<
M
a
p
>
 
u
s
e
r
s
 
=
 
u
s
e
r
D
a
o
.
s
e
l
e
c
t
U
s
e
r
b
y
I
d
s
(
u
s
e
r
I
d
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
u
s
e
r
s
)
;
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 36 -->
(
2
)
在
S
h
a
r
d
i
n
g
-
J
D
B
C
规
则
中
修
改
 
(
3
)
数
据
操
作
新
增
D
i
c
t
D
a
o
：
 
(
4
)
字
典
操
作
测
试
新
增
单
元
测
试
方
法
：
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
_
d
i
c
t
`
 
 
(
 
 
`
d
i
c
t
_
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
 
C
O
M
M
E
N
T
 
'
字
典
i
d
'
,
 
 
`
t
y
p
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
5
0
)
 
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
 
u
t
f
8
 
C
O
L
L
A
T
E
 
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
字
典
类
型
'
,
 
 
`
c
o
d
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
5
0
)
 
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
 
u
t
f
8
 
C
O
L
L
A
T
E
 
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
字
典
编
码
'
,
 
 
`
v
a
l
u
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
5
0
)
 
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
 
u
t
f
8
 
C
O
L
L
A
T
E
 
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
字
典
值
'
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
d
i
c
t
_
i
d
`
)
 
U
S
I
N
G
 
B
T
R
E
E
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
 
=
 
u
t
f
8
 
C
O
L
L
A
T
E
 
=
 
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
 
R
O
W
_
F
O
R
M
A
T
 
=
 
D
y
n
a
m
i
c
;
 
#
 
指
定
t
_
d
i
c
t
为
公
共
表
s
p
r
i
n
g
.
s
h
a
r
d
i
n
g
s
p
h
e
r
e
.
s
h
a
r
d
i
n
g
.
b
r
o
a
d
c
a
s
t
‐
t
a
b
l
e
s
=
t
_
d
i
c
t
@
M
a
p
p
e
r
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
 
i
n
t
e
r
f
a
c
e
 
D
i
c
t
D
a
o
 
{
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
新
增
字
典
 
 
 
 
 
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
 
字
典
类
型
 
 
 
 
 
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
 
字
典
编
码
 
 
 
 
 
*
 
@
p
a
r
a
m
 
v
a
l
u
e
 
字
典
值
 
 
 
 
 
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
I
n
s
e
r
t
(
"
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
 
t
_
d
i
c
t
(
d
i
c
t
_
i
d
,
t
y
p
e
,
c
o
d
e
,
v
a
l
u
e
)
 
v
a
l
u
e
(
#
{
d
i
c
t
I
d
}
,
#
{
t
y
p
e
}
,
#
{
c
o
d
e
}
,
#
{
v
a
l
u
e
}
)
"
)
 
 
 
 
i
n
t
 
i
n
s
e
r
t
D
i
c
t
(
@
P
a
r
a
m
(
"
d
i
c
t
I
d
"
)
 
L
o
n
g
 
d
i
c
t
I
d
,
@
P
a
r
a
m
(
"
t
y
p
e
"
)
 
S
t
r
i
n
g
 
t
y
p
e
,
 
@
P
a
r
a
m
(
"
c
o
d
e
"
)
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
P
a
r
a
m
(
"
v
a
l
u
e
"
)
S
t
r
i
n
g
 
v
a
l
u
e
)
;
 
 
 
 
 
/
*
*
 
 
 
 
 
*
 
删
除
字
典
 
 
 
 
 
*
 
@
p
a
r
a
m
 
d
i
c
t
I
d
 
字
典
i
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
D
e
l
e
t
e
(
"
d
e
l
e
t
e
 
f
r
o
m
 
t
_
d
i
c
t
 
w
h
e
r
e
 
d
i
c
t
_
i
d
 
=
 
#
{
d
i
c
t
I
d
}
"
)
 
 
 
 
i
n
t
 
d
e
l
e
t
e
D
i
c
t
(
@
P
a
r
a
m
(
"
d
i
c
t
I
d
"
)
 
L
o
n
g
 
d
i
c
t
I
d
)
;
 
}
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 37 -->
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
D
i
c
t
(
)
{
 
 
d
i
c
t
D
a
o
.
i
n
s
e
r
t
D
i
c
t
(
1
L
,
"
u
s
e
r
_
t
y
p
e
"
,
"
0
"
,
"
管
理
员
"
)
;
 
 
d
i
c
t
D
a
o
.
i
n
s
e
r
t
D
i
c
t
(
2
L
,
"
u
s
e
r
_
t
y
p
e
"
,
"
1
"
,
"
操
作
员
"
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
D
e
l
e
t
e
D
i
c
t
(
)
{
 
 
d
i
c
t
D
a
o
.
d
e
l
e
t
e
D
i
c
t
(
1
L
)
;
 
 
d
i
c
t
D
a
o
.
d
e
l
e
t
e
D
i
c
t
(
2
L
)
;
 
}
 
 
执
行
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
D
i
c
t
：
通
过
日
志
可
以
看
出
，
对
t
_
d
i
c
t
的
表
的
操
作
被
广
播
至
所
有
数
据
源
。
测
试
删
除
字
典
，
观
察
是
否
把
所
有
数
据
源
中
该
 
公
共
表
的
记
录
删
除
。
 
（
5
）
字
典
关
联
查
询
测
试
字
典
表
已
在
各
各
分
库
存
在
，
各
业
务
表
即
可
和
字
典
表
关
联
查
询
。
定
义
用
户
关
联
查
询
d
a
o
：
在
U
s
e
r
D
a
o
中
定
义
：
/
*
*
 
 
*
 
根
据
i
d
列
表
查
询
多
个
用
户
，
关
联
查
询
字
典
表
 
 
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
I
d
s
 
用
户
i
d
列
表
 
 
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
S
e
l
e
c
t
(
{
"
<
s
c
r
i
p
t
>
"
,
 
 
 
 
 
 
 
 
 
"
 
s
e
l
e
c
t
"
,
 
 
 
 
 
 
 
 
 
"
 
*
 
"
,
 
 
 
 
 
 
 
 
 
"
 
f
r
o
m
 
t
_
u
s
e
r
 
t
 
,
t
_
d
i
c
t
 
b
"
,
 
 
 
 
 
 
 
 
 
"
 
w
h
e
r
e
 
t
.
u
s
e
r
_
t
y
p
e
 
=
 
b
.
c
o
d
e
 
a
n
d
 
t
.
u
s
e
r
_
i
d
 
i
n
"
,
 
 
 
 
 
 
 
 
 
"
<
f
o
r
e
a
c
h
 
c
o
l
l
e
c
t
i
o
n
=
'
u
s
e
r
I
d
s
'
 
i
t
e
m
=
'
i
d
'
 
o
p
e
n
=
'
(
'
 
s
e
p
a
r
a
t
o
r
=
'
,
'
 
c
l
o
s
e
=
'
)
'
>
"
,
 
 
 
 
 
 
 
 
 
"
#
{
i
d
}
"
,
 
 
 
 
 
 
 
 
 
"
<
/
f
o
r
e
a
c
h
>
"
,
 
 
 
 
 
 
 
 
 
"
<
/
s
c
r
i
p
t
>
"
 
}
)
 
L
i
s
t
<
M
a
p
>
 
s
e
l
e
c
t
U
s
e
r
I
n
f
o
b
y
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
"
u
s
e
r
I
d
s
"
)
L
i
s
t
<
L
o
n
g
>
 
u
s
e
r
I
d
s
)
;
 
定
义
测
试
方
法
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 38 -->
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
U
s
e
r
I
n
f
o
b
y
I
d
s
(
)
{
 
 
 
 
 
L
i
s
t
<
L
o
n
g
>
 
u
s
e
r
I
d
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
 
 
 
 
 
u
s
e
r
I
d
s
.
a
d
d
(
1
L
)
;
 
 
 
 
 
u
s
e
r
I
d
s
.
a
d
d
(
2
L
)
;
 
 
 
 
 
L
i
s
t
<
M
a
p
>
 
u
s
e
r
s
 
=
 
u
s
e
r
D
a
o
.
s
e
l
e
c
t
U
s
e
r
I
n
f
o
b
y
I
d
s
(
u
s
e
r
I
d
s
)
;
 
 
 
 
 
J
S
O
N
A
r
r
a
y
 
j
s
o
n
U
s
e
r
s
 
=
 
n
e
w
 
J
S
O
N
A
r
r
a
y
(
u
s
e
r
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
j
s
o
n
U
s
e
r
s
)
;
 
 
}
 
执
行
测
试
方
法
，
查
看
日
志
，
成
功
关
联
查
询
字
典
表
：
 
 
 
附
 
S
Q
L
支
持
说
明
 
详
细
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
s
h
a
r
d
i
n
g
s
p
h
e
r
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
o
c
u
m
e
n
t
/
c
u
r
r
e
n
t
/
c
n
/
f
e
a
t
u
r
e
s
/
s
h
a
r
d
i
n
g
/
u
s
e
-
n
o
r
m
s
/
s
q
l
/
说
明
：
以
下
为
官
方
显
示
内
容
，
具
体
是
否
适
用
以
实
际
测
试
为
准
 
。
支
持
的
S
Q
L
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 39 -->
S
Q
L
必
要
条
件
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
(
c
o
l
1
 
=
 
?
 
o
r
 
c
o
l
2
 
=
 
?
)
 
a
n
d
 
c
o
l
3
 
=
 
?
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
1
 
=
 
?
 
O
R
D
E
R
 
B
Y
 
c
o
l
2
 
D
E
S
C
 
L
I
M
I
T
 
?
 
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
*
)
,
 
S
U
M
(
c
o
l
1
)
,
 
M
I
N
(
c
o
l
1
)
,
 
M
A
X
(
c
o
l
1
)
,
 
A
V
G
(
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
1
 
=
 
?
 
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
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
2
 
=
 
?
 
G
R
O
U
P
 
B
Y
 
c
o
l
1
 
O
R
D
E
R
 
B
Y
 
c
o
l
3
 
D
E
S
C
 
L
I
M
I
T
 
?
,
 
?
 
I
N
S
E
R
T
 
I
N
T
O
 
t
b
l
_
n
a
m
e
 
(
c
o
l
1
,
 
c
o
l
2
,
…
)
 
V
A
L
U
E
S
 
(
?
,
 
?
,
 
…
.
)
 
I
N
S
E
R
T
 
I
N
T
O
 
t
b
l
_
n
a
m
e
 
V
A
L
U
E
S
 
(
?
,
 
?
,
…
.
)
 
I
N
S
E
R
T
 
I
N
T
O
 
t
b
l
_
n
a
m
e
 
(
c
o
l
1
,
 
c
o
l
2
,
 
…
)
 
V
A
L
U
E
S
 
(
?
,
 
?
,
 
…
.
)
,
 
(
?
,
 
?
,
 
…
.
)
 
U
P
D
A
T
E
 
t
b
l
_
n
a
m
e
 
S
E
T
 
c
o
l
1
 
=
 
?
 
W
H
E
R
E
 
c
o
l
2
 
=
 
?
 
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
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
1
 
=
 
?
 
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
 
t
b
l
_
n
a
m
e
 
(
c
o
l
1
 
i
n
t
,
 
…
)
 
A
L
T
E
R
 
T
A
B
L
E
 
t
b
l
_
n
a
m
e
 
A
D
D
 
c
o
l
1
 
v
a
r
c
h
a
r
(
1
0
)
 
D
R
O
P
 
T
A
B
L
E
 
t
b
l
_
n
a
m
e
 
T
R
U
N
C
A
T
E
 
T
A
B
L
E
 
t
b
l
_
n
a
m
e
 
C
R
E
A
T
E
 
I
N
D
E
X
 
i
d
x
_
n
a
m
e
 
O
N
 
t
b
l
_
n
a
m
e
 
D
R
O
P
 
I
N
D
E
X
 
i
d
x
_
n
a
m
e
 
O
N
 
t
b
l
_
n
a
m
e
 
D
R
O
P
 
I
N
D
E
X
 
i
d
x
_
n
a
m
e
 
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
1
 
=
 
?
 
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
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
不
支
持
的
S
Q
L
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 40 -->
S
Q
L
不
支
持
原
因
I
N
S
E
R
T
 
I
N
T
O
 
t
b
l
_
n
a
m
e
 
(
c
o
l
1
,
 
c
o
l
2
,
 
…
)
 
V
A
L
U
E
S
(
1
+
2
,
 
?
,
 
…
)
V
A
L
U
E
S
语
句
不
支
持
运
算
表
达
式
I
N
S
E
R
T
 
I
N
T
O
 
t
b
l
_
n
a
m
e
 
(
c
o
l
1
,
 
c
o
l
2
,
 
…
)
 
S
E
L
E
C
T
 
c
o
l
1
,
 
c
o
l
2
,
 
…
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
3
 
=
 
?
I
N
S
E
R
T
 
.
.
 
S
E
L
E
C
T
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
c
o
l
1
)
 
a
s
 
c
o
u
n
t
_
a
l
i
a
s
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
G
R
O
U
P
 
B
Y
 
c
o
l
1
 
H
A
V
I
N
G
 
c
o
u
n
t
_
a
l
i
a
s
 
>
 
?
H
A
V
I
N
G
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
1
 
U
N
I
O
N
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
2
U
N
I
O
N
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
1
 
U
N
I
O
N
 
A
L
L
 
S
E
L
E
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
2
U
N
I
O
N
 
A
L
L
S
E
L
E
C
T
 
*
 
F
R
O
M
 
d
s
.
t
b
l
_
n
a
m
e
1
包
含
s
c
h
e
m
a
S
E
L
E
C
T
 
S
U
M
(
D
I
S
T
I
N
C
T
 
c
o
l
1
)
,
 
S
U
M
(
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
详
见
D
I
S
T
I
N
C
T
支
持
情
况
详
细
说
明
S
Q
L
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
 
*
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
W
H
E
R
E
 
c
o
l
1
 
=
 
?
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
 
c
o
l
1
 
F
R
O
M
 
t
b
l
_
n
a
m
e
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
 
c
o
l
1
,
 
c
o
l
2
,
 
c
o
l
3
 
F
R
O
M
 
t
b
l
_
n
a
m
e
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
 
c
o
l
1
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
O
R
D
E
R
 
B
Y
 
c
o
l
1
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
 
c
o
l
1
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
O
R
D
E
R
 
B
Y
 
c
o
l
2
S
E
L
E
C
T
 
D
I
S
T
I
N
C
T
(
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
S
E
L
E
C
T
 
A
V
G
(
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
S
E
L
E
C
T
 
S
U
M
(
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
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
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
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
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
G
R
O
U
P
 
B
Y
 
c
o
l
1
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
D
I
S
T
I
N
C
T
 
c
o
l
1
 
+
 
c
o
l
2
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
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
D
I
S
T
I
N
C
T
 
c
o
l
1
)
,
 
S
U
M
(
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
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
D
I
S
T
I
N
C
T
 
c
o
l
1
)
,
 
c
o
l
1
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
G
R
O
U
P
 
B
Y
 
c
o
l
1
S
E
L
E
C
T
 
c
o
l
1
,
 
C
O
U
N
T
(
D
I
S
T
I
N
C
T
 
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
 
G
R
O
U
P
 
B
Y
 
c
o
l
1
D
I
S
T
I
N
C
T
支
持
情
况
详
细
说
明
支
持
的
S
Q
L
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 41 -->
S
Q
L
不
支
持
原
因
S
E
L
E
C
T
 
S
U
M
(
D
I
S
T
I
N
C
T
 
c
o
l
1
)
,
 
S
U
M
(
c
o
l
1
)
 
F
R
O
M
 
t
b
l
_
n
a
m
e
同
时
使
用
普
通
聚
合
函
数
和
D
I
S
T
I
N
C
T
聚
合
函
数
不
支
持
的
S
Q
L
 
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
