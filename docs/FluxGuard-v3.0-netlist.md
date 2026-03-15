# FluxGuard v3.0 - KiCad 原理图网络连线清单

## 🔌 网络定义

### 电源网络
| 网络名 | 电压 | 来源 | 负载 |
|--------|------|------|------|
| VBUS | 5V | USB-C | CH340N, TP4056 |
| +5V | 5V | VBUS经过TVS | ESP32 VBATT |
| +3V3 | 3.3V | AMS1117输出 | ESP32, OLED, ATECC608A, MAX6818 |
| VBATT | 3.7-4.2V | 锂电池 | TP4056, DW01A |
| GND | 0V | 公共地 | 全部 |

### 信号网络
| 网络名 | GPIO | 功能 |
|--------|------|------|
| I2C_SDA | GPIO32 | OLED数据线 |
| I2C_SCL | GPIO33 | OLED时钟线 |
| RGB_DATA | GPIO25 | WS2812B数据 |
| BUZZER_PWM | GPIO26 | 蜂鸣器PWM |
| SEC_IRQ | GPIO27 | 安全芯片中断 |
| TARGET_TX | GPIO14 | 服务器串口TX |
| TARGET_RX | GPIO12 | 服务器串口RX |
| WDT_FEED | GPIO13 | 看门狗喂狗 |
| BTN_OK | GPIO15 | 确认按钮 |
| BTN_NEXT | GPIO4 | 切换按钮 |
| BTN_BACK | GPIO5 | 返回按钮 |
| SEC_SDA | GPIO21 | ATECC608A数据 |
| SEC_SCL | GPIO22 | ATECC608A时钟 |
| USB_TX | GPIO23 | CH340 TX |
| USB_RX | RXD0 | CH340 RX |

---

## 📐 原理图连线说明

### 1. 电源模块连线

```
USB-C (J1)
├── A4/A9/B4/B9 → VBUS
├── A6/B6 → USB_D+ → TVS1 → CH340N D+
├── A7/B7 → USB_D- → TVS1 → CH340N D-
├── A1/A12/B1/B12 → GND
└── A5/B5 → CC1/CC2 → 5.1K下拉 → GND

VBUS
├── TVS1 保护
├── CH340N VCC
├── TP4056 VCC
├── AMS1117 VIN
└── LED_PWR (红) → 1K → GND

AMS1117-3.3
├── VIN → VBUS
├── GND → GND
├── VOUT → +3V3
└── 10uF电容滤波

TP4056
├── VCC → VBUS
├── GND → GND
├── BAT → VBATT
├── PROG → 1.2K → GND (1A充电)
├── CHRG → LED_CHG (黄) → 1K → GND
└── STDBY → LED_DONE (绿) → 1K → GND

DW01A + FS8205A
├── DW01A VCC → VBATT
├── DW01A GND → GND
├── DW01A OD → FS8205A G1
├── DW01A OC → FS8205A G2
├── FS8205A S1 → VBATT+
├── FS8205A S2 → 电池负极
└── FS8205A D → GND
```

### 2. 主控模块连线

```
ESP32-WROOM-32E (U1)
├── 3V3 → +3V3
├── GND → GND (共3个GND引脚)
├── EN → 10K上拉 → +3V3, 100nF → GND
├── IO0 → 10K上拉 → +3V3 (启动模式)
│
├── IO32 (GPIO32) → I2C_SDA → 4.7K上拉 → +3V3
├── IO33 (GPIO33) → I2C_SCL → 4.7K上拉 → +3V3
│
├── IO25 (GPIO25) → RGB_DATA → WS2812B DIN
├── IO26 (GPIO26) → BUZZER_PWM → 蜂鸣器+
│
├── IO27 (GPIO27) → SEC_IRQ → ATECC608A IRQ
│
├── IO14 (GPIO14) → TARGET_TX → TVS2 → J2 Pin3
├── IO12 (GPIO12) → TARGET_RX → TVS2 → J2 Pin4
│
├── IO13 (GPIO13) → WDT_FEED → MAX6818 WDI
│
├── IO15 (GPIO15) → BTN_OK → SW1 → GND, 10K上拉 → +3V3
├── IO4 (GPIO4) → BTN_NEXT → SW2 → GND, 10K上拉 → +3V3
├── IO5 (GPIO5) → BTN_BACK → SW3 → GND, 10K上拉 → +3V3
│
├── IO21 (GPIO21) → SEC_SDA → 4.7K上拉 → +3V3
├── IO22 (GPIO22) → SEC_SCL → 4.7K上拉 → +3V3
│
├── IO23 (GPIO23) → USB_TX → CH340N RX
├── RXD0 → USB_RX → CH340N TX
│
├── TXD0 → DEBUG_TX → J3 Pin3
├── IO2 → DEBUG_LED → LED_DBG (蓝) → 1K → GND
│
└── 晶振连接
    ├── 26MHz XTAL (Y1)
    │   ├── 引脚1 → ESP32 XTAL_32P
    │   ├── 引脚2 → ESP32 XTAL_32N
    │   └── 各22pF → GND
    │
    └── 32.768kHz XTAL (Y2)
        ├── 引脚1 → ESP32 XTAL_N
        ├── 引脚2 → ESP32 XTAL_P
        └── 各10pF → GND
```

### 3. 安全模块连线

```
ATECC608A (U6)
├── VCC → +3V3
├── GND → GND
├── SDA → SEC_SDA (GPIO21)
├── SCL → SEC_SCL (GPIO22)
└── IRQ → SEC_IRQ (GPIO27), 10K上拉 → +3V3

MAX6818 (U7)
├── VCC → +3V3
├── GND → GND
├── WDI → WDT_FEED (GPIO13)
├── WDO → ESP32 EN (复位)
└── SET → GND (1.6秒超时)
```

### 4. 显示模块连线

```
OLED SSD1306 (DISP1)
├── VCC → +3V3
├── GND → GND
├── SDA → I2C_SDA (GPIO32)
├── SCL → I2C_SCL (GPIO33)
├── RES → ESP32 EN (或GPIO预留)
├── DC → GND (I2C模式)
└── CS → GND (I2C模式)

WS2812B (D1)
├── VCC → +3V3
├── GND → GND
├── DIN → RGB_DATA (GPIO25)
└── DOUT → NC (单个LED)

蜂鸣器 (BZ1)
├── + → BUZZER_PWM (GPIO26)
└── - → GND
```

### 5. 按键连线

```
BTN_OK (SW1)
├── 引脚1 → +3V3 (或GPIO15)
├── 引脚2 → GPIO15, 100nF → GND (消抖)
└── 100R串联保护

BTN_NEXT (SW2)
├── 引脚1 → +3V3 (或GPIO4)
├── 引脚2 → GPIO4, 100nF → GND
└── 100R串联保护

BTN_BACK (SW3)
├── 引脚1 → +3V3 (或GPIO5)
├── 引脚2 → GPIO5, 100nF → GND
└── 100R串联保护
```

### 6. 接口连线

```
目标服务器UART (J2, 2x5pin)
├── Pin1 → VCC (可选供电)
├── Pin2 → GND
├── Pin3 → TARGET_TX (GPIO14) → TVS2保护
├── Pin4 → TARGET_RX (GPIO12) → TVS2保护
├── Pin5 → RTS (预留)
├── Pin6 → CTS (预留)
└── Pin7-10 → NC

调试接口 (J3, 2x3pin 1.27mm)
├── Pin1 → +3V3
├── Pin2 → GND
├── Pin3 → DEBUG_TX (TXD0)
├── Pin4 → DEBUG_RX (RXD0)
├── Pin5 → EN
└── Pin6 → IO0

电池接口 (J4, JST-PH 2pin)
├── Pin1 → VBATT+
└── Pin2 → VBATT- (经DW01A/FS8205A)
```

### 7. ESD保护连线

```
TVS1 (SRV05-4) - USB保护
├── 1 → USB_D+
├── 2 → GND
├── 3 → USB_D-
├── 4 → NC
├── 5 → VBUS
└── 6 → GND

TVS2 (SRV05-4) - UART保护
├── 1 → TARGET_TX
├── 2 → GND
├── 3 → TARGET_RX
├── 4 → NC
├── 5 → VCC (如果供电)
└── 6 → GND
```

### 8. 测试点

```
TP1 → +3V3 (电源测试)
TP2 → +5V (USB电源测试)
TP3 → VBATT (电池电压测试)
TP4 → GND (地测试)
TP5 → I2C_SDA (调试)
TP6 → I2C_SCL (调试)
TP7 → TARGET_TX (串口调试)
TP8 → TARGET_RX (串口调试)
```

### 9. LED指示灯

```
LED_PWR (红)
├── + → VBUS
└── - → 1K → GND

LED_CHG (黄) - 充电中
├── + → TP4056 CHRG
└── - → 1K → GND

LED_DONE (绿) - 充电完成
├── + → TP4056 STDBY
└── - → 1K → GND

LED_DBG (蓝) - 调试状态
├── + → GPIO2
└── - → 1K → GND

LED_STATUS (RGB) - WS2812B
├── VCC → +3V3
├── GND → GND
└── DIN → GPIO25
```

---

## 📋 去耦电容布局

| 位置 | 电容 | 数值 | 连接 |
|------|------|------|------|
| U1 每3V3引脚 | C1-C4 | 100nF | 3V3-GND |
| U2 VCC | C5 | 100nF | VBUS-GND |
| U3 VIN | C6 | 10uF | VBUS-GND |
| U3 VOUT | C7 | 22uF | 3V3-GND |
| U4 VCC | C8 | 10uF | VBUS-GND |
| U4 BAT | C9 | 10uF | VBATT-GND |
| U6 VCC | C10 | 100nF | 3V3-GND |
| U7 VCC | C11 | 100nF | 3V3-GND |
| DISP1 VCC | C12 | 100nF | 3V3-GND |
| D1 VCC | C13 | 100nF | 3V3-GND |
| Y1 | C14-C15 | 22pF | 晶振-GND |
| Y2 | C16-C17 | 10pF | 晶振-GND |

---

## ⚠️ 设计注意事项

1. **电源走线**：+3V3和GND走线宽度≥20mil
2. **I2C上拉**：SDA/SCL必须加4.7K上拉电阻
3. **晶振布局**：尽量靠近ESP32，走线短且等长
4. **ESD保护**：TVS管尽量靠近接口
5. **去耦电容**：尽量靠近芯片电源引脚
6. **电池保护**：DW01A+FS8205A必须放在电池和负载之间
7. **看门狗**：WDO连接到ESP32的EN引脚实现硬件复位

---

**生成时间**: 2026-03-15 18:50 (UTC+8)
