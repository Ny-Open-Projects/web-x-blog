package com.imooc.dddq.code;

import com.imooc.dddq.common.ListNode;

import java.util.ArrayList;
import java.util.List;

public class L92 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        // 1. 找到left的上一个节点
        ListNode leftNodePrev = null;
        ListNode leftNode = head;
        ListNode dummyNode = new ListNode(-1);
        dummyNode.next = head;
        leftNodePrev = dummyNode;
        for (int i = 0; i < left - 1; i ++) {
            // 子链表的左边节点
            leftNode = leftNode.next;
            // 子链表的左边节点的上一个节点
            leftNodePrev = leftNodePrev.next;
        }
        // 2. 找到right节点
        ListNode rightNode = leftNodePrev;
        for (int i = 0; i < right - left + 1; i ++) {
            rightNode = rightNode.next;
        }
//        System.out.println(leftNodePrev.val);
//        System.out.println(leftNode.val);
//        System.out.println(rightNode.val);
        // 3. 切断子链表
        ListNode rightNodeNext = rightNode.next;
        leftNodePrev.next = null;
        rightNode.next = null;
        // 4. 反转子链表
        leftNode = reverseList(leftNode);
//        ListNode.travelList(leftNode);
        // 5. 重新连接
        // 左边连接
        leftNodePrev.next = leftNode;
        while (leftNode.next != null) {
            leftNode = leftNode.next;
        }
        leftNode.next = rightNodeNext;
        return dummyNode.next;
    }

    public ListNode reverseList(ListNode head) {
        if (head == null) {
            return null;
        }
        ListNode prev = null;
        ListNode curr = head;
        ListNode next = curr.next;
        while (next != null) {
            curr.next = prev;
            prev = curr;
            curr = next;
            next = next.next;
        }
        curr.next = prev;
        return curr;
    }

    public static void main(String[] args){
        List<Integer> nums = new ArrayList<>();
        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        nums.add(5);
        ListNode head = ListNode.buildList(nums);
        ListNode.travelList(head);
        head = new L92().reverseBetween(head, 1, 5);
        ListNode.travelList(head);
    }
}
