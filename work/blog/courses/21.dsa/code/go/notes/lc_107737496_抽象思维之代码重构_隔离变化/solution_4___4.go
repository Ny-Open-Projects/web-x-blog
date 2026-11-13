// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// placeFill 依据前一位置、方向（DRUL 逆时针）与边界规则确定下一个摆放位置（方案 4）。
func placeFill(n int) [][]int { // 定义函数/方法 placeFill
	m := make([][]int, n) // 把 make([][]int, 元素个数) 写入 m :
	for i := range m {    // 把 range 映射表 { 写入 for i :
		m[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 m[i]
	}
	row, col := 0, 0   // 把 0, 0 写入 row, col :
	direction := "D"   // D 向下, R 向右, U 向上, L 向左（逆时针）
	num := 1           // 把 1 写入 num :
	total := n * n     // 把 元素个数 乘 元素个数 写入 total :
	for num <= total { // 把 总和 { 写入 for num <
		m[row][col] = num     // 把 num 写入 m[row][col]
		num++                 // num 加一
		if direction == "D" { // 若 direction 等于 「D」
			if row+1 < n && m[row+1][col] == 0 { // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
				row++ // row 加一
			} else { // 否则
				direction = "R" // 把 「R」 写入 direction
				col++           // col 加一
			}
		} else if direction == "R" { // 否则，若 direction 等于 「R」
			if col+1 < n && m[row][col+1] == 0 { // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
				col++ // col 加一
			} else { // 否则
				direction = "U" // 把 「U」 写入 direction
				row--           // row 减一
			}
		} else if direction == "U" { // 否则，若 direction 等于 「U」
			if row-1 >= 0 && m[row-1][col] == 0 { // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0
				row-- // row 减一
			} else { // 否则
				direction = "L" // 把 「L」 写入 direction
				col--           // col 减一
			}
		} else { // 'L'
			if col-1 >= 0 && m[row][col-1] == 0 { // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0
				col-- // col 减一
			} else { // 否则
				direction = "D" // 把 「D」 写入 direction
				row++           // row 加一
			}
		}
	}
	return m // 返回 映射表
}

func eqMat(a, b [][]int) bool { // 定义函数/方法 eqMat
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if len(a[i]) != len(b[i]) { // 定义函数/方法 len
			return false // 返回 false
		}
		for j := range a[i] { // 把 range 数组[下标 i] { 写入 for j :
			if a[i][j] != b[i][j] { // 若 数组[下标 i][下标 j] 不等于 b[下标 i][下标 j]
				return false // 返回 false
			}
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		n    int     // 元素个数 int
		want [][]int // want [][]int
	}{ // }{
		{6, [][]int{ // {6, [][]int{
			{1, 20, 19, 18, 17, 16},
			{2, 21, 32, 31, 30, 15},
			{3, 22, 33, 36, 29, 14},
			{4, 23, 34, 35, 28, 13},
			{5, 24, 25, 26, 27, 12},
			{6, 7, 8, 9, 10, 11},
		}},
		{1, [][]int{{1}}},
		{2, [][]int{{1, 4}, {2, 3}}},
		{3, [][]int{{1, 8, 7}, {2, 9, 6}, {3, 4, 5}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := placeFill(c.n); !eqMat(got, c.want) { // 若 got : 赋值为 placeFill(字符.元素个数); 取反 eqMat(got, 字符.want
			ok = false                                                      // 把 false 写入 ok
			fmt.Printf("FAIL placeFill(%d)=%v want %v\n", c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
