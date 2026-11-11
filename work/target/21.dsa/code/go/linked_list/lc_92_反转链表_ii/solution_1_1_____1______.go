// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094075
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"os"      // 「os」
	"reflect" // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy            // 把 哨兵节点 写入 curr :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		curr.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 curr.Next
		curr = curr.Next              // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func listToSlice(head *ListNode) []int { // 定义函数/方法 listToSlice
	var out []int     // var out []int
	for head != nil { // 把 nil { 写入 for head !
		out = append(out, head.Val) // 把 append(out, 头节点.Val) 写入 out
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return out // 返回 out
}

func reverseLinkedList(head *ListNode) *ListNode { // 定义函数/方法 reverseLinkedList
	var prev *ListNode // var 前一个 乘 ListNode
	curr := head       // 把 头节点 写入 curr :
	for curr != nil {  // 把 nil { 写入 for curr !
		nxt := curr.Next // 把 当前值.Next 写入 nxt :
		curr.Next = prev // 把 前一个 写入 curr.Next
		prev = curr      // 把 当前值 写入 前一个
		curr = nxt       // 把 nxt 写入 当前值
	}
	return prev // 返回 前一个
}

// reverseBetween 忠实翻译 Python 参考（反转 [left, right] 区间）
func reverseBetween(head *ListNode, left, right int) *ListNode { // 定义函数/方法 reverseBetween
	if left >= right { // 若 左边界 不低于 右边界
		return head // 返回 头节点
	}
	dummy := &ListNode{Val: -1}   // 把 按位与 ListNode{Val: 减 1} 写入 dummy :
	dummy.Next = head             // 把 头节点 写入 dummy.Next
	pre := dummy                  // 把 哨兵节点 写入 pre :
	for i := 0; i < left-1; i++ { // 让 下标 i 从 0 开始计数
		pre = pre.Next // 把 前缀和.Next 写入 前缀和
	}
	leftNode := pre.Next              // 把 前缀和.Next 写入 leftNode :
	rightNode := pre                  // 把 前缀和 写入 rightNode :
	for i := 0; i < right-left; i++ { // 让 下标 i 从 0 开始计数
		rightNode = rightNode.Next // 把 rightNode.Next 写入 rightNode
	}
	curr := rightNode.Next      // 把 rightNode.Next 写入 curr :
	pre.Next = nil              // 把 nil 写入 pre.Next
	rightNode.Next = nil        // 把 nil 写入 rightNode.Next
	reverseLinkedList(leftNode) // reverseLinkedList(leftNode)
	pre.Next = rightNode        // 把 rightNode 写入 pre.Next
	leftNode.Next = curr        // 把 当前值 写入 leftNode.Next
	return dummy.Next           // 返回 哨兵节点.Next
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		l, r int   // 左指针, 右指针 int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3, 4, 5}, 2, 4, []int{1, 3, 2, 4, 5}},
		{[]int{1, 2, 3, 4, 5}, 1, 3, []int{2, 1, 3, 4, 5}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := listToSlice(reverseBetween(buildList(c.in), c.l, c.r))
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                                            // 把 false 写入 ok
			fmt.Printf("FAIL reverseBetween(%v,%d,%d)=%v want %v\n", c.in, c.l, c.r, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
