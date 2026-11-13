// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107431726
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// getResult 忠实翻译 python ref solution_1___1.py（蛮力 O(n*m^3)，左右哨兵 height）
func getResult(n, m int, matrix []string) int { // 定义函数/方法 getResult
	ans := 0                   // 把 0 写入 ans :
	height := make([]int, m+2) // height[1..m] 为当前行的列高，左右哨兵为 0
	for k := 0; k < n; k++ {   // 让 下标 k 从 0 开始计数
		for i := 1; i <= m; i++ { // 让 下标 i 从 1 开始计数
			if matrix[k][i-1] == '.' { // 若 矩阵[下标 k][下标 i 减 1] 等于 '.'
				height[i]++ // height[下标 i] 加一
			} else { // 否则
				height[i] = 0 // 把 0 写入 height[i]
			}
		}
		for a := 1; a <= m; a++ { // 让 数组 从 1 开始计数
			for b := a; b <= m; b++ { // 把 数组; b 不超过 映射表; b 加一 { 写入 for b :
				minH := 50000             // 把 50000 写入 minH :
				for c := a; c <= b; c++ { // 把 数组; 字符 不超过 b; 字符 加一 { 写入 for c :
					if height[c] < minH { // 若 height[字符] 小于 minH
						minH = height[c] // 把 height[字符] 写入 minH
					}
				}
				area := (b - a + 1) * minH // 把 (b 减 数组 加 1) 乘 minH 写入 area :
				if area > ans {            // 若 area 超过 答案
					ans = area // 把 area 写入 答案
				}
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
