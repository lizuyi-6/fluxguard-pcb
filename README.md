# FluxGuard v3.0 PCB 设计

**版本**: 3.0  
**日期**: 2026-03-15  
**设计**: 杭州视界奇点科技有限公司

---

## 📁 目录结构

```
pcb/
├── kicad/                          # KiCad 源文件
│   ├── FluxGuard-v3.0.kicad_pro    # 项目文件
│   ├── FluxGuard-v3.0.kicad_sch    # 原理图
│   ├── FluxGuard-v3.0.kicad_pcb    # PCB布局
│   ├── generate_schematic.py       # 原理图生成脚本
│   ├── generate_wiring.py          # 连线生成脚本
│   └── gen_kicad9.py               # KiCad 9.0 生成脚本
│
├── docs/                           # 文档
│   ├── FluxGuard-PCB-v3.0.md       # 设计规格
│   ├── FluxGuard-v3.0-bom.csv      # BOM表 (58元件)
│   ├── FluxGuard-v3.0-netlist.md   # 网络连线清单
│   ├── FluxGuard-v3.0-wiring-guide.md  # 连线指南
│   ├── FluxGuard-v3.0-tutorial.md  # KiCad操作教程
│   └── FluxGuard-v3.0-meta.json    # 元数据
│
├── gerber/                         # Gerber 输出 (待生成)
│
└── production/                     # 生产文件 (待生成)
```

---

## 📊 设计规格

| 项目 | 规格 |
|------|------|
| PCB尺寸 | 52mm × 29mm |
| 层数 | 4层 |
| 板厚 | 1.6mm |
| 表面处理 | ENIG |
| 主控 | ESP32-WROOM-32E |
| 元件数 | 74个 |

---

## 🔌 模块清单

| 模块 | 主要元件 |
|------|----------|
| **电源** | USB-C, TP4056, AMS1117-3.3, DW01A |
| **主控** | ESP32-WROOM-32E |
| **安全** | ATECC608A, MAX6818 |
| **显示** | OLED, WS2812B, 蜂鸣器 |
| **接口** | UART, 调试口, 电池接口 |

---

## 📥 下载

GitHub: https://github.com/lizuyi-6/fluxguard-pcb

---

**生成时间**: 2026-03-15 23:10 (UTC+8)
