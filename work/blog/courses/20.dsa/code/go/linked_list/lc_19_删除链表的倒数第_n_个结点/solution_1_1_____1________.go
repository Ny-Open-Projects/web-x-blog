// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145093774
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
	var head, tail *ListNode // var 头节点, 尾节点 乘 ListNode
	for _, v := range vals { // 同时取 _ 与 值 遍历
		n := &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 n :
		if head == nil {       // 若 头节点 等于 nil
			head = n // 把 元素个数 写入 头节点
			tail = n // 把 元素个数 写入 尾节点
		} else { // 否则
			tail.Next = n // 把 元素个数 写入 tail.Next
			tail = n      // 把 元素个数 写入 尾节点
		}
	}
	return head // 返回 头节点
}

func listToSlice(head *ListNode) []int { // 定义函数/方法 listToSlice
	var out []int     // var out []int
	for head != nil { // 把 nil { 写入 for head !
		out = append(out, head.Val) // 把 append(out, 头节点.Val) 写入 out
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return out // 返回 out
}

func removeNthFromEnd(head *ListNode, n int) *ListNode { // 定义函数/方法 removeNthFromEnd
	dummy := &ListNode{Next: head} // 把 按位与 ListNode{Next: 头节点} 写入 dummy :
	length := 0                    // 把 0 写入 length :
	curr := head                   // 把 头节点 写入 curr :
	for curr != nil {              // 把 nil { 写入 for curr !
		length++         // 长度 加一
		curr = curr.Next // 把 当前值.Next 写入 当前值
	}
	step := length - n          // 把 长度 减 元素个数 写入 step :
	curr = dummy                // 把 哨兵节点 写入 当前值
	for i := 0; i < step; i++ { // 让 下标 i 从 0 开始计数
		curr = curr.Next // 把 当前值.Next 写入 当前值
	}
	curr.Next = curr.Next.Next // 把 当前值.Next.Next 写入 curr.Next
	return dummy.Next          // 返回 哨兵节点.Next
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		n    int   // 元素个数 int
		want []int // want []int
	}{ // }{
		{[]int{1, 2, 3, 4, 5}, 2, []int{1, 2, 3, 5}},
		{[]int{1}, 1, nil},
		{[]int{1, 2}, 1, []int{1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := listToSlice(removeNthFromEnd(buildList(c.in), c.n))
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                                      // 把 false 写入 ok
			fmt.Printf("FAIL removeNthFromEnd(%v,%d)=%v want %v\n", c.in, c.n, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
