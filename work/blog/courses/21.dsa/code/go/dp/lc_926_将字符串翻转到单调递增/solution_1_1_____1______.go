// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minFlipsMonoIncr(s string) int { // 定义函数/方法 minFlipsMonoIncr
	n := len(s)              // 把 长度(字符串) 写入 n :
	dp0 := 0                 // 把 0 写入 dp0 :
	dp1 := 0                 // 把 0 写入 dp1 :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		c := s[i]      // 把 字符串[下标 i] 写入 c :
		dp0New := dp0  // 把 dp0 写入 dp0New :
		dp1New := dp0  // 把 dp0 写入 dp1New :
		if dp1 < dp0 { // 若 dp1 小于 dp0
			dp1New = dp1 // 把 dp1 写入 dp1New
		}
		if c == '1' { // 若 字符 等于 '1'
			dp0New++ // dp0New 加一
		} else { // 否则
			dp1New++ // dp1New 加一
		}
		dp0 = dp0New // 把 dp0New 写入 dp0
		dp1 = dp1New // 把 dp1New 写入 dp1
	}
	if dp0 < dp1 { // 若 dp0 小于 dp1
		return dp0 // 返回 dp0
	}
	return dp1 // 返回 dp1
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   string // in string
		want int    // want int
	}{ // }{
		{"00110", 1},
		{"010110", 2},
		{"", 0},
		{"100", 1},
		{"1010", 2},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := minFlipsMonoIncr(c.in); got != c.want { // 若 got : 赋值为 minFlipsMonoIncr(字符.in); got 不等于 字符.want
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL minFlipsMonoIncr(%q)=%d want %d\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
