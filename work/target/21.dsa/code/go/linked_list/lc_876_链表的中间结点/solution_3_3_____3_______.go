// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145096505
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func build(vals []int) *ListNode { // 定义函数/方法 build
	dummy := &ListNode{Val: 0} // 把 按位与 ListNode{Val: 0} 写入 dummy :
	p := dummy                 // 把 哨兵节点 写入 p :
	for _, v := range vals {   // 同时取 _ 与 值 遍历
		p.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 p.Next
		p = p.Next                 // 把 节点.Next 写入 节点
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func middleNode(head *ListNode) *ListNode { // 定义函数/方法 middleNode
	if head == nil { // 若 头节点 等于 nil
		return nil // 返回 nil
	}
	slow := head                          // 把 头节点 写入 slow :
	fast := head                          // 把 头节点 写入 fast :
	for fast != nil && fast.Next != nil { // 把 nil 且 快指针.Next 不等于 nil { 写入 for fast !
		slow = slow.Next      // 把 慢指针.Next 写入 慢指针
		fast = fast.Next.Next // 把 快指针.Next.Next 写入 快指针
	}
	return slow // 返回 慢指针
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		in      []int // in []int
		want    int   // want int
		wantNil bool  // wantNil bool
	}{ // }{
		{[]int{1, 2, 3, 4, 5}, 3, false},
		{[]int{1, 2, 3, 4, 5, 6}, 4, false},
		{nil, 0, true},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := middleNode(build(c.in)) // 把 middleNode(build(字符.in)) 写入 got :
		if c.wantNil {                 // 若 字符.wantNil
			if got != nil { // 若 got 不等于 nil
				ok = false                                                 // 把 false 写入 ok
				fmt.Printf("FAIL middleNode(%v)=%v want nil\n", c.in, got) // 打印输出
			}
		} else { // 否则
			if got == nil || got.Val != c.want { // 若 got 等于 nil 或 got.Val 不等于 字符.want
				ok = false                                                        // 把 false 写入 ok
				fmt.Printf("FAIL middleNode(%v)=%v want %d\n", c.in, got, c.want) // 打印输出
			}
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
