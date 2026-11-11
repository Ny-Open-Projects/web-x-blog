// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130423018
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// countBinarySubstrings3 忠实翻译 python ref solution_5___5.py（cur/prev 在线变体，行为以 pyref 为准）
func countBinarySubstrings3(s string) int { // 定义函数/方法 countBinarySubstrings3
	prev, cur, ans := 0, 1, 0     // 上一组长度、当前组长度、答案
	for i := 1; i < len(s); i++ { // 从下标 1 扫描到末尾
		if s[i] == s[i-1] { // 同组
			cur++
		} else { // 换组
			ans += min(prev, cur) // 结算上一对相邻组
			prev, cur = cur, 1
		}
	}
	return ans + min(prev, cur) // 结算最后一对
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func main() { // 程序入口：跑内嵌自测用例
	cases := map[string]int{"00110011": 6, "10101": 4, "0": 0, "111000": 3}
	ok := true
	for in, want := range cases {
		if got := countBinarySubstrings3(in); got != want {
			ok = false
			fmt.Printf("FAIL %s=%d want %d\n", in, got, want)
		}
	}
	if !ok {
		os.Exit(1)
	}
	fmt.Println("PASS")
}
