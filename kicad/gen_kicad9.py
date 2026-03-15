#!/usr/bin/env python3
"""
FluxGuard v3.0 KiCad 9.0 原理图生成器
生成完整的元件和连线
"""

from kiutils.schematic import Schematic, SchematicSymbol, Junction, LocalLabel, Position, PolyLine
from kiutils.symbol import Property
import uuid

def gen_uuid():
    return str(uuid.uuid4())

def create_schematic():
    sch = Schematic()
    sch.title = "FluxGuard Deployment Dongle v3.0"
    sch.date = "2026-03-15"
    sch.revision = "3.0"
    sch.company = "Hangzhou Visularity Technology Co., Ltd."
    return sch

def add_symbol(sch, lib_nick, lib_name, ref, value, footprint, x, y, unit=1):
    """添加元件符号"""
    props = [
        Property(key="Reference", value=ref),
        Property(key="Value", value=value),
        Property(key="Footprint", value=footprint),
    ]
    sym = SchematicSymbol(
        libraryNickname=lib_nick,
        entryName=lib_name,
        position=Position(x, y, 0),
        uuid=gen_uuid(),
        properties=props,
        unit=unit,
        inBom=True,
        onBoard=True
    )
    sch.schematicSymbols.append(sym)
    return sym

def add_wire(sch, points):
    """添加导线"""
    wire = PolyLine(
        points=[Position(p[0], p[1], 0) for p in points],
        uuid=gen_uuid()
    )
    sch.shapes.append(wire)
    return wire

def add_label(sch, text, x, y):
    """添加网络标签"""
    label = LocalLabel(
        text=text,
        position=Position(x, y, 0),
        uuid=gen_uuid()
    )
    sch.labels.append(label)
    return label

def add_junction(sch, x, y):
    """添加连接点"""
    jct = Junction(
        position=Position(x, y, 0),
        uuid=gen_uuid()
    )
    sch.junctions.append(jct)
    return jct

def main():
    print("生成 FluxGuard v3.0 原理图...")
    sch = create_schematic()
    
    # ========================================
    # 电源符号
    # ========================================
    print("  添加电源符号...")
    add_symbol(sch, "power", "+3V3", "#PWR001", "+3V3", "", 25.4, 20.32)
    add_symbol(sch, "power", "GND", "#PWR002", "GND", "", 25.4, 25.4)
    add_symbol(sch, "power", "VBUS", "#PWR003", "VBUS", "", 15.24, 20.32)
    add_symbol(sch, "power", "VBATT", "#PWR004", "VBATT", "", 35.56, 20.32)
    
    # ========================================
    # USB-C 接口
    # ========================================
    print("  添加USB接口...")
    add_symbol(sch, "Connector", "USB_C_Receptacle_USB2.0_16P", "J1", "USB_C", 
               "Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12", 25.4, 55.88)
    
    # ========================================
    # USB转串口
    # ========================================
    print("  添加USB转串口...")
    add_symbol(sch, "Interface_USB", "CH340N", "U2", "CH340N",
               "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm", 58.42, 53.34)
    
    # ========================================
    # 电源管理
    # ========================================
    print("  添加电源管理...")
    add_symbol(sch, "Regulator_Linear", "AMS1117-3.3", "U3", "AMS1117-3.3",
               "Package_TO_SOT_SMD:SOT-223-3_TabPin2", 25.4, 91.44)
    add_symbol(sch, "Battery_Management", "TP4056", "U4", "TP4056",
               "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm", 58.42, 91.44)
    add_symbol(sch, "Battery_Management", "DW01A", "U5", "DW01A",
               "Package_TO_SOT_SMD:SOT-23-6", 91.44, 91.44)
    
    # ========================================
    # 主控 ESP32
    # ========================================
    print("  添加ESP32...")
    add_symbol(sch, "RF_Module", "ESP32-WROOM-32E", "U1", "ESP32-WROOM-32E",
               "RF_Module:ESP32-WROOM-32", 149.86, 73.66)
    
    # ========================================
    # 安全模块
    # ========================================
    print("  添加安全模块...")
    add_symbol(sch, "Security", "ATECC608A-SSHDA", "U6", "ATECC608A",
               "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm", 205.74, 53.34)
    add_symbol(sch, "Timer", "MAX6818", "U7", "MAX6818",
               "Package_TO_SOT_SMD:SOT-23-5", 205.74, 91.44)
    
    # ========================================
    # 显示模块
    # ========================================
    print("  添加显示模块...")
    add_symbol(sch, "Connector_Generic", "Conn_01x04", "J5", "OLED_I2C",
               "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical", 261.62, 45.72)
    add_symbol(sch, "LED", "WS2812B", "D1", "WS2812B",
               "LED_SMD:LED_WS2812B_PLCC4_5.0x5.0mm_P3.2mm", 261.62, 73.66)
    add_symbol(sch, "Device", "Buzzer", "BZ1", "Buzzer",
               "Buzzer_Beeper:Buzzer_12x9.5RM7.6", 261.62, 96.52)
    
    # ========================================
    # 按键
    # ========================================
    print("  添加按键...")
    add_symbol(sch, "Switch", "SW_Push", "SW1", "BTN_OK",
               "Button_Switch_THT:SW_PUSH_6mm", 289.56, 45.72)
    add_symbol(sch, "Switch", "SW_Push", "SW2", "BTN_NEXT",
               "Button_Switch_THT:SW_PUSH_6mm", 289.56, 63.5)
    add_symbol(sch, "Switch", "SW_Push", "SW3", "BTN_BACK",
               "Button_Switch_THT:SW_PUSH_6mm", 289.56, 81.28)
    
    # ========================================
    # 被动元件
    # ========================================
    print("  添加被动元件...")
    for i in range(1, 11):
        add_symbol(sch, "Device", "C", f"C{i}", "100nF",
                   "Capacitor_SMD:C_0603_1608Metric", 350 + i*10, 20.32)
    for i in range(1, 11):
        add_symbol(sch, "Device", "R", f"R{i}", "10K",
                   "Resistor_SMD:R_0603_1608Metric", 350 + i*10, 35.56)
    
    # ========================================
    # 连线
    # ========================================
    print("  添加连线...")
    
    # 电源网络
    add_wire(sch, [(20.32, 55.88), (20.32, 53.34), (58.42, 53.34)])
    add_label(sch, "VBUS", 40.64, 53.34)
    
    add_wire(sch, [(30.48, 91.44), (30.48, 20.32), (200.66, 20.32)])
    add_label(sch, "+3V3", 30.48, 20.32)
    
    add_wire(sch, [(25.4, 25.4), (350, 25.4)])
    add_label(sch, "GND", 25.4, 25.4)
    
    # USB 通信
    add_wire(sch, [(33.02, 55.88), (33.02, 48.26), (58.42, 48.26)])
    add_label(sch, "USB_D+", 45.72, 48.26)
    
    add_wire(sch, [(35.56, 55.88), (35.56, 45.72), (58.42, 45.72)])
    add_label(sch, "USB_D-", 45.72, 45.72)
    
    # I2C
    add_wire(sch, [(170.18, 73.66), (200, 73.66), (200, 45.72), (261.62, 45.72)])
    add_label(sch, "I2C_SDA", 215.9, 45.72)
    
    add_wire(sch, [(170.18, 76.2), (202.54, 76.2), (202.54, 48.26), (261.62, 48.26)])
    add_label(sch, "I2C_SCL", 218.44, 48.26)
    
    # RGB
    add_wire(sch, [(170.18, 81.28), (230, 81.28), (230, 73.66), (261.62, 73.66)])
    add_label(sch, "RGB_DATA", 240, 73.66)
    
    # 按键
    add_wire(sch, [(170.18, 63.5), (289.56, 63.5)])
    add_label(sch, "BTN_OK", 230, 63.5)
    
    # 连接点
    add_junction(sch, 30.48, 20.32)
    add_junction(sch, 200.66, 20.32)
    
    # 保存
    output_path = "/root/.openclaw/workspace/projects/Networksafe-hardware/kicad/FluxGuard-v3.0.kicad_sch"
    sch.to_file(output_path)
    
    print(f"\n✅ 原理图已生成!")
    print(f"📁 保存到: {output_path}")
    print(f"📊 元件数: {len(sch.schematicSymbols)}")
    print(f"📊 连线数: {len(sch.shapes)}")
    print(f"📊 标签数: {len(sch.labels)}")

if __name__ == "__main__":
    main()
