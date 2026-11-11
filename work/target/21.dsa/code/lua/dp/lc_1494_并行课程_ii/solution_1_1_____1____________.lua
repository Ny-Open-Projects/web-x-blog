-- 来源（blog）：https://blog.csdn.net/tyro_java/article/details/134859412
-- LeetCode 1494. 并行课程II — Lua 版（方案1）
local function min_number_of_semesters(n, relations, k)
	local prereq = {} -- 把 {} 写入 local prereq
	for i = 1, n do
		prereq[i] = 0
	end -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
	for _, r in ipairs(relations) do -- 遍历取 右指针
		prereq[r[2]] = prereq[r[2]] | (1 << (r[1] - 1)) -- 把 prereq[右指针[2]] 按位或 (1 小于 小于 (右指针[1] 减 1)) 写入 prereq[r[2]]
	end -- 终点
	local memo = {} -- 把 {} 写入 local memo
	local function go(done) -- local function go(done)
		if done == (1 << n) - 1 then
			return 0
		end -- 若 done 等于 (1 小于 小于 元素个数) 减 1 then return 0 终点
		if memo[done] then
			return memo[done]
		end -- 若 记忆化表[done] then return 记忆化表[done] 终点
		local avail = 0 -- 把 0 写入 local avail
		for i = 1, n do -- 让 下标 i 从 1 走到 元素个数（Lua 1 基）
			if (done & (1 << (i - 1))) == 0 and (done & prereq[i]) == prereq[i] then
				avail = avail | (1 << (i - 1)) -- 把 avail 按位或 (1 小于 小于 (下标 i 减 1)) 存入 avail
			end -- 终点
		end -- 终点
		local cnt, chosen, a = 0, 0, avail -- 把 0, 0, avail 写入 local cnt, chosen, a
		while a ~= 0 and cnt < k do -- 把 0 and 计数 小于 下标 k do 写入 while a ~
			local low = a & -a -- 把 数组 按位与 ( 减 数组) 写入 local low
			chosen = chosen | low -- 把 chosen 按位或 low 存入 chosen
			a = a ~ low -- 把 数组 ~ low 存入 数组
			cnt = cnt + 1 -- 把 计数 加 1 存入 计数
		end -- 终点
		local r = 1 + go(done | chosen) -- 把 1 加 go(done 按位或 chosen) 写入 local r
		memo[done] = r -- 把 右指针 写入 memo[done]
		return r -- 返回 右指针
	end -- 终点
	return go(0) -- 返回 go(0)
end -- 终点
assert(min_number_of_semesters(4, { { 2, 1 }, { 3, 1 }, { 1, 4 } }, 2) == 3) -- 断言校验
assert(min_number_of_semesters(5, { { 2, 1 }, { 3, 1 }, { 4, 1 }, { 1, 5 } }, 3) == 3) -- 断言校验
assert(min_number_of_semesters(3, {}, 2) == 2) -- 断言校验
assert(min_number_of_semesters(4, { { 1, 2 }, { 2, 3 } }, 1) == 4) -- 断言校验
print("PASS") -- 全部用例通过，输出 PASS
