// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/105893757
package main // 引入依赖

import (
	"fmt" // 「fmt」
	"os"  // 「os」
)

// sortStackRecursive 用递归对栈排序（栈底最小，栈顶最大）：弹出栈顶后先递归排序剩余部分，再有序插入。
func sortStackRecursive(stack []int) []int { // 定义函数/方法 sortStackRecursive
	if len(stack) == 0 { // 若 长度(栈) 等于 0
		return stack // 返回 栈
	}
	top := stack[len(stack)-1]        // 把 栈[长度(栈) 减 1] 写入 top :
	stack = stack[:len(stack)-1]      // 把 栈[:长度(栈) 减 1] 写入 栈
	stack = sortStackRecursive(stack) // 把 sortStackRecursive(栈) 写入 栈
	return sortedInsert(stack, top)   // 定义函数/方法 sortedInsert
}

func sortedInsert(stack []int, val int) []int { // 定义函数/方法 sortedInsert
	if len(stack) == 0 || val > stack[len(stack)-1] { // 若 长度(栈) 等于 0 或 值 超过 栈[长度(栈) 减 1]
		return append(stack, val) // 定义函数/方法 append
	}
	tmp := stack[len(stack)-1]       // 把 栈[长度(栈) 减 1] 写入 tmp :
	stack = stack[:len(stack)-1]     // 把 栈[:长度(栈) 减 1] 写入 栈
	stack = sortedInsert(stack, val) // 把 sortedInsert(栈, 值) 写入 栈
	return append(stack, tmp)        // 定义函数/方法 append
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
		{[]int{1, 3, 2, 4}, []int{1, 2, 3, 4}},
		{[]int{3, 1, 4, 2}, []int{1, 2, 3, 4}},
		{[]int{}, []int{}},
		{[]int{5}, []int{5}},
		{[]int{5, 4, 3, 2, 1}, []int{1, 2, 3, 4, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := sortStackRecursive(c.in); !eqIntSlice(got, c.want) {
			ok = false                                                                // 把 false 写入 ok
			fmt.Printf("FAIL sortStackRecursive(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
