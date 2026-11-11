// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package main // 引入依赖

import (
	"container/heap" // 「container 除以 堆」
	"fmt"            // 「fmt」
	"reflect"        // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

type hItem struct { // 定义类型
	val  int       // 值 int
	idx  int       // idx int
	node *ListNode // 节点 乘 ListNode
}

type minHeap []hItem // 定义类型

func (h minHeap) Len() int { return len(h) } // 定义函数/方法 Len
func (h minHeap) Less(i, j int) bool { // 定义函数/方法 Less
	if h[i].val != h[j].val { // 若 h[下标 i].值 不等于 h[下标 j].值
		return h[i].val < h[j].val // 返回 h[下标 i].值 小于 h[下标 j].值
	}
	return h[i].idx < h[j].idx // 返回 h[下标 i].idx 小于 h[下标 j].idx
}
func (h minHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }    // 定义函数/方法 Swap
func (h *minHeap) Push(x any)   { *h = append(*h, x.(hItem)) } // 定义函数/方法 Push
func (h *minHeap) Pop() any { // 定义函数/方法 Pop
	old := *h      // 把 乘 h 写入 old :
	n := len(old)  // 把 长度(old) 写入 n :
	it := old[n-1] // 把 old[元素个数 减 1] 写入 it :
	*h = old[:n-1]
	return it // 返回 it
}

func merge_k_lists(lists []*ListNode) *ListNode { // 定义函数/方法 merge_k_lists
	h := &minHeap{}              // 把 按位与 minHeap{} 写入 h :
	heap.Init(h)                 // 堆.Init(h)
	for i, node := range lists { // 同时取 下标 i 与 节点 遍历
		if node != nil { // 若 节点 不等于 nil
			heap.Push(h, hItem{val: node.Val, idx: i, node: node}) // 堆.Push(h, hItem{值: 节点.Val, idx: 下标 i, 节点: 节点})
		}
	}
	dummy := &ListNode{} // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy        // 把 哨兵节点 写入 curr :
	for h.Len() > 0 {    // for h.Len() 超过 0 {
		it := heap.Pop(h).(hItem) // 把 堆.Pop(h).(hItem) 写入 it :
		curr.Next = it.node       // 把 it.节点 写入 curr.Next
		curr = curr.Next          // 把 当前值.Next 写入 当前值
		if it.node.Next != nil {  // 若 it.节点.Next 不等于 nil
			heap.Push(h, hItem{val: it.node.Next.Val, idx: it.idx, node: it.node.Next})
		}
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func build(arr []int) *ListNode { // 定义函数/方法 build
	dummy := &ListNode{}    // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy           // 把 哨兵节点 写入 curr :
	for _, v := range arr { // 同时取 _ 与 值 遍历
		curr.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 curr.Next
		curr = curr.Next              // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func toList(node *ListNode) []int { // 定义函数/方法 toList
	res := []int{}    // 把 []int{} 写入 res :
	for node != nil { // 把 nil { 写入 for node !
		res = append(res, node.Val) // 把 append(结果, 节点.Val) 写入 结果
		node = node.Next            // 把 节点.Next 写入 节点
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   [][]int // in [][]int
		want []int   // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[][]int{{1, 4, 5}, {1, 3, 4}, {2, 6}}, []int{1, 1, 2, 3, 4, 4, 5, 6}},
		{[][]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		lists := []*ListNode{}   // 把 [] 乘 ListNode{} 写入 lists :
		for _, a := range c.in { // 同时取 _ 与 数组 遍历
			lists = append(lists, build(a)) // 把 append(lists, build(数组)) 写入 lists
		}
		got := toList(merge_k_lists(lists))  // 把 toList(merge_k_lists(lists)) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%v want=%v\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
