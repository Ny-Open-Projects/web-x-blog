// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130513247
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type ListNode struct {
	Val  int
	Next *ListNode
} // 定义类型

func buildList(vals []int) *ListNode { // 定义函数/方法 buildList
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	cur := dummy             // 把 哨兵节点 写入 cur :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		cur.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 cur.Next
		cur = cur.Next               // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func listToSlice(h *ListNode) []int { // 定义函数/方法 listToSlice
	var r []int    // var 右指针 []int
	for h != nil { // 把 nil { 写入 for h !
		r = append(r, h.Val) // 把 append(右指针, h.Val) 写入 右指针
		h = h.Next           // 把 h.Next 写入 h
	}
	return r // 返回 右指针
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode { // 定义函数/方法 addTwoNumbers
	dummy := &ListNode{}                      // 把 按位与 ListNode{} 写入 dummy :
	cur := dummy                              // 把 哨兵节点 写入 cur :
	carry := 0                                // 把 0 写入 carry :
	for l1 != nil || l2 != nil || carry > 0 { // 把 nil 或 l2 不等于 nil 或 carry 超过 0 { 写入 for l1 !
		v1, v2 := 0, 0 // 把 0, 0 写入 v1, v2 :
		if l1 != nil { // 若 l1 不等于 nil
			v1 = l1.Val  // 把 l1.Val 写入 v1
			l1 = l1.Next // 把 l1.Next 写入 l1
		}
		if l2 != nil { // 若 l2 不等于 nil
			v2 = l2.Val  // 把 l2.Val 写入 v2
			l2 = l2.Next // 把 l2.Next 写入 l2
		}
		total := v1 + v2 + carry              // 把 v1 加 v2 加 carry 写入 total :
		carry = total / 10                    // 把 总和 除以 10 写入 carry
		cur.Next = &ListNode{Val: total % 10} // 把 按位与 ListNode{Val: 总和 对…取模 10} 写入 cur.Next
		cur = cur.Next                        // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func main() { // 程序入口：跑内嵌自测用例
	cases := []struct { // 把 []struct { 写入 cases :
		l1   []int // l1 []int
		l2   []int // l2 []int
		want []int // want []int
	}{ // }{
		{[]int{2, 4, 3}, []int{5, 6, 4}, []int{7, 0, 8}},
		{[]int{0}, []int{0}, []int{0}},
		{[]int{9, 9}, []int{1}, []int{0, 0, 1}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := listToSlice(addTwoNumbers(buildList(c.l1), buildList(c.l2)))
		if fmt.Sprint(got) != fmt.Sprint(c.want) { // 若 fmt.Sprint(got) 不等于 fmt.Sprint(字符.want
			ok = false                                                                    // 把 false 写入 ok
			fmt.Printf("FAIL addTwoNumbers(%v,%v)=%v want %v\n", c.l1, c.l2, got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
