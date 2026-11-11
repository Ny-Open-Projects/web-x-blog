// 来源（blog）：https://blog.csdn.net/tyro_java/article/details/145091535
package main // 引入依赖

import (
	"fmt"
	"os"
) // 引入依赖

type TreeNode struct { // 定义类型
	Val   int       // Val int
	Left  *TreeNode // Left 乘 TreeNode
	Right *TreeNode // Right 乘 TreeNode
}

func constructMaximumBinaryTree(nums []int) *TreeNode { // 定义函数/方法 constructMaximumBinaryTree
	if len(nums) == 0 { // 若 长度(数组) 等于 0
		return nil // 返回 nil
	}
	idx := 0                         // 把 0 写入 idx :
	for i := 0; i < len(nums); i++ { // 让 下标 i 从 0 开始计数
		if nums[i] > nums[idx] { // 若 数组[下标 i] 超过 数组[idx]
			idx = i // 把 下标 i 写入 idx
		}
	}
	root := &TreeNode{Val: nums[idx]}                     // 把 按位与 TreeNode{Val: 数组[idx]} 写入 root :
	root.Left = constructMaximumBinaryTree(nums[:idx])    // 把 constructMaximumBinaryTree(数组[:idx]) 写入 root.Left
	root.Right = constructMaximumBinaryTree(nums[idx+1:]) // 把 constructMaximumBinaryTree(数组[idx 加 1:]) 写入 root.Right
	return root                                           // 返回 根节点
}

func main() { // 程序入口：跑内嵌自测用例
	root := constructMaximumBinaryTree([]int{3, 2, 1, 6, 0, 5})
	if root == nil || root.Val != 6 { // 若 根节点 等于 nil 或 根节点.Val 不等于 6
		fmt.Printf("FAIL root.Val=%v want=6\n", root) // 打印输出
		os.Exit(1)                                    // os.Exit(1)
	}
	fmt.Println("PASS") // 全部用例通过，输出 PASS
}
