-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/133746567
-- LeetCode 19. 删除链表的倒数第N个结点 — Lua 版（方案3）
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
local function remove_nth_from_end(head, n) -- local function remove_nth_from_end(头节点, 元素个数)
	local dummy = ListNode.new(0) -- 把 ListNode.new(0) 写入 local dummy
	dummy.next = head -- 把 头节点 写入 下一个
	local fast, slow = dummy, dummy -- 把 哨兵节点, 哨兵节点 写入 local fast, slow
	for _ = 1, n + 1 do
		fast = fast.next
	end -- 让 _ 从 1 走到 元素个数（Lua 1 基）
	while fast do -- while 快指针 do
		fast = fast.next -- 把 快指针.下一个 存入 快指针
		slow = slow.next -- 把 慢指针.下一个 存入 慢指针
	end -- 终点
	slow.next = slow.next.next -- 把 慢指针.下一个.下一个 写入 下一个
	return dummy.next -- 返回 哨兵节点.下一个
end -- 终点
assert(table.concat(to_vec(remove_nth_from_end(build_list({ 1, 2, 3, 4, 5 }), 2)), ",") == "1,2,3,5") -- 打印输出
assert(#to_vec(remove_nth_from_end(build_list({ 1 }), 1)) == 0) -- 断言校验
assert(table.concat(to_vec(remove_nth_from_end(build_list({ 1, 2 }), 2)), ",") == "2") -- 打印输出
print("PASS") -- 全部用例通过，输出 PASS
