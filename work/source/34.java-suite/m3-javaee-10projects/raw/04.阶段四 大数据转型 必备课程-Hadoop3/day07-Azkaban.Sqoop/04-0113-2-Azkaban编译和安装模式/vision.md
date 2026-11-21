# 画面线理解：2-Azkaban编译和安装模式

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\2-Azkaban编译和安装模式【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:29, 01:15, 01:57, 02:17, 02:39, 03:20, 06:20, 08:55, 09:22, 09:59, 10:24, 11:00, 11:17, 11:46
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 08:57:17

1) 这一组画面整体在讲如何编译安装 Azkaban 3.51.0 版本。

2) 按时间顺序列出每张画面的要点：
画面 1：
- 内容：讲解 Azkaban 安装的“编译”步骤，说明使用 JDK 1.8 编译，若服务器用 JDK 1.7 则需切换。
- 代码命令：
  cd /export/softwares/
  wget https://github.com/azkaban/azkaban/archive/3.51.0.tar.gz
  tar -zxvf 3.51.0.tar.gz -C ../servers/
  cd /export/servers/azkaban-3.51.0/
  yum -y install git
  yum -y install gcc-c++
  ./gradlew build installDist -x test
- 说明：编译完成后会生成 azkaban-exec-server 等安装包。

画面 2：
- 内容：在 SecureCRT 中，用户正在解压一个名为 “apache-flume-1.8.0-bin.tar.gz” 的文件，但因网络问题（rz waiting to receive...）导致解压失败，弹出文件传输对话框。

画面 3：
- 内容：在 SecureCRT 中，用户已进入 azkaban-3.51.0 的源码目录，查看了其目录结构，然后切换到 /servers/ 目录。

3) 无其他需要抄录的内容。

4) 无 PPT 标题、架构图/流程图、表格数据。

5) 无。
