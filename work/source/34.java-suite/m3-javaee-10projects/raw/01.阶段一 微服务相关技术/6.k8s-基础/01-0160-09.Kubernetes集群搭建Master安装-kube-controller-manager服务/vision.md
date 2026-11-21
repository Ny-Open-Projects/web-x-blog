# 画面线理解：09.Kubernetes集群搭建Master安装-kube-controller-manager服务

- 阶段：01.阶段一 微服务相关技术
- 章节：6.k8s-基础
- 源文件：01.阶段一 微服务相关技术\6.k8s-基础\09.Kubernetes集群搭建Master安装-kube-controller-manager服务_【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:21, 00:33, 00:46, 00:52, 00:53, 01:04, 01:13, 01:15, 01:18, 01:25, 01:31, 01:41, 02:03, 02:10
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-27 10:41:00

1) 这一组画面整体在讲什么（一句话）：
演示如何配置并创建 Kubernetes 的 kube-controller-manager 服务的 systemd 单元文件。

2) 按时间顺序列出每张画面的要点，标注它对应的画面序号：
画面 1: 展示了课程 PPT 页面，标题为“2.2.4 kube-controller-manager服务”，并显示了该服务的 systemd 服务文件路径和内容（Unit 和 Service 部分）。
画面 2: 在 SecureCRT 会话中，执行了命令 `vi /etc/kubernetes/controller-manager`，并成功创建了配置文件。
画面 3: SecureCRT 会话窗口显示了空的编辑器界面，准备进行下一步操作。
画面 4: SecureCRT 会话窗口中显示了刚刚编辑并保存的配置文件内容，同时 PPT 页面显示了“2.2.5 kube-scheduler服务”的标题。
画面 5: PPT 页面显示了“2.2.4 kube-controller-manager服务”的完整内容，包括 Unit 和 Service 部分。
画面 6: PPT 页面显示了“2.2.5 kube-scheduler服务”的完整内容，包括 Unit 部分。
画面 7: SecureCRT 会话窗口中显示了刚刚编辑并保存的配置文件内容。
画面 8: PPT 页面底部显示了黑马程序员的公司信息和标语。
画面 9: SecureCRT 会话窗口中显示了刚刚编辑并保存的配置文件内容。
画面 10: PPT 页面显示了“2.2.5 kube-scheduler服务”的完整内容。
画面 11: 屏幕截图显示了多个窗口的切换，包括课程 PPT、SecureCRT、GitHub、VMware Workstation 等。
画面 12: SecureCRT 会话窗口中显示了配置文件内容，其中 `KUBE_CONTROLLER_MANAGER_ARGS` 参数被修改。
画面 13: SecureCRT 会话窗口中显示了配置文件内容，其中 `KUBE_CONTROLLER_MANAGER_ARGS` 参数被修改。
画面 14: PPT 页面显示了“2.2.5 kube-scheduler服务”的完整内容。

3) 画面里出现的**代码、配置、命令、目录结构、SQL、XML/YAML 配置**请原样抄录（逐字，保留缩进与符号）：
画面 1:
[Unit]
Description=kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.service
Requires=kube-apiserver.service

[Service]
EnvironmentFile=/etc/kubernetes/controller-manager
ExecStart=/usr/bin/kube-controller-manager $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

画面 2:
/etc/kubernetes/controller-manager

画面 4:
[Unit]
Description=kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.service
Requires=kube-apiserver.service

[Service]
EnvironmentFile=/etc/kubernetes/controller-manager
ExecStart=/usr/bin/kube-controller-manager $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

画面 6:
[Unit]
Description=kubernetes Scheduler
Documentation=https://github.com/GoogleCloudPlatform/kubernetes

画面 12:
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://192.168.126.140:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

画面 13:
KUBE_CONTROLLER_MANAGER_ARGS="--master=http://192.168.126.140:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

4) 出现的 PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据也要写清楚：
画面 1: 标题为“2.2.4 kube-controller-manager服务”，下方有“配置systemd服务文件：vi /usr/lib/systemd/system/kube-controller-manager.service”。
画面 4: 标题为“2.2.5 kube-scheduler服务”，下方有“配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.service”。
画面 6: 标题为“2.2.5 kube-scheduler服务”，下方有“配置systemd服务文件：vi /usr/lib/systemd/system/kube-scheduler.service”。
画面 8: 底部有“黑马程序员”的公司信息和标语“改变中国IT教育，我们正在行动”。

5) 不要评价画面美观，不要输出与课程无关的内容。
（无）
