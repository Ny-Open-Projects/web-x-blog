# 8-HDFS的shell操作命令

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day02-HDFS
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day02-HDFS\8-HDFS的shell操作命令【海量资源尽在 ubkz.com】.mp4
- 时长 16分41秒（音频 1001s）
- 内容：声音线（教师逐段转写）+ 画面线（屏幕/PPT/代码）；已做同音技术术语纠错（Maven/JDK/Spring Boot 等）与品牌词清理

## 一、声音线（教师讲解，[mm:ss] 为出现时刻）

[00:00] 我们来学习如何对HDFS的文件进行操作来打开我们的HDFS这个文件系统比如说我要对这里的一些文件进行增删改查那如何去做呢有很多种方式我们来先看第一种就是通过命令行的方式对文件进行操作那么在这里边呢我们需要使用到Share命令行这里边有一个命令它的固定格式是HDFS
[00:30] DFS后面跟上一些参数就可以呢进行操作这里边呢我给大家列出来常用的一些命令咱们先看第一个那么这个命令是LS它可以去查看某个目录下面的所有的文件内容来我们来看一下直接我们可以在这里说HDFSDFS这个是固定的后面跟上杠LS是命令然后呢
[01:00] 比如说我要去想查看根目录下面文件内容我们直接回撤好稍等这个时候呢它就会列出了根目录下面的文件的详细信息这里看到的内容啊和我直接打开浏览器通过50070看到内容是一样的好这是第一个命令咱们接下来看第二个还有一个HDFS DFS Make DIR这个命令这个命令呢是创建一个目录或者说创建一个文件夹
[01:30] 来我们来看一下hdfs dfs-mkdir比如说我在根目录下面创建一个文件夹这个文件夹呢比如说叫test我们回车好稍等你可以去再次查看一下ls你会发现有了一个test那我们也可以通过浏览器刷新一下这里边多了一个test我们还可以呢在创建文件夹的时候呢加一个-p
[02:04] 这个杠P呢表示地归的创建你比如说我可以创建文件夹在Test里面呢创建文件夹叫AAA下面呢创建BBB来回车稍等那这个时候呢我们再来刷新一下打开TestTest里面有AAA下面有个BBBOK这是地归创建文件夹好那么接下来看下面这个命令叫move from local这个表示什么意思呢
[02:35] 这个move from local就是把本地词盘上的一个文件呢移动到hdfs上去我们来看一下move from local我们直接把它复制一下把这个语法复制一下站在这里我直接写吧hdfsdfs然后呢-move fromfrom local这个local呢我们来看是大写和小写是一个大写local本地
[03:06] form local就是从本地本地呢移动一个文件我看我这里有没有文件我这样回到我的加盟在这里边呢比如说我有个文件我们来touch一个吧touch一个文件a.t.t然后呢touch a.t.t我在这边随便写点内容hello world好就这么一个文件接下来呢我们来开始hdfsdfs-move
[03:38] 然后呢move什么呢move一个move from是不是我们来检查一下move from local然后呢后面呢写上一个当前的一个文件当前的什么呢a.txt移动到呢根目录下面比如说呢我移动到根目录下type的下面好我们来试一下走好这个时候我们来看一下你看当前目录的a.txt已经消失了
[04:15] 已经没有了没有了之后呢我们来刷新一下刷新之后呢回到我们的test目录你会发现这里多了一个A点贴体好这个就是将当前一个文件移动到HDFS上好这个呢了解一下接下来看下一个这个是move from local而这个呢这个还有个mv这个mv呢是将HDFS一个路径呢某一个文件移动到另外一个路径我们给大家演示一下
[04:44] 是hdfs-mv比如说呢我现在有个需求我现在要将test下面的a.txt移动到哪里呢我们回到根目录吧好移动到我们的temp目录好移动到我们的temp目录那这个时候呢我们可以这样做将根目录下面一个test目录下面的a.txt移动到根目录下面temp目录
[05:15] 大家看一下是这个是这个time目录ok移到这下面去我们来试一下看可不可以好走一下好走一下之后呢我们来看一下刷新一下看这个里边呢test里边a.txt已经没有了没有之后回到time目录你会发现这里多了一个a.txtok这就是在hdfs上呢进行一个目录的文件的移动ok而刚才这个呢
[05:47] 是将本地磁盘移动到HDFS好它是不一样的接下来看下一个一个put这个呢是一个文件的上传我们可以把一个本地的一个文件呢上传到HDFS来我们来试一下好在这里呢在这里呢比如说这个文件叫timer.txt我可以把它上传到HDFSHDFS然后呢dfs-puttimer.txt
[06:17] 比如说我要上传到HDF的根目录稍等好那我们来刷新一下这个刷新一下我们的根目录好这个时候呢已经过来了OK这是文件的上传我们不仅可以上传一个文件我们还可以上传一个文件夹比如说我要把这个shell4啊也上传到我们的根目录我们可以这样做那这个时候呢我们putshell4那这里面呢我们来看
[06:50] 我们上传到根目录Test下面吧上传到根目录下面Test走好稍等那接下来我们来看看Test下面有没有多一个shales刷新Test下面你会发现多了一个shalesshales里边是不是写脚本OK这是put命令put命令好接下来继续看还有一个叫open the to file这个什么意思呢这个可以将多个小文件呢
[07:22] 合并成一个大文件什么意思呢我们来看一下叫open the to file比如说在这里呢我再touch一个a.txt吧touch a.txt b.txtOK然后呢我在a.txt里边呢稍等这里边这个写错了move a.txt重命名a.txt我在a.txt里边呢我写一个hello然后两个hello
[07:59] 那接下来呢在b.ts里边呢我写两个word保存退出保存退出OK写了两个分别呢建了两个文件接下来呢我们可以利用这个open to file可以将这两个小文件呢合并成一个大文件放在hdfs上我们来试一下我们可以用hdfs dfs然后呢-open to file我来
[08:34] 看一下有没有写错open the to file然后呢我们可以写a.txtb.txt然后合并完之后呢把它放在我们的test目录下面然后有个hello.txt我们来看一下那如果说没问题我们的hello.txt里面呢就会出现这两个文件合并合并在一起的内容我们来看一下刷新一下在test目录里边有一个hello.txt
[09:06] 那么我们来点开点开之后我们可以通过这个档可以下载一下这个文件下载完之后呢我们来打开一下你就会发现呢它已经将这两个文件的内容呢进行了合并这个呢有什么用呢这个以后呢可以作为一个小文件的合并咱们注意一个小问题咱们这个HDFS里边呢我们呢尽量避免小文件过多
[09:35] 为什么呢因为一个小文件如果它也放在这个HDFS中它也会占一条原数据信息那么如果你的小文件过多就会造成NameNode压力过大所以说我们有时候需要将这个小文件进行合并好 这是这个问题好 接下来我们看看下面这个命令cat这个是查看一个文件的内容比如说HDFs DFS我们-cat我们查看hello
[10:04] 这个test下面hello.txt走我们看这个文件的内容好你看这个文件内容就出来了好这是这个好接下来呢还有一个cp命令这个呢是在hdfs里面呢拷贝一个文件或者文件夹这是cp我们来演示一下比如说呢我在这里呢想把这个hello.txt就是test下面的hello.txt拷贝到
[10:33] time棚下面去我们来看一下hdfs dfs然后呢这个地方是-cp我要将test下面的hello.txt拷贝到哪里去呢拷贝到time棚下面走来我们来看一下看time棚下面有没有多一个hello.txt哎是不是多了一个ok这个就是cp命令和我们的links很相似那接下来呢还有一个rm这个是删除一个文件或文件夹
[11:06] OK删除一个文件它是地归的删除我们来看一下比如说呢我在这里我想删除我想删除我的一个什么呢先删除文件嘛我想把这个timers tnt删除我们可以看我们可以在这里呢输个rm然后呢根目录下面一个timertmer.txt是这个文件嘛好我们把它删掉走好这个时候呢它有一个
[11:38] 它有个日志的输出它说呢这个文件呢已经放到了已经move到哪里去呢move到一个.tri这个其实就是一个垃圾这个垃圾回收站OK那么我们把这个其实删除的时候呢它是把这个文件呢放在了一个回收站里面那隔一段时间呢它会定期的清空这个回收站我们当时设置的时候呢默认是7天它就会自动清空OK这是一个IM
[12:07] 你也可以删除一个文件夹也是可以的来我们来看来刷一下这个文件就不存在了比如说我把这个test的目录删掉我们来试一下好这个地方呢test删除根目录下面的test稍等好你会发现它有个提醒它说这个test是一个文件夹是一个目录怎么做呢我们可以加个-r这个时候呢它可以递归的删除这个目录好稍等
[12:39] 他说已经放在这个回收站里面了我们来刷新一下你就会发现test已经没有了好那这里边呢他这些命令呢我们基本上呢就这么多还有两个命令呢是权限管理的命令一个是清积MODE-R77一个是清积ON这个呢第一个是改变他的文件的访问权限第二呢改变他的一个用户和用户组来我们先看第一个吧我们打开这个
[13:09] 比如说这个abc.txt它的权限是rwrr比如说我想去打开它所有权限我可以给它设一个权限我们来看一下怎么做呢我们可以做一个hdfsdfs-chimgmod然后这个里边我们可以在后面跟上一个-r这个-r一般是修改
[13:35] 文件夹的时候它可以把这个文件夹中所有的子文件夹修改成777我现在修改的是一个文件我可以不用加杠R然后呢直接777后面跟上一个文件那就轻松的777跟上一个根目的下面abc.txt来我们来看一下走好改完之后我们来刷新一下这个页面你会发现它的权限已经改成了777好接下来我们再去演示一个杠R的问题
[14:07] 我给大家再创建一个目录吧HDFS DFS然后呢这个地方是-MACDR这个地方呢我还是创建一个test创建一个test呢在test里面创建ABV我地归的创建加个-P就可以了地归的创建创建完之后咱们回到这里好test它的目录呢权限是这个进去它的权限是这个接下来
[14:36] 我要把这个目录中所有的子目录包括它本身它的权限都改成77怎么做呢我们可以hdfs dfs-清洁mod然后呢你可以加一个-r看这里一个参数这个参数-r然后呢777把根目录下面的test目录修改权限走走完之后呢我们再来看刷新
[15:07] 好这个test已经是77进去好这个也是77再进去它们都是77好这是一个递归修改权限我们还可以呢去修改它的对应的一个用户和用户组这个叫change on我们来看一下我们这个test目录我们回到根目录它的默认的这个用户呢是一个root用户组呢是supergroup
[15:36] 那这个时候呢我们也可以修改它的一个用户和用户组那这里面呢我没有其他用户我只有一个root用户大家呢可以自己新建一个用户我看一下我这里有没有用户我这里有个Hadoop用户我可以呢去修改把它的所属用户修改成Hadoop怎么做呢hdfs dfs-chain-own然后呢写个-2然后呢这个地方我们来写个
[16:07] 好那这个时候呢我们单独看test你看这里是不是已经修改了好了这就是它的一些全部的命令好这些命令呢大家呢做一个了解OK我们先呢
[16:38] 说到这里

## 二、画面线（屏幕 / PPT / 代码，VLM 抽帧抄录）

1) 这一组画面整体在讲什么（一句话）：
演示 HDFS 命令行操作，包括目录浏览、文件创建、移动、权限修改和文件内容查看等。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 显示 HDFS Web UI 的根目录，包含 abc.txt、export、tmp、user 四个条目。
画面 2: 在 SecureCRT 中执行命令 `hdfs dfs -ls /`，列出 HDFS 根目录下的文件和目录。
画面 3: 在 SecureCRT 中执行命令 `hdfs dfs -mkdir /test`，然后执行 `hdfs dfs -mkdir -p /test/aaa/bbb`，并再次执行 `hdfs dfs -ls /` 验证。
画面 4: 显示 HDFS Web UI 的 /test 目录，包含 aaa 文件。
画面 5: 显示 Typora 中的文档，标题为“1.8. hdfs的命令行使用”，其中列出 hdfs dfs 命令的语法和常用操作命令。
画面 6: SecureCRT 窗口空白，可能为切换或等待状态。
画面 7: 在 HDFS Web UI 中，点击文件 hello.txt 后弹出的文件信息框，显示 Block ID、Block Pool ID、Size、Availability 等信息。
画面 8: 在 SecureCRT 中执行命令 `hdfs dfs -appendToFile a.txt b.txt /test/hello.txt`，然后执行 `hdfs dfs -cat /test/hello.txt` 查看内容。
画面 9: 显示 HDFS Web UI 的根目录，包含 abc.txt、export、test、tmp、user 五个条目。
画面 10: 显示 HDFS Web UI 的根目录，包含 abc.txt、export、test、tmp、user 五个条目，鼠标悬停在 test 目录上。
画面 11: 在 SecureCRT 中执行命令 `hdfs dfs -op /test/hello.txt /tmp`，然后执行 `hdfs dfs -rm /timer.txt`，接着执行 `hdfs dfs -rm -r /test`。
画面 12: 在 SecureCRT 中执行命令 `hdfs dfs -chmod 777 /abc.txt`，然后执行 `hdfs dfs -mkdir -p /test/aaa/bbb`。
画面 13: 在 SecureCRT 中执行命令 `hdfs dfs -chmod -R 777 /test`。
画面 14: 显示 Typora 中的文档，标题为“1.8. hdfs的命令行使用”，其中列出 hdfs dfs 命令的语法和常用操作命令。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 2:
```
hdfs dfs -ls /
```
画面 3:
```
hdfs dfs -mkdir /test
hdfs dfs -mkdir -p /test/aaa/bbb
hdfs dfs -ls /
```
画面 4:
```
/test
```
画面 5:
```
语法: hdfs dfs 命令
hdfs dfs -ls / 查看根目录下的文件或者文件夹
hdfs dfs -mkdir -p /xxx/xxx (hdfs上面的创建文件夹)
hdfs dfs -mv localSourceDir (本地目录的文件或者文件夹) destDir (hdfs的路径)
hdfs dfs -put localFile hdfsDir
hdfs dfs -get hdfsFile localDir
hdfs dfs -appendToFile a.txt b.txt /test/hello.txt
hdfs dfs -cat hdfsSourceDir hdfsDestDir
hdfs dfs -cp hdfsSourceDir hdfsDestDir
hdfs dfs -rm -r [递归] 删除文件或者文件夹
hdfs dfs -chmod 777 /xxx
hdfs dfs -chown -R Hadoop:Hadoop /xxx
```
画面 7:
```
Block ID: 1073741933
Block Pool ID: BP-13329519-192.168.1.74-100-1555938164834
Generation Stamp: 1109
Size: 24
Availability:
  node02.Hadoop.com
  node02.Hadoop.com
  node01.Hadoop.com
```
画面 8:
```
hdfs dfs -appendToFile a.txt b.txt /test/hello.txt
hdfs dfs -cat /test/hello.txt
```
画面 9:
```
/
```
画面 10:
```
/
```
画面 11:
```
hdfs dfs -op /test/hello.txt /tmp
hdfs dfs -rm /timer.txt
hdfs dfs -rm -r /test
```
画面 12:
```
hdfs dfs -chmod 777 /abc.txt
hdfs dfs -mkdir -p /test/aaa/bbb
```
画面 13:
```
hdfs dfs -chmod -R 777 /test
```
画面 14:
```
语法: hdfs dfs 命令
hdfs dfs -ls / 查看根目录下的文件或者文件夹
hdfs dfs -mkdir -p /xxx/xxx (hdfs上面的创建文件夹)
hdfs dfs -mv localSourceDir (本地目录的文件或者文件夹) destDir (hdfs的路径)
hdfs dfs -put localFile hdfsDir
hdfs dfs -get hdfsFile localDir
hdfs dfs -appendToFile a.txt b.txt /test/hello.txt
hdfs dfs -cat hdfsSourceDir hdfsDestDir
hdfs dfs -cp hdfsSourceDir hdfsDestDir
hdfs dfs -rm -r [递归] 删除文件或者文件夹
hdfs dfs -chmod 777 /xxx
hdfs dfs -chown -R Hadoop:Hadoop /xxx
```

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 5 和 14: PPT 标题为“1.8. hdfs的命令行使用”，内容包括“语法: hdfs dfs 命令”和列出的 hdfs dfs 命令语法和常用操作命令。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）

