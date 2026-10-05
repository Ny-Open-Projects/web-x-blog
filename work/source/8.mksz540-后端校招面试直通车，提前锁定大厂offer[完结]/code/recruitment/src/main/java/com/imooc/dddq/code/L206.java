package com.imooc.dddq.code;

import com.imooc.dddq.common.ListNode;

import java.util.ArrayList;
import java.util.List;

public class L206 {
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
        head = new L206().reverseList(head);
        ListNode.travelList(head);
    }
}
