# Gogs安装文档

- 来源：JavaEE中级进修课资料（新版）\10.基于P2P的万信金融项目课程\day17\文档\项目部署文档\讲义\Gogs安装文档【海量资源尽在 666java.com】.pdf
- 页数：5
- 抽取：pypdf 文本层



<!-- page 1 -->
Gogs
安装文档
 
Gogs 
是一个用于代码仓库管理系统的开源项目，它使用
Git
作为代码管理工具，并在此基础上搭建起来
的
web
服务。
Gogs
与
GitHub
的功能相似，通常企业使用
Gogs
在局域网搭建自己的
Git
代码管理仓库。
一
. 
安装
Gogs
 
1
. 
新建
gogs
目录，编写
dock
er-compose.yml
文件：
2
. 
启动
Gogs: 
d
o
c
k
e
r
-
c
o
m
p
o
s
e
 
u
p
3
. 
浏览器访问：
[
http://127.0.0.1:10080/
]
4
. 
初次访问需要等待一段时间，然后进行基本配置，填写数据库用户名和密码：
gogs/gogs
g
o
g
s
:
 
 
i
m
a
g
e
:
 
d
o
c
k
e
r
.
i
o
/
g
o
g
s
/
g
o
g
s
:
l
a
t
e
s
t
 
 
l
i
n
k
s
:
 
 
 
 
-
 
m
y
s
q
l
-
g
o
g
s
:
m
y
s
q
l
 
 
p
o
r
t
s
:
 
 
 
 
-
 
"
1
0
0
2
2
:
2
2
"
 
 
 
 
-
 
"
1
0
0
8
0
:
3
0
0
0
"
 
 
v
o
l
u
m
e
s
:
 
 
 
 
-
 
"
.
/
d
a
t
a
:
/
d
a
t
a
/
g
o
g
s
"
 
 
 
 
-
 
"
.
/
r
e
p
o
:
/
d
a
t
a
/
g
i
t
/
g
o
g
s
-
r
e
p
o
s
i
t
o
r
i
e
s
"
 
 
r
e
s
t
a
r
t
:
 
a
l
w
a
y
s
m
y
s
q
l
-
g
o
g
s
:
 
 
i
m
a
g
e
:
 
d
o
c
k
e
r
.
i
o
/
m
y
s
q
l
:
5
.
7
.
2
1
 
 
p
o
r
t
s
:
 
 
 
 
-
 
"
3
3
0
6
:
3
3
0
6
"
 
 
v
o
l
u
m
e
s
:
 
 
 
 
-
 
.
/
m
y
s
q
l
-
g
o
g
s
/
m
y
s
q
l
:
/
v
a
r
/
l
i
b
/
m
y
s
q
l
 
 
 
 
-
 
.
/
m
y
s
q
l
-
g
o
g
s
/
c
o
n
f
.
d
:
/
e
t
c
/
m
y
s
q
l
/
c
o
n
f
.
d
:
r
w
 
 
e
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
:
 
 
 
 
-
 
M
Y
S
Q
L
_
D
A
T
A
B
A
S
E
=
g
o
g
s
 
 
 
 
-
 
M
Y
S
Q
L
_
U
S
E
R
=
g
o
g
s
 
 
 
 
-
 
M
Y
S
Q
L
_
P
A
S
S
W
O
R
D
=
g
o
g
s
 
 
 
 
-
 
M
Y
S
Q
L
_
R
O
O
T
_
P
A
S
S
W
O
R
D
=
r
o
o
t
 
 
c
o
m
m
a
n
d
:
 
m
y
s
q
l
d
 
-
-
l
o
w
e
r
_
c
a
s
e
_
t
a
b
l
e
_
n
a
m
e
s
=
1
 
-
-
c
h
a
r
a
c
t
e
r
-
s
e
t
-
s
e
r
v
e
r
=
u
t
f
8
m
b
4
 
-
-
c
o
l
l
a
t
i
o
n
-
s
e
r
v
e
r
=
u
t
f
8
m
b
4
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
 
 
r
e
s
t
a
r
t
:
 
a
l
w
a
y
s
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 2 -->
5
. 
初始化成功后，即可通过注册新建用户：
http://127.0.0.1:10080/user/sign_up
6
. 
注册成功即可登录
二
. 
新建仓库
 
1
. 
登录后，即可新建仓库：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 3 -->
2
. 
项目新建成功，进入项目主页，通过项目主页即可访问项目内容，并得到项目的
Git
仓库地址：
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 4 -->
三
. 
使用
Git
管理项目
 
在
Idea
中集成
Git
，并用
Git
管理万信金融项目。
1
. 
设置
Git
在本机安装
Git
，并在
Idea
中设置
Git
路径
设置修改代码后父级目录颜色变化：
2
. 
从
Gogs
仓库检出项目
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090

<!-- page 5 -->
打开
idea
，按下图菜单指示从
Gogs
克隆项目：
输入项目的
Git
仓库地址进行克隆：
3
. 
克隆完毕后，在工程根目录创建
 .gitignor
e
，此文件中记录了在提交代码时哪些文件或目录被忽略
4
. 
把之前开发好的项目代码复制到该目录中
5
. 
执行
add
6
. 
执行
commit 
提交文件到本地仓库
7
. 
提交到
Gogs
远程仓库
.
i
d
e
a
/
t
a
r
g
e
t
/
*
.
i
m
l
北京市昌平区建材城西路金燕龙办公楼一层   电话：400-618-9090
