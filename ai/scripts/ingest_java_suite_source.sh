#!/bin/bash
# 34.java-suite 素材归档 v2：外置盘 07/08/09/10 → work/source/34.java-suite（只读锁在最后统一加）
# 修正点：① 全部拷完才 chmod ② 先 mkdir -p 父目录 ③ src 带尾斜杠避免嵌套
# 排除大体积二进制与流水线中间产物：wav / class / pyc / _bin / _logs / _state / _smoke / _tmp* / audio_line / vision_line / __pycache__ / _code_*
set -uo pipefail

SRC="/Volumes/SAMSUNG/ai-done"
DST="/Users/Wang/Code/github/web-x-blog/work/source/34.java-suite"
LOG="/Users/Wang/Code/github/web-x-blog/work/target/34-java-suite/_ingest_source.log"

EXCLUDES=(
  --exclude '*.wav' --exclude '*.class' --exclude '*.pyc' --exclude '*.pyo'
  --exclude '__pycache__/' --exclude '_bin/' --exclude '_logs/' --exclude '_state/'
  --exclude '_smoke/' --exclude '_tmp/' --exclude '_tmp_*' --exclude '_code_blocks/'
  --exclude '_code_run/' --exclude 'audio_line/' --exclude 'vision_line/'
  --exclude '.DS_Store' --exclude '._*'
)

step() {
  local label="$1" src="$2" dst="$3"; shift 3
  mkdir -p "$dst"
  echo "[$(date '+%F %T')] >>> $label" | tee -a "$LOG"
  rsync -a --info=stats2 "${EXCLUDES[@]}" "$@" "$src/" "$dst/" 2>&1 | tail -6 | tee -a "$LOG"
}

# 清空重来
rm -rf "$DST"
mkdir -p "$DST"
: > "$LOG"

# M1：阶段七 面试专题（260 md + INDEX + 术语注解 + images 188 png + demos html/js/css）
step "m1-interview" "$SRC/07、阶段七 面试专题_20261025_002609/blog_interview" "$DST/m1-interview"

# M2：就业指导（12 成稿 + 8 merged 原料 + manifest/progress）
step "m2-jobguide" "$SRC/08、阶段八 就业指导课+拓展学习_20261025_235658/blog_jobguide" "$DST/m2-jobguide"
mkdir -p "$DST/m2-jobguide/_raw"
rsync -a --info=stats2 "${EXCLUDES[@]}" \
  --include '*_merged.md' --include 'manifest.json' --include 'stage8_progress.json' \
  --exclude '*' \
  "$SRC/08、阶段八 就业指导课+拓展学习_20261025_235658/" "$DST/m2-jobguide/_raw/" 2>&1 | tail -4 | tee -a "$LOG"

# M3：JavaEE 十大中级项目（blog 1629 + raw 双线转写 + docs 8.5M + 交接文档；跳过 materials/code 1.1G 与 wav）
step "m3-blog" "$SRC/09、赠送-JavaEE中级进修课【包含十大中级项目】/blog" "$DST/m3-javaee-10projects/blog"
step "m3-raw" "$SRC/09、赠送-JavaEE中级进修课【包含十大中级项目】/raw" "$DST/m3-javaee-10projects/raw"
step "m3-docs" "$SRC/09、赠送-JavaEE中级进修课【包含十大中级项目】/materials/docs" "$DST/m3-javaee-10projects/materials-docs"
for f in INDEX.md HANDOFF.md PROGRESS.md 安全与合规须知.md 评审报告-A-合并大篇质量.md 评审报告-B-技术栈与生产落地.md 评审报告-总览.md; do
  cp -p "$SRC/09、赠送-JavaEE中级进修课【包含十大中级项目】/$f" "$DST/m3-javaee-10projects/" 2>/dev/null
done

# M4：精英进阶六大项目（根 merged 1671 双线合并稿 + manifest；跳过 audio_line 19G / vision_line 418M）
mkdir -p "$DST/m4-advanced-6projects"
rsync -a --info=stats2 "${EXCLUDES[@]}" \
  --include '*_merged.md' --include 'manifest.json' --exclude '*' \
  "$SRC/10、赠送精英进阶【包含六大进阶项目】_20261029_122215/" "$DST/m4-advanced-6projects/" 2>&1 | tail -4 | tee -a "$LOG"

# 统一只读锁（最后一步）
find "$DST" -type d -exec chmod a-w {} + 2>/dev/null
find "$DST" -type f -exec chmod a-w {} + 2>/dev/null

echo "[$(date '+%F %T')] === 归档完成 ===" | tee -a "$LOG"
du -sh "$DST" "$DST"/* | tee -a "$LOG"
echo "md 总数: $(find "$DST" -name '*.md' | wc -l)" | tee -a "$LOG"
echo "png 总数: $(find "$DST" -name '*.png' | wc -l)" | tee -a "$LOG"
