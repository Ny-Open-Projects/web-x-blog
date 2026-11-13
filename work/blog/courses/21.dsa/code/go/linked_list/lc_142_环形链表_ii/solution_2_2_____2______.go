// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145094299
package main // 引入依赖
import (
	"fmt"
	"os"
) // 引入依赖
type ListNode struct {
	Val  int
	Next *ListNode
} // 定义类型
func detectCycle(head *ListNode) *ListNode { // 定义函数/方法 detectCycle
	if head == nil {
		return nil
	} // 若 头节点 等于 nil { return nil }
	slow, fast := head, head // 把 头节点, 头节点 写入 slow, fast :
	for fast != nil {        // 把 nil { 写入 for fast !
		slow = slow.Next // 把 慢指针.Next 写入 慢指针
		if fast.Next == nil {
			return nil
		} // 若 快指针.Next 等于 nil { return nil }
		fast = fast.Next.Next // 把 快指针.Next.Next 写入 快指针
		if fast == slow {     // 若 快指针 等于 慢指针
			ptr := head // 把 头节点 写入 ptr :
			for ptr != slow {
				ptr = ptr.Next
				slow = slow.Next
			} // 把 慢指针 { ptr 赋值为 ptr.Next; 慢指针 赋值为 慢指针.Next } 写入 for ptr !
			return ptr // 返回 ptr
		}
	}
	return nil // 返回 nil
}
func buildCycle() *ListNode { // 定义函数/方法 buildCycle
	n3 := &ListNode{Val: 3}            // 把 按位与 ListNode{Val:3} 写入 n3 :
	n2 := &ListNode{Val: 2, Next: n3}  // 把 按位与 ListNode{Val:2, Next:n3} 写入 n2 :
	n0 := &ListNode{Val: 0, Next: n2}  // 把 按位与 ListNode{Val:0, Next:n2} 写入 n0 :
	n4 := &ListNode{Val: -4, Next: n2} // 把 按位与 ListNode{Val: 减 4, Next:n2} 写入 n4 :
	n3.Next = n4                       // 把 n4 写入 n3.Next
	return n0                          // 返回 n0
}
func main() { // 程序入口：跑内嵌自测用例
	ok := true // 把 true 写入 ok :
	if detectCycle(nil) != nil {
		ok = false
		fmt.Println("FAIL nil")
	}
	c := detectCycle(buildCycle()) // 把 detectCycle(buildCycle()) 写入 c :
	if c == nil || c.Val != 2 {
		ok = false
		fmt.Printf("FAIL cycle val=%v\n", c)
	}
	if !ok {
		os.Exit(1)
	} // 若 取反 ok { os.Exit(1) }
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
