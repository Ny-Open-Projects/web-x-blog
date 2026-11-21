# 画面线理解：23.课程总结

- 阶段：03.阶段三 好客租房(生活服务)项目
- 章节：day18-项目发布以及各种服务集群搭建
- 源文件：03.阶段三 好客租房(生活服务)项目\day18-项目发布以及各种服务集群搭建\23.课程总结【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:00, 00:32, 01:43, 02:02, 02:20, 02:25, 02:32, 03:25, 03:33, 03:42, 03:57, 04:02, 04:11, 04:20
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 00:02:07

1) 这一组画面整体在讲一个名为“haoke”的分布式系统从部署架构、数据库、中间件到项目打包和前端配置的完整技术实现过程。

2) 按时间顺序列出每张画面的要点：
画面1：展示课程目录结构，当前位于“1、部署架构”章节，右侧显示部署架构图，包含Nginx、Redis、MySQL、Elasticsearch、RocketMQ、Zookeeper等组件及其连接关系。
画面2：鼠标选中目录结构中的“2、部署计划”，但画面内容未变，仍显示“1、部署架构”图。
画面3：切换到“2.2、部署Redis集群”章节，显示创建Redis主从节点的Docker命令和配置文件内容。
画面4：鼠标选中目录结构中的“2.4、部署RocketMQ集群”，但画面内容未变，仍显示“2.3.3、文档mapping”配置。
画面5：切换到“2.5.2、实施”章节，显示创建Zookeeper集群的Docker命令。
画面6：切换到“3、项目打包”章节，显示“3.1、打包springboot项目”的内容。
画面7：在“3.1、打包springboot项目”中，展示添加Spring Boot Maven插件的配置代码。
画面8：在“3.2、构建Ant Design Pro”中，展示执行npm install命令的终端界面。
画面9：在“3.4、配置虚拟域名”中，展示Nginx配置文件，用于代理管理后台。
画面10：在“3.5、nginx反向代理websocket”中，展示Nginx配置文件，用于代理WebSocket连接。
画面11：在浏览器中访问haoke系统首页，显示前端页面和控制台错误日志。
画面12：在浏览器中访问haoke系统首页，页面内容切换为“南桥百联旁 80-90m²线高层”广告。
画面13：在浏览器中访问haoke系统首页，页面内容切换为“一线江景度假房 11月收官广告”。
画面14：在浏览器中打开SwitchHosts!工具，显示生产环境的主机配置，包括manage.haoke.com和im.haoke.com。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（逐字抄录）：
画面3：
```bash
#创建容器
docker create --name ms_node1 -v /var/lib/mysql -v /data/mysql/haoke/master01/conf:/etc/my.cnf -p 13310:3306 -e MYSQL_ROOT_PASSWORD=root percona:5.7.23

#启动
docker start ms_node1 & docker logs -f ms_node1

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
docker pull zookeeper:3.4

#创建容器
docker create --name zk01 --net host -e ZOO_MY_ID=1 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4

docker create --name zk02 --net host -e ZOO_MY_ID=2 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4

docker create --name zk03 --net host -e ZOO_MY_ID=3 -e ZOO_SERVERS="server.1=192.168.1.7:2888:3888 server.2=192.168.1.18:2888:3888 server.3=192.168.1.19:2888:3888" zookeeper:3.4

#启动容器
docker start zk01 & docker logs -f zk01
docker start zk02 & docker logs -f zk02
docker start zk03 & docker logs -f zk03
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
```nginx
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
```nginx
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
