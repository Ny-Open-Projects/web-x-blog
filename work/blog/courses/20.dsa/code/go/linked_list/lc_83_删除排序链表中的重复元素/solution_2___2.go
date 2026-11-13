// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513986
package main // 引入依赖

import (
	"fmt"
	"os"
	"reflect"
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

func listToSlice(head *ListNode) []int { // 定义函数/方法 listToSlice
	var out []int     // var out []int
	for head != nil { // 把 nil { 写入 for head !
		out = append(out, head.Val) // 把 append(out, 头节点.Val) 写入 out
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return out // 返回 out
}

func deleteDuplicates(head *ListNode) *ListNode { // 定义函数/方法 deleteDuplicates
	curr := head      // 把 头节点 写入 curr :
	for curr != nil { // 把 nil { 写入 for curr !
		for curr.Next != nil && curr.Val == curr.Next.Val { // 把 nil 且 当前值.Val 等于 当前值.Next.Val { 写入 for curr.Next !
			curr.Next = curr.Next.Next // 把 当前值.Next.Next 写入 curr.Next
		}
		curr = curr.Next // 把 当前值.Next 写入 当前值
	}
	return head // 返回 头节点
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{[]int{1, 1, 2, 3, 3}, []int{1, 2, 3}},
		{[]int{1, 1, 1}, []int{1}},
		{nil, nil},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := listToSlice(deleteDuplicates(buildList(c.in))) // 把 listToSlice(deleteDuplicates(buildList(字符.in))) 写入 got :
		if !reflect.DeepEqual(got, c.want) {                  // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                              // 把 false 写入 ok
			fmt.Printf("FAIL deleteDuplicates(%v)=%v want %v\n", c.in, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
