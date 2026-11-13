// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144831489
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func minFlipsMonoIncr(s string) int { // 定义函数/方法 minFlipsMonoIncr
	one := 0                      // 把 0 写入 one :
	dp := 0                       // 把 0 写入 dp :
	for i := 0; i < len(s); i++ { // 让 下标 i 从 0 开始计数
		c := s[i]     // 把 字符串[下标 i] 写入 c :
		if c == '0' { // 若 字符 等于 '0'
			if one < dp+1 { // 若 one 小于 DP 表 加 1
				dp = one // 把 one 写入 DP 表
			} else { // 否则
				dp = dp + 1 // 把 DP 表 加 1 写入 DP 表
			}
		} else { // 否则
			one++ // one 加一
		}
	}
	return dp // 返回 DP 表
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
