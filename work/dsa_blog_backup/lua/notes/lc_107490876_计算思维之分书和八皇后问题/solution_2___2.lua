-- 来源：https://blog.csdn.net/tyro_java/article/details/107490876
-- LeetCode 107490876. 分书和八皇后问题 — Lua 版（方案2：分书，函数式不可变副本）
local like = { -- 把 { 写入 local like
	{ 0, 0, 1, 1, 0 },
	{ 1, 1, 0, 0, 1 },
	{ 0, 1, 1, 0, 1 },
	{ 0, 0, 0, 1, 0 },
	{ 0, 1, 0, 0, 1 },
}

local function allocate_books_func() -- local function allocate_books_func()
	local results = {} -- 把 {} 写入 local results

	local function try_assign(reader, assigned) -- local function try_assign(reader, assigned)
		if reader > 5 then -- 若 reader 超过 5 then
			local snap = {} -- 把 {} 写入 local snap
			for i = 1, 5 do
				snap[i] = assigned[i] - 1
			end -- 让 下标 i 从 1 走到 5（Lua 1 基）
			results[#results + 1] = snap -- 把 snap 写入 results[#results + 1]
			return -- return
		end -- 终点
		for book = 1, 5 do -- 让 book 从 1 走到 5（Lua 1 基）
			if like[reader][book] == 1 and assigned[book] == -1 then -- 若 like[reader][book] 等于 1 and assigned[book] 等于 减 1 then
				local nxt = {} -- 把 {} 写入 local nxt
				for i = 1, 5 do
					nxt[i] = assigned[i]
				end -- 让 下标 i 从 1 走到 5（Lua 1 基）
				nxt[book] = reader -- 把 reader 写入 nxt[book]
				try_assign(reader + 1, nxt) -- try_assign(reader 加 1, nxt)
			end -- 终点
		end -- 终点
	end -- 终点

	try_assign(1, { -1, -1, -1, -1, -1 }) -- try_assign(1, { 减 1, 减 1, 减 1, 减 1, 减 1})
	return results -- 返回 results
end -- 终点

local want = { { 1, 2, 0, 3, 4 }, { 1, 4, 0, 3, 2 } } -- 把 {{1, 2, 0, 3, 4}, {1, 4, 0, 3, 2}} 写入 local want
local res = allocate_books_func() -- 把 allocate_books_func() 写入 local res
assert(#res == #want, "count mismatch") -- 断言校验
for i = 1, #want do -- 把 1, #want do 写入 for i
	for j = 1, 5 do -- 让 下标 j 从 1 走到 5（Lua 1 基）
		assert(res[i][j] == want[i][j], "scheme " .. i .. " mismatch") -- 断言校验
	end -- 终点
end -- 终点
print("PASS") -- 全部用例通过，输出 PASS
