package search

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/olivere/elastic/v7"

	"es-demo/internal/es/client"
)

func mockSearch(t *testing.T, body string) *httptest.Server {
	t.Helper()
	return httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Write([]byte(body))
	}))
}

const sampleSearchResp = `{
  "took":1,"timed_out":false,
  "hits":{"total":{"value":2,"relation":"eq"},
    "hits":[
      {"_index":"product","_id":"p1","_source":{"id":"p1","title":"iPhone 15"}},
      {"_index":"product","_id":"p2","_source":{"id":"p2","title":"华为 Mate 60"}}
    ]}}`

func newSearcher(t *testing.T) (*Searcher, func()) {
	srv := mockSearch(t, sampleSearchResp)
	c, err := client.New(client.WithURLs(srv.URL), client.WithSniff(false), client.WithHealthcheck(false), client.WithHTTPClient(srv.Client()))
	if err != nil {
		t.Fatal(err)
	}
	return New(c), srv.Close
}

func TestSimple(t *testing.T) {
	s, closeFn := newSearcher(t)
	defer closeFn()

	res, err := s.Simple(context.Background(), "product", "",
		[]elastic.Query{elastic.NewMatchQuery("title", "iPhone")}, nil, nil, 0, 10,
		elastic.NewFieldSort("sales").Desc())
	if err != nil {
		t.Fatal(err)
	}
	if res.Total != 2 {
		t.Fatalf("total = %d, want 2", res.Total)
	}
	if len(res.Sources) != 2 {
		t.Fatalf("hits = %d, want 2", len(res.Sources))
	}
	if got := string(res.Sources[0]); got == "" {
		t.Fatal("first hit source empty")
	}
}

func TestNested(t *testing.T) {
	s, closeFn := newSearcher(t)
	defer closeFn()
	inner := elastic.NewBoolQuery().Must(elastic.NewMatchQuery("items.name", "iPhone"))
	if _, err := s.Nested(context.Background(), "order", "items", inner); err != nil {
		t.Fatal(err)
	}
}

func TestScroll(t *testing.T) {
	s, closeFn := newSearcher(t)
	defer closeFn()
	count := 0
	err := s.Scroll(context.Background(), "app_log", "", elastic.NewMatchAllQuery(), 10, func(src []byte) error {
		count++
		return nil
	})
	if err != nil {
		t.Fatal(err)
	}
	if count != 2 {
		t.Fatalf("scroll hits = %d, want 2", count)
	}
}

func TestSearchAfter(t *testing.T) {
	s, closeFn := newSearcher(t)
	defer closeFn()
	sort := elastic.NewFieldSort("sales").Desc()
	if _, err := s.SearchAfter(context.Background(), "product", elastic.NewMatchAllQuery(), sort, nil); err != nil {
		t.Fatal(err)
	}
}
