// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347105
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

func nextGreaterElement(nums1, nums2 []int) []int { // 定义函数/方法 nextGreaterElement
	stack := []int{}            // 把 []int{} 写入 stack :
	greaterMap := map[int]int{} // 把 映射表[int]int{} 写入 greaterMap :
	for _, num := range nums2 { // 同时取 _ 与 num 遍历
		for len(stack) > 0 && stack[len(stack)-1] < num { // for 长度(栈) 超过 0 且 栈[长度(栈) 减 1] 小于 num {
			greaterMap[stack[len(stack)-1]] = num // 把 num 写入 greaterMap[stack[len(stack)-1]]
			stack = stack[:len(stack)-1]          // 把 栈[:长度(栈) 减 1] 写入 栈
		}
		stack = append(stack, num) // 把 append(栈, num) 写入 栈
	}
	result := []int{}           // 把 []int{} 写入 result :
	for _, num := range nums1 { // 同时取 _ 与 num 遍历
		if v, ok := greaterMap[num]; ok { // 若 值, ok : 赋值为 greaterMap[num]; ok
			result = append(result, v) // 把 append(结果, 值) 写入 结果
		} else { // 否则
			result = append(result, -1) // 把 append(结果, 减 1) 写入 结果
		}
	}
	return result // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in1  []int // in1 []int
		in2  []int // in2 []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{4, 1, 2}, []int{1, 3, 4, 2}, []int{-1, 3, -1}},
		{[]int{2, 4}, []int{1, 2, 3, 4}, []int{3, -1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := nextGreaterElement(c.in1, c.in2); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                           // 把 false 写入 ok
			fmt.Printf("FAIL nextGreaterElement(%v,%v)=%v want %v\n", c.in1, c.in2, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
