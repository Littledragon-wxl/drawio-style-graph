#!/usr/bin/env python3
"""Quick validation of the autolayout.py XML structure fix."""
import sys
import xml.etree.ElementTree as ET

def validate_xml_structure():
    """Check that autolayout.py generates correct XML structure."""
    
    # Simulate what autolayout.py should generate
    expected_start = '<?xml version="1.0" encoding="UTF-8"?>'
    expected_mxfile = '<mxfile host="drawio" version="26.0.0">'
    expected_diagram = '<diagram name="Page-1">'
    expected_root = '<root>'
    expected_end = '</mxfile>'
    
    # Read autolayout.py and extract the return statement
    with open('scripts/autolayout.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the return statement in to_drawio function
    start_idx = content.find("    return (")
    if start_idx == -1:
        print("❌ Could not find return statement in to_drawio()")
        return False
    
    # Check for the required XML structure
    checks = [
        ("XML Declaration", '<?xml version="1.0" encoding="UTF-8"?>'),
        ("mxfile with host attribute", '<mxfile host="drawio" version="26.0.0">'),
        ("diagram name attribute", '<diagram name="Page-1">'),
        ("mxGraphModel", '<mxGraphModel>'),
        ("root element", '<root>'),
        ("mxCell id=0", '<mxCell id="0" />'),
        ("mxCell id=1", '<mxCell id="1" parent="0" />'),
        ("closing root", '</root>'),
        ("closing mxGraphModel", '</mxGraphModel>'),
        ("closing diagram", '</diagram>'),
        ("closing mxfile", '</mxfile>'),
    ]
    
    all_passed = True
    for name, pattern in checks:
        if pattern in content:
            print(f"✅ Found: {name}")
        else:
            print(f"❌ Missing: {name}")
            all_passed = False
    
    return all_passed


def test_open_drawio_script():
    """Verify open_drawio.py exists and has proper structure."""
    try:
        with open('scripts/open_drawio.py', 'r', encoding='utf-8') as f:
            content = f.read()
        
        checks = [
            ("find_drawio_app function", "def find_drawio_app"),
            ("open_with_desktop_app function", "def open_with_desktop_app"),
            ("open_with_browser function", "def open_with_browser"),
            ("macOS support", 'Path("/Applications/draw.io.app')
            ("Windows support", 'Path("C:/Program Files/draw.io'),
            ("Linux support", '"drawio"'),
        ]
        
        all_passed = True
        for name, pattern in checks:
            if pattern in content:
                print(f"✅ Found: {name}")
            else:
                print(f"❌ Missing: {name}")
                all_passed = False
        
        return all_passed
    except FileNotFoundError:
        print("❌ open_drawio.py not found")
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("VALIDATION: autolayout.py XML Structure Fix")
    print("=" * 60)
    result1 = validate_xml_structure()
    
    print("\n" + "=" * 60)
    print("VALIDATION: open_drawio.py Script")
    print("=" * 60)
    result2 = test_open_drawio_script()
    
    print("\n" + "=" * 60)
    if result1 and result2:
        print("✅ All validations passed!")
        sys.exit(0)
    else:
        print("❌ Some validations failed")
        sys.exit(1)
