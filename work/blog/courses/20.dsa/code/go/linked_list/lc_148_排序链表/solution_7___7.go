// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130536355
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func sortList(head *ListNode) *ListNode { // 定义函数/方法 sortList
	if head == nil || head.Next == nil { // 若 头节点 等于 nil 或 头节点.Next 等于 nil
		return head // 返回 头节点
	}
	slow, fast := head, head.Next         // 把 头节点, 头节点.Next 写入 slow, fast :
	for fast != nil && fast.Next != nil { // 把 nil 且 快指针.Next 不等于 nil { 写入 for fast !
		slow = slow.Next      // 把 慢指针.Next 写入 慢指针
		fast = fast.Next.Next // 把 快指针.Next.Next 写入 快指针
	}
	mid := slow.Next                  // 把 慢指针.Next 写入 mid :
	slow.Next = nil                   // 把 nil 写入 slow.Next
	left := sortList(head)            // 把 sortList(头节点) 写入 left :
	right := sortList(mid)            // 把 sortList(中点) 写入 right :
	dummy := &ListNode{}              // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy                     // 把 哨兵节点 写入 curr :
	for left != nil && right != nil { // 把 nil 且 右边界 不等于 nil { 写入 for left !
		if left.Val <= right.Val { // 若 左边界.Val 不超过 右边界.Val
			curr.Next = left // 把 左边界 写入 curr.Next
			left = left.Next // 把 左边界.Next 写入 左边界
		} else { // 否则
			curr.Next = right  // 把 右边界 写入 curr.Next
			right = right.Next // 把 右边界.Next 写入 右边界
		}
		curr = curr.Next // 把 当前值.Next 写入 当前值
	}
	if left != nil { // 若 左边界 不等于 nil
		curr.Next = left // 把 左边界 写入 curr.Next
	} else { // 否则
		curr.Next = right // 把 右边界 写入 curr.Next
	}
	return dummy.Next // 返回 哨兵节点.Next
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

func toList(head *ListNode) []int { // 定义函数/方法 toList
	res := []int{}    // 把 []int{} 写入 res :
	for head != nil { // 把 nil { 写入 for head !
		res = append(res, head.Val) // 把 append(结果, 头节点.Val) 写入 结果
		head = head.Next            // 把 头节点.Next 写入 头节点
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   []int // in []int
		want []int // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[]int{4, 2, 1, 3}, []int{1, 2, 3, 4}},
		{nil, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		got := toList(sortList(buildList(c.in))) // 把 toList(sortList(buildList(字符.in))) 写入 got :
		if !reflect.DeepEqual(got, c.want) {     // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%v want=%v\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
