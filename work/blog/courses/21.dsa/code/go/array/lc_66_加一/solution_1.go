package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

// plusOne 加一。忠实翻译 Python 参考实现 ref_plusOne。
func plusOne(digits []int) []int { // 定义函数/方法 plusOne
	d := make([]int, len(digits))      // 把 make([]int, 长度(digits)) 写入 d :
	copy(d, digits)                    // copy(d, digits)
	for i := len(d) - 1; i >= 0; i-- { // 把 长度(d) 减 1; 下标 i 不低于 0; 下标 i 减一 { 写入 for i :
		if d[i] == 9 { // 若 d[下标 i] 等于 9
			d[i] = 0 // 把 0 写入 d[i]
		} else { // 否则
			d[i]++   // d[下标 i] 加一
			return d // 返回 d
		}
	}
	res := make([]int, len(digits)+1) // 把 make([]int, 长度(digits) 加 1) 写入 res :
	res[0] = 1                        // 把 1 写入 res[0]
	return res                        // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	// 用例来自 _tools/correctness_check.py PROBLEMS["lc_66_加一"]
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3}, []int{1, 2, 4}},
		{[]int{4, 3, 2, 1}, []int{4, 3, 2, 2}},
		{[]int{9, 9, 9}, []int{1, 0, 0, 0}},
	}
	allOK := true             // 把 true 写入 allOK :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := plusOne(c.in)                 // 把 plusOne(字符.in) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			allOK = false                                                     // 把 false 写入 allOK
			fmt.Printf("FAIL plusOne(%v) = %v, want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !allOK { // 若 取反 allOK
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
