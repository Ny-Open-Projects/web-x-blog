// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func getResult(n int, h []int) int { // 定义函数/方法 getResult
	res := 0                  // 把 0 写入 res :
	for a := 1; a <= n; a++ { // 让 数组 从 1 开始计数
		for b := a; b <= n; b++ { // 把 数组; b 不超过 元素个数; b 加一 { 写入 for b :
			minH := 50000             // 把 50000 写入 minH :
			for c := a; c <= b; c++ { // 把 数组; 字符 不超过 b; 字符 加一 { 写入 for c :
				if h[c] < minH { // 若 h[字符] 小于 minH
					minH = h[c] // 把 h[字符] 写入 minH
				}
			}
			area := (b - a + 1) * minH // 把 (b 减 数组 加 1) 乘 minH 写入 area :
			if area > res {            // 若 area 超过 结果
				res = area // 把 area 写入 结果
			}
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
