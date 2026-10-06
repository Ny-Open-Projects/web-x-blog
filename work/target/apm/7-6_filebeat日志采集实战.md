# Go APM 监控系统实战: Filebeat 日志采集实战

## 纲要

- docker-compose 新增 Filebeat 容器，把宿主机 `logs` 目录挂载到容器内 `/logs`
- 配置分离：主配置 `filebeat.yml` + `collect` 目录下放各采集任务配置（inputs）
- inputs 指定采集路径：收集 `/logs/*.log` 结尾的文件
- 先验证：output 打到控制台（debug 模式），确认 JSON 日志进 `message` 字段
- 资源限制：Filebeat 与应用同机，必须限制最大内存与 CPU 核数（本例限 1 核），避免影响业务
- 切换输出：output 只能有一个，验证通过后把 output 改为发往 Logstash 的 5044 端口

## 素材索引

```mermaid
flowchart LR
    HD[宿主机 /logs/*.log] -->|volume| FB[Filebeat 容器 /logs]
    FB -->|inputs 采集| CFG[filebeat.yml + collect/*.yml]
    CFG -->|output console(调试)| OUT[控制台 JSON]
    CFG -->|output logstash| LS[Logstash :5044]
```

## 在 docker-compose 里加 Filebeat

上一节应用已把日志写到宿主机 `logs` 目录。这节让 Filebeat 把日志收上来。在 `docker-compose.yml` 里新增一个 Filebeat 服务：

- 把宿主机的 `logs` 目录映射到容器内的 `/logs`；
- 同时映射两个配置目录：一个放 Filebeat 自身的 `filebeat.yml`，一个放采集任务配置（`collect` 目录）；
- 容器启动命令用 `filebeat -e -d "*"` 以 debug 形式启动，把自身输出全部打到控制台，方便我们观察它到底收没收到日志。

## 采集配置

Filebeat 的采集逻辑无非「输入 + 输出」。由于我们还没讲 Logstash，先把 output 指向控制台（便于验证）。输入用 `filebeat.inputs` 指定采集目录：

```yaml
# collect/app-log.yml —— 根据讲稿逻辑补充
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /logs/*.log          # 收集 /logs 下所有 .log 文件
```

`filebeat.yml` 里通过 `filebeat.config.inputs` 指定这些采集配置所在的目录（`collect`），启动时会加载该目录下所有配置。这里只放了一个，实际可按业务放多个。

启动 Filebeat 后，向应用发几次请求，再进 Filebeat 容器看控制台：能看到应用日志以 **JSON 格式**出现，且带采集时间。注意两点：

- 日志原文落在 `message` 字段里，是一个 JSON 字符串；
- 这里的 `host` 是 **Filebeat 容器自身**的主机，并非应用所在主机（应用主机要靠我们在 7-5 注入的 `host` 字段区分）。

## 资源限制（生产必做）

Filebeat 通常和业务应用部署在同一台机器。为不让采集影响业务，必须限制它的资源占用：

- 限制最大内存；
- 限制使用的 CPU 核数（本例最多 1 核）。

这样能最大限度保证日志收集不影响应用运行。其他如单条日志最大长度等参数可查阅官网。

## 切换到发往 Logstash

验证控制台能收到日志后，把 output 切到 Logstash。注意 **Filebeat 的 output 只能定义一个**，所以把原来的控制台 output 注释掉，改为：

```yaml
# filebeat.yml —— 根据讲稿逻辑补充
output.logstash:
  hosts: ["logstash:5044"]   # Logstash 暴露的端口
```

改完需重启 Filebeat 容器使配置生效。

## 应用侧：产出可被采集的结构化日志

Filebeat 采集的是文件，下面这段 Go 持续写出 7-5 那样的 JSON 日志（根据讲稿逻辑补充，自包含可运行，需 `go get github.com/sirupsen/logrus github.com/lestrrat-go/file-rotatelogs`）：

```go
// appwriter/main.go —— 根据讲稿逻辑补充
package main

import (
	"time"

	"github.com/lestrrat-go/file-rotatelogs"
	"github.com/sirupsen/logrus"
)

func main() {
	rl, _ := rotatelogs.New("/logs/app-%Y%m%d.log",
		rotatelogs.WithRotationTime(24*time.Hour))
	log := logrus.New()
	log.SetOutput(rl)
	log.SetFormatter(&logrus.JSONFormatter{})
	// 模拟持续产生日志，供 Filebeat 采集
	for i := 0; i < 3; i++ {
		log.WithField("uid", i).WithField("app", "order").
			WithField("host", "node-1").Info("handle request")
		time.Sleep(time.Second)
	}
}
```

## 技术点总结

- Filebeat 容器经 volume 读宿主机 `logs`，配置分主配置与采集任务两类
- 先用 output console 验证采集是否生效，再切 output.logstash
- `message` 字段装原始 JSON 文本；Filebeat 自身 host ≠ 应用 host
- 同机部署必须限内存、限 CPU（1 核）保业务
- Filebeat output 仅能配置一个

相关度：90%。是否需要继续：[是]。代码是否可运行：[是]。
