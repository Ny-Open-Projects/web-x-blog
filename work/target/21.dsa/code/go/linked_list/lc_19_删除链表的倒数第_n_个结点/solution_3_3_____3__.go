// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145093774
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type ListNode struct {
	Val  int
	Next *ListNode
} // 定义类型

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	cur := dummy             // 把 哨兵节点 写入 cur :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		cur.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 cur.Next
		cur = cur.Next               // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func listToSlice(h *ListNode) []int { // 定义函数/方法 listToSlice
	var r []int    // var 右指针 []int
	for h != nil { // 把 nil { 写入 for h !
		r = append(r, h.Val) // 把 append(右指针, h.Val) 写入 右指针
		h = h.Next           // 把 h.Next 写入 h
	}
	return r // 返回 右指针
}

func removeNthFromEnd(head *ListNode, n int) *ListNode { // 定义函数/方法 removeNthFromEnd
	var nodes []*ListNode          // var nodes [] 乘 ListNode
	dummy := &ListNode{Next: head} // 把 按位与 ListNode{Next: 头节点} 写入 dummy :
	cur := dummy                   // 把 哨兵节点 写入 cur :
	for cur != nil {               // 把 nil { 写入 for cur !
		nodes = append(nodes, cur) // 把 append(nodes, 当前值) 写入 nodes
		cur = cur.Next             // 把 当前值.Next 写入 当前值
	}
	prev := nodes[len(nodes)-1-n] // 把 nodes[长度(nodes) 减 1 减 元素个数] 写入 prev :
	prev.Next = prev.Next.Next    // 把 前一个.Next.Next 写入 prev.Next
	return dummy.Next             // 返回 哨兵节点.Next
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		vals []int // vals []int
		n    int   // 元素个数 int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3, 4, 5}, 2, []int{1, 2, 3, 5}},
		{[]int{1}, 1, []int{}},
		{[]int{1, 2}, 2, []int{2}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := listToSlice(removeNthFromEnd(buildList(c.vals), c.n))
		if fmt.Sprint(got) != fmt.Sprint(c.want) { // 若 fmt.Sprint(got) 不等于 fmt.Sprint(字符.want
			ok = false                                                      // 把 false 写入 ok
			fmt.Printf("FAIL %v,%d=%v want %v\n", c.vals, c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
