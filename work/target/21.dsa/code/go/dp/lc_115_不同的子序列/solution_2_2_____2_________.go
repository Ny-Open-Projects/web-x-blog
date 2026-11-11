// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144848405
package main // 引入依赖

import (
	"fmt"
	"os"
	"strconv"
) // 引入依赖

func numDistinct(s, t string) int { // 定义函数/方法 numDistinct
	sLen, tLen := len(s), len(t)  // 把 长度(字符串), 长度(另一字符串) 写入 sLen, tLen :
	memo := map[string]int{}      // 把 映射表[string]int{} 写入 memo :
	var helper func(int, int) int // var helper func(int, int) int
	helper = func(i, j int) int { // 把 func(下标 i, 下标 j int) int { 写入 helper
		if j < 0 { // 若 下标 j 小于 0
			return 1 // 返回 1
		}
		if i < 0 { // 若 下标 i 小于 0
			return 0 // 返回 0
		}
		key := strconv.Itoa(i) + "," + strconv.Itoa(j) // 把 strconv.Itoa(下标 i) 加 「,」 加 strconv.Itoa(下标 j) 写入 key :
		if v, ok := memo[key]; ok {                    // 若 值, ok : 赋值为 记忆化表[key]; ok
			return v // 返回 值
		}
		var r int         // var 右指针 int
		if s[i] == t[j] { // 若 字符串[下标 i] 等于 另一字符串[下标 j]
			r = helper(i-1, j) + helper(i-1, j-1) // 把 helper(下标 i 减 1, 下标 j) 加 helper(下标 i 减 1, 下标 j 减 1) 写入 右指针
		} else { // 否则
			r = helper(i-1, j) // 把 helper(下标 i 减 1, 下标 j) 写入 右指针
		}
		memo[key] = r // 把 右指针 写入 memo[key]
		return r      // 返回 右指针
	}
	return helper(sLen-1, tLen-1) // 定义函数/方法 helper
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		s, t string // 字符串, 另一字符串 string
		want int    // want int
	}{ // }{
		{"rabbbit", "rabbit", 3},
		{"babgbag", "bag", 5},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if g := numDistinct(c.s, c.t); g != c.want { // 若 g : 赋值为 numDistinct(字符.字符串, 字符.另一字符串); g 不等于 字符.want
			ok = false                                                 // 把 false 写入 ok
			fmt.Printf("FAIL %q,%q=%v want %v\n", c.s, c.t, g, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
