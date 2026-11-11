// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func getResult(n int, h []int) int { // 定义函数/方法 getResult
	res := 0                  // 把 0 写入 res :
	for a := 1; a <= n; a++ { // 让 数组 从 1 开始计数
		curH := h[a]                   // 把 h[数组] 写入 curH :
		lo := a - 1                    // 把 数组 减 1 写入 lo :
		for lo >= 1 && h[lo] >= curH { // 把 1 且 h[左边界] 不低于 curH { 写入 for lo >
			lo-- // 左边界 减一
		}
		hi := a + 1                    // 把 数组 加 1 写入 hi :
		for hi <= n && h[hi] >= curH { // 把 元素个数 且 h[右边界] 不低于 curH { 写入 for hi <
			hi++ // 右边界 加一
		}
		area := (hi - lo - 1) * curH // 把 (右边界 减 左边界 减 1) 乘 curH 写入 area :
		if area > res {              // 若 area 超过 结果
			res = area // 把 area 写入 结果
		}
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		n    int   // 元素个数 int
		h    []int // h []int
		want int   // want int
	}{ // }{
		{5, []int{0, 2, 3, 3, 3, 2, 0}, 10},
		{1, []int{0, 1, 0}, 1},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := getResult(c.n, c.h); got != c.want { // 若 got : 赋值为 getResult(字符.元素个数, 字符.h); got 不等于 字符.want
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL getResult(%d,%v)=%d want %d\n", c.n, c.h, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
