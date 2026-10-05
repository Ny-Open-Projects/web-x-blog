package ops

import "testing"

func TestWatermarkValidate(t *testing.T) {
	if err := Defaults().Validate(); err != nil {
		t.Fatalf("defaults should be valid: %v", err)
	}
	// 混用百分比与具体空间 -> 非法
	mixed := WatermarkSet{
		Low:   Watermark{IsPercent: true, Percent: 85},
		High:  Watermark{IsPercent: false, FreeGB: 100},
		Flood: Watermark{IsPercent: true, Percent: 95},
	}
	if err := mixed.Validate(); err == nil {
		t.Fatal("mixed percent/absolute should be invalid")
	}
}

func TestWatermarkEvaluate(t *testing.T) {
	wm := Defaults()
	cases := []struct {
		used   float64
		expect string
	}{
		{500, "正常"},
		{870, "低水位线"},
		{920, "高水位线"},
		{970, "洪水线"},
	}
	for _, c := range cases {
		if got := wm.Evaluate(1000, c.used).Name; got != c.expect {
			t.Errorf("used=%v -> %s, want %s", c.used, got, c.expect)
		}
	}
}

func TestDiagnose(t *testing.T) {
	ex := Explain{Index: "order", Shard: 0, Primary: true, Reason: "node_left the node recently left"}
	ops := Diagnose(ex)
	if len(ops) == 0 {
		t.Fatal("expected a playbook match for node_left")
	}
	// 未命中剧本
	unknown := Diagnose(Explain{Reason: "totally unknown"})
	if len(unknown) != 1 || unknown[0].Action == "" {
		t.Fatal("unknown reason should fall back to manual")
	}
}

func TestValidateEnable(t *testing.T) {
	if _, err := ValidateEnable("none"); err == nil {
		t.Fatal("none must be rejected in rolling restart")
	}
	for _, v := range []string{"all", "null", "primaries", "new_primaries"} {
		if _, err := ValidateEnable(v); err != nil {
			t.Errorf("validateEnable(%s) unexpected err: %v", v, err)
		}
	}
}

func TestRestartPlan(t *testing.T) {
	steps := RestartPlan("es-01")
	if len(steps) != 6 {
		t.Fatalf("expect 6 steps, got %d", len(steps))
	}
	if steps[4].Command == "" {
		t.Fatal("step 5 (restore allocation) missing")
	}
}

func TestThreadPoolHealth(t *testing.T) {
	p := ThreadPool{Name: "write", Size: 16, Rejected: 3}
	if p.Health().Level != "危险" {
		t.Fatalf("rejected>0 should be 危险, got %s", p.Health().Level)
	}
	ok := ThreadPool{Name: "search", Size: 32, Active: 1, Queue: 0}
	if ok.Health().Level != "正常" {
		t.Fatalf("idle pool should be 正常, got %s", ok.Health().Level)
	}
}
