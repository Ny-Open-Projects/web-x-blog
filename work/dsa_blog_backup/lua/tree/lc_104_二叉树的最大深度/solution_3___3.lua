-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/130815631
-- LeetCode 104. 二叉树的最大深度 — Lua 版（方案3：分治递归（紧凑版，附层序/相同树/中序辅助函数））
-- harness：层序数组建树，"null" 表示空节点

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

-- 辅助：层序遍历按层分组
local function level_list(root) -- local function level_list(根节点)
	local res = {} -- 把 {} 写入 local res
	local queue = {} -- 把 {} 写入 local queue
	if root then
		queue[1] = root
	end -- 若 根节点 then 队列[1] 赋值为 根节点 终点
	local head = 1 -- 把 1 写入 local head
	while head <= #queue do -- 把 #队列 do 写入 while head <
		local nxt = {} -- 把 {} 写入 local nxt
		local vals = {} -- 把 {} 写入 local vals
		local tail = head -- 把 头节点 写入 local tail
		for i = head, #queue do -- 把 头节点, #队列 do 写入 for i
			local node = queue[i] -- 把 队列[下标 i] 写入 local node
			vals[#vals + 1] = node.val -- 把 节点.值 写入 vals[#vals + 1]
			if node.left then
				nxt[#nxt + 1] = node.left
			end -- 若 节点.左边界 then nxt[#nxt 加 1] 赋值为 节点.左边界 终点
			if node.right then
				nxt[#nxt + 1] = node.right
			end -- 若 节点.右边界 then nxt[#nxt 加 1] 赋值为 节点.右边界 终点
		end -- 终点
		res[#res + 1] = vals -- 把 vals 写入 res[#res + 1]
		queue = nxt -- 把 nxt 存入 队列
		head = 1 -- 把 1 存入 头节点
	end -- 终点
	return res -- 返回 结果
end -- 终点

-- 辅助：判断两棵树是否相同
local function same_tree(a, b) -- local function same_tree(数组, b)
	if not a and not b then
		return true
	end -- 若 not 数组 and not b then return true 终点
	if not a or not b then
		return false
	end -- 若 not 数组 or not b then return false 终点
	return a.val == b.val and same_tree(a.left, b.left) and same_tree(a.right, b.right)
end -- 终点

-- 辅助：中序遍历
local function inorder_t(root) -- local function inorder_t(根节点)
	if not root then
		return {}
	end -- 若 not 根节点 then return {} 终点
	local out = {} -- 把 {} 写入 local out
	for _, v in ipairs(inorder_t(root.left)) do
		out[#out + 1] = v
	end -- 遍历取 值
	out[#out + 1] = root.val -- 把 根节点.值 写入 out[#out + 1]
	for _, v in ipairs(inorder_t(root.right)) do
		out[#out + 1] = v
	end -- 遍历取 值
	return out -- 返回 out
end -- 终点

-- 主解法：分治递归，深度 = 1 + max(左子树深度, 右子树深度)
local function max_depth(root) -- local function max_depth(根节点)
	if not root then
		return 0
	end -- 若 not 根节点 then return 0 终点
	local l = max_depth(root.left) -- 把 max_depth(根节点.左边界) 写入 local l
	local r = max_depth(root.right) -- 把 max_depth(根节点.右边界) 写入 local r
	if l > r then
		return 1 + l
	else
		return 1 + r
	end -- 若 左指针 超过 右指针 then return 1 加 左指针 else return 1 加 右指针 终点
end -- 终点

-- 自测：与 blog 方案用例一致
local tests = { -- 把 { 写入 local tests
	{ { 3, 9, 20, "null", "null", 15, 7 }, 3 },
	{ { 1, 2, 3, 4, 5, "null", "null", "null", 6 }, 4 },
	{ {}, 0 },
}
for idx, t in ipairs(tests) do -- 遍历取 另一字符串
	local got = max_depth(build_tree(t[1])) -- 把 max_depth(build_tree(另一字符串[1])) 写入 local got
	local want = t[2] -- 把 另一字符串[2] 写入 local want
	assert(got == want, string.format("case %d failed: got %d want %d", idx, got, want)) -- 断言校验
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
