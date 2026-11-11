-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134283831
-- LeetCode 23. 合并K个升序链表 — Lua 版（方案2）
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
local function merge_k_lists(lists) -- local function merge_k_lists(lists)
	local ptrs = {} -- 把 {} 写入 local ptrs
	for i, l in ipairs(lists) do
		ptrs[i] = l
	end -- 遍历取 左指针
	local dummy = ListNode.new(0) -- 把 ListNode.new(0) 写入 local dummy
	local tail = dummy -- 把 哨兵节点 写入 local tail
	while true do -- while true do
		local best, bi = nil, 0 -- 把 nil, 0 写入 local best, bi
		for i = 1, #ptrs do -- 把 1, #ptrs do 写入 for i
			local p = ptrs[i] -- 把 ptrs[下标 i] 写入 local p
			if p and (best == nil or p.val < best) then
				best = p.val
				bi = i
			end
		end -- 终点
		if bi == 0 then
			break
		end -- 若 bi 等于 0 then break 终点
		tail.next = ptrs[bi] -- 把 ptrs[bi] 写入 下一个
		ptrs[bi] = ptrs[bi].next -- 把 ptrs[bi].下一个 写入 ptrs[bi]
		tail = tail.next -- 把 尾节点.下一个 存入 尾节点
	end -- 终点
	return dummy.next -- 返回 哨兵节点.下一个
end -- 终点
local got = list_to_vec(merge_k_lists({ build_list({ 1, 4, 5 }), build_list({ 1, 3, 4 }), build_list({ 2, 6 }) }))
assert(#got == 8 and table.concat(got, ",") == "1,1,2,3,4,4,5,6") -- 打印输出
assert(#list_to_vec(merge_k_lists({})) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
