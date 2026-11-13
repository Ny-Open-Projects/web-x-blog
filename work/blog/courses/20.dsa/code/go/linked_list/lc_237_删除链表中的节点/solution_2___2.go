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

func deleteNode(node *ListNode) { // 定义函数/方法 deleteNode
	node.Val = node.Next.Val   // 把 节点.Next.Val 写入 node.Val
	node.Next = node.Next.Next // 把 节点.Next.Next 写入 node.Next
}

func main() { // 程序入口：跑内嵌自测用例
	head := buildList([]int{4, 5, 1, 9}) // 把 buildList([]int{4, 5, 1, 9}) 写入 head :
	target := head.Next.Next             // value 1
	deleteNode(target)                   // deleteNode(目标值)
	if got := listToSlice(head); !reflect.DeepEqual(got, []int{4, 5, 9}) {
		fmt.Printf("FAIL deleteNode=%v want [4 5 9]\n", got) // 打印输出
		os.Exit(1)                                           // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
