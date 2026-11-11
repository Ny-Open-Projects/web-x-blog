-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134541657
-- LeetCode 226. 翻转二叉树 — Lua 版（方案6）
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

local function invert_tree(root) -- local function invert_tree(根节点)
	if not root then
		return nil
	end -- 若 not 根节点 then return nil 终点
	local stack = { root } -- 把 {根节点} 写入 local stack
	while #stack > 0 do -- while #栈 超过 0 do
		local node = table.remove(stack) -- 把 table 弹出 栈) 写入 local node
		node.left, node.right = node.right, node.left -- 把 节点.右边界, 节点.左边界 写入 右边界
		if node.left then
			stack[#stack + 1] = node.left
		end -- 若 节点.左边界 then 栈[#栈 加 1] 赋值为 节点.左边界 终点
		if node.right then
			stack[#stack + 1] = node.right
		end -- 若 节点.右边界 then 栈[#栈 加 1] 赋值为 节点.右边界 终点
	end -- 终点
	return root -- 返回 根节点
end -- 终点
local function levels(root) -- local function levels(根节点)
	if not root then
		return {}
	end -- 若 not 根节点 then return {} 终点
	local res = {} -- 把 {} 写入 local res
	local q = { root } -- 把 {根节点} 写入 local q
	while #q > 0 do -- while #节点 超过 0 do
		local cur = {} -- 把 {} 写入 local cur
		local n = #q -- 把 #节点 写入 local n
		for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
			local node = table.remove(q, 1) -- 把 table 弹出 节点, 1) 写入 local node
			cur[#cur + 1] = node.val -- 把 节点.值 写入 cur[#cur + 1]
			if node.left then
				q[#q + 1] = node.left
			end -- 若 节点.左边界 then 节点[#节点 加 1] 赋值为 节点.左边界 终点
			if node.right then
				q[#q + 1] = node.right
			end -- 若 节点.右边界 then 节点[#节点 加 1] 赋值为 节点.右边界 终点
		end -- 终点
		res[#res + 1] = cur -- 把 当前值 写入 res[#res + 1]
	end -- 终点
	return res -- 返回 结果
end -- 终点
local got = levels(invert_tree(build_tree({ 4, 2, 7, 1, 3, 6, 9 })))
assert(
	#got == 3 and got[1][1] == 4 and got[2][1] == 7 and got[2][2] == 2 and got[3][1] == 9 and got[3][4] == 1,
	"invert failed"
) -- 断言校验
assert(#levels(invert_tree(nil)) == 0) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
