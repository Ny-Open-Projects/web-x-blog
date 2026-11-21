# freemarker基础v1.1

- 来源：10.阶段十 万信金融项目\JavaEE中级进修课资料（新版）\09.基于微服务构建闪聚支付项目\day08 C扫B支付 生成门店二维码\讲义-pdf\freemarker基础v1.1【海量资源尽在 666java.com】.pdf
- 页数：13
- 抽取：pypdf 文本层



<!-- page 1 -->
F
r
e
e
m
a
r
k
e
基
础
 
 
1
 
F
r
e
e
M
a
r
k
e
r
 
入
门
 
1
.
1
 
F
r
e
e
M
a
r
k
e
r
介
绍
 
1
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
是
一
个
用
J
a
v
a
开
发
的
模
板
引
擎
 
 
 
常
用
的
j
a
v
a
模
板
引
擎
还
有
哪
些
？
J
s
p
、
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
、
T
h
y
m
e
l
e
a
f
 
、
V
e
l
o
c
i
t
y
 
等
。
 
2
、
模
板
+
数
据
模
型
=
输
出
 
 
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
并
不
关
心
数
据
的
来
源
，
只
是
根
据
模
板
的
内
容
，
将
数
据
模
型
在
模
板
中
显
示
并
输
出
文
件
（
通
常
为
h
t
m
l
，
也
可
以
生
成
其
它
格
式
的
文
本
文
件
）
1
、
数
据
模
型
数
据
模
型
在
j
a
v
a
中
可
以
是
基
本
类
型
也
可
以
L
i
s
t
、
M
a
p
、
P
o
j
o
等
复
杂
类
型
。
2
、
来
自
官
方
的
例
子
：
（
h
t
t
p
s
:
/
/
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
s
/
d
g
u
i
_
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
_
b
a
s
i
c
s
.
h
t
m
l
）
数
据
模
型
：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
模
板
：
输
出
：
 
 
1
.
2
 
F
r
e
e
M
a
r
k
e
r
快
速
入
门
 
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
作
为
s
p
r
i
n
g
m
v
c
一
种
视
图
格
式
，
默
认
情
况
下
S
p
r
i
n
g
M
V
C
支
持
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
视
图
格
式
。
需
要
创
建
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
+
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
工
程
用
于
测
试
模
板
。
1
.
2
.
1
 
创
建
测
试
工
程
 
创
建
一
个
t
e
s
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
 
的
测
试
工
程
专
门
用
于
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
的
功
能
测
试
。
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
父
工
程
指
定
了
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
的
版
本
 
p
o
m
.
x
m
l
文
件
如
下
：
 
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
a
p
a
c
h
e
.
c
o
m
m
o
n
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
c
o
m
m
o
n
s
‐
i
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
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
t
e
s
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
工
程
 
的
p
o
m
继
承
父
工
程
 
p
o
m
，
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
版
本
为
2
.
3
.
2
8
 
1
.
2
.
2
 
配
置
文
件
 
配
置
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
和
 
l
o
g
b
a
c
k
-
s
p
r
i
n
g
.
x
m
l
，
从
资
料
文
件
夹
拷
贝
这
两
个
文
件
，
进
行
更
改
，
 
l
o
g
b
a
c
k
-
s
p
r
i
n
g
.
x
m
l
无
需
更
改
，
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
内
容
如
下
：
 
1
.
2
.
3
 
创
建
模
型
类
 
在
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
的
测
试
工
程
下
创
建
模
型
类
型
用
于
测
试
 
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
0
8
8
 
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
t
e
s
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
e
s
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
 
#
指
定
服
务
名
 
 
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
f
t
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
 
 
 
 
t
e
m
p
l
a
t
e
‐
l
o
a
d
e
r
‐
p
a
t
h
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
/
t
e
m
p
l
a
t
e
s
/
 
 
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
D
a
t
a
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
 
S
t
u
d
e
n
t
 
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
 
n
a
m
e
;
/
/
姓
名
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
1
.
2
.
3
 
创
建
模
板
 
在
 
s
r
c
/
m
a
i
n
/
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
，
此
目
录
为
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
的
默
认
模
板
存
放
目
录
。
在
t
e
m
p
l
a
t
e
s
下
创
建
模
板
文
件
t
e
s
t
1
.
f
t
l
，
模
板
中
的
$
{
n
a
m
e
}
最
终
会
被
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
替
换
成
具
体
的
数
据
。
 
 
1
.
2
.
4
 
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
类
，
向
M
a
p
中
添
加
n
a
m
e
，
最
后
返
回
模
板
文
件
。
 
 
 
 
 
p
r
i
v
a
t
e
 
i
n
t
 
a
g
e
;
/
/
年
龄
 
 
 
 
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
 
b
i
r
t
h
d
a
y
;
/
/
生
日
 
 
 
 
p
r
i
v
a
t
e
 
F
l
o
a
t
 
m
o
n
d
y
;
/
/
钱
包
 
 
 
 
p
r
i
v
a
t
e
 
L
i
s
t
<
S
t
u
d
e
n
t
>
 
f
r
i
e
n
d
s
;
/
/
朋
友
列
表
 
 
 
 
p
r
i
v
a
t
e
 
S
t
u
d
e
n
t
 
b
e
s
t
F
r
i
e
n
d
;
/
/
最
好
的
朋
友
}
 
 
<
!
D
O
C
T
Y
P
E
 
h
t
m
l
>
<
h
t
m
l
>
<
h
e
a
d
>
 
 
 
 
<
m
e
t
a
 
c
h
a
r
s
e
t
=
"
u
t
f
‐
8
"
>
 
 
 
 
<
t
i
t
l
e
>
H
e
l
l
o
 
W
o
r
l
d
!
<
/
t
i
t
l
e
>
<
/
h
e
a
d
>
<
b
o
d
y
>
H
e
l
l
o
 
$
{
n
a
m
e
}
!
<
/
b
o
d
y
>
<
/
h
t
m
l
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
;
 
 
 
 
 
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
"
/
t
e
s
t
1
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
(
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
 
O
b
j
e
c
t
>
 
m
a
p
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
 
 
 
 
 
 
 
 
m
a
p
.
p
u
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
w
o
r
l
d
"
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 6 -->
1
.
2
.
5
 
创
建
启
动
类
 
 
1
.
2
.
6
 
测
试
 
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
8
0
8
8
/
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
/
t
e
s
t
1
屏
幕
显
示
：
H
e
l
l
o
 
w
o
r
l
d
!
 
2
 
F
r
e
e
M
a
r
k
e
r
 
基
础
指
令
 
2
.
1
 
数
据
模
型
 
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
静
态
化
依
赖
数
据
模
型
和
模
板
，
下
边
定
义
数
据
模
型
：
下
边
方
法
形
参
m
a
p
即
为
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
静
态
化
所
需
要
的
数
据
模
型
，
在
m
a
p
中
填
充
数
据
：
 
 
 
 
 
 
 
 
 
/
/
返
回
模
板
文
件
名
称
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
t
e
s
t
1
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
s
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
s
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
"
/
t
e
s
t
1
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
(
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
 
O
b
j
e
c
t
>
 
m
a
p
)
{
 
 
 
 
 
 
 
 
/
/
向
数
据
模
型
放
数
据
 
 
 
 
 
 
 
 
m
a
p
.
p
u
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
w
o
r
l
d
"
)
;
 
 
 
 
 
 
 
 
S
t
u
d
e
n
t
 
s
t
u
1
 
=
 
n
e
w
 
S
t
u
d
e
n
t
(
)
;
 
 
 
 
 
 
 
 
s
t
u
1
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
小
明
"
)
;
 
 
 
 
 
 
 
 
s
t
u
1
.
s
e
t
A
g
e
(
1
8
)
;
 
 
 
 
 
 
 
 
s
t
u
1
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
0
0
0
.
8
6
f
)
;
 
 
 
 
 
 
 
 
s
t
u
1
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
 
 
 
 
 
 
 
 
S
t
u
d
e
n
t
 
s
t
u
2
 
=
 
n
e
w
 
S
t
u
d
e
n
t
(
)
;
 
 
 
 
 
 
 
 
s
t
u
2
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
小
红
"
)
;
 
 
 
 
 
 
 
 
s
t
u
2
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
2
0
0
.
1
f
)
;
 
 
 
 
 
 
 
 
s
t
u
2
.
s
e
t
A
g
e
(
1
9
)
;
/
/
 
 
 
 
 
 
 
 
s
t
u
2
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
 
 
 
 
 
 
 
 
L
i
s
t
<
S
t
u
d
e
n
t
>
 
f
r
i
e
n
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
 
 
 
 
 
 
 
 
f
r
i
e
n
d
s
.
a
d
d
(
s
t
u
1
)
;
 
 
 
 
 
 
 
 
s
t
u
2
.
s
e
t
F
r
i
e
n
d
s
(
f
r
i
e
n
d
s
)
;
 
 
 
 
 
 
 
 
s
t
u
2
.
s
e
t
B
e
s
t
F
r
i
e
n
d
(
s
t
u
1
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 7 -->
2
.
2
 
L
i
s
t
指
令
 
本
节
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
，
模
板
中
使
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
的
指
令
，
关
于
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
的
指
令
需
要
知
道
：
 
在
t
e
s
t
1
.
f
t
l
模
板
中
使
用
l
i
s
t
指
令
遍
历
数
据
模
型
中
的
数
据
：
 
3
、
输
出
：
H
e
l
l
o
 
w
o
r
l
d
!
 
序
号
 
姓
名
 
年
龄
 
钱
包
 
1
 
小
明
 
1
8
 
1
,
0
0
0
.
8
6
 
2
 
小
红
 
1
9
 
2
0
0
.
1
 
 
 
 
 
 
 
 
L
i
s
t
<
S
t
u
d
e
n
t
>
 
s
t
u
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
 
 
 
 
 
 
 
 
s
t
u
s
.
a
d
d
(
s
t
u
1
)
;
 
 
 
 
 
 
 
 
s
t
u
s
.
a
d
d
(
s
t
u
2
)
;
 
 
 
 
 
 
 
 
/
/
向
数
据
模
型
放
数
据
 
 
 
 
 
 
 
 
m
a
p
.
p
u
t
(
"
s
t
u
s
"
,
s
t
u
s
)
;
 
 
 
 
 
 
 
 
/
/
准
备
m
a
p
数
据
 
 
 
 
 
 
 
 
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
u
d
e
n
t
>
 
s
t
u
M
a
p
 
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
 
 
 
 
 
 
 
 
s
t
u
M
a
p
.
p
u
t
(
"
s
t
u
1
"
,
s
t
u
1
)
;
 
 
 
 
 
 
 
 
s
t
u
M
a
p
.
p
u
t
(
"
s
t
u
2
"
,
s
t
u
2
)
;
 
 
 
 
 
 
 
 
/
/
向
数
据
模
型
放
数
据
 
 
 
 
 
 
 
 
m
a
p
.
p
u
t
(
"
s
t
u
1
"
,
s
t
u
1
)
;
 
 
 
 
 
 
 
 
/
/
向
数
据
模
型
放
数
据
 
 
 
 
 
 
 
 
m
a
p
.
p
u
t
(
"
s
t
u
M
a
p
"
,
s
t
u
M
a
p
)
;
 
 
 
 
 
 
 
 
/
/
返
回
模
板
文
件
名
称
 
 
 
 
 
 
 
 
r
e
t
u
r
n
 
"
t
e
s
t
1
"
;
 
 
 
 
}
1
、
注
释
，
即
<
#
‐
‐
和
‐
‐
>
，
介
于
其
之
间
的
内
容
会
被
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
忽
略
2
、
插
值
（
I
n
t
e
r
p
o
l
a
t
i
o
n
）
：
即
$
{
.
.
}
部
分
,
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
会
用
真
实
的
值
代
替
$
{
.
.
}
3
、
F
T
L
指
令
：
和
H
T
M
L
标
记
类
似
，
名
字
前
加
#
予
以
区
分
，
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
会
解
析
标
签
中
的
表
达
式
或
逻
辑
。
4
、
文
本
，
仅
文
本
信
息
，
这
些
不
是
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
的
注
释
、
插
值
、
F
T
L
指
令
的
内
容
会
被
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
忽
略
解
析
，
直
接
输
出
内
容
。
<
t
a
b
l
e
>
 
 
 
 
<
t
r
>
 
 
 
 
<
t
d
>
序
号
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
姓
名
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
年
龄
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
钱
包
<
/
t
d
>
 
 
 
 
<
/
t
r
>
 
 
 
 
<
#
l
i
s
t
 
s
t
u
s
 
a
s
 
s
t
u
>
 
 
 
 
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
_
i
n
d
e
x
 
+
 
1
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
n
a
m
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
a
g
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
m
o
n
d
y
}
<
/
t
d
>
 
 
 
 
 
 
 
 
<
/
t
r
>
 
 
 
 
<
/
#
l
i
s
t
>
 
<
/
t
a
b
l
e
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 8 -->
2
.
3
 
遍
历
M
a
p
数
据
 
1
、
数
据
模
型
使
用
m
a
p
指
令
遍
历
数
据
模
型
中
的
s
t
u
M
a
p
。
2
、
模
板
 
3
、
输
出
 
 
2
.
4
 
i
f
指
令
 
说
明
：
_
i
n
d
e
x
：
得
到
循
环
的
下
标
，
使
用
方
法
是
在
s
t
u
后
边
加
"
_
i
n
d
e
x
"
，
它
的
值
是
从
0
开
始
 
输
出
s
t
u
1
的
学
生
信
息
：
<
b
r
/
>
姓
名
：
$
{
s
t
u
M
a
p
[
'
s
t
u
1
'
]
.
n
a
m
e
}
<
b
r
/
>
年
龄
：
$
{
s
t
u
M
a
p
[
'
s
t
u
1
'
]
.
a
g
e
}
<
b
r
/
>
输
出
s
t
u
1
的
学
生
信
息
：
<
b
r
/
>
姓
名
：
$
{
s
t
u
M
a
p
.
s
t
u
1
.
n
a
m
e
}
<
b
r
/
>
年
龄
：
$
{
s
t
u
M
a
p
.
s
t
u
1
.
a
g
e
}
<
b
r
/
>
遍
历
输
出
两
个
学
生
信
息
：
<
b
r
/
>
<
t
a
b
l
e
>
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
<
t
d
>
序
号
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
姓
名
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
年
龄
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
钱
包
<
/
t
d
>
 
 
 
 
<
/
t
r
>
<
#
l
i
s
t
 
s
t
u
M
a
p
?
k
e
y
s
 
a
s
 
k
>
<
t
r
>
 
 
 
 
<
t
d
>
$
{
k
_
i
n
d
e
x
 
+
 
1
}
<
/
t
d
>
 
 
 
 
<
t
d
>
$
{
s
t
u
M
a
p
[
k
]
.
n
a
m
e
}
<
/
t
d
>
 
 
 
 
<
t
d
>
$
{
s
t
u
M
a
p
[
k
]
.
a
g
e
}
<
/
t
d
>
 
 
 
 
<
t
d
 
>
$
{
s
t
u
M
a
p
[
k
]
.
m
o
n
d
y
}
<
/
t
d
>
<
/
t
r
>
<
/
#
l
i
s
t
>
<
/
t
a
b
l
e
>
输
出
s
t
u
1
的
学
生
信
息
：
姓
名
：
小
明
年
龄
：
1
8
输
出
s
t
u
1
的
学
生
信
息
：
姓
名
：
小
明
年
龄
：
1
8
遍
历
输
出
两
个
学
生
信
息
：
序
号
姓
名
年
龄
钱
包
 
 
 
 
 
 
1
小
红
1
9
2
0
0
.
1
 
 
 
 
 
 
 
2
小
明
1
8
1
,
0
0
0
.
8
6
 
 
 
 
 
 
 
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 9 -->
2
.
4
 
i
f
指
令
 
 
 
i
f
 
指
令
即
判
断
指
令
，
是
常
用
的
F
T
L
指
令
，
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
在
解
析
时
遇
到
i
f
会
进
行
判
断
，
条
件
为
真
则
输
出
i
f
中
间
的
内
容
，
否
则
跳
过
内
容
不
再
输
出
。
1
、
数
据
模
型
：
使
用
l
i
s
t
指
令
中
测
试
数
据
模
型
。
2
、
模
板
：
 
通
过
阅
读
上
边
的
代
码
，
实
现
的
功
能
是
：
如
果
姓
名
为
“
小
明
”
则
背
景
色
显
示
为
红
色
。
 
3
、
输
出
：
通
过
测
试
发
现
 
姓
名
为
小
明
的
背
景
色
为
红
色
。
2
.
5
 
运
算
符
 
1
、
算
数
运
算
符
 
F
r
e
e
M
a
r
k
e
r
表
达
式
中
完
全
支
持
算
术
运
算
,
F
r
e
e
M
a
r
k
e
r
支
持
的
算
术
运
算
符
包
括
:
+
,
 
-
 
,
 
*
 
,
 
/
 
,
 
%
 
2
、
逻
辑
运
算
符
 
逻
辑
运
算
符
有
如
下
几
个
:
 
逻
辑
与
:
&
&
 
逻
辑
或
:
|
|
 
逻
辑
非
:
!
 
逻
辑
运
算
符
只
能
作
用
于
布
尔
值
,
否
则
将
产
生
错
误
 
3
、
比
较
运
算
符
 
表
达
式
中
支
持
的
比
较
运
算
符
有
如
下
几
个
:
 
1
 
=
或
者
=
=
:
判
断
两
个
值
是
否
相
等
.
 
2
 
!
=
:
判
断
两
个
值
是
否
不
等
.
 
3
 
>
或
者
g
t
:
判
断
左
边
值
是
否
大
于
右
边
值
 
4
 
>
=
或
者
g
t
e
:
判
断
左
边
值
是
否
大
于
等
于
右
边
值
 
5
 
<
或
者
l
t
:
判
断
左
边
值
是
否
小
于
右
边
值
 
6
 
<
=
或
者
l
t
e
:
判
断
左
边
值
是
否
小
于
等
于
右
边
值
注
意
:
 
=
和
!
=
可
以
用
于
字
符
串
,
数
值
和
日
期
来
比
较
是
否
相
等
,
但
=
和
!
=
两
边
必
须
是
相
同
类
型
的
值
,
否
则
会
产
生
错
误
,
而
且
F
r
e
e
M
a
r
k
e
r
是
精
确
比
较
,
"
x
"
,
"
x
 
"
,
"
X
"
是
不
等
的
.
其
它
的
运
行
符
可
以
作
用
于
数
字
和
日
期
,
但
不
能
作
用
于
字
符
串
,
大
部
分
的
时
候
,
使
用
g
t
等
字
母
运
算
符
代
替
>
会
有
更
好
的
效
果
,
因
为
 
F
r
e
e
M
a
r
k
e
r
会
把
>
解
释
成
F
T
L
标
签
的
结
束
字
符
,
当
然
,
也
可
以
使
用
括
号
来
避
免
这
种
情
况
,
如
:
<
#
i
f
 
(
x
>
y
)
>
 
2
.
6
 
空
值
处
理
 
1
、
判
断
某
变
量
是
否
存
在
使
用
 
“
?
?
”
 
用
法
为
:
v
a
r
i
a
b
l
e
?
?
,
如
果
该
变
量
存
在
,
返
回
t
r
u
e
,
否
则
返
回
f
a
l
s
e
<
t
a
b
l
e
>
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
<
t
d
>
姓
名
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
年
龄
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
钱
包
<
/
t
d
>
 
 
 
 
<
/
t
r
>
 
 
 
 
<
#
l
i
s
t
 
s
t
u
s
 
a
s
 
s
t
u
>
 
 
 
 
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
 
<
#
i
f
 
s
t
u
.
n
a
m
e
 
=
=
'
小
明
'
>
s
t
y
l
e
=
"
b
a
c
k
g
r
o
u
n
d
:
r
e
d
;
"
<
/
#
i
f
>
>
$
{
s
t
u
.
n
a
m
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
a
g
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
 
>
$
{
s
t
u
.
m
o
n
d
y
}
<
/
t
d
>
 
 
 
 
 
 
 
 
<
/
t
r
>
 
 
 
 
<
/
#
l
i
s
t
>
 
<
/
t
a
b
l
e
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 10 -->
例
：
为
防
止
s
t
u
s
为
空
报
错
可
以
加
上
判
断
如
下
：
 
2
、
缺
失
变
量
默
认
值
使
用
 
“
!
”
 
使
用
!
要
以
指
定
一
个
默
认
值
，
当
变
量
为
空
时
显
示
默
认
值
。
例
：
 
$
{
n
a
m
e
!
'
'
}
表
示
如
果
n
a
m
e
为
空
显
示
空
字
符
串
。
 
如
果
是
嵌
套
对
象
则
建
议
使
用
（
）
括
起
来
。
例
：
 
$
{
(
s
t
u
.
b
e
s
t
F
r
i
e
n
d
.
n
a
m
e
)
!
'
'
}
表
示
，
如
果
s
t
u
或
b
e
s
t
F
r
i
e
n
d
或
n
a
m
e
为
空
默
认
显
示
空
字
符
串
。
 
2
.
7
 
内
置
对
象
 
在
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
中
可
以
访
问
R
e
q
u
e
s
t
、
S
e
s
s
i
o
n
等
内
置
对
象
。
R
e
q
u
e
s
t
：
 
用
于
获
取
R
e
q
u
e
s
t
对
象
中
的
a
t
t
r
i
b
u
t
e
对
象
。
S
e
s
s
i
o
n
：
用
于
获
取
S
e
s
s
i
o
n
对
象
中
的
a
t
t
r
i
b
u
t
e
对
象
。
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
e
t
e
r
s
：
用
于
获
取
R
e
q
u
e
s
t
对
象
的
p
a
r
a
m
e
t
e
r
参
数
（
浏
览
器
端
发
送
的
请
求
数
据
）
1
、
配
置
 
2
、
例
子
1
）
在
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
设
置
r
e
q
u
e
s
t
、
s
e
s
s
i
o
n
的
属
性
值
 
2
）
页
面
获
取
数
据
 
 
 
 
<
#
i
f
 
s
t
u
s
?
?
>
 
 
 
 
<
#
l
i
s
t
 
s
t
u
s
 
a
s
 
s
t
u
>
 
 
 
 
.
.
.
.
.
.
 
 
 
 
 
 
 
 
<
/
#
l
i
s
t
>
 
 
 
 
<
/
#
i
f
>
 
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
 
 
#
把
S
p
r
i
n
g
的
R
e
q
u
e
s
t
C
o
n
t
e
x
t
对
象
暴
露
为
变
量
r
c
 
 
 
 
 
 
e
x
p
o
s
e
‐
r
e
q
u
e
s
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
s
:
 
t
r
u
e
 
 
 
 
 
 
e
x
p
o
s
e
‐
s
e
s
s
i
o
n
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
s
:
 
t
r
u
e
/
/
测
试
内
置
对
象
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
A
t
t
r
i
b
u
t
e
(
"
a
t
t
r
1
"
,
"
t
e
s
t
"
)
;
H
t
t
p
S
e
s
s
i
o
n
 
s
e
s
s
i
o
n
 
=
 
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
S
e
s
s
i
o
n
(
)
;
s
e
s
s
i
o
n
.
s
e
t
A
t
t
r
i
b
u
t
e
(
"
s
e
s
s
i
o
n
1
"
,
 
"
u
s
e
r
1
"
)
;
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 11 -->
附
 
完
整
的
模
板
上
边
测
试
的
模
板
内
容
如
下
，
可
自
行
进
行
对
照
测
试
。
 
u
r
l
请
求
参
数
：
$
{
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
e
t
e
r
s
[
'
p
a
r
a
m
1
'
]
!
"
"
}
r
e
q
u
e
s
t
 
A
t
t
r
i
b
u
t
e
:
$
{
R
e
q
u
e
s
t
[
"
a
t
t
r
1
"
]
!
"
"
}
s
e
s
s
i
o
n
 
A
t
t
r
i
b
u
t
e
:
$
{
S
e
s
s
i
o
n
[
"
s
e
s
s
i
o
n
1
"
]
!
"
"
}
工
程
路
径
：
$
{
r
c
.
c
o
n
t
e
x
t
P
a
t
h
}
请
求
地
址
:
 
$
{
r
c
.
r
e
q
u
e
s
t
U
r
i
}
<
!
D
O
C
T
Y
P
E
 
h
t
m
l
>
<
h
t
m
l
>
<
h
e
a
d
>
 
 
 
 
<
m
e
t
a
 
c
h
a
r
s
e
t
=
"
u
t
f
‐
8
"
>
 
 
 
 
<
t
i
t
l
e
>
H
e
l
l
o
 
W
o
r
l
d
!
<
/
t
i
t
l
e
>
<
/
h
e
a
d
>
<
b
o
d
y
>
H
e
l
l
o
 
$
{
n
a
m
e
}
!
<
b
r
/
>
<
t
a
b
l
e
>
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
<
t
d
>
序
号
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
姓
名
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
年
龄
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
钱
包
<
/
t
d
>
 
 
 
 
<
/
t
r
>
 
 
 
 
<
#
l
i
s
t
 
s
t
u
s
 
a
s
 
s
t
u
>
 
 
 
 
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
_
i
n
d
e
x
 
+
 
1
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
 
<
#
i
f
 
s
t
u
.
n
a
m
e
 
=
=
'
小
明
'
>
s
t
y
l
e
=
"
b
a
c
k
g
r
o
u
n
d
:
r
e
d
;
"
<
/
#
i
f
>
>
$
{
s
t
u
.
n
a
m
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
a
g
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
 
>
$
{
s
t
u
.
m
o
n
d
y
}
<
/
t
d
>
 
 
 
 
 
 
 
 
<
/
t
r
>
 
 
 
 
<
/
#
l
i
s
t
>
 
<
/
t
a
b
l
e
>
<
b
r
/
>
<
b
r
/
>
输
出
s
t
u
1
的
学
生
信
息
：
<
b
r
/
>
姓
名
：
$
{
s
t
u
M
a
p
[
'
s
t
u
1
'
]
.
n
a
m
e
}
<
b
r
/
>
年
龄
：
$
{
s
t
u
M
a
p
[
'
s
t
u
1
'
]
.
a
g
e
}
<
b
r
/
>
输
出
s
t
u
1
的
学
生
信
息
：
<
b
r
/
>
姓
名
：
$
{
s
t
u
1
.
n
a
m
e
}
<
b
r
/
>
年
龄
：
$
{
s
t
u
1
.
a
g
e
}
<
b
r
/
>
遍
历
输
出
两
个
学
生
信
息
：
<
b
r
/
>
<
t
a
b
l
e
>
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
<
t
d
>
序
号
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
姓
名
<
/
t
d
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 12 -->
<
t
d
>
年
龄
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
钱
包
<
/
t
d
>
 
 
 
 
<
/
t
r
>
<
#
l
i
s
t
 
s
t
u
M
a
p
?
k
e
y
s
 
a
s
 
k
>
<
t
r
>
 
 
 
 
<
t
d
>
$
{
k
_
i
n
d
e
x
 
+
 
1
}
<
/
t
d
>
 
 
 
 
<
t
d
>
$
{
s
t
u
M
a
p
[
k
]
.
n
a
m
e
}
<
/
t
d
>
 
 
 
 
<
t
d
>
$
{
s
t
u
M
a
p
[
k
]
.
a
g
e
}
<
/
t
d
>
 
 
 
 
<
t
d
 
>
$
{
s
t
u
M
a
p
[
k
]
.
m
o
n
d
y
}
<
/
t
d
>
<
/
t
r
>
<
/
#
l
i
s
t
>
<
/
t
a
b
l
e
>
<
/
b
r
>
<
t
a
b
l
e
>
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
<
t
d
>
姓
名
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
年
龄
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
出
生
日
期
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
钱
包
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
最
好
的
朋
友
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
朋
友
个
数
<
/
t
d
>
 
 
 
 
 
 
 
 
<
t
d
>
朋
友
列
表
<
/
t
d
>
 
 
 
 
<
/
t
r
>
 
 
 
 
<
#
i
f
 
s
t
u
s
?
?
>
 
 
 
 
<
#
l
i
s
t
 
s
t
u
s
 
a
s
 
s
t
u
>
 
 
 
 
 
 
 
 
<
t
r
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
n
a
m
e
!
'
'
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
a
g
e
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
(
s
t
u
.
b
i
r
t
h
d
a
y
?
d
a
t
e
)
!
'
'
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
s
t
u
.
m
o
n
d
y
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
(
s
t
u
.
b
e
s
t
F
r
i
e
n
d
.
n
a
m
e
)
!
'
'
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
$
{
(
s
t
u
.
f
r
i
e
n
d
s
?
s
i
z
e
)
!
0
}
<
/
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
<
t
d
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
#
i
f
 
s
t
u
.
f
r
i
e
n
d
s
?
?
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
#
l
i
s
t
 
s
t
u
.
f
r
i
e
n
d
s
 
a
s
 
f
i
r
e
n
d
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
$
{
f
i
r
e
n
d
.
n
a
m
e
!
'
'
}
<
b
r
/
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
/
#
l
i
s
t
>
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
<
/
#
i
f
>
 
 
 
 
 
 
 
 
 
 
 
 
<
/
t
d
>
 
 
 
 
 
 
 
 
<
/
t
r
>
 
 
 
 
<
/
#
l
i
s
t
>
 
 
 
 
<
/
#
i
f
>
 
<
/
t
a
b
l
e
>
<
b
r
/
>
<
#
a
s
s
i
g
n
 
t
e
x
t
=
"
{
'
b
a
n
k
'
:
'
工
商
银
行
'
,
'
a
c
c
o
u
n
t
'
:
'
1
0
1
0
1
9
2
0
2
0
1
9
2
0
2
1
2
'
}
"
 
/
>
<
#
a
s
s
i
g
n
 
d
a
t
a
=
t
e
x
t
?
e
v
a
l
 
/
>
开
户
行
：
$
{
d
a
t
a
.
b
a
n
k
}
 
 
账
号
：
$
{
d
a
t
a
.
a
c
c
o
u
n
t
}
<
b
r
/
>
u
r
l
请
求
参
数
：
$
{
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
e
t
e
r
s
[
'
p
a
r
a
m
1
'
]
!
"
"
}
<
b
r
/
>
r
e
q
u
e
s
t
 
A
t
t
r
i
b
u
t
e
:
$
{
R
e
q
u
e
s
t
[
"
a
t
t
r
1
"
]
!
"
"
}
<
b
r
/
>
s
e
s
s
i
o
n
 
A
t
t
r
i
b
u
t
e
:
$
{
S
e
s
s
i
o
n
[
"
s
e
s
s
i
o
n
1
"
]
!
"
"
}
<
b
r
/
>
工
程
路
径
：
$
{
r
c
.
c
o
n
t
e
x
t
P
a
t
h
}
<
b
r
/
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 13 -->
附
 
S
p
r
i
n
g
 
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
配
置
s
p
r
i
n
g
.
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
a
l
l
o
w
-
r
e
q
u
e
s
t
-
o
v
e
r
r
i
d
e
=
f
a
l
s
e
 
#
 
S
e
t
 
w
h
e
t
h
e
r
 
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
 
a
t
t
r
i
b
u
t
e
s
 
a
r
e
 
a
l
l
o
w
e
d
 
t
o
o
v
e
r
r
i
d
e
 
(
h
i
d
e
)
 
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
 
g
e
n
e
r
a
t
e
d
 
m
o
d
e
l
 
a
t
t
r
i
b
u
t
e
s
 
o
f
 
t
h
e
 
s
a
m
e
 
n
a
m
e
.
 
s
p
r
i
n
g
.
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
a
l
l
o
w
-
s
e
s
s
i
o
n
-
o
v
e
r
r
i
d
e
=
f
a
l
s
e
 
#
 
S
e
t
 
w
h
e
t
h
e
r
 
H
t
t
p
S
e
s
s
i
o
n
 
a
t
t
r
i
b
u
t
e
s
 
a
r
e
 
a
l
l
o
w
e
d
 
t
o
 
o
v
e
r
r
i
d
e
 
(
h
i
d
e
)
 
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
 
g
e
n
e
r
a
t
e
d
m
o
d
e
l
 
a
t
t
r
i
b
u
t
e
s
 
o
f
 
t
h
e
 
s
a
m
e
 
n
a
m
e
.
 
s
p
r
i
n
g
.
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
c
a
c
h
e
=
f
a
l
s
e
 
#
 
E
n
a
b
l
e
 
t
e
m
p
l
a
t
e
 
c
a
c
h
i
n
g
.
s
p
r
i
n
g
.
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
-
8
 
#
 
T
e
m
p
l
a
t
e
 
e
n
c
o
d
i
n
g
.
 
s
p
r
i
n
g
.
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
c
h
e
c
k
-
t
e
m
p
l
a
t
e
-
l
o
c
a
t
i
o
n
=
t
r
u
e
 
#
C
h
e
c
k
 
t
h
a
t
 
t
h
e
 
t
e
m
p
l
a
t
e
s
 
l
o
c
a
t
i
o
n
 
e
x
i
s
t
s
.
 
s
p
r
i
n
g
.
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
c
o
n
t
e
n
t
-
t
y
p
e
=
t
e
x
t
/
h
t
m
l
 
#
 
C
o
n
t
e
n
t
-
T
y
p
e
 
v
a
l
u
e
.
s
p
r
i
n
g
.
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
 
#
 
E
n
a
b
l
e
 
M
V
C
 
v
i
e
w
 
r
e
s
o
l
u
t
i
o
n
 
f
o
r
 
t
h
i
s
 
t
e
c
h
n
o
l
o
g
y
.
s
p
r
i
n
g
.
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
e
x
p
o
s
e
-
r
e
q
u
e
s
t
-
a
t
t
r
i
b
u
t
e
s
=
f
a
l
s
e
 
#
 
S
e
t
 
w
h
e
t
h
e
r
 
a
l
l
 
r
e
q
u
e
s
t
 
a
t
t
r
i
b
u
t
e
s
 
s
h
o
u
l
d
 
b
e
 
a
d
d
e
d
 
t
o
t
h
e
 
m
o
d
e
l
 
p
r
i
o
r
 
t
o
 
m
e
r
g
i
n
g
 
w
i
t
h
 
t
h
e
 
t
e
m
p
l
a
t
e
.
 
s
p
r
i
n
g
.
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
e
x
p
o
s
e
-
s
e
s
s
i
o
n
-
a
t
t
r
i
b
u
t
e
s
=
f
a
l
s
e
 
#
 
S
e
t
w
h
e
t
h
e
r
 
a
l
l
 
H
t
t
p
S
e
s
s
i
o
n
 
a
t
t
r
i
b
u
t
e
s
 
s
h
o
u
l
d
 
b
e
 
a
d
d
e
d
 
t
o
 
t
h
e
 
m
o
d
e
l
 
p
r
i
o
r
 
t
o
 
m
e
r
g
i
n
g
 
w
i
t
h
 
t
h
e
 
t
e
m
p
l
a
t
e
.
s
p
r
i
n
g
.
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
e
x
p
o
s
e
-
s
p
r
i
n
g
-
m
a
c
r
o
-
h
e
l
p
e
r
s
=
t
r
u
e
 
#
 
S
e
t
 
w
h
e
t
h
e
r
 
t
o
 
e
x
p
o
s
e
 
a
 
R
e
q
u
e
s
t
C
o
n
t
e
x
t
 
f
o
r
 
u
s
e
 
b
y
S
p
r
i
n
g
'
s
 
m
a
c
r
o
 
l
i
b
r
a
r
y
,
 
u
n
d
e
r
 
t
h
e
 
n
a
m
e
 
"
s
p
r
i
n
g
M
a
c
r
o
R
e
q
u
e
s
t
C
o
n
t
e
x
t
"
.
 
s
p
r
i
n
g
.
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
p
r
e
f
e
r
-
ﬁ
l
e
-
s
y
s
t
e
m
-
a
c
c
e
s
s
=
t
r
u
e
 
#
 
P
r
e
f
e
r
 
ﬁ
l
e
 
s
y
s
t
e
m
 
a
c
c
e
s
s
 
f
o
r
 
t
e
m
p
l
a
t
e
 
l
o
a
d
i
n
g
.
 
F
i
l
e
 
s
y
s
t
e
m
 
a
c
c
e
s
s
 
e
n
a
b
l
e
s
 
h
o
t
 
d
e
t
e
c
t
i
o
n
 
o
f
t
e
m
p
l
a
t
e
 
c
h
a
n
g
e
s
.
 
s
p
r
i
n
g
.
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
p
r
e
ﬁ
x
=
 
#
 
P
r
e
ﬁ
x
 
t
h
a
t
 
g
e
t
s
 
p
r
e
p
e
n
d
e
d
 
t
o
 
v
i
e
w
 
n
a
m
e
s
 
w
h
e
n
 
b
u
i
l
d
i
n
g
 
a
U
R
L
.
 
s
p
r
i
n
g
.
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
r
e
q
u
e
s
t
-
c
o
n
t
e
x
t
-
a
t
t
r
i
b
u
t
e
=
 
#
 
N
a
m
e
 
o
f
 
t
h
e
 
R
e
q
u
e
s
t
C
o
n
t
e
x
t
 
a
t
t
r
i
b
u
t
e
 
f
o
r
 
a
l
l
 
v
i
e
w
s
.
s
p
r
i
n
g
.
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
s
e
t
t
i
n
g
s
.
*
=
 
#
 
W
e
l
l
-
k
n
o
w
n
 
F
r
e
e
M
a
r
k
e
r
 
k
e
y
s
 
w
h
i
c
h
 
w
i
l
l
 
b
e
 
p
a
s
s
e
d
 
t
o
 
F
r
e
e
M
a
r
k
e
r
'
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
.
 
s
p
r
i
n
g
.
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
s
u
ﬃ
x
=
 
#
 
S
u
ﬃ
x
 
t
h
a
t
 
g
e
t
s
 
a
p
p
e
n
d
e
d
 
t
o
 
v
i
e
w
 
n
a
m
e
s
 
w
h
e
n
 
b
u
i
l
d
i
n
g
 
a
 
U
R
L
.
s
p
r
i
n
g
.
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
t
e
m
p
l
a
t
e
-
l
o
a
d
e
r
-
p
a
t
h
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
/
t
e
m
p
l
a
t
e
s
/
 
#
 
C
o
m
m
a
-
s
e
p
a
r
a
t
e
d
 
l
i
s
t
 
o
f
 
t
e
m
p
l
a
t
e
 
p
a
t
h
s
.
s
p
r
i
n
g
.
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
v
i
e
w
-
n
a
m
e
s
=
 
#
 
W
h
i
t
e
 
l
i
s
t
 
o
f
 
v
i
e
w
 
n
a
m
e
s
 
t
h
a
t
 
c
a
n
 
b
e
 
r
e
s
o
l
v
e
d
.
 
请
求
地
址
:
 
$
{
r
c
.
r
e
q
u
e
s
t
U
r
i
}
<
b
r
/
>
<
/
b
o
d
y
>
<
/
h
t
m
l
>
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
