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

// Filler 填充器：依据规则串（如 ESVM 逆时针 / semv 顺时针）逐位置前进（方案 9）。
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

func (f *Filler) current() Location { return f.pos } // 定义函数/方法 current

// next 先返回当前位置副本，再按规则前进（对应 python __next__）
func (f *Filler) next() Location { // 定义函数/方法 next
	res := f.pos                    // 把 f.pos 写入 res :
	ch := f.rule[f.idx%len(f.rule)] // 把 f.rule[f.idx 对…取模 长度(f.rule)] 写入 ch :
	if ch == 'E' {                  // 向下
		f.pos.Row++              // f.pos.Row 加一
		if f.pos.Row == f.rMax { // 若 f.pos.Row 等于 f.rMax
			f.idx++  // f.idx 加一
			f.cMin++ // f.cMin 加一
		}
	} else if ch == 'S' { // 向右
		f.pos.Col++              // f.pos.Col 加一
		if f.pos.Col == f.cMax { // 若 f.pos.Col 等于 f.cMax
			f.idx++  // f.idx 加一
			f.rMax-- // f.rMax 减一
		}
	} else if ch == 'V' { // 向上
		f.pos.Row--              // f.pos.Row 减一
		if f.pos.Row == f.rMin { // 若 f.pos.Row 等于 f.rMin
			f.idx++  // f.idx 加一
			f.cMax-- // f.cMax 减一
		}
	} else if ch == 'M' { // 向左
		f.pos.Col--              // f.pos.Col 减一
		if f.pos.Col == f.cMin { // 若 f.pos.Col 等于 f.cMin
			f.idx++  // f.idx 加一
			f.rMin++ // f.rMin 加一
		}
	} else if ch == 'e' { // 顺时针：向下
		f.pos.Row++              // f.pos.Row 加一
		if f.pos.Row == f.rMax { // 若 f.pos.Row 等于 f.rMax
			f.idx++  // f.idx 加一
			f.cMax-- // f.cMax 减一
		}
	} else if ch == 's' { // 顺时针：向右
		f.pos.Col++              // f.pos.Col 加一
		if f.pos.Col == f.cMax { // 若 f.pos.Col 等于 f.cMax
			f.idx++  // f.idx 加一
			f.rMin++ // f.rMin 加一
		}
	} else if ch == 'v' { // 顺时针：向上
		f.pos.Row--              // f.pos.Row 减一
		if f.pos.Row == f.rMin { // 若 f.pos.Row 等于 f.rMin
			f.idx++  // f.idx 加一
			f.cMin++ // f.cMin 加一
		}
	} else if ch == 'm' { // 顺时针：向左
		f.pos.Col--              // f.pos.Col 减一
		if f.pos.Col == f.cMin { // 若 f.pos.Col 等于 f.cMin
			f.idx++  // f.idx 加一
			f.rMax-- // f.rMax 减一
		}
	}
	return res // 返回 结果
}

func test(rule string, rn, cn int) []Location { // 定义函数/方法 test
	obj := NewFiller(rn, cn)          // 把 NewFiller(rn, cn) 写入 obj :
	obj.setRule(rule)                 // obj.setRule(rule)
	seq := make([]Location, 0, rn*cn) // 把 make([]Location, 0, rn 乘 cn) 写入 seq :
	for i := 0; i < rn*cn; i++ {      // 让 下标 i 从 0 开始计数
		seq = append(seq, obj.next()) // 把 append(seq, obj.下一个()) 写入 seq
	}
	return seq // 返回 seq
}

func eqSeq(a, b []Location) bool { // 定义函数/方法 eqSeq
	if len(a) != len(b) { // 定义函数/方法 len
		return false // 返回 false
	}
	for i := range a { // 把 range 数组 { 写入 for i :
		if a[i] != b[i] { // 若 数组[下标 i] 不等于 b[下标 i]
			return false // 返回 false
		}
	}
	return true // 返回 true
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		rule   string     // rule string
		rn, cn int        // rn, cn int
		want   []Location // want []Location
	}{ // }{
		{"ESVM", 4, 4, []Location{ // {「ESVM」, 4, 4, []Location{
			{0, 0}, {1, 0}, {2, 0}, {3, 0}, {3, 1}, {3, 2}, {3, 3}, {2, 3},
			{1, 3}, {0, 3}, {0, 2}, {0, 1}, {1, 1}, {2, 1}, {2, 2}, {1, 2},
		}},
		{"semv", 4, 4, []Location{ // {「semv」, 4, 4, []Location{
			{0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 3}, {2, 3}, {3, 3}, {3, 2},
			{3, 1}, {3, 0}, {2, 0}, {1, 0}, {1, 1}, {1, 2}, {2, 2}, {2, 1},
		}},
		{"ESVM", 1, 1, []Location{{0, 0}}},
		{"semv", 2, 2, []Location{{0, 0}, {0, 1}, {1, 1}, {1, 0}}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := test(c.rule, c.rn, c.cn); !eqSeq(got, c.want) {
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL test(%q,%d,%d)=%v want %v\n", c.rule, c.rn, c.cn, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
