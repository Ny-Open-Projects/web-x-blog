// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// place 根据前一位置、方向(DRUL)与边界规则确定下一个摆放数据的位置（方案 7）。
// 返回值：新行、新列；changed 为 true 时 newDir 为更新后的方向（对应 python 的三元素返回）。
func place(num, row, col int, direction string, n int, m [][]int) (int, int, string, bool) { // 定义函数/方法 place
	switch direction { // switch direction {
	case "D": // case 「D」:
		if row+1 < n && m[row+1][col] == 0 { // 若 row 加 1 小于 元素个数 且 映射表[row 加 1][col] 等于 0
			return row + 1, col, direction, false // 返回 row 加 1, col, direction, false
		}
		return row, col + 1, "R", true // 返回 row, col 加 1, 「R」, true
	case "R": // case 「R」:
		if col+1 < n && m[row][col+1] == 0 { // 若 col 加 1 小于 元素个数 且 映射表[row][col 加 1] 等于 0
			return row, col + 1, direction, false // 返回 row, col 加 1, direction, false
		}
		return row - 1, col, "U", true // 返回 row 减 1, col, 「U」, true
	case "U": // case 「U」:
		if row-1 >= 0 && m[row-1][col] == 0 { // 若 row 减 1 不低于 0 且 映射表[row 减 1][col] 等于 0
			return row - 1, col, direction, false // 返回 row 减 1, col, direction, false
		}
		return row, col - 1, "L", true // 返回 row, col 减 1, 「L」, true
	default: // 'L'
		if col-1 >= 0 && m[row][col-1] == 0 { // 若 col 减 1 不低于 0 且 映射表[row][col 减 1] 等于 0
			return row, col - 1, direction, false // 返回 row, col 减 1, direction, false
		}
		return row + 1, col, "D", true // 返回 row 加 1, col, 「D」, true
	}
}

func fillSpiral(n int) [][]int { // 定义函数/方法 fillSpiral
	m := make([][]int, n) // 把 make([][]int, 元素个数) 写入 m :
	for i := range m {    // 把 range 映射表 { 写入 for i :
		m[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 m[i]
	}
	row, col := 0, 0 // 把 0, 0 写入 row, col :
	direction := "D" // 把 「D」 写入 direction :
	num := 1         // 把 1 写入 num :
	for num <= n*n { // 把 元素个数 乘 元素个数 { 写入 for num <
		m[row][col] = num // 把 num 写入 m[row][col]
		num++             // num 加一
		nr, nc, nd, changed := place(num, row, col, direction, n, m)
		row, col = nr, nc // 把 nr, nc 写入 row, col
		if changed {      // 若 changed
			direction = nd // 把 nd 写入 direction
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
		if got := fillSpiral(c.n); !eqMat(got, c.want) { // 若 got : 赋值为 fillSpiral(字符.元素个数); 取反 eqMat(got, 字符.want
			ok = false                                                       // 把 false 写入 ok
			fmt.Printf("FAIL fillSpiral(%d)=%v want %v\n", c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
