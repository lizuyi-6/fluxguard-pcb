# FluxGuard v3.0 - KiCad 手动连线指南

## 🎯 快速开始

1. 打开 KiCad，加载项目 `FluxGuard-v3.0.kicad_pro`
2. 打开原理图编辑器 (Eeschema)
3. 按照本指南逐个连线

---

## 📐 连线顺序（建议）

### 第一步：电源网络

| 网络名 | 颜色 | 连接 |
|--------|------|------|
| **VBUS** | 红色 | J1-A4/A9/B4/B9 → U2-VCC → U4-VCC → U3-VIN → TVS1-5 |
| **+3V3** | 橙色 | U3-VOUT → U1-3V3 → U6-VCC → U7-VCC → DISP1-VCC → D1-VCC |
| **VBATT** | 黄色 | U4-BAT → U5-VCC → Q1-S1 → J4-1 |
| **GND** | 黑色 | 所有GND引脚 → 公共地 |

### 第二步：USB通信

| 网络 | 连接 |
|------|------|
| USB_D+ | J1-A6/B6 → TVS1-1 → U2-D+ |
| USB_D- | J1-A7/B7 → TVS1-3 → U2-D- |
| USB_TX | U2-TX → U1-GPIO23 |
| USB_RX | U2-RX → U1-RXD0 |

### 第三步：I2C总线

| 网络 | 连接 | 上拉 |
|------|------|------|
| **I2C_SDA** | U1-GPIO32 → DISP1-SDA | 4.7K → +3V3 |
| **I2C_SCL** | U1-GPIO33 → DISP1-SCL | 4.7K → +3V3 |
| **SEC_SDA** | U1-GPIO21 → U6-SDA | 4.7K → +3V3 |
| **SEC_SCL** | U1-GPIO22 → U6-SCL | 4.7K → +3V3 |

### 第四步：显示与交互

| 网络 | 连接 |
|------|------|
| RGB_DATA | U1-GPIO25 → D1-DIN |
| BUZZER_PWM | U1-GPIO26 → BZ1-+ |
| BTN_OK | U1-GPIO15 → SW1-2 (10K上拉+100nF消抖) |
| BTN_NEXT | U1-GPIO4 → SW2-2 (10K上拉+100nF消抖) |
| BTN_BACK | U1-GPIO5 → SW3-2 (10K上拉+100nF消抖) |

### 第五步：服务器通信

| 网络 | 连接 |
|------|------|
| TARGET_TX | U1-GPIO14 → TVS2-1 → J2-3 |
| TARGET_RX | U1-GPIO12 → TVS2-3 → J2-4 |

### 第六步：安全模块

| 网络 | 连接 |
|------|------|
| SEC_IRQ | U6-IRQ → U1-GPIO27 (10K上拉) |
| WDT_FEED | U1-GPIO13 → U7-WDI |
| WDT_RST | U7-WDO → U1-EN |

### 第七步：电池管理

| 网络 | 连接 |
|------|------|
| CHRG_IND | U4-CHRG → LED_Y → 1K → GND |
| STDBY_IND | U4-STDBY → LED_G → 1K → GND |
| PROG | U4-PROG → 1.2K → GND |

---

## 🔧 快捷键

| 操作 | 快捷键 |
|------|--------|
| 添加导线 | W |
| 添加标签 | L |
| 添加电源 | P |
| 添加接地 | G |
| 移动元件 | M |
| 复制元件 | C |
| 旋转元件 | R |
| 镜像元件 | X/Y |
| 删除 | Del |

---

## ⚠️ 常见问题

### 1. 网络未连接
- 检查标签是否一致（区分大小写）
- 确保导线连接到引脚中心

### 2. 电源符号未找到
- 使用 `P` 快捷键添加电源符号
- 选择 `+3V3`、`VBUS`、`GND` 等

### 3. 元件封装缺失
- 双击元件 → 选择正确封装
- 参考 `FluxGuard-v3.0-bom.csv`

---

## 📋 检查清单

- [ ] 电源网络完整
- [ ] I2C上拉电阻
- [ ] 按键消抖电容
- [ ] ESD保护TVS
- [ ] 去耦电容布局
- [ ] 网络标签一致
- [ ] ERC检查通过

---

**生成时间**: 2026-03-15 18:52 (UTC+8)
