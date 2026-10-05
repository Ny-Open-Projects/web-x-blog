# Go PaaS 平台开发: cephadm 安装基础集群（下）

## 纲要

- 引导（bootstrap）完成后，通过 Dashboard 激活监控并核验集群初始状态
- 将首个节点的 SSH 公钥分发给其他节点，并用 `ceph orch host add` 加入新节点
- 添加 OSD：自动方式（`--all-available-devices`）与手动方式（`orch daemon add osd`）
- 查看集群状态：`ceph -s`、`ceph osd status`、`ceph fsid` 等命令

## 引导后初始化管理端

在上一节用 `cephadm bootstrap` 引导出第一个节点（ceph01）之后，登录 Dashboard（通过 bootstrap 输出的端口），需要：

1. 在 Dashboard 中点击「激活 / Enable」启动监控模块；
2. 同意协议（Agree），点击两个开关并「Update」使其生效；
3. 若进入时已错过激活引导，可用命令重新激活 License：

```bash
ceph mgr module enable dashboard
ceph dashboard ac-user-set-password admin '<你的密码>'
```

激活成功后，Dashboard 会出现监控指标。需要记住此时集群里「有哪些、缺哪些」：

- 主机（Hosts）：目前只有 ceph01 一个节点；
- 设备（Devices）：OSD 尚未安装；
- 存储池（Pools）：尚未创建；
- 文件系统（CephFS）、对象网关（RGW）、iSCSI 网关：均为空，后续安装后才会出现。

如果之前设置的带标记密码丢失，重新安装系统会很麻烦，可通过上面的 `ac-user-set-password` 命令重置。

## 添加其它节点

引导好 ceph01 后，需要把集群扩展到更多节点。

### 分发 SSH 公钥

cephadm 通过 SSH 管理其它节点，需要把 ceph01 生成的公钥拷贝给 ceph02、ceph03：

```bash
# 在 ceph01 上执行
ssh-copy-id -f -i /etc/ceph/ceph.pub root@ceph02
ssh-copy-id -f -i /etc/ceph/ceph.pub root@ceph03
```

### 加入主机

添加节点时要带上主机名、内网 IP：

```bash
ceph orch host add ceph02 172.31.96.74
ceph orch host add ceph03 172.31.96.75
```

添加后，Dashboard 的 Hosts 列表会立即出现 ceph02、ceph03（节点信息同步稍慢属正常）。查看集群主机：

```bash
ceph orch host ls
```

输出会显示三个节点（ceph01/ceph02/ceph03），其中 ceph01 带有 `admin` 标签。

## 添加 OSD

OSD 对应真实的物理硬盘，是数据真正落盘的地方。添加 OSD 对设备有要求：

- 设备必须未被分区、未被格式化（例如阿里云新购的 20G 数据盘，未做任何操作）；
- 不能包含 LVM 元数据；
- 不能被其它主机使用，也不应含操作系统；
- 设备不能被挂载（mount），且容量需大于 5G。

### 自动添加（推荐）

一条命令把集群中所有满足条件的裸盘全部加入：

```bash
ceph orch apply osd --all-available-devices
```

该方式适合云上全新数据盘，由 Ceph 自动识别并初始化。

### 手动添加

如果是在虚拟机等环境、担心自动方式误伤已有盘，可指定单盘手动添加：

```bash
# 在 ceph01 上为其某块裸盘（如 /dev/sdb）添加 OSD
ceph orch daemon add osd ceph01:/dev/sdb
```

本课程采用自动识别方式。执行后可通过以下命令观察 OSD 状态：

```bash
ceph osd status
ceph osd tree
```

例如可看到 ceph01 上有一块 HDD（vdb，约 21.4G），说明硬盘已成功纳入 OSD。

## 核验集群状态

添加 OSD 后，Dashboard 上 ceph02 / ceph03 从空变为有对应 OSD 初始化（编号 0/1/2 分布在各硬盘上）。查看整体集群：

```bash
# 集群健康、FSID、各守护进程数量、PG 数、容量使用
ceph -s

# 查看集群唯一 ID（fsid），后续接入 K8s 时会用到
ceph fsid
```

关键观察项：

- **fsid / cluster ID**：集群唯一标识，必须记录下来；
- **health**：应为 `HEALTH_OK`；
- **MON / MGR / OSD 进程数**：例如 MON 3 个、MGR 1 个（管理端）、OSD 3 块；
- **PG 数**：初始较小（约 250 左右）；
- **容量**：例如 60G 仅用 15M 左右，说明集群刚起步。

此时 Dashboard 的 Pools 里会出现一个监控用存储池，OSD 列表也能看到三块盘关联成功，说明 OSD 添加完成。所有数据落盘最终都会落到 OSD 上。

## 下一步

至此，一个基础 Ceph 集群（含 MON、MGR、OSD）已经引导完成，后续将继续安装 RGW、CephFS、iSCSI 等核心组件。

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/docker-compose/chapter3/prometheus.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：92%。是否需要继续：[是]。代码是否可运行：[是]。
