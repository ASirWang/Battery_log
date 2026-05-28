import re
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates

# 解析日志文件
log_data = """[2026-05-28 10:14:43]  ..\Writer\Power\battery_interface.c: 2162: 90,   8084, 11768, 687
[2026-05-28 10:14:43]  ..\Writer\Power\battery_interface.c: 2162: 90,   7980, 11770, 678
[2026-05-28 10:14:44]  ..\Writer\Power\battery_interface.c: 2162: 90,   7980, 11770, 678
[2026-05-28 10:14:44]  ..\Writer\Power\battery_interface.c: 2162: 90,   8086, 11771, 687
[2026-05-28 10:14:45]  ..\Writer\Power\battery_interface.c: 2162: 90,   8085, 11770, 687
[2026-05-28 10:14:45]  ..\Writer\Power\battery_interface.c: 2162: 90,   8086, 11771, 687
[2026-05-28 10:14:46]  ..\Writer\Power\battery_interface.c: 2162: 90,   7980, 11770, 678
[2026-05-28 10:14:46]  ..\Writer\Power\battery_interface.c: 2162: 90,   8085, 11770, 687
[2026-05-28 10:14:47]  ..\Writer\Power\battery_interface.c: 2162: 90,   8084, 11768, 687
[2026-05-28 10:14:47]  ..\Writer\Power\battery_interface.c: 2162: 90,   7980, 11771, 678
[2026-05-28 10:14:48]  ..\Writer\Power\battery_interface.c: 2162: 90,   7979, 11769, 678
[2026-05-28 10:14:48]  ..\Writer\Power\battery_interface.c: 2162: 90,   7980, 11771, 678
[2026-05-28 10:14:49]  ..\Writer\Power\battery_interface.c: 2162: 90,   8084, 11768, 687
[2026-05-28 10:14:49]  ..\Writer\Power\battery_interface.c: 2162: 90,   7979, 11769, 678
[2026-05-28 10:14:50]  ..\Writer\Power\battery_interface.c: 2162: 90,   8625, 11767, 733
[2026-05-28 10:14:50]  ..\Writer\Power\battery_interface.c: 2162: 90,   11206, 11759, 953
[2026-05-28 10:14:51]  ..\Writer\Power\battery_interface.c: 2162: 90,   24731, 11573, 2137
[2026-05-28 10:14:51]  ..\Writer\Power\battery_interface.c: 2162: 90,   22256, 11610, 1917
[2026-05-28 10:14:52]  ..\Writer\Power\battery_interface.c: 2162: 90,   22676, 11611, 1953
[2026-05-28 10:14:52]  ..\Writer\Power\battery_interface.c: 2162: 90,   19239, 11653, 1651
[2026-05-28 10:14:53]  ..\Writer\Power\battery_interface.c: 2162: 90,   19240, 11654, 1651
[2026-05-28 10:14:53]  ..\Writer\Power\battery_interface.c: 2162: 90,   22654, 11600, 1953
[2026-05-28 10:14:54]  ..\Writer\Power\battery_interface.c: 2162: 90,   19244, 11656, 1651
[2026-05-28 10:14:54]  ..\Writer\Power\battery_interface.c: 2162: 90,   19011, 11649, 1632
[2026-05-28 10:14:55]  ..\Writer\Power\battery_interface.c: 2162: 90,   18283, 11594, 1577
[2026-05-28 10:14:56]  ..\Writer\Power\battery_interface.c: 2162: 90,   21581, 11653, 1852
[2026-05-28 10:14:56]  ..\Writer\Power\battery_interface.c: 2162: 90,   19009, 11648, 1632
[2026-05-28 10:14:57]  ..\Writer\Power\battery_interface.c: 2162: 90,   19231, 11585, 1660
[2026-05-28 10:14:57]  ..\Writer\Power\battery_interface.c: 2162: 90,   22628, 11640, 1944
[2026-05-28 10:14:58]  ..\Writer\Power\battery_interface.c: 2162: 90,   19097, 11638, 1641
[2026-05-28 10:14:58]  ..\Writer\Power\battery_interface.c: 2162: 90,   18076, 11595, 1559
[2026-05-28 10:14:59]  ..\Writer\Power\battery_interface.c: 2162: 90,   21681, 11644, 1862
[2026-05-28 10:14:59]  ..\Writer\Power\battery_interface.c: 2162: 90,   17945, 11578, 1550
[2026-05-28 10:15:00]  ..\Writer\Power\battery_interface.c: 2162: 90,   20469, 11624, 1761
[2026-05-28 10:15:00]  ..\Writer\Power\battery_interface.c: 2162: 90,   19930, 11621, 1715
[2026-05-28 10:15:01]  ..\Writer\Power\battery_interface.c: 2162: 90,   24273, 11559, 2100
[2026-05-28 10:15:01]  ..\Writer\Power\battery_interface.c: 2162: 90,   19294, 11623, 1660
[2026-05-28 10:15:02]  ..\Writer\Power\battery_interface.c: 2162: 90,   18145, 11639, 1559
[2026-05-28 10:15:02]  ..\Writer\Power\battery_interface.c: 2162: 90,   21747, 11568, 1880
[2026-05-28 10:15:03]  ..\Writer\Power\battery_interface.c: 2162: 90,   18351, 11637, 1577
[2026-05-28 10:15:03]  ..\Writer\Power\battery_interface.c: 2162: 90,   18559, 11629, 1596
[2026-05-28 10:15:04]  ..\Writer\Power\battery_interface.c: 2162: 90,   27858, 11507, 2421
[2026-05-28 10:15:04]  ..\Writer\Power\battery_interface.c: 2162: 90,   19179, 11617, 1651
[2026-05-28 10:15:05]  ..\Writer\Power\battery_interface.c: 2162: 90,   18120, 11623, 1559
[2026-05-28 10:15:06]  ..\Writer\Power\battery_interface.c: 2162: 90,   18849, 11550, 1632
[2026-05-28 10:15:06]  ..\Writer\Power\battery_interface.c: 2162: 90,   22486, 11621, 1935
[2026-05-28 10:15:07]  ..\Writer\Power\battery_interface.c: 2162: 90,   18749, 11617, 1614
[2026-05-28 10:15:07]  ..\Writer\Power\battery_interface.c: 2162: 90,   18212, 11549, 1577
[2026-05-28 10:15:08]  ..\Writer\Power\battery_interface.c: 2162: 90,   21423, 11624, 1843
[2026-05-28 10:15:08]  ..\Writer\Power\battery_interface.c: 2162: 90,   18958, 11617, 1632
[2026-05-28 10:15:09]  ..\Writer\Power\battery_interface.c: 2162: 90,   19055, 11542, 1651
[2026-05-28 10:15:09]  ..\Writer\Power\battery_interface.c: 2162: 90,   22459, 11607, 1935
[2026-05-28 10:15:10]  ..\Writer\Power\battery_interface.c: 2162: 90,   18950, 11548, 1641
[2026-05-28 10:15:10]  ..\Writer\Power\battery_interface.c: 2162: 89,   18220, 11620, 1568
[2026-05-28 10:15:11]  ..\Writer\Power\battery_interface.c: 2162: 89,   18224, 11623, 1568
[2026-05-28 10:15:11]  ..\Writer\Power\battery_interface.c: 2162: 89,   21693, 11539, 1880
[2026-05-28 10:15:12]  ..\Writer\Power\battery_interface.c: 2162: 89,   20544, 11607, 1770
[2026-05-28 10:15:12]  ..\Writer\Power\battery_interface.c: 2162: 89,   19791, 11601, 1706
[2026-05-28 10:15:13]  ..\Writer\Power\battery_interface.c: 2162: 89,   23773, 11518, 2064
[2026-05-28 10:15:13]  ..\Writer\Power\battery_interface.c: 2162: 89,   19262, 11604, 1660
[2026-05-28 10:15:14]  ..\Writer\Power\battery_interface.c: 2162: 89,   18006, 11617, 1550
[2026-05-28 10:15:14]  ..\Writer\Power\battery_interface.c: 2162: 89,   22099, 11528, 1917
[2026-05-28 10:15:15]  ..\Writer\Power\battery_interface.c: 2162: 89,   18421, 11615, 1586
[2026-05-28 10:15:16]  ..\Writer\Power\battery_interface.c: 2162: 89,   26494, 11600, 2284
[2026-05-28 10:15:16]  ..\Writer\Power\battery_interface.c: 2162: 89,   19133, 11526, 1660
[2026-05-28 10:15:17]  ..\Writer\Power\battery_interface.c: 2162: 89,   22658, 11602, 1953
[2026-05-28 10:15:17]  ..\Writer\Power\battery_interface.c: 2162: 89,   19055, 11612, 1641
[2026-05-28 10:15:18]  ..\Writer\Power\battery_interface.c: 2162: 89,   19129, 11524, 1660
[2026-05-28 10:15:18]  ..\Writer\Power\battery_interface.c: 2162: 89,   22357, 11608, 1926
[2026-05-28 10:15:19]  ..\Writer\Power\battery_interface.c: 2162: 89,   19159, 11605, 1651
[2026-05-28 10:15:19]  ..\Writer\Power\battery_interface.c: 2162: 89,   18085, 11601, 1559
[2026-05-28 10:15:20]  ..\Writer\Power\battery_interface.c: 2162: 89,   23276, 11592, 2008
[2026-05-28 10:15:20]  ..\Writer\Power\battery_interface.c: 2162: 89,   19310, 11508, 1678
[2026-05-28 10:15:21]  ..\Writer\Power\battery_interface.c: 2162: 89,   20184, 11587, 1742
[2026-05-28 10:15:21]  ..\Writer\Power\battery_interface.c: 2162: 89,   16940, 11619, 1458
[2026-05-28 10:15:22]  ..\Writer\Power\battery_interface.c: 2162: 89,   17468, 11615, 1504
[2026-05-28 10:15:22]  ..\Writer\Power\battery_interface.c: 2162: 89,   17046, 11620, 1467
[2026-05-28 10:15:23]  ..\Writer\Power\battery_interface.c: 2162: 89,   16943, 11621, 1458
[2026-05-28 10:15:23]  ..\Writer\Power\battery_interface.c: 2162: 89,   16732, 11620, 1440
[2026-05-28 10:15:24]  ..\Writer\Power\battery_interface.c: 2162: 89,   15441, 11619, 1329
[2026-05-28 10:15:24]  ..\Writer\Power\battery_interface.c: 2162: 89,   8141, 11698, 696
[2026-05-28 10:15:25]  ..\Writer\Power\battery_interface.c: 2162: 89,   8143, 11700, 696
[2026-05-28 10:15:25]  ..\Writer\Power\battery_interface.c: 2162: 89,   8144, 11702, 696
[2026-05-28 10:15:26]  ..\Writer\Power\battery_interface.c: 2162: 89,   8145, 11704, 696
[2026-05-28 10:15:27]  ..\Writer\Power\battery_interface.c: 2162: 89,   8264, 11706, 706"""

timestamps = []
primary_values = []   # 冒号后的第一个数值（电池百分比）
secondary_values = [] # 第一个逗号前的数值（功率/能量值）

pattern = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\].*2162:\s*(\d+),\s*(\d+),'

for match in re.finditer(pattern, log_data):
    timestamp_str = match.group(1)
    primary = int(match.group(2))
    secondary = int(match.group(3))
    
    timestamps.append(datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S'))
    primary_values.append(primary)
    secondary_values.append(secondary)

# 创建双坐标轴图表
fig, ax1 = plt.subplots(figsize=(14, 8))

# 主轴（蓝色）：电池百分比
color1 = 'tab:blue'
ax1.set_xlabel('时间', fontsize=12, fontweight='bold')
ax1.set_ylabel('电池百分比 (%)', color=color1, fontsize=12, fontweight='bold')
line1 = ax1.plot(timestamps, primary_values, color=color1, marker='o', markersize=5, 
                 label='电池百分比', linewidth=2.5, linestyle='-')
ax1.tick_params(axis='y', labelcolor=color1)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.set_ylim(88, 91)

# 次轴（橙色）：功率/能量值
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel('功率/能量值 (mW)', color=color2, fontsize=12, fontweight='bold')
line2 = ax2.plot(timestamps, secondary_values, color=color2, marker='s', markersize=5, 
                 label='功率/能量值', linewidth=2.5, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color2)

# 格式化x轴（时间）
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
ax1.xaxis.set_major_locator(mdates.SecondLocator(interval=3))
plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')

# 标题和图例
plt.title('电池接口日志分析\n201-018_10mm_Normal_DigitalRhythm', 
          fontsize=14, fontweight='bold', pad=20)
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper left', fontsize=11, framealpha=0.9)

plt.tight_layout()
plt.savefig('battery_analysis_chart.png', dpi=300, bbox_inches='tight')
print("✓ 图表已保存为 'battery_analysis_chart.png'")
print(f"\n📊 数据统计（共 {len(timestamps)} 个数据点）：")
print(f"\n电池百分比 (%)：")
print(f"  最小值: {min(primary_values)}%, 最大值: {max(primary_values)}%, 平均值: {sum(primary_values)/len(primary_values):.1f}%")
print(f"\n功率/能量值 (mW)：")
print(f"  最小值: {min(secondary_values)} mW")
print(f"  最大值: {max(secondary_values)} mW")
print(f"  平均值: {sum(secondary_values)/len(secondary_values):.0f} mW")
print(f"\n时间范围：{timestamps[0].strftime('%H:%M:%S')} ~ {timestamps[-1].strftime('%H:%M:%S')}")