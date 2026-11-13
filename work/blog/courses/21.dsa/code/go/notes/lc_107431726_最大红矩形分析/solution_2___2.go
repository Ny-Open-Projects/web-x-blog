// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// getResult 忠实翻译 python ref solution_2___2.py（卡位做法 O(n*m^2)）
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
		for a := 1; a <= m; a++ { // 让 数组 从 1 开始计数
			curH := height[a] // 把 height[数组] 写入 curH :
			// 找左卡位点
			lo := a - 1                         // 把 数组 减 1 写入 lo :
			for lo >= 1 && height[lo] >= curH { // 把 1 且 height[左边界] 不低于 curH { 写入 for lo >
				lo-- // 左边界 减一
			}
			// 找右卡位点
			hi := a + 1                         // 把 数组 加 1 写入 hi :
			for hi <= m && height[hi] >= curH { // 把 映射表 且 height[右边界] 不低于 curH { 写入 for hi <
				hi++ // 右边界 加一
			}
			area := (hi - lo - 1) * curH // 把 (右边界 减 左边界 减 1) 乘 curH 写入 area :
			if area > ans {              // 若 area 超过 答案
				ans = area // 把 area 写入 答案
			}
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
