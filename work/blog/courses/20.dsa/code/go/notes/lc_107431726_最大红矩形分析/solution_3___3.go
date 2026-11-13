// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// getResult 忠实翻译 python ref solution_3___3.py（单调栈 O(n*m)，哨兵 height[0]=height[m+1]=0）
func getResult(n, m int, matrix []string) int { // 定义函数/方法 getResult
	ans := 0                   // 把 0 写入 ans :
	height := make([]int, m+2) // 把 make([]int, 映射表 加 2) 写入 height :
	for k := 0; k < n; k++ {   // 让 下标 k 从 0 开始计数
		for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
			if matrix[k][i-1] == '.' { // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
				height[i]++ // height[下标 i] 加一
			} else { // 否则
				height[i] = 0 // 把 0 写入 height[i]
			}
		}
		stack := []int{0}           // 把 []int{0} 写入 stack :
		for i := 1; i <= m+1; i++ { // 让 下标 i 从 1 开始计数
			for len(stack) > 0 && height[stack[len(stack)-1]] > height[i] { // for 长度(栈) 超过 0 且 height[栈[长度(栈) 减 1]] 超过 height[下标 i] {
				nowH := height[stack[len(stack)-1]]  // 把 height[栈[长度(栈) 减 1]] 写入 nowH :
				stack = stack[:len(stack)-1]         // 把 栈[:长度(栈) 减 1] 写入 栈
				width := i - stack[len(stack)-1] - 1 // 把 下标 i 减 栈[长度(栈) 减 1] 减 1 写入 width :
				area := nowH * width                 // 把 nowH 乘 width 写入 area :
				if area > ans {                      // 若 area 超过 答案
					ans = area // 把 area 写入 答案
				}
			}
			stack = append(stack, i) // 把 append(栈, 下标 i) 写入 栈
		}
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		matrix []string // 矩阵 []string
		want   int      // want int
	}{ // }{
		{[]string{".....", "XXXXX", ".X...", "....."}, 6},
		{[]string{"...", "...", "..."}, 9},
		{[]string{"XXX", "XXX"}, 0},
		{[]string{"."}, 1},
		{[]string{"....", "....", "XXXX", "....", "...."}, 8},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := getResult(len(c.matrix), len(c.matrix[0]), c.matrix); got != c.want {
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL solve(%v)=%d want %d\n", c.matrix, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
