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
	lists = filterNil(lists) // 把 filterNil(lists) 写入 lists
	if len(lists) == 0 {     // 若 长度(lists) 等于 0
		return nil // 返回 nil
	}
	for len(lists) > 1 { // for 长度(lists) 超过 1 {
		merged := []*ListNode{}              // 把 [] 乘 ListNode{} 写入 merged :
		for i := 0; i < len(lists); i += 2 { // 让 下标 i 从 0 开始计数
			a := lists[i]         // 把 lists[下标 i] 写入 a :
			var b *ListNode       // var b 乘 ListNode
			if i+1 < len(lists) { // 若 下标 i 加 1 小于 长度(lists
				b = lists[i+1] // 把 lists[下标 i 加 1] 写入 b
			}
			merged = append(merged, merge_two(a, b)) // 把 append(merged, merge_two(数组, b)) 写入 merged
		}
		lists = merged // 把 merged 写入 lists
	}
	return lists[0] // 返回 lists[0]
}

func filterNil(lists []*ListNode) []*ListNode { // 定义函数/方法 filterNil
	out := []*ListNode{}      // 把 [] 乘 ListNode{} 写入 out :
	for _, l := range lists { // 同时取 _ 与 左指针 遍历
		if l != nil { // 若 左指针 不等于 nil
			out = append(out, l) // 把 append(out, 左指针) 写入 out
		}
	}
	return out // 返回 out
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
