// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145397916
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
	"sort"    // 「sort」
)

func secondGreaterElement(nums []int) []int { // 定义函数/方法 secondGreaterElement
	n := len(nums)        // 把 长度(数组) 写入 n :
	res := make([]int, n) // 把 make([]int, 元素个数) 写入 res :
	for i := range res {  // 把 range 结果 { 写入 for i :
		res[i] = -1 // 把 减 1 写入 res[i]
	}
	stack := []int{}         // 把 []int{} 写入 stack :
	pq := [][2]int{}         // 把 [][2]int{} 写入 pq :
	for i := 0; i < n; i++ { // 让 下标 i 从 0 开始计数
		for len(pq) > 0 && pq[0][0] < nums[i] { // for 长度(优先队列) 超过 0 且 优先队列[0][0] 小于 数组[下标 i] {
			idx := pq[0][1]    // 把 优先队列[0][1] 写入 idx :
			res[idx] = nums[i] // 把 数组[下标 i] 写入 res[idx]
			pq = pq[1:]        // 把 优先队列[1:] 写入 优先队列
		}
		for len(stack) > 0 && nums[stack[len(stack)-1]] < nums[i] { // for 长度(栈) 超过 0 且 数组[栈[长度(栈) 减 1]] 小于 数组[下标 i] {
			idx := stack[len(stack)-1]              // 把 栈[长度(栈) 减 1] 写入 idx :
			stack = stack[:len(stack)-1]            // 把 栈[:长度(栈) 减 1] 写入 栈
			pq = append(pq, [2]int{nums[idx], idx}) // 把 append(优先队列, [2]int{数组[idx], idx}) 写入 优先队列
			sort.Slice(pq, func(a, b int) bool { return pq[a][0] < pq[b][0] })
		}
		stack = append(stack, i) // 把 append(栈, 下标 i) 写入 栈
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{1, 2, 3}, []int{3, -1, -1}},
		{[]int{2, 4, 0, 9, 6}, []int{9, 6, 6, -1, -1}},
		{[]int{4, 2, 5, 8, 3, 1, 7}, []int{8, 8, 7, -1, -1, -1, -1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := secondGreaterElement(c.in); !reflect.DeepEqual(got, c.want) {
			ok = false                                                                  // 把 false 写入 ok
			fmt.Printf("FAIL secondGreaterElement(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
