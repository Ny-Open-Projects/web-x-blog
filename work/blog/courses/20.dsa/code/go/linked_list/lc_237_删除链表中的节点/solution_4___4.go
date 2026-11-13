// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130508569
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

func deleteNode(node *ListNode) { // 定义函数/方法 deleteNode
	curr := node                          // 把 节点 写入 curr :
	for curr != nil && curr.Next != nil { // 把 nil 且 当前值.Next 不等于 nil { 写入 for curr !
		curr.Val = curr.Next.Val   // 把 当前值.Next.Val 写入 curr.Val
		if curr.Next.Next == nil { // 若 当前值.Next.Next 等于 nil
			curr.Next = nil // 把 nil 写入 curr.Next
			break           // 跳出循环
		}
		curr = curr.Next // 把 当前值.Next 写入 当前值
	}
}

func main() { // 程序入口：跑内嵌自测用例
	deleteNode(nil)                      // must not panic
	head := buildList([]int{4, 5, 1, 9}) // 把 buildList([]int{4, 5, 1, 9}) 写入 head :
	n := head                            // delete head (value 4)
	deleteNode(n)                        // deleteNode(元素个数)
	if got := listToSlice(head); !reflect.DeepEqual(got, []int{5, 1, 9}) {
		fmt.Printf("FAIL deleteNode=%v want [5 1 9]\n", got) // 打印输出
		os.Exit(1)                                           // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
