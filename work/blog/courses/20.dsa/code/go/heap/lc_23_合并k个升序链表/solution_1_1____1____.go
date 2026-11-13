// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

type MinHeap struct { // 定义类型
	heap []*ListNode // 堆 [] 乘 ListNode
}

func NewMinHeap() *MinHeap { // 定义函数/方法 NewMinHeap
	return &MinHeap{heap: []*ListNode{}} // 返回 按位与 MinHeap{堆: [] 乘 ListNode{}}
}

func (h *MinHeap) Push(node *ListNode) { // 定义函数/方法 Push
	h.heap = append(h.heap, node) // 把 append(h.堆, 节点) 写入 堆
	h.shiftUp(len(h.heap) - 1)    // h.shiftUp(长度(h.堆) 减 1)
}

func (h *MinHeap) Pop() *ListNode { // 定义函数/方法 Pop
	if len(h.heap) == 0 { // 若 长度(h.堆) 等于 0
		return nil // 返回 nil
	}
	res := h.heap[0]                // 把 h.堆[0] 写入 res :
	last := h.heap[len(h.heap)-1]   // 把 h.堆[长度(h.堆) 减 1] 写入 last :
	h.heap = h.heap[:len(h.heap)-1] // 把 h.堆[:长度(h.堆) 减 1] 写入 堆
	if len(h.heap) > 0 {            // 若 长度(h.堆) 超过 0
		h.heap[0] = last // 把 last 写入 h.heap[0]
		h.shiftDown(0)   // h.shiftDown(0)
	}
	return res // 返回 结果
}

func (h *MinHeap) Size() int { return len(h.heap) } // 定义函数/方法 Size

func (h *MinHeap) shiftUp(i int) { // 定义函数/方法 shiftUp
	for i > 0 { // for 下标 i 超过 0 {
		parent := (i - 1) >> 1                  // 把 (下标 i 减 1) 超过 超过 1 写入 parent :
		if h.heap[parent].Val > h.heap[i].Val { // 若 h.堆[parent].Val 超过 h.堆[下标 i].Val
			h.heap[parent], h.heap[i] = h.heap[i], h.heap[parent] // 把 h.堆[下标 i], h.堆[parent] 写入 h.heap[parent], h.heap[i]
			i = parent                                            // 把 parent 写入 下标 i
		} else { // 否则
			break // 跳出循环
		}
	}
}

func (h *MinHeap) shiftDown(i int) { // 定义函数/方法 shiftDown
	size := len(h.heap) // 把 长度(h.堆) 写入 size :
	for {               // for {
		smallest := i                                               // 把 下标 i 写入 smallest :
		left := 2*i + 1                                             // 把 2 乘 下标 i 加 1 写入 left :
		right := 2*i + 2                                            // 把 2 乘 下标 i 加 2 写入 right :
		if left < size && h.heap[left].Val < h.heap[smallest].Val { // 若 左边界 小于 大小 且 h.堆[左边界].Val 小于 h.堆[smallest].Val
			smallest = left // 把 左边界 写入 smallest
		}
		if right < size && h.heap[right].Val < h.heap[smallest].Val { // 若 右边界 小于 大小 且 h.堆[右边界].Val 小于 h.堆[smallest].Val
			smallest = right // 把 右边界 写入 smallest
		}
		if smallest == i { // 若 smallest 等于 下标 i
			break // 跳出循环
		}
		h.heap[smallest], h.heap[i] = h.heap[i], h.heap[smallest] // 把 h.堆[下标 i], h.堆[smallest] 写入 h.heap[smallest], h.heap[i]
		i = smallest                                              // 把 smallest 写入 下标 i
	}
}

func mergeKLists(lists []*ListNode) *ListNode { // 定义函数/方法 mergeKLists
	h := NewMinHeap()            // 把 NewMinHeap() 写入 h :
	for _, node := range lists { // 同时取 _ 与 节点 遍历
		if node != nil { // 若 节点 不等于 nil
			h.Push(node) // h.Push(节点)
		}
	}
	dummy := &ListNode{} // 把 按位与 ListNode{} 写入 dummy :
	p := dummy           // 把 哨兵节点 写入 p :
	for h.Size() > 0 {   // for h.Size() 超过 0 {
		node := h.Pop()       // 把 h.Pop() 写入 node :
		p.Next = node         // 把 节点 写入 p.Next
		p = p.Next            // 把 节点.Next 写入 节点
		if node.Next != nil { // 若 节点.Next 不等于 nil
			h.Push(node.Next) // h.Push(节点.Next)
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
		got := toList(mergeKLists(lists))    // 把 toList(mergeKLists(lists)) 写入 got :
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
