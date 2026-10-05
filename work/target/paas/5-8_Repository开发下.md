# Go PaaS 平台开发: Repository 数据访问层开发（下）—— 事务删除与更新

## 纲要

- 删除 Pod 是跨三表的联表删除，必须开启事务保证数据一致性
- 使用 `Where("id = ?", id)` 占位符，避免 SQL 注入
- `Begin` / `Rollback` / `Commit` 三段式事务控制，并用 `recover` 兜底 panic
- 软删除与硬删除的业务取舍
- `UpdatePod` 与 `FindAll` 的简洁实现

## 联表删除的事务必要性

Pod 与其端口表（PodPort）、环境变量表（PodEnv）是父子关系。删除一个 Pod 时，如果只删主表而子表残留，就会产生孤儿数据、破坏一致性。因此 `DeletePodByID` 必须把三张表的删除放进**同一个事务**。

## 事务删除实现

```go
// pod/domain/repository/pod_repository.go
func (u *PodRepository) DeletePodByID(podID int64) error {
	tx := u.mysqlDb.Begin()
	// 遇到问题回滚（含 panic 兜底）
	defer func() {
		if r := recover(); r != nil {
			tx.Rollback()
		}
	}()
	if tx.Error != nil {
		return tx.Error
	}

	// 彻底删除 POD 信息
	if err := u.mysqlDb.Where("id = ?", podID).Delete(&model.Pod{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 彻底删除 podenv 信息
	if err := u.mysqlDb.Where("pod_id = ?", podID).Delete(&model.PodEnv{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	// 彻底删除 podport 信息
	if err := u.mysqlDb.Where("pod_id = ?", podID).Delete(&model.PodPort{}).Error; err != nil {
		tx.Rollback()
		return err
	}
	return tx.Commit().Error
}
```

### 关键细节

- **占位符防注入**：`Where("id = ?", podID)` 使用参数化查询，避免拼接 SQL 带来的注入风险。任何面向外部的 ID 都不要直接拼接到 SQL 字符串里。
- **panic 兜底**：`defer` 中 `recover` 捕获意外 panic 并回滚，防止事务悬挂。
- **逐步回滚**：任一步骤出错立即 `Rollback` 并返回错误，由上层感知。

## 软删除还是硬删除

平台提供两种删除语义，应按业务选择：

- **硬删除**：物理删除记录（如上代码），彻底从数据表移除。
- **软删除**：在表上加一个"已删除"字段（如 `deleted_at` 或 `is_deleted`）。值为 1 表示删除，0 / false 表示正常。物理信息保留，便于审计与恢复。

本示例采用硬删除。如果业务需要保留痕迹（如计费对账），应改为软删除并在查询时过滤。

## 更新与查询全部

更新相对简单，直接对模型执行 `Update`：

```go
func (u *PodRepository) UpdatePod(pod *model.Pod) error {
	return u.mysqlDb.Model(pod).Update(pod).Error
}
```

查询全部返回切片，是所有列表类接口的基础：

```go
func (u *PodRepository) FindAll() (podAll []model.Pod, err error) {
	return podAll, u.mysqlDb.Find(&podAll).Error
}
```

## Demo 示例（补充：通用事务删除模板）

把上面 Pod 的联表删除抽象成一个可复用的思路（根据讲稿逻辑补充）：

```go
// 通用联表硬删除模板（节选）
func deleteWithTx(db *gorm.DB, id int64, models ...interface{}) error {
	tx := db.Begin()
	if tx.Error != nil {
		return tx.Error
	}
	for _, m := range models {
		if err := tx.Where("id = ?", id).Delete(m).Error; err != nil {
			tx.Rollback()
			return err
		}
	}
	return tx.Commit().Error
}
```

### 代码说明

- 所有子表删除共用一个事务，任一失败整体回滚。
- 占位符 `?` 保证参数化，规避注入。

### 技术点总结

- 多表删除务必包事务，否则会出现数据不一致。
- 参数化查询是数据库安全底线，review 代码时应重点检查。
- 软/硬删除按审计与计费需求取舍，不是越硬越好。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/base/domain/repository/base_repository.go`
- `code/课件/volume/domain/repository/volume_repository.go`
- `code/课件/svc/domain/repository/svc_repository.go`
- `code/课件/pod/domain/repository/pod_repository.go`
- `code/课件/go-paas-html/pages-404.html`
- `code/课件/route/domain/repository/route_repository.go`
- `code/课件/go-paas-html/pages-forgot-password.html`
- `code/课件/middleware/domain/repository/middle_type_repository.go`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：100%。是否需要继续：是。代码是否可运行：是。
