// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145347672
package main // 引入依赖

import (
	"container/heap" // 「container 除以 堆」
	"fmt"            // 「fmt」
	"sort"           // 「sort」
)

type pHeap []int // 定义类型

func (h pHeap) Len() int           { return len(h) }            // 定义函数/方法 Len
func (h pHeap) Less(i, j int) bool { return h[i] > h[j] }       // 定义函数/方法 Less
func (h pHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }  // 定义函数/方法 Swap
func (h *pHeap) Push(x any)        { *h = append(*h, x.(int)) } // 定义函数/方法 Push
func (h *pHeap) Pop() any { // 定义函数/方法 Pop
	old := *h      // 把 乘 h 写入 old :
	n := len(old)  // 把 长度(old) 写入 n :
	it := old[n-1] // 把 old[元素个数 减 1] 写入 it :
	*h = old[:n-1]
	return it // 返回 it
}

func findMaximizedCapital(k int, w int, profits []int, capital []int) int { // 定义函数/方法 findMaximizedCapital
	n := len(profits)         // 把 长度(profits) 写入 n :
	indices := make([]int, n) // 把 make([]int, 元素个数) 写入 indices :
	for i := 0; i < n; i++ {  // 让 下标 i 从 0 开始计数
		indices[i] = i // 把 下标 i 写入 indices[i]
	}
	sort.Slice(indices, func(a, b int) bool { // sort.Slice(indices, func(数组, b int) bool {
		return capital[indices[a]] < capital[indices[b]] // 返回 capital[indices[数组]] 小于 capital[indices[b]]
	}) // })
	maxHeap := &pHeap{}      // 把 按位与 pHeap{} 写入 maxHeap :
	heap.Init(maxHeap)       // 堆.Init(maxHeap)
	i := 0                   // 把 0 写入 i :
	for t := 0; t < k; t++ { // 让 另一字符串 从 0 开始计数
		for i < n && capital[indices[i]] <= w { // 把 权重 { 写入 for i < n && capital[indices[i]] <
			heap.Push(maxHeap, profits[indices[i]]) // 堆.Push(maxHeap, profits[indices[下标 i]])
			i++                                     // 下标 i 加一
		}
		if maxHeap.Len() == 0 { // 若 maxHeap.Len() 等于 0
			break // 跳出循环
		}
		w += heap.Pop(maxHeap).(int) // 权重累加 堆.Pop(maxHeap).(int)
	}
	return w // 返回 权重
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		k       int   // 下标 k int
		w       int   // 权重 int
		profits []int // profits []int
		capital []int // capital []int
		want    int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{2, 0, []int{1, 2, 3}, []int{0, 1, 1}, 4},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := findMaximizedCapital(c.k, c.w, c.profits, c.capital)
		if got != c.want { // 若 got 不等于 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%d want=%d\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
