// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133625091
package main // 引入依赖

import (
	"container/heap" // 「container 除以 堆」
	"fmt"            // 「fmt」
)

type uItem struct { // 定义类型
	val int // 值 int
	idx int // idx int
}

type uHeap []uItem // 定义类型

func (h uHeap) Len() int           { return len(h) }              // 定义函数/方法 Len
func (h uHeap) Less(i, j int) bool { return h[i].val < h[j].val } // 定义函数/方法 Less
func (h uHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }    // 定义函数/方法 Swap
func (h *uHeap) Push(x any)        { *h = append(*h, x.(uItem)) } // 定义函数/方法 Push
func (h *uHeap) Pop() any { // 定义函数/方法 Pop
	old := *h      // 把 乘 h 写入 old :
	n := len(old)  // 把 长度(old) 写入 n :
	it := old[n-1] // 把 old[元素个数 减 1] 写入 it :
	*h = old[:n-1]
	return it // 返回 it
}

func nthSuperUglyNumber(n int, primes []int) int { // 定义函数/方法 nthSuperUglyNumber
	ugly := make([]int, n)        // 把 make([]int, 元素个数) 写入 ugly :
	ugly[0] = 1                   // 把 1 写入 ugly[0]
	p := make([]int, len(primes)) // 把 make([]int, 长度(primes)) 写入 p :
	h := &uHeap{}                 // 把 按位与 uHeap{} 写入 h :
	heap.Init(h)                  // 堆.Init(h)
	for j := range primes {       // 把 range primes { 写入 for j :
		heap.Push(h, uItem{val: primes[j], idx: j}) // 堆.Push(h, uItem{值: primes[下标 j], idx: 下标 j})
	}
	for i := 1; i < n; i++ { // 让 下标 i 从 1 开始计数
		it := heap.Pop(h).(uItem) // 把 堆.Pop(h).(uItem) 写入 it :
		val := it.val             // 把 it.值 写入 val :
		for val == ugly[i-1] {    // 把 赋值为 ugly[下标 i 减 1] { 写入 for val
			p[it.idx]++ // 节点[it.idx] 加一
			heap.Push(h, uItem{val: ugly[p[it.idx]] * primes[it.idx], idx: it.idx})
			it = heap.Pop(h).(uItem) // 把 堆.Pop(h).(uItem) 写入 it
			val = it.val             // 把 it.值 写入 值
		}
		ugly[i] = val // 把 值 写入 ugly[i]
		p[it.idx]++   // 节点[it.idx] 加一
		heap.Push(h, uItem{val: ugly[p[it.idx]] * primes[it.idx], idx: it.idx})
	}
	return ugly[n-1] // 返回 ugly[元素个数 减 1]
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		n      int   // 元素个数 int
		primes []int // primes []int
		want   int   // want int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{12, []int{2, 7, 13, 19}, 32},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := nthSuperUglyNumber(c.n, c.primes) // 把 nthSuperUglyNumber(字符.元素个数, 字符.primes) 写入 got :
		if got != c.want {                       // 若 got 不等于 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%d want=%d\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
