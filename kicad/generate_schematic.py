#!/usr/bin/env python3
"""
FluxGuard v3.0 KiCad 原理图生成器
使用 kiutils 库生成完整的 KiCad 原理图
"""

from kiutils.schematic import Schematic, SchematicSymbol, Property, Position
import uuid

def create_schematic():
    """创建原理图"""
    sch = Schematic()
    
    # 设置标题信息
    sch.title = "FluxGuard Deployment Dongle v3.0"
    sch.date = "2026-03-15"
    sch.revision = "3.0"
    sch.company = "杭州视界奇点科技有限公司"
    
    return sch

def add_component(sch, lib_nickname, entry_name, reference, value, footprint, x, y):
    """添加元件到原理图"""
    # 创建属性
    properties = [
        Property(key="Reference", value=reference),
        Property(key="Value", value=value),
        Property(key="Footprint", value=footprint)
    ]
    
    # 创建元件符号
    symbol = SchematicSymbol(
        libraryNickname=lib_nickname,
        entryName=entry_name,
        position=Position(x, y, 0),
        uuid=str(uuid.uuid4()),
        properties=properties,
        inBom=True,
        onBoard=True
    )
    sch.schematicSymbols.append(symbol)
    return symbol

def main():
    # 创建原理图
    sch = create_schematic()
    
    print("正在生成原理图...")
    
    # ========================================
    # 电源符号
    # ========================================
    add_component(sch, "power", "+3V3", "#PWR001", "+3V3", "", 25.4, 20.32)
    add_component(sch, "power", "GND", "#PWR002", "GND", "", 25.4, 25.4)
    add_component(sch, "power", "VBUS", "#PWR003", "VBUS", "", 15.24, 20.32)
    add_component(sch, "power", "VBATT", "#PWR004", "VBATT", "", 35.56, 20.32)
    
    # ========================================
    # USB-C 接口
    # ========================================
    add_component(sch, 
        "Connector", "USB_C_Receptacle_USB2.0_16P",
        "J1", "USB_C_Receptacle",
        "Connector_USB:USB_C_Receptacle_HRO_TYPE-C-31-M-12_2x6_P0.5mm_Horizontal",
        25.4, 55.88)
    
    # ========================================
    # USB转串口
    # ========================================
    add_component(sch,
        "Interface_USB", "CH340N",
        "U2", "CH340N",
        "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        58.42, 53.34)
    
    # ========================================
    # 电源管理
    # ========================================
    add_component(sch,
        "Regulator_Linear", "AMS1117-3.3",
        "U3", "AMS1117-3.3",
        "Package_TO_SOT_SMD:SOT-223-3_TabPin2",
        25.4, 91.44)
    
    add_component(sch,
        "Battery_Management", "TP4056",
        "U4", "TP4056",
        "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        58.42, 91.44)
    
    add_component(sch,
        "Battery_Management", "DW01A",
        "U5", "DW01A",
        "Package_TO_SOT_SMD:SOT-23-6",
        91.44, 91.44)
    
    add_component(sch,
        "Device", "Q_Dual_PMOS_S1G1D2S2G2D1",
        "Q1", "FS8205A",
        "Package_SO:TSSOP-8_4.4x3mm_P0.65mm",
        114.3, 91.44)
    
    # ========================================
    # 主控 ESP32
    # ========================================
    add_component(sch,
        "RF_Module", "ESP32-WROOM-32E",
        "U1", "ESP32-WROOM-32E",
        "RF_Module:ESP32-WROOM-32",
        149.86, 73.66)
    
    # ========================================
    # 安全模块
    # ========================================
    add_component(sch,
        "Security", "ATECC608A-SSHDA",
        "U6", "ATECC608A",
        "Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
        205.74, 53.34)
    
    add_component(sch,
        "Timer", "MAX6818",
        "U7", "MAX6818",
        "Package_TO_SOT_SMD:SOT-23-5",
        205.74, 91.44)
    
    # ========================================
    # 显示模块
    # ========================================
    add_component(sch,
        "Display", "SSD1306_OLED_0.96in",
        "DISP1", "SSD1306_0.96in",
        "Display:OLED_0.96in_128x64_FPC30",
        261.62, 45.72)
    
    add_component(sch,
        "LED", "WS2812B",
        "D1", "WS2812B-2020",
        "LED_SMD:LED_WS2812B-2020_PLCC4_2.0x2.0mm",
        261.62, 73.66)
    
    add_component(sch,
        "Device", "Buzzer",
        "BZ1", "MLT-8530",
        "Buzzer_Beeper:Buzzer_MLT-8530",
        261.62, 96.52)
    
    # ========================================
    # 按键
    # ========================================
    add_component(sch,
        "Switch", "SW_Push",
        "SW1", "BTN_OK",
        "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm",
        289.56, 45.72)
    
    add_component(sch,
        "Switch", "SW_Push",
        "SW2", "BTN_NEXT",
        "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm",
        289.56, 63.5)
    
    add_component(sch,
        "Switch", "SW_Push",
        "SW3", "BTN_BACK",
        "Button_Switch_SMD:SW_Push_1P1T_NO_6x6mm_H9.5mm",
        289.56, 81.28)
    
    # ========================================
    # ESD保护
    # ========================================
    add_component(sch,
        "Device", "TVS_4x",
        "TVS1", "SRV05-4",
        "Package_TO_SOT_SMD:SOT-23-6",
        25.4, 119.38)
    
    add_component(sch,
        "Device", "TVS_4x",
        "TVS2", "SRV05-4",
        "Package_TO_SOT_SMD:SOT-23-6",
        48.26, 119.38)
    
    # ========================================
    # 接口连接器
    # ========================================
    add_component(sch,
        "Connector", "Conn_01x10_Male",
        "J2", "TARGET_UART",
        "Connector_PinHeader_2.54mm:PinHeader_2x05_P2.54mm_Vertical",
        289.56, 119.38)
    
    add_component(sch,
        "Connector", "Conn_01x06_Male",
        "J3", "DEBUG",
        "Connector_PinHeader_1.27mm:PinHeader_2x03_P1.27mm_Vertical",
        309.88, 119.38)
    
    add_component(sch,
        "Connector", "Conn_01x02_Male",
        "J4", "BATTERY",
        "Connector_JST:JST_PH_B2B-PH-K_1x02_P2.00mm_Vertical",
        330.2, 119.38)
    
    # ========================================
    # 被动元件 - 电容
    # ========================================
    for i in range(1, 16):
        add_component(sch,
            "Device", "C",
            f"C{i}", "100nF",
            "Capacitor_SMD:C_0603_1608Metric",
            350 + (i * 10), 20.32)
    
    for i in range(16, 20):
        add_component(sch,
            "Device", "C",
            f"C{i}", "10uF",
            "Capacitor_SMD:C_0805_2012Metric",
            350 + (i * 10), 35.56)
    
    for i in range(20, 22):
        add_component(sch,
            "Device", "C",
            f"C{i}", "22uF",
            "Capacitor_SMD:C_1206_3216Metric",
            350 + (i * 10), 50.8)
    
    # ========================================
    # 被动元件 - 电阻
    # ========================================
    for i in range(1, 11):
        add_component(sch,
            "Device", "R",
            f"R{i}", "10K",
            "Resistor_SMD:R_0603_1608Metric",
            350 + (i * 10), 66.04)
    
    for i in range(11, 13):
        add_component(sch,
            "Device", "R",
            f"R{i}", "4.7K",
            "Resistor_SMD:R_0603_1608Metric",
            350 + (i * 10), 81.28)
    
    for i in range(13, 16):
        add_component(sch,
            "Device", "R",
            f"R{i}", "100R",
            "Resistor_SMD:R_0603_1608Metric",
            350 + (i * 10), 96.52)
    
    # ========================================
    # 其他元件
    # ========================================
    add_component(sch,
        "Device", "L",
        "L1", "2.2uH",
        "Inductor_SMD:L_0805_2012Metric",
        350, 111.76)
    
    add_component(sch,
        "Device", "Crystal",
        "Y1", "26MHz",
        "Oscillator:Oscillator_SMD_3225-4Pin_3.2x2.5mm",
        370, 111.76)
    
    add_component(sch,
        "Device", "Crystal",
        "Y2", "32.768kHz",
        "Crystal:Crystal_SMD_2012-2Pin_2.0x1.2mm",
        390, 111.76)
    
    # LED指示灯
    add_component(sch,
        "Device", "LED",
        "D2", "PWR_RED",
        "LED_SMD:LED_0603_1608Metric",
        410, 111.76)
    
    add_component(sch,
        "Device", "LED",
        "D3", "CHG_YELLOW",
        "LED_SMD:LED_0603_1608Metric",
        430, 111.76)
    
    add_component(sch,
        "Device", "LED",
        "D4", "DONE_GREEN",
        "LED_SMD:LED_0603_1608Metric",
        450, 111.76)
    
    # 测试点
    test_points = [
        ("TP1", "+3V3"),
        ("TP2", "VBUS"),
        ("TP3", "VBATT"),
        ("TP4", "GND"),
        ("TP5", "I2C_SDA"),
        ("TP6", "I2C_SCL"),
        ("TP7", "TARGET_TX"),
        ("TP8", "TARGET_RX")
    ]
    
    for i, (name, net) in enumerate(test_points):
        add_component(sch,
            "Connector", "TestPoint",
            name, net,
            "TestPoint:TestPoint_Pad_D1.0mm",
            470 + (i * 10), 111.76)
    
    # 保存原理图
    output_path = "/root/.openclaw/workspace/projects/Networksafe-hardware/kicad/FluxGuard-v3.0.kicad_sch"
    sch.to_file(output_path)
    
    print(f"✅ 原理图已保存到: {output_path}")
    print(f"📊 元件总数: {len(sch.schematicSymbols)}")

if __name__ == "__main__":
    main()
