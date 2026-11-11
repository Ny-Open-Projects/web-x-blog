-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133813394
-- LeetCode 203. 移除链表元素 — Lua 版（方案1）
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
local function to_vec(h) -- local function to_vec(h)
	local out = {} -- 把 {} 写入 local out
	while h do
		out[#out + 1] = h.val
		h = h.next
	end -- 把 h.值; h 赋值为 h.下一个 终点 写入 while h do out[#out + 1]
	return out -- 返回 out
end -- 终点
local function remove_elements(head, val) -- local function remove_elements(头节点, 值)
	local dummy = ListNode.new(0) -- 把 ListNode.new(0) 写入 local dummy
	dummy.next = head -- 把 头节点 写入 下一个
	local cur = dummy -- 把 哨兵节点 写入 local cur
	while cur.next do -- while 当前值.下一个 do
		if cur.next.val == val then -- 若 当前值.下一个.值 等于 值 then
			cur.next = cur.next.next -- 把 当前值.下一个.下一个 写入 下一个
		else -- 否则
			cur = cur.next -- 把 当前值.下一个 存入 当前值
		end -- 终点
	end -- 终点
	return dummy.next -- 返回 哨兵节点.下一个
end -- 终点
assert(table.concat(to_vec(remove_elements(build_list({ 1, 2, 3, 4, 5, 6 }), 6)), ",") == "1,2,3,4,5") -- 打印输出
assert(remove_elements(build_list({ 7, 7, 7, 7 }), 7) == nil) -- 断言校验
assert(table.concat(to_vec(remove_elements(build_list({ 1, 2, 2, 1 }), 2)), ",") == "1,1") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
