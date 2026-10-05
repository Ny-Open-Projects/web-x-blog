package client

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"
)

// mockES 返回一个 httptest 服务器，对常见端点返回最小合法 JSON，
// 用于在不依赖真实集群的情况下验证客户端请求构造与响应解析。
func mockES(t *testing.T) *httptest.Server {
	t.Helper()
	return httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		switch {
		case r.URL.Path == "/":
			w.Write([]byte(`{"version":{"number":"7.17.18"},"cluster_name":"test"}`))
		case r.URL.Path == "/_cluster/health":
			w.Write([]byte(`{"status":"green"}`))
		default:
			w.Write([]byte(`{}`))
		}
	}))
}

func TestPing(t *testing.T) {
	srv := mockES(t)
	defer srv.Close()

	c, err := New(WithURLs(srv.URL), WithSniff(false), WithHealthcheck(false), WithHTTPClient(srv.Client()))
	if err != nil {
		t.Fatal(err)
	}
	ver, err := c.Ping(context.Background())
	if err != nil {
		t.Fatal(err)
	}
	if ver != "7.17.18" {
		t.Fatalf("version = %q, want 7.17.18", ver)
	}
}

func TestHealth(t *testing.T) {
	srv := mockES(t)
	defer srv.Close()
	c, _ := New(WithURLs(srv.URL), WithSniff(false), WithHealthcheck(false), WithHTTPClient(srv.Client()))
	st, err := c.Health(context.Background())
	if err != nil {
		t.Fatal(err)
	}
	if st != "green" {
		t.Fatalf("health = %q, want green", st)
	}
}
