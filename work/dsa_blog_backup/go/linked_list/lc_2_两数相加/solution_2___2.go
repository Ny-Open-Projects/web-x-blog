// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
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

func addTwoNumbers(l1, l2 *ListNode) *ListNode { // 定义函数/方法 addTwoNumbers
	if l1 == nil && l2 == nil { // 若 l1 等于 nil 且 l2 等于 nil
		return nil // 返回 nil
	}
	if l1 == nil { // 若 l1 等于 nil
		return l2 // 返回 l2
	}
	if l2 == nil { // 若 l2 等于 nil
		return l1 // 返回 l1
	}
	var head, tail *ListNode     // var 头节点, 尾节点 乘 ListNode
	carry := 0                   // 把 0 写入 carry :
	for l1 != nil || l2 != nil { // 把 nil 或 l2 不等于 nil { 写入 for l1 !
		v1, v2 := 0, 0 // 把 0, 0 写入 v1, v2 :
		if l1 != nil { // 若 l1 不等于 nil
			v1 = l1.Val // 把 l1.Val 写入 v1
		}
		if l2 != nil { // 若 l2 不等于 nil
			v2 = l2.Val // 把 l2.Val 写入 v2
		}
		total := v1 + v2 + carry           // 把 v1 加 v2 加 carry 写入 total :
		node := &ListNode{Val: total % 10} // 把 按位与 ListNode{Val: 总和 对…取模 10} 写入 node :
		carry = total / 10                 // 把 总和 除以 10 写入 carry
		if head == nil {                   // 若 头节点 等于 nil
			head = node // 把 节点 写入 头节点
			tail = node // 把 节点 写入 尾节点
		} else { // 否则
			tail.Next = node // 把 节点 写入 tail.Next
			tail = node      // 把 节点 写入 尾节点
		}
		if l1 != nil { // 若 l1 不等于 nil
			l1 = l1.Next // 把 l1.Next 写入 l1
		}
		if l2 != nil { // 若 l2 不等于 nil
			l2 = l2.Next // 把 l2.Next 写入 l2
		}
	}
	if carry != 0 { // 若 carry 不等于 0
		tail.Next = &ListNode{Val: carry} // 把 按位与 ListNode{Val: carry} 写入 tail.Next
	}
	return head // 返回 头节点
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		a, b []int // 数组, b []int
		want []int // want []int
	}{ // }{
		{[]int{2, 4, 3}, []int{5, 6, 4}, []int{7, 0, 8}},
		{[]int{5}, []int{5}, []int{0, 1}},
		{[]int{9, 9}, []int{1}, []int{0, 0, 1}},
		{nil, nil, nil},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := listToSlice(addTwoNumbers(buildList(c.a), buildList(c.b)))
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                                                  // 把 false 写入 ok
			fmt.Printf("FAIL addTwoNumbers(%v,%v)=%v want %v\n", c.a, c.b, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
