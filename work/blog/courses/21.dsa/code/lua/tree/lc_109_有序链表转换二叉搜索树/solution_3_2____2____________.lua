-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135270549
-- LeetCode 109. 有序链表转换二叉搜索树 — Lua 版（方案3）
local TreeNode = {} -- 把 {} 写入 local TreeNode
TreeNode.__index = TreeNode -- 把 TreeNode 写入 TreeNode.__index
function TreeNode.new(val) -- function TreeNode.new(值)
	return setmetatable({ val = val, left = nil, right = nil }, TreeNode)
end -- 终点

local function build_tree(vals) -- local function build_tree(vals)
	if not vals or #vals == 0 or vals[1] == "null" then
		return nil
	end
	local root = TreeNode.new(vals[1]) -- 把 TreeNode.new(vals[1]) 写入 local root
	local queue = { root } -- 把 {根节点} 写入 local queue
	local head = 1 -- 把 1 写入 local head
	local i = 2 -- 把 2 写入 local i
	while head <= #queue and i <= #vals do -- 把 #队列 and 下标 i 不超过 #vals do 写入 while head <
		local node = queue[head] -- 把 队列[头节点] 写入 local node
		head = head + 1 -- 把 头节点 加 1 存入 头节点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.left = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 左边界
				queue[#queue + 1] = node.left -- 把 节点.左边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
		if i <= #vals then -- 若 下标 i 不超过 #vals then
			if vals[i] ~= "null" then -- 若 vals[下标 i] ~ 赋值为 「null」 then
				node.right = TreeNode.new(vals[i]) -- 把 TreeNode.new(vals[下标 i]) 写入 右边界
				queue[#queue + 1] = node.right -- 把 节点.右边界 写入 queue[#queue + 1]
			end -- 终点
			i = i + 1 -- 把 下标 i 加 1 存入 下标 i
		end -- 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点

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
local function sorted_list_to_bst(head) -- local function sorted_list_to_bst(头节点)
	local nodes = {} -- 把 {} 写入 local nodes
	local cur = head -- 把 头节点 写入 local cur
	while cur do
		nodes[#nodes + 1] = cur.val
		cur = cur.next
	end
	local function build(left, right) -- local function build(左边界, 右边界)
		if left > right then
			return nil
		end -- 若 左边界 超过 右边界 then return nil 终点
		local mid = left + math.floor((right - left) / 2) -- 把 左边界 加 math.floor((右边界 减 左边界) 除以 2) 写入 local mid
		local root = TreeNode.new(nodes[mid]) -- 把 TreeNode.new(nodes[中点]) 写入 local root
		root.left = build(left, mid - 1) -- 把 build(左边界, 中点 减 1) 写入 左边界
		root.right = build(mid + 1, right) -- 把 build(中点 加 1, 右边界) 写入 右边界
		return root -- 返回 根节点
	end -- 终点
	if #nodes == 0 then
		return nil
	end -- 若 #nodes 等于 0 then return nil 终点
	return build(1, #nodes) -- 返回 build(1, #nodes)
end -- 终点
local function inorder(n, out) -- local function inorder(元素个数, out)
	if not n then
		return
	end -- 若 not 元素个数 then return 终点
	inorder(n.left, out) -- inorder(元素个数.左边界, out)
	out[#out + 1] = n.val -- 把 元素个数.值 写入 out[#out + 1]
	inorder(n.right, out) -- inorder(元素个数.右边界, out)
end -- 终点
assert(sorted_list_to_bst(nil) == nil) -- 断言校验
local t = sorted_list_to_bst(build_list({ 1, 2, 3 })) -- 把 sorted_list_to_bst(build_list({1, 2, 3})) 写入 local t
local out = {} -- 把 {} 写入 local out
inorder(t, out) -- inorder(另一字符串, out)
assert(#out == 3 and out[1] == 1 and out[2] == 2 and out[3] == 3) -- 断言校验
-- 结构验证：层序 [2,1,3]
local q, flat = { t }, {} -- 把 {另一字符串}, {} 写入 local q, flat
while #q > 0 do -- while #节点 超过 0 do
	local n = table.remove(q, 1) -- 把 table 弹出 节点, 1) 写入 local n
	flat[#flat + 1] = n.val -- 把 元素个数.值 写入 flat[#flat + 1]
	if n.left then
		q[#q + 1] = n.left
	end -- 若 元素个数.左边界 then 节点[#节点 加 1] 赋值为 元素个数.左边界 终点
	if n.right then
		q[#q + 1] = n.right
	end -- 若 元素个数.右边界 then 节点[#节点 加 1] 赋值为 元素个数.右边界 终点
end -- 终点
assert(#flat == 3 and flat[1] == 2 and flat[2] == 1 and flat[3] == 3) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
