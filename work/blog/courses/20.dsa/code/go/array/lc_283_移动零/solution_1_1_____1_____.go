// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145116601
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// moveZeroes 把数组中的 0 移到末尾，保持非零元素的相对顺序。
// 忠实翻译自 Python 参考实现：双指针原地交换，返回结果切片。
func moveZeroes(nums []int) []int { // 定义函数/方法 moveZeroes
	res := make([]int, len(nums))               // 把 make([]int, 长度(数组)) 写入 res :
	copy(res, nums)                             // copy(结果, 数组)
	left := 0                                   // 把 0 写入 left :
	for right := 0; right < len(res); right++ { // 让 右边界 从 0 开始计数
		if res[right] != 0 { // 若 结果[右边界] 不等于 0
			res[left], res[right] = res[right], res[left] // 把 结果[右边界], 结果[左边界] 写入 res[left], res[right]
			left++                                        // 左边界 加一
		}
	}
	return res // 返回 结果
}

func eqIntSlice(a, b []int) bool { // 定义函数/方法 eqIntSlice
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

func selfCheck() bool { // 定义函数/方法 selfCheck
	// (args, expected) 取自 _tools/correctness_check.py 的 lc_283_移动零 cases
	cases := []struct { // 把 []struct { 写入 cases :
		name string // name string
		in   []int  // in []int
		want []int  // want []int
	}{ // }{
		{"case1", []int{0, 1, 0, 3, 12}, []int{1, 3, 12, 0, 0}},
		{"case2", []int{0}, []int{0}},
		{"case3", []int{1, 2, 3}, []int{1, 2, 3}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := moveZeroes(c.in)       // 把 moveZeroes(字符.in) 写入 got :
		if !eqIntSlice(got, c.want) { // 若 取反 eqIntSlice(got, 字符.want
			ok = false                                                   // 把 false 写入 ok
			fmt.Printf("FAIL %s: got %v want %v\n", c.name, got, c.want) // 打印输出
		}
	}
	return ok // 返回 ok
}

func main() { // 程序入口：跑内嵌自测用例
	if !selfCheck() { // 若 取反 selfCheck(
		fmt.Println("FAIL") // 打印输出
		os.Exit(1)          // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
