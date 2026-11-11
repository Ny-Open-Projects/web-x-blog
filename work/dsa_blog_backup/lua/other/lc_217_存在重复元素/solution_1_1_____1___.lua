-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/135038527
-- LeetCode 217. 存在重复元素 — Lua 版（方案1）
local function contains_duplicate(nums) -- local function contains_duplicate(数组)
	local set = {} -- 把 {} 写入 local set
	local cnt = 0 -- 把 0 写入 local cnt
	for _, v in ipairs(nums) do -- 遍历取 值
		if not set[v] then
			set[v] = true
			cnt = cnt + 1
		end -- 若 not set[值] then set[值] 赋值为 true; 计数 赋值为 计数 加 1 终点
	end -- 终点
	return cnt ~= #nums -- 返回 计数 ~ 赋值为 #数组
end -- 终点
assert(contains_duplicate({ 1, 2, 3, 1 }) == true) -- 断言校验
assert(contains_duplicate({ 1, 2, 3, 4 }) == false) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
