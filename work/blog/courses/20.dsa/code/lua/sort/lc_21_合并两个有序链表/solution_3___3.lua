-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133594090
-- LeetCode 21. 合并两个有序链表 — Lua 版（方案3）
local ListNode = {} -- 把 {} 写入 local ListNode
ListNode.__index = ListNode -- 把 ListNode 写入 ListNode.__index
function ListNode.new(val, next)
	return setmetatable({ val = val, next = next }, ListNode)
end
local function build_list(vals) -- local function build_list(vals)
	local head, cur = nil, nil -- 把 nil, nil 写入 local head, cur
	for _, v in ipairs(vals) do -- 遍历取 值
		local n = ListNode.new(v) -- 把 ListNode.new(值) 写入 local n
		if not head then
			head, cur = n, n
		else
			cur.next, cur = n, n
		end
	end -- 终点
	return head -- 返回 头节点
end -- 终点
local function list_to_vec(head) -- local function list_to_vec(头节点)
	local out = {} -- 把 {} 写入 local out
	while head do
		out[#out + 1] = head.val
		head = head.next
	end -- 把 头节点.值; 头节点 赋值为 头节点.下一个 终点 写入 while head do out[#out + 1]
	return out -- 返回 out
end -- 终点
local function merge_two_lists(list1, list2) -- local function merge_two_lists(list1, list2)
	local dummy = ListNode.new(0) -- 把 ListNode.new(0) 写入 local dummy
	local p = dummy -- 把 哨兵节点 写入 local p
	local p1, p2 = list1, list2 -- 把 list1, list2 写入 local p1, p2
	while p1 and p2 do -- while p1 and p2 do
		if p1.val < p2.val then -- 若 p1.值 小于 p2.值 then
			p.next = p1 -- 把 p1 写入 下一个
			p1 = p1.next -- 把 p1.下一个 存入 p1
		else -- 否则
			p.next = p2 -- 把 p2 写入 下一个
			p2 = p2.next -- 把 p2.下一个 存入 p2
		end -- 终点
		p = p.next -- 把 节点.下一个 存入 节点
	end -- 终点
	p.next = p1 or p2 -- 把 p1 or p2 写入 下一个
	return dummy.next -- 返回 哨兵节点.下一个
end -- 终点
local a = list_to_vec(merge_two_lists(build_list({ 1, 2, 4 }), build_list({ 1, 3, 4 })))
assert(#a == 6 and table.concat(a, ",") == "1,1,2,3,4,4") -- 打印输出
assert(#list_to_vec(merge_two_lists(build_list({}), build_list({}))) == 0) -- 断言校验
local c = list_to_vec(merge_two_lists(build_list({}), build_list({ 0 })))
assert(#c == 1 and c[1] == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
