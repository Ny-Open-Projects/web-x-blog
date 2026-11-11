-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133922762
-- LeetCode 160. 相交链表 — Lua 版（方案1）
local ListNode = {} -- 把 {} 写入 local ListNode
ListNode.__index = ListNode -- 把 ListNode 写入 ListNode.__index
function ListNode.new(val, next)
	return setmetatable({ val = val, next = next }, ListNode)
end
local function get_intersection_node(headA, headB) -- local function get_intersection_node(链表 A, 链表 B)
	if not headA or not headB then
		return nil
	end -- 若 not 链表 A or not 链表 B then return nil 终点
	local p1, p2 = headA, headB -- 把 链表 A, 链表 B 写入 local p1, p2
	while p1 ~= p2 do -- 把 p2 do 写入 while p1 ~
		if p1 then
			p1 = p1.next
		else
			p1 = headB
		end -- 若 p1 then p1 赋值为 p1.下一个 else p1 赋值为 链表 B 终点
		if p2 then
			p2 = p2.next
		else
			p2 = headA
		end -- 若 p2 then p2 赋值为 p2.下一个 else p2 赋值为 链表 A 终点
	end -- 终点
	return p1 -- 返回 p1
end -- 终点
local shared = ListNode.new(8, ListNode.new(4, ListNode.new(5)))
local a = ListNode.new(4, ListNode.new(1, shared)) -- 把 ListNode.new(4, ListNode.new(1, shared)) 写入 local a
local b = ListNode.new(5, ListNode.new(6, ListNode.new(1, shared)))
assert(get_intersection_node(a, b) == shared) -- 断言校验
assert(get_intersection_node(ListNode.new(1), ListNode.new(1)) == nil) -- 断言校验
assert(get_intersection_node(nil, nil) == nil) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
