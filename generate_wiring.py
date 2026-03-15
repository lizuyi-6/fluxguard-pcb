#!/usr/bin/env python3
"""
FluxGuard v3.0 KiCad 原理图连线生成器
使用 PolyLine 添加连线
"""

from kiutils.schematic import Schematic, PolyLine, Junction, LocalLabel, Position
import uuid

def load_schematic():
    """加载原理图"""
    sch_path = "/root/.openclaw/workspace/projects/Networksafe-hardware/kicad/FluxGuard-v3.0.kicad_sch"
    return Schematic.from_file(sch_path)

def add_wire(sch, points):
    """添加导线 (使用 PolyLine)"""
    wire = PolyLine(
        points=[Position(p[0], p[1], 0) for p in points],
        uuid=str(uuid.uuid4())
    )
    sch.shapes.append(wire)
    return wire

def add_label(sch, text, x, y):
    """添加网络标签"""
    label = LocalLabel(
        text=text,
        position=Position(x, y, 0),
        uuid=str(uuid.uuid4())
    )
    sch.labels.append(label)
    return label

def add_junction(sch, x, y):
    """添加连接点"""
    junction = Junction(
        position=Position(x, y, 0),
        uuid=str(uuid.uuid4())
    )
    sch.junctions.append(junction)
    return junction

def main():
    print("加载原理图...")
    sch = load_schematic()
    
    print("开始连线...")
    
    # ========================================
    # 电源网络
    # ========================================
    print("  - 电源网络...")
    
    # VBUS 主线
    add_wire(sch, [(20.32, 55.88), (20.32, 53.34), (58.42, 53.34)])
    add_wire(sch, [(58.42, 53.34), (58.42, 91.44), (25.4, 91.44)])
    add_label(sch, "VBUS", 40.64, 53.34)
    
    # +3V3 主线
    add_wire(sch, [(30.48, 91.44), (30.48, 20.32), (200.66, 20.32)])
    add_wire(sch, [(200.66, 20.32), (200.66, 53.34), (205.74, 53.34)])
    add_wire(sch, [(200.66, 20.32), (200.66, 91.44), (205.74, 91.44)])
    add_label(sch, "+3V3", 30.48, 20.32)
    
    # GND 主线
    add_wire(sch, [(25.4, 25.4), (350.0, 25.4)])
    add_label(sch, "GND", 25.4, 25.4)
    
    # ========================================
    # USB 通信
    # ========================================
    print("  - USB通信...")
    
    # USB D+
    add_wire(sch, [(33.02, 55.88), (33.02, 48.26), (48.26, 48.26)])
    add_label(sch, "USB_D+", 40.64, 48.26)
    
    # USB D-
    add_wire(sch, [(35.56, 55.88), (35.56, 45.72), (48.26, 45.72)])
    add_label(sch, "USB_D-", 40.64, 45.72)
    
    # CH340N TX → ESP32 GPIO23
    add_wire(sch, [(68.58, 53.34), (73.66, 53.34), (73.66, 73.66), (149.86, 73.66)])
    add_label(sch, "USB_TX", 111.76, 53.34)
    
    # CH340N RX ← ESP32 RXD0
    add_wire(sch, [(68.58, 55.88), (76.2, 55.88), (76.2, 76.2), (149.86, 76.2)])
    add_label(sch, "USB_RX", 111.76, 55.88)
    
    # ========================================
    # I2C 总线
    # ========================================
    print("  - I2C总线...")
    
    # I2C_SDA (GPIO32 → OLED)
    add_wire(sch, [(170.18, 73.66), (175.26, 73.66), (175.26, 45.72), (261.62, 45.72)])
    add_label(sch, "I2C_SDA", 218.44, 45.72)
    
    # I2C_SCL (GPIO33 → OLED)
    add_wire(sch, [(170.18, 76.2), (177.8, 76.2), (177.8, 48.26), (261.62, 48.26)])
    add_label(sch, "I2C_SCL", 218.44, 48.26)
    
    # SEC_SDA (GPIO21 → ATECC608A)
    add_wire(sch, [(170.18, 68.58), (180.34, 68.58), (180.34, 55.88), (205.74, 55.88)])
    add_label(sch, "SEC_SDA", 193.04, 55.88)
    
    # SEC_SCL (GPIO22 → ATECC608A)
    add_wire(sch, [(170.18, 71.12), (182.88, 71.12), (182.88, 58.42), (205.74, 58.42)])
    add_label(sch, "SEC_SCL", 193.04, 58.42)
    
    # ========================================
    # 显示与交互
    # ========================================
    print("  - 显示与交互...")
    
    # RGB_DATA (GPIO25 → WS2812B)
    add_wire(sch, [(170.18, 81.28), (190.5, 81.28), (190.5, 73.66), (261.62, 73.66)])
    add_label(sch, "RGB_DATA", 226.06, 73.66)
    
    # BUZZER (GPIO26)
    add_wire(sch, [(170.18, 83.82), (193.04, 83.82), (193.04, 96.52), (261.62, 96.52)])
    add_label(sch, "BUZZER_PWM", 226.06, 96.52)
    
    # BTN_OK (GPIO15)
    add_wire(sch, [(170.18, 63.5), (195.58, 63.5), (195.58, 45.72), (289.56, 45.72)])
    add_label(sch, "BTN_OK", 242.57, 45.72)
    
    # BTN_NEXT (GPIO4)
    add_wire(sch, [(149.86, 68.58), (149.86, 66.04), (198.12, 66.04), (198.12, 63.5), (289.56, 63.5)])
    add_label(sch, "BTN_NEXT", 242.57, 63.5)
    
    # BTN_BACK (GPIO5)
    add_wire(sch, [(149.86, 71.12), (147.32, 71.12), (147.32, 81.28), (289.56, 81.28)])
    add_label(sch, "BTN_BACK", 218.44, 81.28)
    
    # ========================================
    # 服务器通信
    # ========================================
    print("  - 服务器通信...")
    
    # TARGET_TX (GPIO14)
    add_wire(sch, [(170.18, 88.9), (213.36, 88.9), (213.36, 119.38), (289.56, 119.38)])
    add_label(sch, "TARGET_TX", 251.46, 88.9)
    
    # TARGET_RX (GPIO12)
    add_wire(sch, [(170.18, 91.44), (215.9, 91.44), (215.9, 121.92), (289.56, 121.92)])
    add_label(sch, "TARGET_RX", 251.46, 91.44)
    
    # ========================================
    # 安全模块
    # ========================================
    print("  - 安全模块...")
    
    # SEC_IRQ (GPIO27)
    add_wire(sch, [(170.18, 86.36), (208.28, 86.36), (208.28, 53.34)])
    add_label(sch, "SEC_IRQ", 187.96, 86.36)
    
    # WDT_FEED (GPIO13)
    add_wire(sch, [(170.18, 93.98), (205.74, 93.98)])
    add_label(sch, "WDT_FEED", 187.96, 93.98)
    
    # WDT_RST
    add_wire(sch, [(205.74, 96.52), (144.78, 96.52), (144.78, 73.66)])
    add_label(sch, "WDT_RST", 175.26, 96.52)
    
    # ========================================
    # 电池管理
    # ========================================
    print("  - 电池管理...")
    
    # VBATT
    add_wire(sch, [(68.58, 91.44), (68.58, 88.9), (91.44, 88.9), (91.44, 91.44)])
    add_label(sch, "VBATT", 78.74, 88.9)
    
    # CHRG
    add_wire(sch, [(68.58, 93.98), (78.74, 93.98)])
    add_label(sch, "CHRG", 73.66, 93.98)
    
    # STDBY
    add_wire(sch, [(68.58, 96.52), (78.74, 96.52)])
    add_label(sch, "STDBY", 73.66, 96.52)
    
    # ========================================
    # 添加连接点
    # ========================================
    print("  - 添加连接点...")
    
    add_junction(sch, 40.64, 53.34)   # VBUS
    add_junction(sch, 30.48, 20.32)   # +3V3
    add_junction(sch, 200.66, 20.32)  # +3V3 分支
    add_junction(sch, 175.26, 45.72)  # I2C_SDA
    add_junction(sch, 177.8, 48.26)   # I2C_SCL
    
    # 保存原理图
    output_path = "/root/.openclaw/workspace/projects/Networksafe-hardware/kicad/FluxGuard-v3.0.kicad_sch"
    sch.to_file(output_path)
    
    # 统计
    wire_count = len([x for x in sch.shapes if isinstance(x, PolyLine)])
    
    print(f"\n✅ 原理图连线完成！")
    print(f"📁 保存到: {output_path}")
    print(f"📊 导线数: {wire_count}")
    print(f"📊 标签数: {len(sch.labels)}")
    print(f"📊 连接点: {len(sch.junctions)}")

if __name__ == "__main__":
    main()
