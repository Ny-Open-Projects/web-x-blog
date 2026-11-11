-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133874671
-- LeetCode 142. 环形链表II — Lua 版（方案1）
local ListNode = {} -- 把 {} 写入 local ListNode
ListNode.__index = ListNode -- 把 ListNode 写入 ListNode.__index
function ListNode.new(val, next)
	return setmetatable({ val = val, next = next }, ListNode)
end
local function detect_cycle(head) -- local function detect_cycle(头节点)
	local slow, fast = head, head -- 把 头节点, 头节点 写入 local slow, fast
	while fast and fast.next do -- while 快指针 and 快指针.下一个 do
		slow = slow.next -- 把 慢指针.下一个 存入 慢指针
		fast = fast.next.next -- 把 快指针.下一个.下一个 存入 快指针
		if slow == fast then -- 若 慢指针 等于 快指针 then
			local p1, p2 = head, slow -- 把 头节点, 慢指针 写入 local p1, p2
			while p1 ~= p2 do -- 把 p2 do 写入 while p1 ~
				p1 = p1.next -- 把 p1.下一个 存入 p1
				p2 = p2.next -- 把 p2.下一个 存入 p2
			end -- 终点
			return p1 -- 返回 p1
		end -- 终点
	end -- 终点
	return nil -- 返回 nil
end -- 终点
local function build_with_cycle(vals, pos) -- local function build_with_cycle(vals, pos)
	local head, cur, tail_at = nil, nil, nil -- 把 nil, nil, nil 写入 local head, cur, tail_at
	for i, v in ipairs(vals) do -- 遍历取 值
		local n = ListNode.new(v) -- 把 ListNode.new(值) 写入 local n
		if not head then
			head, cur = n, n
		else
			cur.next, cur = n, n
		end
		if i == pos then
			tail_at = n
		end -- 若 下标 i 等于 pos then tail_at 赋值为 元素个数 终点
	end -- 终点
	if cur and tail_at then
		cur.next = tail_at
	end -- 若 当前值 and tail_at then 当前值.下一个 赋值为 tail_at 终点
	return head -- 返回 头节点
end -- 终点
local h = build_with_cycle({ 3, 2, 0, -4 }, 2) -- 把 build_with_cycle({3, 2, 0, 减 4}, 2) 写入 local h
assert(detect_cycle(h) ~= nil and detect_cycle(h).val == 2) -- 断言校验
assert(detect_cycle(ListNode.new(1)) == nil) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
