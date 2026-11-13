// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347297
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func nextGreaterElements(nums []int) []int { // 定义函数/方法 nextGreaterElements
	n := len(nums)           // 把 长度(数组) 写入 n :
	result := make([]int, n) // 把 make([]int, 元素个数) 写入 result :
	for i := range result {  // 把 range 结果 { 写入 for i :
		result[i] = -1 // 把 减 1 写入 result[i]
	}
	stack := []int{}           // 把 []int{} 写入 stack :
	for i := 0; i < 2*n; i++ { // 让 下标 i 从 0 开始计数
		num := nums[i%n]                                        // 把 数组[下标 i 对…取模 元素个数] 写入 num :
		for len(stack) > 0 && nums[stack[len(stack)-1]] < num { // for 长度(栈) 超过 0 且 数组[栈[长度(栈) 减 1]] 小于 num {
			idx := stack[len(stack)-1]   // 把 栈[长度(栈) 减 1] 写入 idx :
			stack = stack[:len(stack)-1] // 把 栈[:长度(栈) 减 1] 写入 栈
			result[idx] = num            // 把 num 写入 result[idx]
		}
		if i < n { // 若 下标 i 小于 元素个数
			stack = append(stack, i) // 把 append(栈, 下标 i) 写入 栈
		}
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 1}, []int{2, -1, 2}},
		{[]int{1, 2, 3, 4, 3}, []int{2, 3, 4, -1, 4}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := nextGreaterElements(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                 // 把 false 写入 ok
			fmt.Printf("FAIL nextGreaterElements(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
