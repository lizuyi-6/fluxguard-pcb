# KiCad 操作指南 - FluxGuard v3.0

## 🚀 第一步：打开项目

1. 打开 KiCad
2. 点击 **File → Open Project**
3. 选择 `FluxGuard-v3.0.kicad_pro`
4. 项目窗口会显示文件列表

---

## 📐 第二步：查看原理图

1. 在项目窗口，点击 **Schematic Editor** 图标（或按 `E`）
2. 会打开 Eeschema 原理图编辑器
3. 你会看到所有元件（74个）和连线（27条）

### 原理图检查清单
- [ ] 检查所有元件是否显示
- [ ] 检查网络标签是否正确
- [ ] 运行 ERC 检查

### 运行 ERC（电气规则检查）
1. 点击 **Inspect → Electrical Rules Checker**
2. 点击 **Run ERC**
3. 查看是否有错误或警告

---

## 🔧 第三步：分配封装

在原理图中为元件分配正确的封装：

1. 双击任意元件
2. 在属性对话框中，点击 **Footprint** 栏的浏览按钮
3. 选择正确的封装

### 关键元件封装列表

| 元件 | 封装 |
|------|------|
| ESP32-WROOM-32E | `RF_Module:ESP32-WROOM-32` |
| CH340N | `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` |
| AMS1117-3.3 | `Package_TO_SOT_SMD:SOT-223-3_TabPin2` |
| TP4056 | `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` |
| DW01A | `Package_TO_SOT_SMD:SOT-23-6` |
| FS8205A | `Package_SO:TSSOP-8_4.4x3mm_P0.65mm` |
| ATECC608A | `Package_SO:SOIC-8_3.9x4.9mm_P1.27mm` |
| MAX6818 | `Package_TO_SOT_SMD:SOT-23-5` |
| WS2812B | `LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm` |
| USB-C | `Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12_2x6_P0.5mm_Horizontal` |
| 电容 100nF | `Capacitor_SMD:C_0603_1608Metric` |
| 电阻 10K | `Resistor_SMD:R_0603_1608Metric` |

---

## 📦 第四步：生成网表

1. 在原理图编辑器中，点击 **Tools → Generate Netlist**
2. 选择 **PCBNew** 格式
3. 点击 **Generate Netlist**
4. 保存为 `FluxGuard-v3.0.net`

---

## 🖨️ 第五步：打开 PCB 编辑器

1. 回到项目窗口
2. 点击 **PCB Editor** 图标（或按 `P`）
3. 会打开 PCBNew 编辑器

---

## 📥 第六步：导入网表

1. 在 PCB 编辑器中，点击 **File → Import Netlist**
2. 选择 `FluxGuard-v3.0.net`
3. 点击 **Import**
4. 所有元件会堆叠在一起

---

## 📍 第七步：布局元件

### 布局原则
1. **电源模块** 放在左侧（USB入口）
2. **主控模块** 放在中央
3. **显示模块** 放在右侧
4. **接口** 放在边缘

### 操作方法
1. 按 `M` 键，点击元件移动
2. 按 `R` 键旋转元件
3. 按 `F` 键翻转到背面
4. 按 `Del` 删除

### 布局顺序
1. 先放 **USB-C** (左上角)
2. 放 **ESP32** (中央)
3. 放 **电源管理** (左侧)
4. 放 **OLED** (右侧)
5. 放 **按键** (右下)
6. 放 **接口** (边缘)

---

## 🔌 第八步：布线

### 布线规则
| 网络 | 线宽 | 层 |
|------|------|-----|
| VBUS | 0.4mm | F.Cu |
| +3V3 | 0.4mm | F.Cu |
| GND | 0.4mm | In1.Cu (整层铺铜) |
| 信号线 | 0.2mm | F.Cu / B.Cu |

### 布线操作
1. 按 `X` 键开始布线
2. 点击元件焊盘开始
3. 移动鼠标拉线
4. 按 `V` 添加过孔
5. 点击目标焊盘结束

### 快捷键
| 操作 | 快捷键 |
|------|--------|
| 布线 | `X` |
| 移动 | `M` |
| 旋转 | `R` |
| 删除 | `Del` |
| 添加过孔 | `V` |
| 切换层 | `+` / `-` |
| 缩放 | 滚轮 |
| 平移 | 右键拖动 |

---

## 🟩 第九步：铺铜

1. 点击 **Add Filled Zone** 工具
2. 在 PCB 周围画一个框
3. 选择 **GND** 网络
4. 选择 **In1.Cu** 层
5. 重复 **F.Cu** 和 **B.Cu** 层

---

## 📏 第十步：设计规则检查 (DRC)

1. 点击 **Inspect → Design Rules Checker**
2. 点击 **Run DRC**
3. 查看并修复所有错误

---

## 📤 第十一步：生成 Gerber

1. 点击 **File → Plot**
2. 选择输出目录
3. 勾选需要生成的层：
   - F.Cu
   - B.Cu
   - In1.Cu
   - In2.Cu
   - F.Paste
   - B.Paste
   - F.SilkS
   - B.SilkS
   - F.Mask
   - B.Mask
   - Edge.Cuts
4. 点击 **Plot**

### 生成钻孔文件
1. 点击 **Generate Drill Files**
2. 选择 **PTH and NPTH**
3. 点击 **Generate**

---

## 🏭 第十二步：打样

### 推荐厂商
| 厂商 | 网站 | 价格参考 |
|------|------|----------|
| 嘉立创 | jlc.com | 5片/50元 |
| 捷配 | jiepei.com | 5片/30元 |
| 立创EDA | lceda.cn | 5片/50元 |

### 提交文件
- Gerber 文件夹（压缩）
- 钻孔文件
- BOM 表（可选）
- 坐标文件（可选）

---

## ⚠️ 常见问题

### 1. 元件找不到封装
- 下载 KiCad 官方库
- 或者自己创建封装

### 2. 网表导入失败
- 检查原理图 ERC
- 确保所有元件有唯一标识

### 3. DRC 报错
- 线距太近：调整走线
- 焊盘间距：调整元件位置
- 未连接：检查网表

### 4. 无法布线
- 检查层是否正确
- 检查网络是否连接

---

**生成时间**: 2026-03-15 19:38 (UTC+8)
