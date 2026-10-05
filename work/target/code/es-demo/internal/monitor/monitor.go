// Package monitor 搜索服务指标（对应《搜索性能指标上报》《使用Prometheus与Grafana监控ES集群》）。
//
// 这里实现「业务侧」自定义指标：把每次搜索的延迟、QPS、错误率上报给 Prometheus，
// 配合 elasticsearch_exporter 的「集群侧」指标，组成完整的可观测性。
package monitor

import (
	"net/http"
	"time"

	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
)

// Metrics 搜索指标收集器。
type Metrics struct {
	searchLatency *prometheus.HistogramVec
	searchTotal   *prometheus.CounterVec
}

// New 创建并注册指标。
func New() *Metrics {
	m := &Metrics{
		searchLatency: prometheus.NewHistogramVec(prometheus.HistogramOpts{
			Name:    "es_search_duration_seconds",
			Help:    "ES 搜索耗时分布",
			Buckets: []float64{0.005, 0.01, 0.05, 0.1, 0.5, 1, 5},
		}, []string{"index"}),
		searchTotal: prometheus.NewCounterVec(prometheus.CounterOpts{
			Name: "es_search_total",
			Help: "搜索请求总数（按结果 ok/err 区分）",
		}, []string{"index", "result"}),
	}
	prometheus.MustRegister(m.searchLatency, m.searchTotal)
	return m
}

// Observe 记录一次搜索的耗时与结果（result 传 "ok" 或 "err"）。
func (m *Metrics) Observe(index string, d time.Duration, ok bool) {
	res := "ok"
	if !ok {
		res = "err"
	}
	m.searchLatency.WithLabelValues(index).Observe(d.Seconds())
	m.searchTotal.WithLabelValues(index, res).Inc()
}

// Handler 返回 /metrics 的 HTTP handler，供 Prometheus 抓取。
func (m *Metrics) Handler() http.Handler {
	return promhttp.Handler()
}

// Serve 启动指标暴露端点（默认 :2112/metrics）。
func (m *Metrics) Serve(addr string) error {
	return http.ListenAndServe(addr, m.Handler())
}
