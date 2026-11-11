// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/144850725
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	val         int       // 值 int
	left, right *TreeNode // 左边界, 右边界 乘 TreeNode
}

func rob(root *TreeNode) int { // 定义函数/方法 rob
	st := dfs(root)    // 把 dfs(根节点) 写入 st :
	if st[0] > st[1] { // 若 st[0] 超过 st[1]
		return st[0] // 返回 st[0]
	}
	return st[1] // 返回 st[1]
}

func dfs(node *TreeNode) [2]int { // 定义函数/方法 dfs
	if node == nil { // 若 节点 等于 nil
		return [2]int{0, 0} // 返回 [2]int{0, 0}
	}
	l := dfs(node.left)                // 把 dfs(节点.左边界) 写入 l :
	r := dfs(node.right)               // 把 dfs(节点.右边界) 写入 r :
	selected := node.val + l[1] + r[1] // 把 节点.值 加 左指针[1] 加 右指针[1] 写入 selected :
	notSelected := max(l[0], l[1]) + max(r[0], r[1])
	return [2]int{selected, notSelected} // 返回 [2]int{selected, notSelected}
}

func max(a, b int) int { // 定义函数/方法 max
	if a > b { // 若 数组 超过 b
		return a // 返回 数组
	}
	return b // 返回 b
}

func main() { // 程序入口：跑内嵌自测用例
	ok := true         // 把 true 写入 ok :
	if rob(nil) != 0 { // 若 rob(nil) 不等于 0
		ok = false              // 把 false 写入 ok
		fmt.Println("FAIL nil") // 打印输出
	}
	single := &TreeNode{val: 5} // 把 按位与 TreeNode{值: 5} 写入 single :
	if rob(single) != 5 {       // 若 rob(single) 不等于 5
		ok = false                 // 把 false 写入 ok
		fmt.Println("FAIL single") // 打印输出
	}
	root := &TreeNode{val: 3, left: &TreeNode{val: 2, right: &TreeNode{val: 3}}, right: &TreeNode{val: 3, right: &TreeNode{val: 1}}}
	if rob(root) != 7 { // 若 rob(根节点) 不等于 7
		ok = false               // 把 false 写入 ok
		fmt.Println("FAIL demo") // 打印输出
	}
	if !ok { // 若 取反 ok
		os.Exit(1) // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
