# 715 Viper 动态监听 · 深挖

## 思路与架构
Viper 内部由「配置源抽象 + 键路径解析 + 变更通知」三层构成。读取阶段用 mapstructure 把扁平键（如 app.env、mysql.dbname）按结构体标签映射到嵌套字段；监听阶段 WatchConfig 依托 fsnotify 监控文件，变更时触发 OnConfigChange 回调，回调内重新 Unmarshal 得到新快照。生产架构上，全局配置应作为**不可变快照**通过原子指针/读写锁对外暴露，避免读改写竞态。远程配置（etcd/Nacos）则需额外引入 poll 或 watch 长连接，Viper 原生只覆盖本地文件。

## 方案取舍
- **全局单例 vs viper.New()**：单例方便但多配置源易串扰，独立实例隔离更清晰，推荐 New()。
- **热更新 vs 发版重启**：热更新快但风险高，连接类、开关类配置应走发版；仅非关键、可校验的配置才热更。
- **mapstructure vs yaml 标签**：mapstructure 是 Viper 官方首选，兼容带分隔符的键；yaml 标签在下划线键上会失效。
- **panic vs 返回 error**：读配置失败在启动期 panic 可接受，运行期热更失败应跳过覆盖并告警。

## 答题技巧
面试答动态配置题，先给四步加载（New→SetConfigFile→ReadInConfig→Unmarshal），再给热更两 API（WatchConfig+OnConfigChange）并强调「回调里重 Unmarshal + 并发安全替换」。必点两个坑：下划线字段与冒号后空格导致静默零值；以及稳定性红线——连接配置不热更、走发版。追问到架构时，用「不可变快照 + 原子指针」收尾，体现工程深度。

## 细节与核心 API

```go
import "github.com/spf13/viper"
v := viper.New()
v.SetConfigFile("config.yaml")
v.ReadInConfig()
// 动态监听文件变化（热更新）
v.WatchConfig()
v.OnConfigChange(func(e fsnotify.Event) {
    log.Println("config changed:", e.Name)
    // 重新加载到内存中的配置对象（注意并发读需加锁或原子替换指针）
})
port := v.GetInt("server.port")
dsn := v.GetString("db.dsn")
// 多源优先级：Set > flag > env > config > key/value > default
// 注意：热更新要处理运行中配置被并发读取的可见性与一致性
_ = port; _ = dsn
```
