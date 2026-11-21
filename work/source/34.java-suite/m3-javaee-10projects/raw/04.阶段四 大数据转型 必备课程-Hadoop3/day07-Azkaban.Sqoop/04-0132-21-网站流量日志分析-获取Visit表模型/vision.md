# 画面线理解：21-网站流量日志分析-获取Visit表模型

- 阶段：04.阶段四 大数据转型 必备课程-Hadoop3
- 章节：day07-Azkaban.Sqoop
- 源文件：04.阶段四 大数据转型 必备课程-Hadoop3\day07-Azkaban.Sqoop\21-网站流量日志分析-获取Visit表模型【海量资源尽在 ubkz.com】.mp4
- 抽帧：14 帧 @ 00:43, 01:09, 01:56, 02:33, 03:37, 03:54, 04:08, 04:56, 05:18, 05:38, 05:51, 06:05, 06:18, 06:23
- 模型：Qwen3-VL-8B-Instruct-Q4_K_M
- 生成时间：2026-10-28 10:19:45

1) 这一组画面整体在讲如何通过 MapReduce 程序将原始点击流日志数据（session 级别）转换为 visit 表模型，以便进行后续的用户行为分析。

2) 按时间顺序列出每张画面的要点：
画面001: 展示了原始的 session 数据结构，包含 session ID、IP、访问时间、页面、时长等信息，并用箭头指向 session003 的数据行，说明其包含两个页面访问记录。
画面002: 与画面001类似，但箭头指向 session003 的第二个页面访问记录，强调 session 会话中包含多个页面访问。
画面003: 在 IntelliJ IDEA 中展示 ClickStreamPageView.java 文件，其中包含 job.setMapOutputValueClass(PageViewsBean.class)、job.setOutputKeyClass(NullWritable.class)、job.setOutputValueClass(VisitBean.class) 等配置，以及 ClickStreamVisitMapper 类的 map 方法，用于将原始日志行解析为 PageViewsBean 对象。
画面004: 与画面003 类似，但高亮显示了 ClickStreamVisitMapper 类中 map 方法的代码，特别是将字段赋值给 pvBean 对象的部分。
画面005: 与画面004 类似，但高亮显示了 map 方法中设置 pvBean 的 session 字段的代码：pvBean.setSession(session);。
画面006: 展示 ClickStreamVisitReducer 类的 reduce 方法，用于对 PageViewsBean 对象进行聚合处理。
画面007: 与画面006 类似，但高亮显示了 reduce 方法中用于对 PageViewsBean 列表进行排序的 Comparator 比较器代码：return o1.getStep() > o2.getStep() ? 1 : -1;。
画面008: 与画面007 类似，但高亮显示了 reduce 方法中创建 VisitBean 并设置其属性的代码，包括 visitBean.setPageVisits(pvBeansList.size());。
画面009: 展示了 PPT 页面，标题为“3.1 点击流模型 pageviews 表”，内容包括 Pageviews 表模型数据生成的代码示例和数据格式说明。
画面010: 展示了 Hadoop 输出目录下的 part-r-00000 文件，右键菜单显示“编辑 with Notepad++”选项。
画面011: 展示了 Notepad++ 中打开的 part-r-00000 文件内容，显示了经过 MapReduce 处理后的数据，包含 session ID、IP、时间戳、页面路径、URL 等字段。
画面012: 与画面011 类似，但显示了 part-r-00000 文件中更详细的数据行，包含具体的页面路径和 URL。
画面013: 展示了 PPT 页面，标题为“3.1 点击流模型 pageviews 表”，内容包括 Pageviews 表模型数据生成的代码示例和数据格式说明。
画面014: 展示了 PPT 页面，标题为“3.1 点击流模型 pageviews 表”，内容包括一个架构图，显示了从 Web 系统到 HDFS、MapReduce、Hive、Sqoop 最终到 MySQL 的数据处理流程。

3) 代码、配置、命令、目录结构、SQL、XML/YAML 配置（原样抄录）：
画面003:
job.setMapOutputValueClass(PageViewsBean.class);
job.setOutputKeyClass(NullWritable.class);
job.setOutputValueClass(VisitBean.class);
boolean res = job.waitForCompletion(true);
return res==0;

// 以session作为key，发送数据给reducer
static class ClickStreamVisitMapper extends Mapper<LongWritable, Text, Text, PageViewsBean> {
    PageViewsBean pvBean = new PageViewsBean();
    Text k = new Text();
    @Override
    protected void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String[] fields = line.split("\t");
        int step = Integer.parseInt(fields[5]);
        // (string session, string remote_addr, string request, int step, string stayLong, string referer, string url, string timeStr)
        pvBean.set(fields[0], fields[1], fields[2], fields[3], fields[4], step, fields[6], fields[7], fields[8], fields[9]);
        k.set(pvBean.getSession());
        context.write(k, pvBean);
    }
}

画面006:
static class ClickStreamVisitReducer extends Reducer<Text, PageViewsBean, NullWritable, VisitBean> {
    @Override
    protected void reduce(Text session, Iterable<PageViewsBean> pvBeans, Context context) throws IOException, InterruptedException {
        // 将pvBeans按step排序
        ArrayList<PageViewsBean> pvBeansList = new ArrayList<PageViewsBean>();
        for (PageViewsBean pvBean : pvBeans) {
            PageViewsBean bean = new PageViewsBean();
            try {
                BeanUtils.copyProperties(bean, pvBean);
                pvBeansList.add(bean);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        Collections.sort(pvBeansList, new Comparator<PageViewsBean>() {
            @Override
            public int compare(PageViewsBean o1, PageViewsBean o2) {
                return o1.getStep() > o2.getStep() ? 1 : -1;
            }
        });
        // 取这次visit的所有pageview记录，将数据放入VisitBean中
        VisitBean visitBean = new VisitBean();
        // 取visit的首记录
        visitBean.setInPage(pvBeansList.get(0).getRequest());
        visitBean.setInTime(pvBeansList.get(0).getTimeStr());
        // 取visit的尾记录
        visitBean.setOutPage(pvBeansList.get(pvBeansList.size() - 1).getRequest());
        visitBean.setOutTime(pvBeansList.get(pvBeansList.size() - 1).getTimeStr());
        // visit访问的页面数
        visitBean.setPageVisits(pvBeansList.size());
        // 来访者的ip
        visitBean.setRemote_addr(pvBeansList.get(0).getRemote_addr());
        // 本次visit的referer
        visitBean.setReferal(pvBeansList.get(0).getReferal());
        visitBean.setSession(session.toString());
        context.write(NullWritable.get(), visitBean);
    }
}

4) PPT 标题、架构图/流程图的结构（谁指向谁）、表格数据：
画面014:
架构图结构：
- Web 系统 → HDFS
- HDFS → MapReduce
- MapReduce → Hive
- Hive → Sqoop
- Sqoop → MySQL

5) 无
