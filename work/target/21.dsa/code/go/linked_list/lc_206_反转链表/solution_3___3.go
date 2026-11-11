// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130510175
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

// reverseList 递归反转链表（忠实翻译 Python 参考）
func reverseList(head *ListNode) *ListNode { // 定义函数/方法 reverseList
	if head == nil || head.Next == nil { // 若 头节点 等于 nil 或 头节点.Next 等于 nil
		return head // 返回 头节点
	}
	newHead := reverseList(head.Next) // 把 reverseList(头节点.Next) 写入 newHead :
	head.Next.Next = head             // 把 头节点 写入 head.Next.Next
	head.Next = nil                   // 把 nil 写入 head.Next
	return newHead                    // 返回 newHead
}

func fromSlice(vals []int) *ListNode { // 定义函数/方法 fromSlice
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

func toSlice(head *ListNode) []int { // 定义函数/方法 toSlice
	var res []int     // var 结果 []int
	for head != nil { // 把 nil { 写入 for head !
		res = append(res, head.Val) // 把 append(结果, 头节点.Val) 写入 结果
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in   []int // in []int
		want []int // want []int
	}{ // }{
		{nil, nil},
		{[]int{1, 2, 3}, []int{3, 2, 1}},
		{[]int{1}, []int{1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toSlice(reverseList(fromSlice(c.in))) // 把 toSlice(reverseList(fromSlice(字符.in))) 写入 got :
		if !reflect.DeepEqual(got, c.want) {         // 若 取反 reflect.DeepEqual(got, 字符.want
			fmt.Printf("FAIL in=%v got=%v want=%v\n", c.in, got, c.want) // 打印输出
			ok = false                                                   // 把 false 写入 ok
		}
	}
	// 忠实复刻 __main__: print(reverseList(None)) -> None
	if reverseList(nil) != nil { // 若 reverseList(nil) 不等于 nil
		fmt.Println("FAIL reverseList(nil) should be nil") // 打印输出
		ok = false                                         // 把 false 写入 ok
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
