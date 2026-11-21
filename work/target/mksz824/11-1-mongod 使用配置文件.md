# 11-1-mongod 使用配置文件

上节课我们添加了 PATH 环境变量，可以用全局命令运行 mongod 了。但还有个问题：我们希望任务在后台执行，而不是在终端上输出一大堆信息。这就要用到 mongod 的一个选项。先用 help 列出所有选项，能看到有个 fork，注释是 server process。

加上 --fork 运行 mongod --dbpass --fork，它直接报错：fork has to be used with logpath or syslog。意思是想让进程在后台运行，必须指定一个日志地址来存放日志，这个日志会记录 MongoDB 运行期间的输出。于是先创建一个日志目录，选择系统用户安装软件后日常存放 log 的位置：/usr/local/var/log，我之前装的 nginx 的 log 就在这里。执行 mkdir -p /usr/local/var/log/mongodb 创建目录。老生常谈，注意权限，这个目录要属于当前用户。

有了目录就可以启动了。先设置 dbpath，再设置日志位置 logpath 为 /usr/local/var/log/mongodb 下随便取的一个文件名（会自动创建），最后调用 --fork。稍等片刻看到 child process started successfully，启动成功。验证一下：ps aux | grep mongodb，能看到进程在运行，--dbpass 对应的 PID 是 58247。想结束进程就用 kill -9 加上这个 PID，再查一次确实被 kill 掉了。

但这样参数非常长，输入很不方便。如果借助配置文件就方便多了，MongoDB 恰好支持这种形式。官方文档 configuration file options 描述了如何用文件完成配置，配置项用 YAML 书写，这种格式我们很熟悉也好用。文档还提到：如果用包管理器安装（Linux 的 YUM 或 APT、macOS 的 Brew），会自动在特定位置创建配置文件，Linux、macOS、Windows 各有对应位置。我们现在手动走的流程，正好演示了包管理器一步步做了什么。

第一个任务是创建配置文件。常见配置文件放置路径是 /usr/local/etc，etc 意思是"一系列其他的文件"，一般配置文件都放这里，ls 能看到 redis.conf 等其他软件的配置。在这里 touch 新建 mongodb.conf，用喜欢的编辑器打开编辑。把配置选项贴进去，注意命令行参数是一项一项的，而配置文件按分组管理，看起来更清晰。对应关系可以参考我提供的文档：某个命令行参数对应写到某个配置项下面。

三个大类：第一类 systemLog 是日志选项，destination 设为 file 表示日志是文件类型，path 写刚才创建的日志地址，logAppend 设为 true 表示日志源源不断追加写入而不是覆盖。第二类 storage 里的 dbPath 就是存放数据库文件的地方。第三类 processManagement 里 fork 设为 true，对应 --fork 选项。

配置完成后运行验证。mongod 读取配置的参数是 --config，后面跟上文件路径 /usr/local/etc/mongodb.conf。回车后输出和刚才一样，启动成功，用 ps 查看进程确实在运行。

到这里，mongod 启动的参数、配置和对应关系都比较清楚了。感兴趣的同学可以再用 Homebrew 装一遍，复制几行命令就行，会发现它内部过程和我们的手动流程高度相似。我甚至看过它对应的 Ruby 文件，里面的配置文件和我们写的非常相似。看到这些就不得不强调手动安装的好处：包管理器安装整个是黑盒，各种对应关系不清楚；手动安装能搞清楚文件和配置的关系，以后想修改选项就方便很多。要装其他平台的 MongoDB，去看官方文档，它永远是最好的指南。
