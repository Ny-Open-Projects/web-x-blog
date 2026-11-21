# 23.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\23.课程总结【海量资源尽在 ubkz.com】.mp4
- 时长 4分30秒（音频 270s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 好那么接下来呢我们对今天的课程呢做一个小节那么今天呢我们主要呢是将我们的项目呢去部署到我们的生产环境那么我们讲了我们的一个部署的一个架构那么这个架构呢希望大家呢能够去融会贯通那么在未来呢大家在做项目的时候呢可以在发布的时候呢把我们所有的一些这种服务以及我们所需要的一些这种服务的支持啊一些基础的服务啊等等那么都可以去做这样的一个架构或者说做这样的一个规划
[00:30] 然后呢我们也希望大家呢可以去按照我们的这个部署的这个步骤啊那么从我们最底层的一些基础服务的开始然后呢去做一个部署的一个计划然后呢可以去得出或者说计算出我们所需要的一些服务器的一些这种资源
[00:47] 那么当然了我们处于学习阶段呢我们的资源是有限的那么我们可能就需要在我们现有的资源上面去做一些这种分配那么有同学可能会看到啊我在部署的时候呢有些机器会比较卡那么这个是取决于这个我的机器的这个问题啊那么如果我们在在企业中去做正式项目的话那么相信在企业中一定会有一些比较优秀的资源会分配给你然后呢去让你部署这个项目的OK好那么我们部署了有什么呢有这个MySQL服务
[01:17] 那MySQL服务呢也做了一些这个集群包括有PXC集群也有这我们的MS集群还用了什么呢MyCat以及HAPopsy这样的一些相关的一些服务那么搭建了一个相对比较完整的这样一个MySQL的一个集群的服务这个集群服务呢大家可以基于这个基础之上呢去做一些这种横向的扩展那么OK那么这样的话呢就是一个比较相对比较完善的这样的一个集群了那么紧接着呢我们部署了我们的Redis
[01:44] 那我们在这所采用的是一个三组三重的一个架构那么同理也可以继续去扩充我们的RedisOK好那么我们又部署了什么Elixir的集群那么我们也是部署了一个最基本的一个集群就是三个节点的这样的一个集群然后我们又部署了RocketMQ的一个集群那么使用的是两个Must加两个Sleeve这样的一个集群那么总共需要有六个这个节点OK好那么我们后面又部署了一个ZK集群也是一个相对比较
[02:14] 简单的一个接群就是有三个这个节点好那么最后我们就去把我们项目的做了一些打包对吧那么打包我们讲了有sprint boot的项目打包那么怎么去做首先添加一个sprint boot maven这个插件然后要指定一个它的一个全路径然后我们执行这样的一个命令就可以去
[02:34] 按照我们所期望的去打成我们所最终所要运行的一个包其实就是我们得到一个加包那么得到这个加包之后呢我们就可以通过一个加码杠架这个命令去运行我们这个加包那么最多我们这个服务呢就可以跑起来了而这第一个那第二个呢我们是讲了一个按照敌人的一个这个打包那么我们通过一个污名的一个bill的这样的一个命令就可以把我们的这个页面呢
[02:59] 构建成一个静态页面去做一个部署那么其实呢我们如果不使用这个5米这个框架那么使用这个node.js所提供的npm的管理包的包的管理工具呢也是同样可以通过这个build的方式去做一个构建那么这样的话呢我们最终所发布的也是一些静态页面那么其实呢本质上面按照迪战跟我们自己去通过node.js去构建本质上呢都是一样的啊没有什么区别OK
[03:25] 那么后面我们又去安装了Nginx去设置了一系列的反向的代理包括我们managerweb系统的代理以及我们的一些设置了APImanager这样域名的访问后面我们又讲了是通过Nginx去反向代理到WebSocket这样的话就可以实现我们一个IM系统的一个这样的一个访问OK那么最后其实我们就是把我们的
[03:54] 这个系统把我们这个系统的去发布到我们的一个这个服务器上面那么发布到服务器上面呢可以看到我们最终的一个效果跟我们本地是一样的当然了我们也是通过
[04:05] 通过这样的一个域名去做一个访问大家一定要记住就是这个域名的访问一定要有你本地的这样的一个映射要不然的话他是不能够去访问成功的OK好嘞好那么这个就是我们以上今天所有的一些内容那么今天主要其实就是在做什么呢在做这个部署OK好那么那么关于这个小节呢那我们就先讲到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲一个名为“haoke”的分布式系统从部署架构、数据库、中间件到项目打包和前端配置的完整技术实现过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录结构，当前位于“1、部署架构”章节，右侧显示部署架构图，包含Nginx、Redis、MySQL、Elasticsearch、RocketMQ、Zookeeper等组件及其连接关系。
画面2：鼠标选中目录结构中的“2、部署计划”，但画面内容未变，仍显示“1、部署架构”图。
画面3：切换到“2.2、部署Redis集群”章节，显示创建Redis主从节点的Docker命令和配置文件内容。
画面4：鼠标选中目录结构中的“2.4、部署RocketMQ集群”，但画面内容未变，仍显示“2.3.3、文档mapping”配置。
画面5：切换到“2.5.2、实施”章节，显示创建Zookeeper集群的Docker命令。
画面6：切换到“3、项目打包”章节，显示“3.1、打包Spring Boot项目”的内容。
画面7：在“3.1、打包Spring Boot项目”中，展示添加Spring Boot Maven插件的配置代码。
画面8：在“3.2、构建Ant Design Pro”中，展示执行npm install命令的终端界面。
画面9：在“3.4、配置虚拟域名”中，展示Nginx配置文件，用于代理管理后台。
画面10：在“3.5、Nginx反向代理WebSocket”中，展示Nginx配置文件，用于代理WebSocket连接。
画面11：在浏览器中访问haoke系统首页，显示前端页面和控制台错误日志。
画面12：在浏览器中访问haoke系统首页，页面内容切换为“南桥百联旁 80-90m²线高层”广告。
画面13：在浏览器中访问haoke系统首页，页面内容切换为“一线江景度假房 11月收官广告”。
画面14：在浏览器中打开SwitchHosts!工具，显示生产环境的主机配置，包括manage.haoke.com和im.haoke.com。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3：
```bash
#创建容器
Docker create --name ms_node1 -v /var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
Docker start ms_node1 & Docker logs -f ms_node1

#创建用户和权限
create user 'haoke'@'%' identified by 'haoke';
grant replication slave on *.* to 'haoke'@'%';
flush privileges;

#查看master状态
show master status;

#slave
mkdir -p /data/mysql/haoke/slave01/conf
vim my.cnf

#输入如下内容
[mysqld]
server-id=2
#服务端，不可重复
sql_mode=STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION

#创建容器
```

画面5：
```bash
#拉取镜像
Docker pull ZooKeeper:3.4

#创建容器
Docker create --name zk01 --net host -e ZOO_MY_ID=1 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" ZooKeeper:3.4

Docker create --name zk02 --net host -e ZOO_MY_ID=2 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" ZooKeeper:3.4

Docker create --name zk03 --net host -e ZOO_MY_ID=3 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" ZooKeeper:3.4

#启动容器
Docker start zk01 & Docker logs -f zk01
Docker start zk02 & Docker logs -f zk02
Docker start zk03 & Docker logs -f zk03
```

画面6：
```xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <configuration>
        <!--替换成本机的类全路径-->
        <mainClass>cn.itcast.haoke.dubbo.server.DubboProvider</mainClass>
    </configuration>
    <executions>
        <execution>
            <goals>
                <goal>repackage</goal>
            </goals>
        </execution>
    </executions>
</plugin>
```

画面7：
```bash
mvn install -Dmaven.test.skip=true
```

画面8：
```bash
#建立npm命令进行构建，构建成功后会生成静态页面
npm build
```

画面9：
```Nginx
server {
    listen 80;
    server_name manage.haoke.com;

    #charset koi8-r;

    access_log logs/host.access.log main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location ~ ^/haoke/ {
        proxy_pass http://192.168.1.7:18080/;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
    }

    location / {
        root /haoke/publish/manage-web;
    }
}
```

画面10：
```Nginx
server {
    listen 80;
    server_name im.haoke.com;

    #charset koi8-r;

    access_log logs/host.access.log main;

    proxy_set_header X-Forwarded-Host $host;
    proxy_set_header X-Forwarded-Server $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;

    location / {
        proxy_pass http://192.168.1.19:18081;
        proxy_connect_timeout 600;
        proxy_read_timeout 600;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面1：架构图中，用户通过www.haoke.com访问DNS，DNS指向Nginx，Nginx通过负载均衡指向多个服务（如haoke-manage、haoke-web等），这些服务又分别连接到Redis、MySQL、Elasticsearch、RocketMQ、Zookeeper等中间件。

画面2：架构图结构与画面1相同，但未展示新内容。

5) 无。

