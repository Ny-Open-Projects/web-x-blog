// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134358253
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func mergeTwoLists(list1, list2 *ListNode) *ListNode { // 定义函数/方法 mergeTwoLists
	res := &ListNode{}           // 把 按位与 ListNode{} 写入 res :
	p := res                     // 把 结果 写入 p :
	p1, p2 := list1, list2       // 把 list1, list2 写入 p1, p2 :
	for p1 != nil && p2 != nil { // 把 nil 且 p2 不等于 nil { 写入 for p1 !
		if p1.Val < p2.Val { // 若 p1.Val 小于 p2.Val
			p.Next = p1  // 把 p1 写入 p.Next
			p1 = p1.Next // 把 p1.Next 写入 p1
		} else { // 否则
			p.Next = p2  // 把 p2 写入 p.Next
			p2 = p2.Next // 把 p2.Next 写入 p2
		}
		p = p.Next // 把 节点.Next 写入 节点
	}
	if p1 != nil { // 若 p1 不等于 nil
		p.Next = p1 // 把 p1 写入 p.Next
	} else { // 否则
		p.Next = p2 // 把 p2 写入 p.Next
	}
	return res.Next // 返回 结果.Next
}

func build(vals []int) *ListNode { // 定义函数/方法 build
	dummy := &ListNode{}     // 把 按位与 ListNode{} 写入 dummy :
	p := dummy               // 把 哨兵节点 写入 p :
	for _, v := range vals { // 同时取 _ 与 值 遍历
		p.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 p.Next
		p = p.Next                 // 把 节点.Next 写入 节点
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func toList(n *ListNode) []int { // 定义函数/方法 toList
	out := []int{} // 把 []int{} 写入 out :
	for n != nil { // 把 nil { 写入 for n !
		out = append(out, n.Val) // 把 append(out, 元素个数.Val) 写入 out
		n = n.Next               // 把 元素个数.Next 写入 元素个数
	}
	return out // 返回 out
}

func main() { // 程序入口：跑内嵌自测用例
	want := []int{1, 1, 2, 3, 4, 4} // 把 []int{1, 1, 2, 3, 4, 4} 写入 want :
	got := toList(mergeTwoLists(build([]int{1, 2, 4}), build([]int{1, 3, 4})))
	if !reflect.DeepEqual(got, want) { // 若 取反 reflect.DeepEqual(got, want
		fmt.Println("FAIL", got) // 打印输出
		return                   // return
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
