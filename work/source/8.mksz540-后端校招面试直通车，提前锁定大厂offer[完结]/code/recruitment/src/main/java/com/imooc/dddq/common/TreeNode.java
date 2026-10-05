package com.imooc.dddq.common;

import java.util.*;

public class TreeNode {
    public TreeNode leftNode;
    public TreeNode rightNode;
    public Integer val;

    public TreeNode(Integer val) {
        this.val = val;
    }

    public TreeNode(Integer val, TreeNode left, TreeNode right) {
        this.val = val;
        this.leftNode = left;
        this.rightNode = right;
    }

    public static TreeNode buildTree(List<Integer> nums) {
        if (nums.size() == 0) {
            return null;
        }
        List<TreeNode> treeNodes = new ArrayList<>();
        for(int i = 0; i < nums.size(); i ++) {
            treeNodes.add(new TreeNode(nums.get(i)));
        }
        for(int i = 0; i < treeNodes.size(); i ++) {
            int leftNodeIndex = i * 2 + 1;
            int rightNodeIndex = i * 2 + 2;
            if (leftNodeIndex < treeNodes.size() && treeNodes.get(leftNodeIndex) != null) {
                treeNodes.get(i).leftNode = treeNodes.get(leftNodeIndex);
            }if (rightNodeIndex < treeNodes.size() && treeNodes.get(rightNodeIndex) != null) {
                treeNodes.get(i).rightNode = treeNodes.get(rightNodeIndex);
            }
        }
        return treeNodes.get(0);
    }

    // 前序遍历
    public static void preOrder(List<Integer> result, TreeNode head) {
        if (head == null) {
            return;
        }
        result.add(head.val);
        preOrder(result, head.leftNode);
        preOrder(result, head.rightNode);
    }

    // 中序遍历
    public static void inOrder(List<Integer> result, TreeNode head) {
        if (head == null) {
            return;
        }
        inOrder(result, head.leftNode);
        result.add(head.val);
        inOrder(result, head.rightNode);
    }

    // 后序遍历
    public static void postOrder(List<Integer> result, TreeNode head) {
        if (head == null) {
            return;
        }
        postOrder(result, head.leftNode);
        postOrder(result, head.rightNode);
        result.add(head.val);
    }

    // 层序遍历（广度优先遍历）
    public static void levelOrder(List<Integer> result, TreeNode head) {
        if(head == null) {
            return;
        }
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(head);
        while (! queue.isEmpty()) {
            TreeNode node = queue.poll();
            result.add(node.val);
            if (node.leftNode != null) {
                queue.offer(node.leftNode);
            }
            if (node.rightNode != null) {
                queue.offer(node.rightNode);
            }
        }
    }

    /**
     *          1
     *        2   3
     *      4  5 6  7
     *    8  9
     *
     * @param args
     */
    public static void main(String[] args) {
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        nums.add(5);
        nums.add(6);
        nums.add(7);
        nums.add(8);
        nums.add(9);
        TreeNode head = buildTree(nums);
        List<Integer> result = new ArrayList<>();
        preOrder(result, head);
        System.out.println(result);
        result.clear();
        inOrder(result, head);
        System.out.println(result);
        result.clear();
        postOrder(result, head);
        System.out.println(result);
        result.clear();
        levelOrder(result, head);
        System.out.println(result);
    }
}
