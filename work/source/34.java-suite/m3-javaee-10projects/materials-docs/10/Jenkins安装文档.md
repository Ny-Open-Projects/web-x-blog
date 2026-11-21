# Jenkins安装文档

- 来源：JavaEE中级进修课资料（新版）\10.基于P2P的万信金融项目课程\day17\文档\项目部署文档\讲义\Jenkins安装文档【海量资源尽在 666java.com】.pdf
- 页数：6
- 抽取：pypdf 文本层



<!-- page 1 -->
Jenkins
安装文档
 
一
. 
安装
Jenkins
 
本教程在
dock
er
下安装
Jenkins
：
1
. 
拉取镜像：
2
. 
创建容器：
3
. 
启动容器：
4
. 
通过浏览器访问
http://ip:8091
初次运行
Jenkins
会经过一个安装过程，一般情况使用默认配置，一直下一步安装即可，其中一步需要
输入密码，如下图所示：
分别执行如下命令即可得到初始密码
(
账户名默认是
admin)
d
o
c
k
e
r
 
p
u
l
l
 
j
e
n
k
i
n
s
c
i
/
b
l
u
e
o
c
e
a
n
d
o
c
k
e
r
 
c
r
e
a
t
e
 
-
-
n
a
m
e
 
j
e
n
k
i
n
s
 
-
u
 
r
o
o
t
 
-
p
 
8
0
9
1
:
8
0
8
0
 
-
-
p
r
i
v
i
l
e
g
e
d
=
t
r
u
e
 
 
-
v
 
j
e
n
k
i
n
s
-
d
a
t
a
:
/
v
a
r
/
j
e
n
k
i
n
s
_
h
o
m
e
 
 
-
v
 
/
v
a
r
/
r
u
n
/
d
o
c
k
e
r
.
s
o
c
k
:
/
v
a
r
/
r
u
n
/
d
o
c
k
e
r
.
s
o
c
k
 
 
 
-
v
 
/
h
o
m
e
/
j
e
n
k
i
n
s
:
/
h
o
m
e
 
 
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
j
e
n
k
i
n
s
c
i
/
b
l
u
e
o
c
e
a
n
d
o
c
k
e
r
 
s
t
a
r
t
 
j
e
n
k
i
n
s
d
o
c
k
e
r
 
e
x
e
c
 
-
i
t
 
j
e
n
k
i
n
s
 
/
b
i
n
/
b
a
s
h
c
a
t
 
/
v
a
r
/
j
e
n
k
i
n
s
_
h
o
m
e
/
s
e
c
r
e
t
s
/
i
n
i
t
i
a
l
A
d
m
i
n
P
a
s
s
w
o
r
d

<!-- page 2 -->
建议首次登录成功后，修改密码。
二
. Jenkins
常用插件安装
 
要想让
Jenkin
更好的和其他工具集成到一起工作，就需要安装一些常用的插件。

<!-- page 3 -->
搜索如下插件并安装：
 
三
. Jenkins
全局工具配置
 
Jenkins
在进行持续集成工作时依赖
Jdk1.8
、
Git
、
maven
，所以需要进行一些全局工具配置，如下图所
示：

<!-- page 4 -->
1
、
Maven
安装：

<!-- page 5 -->
可以采用
“
自动安装
”
，在上图中勾选自动安装，选择
maven
版本即可。或将
maven
程序目录拷贝到宿主
机
/home
下，按上图进行配置即可。
2
、
Jdk
安装配置
 
与
maven
安装相同，也可以采用自动安装或手动安装的方法。
3
、
Git
安装方法同上
git
安装完成配置如下图：
4
、配置
git
凭证

<!-- page 6 -->
此凭证用于远程从
git
仓库获取工程源代码，输入
git
仓库的账号和密码
有了该凭证后，
Jenkins
即可以从
Gogs
仓库中获取项目源码。
