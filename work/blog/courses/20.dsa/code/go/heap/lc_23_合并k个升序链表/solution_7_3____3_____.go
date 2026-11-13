// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
package main // 引入依赖

import (
	"fmt"     // 「fmt」
	"reflect" // 「reflect」
)

type ListNode struct { // 定义类型
	Val  int       // Val int
	Next *ListNode // Next 乘 ListNode
}

func merge_two(a, b *ListNode) *ListNode { // 定义函数/方法 merge_two
	dummy := &ListNode{}       // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy              // 把 哨兵节点 写入 curr :
	for a != nil && b != nil { // 把 nil 且 b 不等于 nil { 写入 for a !
		if a.Val <= b.Val { // 若 数组.Val 不超过 b.Val
			curr.Next = a // 把 数组 写入 curr.Next
			a = a.Next    // 把 数组.Next 写入 数组
		} else { // 否则
			curr.Next = b // 把 b 写入 curr.Next
			b = b.Next    // 把 b.Next 写入 b
		}
		curr = curr.Next // 把 当前值.Next 写入 当前值
	}
	if a != nil { // 若 数组 不等于 nil
		curr.Next = a // 把 数组 写入 curr.Next
	} else { // 否则
		curr.Next = b // 把 b 写入 curr.Next
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func merge_k_lists(lists []*ListNode) *ListNode { // 定义函数/方法 merge_k_lists
	if len(lists) == 0 { // 若 长度(lists) 等于 0
		return nil // 返回 nil
	}
	var divide func(lo, hi int) *ListNode // var divide func(左边界, 右边界 int) 乘 ListNode
	divide = func(lo, hi int) *ListNode { // 把 func(左边界, 右边界 int) 乘 ListNode { 写入 divide
		if lo == hi { // 若 左边界 等于 右边界
			return lists[lo] // 返回 lists[左边界]
		}
		mid := (lo + hi) / 2          // 把 (左边界 加 右边界) 除以 2 写入 mid :
		left := divide(lo, mid)       // 把 divide(左边界, 中点) 写入 left :
		right := divide(mid+1, hi)    // 把 divide(中点 加 1, 右边界) 写入 right :
		return merge_two(left, right) // 定义函数/方法 merge_two
	}
	return divide(0, len(lists)-1) // 定义函数/方法 divide
}

func build(arr []int) *ListNode { // 定义函数/方法 build
	dummy := &ListNode{}    // 把 按位与 ListNode{} 写入 dummy :
	curr := dummy           // 把 哨兵节点 写入 curr :
	for _, v := range arr { // 同时取 _ 与 值 遍历
		curr.Next = &ListNode{Val: v} // 把 按位与 ListNode{Val: 值} 写入 curr.Next
		curr = curr.Next              // 把 当前值.Next 写入 当前值
	}
	return dummy.Next // 返回 哨兵节点.Next
}

func toList(node *ListNode) []int { // 定义函数/方法 toList
	res := []int{}    // 把 []int{} 写入 res :
	for node != nil { // 把 nil { 写入 for node !
		res = append(res, node.Val) // 把 append(结果, 节点.Val) 写入 结果
		node = node.Next            // 把 节点.Next 写入 节点
	}
	return res // 返回 结果
}

func main() { // 程序入口：跑内嵌自测用例
	type tc struct { // 定义类型
		in   [][]int // in [][]int
		want []int   // want []int
	}
	cases := []tc{ // 把 []tc{ 写入 cases :
		{[][]int{{1, 4, 5}, {1, 3, 4}, {2, 6}}, []int{1, 1, 2, 3, 4, 4, 5, 6}},
		{[][]int{}, []int{}},
	}
	ok := true                // 把 true 写入 ok :
	for _, c := range cases { // 同时取 _ 与 字符 遍历
		lists := []*ListNode{}   // 把 [] 乘 ListNode{} 写入 lists :
		for _, a := range c.in { // 同时取 _ 与 数组 遍历
			lists = append(lists, build(a)) // 把 append(lists, build(数组)) 写入 lists
		}
		got := toList(merge_k_lists(lists))  // 把 toList(merge_k_lists(lists)) 写入 got :
		if !reflect.DeepEqual(got, c.want) { // 若 取反 reflect.DeepEqual(got, 字符.want
			ok = false                                       // 把 false 写入 ok
			fmt.Printf("FAIL got=%v want=%v\n", got, c.want) // 打印输出
		}
	}
	if !ok { // 若 取反 ok
		panic("FAILED") // panic(「FAILED」)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
