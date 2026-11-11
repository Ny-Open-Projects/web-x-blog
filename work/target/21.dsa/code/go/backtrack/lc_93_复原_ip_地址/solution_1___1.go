// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135037359
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
	"strings" // 「strings」
)

func restoreIpAddresses(s string) []string { // 定义函数/方法 restoreIpAddresses
	res := []string{}             // 结果集
	segs := []string{}            // 当前段
	var valid func(t string) bool // 段合法性：0-255 且无前导零
	valid = func(t string) bool {
		if len(t) == 0 || len(t) > 3 {
			return false
		}
		if len(t) > 1 && t[0] == '0' {
			return false
		}
		v := 0
		for _, ch := range t {
			v = v*10 + int(ch-'0')
		}
		return v <= 255
	}
	var dfs func(start int) // 回溯：从 start 切下一段
	dfs = func(start int) {
		if len(segs) == 4 { // 已切满 4 段
			if start == len(s) { // 恰好用完字符串才收答案
				res = append(res, strings.Join(segs, "."))
			}
			return
		}
		for l := 1; l <= 3 && start+l <= len(s); l++ { // 每段取 1 到 3 个字符
			t := s[start : start+l]
			if !valid(t) {
				continue
			}
			segs = append(segs, t)
			dfs(start + l)
			segs = segs[:len(segs)-1]
		}
	}
	dfs(0)
	return res
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   string
		want []string
	}{
		{"25525511135", []string{"255.255.111.35", "255.255.11.135"}},
		{"0000", []string{"0.0.0.0"}},
		{"abc", []string{}},
	}
	ok := true
	for _, c := range cases {
		got := restoreIpAddresses(c.in)
		sort.Strings(got)
		want := append([]string{}, c.want...)
		sort.Strings(want)
		if !reflect.DeepEqual(got, want) {
			ok = false
			fmt.Printf("FAIL %q=%v want %v\n", c.in, got, want)
		}
	}
	if !ok {
		os.Exit(1)
	}
	fmt.Println("PASS")
}
