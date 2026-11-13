-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
-- LeetCode 23. 合并K个升序链表 — Lua 版（方案3）
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
local function merge_two(a, b) -- local function merge_two(数组, b)
	local dummy = ListNode.new(0) -- 把 ListNode.new(0) 写入 local dummy
	local cur = dummy -- 把 哨兵节点 写入 local cur
	while a and b do -- while 数组 and b do
		if a.val <= b.val then
			cur.next = a
			a = a.next
		else
			cur.next = b
			b = b.next
		end
		cur = cur.next -- 把 当前值.下一个 存入 当前值
	end -- 终点
	cur.next = a or b -- 把 数组 or b 写入 下一个
	return dummy.next -- 返回 哨兵节点.下一个
end -- 终点
local function merge_k_lists(lists) -- local function merge_k_lists(lists)
	local acc = nil -- 把 nil 写入 local acc
	for _, l in ipairs(lists) do
		acc = merge_two(acc, l)
	end -- 遍历取 左指针
	return acc -- 返回 累加器
end -- 终点
local got = list_to_vec(merge_k_lists({ build_list({ 1, 4, 5 }), build_list({ 1, 3, 4 }), build_list({ 2, 6 }) }))
assert(#got == 8 and table.concat(got, ",") == "1,1,2,3,4,4,5,6") -- 打印输出
assert(#list_to_vec(merge_k_lists({})) == 0) -- 断言校验
assert(#list_to_vec(merge_k_lists({ build_list({}) })) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
