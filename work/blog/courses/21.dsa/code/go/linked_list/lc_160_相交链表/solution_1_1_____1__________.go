// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145095015
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

func getIntersectionNode(headA, headB *ListNode) *ListNode { // 定义函数/方法 getIntersectionNode
	visited := map[*ListNode]bool{} // 把 映射表[ 乘 ListNode]bool{} 写入 visited :
	temp := headA                   // 把 链表 A 写入 temp :
	for temp != nil {               // 把 nil { 写入 for temp !
		visited[temp] = true // 把 true 写入 visited[temp]
		temp = temp.Next     // 把 临时变量.Next 写入 临时变量
	}
	temp = headB      // 把 链表 B 写入 临时变量
	for temp != nil { // 把 nil { 写入 for temp !
		if visited[temp] { // 若 已访问集合[临时变量]
			return temp // 返回 临时变量
		}
		temp = temp.Next // 把 临时变量.Next 写入 临时变量
	}
	return nil // 返回 nil
}

func main() { // 程序入口：跑内嵌自测用例
	if getIntersectionNode(nil, nil) != nil { // 若 getIntersectionNode(nil, nil) 不等于 nil
		fmt.Println("FAIL nil case") // 打印输出
		os.Exit(1)                   // os.Exit(1)
	}
	tail := buildList([]int{8, 4, 5}) // 把 buildList([]int{8, 4, 5}) 写入 tail :
	a := &ListNode{Val: 4, Next: &ListNode{Val: 1, Next: tail}}
	b := &ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 1, Next: tail}}}
	got := getIntersectionNode(a, b) // 把 getIntersectionNode(数组, b) 写入 got :
	if got == nil || got.Val != 8 {  // 若 got 等于 nil 或 got.Val 不等于 8
		fmt.Printf("FAIL intersection got=%v\n", got) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
