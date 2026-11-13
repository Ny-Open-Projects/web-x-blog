// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107391023
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

func getResult(n int, h []int) int { // 定义函数/方法 getResult
	res := 0                    // 把 0 写入 res :
	stack := []int{0}           // 把 []int{0} 写入 stack :
	for i := 1; i <= n+1; i++ { // 让 下标 i 从 1 开始计数
		for len(stack) > 0 && h[stack[len(stack)-1]] > h[i] { // for 长度(栈) 超过 0 且 h[栈[长度(栈) 减 1]] 超过 h[下标 i] {
			nowH := h[stack[len(stack)-1]]       // 把 h[栈[长度(栈) 减 1]] 写入 nowH :
			stack = stack[:len(stack)-1]         // 把 栈[:长度(栈) 减 1] 写入 栈
			width := i - stack[len(stack)-1] - 1 // 把 下标 i 减 栈[长度(栈) 减 1] 减 1 写入 width :
			area := nowH * width                 // 把 nowH 乘 width 写入 area :
			if area > res {                      // 若 area 超过 结果
				res = area // 把 area 写入 结果
			}
		}
		stack = append(stack, i) // 把 append(栈, 下标 i) 写入 栈
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
