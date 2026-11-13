-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/137532387
-- LeetCode 429. N叉树的层序遍历 — Lua 版（方案1）
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

local function new_node(v)
	return { val = v, children = {} }
end
local function level_order(root) -- local function level_order(根节点)
	if not root then
		return {}
	end -- 若 not 根节点 then return {} 终点
	local res = {} -- 把 {} 写入 local res
	local q = { root } -- 把 {根节点} 写入 local q
	while #q > 0 do -- while #节点 超过 0 do
		local level = {} -- 把 {} 写入 local level
		local nxt = {} -- 把 {} 写入 local nxt
		for i = 1, #q do -- 把 1, #节点 do 写入 for i
			local n = q[i] -- 把 节点[下标 i] 写入 local n
			level[#level + 1] = n.val -- 把 元素个数.值 写入 level[#level + 1]
			for _, c in ipairs(n.children) do
				nxt[#nxt + 1] = c
			end -- 遍历取 字符
		end -- 终点
		res[#res + 1] = level -- 把 level 写入 res[#res + 1]
		q = nxt -- 把 nxt 存入 节点
	end -- 终点
	return res -- 返回 结果
end -- 终点
local root = new_node(1) -- 把 new_node(1) 写入 local root
local c3 = new_node(3) -- 把 new_node(3) 写入 local c3
c3.children = { new_node(5), new_node(6) } -- 把 {new_node(5), new_node(6)} 写入 c3.children
root.children = { c3, new_node(2), new_node(4) } -- 把 {c3, new_node(2), new_node(4)} 写入 root.children
local a = level_order(root) -- 把 level_order(根节点) 写入 local a
assert(#a == 3 and a[1][1] == 1 and a[2][1] == 3 and a[2][2] == 2 and a[2][3] == 4 and a[3][1] == 5 and a[3][2] == 6) -- 断言校验
assert(#level_order(nil) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
