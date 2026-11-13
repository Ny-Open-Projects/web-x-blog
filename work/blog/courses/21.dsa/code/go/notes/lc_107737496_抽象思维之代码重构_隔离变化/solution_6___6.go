// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"strings" // 「strings」
)

// Matrix 矩阵类：用 Get 支持多下标访问 m(r, c)，并支持打印（方案 6）。
type Matrix struct { // 定义类型
	row, col int     // row, col int
	buf      [][]int // buf [][]int
}

func NewMatrix(r, c int) *Matrix { // 定义函数/方法 NewMatrix
	buf := make([][]int, r) // 把 make([][]int, 右指针) 写入 buf :
	for i := range buf {    // 把 range buf { 写入 for i :
		buf[i] = make([]int, c) // 把 make([]int, 字符) 写入 buf[i]
	}
	return &Matrix{row: r, col: c, buf: buf} // 返回 按位与 Matrix{row: 右指针, col: 字符, buf: buf}
}

func (m *Matrix) Get(rr, cc int) int { return m.buf[rr][cc] } // 定义函数/方法 Get

func (m *Matrix) str() string { // 定义函数/方法 str
	lines := []string{}         // 把 []string{} 写入 lines :
	for _, row := range m.buf { // 同时取 _ 与 row 遍历
		cells := []string{}     // 把 []string{} 写入 cells :
		for _, x := range row { // 同时取 _ 与 x 遍历
			cells = append(cells, fmt.Sprintf("%2d", x)) // 打印输出
		}
		lines = append(lines, strings.Join(cells, " ")) // 把 append(lines, strings.Join(cells, 「 」)) 写入 lines
	}
	return strings.Join(lines, "\n") // 返回 strings.Join(lines, 「 」)
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :

	// 正常用例：4x5 矩阵，m[i][j] = i*j（直接写 buf，与 python 参考一致）
	m := NewMatrix(4, 5)     // 把 NewMatrix(4, 5) 写入 m :
	for i := 0; i < 4; i++ { // 让 下标 i 从 0 开始计数
		for j := 0; j < 5; j++ { // 让 下标 j 从 0 开始计数
			m.buf[i][j] = i * j // 把 下标 i 乘 下标 j 写入 m.buf[i][j]
		}
	}
	if m.Get(2, 3) != 6 { // 若 映射表.Get(2, 3) 不等于 6
		ok = false                                          // 把 false 写入 ok
		fmt.Printf("FAIL m(2, 3)=%d want 6\n", m.Get(2, 3)) // 打印输出
	}
	if m.Get(1, 4) != 4 { // 若 映射表.Get(1, 4) 不等于 4
		ok = false                                          // 把 false 写入 ok
		fmt.Printf("FAIL m(1, 4)=%d want 4\n", m.Get(1, 4)) // 打印输出
	}
	wantStr := " 0  0  0  0  0\n 0  1  2  3  4\n 0  2  4  6  8\n 0  3  6  9 12" // 把 「 0 0 0 0 0 0 1 2 3 4 0 2 4 6 8 0 3 6 9 12」 写入 wantStr :
	if m.str() != wantStr {                                                     // 若 映射表.str() 不等于 wantStr
		ok = false                                              // 把 false 写入 ok
		fmt.Printf("FAIL str()=%q want %q\n", m.str(), wantStr) // 打印输出
	}

	// 边界用例：1x1
	one := NewMatrix(1, 1)  // 把 NewMatrix(1, 1) 写入 one :
	one.buf[0][0] = 7       // 把 7 写入 one.buf[0][0]
	if one.Get(0, 0) != 7 { // 若 one.Get(0, 0) 不等于 7
		ok = false                                                 // 把 false 写入 ok
		fmt.Printf("FAIL one.Get(0,0)=%d want 7\n", one.Get(0, 0)) // 打印输出
	}

	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
