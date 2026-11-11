// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// 将 num 开头的数，从 (begin, begin) 开始逆时针旋转填充 size*size 的子矩阵。
func fill(matrix [][]int, num, begin, size int) int { // 定义函数/方法 fill
	if size == 0 { // 若 大小 等于 0
		return num // 返回 num
	}
	if size == 1 { // 若 大小 等于 1
		matrix[begin][begin] = num // 把 num 写入 matrix[begin][begin]
		return num + 1             // 返回 num 加 1
	}
	// 左列向下
	for j := 0; j < size-1; j++ { // 让 下标 j 从 0 开始计数
		matrix[begin+j][begin] = num // 把 num 写入 matrix[begin+j][begin]
		num++                        // num 加一
	}
	// 底行向右
	for j := 0; j < size-1; j++ { // 让 下标 j 从 0 开始计数
		matrix[begin+size-1][begin+j] = num // 把 num 写入 matrix[begin+size-1][begin+j]
		num++                               // num 加一
	}
	// 右列向上
	for j := size - 1; j > 0; j-- { // 把 大小 减 1; 下标 j 超过 0; 下标 j 减一 { 写入 for j :
		matrix[begin+j][begin+size-1] = num // 把 num 写入 matrix[begin+j][begin+size-1]
		num++                               // num 加一
	}
	// 顶行向左
	for j := size - 1; j > 0; j-- { // 把 大小 减 1; 下标 j 超过 0; 下标 j 减一 { 写入 for j :
		matrix[begin][begin+j] = num // 把 num 写入 matrix[begin][begin+j]
		num++                        // num 加一
	}
	return fill(matrix, num, begin+1, size-2) // 定义函数/方法 fill
}

func generateSquareMatrix(n int) [][]int { // 定义函数/方法 generateSquareMatrix
	m := make([][]int, n) // 把 make([][]int, 元素个数) 写入 m :
	for i := range m {    // 把 range 映射表 { 写入 for i :
		m[i] = make([]int, n) // 把 make([]int, 元素个数) 写入 m[i]
	}
	fill(m, 1, 0, n) // fill(映射表, 1, 0, 元素个数)
	return m         // 返回 映射表
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
		if got := generateSquareMatrix(c.n); !eqMat(got, c.want) {
			ok = false                                                                 // 把 false 写入 ok
			fmt.Printf("FAIL generateSquareMatrix(%d)=%v want %v\n", c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
