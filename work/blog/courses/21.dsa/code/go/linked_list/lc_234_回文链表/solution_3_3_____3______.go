// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096059
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

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

func reverseList(node *ListNode) *ListNode { // 定义函数/方法 reverseList
	var prev *ListNode // var 前一个 乘 ListNode
	curr := node       // 把 节点 写入 curr :
	for curr != nil {  // 把 nil { 写入 for curr !
		nxt := curr.Next // 把 当前值.Next 写入 nxt :
		curr.Next = prev // 把 前一个 写入 curr.Next
		prev = curr      // 把 当前值 写入 前一个
		curr = nxt       // 把 nxt 写入 当前值
	}
	return prev // 返回 前一个
}

func endOfFirstHalf(node *ListNode) *ListNode { // 定义函数/方法 endOfFirstHalf
	fast := node                                    // 把 节点 写入 fast :
	slow := node                                    // 把 节点 写入 slow :
	for fast.Next != nil && fast.Next.Next != nil { // 把 nil 且 快指针.Next.Next 不等于 nil { 写入 for fast.Next !
		fast = fast.Next.Next // 把 快指针.Next.Next 写入 快指针
		slow = slow.Next      // 把 慢指针.Next 写入 慢指针
	}
	return slow // 返回 慢指针
}

func isPalindrome(head *ListNode) bool { // 定义判定函数 isPalindrome
	if head == nil { // 若 头节点 等于 nil
		return true // 返回 true
	}
	firstHalfEnd := endOfFirstHalf(head)              // 把 endOfFirstHalf(头节点) 写入 firstHalfEnd :
	secondHalfStart := reverseList(firstHalfEnd.Next) // 把 reverseList(firstHalfEnd.Next) 写入 secondHalfStart :
	p1, p2 := head, secondHalfStart                   // 把 头节点, secondHalfStart 写入 p1, p2 :
	result := true                                    // 把 true 写入 result :
	for p2 != nil && result {                         // 把 nil 且 结果 { 写入 for p2 !
		if p1.Val != p2.Val { // 若 p1.Val 不等于 p2.Val
			result = false // 把 false 写入 结果
		}
		p1 = p1.Next // 把 p1.Next 写入 p1
		p2 = p2.Next // 把 p2.Next 写入 p2
	}
	firstHalfEnd.Next = reverseList(secondHalfStart) // 把 reverseList(secondHalfStart) 写入 firstHalfEnd.Next
	return result                                    // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want bool  // want bool
	}{ // }{
		{[]int{1, 2, 2, 1}, true},
		{nil, true},
		{[]int{1, 2}, false},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		if got := isPalindrome(buildList(c.in)); got != c.want { // 若 got : 赋值为 isPalindrome(buildList(字符.in)); got 不等于 字符.want
			ok = false                                                          // 把 false 写入 ok
			fmt.Printf("FAIL isPalindrome(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
