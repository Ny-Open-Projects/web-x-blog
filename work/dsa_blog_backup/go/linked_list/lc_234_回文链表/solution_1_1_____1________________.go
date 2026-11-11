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

func isPalindrome(head *ListNode) bool { // 定义判定函数 isPalindrome
	vals := []int{}   // 把 []int{} 写入 vals :
	for head != nil { // 把 nil { 写入 for head !
		vals = append(vals, head.Val) // 把 append(vals, 头节点.Val) 写入 vals
		head = head.Next              // 把 头节点.Next 写入 头节点
	}
	left, right := 0, len(vals)-1 // 把 0, 长度(vals) 减 1 写入 left, right :
	for left < right {            // for 左边界 小于 右边界 {
		if vals[left] != vals[right] { // 若 vals[左边界] 不等于 vals[右边界]
			return false // 返回 false
		}
		left++  // 左边界 加一
		right-- // 右边界 减一
	}
	return true // 返回 true
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
