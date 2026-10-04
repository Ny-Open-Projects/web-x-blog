# K8s 课程素材 · 机翻/语音转写术语还原表

> 素材是**课程音频转写 + 机器翻译**的双重噪音产物，和 ES 那套（见 `ES-MT-GLOSSARY.md`）同源。
> **写博客前先对照本表还原术语**，否则会把 `ingress` 写成 `interess` 这种笑话写进正式博客。
> **遇到新的错译追加到对应小节，别攒着。**

## 一、最高频：把专有名词连读/听错了

| 转写/机翻出来的 | 正确术语 | 说明 |
| --- | --- | --- |
| `k八x` / `kbox` / `kboss` / `加BCK` / `k8x` / `kubx` / `k8s集群` | **Kubernetes / K8s** | 语音转写把 K8s 听成各种怪词，是最最高频 |
| `加PC` / `加Pc` / `加pC` / `假PC` / `CRPC` | **gRPC** | 「加」= g（读音），`PC` = RPC |
| `ATTP` / `Attp` / `ALLP` / `AGTPS` / `APTS` | **HTTP / HTTPS** | |
| `UL` / `U L` / `路径UL` | **URL** | |
| `ETChost` / `etc hosts` / `ETC host` | **/etc/hosts** | |
| `interess` / `engresh` / `incress` / `ingressive` / `integress` / `ineress` | **ingress / ingress controller** | 这一族错法至少有 6 种 |
| `controllermanager` / `controlmanager` / `controller manger` | **kube-controller-manager** | |
| `APIServer` / `APIserver` / `apiservre` | **API Server** | |
| `confimap` / `configmep` / `cmaps` | **ConfigMap** | |
| `servicacc` / `service account` 被翻成「服务账号」尚可，但别写成「服务帐号」 | **ServiceAccount（sa）** | |
| `cronjob` / `cron job` 被写得像「_cron 工作_」 | **CronJob** | |
| `livenessprobe` / `readinessprobe` 常被译「存活性探测/准备好探测」 | **存活探针 / 就绪探针** | 中文标准叫法 |
| `sidecar` 被译成「副车/边卡车」 | **sidecar（边车容器）** | 直接写英文+中文注释 |
| `crd` / `customresource` | **CRD / Custom Resource** | |

## 二、数字被听错（老写错端口）

| 转写的 | 正确 |
| --- | --- |
| `八零端口` / `八连端口` / `八零的转发规则` | **80 端口** |
| `四十三端口` / `四十三的转发` | **443 端口** |
| `九零 port` / `nodeport` 写成「节点端口」是对的，但别写成「节点港口」 | **NodePort** |
| `三零秒 / 二零秒` 这种中文数字读秒 | 按上下文还原成 `30s` / `20s`，时间参数统一用阿拉伯数字 |

## 三、需要"意译还原"的黑话

| 机翻给的中文 | 应该还原成 |
| --- | --- |
| 「让一个服务被暴露出去」 | **expose / 暴露服务（Service 的暴露方式）** |
| 「拉起一个 pod」 | **创建 Pod** |
| 「调度到某个节点上」 | **调度（scheduler）到 Node** |
| 「滚动升级 / 平滑更新」 | **滚动更新（rolling update）** |
| 「污点 / 污辱」 | **taint（污点）/ toleration（容忍）** |
| 「亲和性 / 亲密度」 | **affinity（节点亲和性）/ anti-affinity（反亲和）** |
| 「水平伸缩 / 横向扩展」 | **HPA（HorizontalPodAutoscaler）** |
| 「 disruption / 打断预算」 | **PodDisruptionBudget（PDB）** |
| 「守护进程集 / 驻留集」 | **DaemonSet** |
| 「有状态副本集」 | **StatefulSet** |
| 「无状态前端」 | **Deployment** |
| 「入口网关 / 入口控制器」 | **Ingress Controller** |
| 「pod 被驱逐 / 被踢走」 | **Pod 被驱逐（evicted）** |
| 「就绪检查 / 活体检查」 | **readinessProbe / livenessProbe** |

## 四、写法约定（和 ES 那批保持一致的调性）

- 术语**首次出现**时给「中文（English）」双写，之后用英文；
- 组件名一律用官方大小写：`kubelet`、`kubeadm`、`kubectl`、`kube-proxy`、`CNI`、`CSI`；
- 命令块用 `kubectl`、资源清单用 `yaml`，**别用 go 代码块硬凑**（K8s 课以 yaml / 命令为主，
  只有讲 Go 客户端（`client-go`）时才用 `go` 块）；
- 原文里大量口语（「咱们」「大家」「这一节咱们」）**全部删掉**，不留讲课腔。

## 五、每批改稿后要做的

把这次新踩到的错译（表里没有的）**追加进对应小节**，并在文件头注明日期。

## 六、5.k8s5-prod 批新发现的错译（2026-10-02 补）

| 机翻/听错写法 | 正确写法 | 备注 |
| --- | --- | --- |
| `hostaliases` | `hostAliases` | **字段名必须驼峰**；其下的 key 是 `hostnames`（**带 s**，漏 s 会报 field 不存在） |
| downloadAPI / download api | Downward API | 把 Pod 信息注入容器的机制 |
| 后置 / 视文件 / ETChost | `/etc/hosts` | 语音转写把路径整个听没了 |
| KIFA 就 coalition 之类无意义串 | 按上下文还原或整句删 | 转写彻底失败时不要硬猜，删掉比写错强 |
| limits / requests 讲成"限制/请求" | 保持英文 `requests` / `limits` | 首次出现给中文双写 |
| LimitRange / ResourceQuota 讲成"限制范围" | 保持英文原名 | 同下 |

## 七、3.k8s3-top 第 6~7 章（云原生存储 / 中间件 / 监控篇，2026-10-03 夜间批补）

这一章讲 Rook + Ceph + Helm + Prometheus，专有名词密集且**大多是语音转写首见**，
错译率明显高于前面几章，写文前务必对照。

| 机翻/听错写法 | 正确写法 | 备注 |
| --- | --- | --- |
| `roock` / `入口` / `ark` | **Rook** | 云原生存储编排器；`i进程` 指的是 Rook 的 **agent** 组件 |
| `safe` / `shift` / `税ve` | **Ceph** | 分布式存储；`OSD`/`mon`/`MDS`/`RGW`/`MGR` **保持英文原名不译** |
| `xboard` / `xbod` / `x波` / `斯维斯` | **exporter** / **Service** | 看上下文，讲采集组件是 exporter，讲服务发现是 Service |
| `servicemoneor` / `servicemonit` | **ServiceMonitor** | Prometheus Operator 的 CRD，注意驼峰 |
| `andpoint` / `anderpoint` | **Endpoint** | 不是「端点 checkpoint」 |
| `magic` / `mesicx` / `mafic` | **`/metrics`** | Prometheus 抓取路径，`prometheus.io/path` annotation 上用 |
| `class入` / `classroom` / `class柱` | **ClusterRole** | 和 `Role` 的区别是集群级 vs namespace 级 |
| `如班顶` / `rulebanding` | **RoleBinding** | 配套 `ClusterRoleBinding` 同理 |
| `preset` / `putprayset` / `厚的白色` | **PodPreset** | 准入控制器，1.20+ 已移除，写文要点明版本限制 |
| `limitrunge` / `living的round` | **LimitRange** | namespace 级默认值/上下限注入 |
| `resultcode` | **ResourceQuota** | 和资源限制搞混了，注意是「配额」不是「限制」 |
| `bestafoot` / `besteffort` | **BestEffort** | QoS 三档之一 |
| `birstable` / `firststep` | **Burstable** | QoS 三档之一 |
| `gaeret` / `gurantee` | **Guaranteed** | QoS 三档之一（拼写别漏 `d`） |
| `fluent` / `floent` | **Fluentd** | EFK 里的 F |
| `k断码` / `k八的` | **Kibana** | EFK 里的 K |
| `八六b` / `发热b` / `farbit` | **Filebeat** | 有时是指 Filebeat，别和 Fluentd 混 |
| `notepode` / `noteput` | **NodePort** | Service 类型之一 |

## 八、3.k8s3-top 第 8 章（Ingress-Nginx 章，2026-10-04 夜间批补）

这一章讲 ingress-nginx 的 auth / TLS / 灰度金丝雀 / 自定义 snippet / 请求头，
并穿插 Prometheus / Grafana / Dashboard 监控栈，**专有名词首见且听错率极高**，
写文前务必对照。

| 机翻/听错写法 | 正确写法 | 备注 |
| --- | --- | --- |
| 普罗明斯 / 普米修斯 / 罗米修斯 / 米修斯 / 米公司 | **Prometheus** | 监控系统，固定译名「普罗米修斯」 |
| QSF发现 / 求发现 | **服务发现（service discovery）** | 监控/ingress 上下文里的「服务发现」 |
| "put"（监控上下文，如"普罗米修斯的put""ingress-nginx里面的put"） | **Pod** | 语音把 Pod 听成 put |
| 负总的要压麦尔文件 / 肉啊 | **yaml 清单（yaml manifest）** | manifest 听成「压麦尔文件」 |
| 西格玛（relabel 里） | **scheme** | relabel_configs 里的 scheme 字段 |
| 破的（capture group port） | **port** | 捕获组里的 port |
| 元子一 / 元子二 / 元组 | **捕获组（capture group）** | 正则捕获组 |
| jobname | **job_name** | Prometheus job 配置项，驼峰 |
| jodrop / rop | **drop** | relabel action：drop |
| 消费者费者sercot | **ServiceAccount**（如 prometheus-k8s） | 听错：ServiceAccount |
| classroombunding | **ClusterRoleBinding** | classroom 已在第七节=ClusterRole |
| grass / graphservice / grapanor / NDX / 尼克斯 | **Grafana** | 监控可视化 |
| 电视爆 / 待社报道 / 单车报 / 呆时报 | **Dashboard**（Kubernetes Dashboard） | 看上下文 |
| 盖世board / 盖是board | **kubernetes-dashboard** | Dashboard 资源名 |
| APPS / HPP / HPPAPPP | **HTTPS / HTTP** | Dashboard 上下文的协议 |
| SSLpass怕都 | **ssl-passthrough** | ingress-nginx annotation |
| backbackking的portocol | **backend-protocol** | ingress-nginx annotation |
| 铁ios点 / PLS一二四二 / tios点 | **TLS** | 证书/加密 |
| autogenerate | **auto-generate-certificates** | Dashboard 自动生成证书参数 |
| 海尔图 / 海图 / 还图 / 拍摄头 | **header**（HTTP 请求头） | 如 X-Forwarded-* header |
| 请镜头 / 请镜图 / 镜 | **canary**（金丝雀） | 灰度发布 |
| 帕龙 / palon | **pattern**（正则 pattern） | 匹配模式 |
| 枯边 / cool边 / cookie库 | **cookie** | 会话/匹配 |
| server-snapped / serversnaked / serversnaep | **server-snippet**（configuration-snippet） | ingress-nginx 自定义片段 |
| snap | **snippet** | 同上 |
| OS（金丝雀误听成 always） | **always**（金丝雀值 always/never） | canary 的 enabled 取值 |

## 九、3.k8s3-top 第 9 章（Jenkins / SpringCloud / CI-CD 章，2026-10-04 夜间批补）

这一章讲 Jenkins 安装/流水线/多集群发版、GitLab、BlueOcean、SpringCloud 上 k8s，
专有名词密集且**大多是语音转写首见**，写文前务必对照。

### Jenkins 体系
| 机翻/听错写法 | 正确写法 |
| --- | --- |
| 接听子 / 接近子 / 接顶 / 接信层 / 接面 / 接定 / 接并词 / 接克 | **Jenkins** |
| jack / jacens / jacks / jackks / jackson / jacking / jackstyle / jackingfive / jackfile / jaconfile / jaksonfile / jack's five | **Jenkinsfile** |
| 六十线 / 六水线 / 牛排版 | **流水线（pipeline）** |
| i技能 | **agent** |
| sasch / stasch / state / 时代者 | **stage** |
| shpost | **post** |
| 教务 / 效母 / 教补 / 交补 / 校务 | **job** |
| 界片发ile / 结根发 / 基根发 | **Jenkinsfile** |

### GitLab 体系
| 机翻/听错写法 | 正确写法 |
| --- | --- |
| gatelife / gatelab / gatelive / gadlep / gaylove / gailab / gitlive / gatlep / 配套装 | **GitLab** |
| gateround / gaterunner | **GitLab Runner** |
| 凹凸 / 凹凸develop / autodemo | **Auto DevOps** |
| 钉钉（"在…上选择版本"语境） | **界面 / UI** |

### BlueOcean 体系
| 机翻/听错写法 | 正确写法 |
| --- | --- |
| blotion / blowersion / blowoption / openpollutional / prolution / blution / glowoption / bloopsion / pology | **BlueOcean** |
| flutioneditor / blowoptioneditor / blutioneditor | **BlueOcean Editor** |

### kubectl / K8s 资源
| 机翻/听错写法 | 正确写法 |
| --- | --- |
| QQ卡 / 夸卡 / QQCCL / QBCTL / Q客 / 客（单指命令） | **kubectl** |
| stripeforset / levelforset / staplforset | **StatefulSet** |
| demot | **DaemonSet** |
| level | **label** |
| confit | **config** |
| integress / ingrass | **Ingress** |
| container / conttain容 | **container** |

### Docker / 镜像仓库
| 机翻/听错写法 | 正确写法 |
| --- | --- |
| 刀壳 / dodoker / dollar / dogfile | **docker** |
| 刀口 / 定点 / 定向 | **docker image** |
| help / helb / hubb / 汉堡 / 哈堡 / 哈服 / 汉本 | **Harbor** |
| hardress / hubaddress / huveraddress / hibaddress / harperdress | **Harbor 地址（registry address）** |
| reporstry / reportertion / 定向仓库 | **镜像仓库（repository）** |
| XSK | **AccessKey（AK/SK）** |
| CItools / CItooth | **CI tools** |
| cr | **容器镜像服务（ACR）** |

### 其它
| 机翻/听错写法 | 正确写法 |
| --- | --- |
| marvin / marvin三杠 | **Maven** |
| noteGS / NPM / 八类 | **NodeJS** |
| g联 / 计联 / 基点 / 鉴定费向 / 机联面量 / 接联 | **级联（cascading / Active Choices）** |
| sninome / nemo四ze / namoSpace / sigma | **namespace** |
| brunch / brush / 歪角 / 分病 | **分支（branch）** |
| gq | **jq** |
| menu参数 | **手动 / manual** |

> 存疑待人工复核：「临时的集训模式」一词含义不明，疑似 GitLab 高可用 / 临时 Runner，建议人工确认原术语后再定稿。
