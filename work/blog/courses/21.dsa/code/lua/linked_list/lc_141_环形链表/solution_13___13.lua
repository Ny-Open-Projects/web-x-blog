-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133816714
-- LeetCode 141. 环形链表 — Lua 版（方案13）
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
local function has_cycle(head) -- local function has_cycle(头节点)
	local slow, fast = head, head -- 把 头节点, 头节点 写入 local slow, fast
	while fast and fast.next do -- while 快指针 and 快指针.下一个 do
		slow = slow.next -- 把 慢指针.下一个 存入 慢指针
		fast = fast.next.next -- 把 快指针.下一个.下一个 存入 快指针
		if slow == fast then
			return true
		end -- 若 慢指针 等于 快指针 then return true 终点
	end -- 终点
	return false -- 返回 false
end -- 终点
assert(has_cycle(build_list({ 3, 2, 0, -4 })) == false) -- 断言校验
local h = build_list({ 1 }) -- 把 build_list({1}) 写入 local h
h.next = h -- 把 h 写入 下一个
assert(has_cycle(h) == true) -- 断言校验
assert(has_cycle(nil) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
