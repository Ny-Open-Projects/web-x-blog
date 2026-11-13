// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// getMin 弹出栈中所有元素并找出其中最小值，其余元素压回（栈中移除一个最小值）。
func getMin(stack *[]int) int { // 定义函数/方法 getMin
	s := *stack      // 把 乘 栈 写入 s :
	if len(s) == 1 { // 若 长度(字符串) 等于 1
		*stack = s[:0]
		return s[0] // 返回 字符串[0]
	}
	top := s[len(s)-1] // 把 字符串[长度(字符串) 减 1] 写入 top :
	*stack = s[:len(s)-1]
	restMin := getMin(stack) // 把 getMin(栈) 写入 restMin :
	if top < restMin {       // 若 top 小于 restMin
		*stack = append(*stack, restMin)
		return top // 返回 top
	}
	*stack = append(*stack, top)
	return restMin // 返回 restMin
}

// sortStackMin 用“反复取最小值”的方式对栈排序（选择排序思想），得到升序列表。
func sortStackMin(stack []int) []int { // 定义函数/方法 sortStackMin
	res := []int{}       // 把 []int{} 写入 res :
	for len(stack) > 0 { // for 长度(栈) 超过 0 {
		res = append(res, getMin(&stack)) // 把 append(结果, getMin( 按位与 栈)) 写入 结果
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

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{3, 1, 4, 2}, []int{1, 2, 3, 4}},
		{[]int{1, 3, 2, 4}, []int{1, 2, 3, 4}},
		{[]int{1}, []int{1}},
		{[]int{}, []int{}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := sortStackMin(c.in); !eqIntSlice(got, c.want) { // 若 got : 赋值为 sortStackMin(字符.in); 取反 eqIntSlice(got, 字符.want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL sortStackMin(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
