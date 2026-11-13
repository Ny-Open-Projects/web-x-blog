// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// Filler 填充器（迭代器风格）：按规则串（如 'ESVM' 逆时针）在 matrix 上逐格前进。
// 规则字母：E/S/V/M 表示 下/右/上/左；遇到边界后收缩对应的最小/最大行列，实现旋转填充。
type Filler struct { // 定义类型
	rowNum, colNum int    // rowNum, colNum int
	rule           string // rule string
	posRow, posCol int    // posRow, posCol int
	idx            int    // idx int
	rMin, cMin     int    // rMin, cMin int
	rMax, cMax     int    // rMax, cMax int
}

func NewFiller(rn, cn int) *Filler { // 定义函数/方法 NewFiller
	return &Filler{ // 返回 按位与 Filler{
		rowNum: rn, colNum: cn,
		rule:   "ESVM",
		posRow: 0, posCol: 0,
		idx:  0,
		rMin: 0, cMin: 0,
		rMax: rn - 1, cMax: cn - 1,
	}
}

func (f *Filler) setRule(r string) { f.rule = r } // 定义函数/方法 setRule

func (f *Filler) reset() { // 定义函数/方法 reset
	f.posRow, f.posCol = 0, 0 // 把 0, 0 写入 f.posRow, f.posCol
	f.idx = 0                 // 把 0 写入 f.idx
	f.rMin, f.cMin = 0, 0     // 把 0, 0 写入 f.rMin, f.cMin
	f.rMax = f.rowNum - 1     // 把 f.rowNum 减 1 写入 f.rMax
	f.cMax = f.colNum - 1     // 把 f.colNum 减 1 写入 f.cMax
}

// inBounds 对应 python __iter__ 的 while 条件
func (f *Filler) inBounds() bool { // 定义函数/方法 inBounds
	return f.rMin <= f.posRow && f.posRow <= f.rMax && f.cMin <= f.posCol && f.posCol <= f.cMax
}

func (f *Filler) advance() { // 定义函数/方法 advance
	cmd := f.rule[f.idx%4] // 把 f.rule[f.idx 对…取模 4] 写入 cmd :
	if cmd == 'E' {        // 向下
		f.posRow++              // f.posRow 加一
		if f.posRow == f.rMax { // 若 f.posRow 等于 f.rMax
			f.idx++  // f.idx 加一
			f.cMin++ // f.cMin 加一
		}
	} else if cmd == 'S' { // 向右
		f.posCol++              // f.posCol 加一
		if f.posCol == f.cMax { // 若 f.posCol 等于 f.cMax
			f.idx++  // f.idx 加一
			f.rMax-- // f.rMax 减一
		}
	} else if cmd == 'V' { // 向上
		f.posRow--              // f.posRow 减一
		if f.posRow == f.rMin { // 若 f.posRow 等于 f.rMin
			f.idx++  // f.idx 加一
			f.cMax-- // f.cMax 减一
		}
	} else if cmd == 'M' { // 向左
		f.posCol--              // f.posCol 减一
		if f.posCol == f.cMin { // 若 f.posCol 等于 f.cMin
			f.idx++  // f.idx 加一
			f.rMin++ // f.rMin 加一
		}
	}
}

// next 对应 python 生成器的一次 yield：先返回当前位置，再前进；越界返回 ok=false
func (f *Filler) next() (int, int, bool) { // 定义函数/方法 next
	if !f.inBounds() { // 若 取反 f.inBounds(
		return 0, 0, false // 返回 0, 0, false
	}
	r, c := f.posRow, f.posCol // 把 f.posRow, f.posCol 写入 r, c :
	f.advance()                // f.advance()
	return r, c, true          // 返回 右指针, 字符, true
}

func fillMatrix(rn, cn int, rule string) [][]int { // 定义函数/方法 fillMatrix
	mat := make([][]int, rn) // 把 make([][]int, rn) 写入 mat :
	for i := range mat {     // 把 range mat { 写入 for i :
		mat[i] = make([]int, cn) // 把 make([]int, cn) 写入 mat[i]
	}
	f := NewFiller(rn, cn) // 把 NewFiller(rn, cn) 写入 f :
	f.setRule(rule)        // f.setRule(rule)
	i := 1                 // 把 1 写入 i :
	for {                  // for {
		r, c, ok := f.next() // 把 f.下一个() 写入 r, c, ok :
		if !ok {             // 若 取反 ok
			break // 跳出循环
		}
		mat[r][c] = i // 把 下标 i 写入 mat[r][c]
		i++           // 下标 i 加一
	}
	return mat // 返回 mat
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
		rn, cn int     // rn, cn int
		rule   string  // rule string
		want   [][]int // want [][]int
	}{ // }{
		{6, 6, "ESVM", [][]int{ // {6, 6, 「ESVM」, [][]int{
			{1, 0, 0, 0, 0, 0},
			{2, 0, 0, 0, 0, 0},
			{3, 0, 0, 0, 0, 0},
			{4, 0, 0, 0, 0, 0},
			{5, 0, 0, 0, 0, 0},
			{0, 0, 0, 0, 0, 0},
		}},
		{4, 5, "ESVM", [][]int{ // {4, 5, 「ESVM」, [][]int{
			{1, 0, 0, 0, 0},
			{2, 0, 0, 0, 0},
			{3, 0, 0, 0, 0},
			{0, 0, 0, 0, 0},
		}},
		{1, 1, "ESVM", [][]int{{1}}},
		{2, 3, "ESVM", [][]int{{1, 0, 0}, {0, 0, 0}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := fillMatrix(c.rn, c.cn, c.rule); !eqMat(got, c.want) {
			ok = false                                                                            // 把 false 写入 ok
			fmt.Printf("FAIL fillMatrix(%d,%d,%q)=%v want %v\n", c.rn, c.cn, c.rule, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
