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

func mergeKLists(lists []*ListNode) *ListNode { // 定义函数/方法 mergeKLists
	return merge(lists, 0, len(lists)-1) // 定义函数/方法 merge
}

func merge(lists []*ListNode, l, r int) *ListNode { // 定义函数/方法 merge
	if l == r { // 若 左指针 等于 右指针
		return lists[l] // 返回 lists[左指针]
	}
	if l > r { // 若 左指针 超过 右指针
		return nil // 返回 nil
	}
	mid := (l + r) / 2                                                 // 把 (左指针 加 右指针) 除以 2 写入 mid :
	return mergeTwoLists(merge(lists, l, mid), merge(lists, mid+1, r)) // 定义函数/方法 mergeTwoLists
}

func mergeTwoLists(a, b *ListNode) *ListNode { // 定义函数/方法 mergeTwoLists
	if a == nil { // 若 数组 等于 nil
		return b // 返回 b
	}
	if b == nil { // 若 b 等于 nil
		return a // 返回 数组
	}
	head := &ListNode{}              // 把 按位与 ListNode{} 写入 head :
	tail := head                     // 把 头节点 写入 tail :
	aPtr := a                        // 把 数组 写入 aPtr :
	bPtr := b                        // 把 b 写入 bPtr :
	for aPtr != nil && bPtr != nil { // 把 nil 且 bPtr 不等于 nil { 写入 for aPtr !
		if aPtr.Val < bPtr.Val { // 若 aPtr.Val 小于 bPtr.Val
			tail.Next = aPtr // 把 aPtr 写入 tail.Next
			aPtr = aPtr.Next // 把 aPtr.Next 写入 aPtr
		} else { // 否则
			tail.Next = bPtr // 把 bPtr 写入 tail.Next
			bPtr = bPtr.Next // 把 bPtr.Next 写入 bPtr
		}
		tail = tail.Next // 把 尾节点.Next 写入 尾节点
	}
	if aPtr != nil { // 若 aPtr 不等于 nil
		tail.Next = aPtr // 把 aPtr 写入 tail.Next
	} else { // 否则
		tail.Next = bPtr // 把 bPtr 写入 tail.Next
	}
	return head.Next // 返回 头节点.Next
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
		got := toList(mergeKLists(lists))    // 把 toList(mergeKLists(lists)) 写入 got :
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
