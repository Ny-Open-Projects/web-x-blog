// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133499836
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

func mergeTwoLists(a, b *ListNode) *ListNode { // 定义函数/方法 mergeTwoLists
	if a == nil { // 若 数组 等于 nil
		return b // 返回 b
	}
	if b == nil { // 若 b 等于 nil
		return a // 返回 数组
	}
	head := &ListNode{}              // 把 按位与 ListNode{} 写入 head :
	tail := head                     // 把 头节点 写入 tail :
	aPtr, bPtr := a, b               // 把 数组, b 写入 aPtr, bPtr :
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

func mergeKLists(lists []*ListNode) *ListNode { // 定义函数/方法 mergeKLists
	var ans *ListNode                 // var 答案 乘 ListNode
	for i := 0; i < len(lists); i++ { // 让 下标 i 从 0 开始计数
		ans = mergeTwoLists(ans, lists[i]) // 把 mergeTwoLists(答案, lists[下标 i]) 写入 答案
	}
	return ans // 返回 答案
}

func main() { // 程序入口：跑内嵌自测用例
	lists := []*ListNode{buildList([]int{1, 4, 5}), buildList([]int{1, 3, 4}), buildList([]int{2, 6})}
	got := listToSlice(mergeKLists(lists))   // 把 listToSlice(mergeKLists(lists)) 写入 got :
	want := []int{1, 1, 2, 3, 4, 4, 5, 6}    // 把 []int{1, 1, 2, 3, 4, 4, 5, 6} 写入 want :
	if fmt.Sprint(got) != fmt.Sprint(want) { // 若 fmt.Sprint(got) 不等于 fmt.Sprint(want
		fmt.Printf("FAIL =%v want %v\n", got, want) // 打印输出
		os.Exit(1)                                  // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
