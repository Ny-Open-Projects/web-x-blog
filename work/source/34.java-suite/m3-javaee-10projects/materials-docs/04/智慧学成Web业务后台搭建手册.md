# 智慧学成Web业务后台搭建手册

- 来源：04.阶段四 大数据转型 必备课程-Hadoop3\JavaEE中级进修课资料（新版）\08.基于大数据的智慧学成项目课程\day03\资料\第3章-课程分析\文档\智慧学成Web业务后台搭建手册【海量资源尽在 666java.com】.pdf
- 页数：3
- 抽取：pypdf 文本层



<!-- page 1 -->
智慧学成 Web 业务后台搭建  
1 简介  
智慧学成 Web 业务后台是 : 为 Web 前端提供数据的 API 平台 , 数据来⾃数据分析落地的业务库  , 源码路径 :
源码内⽬录结构如下 :
business.sql 是⼤数据分析落地的业务库表结构 , 项⽬启动前要导⼊到数据库 , 使⽤的数据库为 : xc-
online-mysql,
导⼊之前需要新建数据库 business, 步骤及命令如下 :
PS: 导⼊学成在线业务库时，  此数据库⽂件已导⼊
 
2 打包  
.
└──  授课资料
    └──  第 3 章 - 课程分析
        └──  code
            └──  xc-web
.
├── pom.xml
├── sql
│   └── business.sql // 数据库 , ⼤数据分析落地的业务库
└── src
    ├── main
    │   ├── java
    │   │   └── // 项⽬源码 , 核⼼ API
    │   └── resources
    │       └── // 配置⽂件
    └── test
        └── // 测试类
-- 把  business.sql 上传到 xc-online-mysql 容器
-- 需要在 business.sql 所在⽬录 , 使⽤命令登陆 mysql, 
-- 1, 创建数据
create database business;
-- 2, 使⽤数据库
use business;
-- 导⼊表结构
source business.sql;
-- 也可以使⽤⼯具连接数据导⼊

<!-- page 2 -->
打包需要 Maven 及 Java 环境 , 并配置环境变量  !
在源码⽬录执⾏命令 , 命令如下 :
命令执⾏完成后⽣成  target ⽬录 , ⽬录内  xc-web-0.0.1-SNAPSHOT.jar 即  Web 业务后台程序
 
3 部署 & 启动  
xc-web.jar 需要部署在 docker 服务器上 , 占⽤端⼝ : 2019, 这⾥以 /opt ⽬录为例 :
接⼝地址是 : ip: 2019, 这 docker 服务器 ip 是 : 172.16.0.165, 访问地址为 : http://172.16.0.165:2019, 这⾥
推荐域名访问 , 172.16.0.165 映射的域名为 : xc-online, 最终访问地址为 : http://xc-online:2019
4, 测试  
智慧学成 Web 业务后台部署后 Web 前端使⽤时需要修改接⼝地址 , 配置⽂件是 : vue.conﬁg.js, 将  target
属性修改为 : http://xc-online:2019, 如下图所⽰ :
mvn clean package -DskipTests
# 上传   xc-web-0.0.1-SNAPSHOT.jar 到 /opt ⽬录
# 终端切换到 /opt
cd /opt
# 启动
nohup java -jar xc-web.jar &

<!-- page 3 -->
前端访问效果如下 :
