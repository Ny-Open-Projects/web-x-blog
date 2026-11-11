// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package main // 引入依赖
import (
	"container/heap" // 引入依赖
	"fmt"
	"os"
	"reflect"
)

type ListNode struct {
	Val  int
	Next *ListNode
} // 定义类型
func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}
	p := dummy // 把 按位与 ListNode{}; 节点 : 赋值为 哨兵节点 写入 dummy :
	for _, v := range vals {
		p.Next = &ListNode{Val: v}
		p = p.Next
	} // 同时取 _ 与 值 遍历
	return dummy.Next // 返回 哨兵节点.Next
}
func toArr(head *ListNode) []int { // 定义函数/方法 toArr
	res := []int{} // 把 []int{} 写入 res :
	for head != nil {
		res = append(res, head.Val)
		head = head.Next
	}
	return res // 返回 结果
}

type Item struct {
	node *ListNode
	idx  int
}                                     // 定义类型
type MinHeap []Item                   // 定义类型
func (h MinHeap) Len() int            { return len(h) }                        // 定义函数/方法 Len
func (h MinHeap) Less(i, j int) bool  { return h[i].node.Val < h[j].node.Val } // 定义函数/方法 Less
func (h MinHeap) Swap(i, j int)       { h[i], h[j] = h[j], h[i] }              // 定义函数/方法 Swap
func (h *MinHeap) Push(x interface{}) { *h = append(*h, x.(Item)) }            // 定义函数/方法 Push
func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
} // 定义函数/方法 Pop
func mergeKLists(lists []*ListNode) *ListNode { // 定义函数/方法 mergeKLists
	h := &MinHeap{}
	heap.Init(h) // 把 按位与 MinHeap{}; 堆.Init(h) 写入 h :
	for i, l := range lists {
		if l != nil {
			heap.Push(h, Item{node: l, idx: i})
		}
	} // 同时取 下标 i 与 左指针 遍历
	dummy := &ListNode{}
	p := dummy        // 把 按位与 ListNode{}; 节点 : 赋值为 哨兵节点 写入 dummy :
	for h.Len() > 0 { // for h.Len() 超过 0 {
		it := heap.Pop(h).(Item)
		p.Next = it.node
		p = p.Next // 把 堆.Pop(h).(Item); 节点.Next 赋值为 it.节点; 节点 赋值为 节点.Next 写入 it :
		if it.node.Next != nil {
			heap.Push(h, Item{node: it.node.Next, idx: it.idx})
		}
	}
	return dummy.Next // 返回 哨兵节点.Next
}
func main() { // 程序入口：跑内嵌自测用例
	cases := []struct {
		in   [][]int
		want []int
	}{ // 把 []struct{ in [][]int; want []int }{ 写入 cases :
		{[][]int{{1, 4, 5}, {1, 3, 4}, {2, 6}}, []int{1, 1, 2, 3, 4, 4, 5, 6}},
		{[][]int{{}}, []int{}},
		{[][]int{{1}}, []int{1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		lists := make([]*ListNode, len(c.in)) // 把 make([] 乘 ListNode, 长度(字符.in)) 写入 lists :
		for i := range c.in {
			lists[i] = buildList(c.in[i])
		}
		got := toArr(mergeKLists(lists)) // 把 toArr(mergeKLists(lists)) 写入 got :
		if !reflect.DeepEqual(got, c.want) {
			ok = false
			fmt.Printf("FAIL %v\n", got)
		}
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
