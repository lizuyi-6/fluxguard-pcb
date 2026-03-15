# FluxGuard v3.0 PCB设计文件

**版本**: 3.0  
**日期**: 2026-03-15  
**设计**: 杭州视界奇点科技有限公司

---

## 📦 文件清单

| 文件 | 说明 |
|------|------|
| `FluxGuard-v3.0.kicad_pro` | KiCad 项目文件 |
| `FluxGuard-v3.0.kicad_sch` | 原理图 (74元件, 已连线) |
| `FluxGuard-v3.0.kicad_pcb` | PCB布局文件 |
| `FluxGuard-v3.0-bom.csv` | BOM表 (58元件) |
| `FluxGuard-v3.0-netlist.md` | 网络连线清单 |
| `FluxGuard-v3.0-wiring-guide.md` | 连线指南 |

---

## 📊 设计规格

| 项目 | 规格 |
|------|------|
| PCB尺寸 | 52mm x 29mm |
| 层数 | 4层 |
| 板厚 | 1.6mm |
| 表面处理 | ENIG |
| 主控 | ESP32-WROOM-32E |
| 元件数 | 74个 |

---

## 🔌 主要模块

### 1. 电源管理
- USB-C 16pin 输入
- TP4056 锂电池充电 (1A)
- DW01A + FS8205A 电池保护
- AMS1117-3.3 稳压

### 2. 主控
- ESP32-WROOM-32E (WiFi + BT)
- 26MHz 主晶振
- 32.768kHz RTC晶振

### 3. 安全模块
- ATECC608A 硬件加密芯片
- MAX6818 硬件看门狗

### 4. 显示与交互
- 0.96" OLED SSD1306 (I2C)
- WS2812B-2020 RGB LED
- MLT-8530 有源蜂鸣器
- 3x 轻触按键 (OK/NEXT/BACK)

### 5. 通信接口
- CH340N USB转串口
- 目标服务器UART (2x5pin)
- 调试接口 (2x3pin 1.27mm)

### 6. ESD保护
- SRV05-4 x2 (USB + UART)

---

## 🔌 GPIO分配

| GPIO | 功能 | 连接 |
|------|------|------|
| GPIO32 | I2C_SDA | OLED |
| GPIO33 | I2C_SCL | OLED |
| GPIO25 | RGB_DATA | WS2812B |
| GPIO26 | BUZZER | 蜂鸣器 |
| GPIO27 | SEC_IRQ | ATECC608A |
| GPIO14 | TARGET_TX | 服务器串口 |
| GPIO12 | TARGET_RX | 服务器串口 |
| GPIO13 | WDT_FEED | 看门狗 |
| GPIO15 | BTN_OK | 确认按钮 |
| GPIO4 | BTN_NEXT | 切换按钮 |
| GPIO5 | BTN_BACK | 返回按钮 |
| GPIO21 | SEC_SDA | ATECC608A |
| GPIO22 | SEC_SCL | ATECC608A |
| GPIO23 | USB_TX | CH340N |
| RXD0 | USB_RX | CH340N |

---

## 🔧 使用方法

1. 克隆仓库
```bash
git clone https://github.com/lizuyi-6/fluxguard-pcb.git
```

2. 用 KiCad 打开项目
```bash
cd fluxguard-pcb
kicad FluxGuard-v3.0.kicad_pro
```

3. 检查原理图连线
4. 完成PCB布局
5. 生成Gerber文件
6. 提交打样

---

## 📋 生产要求

### PCB规格
- 层数: 4层
- 板厚: 1.6mm
- 铜厚: 1oz (外层) / 0.5oz (内层)
- 表面处理: ENIG
- 阻焊: 黑色
- 丝印: 白色

### 推荐厂商
- 嘉立创 (4层板)
- 捷配
- 立创EDA

---

## 📄 License

MIT License

---

**生成时间**: 2026-03-15 19:28 (UTC+8)
