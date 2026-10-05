package write

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/es/client"
)

func mockWrite(t *testing.T) *httptest.Server {
	t.Helper()
	return httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		switch {
		case r.URL.Path == "/_bulk":
			w.Write([]byte(`{"errors":false,"items":[]}`))
		default:
			w.Write([]byte(`{"_index":"product","_id":"p1","result":"created","_version":1,"_shards":{"total":2,"successful":1,"failed":0}}`))
		}
	}))
}

func newWriter(t *testing.T) (*Writer, func()) {
	srv := mockWrite(t)
	c, err := client.New(client.WithURLs(srv.URL), client.WithSniff(false), client.WithHealthcheck(false), client.WithHTTPClient(srv.Client()))
	if err != nil {
		t.Fatal(err)
	}
	w, err := NewWriter(context.Background(), c)
	if err != nil {
		t.Fatal(err)
	}
	return w, func() { _ = w.Close(); srv.Close() }
}

func TestIndex(t *testing.T) {
	w, closeFn := newWriter(t)
	defer closeFn()
	doc := map[string]interface{}{"id": "p1", "title": "iPhone 15"}
	if err := w.Index(context.Background(), "product", "p1", "", doc, RefreshWaitFor); err != nil {
		t.Fatal(err)
	}
}

func TestIndexWithVersion(t *testing.T) {
	w, closeFn := newWriter(t)
	defer closeFn()
	doc := map[string]interface{}{"id": "p1", "title": "iPhone 15 v2"}
	if err := w.IndexWithVersion(context.Background(), "product", "p1", doc, 2); err != nil {
		t.Fatal(err)
	}
}

func TestBulkNow(t *testing.T) {
	w, closeFn := newWriter(t)
	defer closeFn()
	docs := []elastic.BulkableRequest{
		elastic.NewBulkIndexRequest().Index("product").Id("p1").Doc(map[string]interface{}{"id": "p1"}),
		elastic.NewBulkIndexRequest().Index("product").Id("p2").Doc(map[string]interface{}{"id": "p2"}),
	}
	ok, err := w.BulkNow(context.Background(), "product", docs)
	if err != nil {
		t.Fatal(err)
	}
	if !ok {
		t.Fatal("bulk reported errors=true")
	}
}
