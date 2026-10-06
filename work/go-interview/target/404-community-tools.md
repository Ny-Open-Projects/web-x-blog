# 44 社区包管理工具：godep / glide / govendor

> 分类：Go 工程化 | 难度：L3 | 题型：演进题 | 频率：中 | 关键词：**godep**/**glide**/**govendor**/**vendor 目录**/**GO15VENDOREXPERIMENT**
> 原文锚点：第 76~103 段「godep / glide / govendor 三个社区工具」

## 一句话总述
官方统一方案出现前，社区先后涌现 godep(2013)、glide(2014)、govendor(2015) 三种主流工具：godep 用 workspace 快照、glide 用 yaml/lock 记录版本、govendor 基于 vendor 目录（GO15VENDOREXPERIMENT 开启）把依赖拷进工程，各有取舍。

## 面试官视角
- 考察意图：知不知道 Go 包管理「百家争鸣」的历史，以及各工具的机制与优劣。
- 分档：P5 知有这三种工具；P6 知各自机制（快照/yaml/vendor）；P7 知 govendor 的 vendor 实验与 CICD 提速、依赖不能复用的代价。
- 红旗答案：把三者混为一谈；或不知道 vendor 目录的来历。
- 惊艳点：点出「govendor 借 Docker 把 workspace 打进镜像即可带齐依赖，故早期 K8s/Docker 用过」。

## 主问答
**Q（面试官原话）：** GOPATH 之后有哪些社区包管理工具？
**A：**
1. **godep（2013）**：第一个社区工具，扫描并记录版本控制信息，配合 go 命令加壳；把所有源码存到 `Godeps/_workspace` 作为唯一 GOPATH，提供 godep save/restore；相当于对 GOPATH 源码做快照。Docker 火起后把 workspace 打进镜像即带齐依赖，早期 Docker/K8s 用过。
2. **glide（2014）**：号称参照各语言最佳实践；`glide.yaml` 记录依赖、`glide.lock` 追踪每个包的具体修改；指定版本/范围像 npm/pip。
3. **govendor（2015）**：基于 vendor 目录（go1.5 引入，GO15VENDOREXPERIMENT 环境变量开启；1.6 默认开；1.7 作为功能取消该变量）；把源码拷贝到 vendor 目录并维护 vendor.json 指定版本。
4. **govendor 搜索顺序**：编译时先从 vendor 找 → GOPATH → GOROOT。
5. **govendor 取舍**：把第三方依赖完全整合进工程，加速构建（尤其微服务 CICD）；缺点是依赖不能复用、冗余提升、依赖冲突解决不力。官方现推 Go Modules，但旧项目仍用 govendor。

## 追问链
| 层 | 追问 | 在测什么 | 怎么接 | 答不出停在哪档 |
| --- | --- | --- | --- | --- |
| L1 | 有哪三个社区工具？ | 基础 | godep/glide/govendor | P5 |
| L2 | glide 用什么记录？ | 机制 | yaml + lock | P6 |
| L3 | vendor 目录怎么来的？ | 演进 | go1.5 GO15VENDOREXPERIMENT | P6 |
| L4 | govendor 优缺点？ | 取舍 | 构建快但冗余、冲突难解 | P7 |
| L5 | 为什么仍要懂旧工具？ | 进阶 | 旧项目维护 | P7+ |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
| --- | --- | --- |
| Go 1.5~1.6 | vendor 实验→默认；1.7 取消 GO15VENDOREXPERIMENT | 新项目用 Go Modules；vendor 机制被 Modules 的 vendor/ 兼容保留 |

## 关键代码
```bash
# govendor 典型用法
go get github.com/kardianos/govendor
govendor init                 # 初始化 vendor
govendor add +external       # 把依赖拷进 vendor
govendor remove -unused      # 移除未用依赖
```

## 总结与追问预判
社区三工具是「从快照→声明式→vendor 目录」的演进，最终被 Go Modules 一统。下一步常问 Go Modules 本身与 go.mod/go.sum。

## ⚠️ 原文纠错
1. 事实核校： [经验] godep workspace 快照、glide yaml/lock、govendor vendor 目录+GO15VENDOREXPERIMENT(1.5 引入/1.6 默认/1.7 取消)、govendor 搜索顺序与取舍——均正确。
2. 崩坏词归一：源码将 Go 音译为勾那/购、Golang 音译为 golwn/godown、godep 音译为 go第一批、glide 音译为 glade、govendor 音译为 gorender/点derder、GO15VENDOREXPERIMENT 音译为 go十五renderexperiment、vendor 音译为 render、Docker 音译为 docork、K8s 音译为括OS；源码将 Go 语言 音译为崩坏词，本卡统一为 Go 语言。
