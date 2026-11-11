// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/107737496
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

type Location struct { // 定义类型
	Row int // Row int
	Col int // Col int
}

// Filler（ESVM 逆时针规则）
type Filler struct { // 定义类型
	rowNum, colNum int      // rowNum, colNum int
	pos            Location // pos Location
	idx            int      // idx int
	rMin, cMin     int      // rMin, cMin int
	rMax, cMax     int      // rMax, cMax int
	rule           string   // rule string
}

func NewFiller(rn, cn int) *Filler { // 定义函数/方法 NewFiller
	return &Filler{ // 返回 按位与 Filler{
		rowNum: rn, colNum: cn,
		pos:  Location{0, 0},
		idx:  0,
		rMin: 0, cMin: 0,
		rMax: rn - 1, cMax: cn - 1,
		rule: "ESVM",
	}
}

func (f *Filler) reset() { // 定义函数/方法 reset
	f.pos = Location{0, 0} // 把 Location{0, 0} 写入 f.pos
	f.idx = 0              // 把 0 写入 f.idx
	f.rMin, f.cMin = 0, 0  // 把 0, 0 写入 f.rMin, f.cMin
	f.rMax = f.rowNum - 1  // 把 f.rowNum 减 1 写入 f.rMax
	f.cMax = f.colNum - 1  // 把 f.colNum 减 1 写入 f.cMax
	f.rule = "ESVM"        // 把 「ESVM」 写入 f.rule
}

func (f *Filler) setRule(rule string) { f.rule = rule } // 定义函数/方法 setRule

func (f *Filler) next() Location { // 定义函数/方法 next
	res := f.pos                    // 把 f.pos 写入 res :
	ch := f.rule[f.idx%len(f.rule)] // 把 f.rule[f.idx 对…取模 长度(f.rule)] 写入 ch :
	if ch == 'E' {                  // 若 字符 等于 'E'
		f.pos.Row++              // f.pos.Row 加一
		if f.pos.Row == f.rMax { // 若 f.pos.Row 等于 f.rMax
			f.idx++  // f.idx 加一
			f.cMin++ // f.cMin 加一
		}
	} else if ch == 'S' { // 否则，若 字符 等于 'S'
		f.pos.Col++              // f.pos.Col 加一
		if f.pos.Col == f.cMax { // 若 f.pos.Col 等于 f.cMax
			f.idx++  // f.idx 加一
			f.rMax-- // f.rMax 减一
		}
	} else if ch == 'V' { // 否则，若 字符 等于 'V'
		f.pos.Row--              // f.pos.Row 减一
		if f.pos.Row == f.rMin { // 若 f.pos.Row 等于 f.rMin
			f.idx++  // f.idx 加一
			f.cMax-- // f.cMax 减一
		}
	} else if ch == 'M' { // 否则，若 字符 等于 'M'
		f.pos.Col--              // f.pos.Col 减一
		if f.pos.Col == f.cMin { // 若 f.pos.Col 等于 f.cMin
			f.idx++  // f.idx 加一
			f.rMin++ // f.rMin 加一
		}
	}
	return res // 返回 结果
}

// Matrix：Get 支持多下标访问 m(r, c)，Set 对应 python 的 __setitem__
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

func (m *Matrix) Get(r, c int) int { return m.buf[r][c] } // 定义函数/方法 Get

func (m *Matrix) Set(r, c, v int) { m.buf[r][c] = v } // 定义函数/方法 Set

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
	ok := true // 把 true 写入 ok :

	// 正常用例：9x9 逆时针填充（与 python 参考 demo 一致）
	rn := 9                      // 把 9 写入 rn :
	cn := 9                      // 把 9 写入 cn :
	obj := NewFiller(rn, cn)     // 把 NewFiller(rn, cn) 写入 obj :
	obj.setRule("ESVM")          // 逆时针
	m := NewMatrix(rn, cn)       // 把 NewMatrix(rn, cn) 写入 m :
	for i := 0; i < rn*cn; i++ { // 让 下标 i 从 0 开始计数
		p := obj.next()          // 把 obj.下一个() 写入 p :
		m.Set(p.Row, p.Col, i+1) // 映射表.Set(节点.Row, 节点.Col, 下标 i 加 1)
	}
	want9 := [][]int{ // 把 [][]int{ 写入 want9 :
		{1, 32, 31, 30, 29, 28, 27, 26, 25},
		{2, 33, 56, 55, 54, 53, 52, 51, 24},
		{3, 34, 57, 72, 71, 70, 69, 50, 23},
		{4, 35, 58, 73, 80, 79, 68, 49, 22},
		{5, 36, 59, 74, 81, 78, 67, 48, 21},
		{6, 37, 60, 75, 76, 77, 66, 47, 20},
		{7, 38, 61, 62, 63, 64, 65, 46, 19},
		{8, 39, 40, 41, 42, 43, 44, 45, 18},
		{9, 10, 11, 12, 13, 14, 15, 16, 17},
	}
	if !eqMat(m.buf, want9) { // 若 取反 eqMat(映射表.buf, want9
		ok = false                                             // 把 false 写入 ok
		fmt.Printf("FAIL 9x9 fill=%v want %v\n", m.buf, want9) // 打印输出
	}

	// 边界用例：1x1
	f1 := NewFiller(1, 1)    // 把 NewFiller(1, 1) 写入 f1 :
	m1 := NewMatrix(1, 1)    // 把 NewMatrix(1, 1) 写入 m1 :
	for i := 0; i < 1; i++ { // 让 下标 i 从 0 开始计数
		p := f1.next()            // 把 f1.下一个() 写入 p :
		m1.Set(p.Row, p.Col, i+1) // m1.Set(节点.Row, 节点.Col, 下标 i 加 1)
	}
	if !eqMat(m1.buf, [][]int{{1}}) { // 若 取反 eqMat(m1.buf, [][]int{{1}}
		ok = false                                          // 把 false 写入 ok
		fmt.Printf("FAIL 1x1 fill=%v want [[1]]\n", m1.buf) // 打印输出
	}

	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
