#!/usr/bin/env python3
"""Open a .drawio file in the native draw.io application or browser.

Automatically detects the draw.io desktop app across platforms (macOS/Windows/Linux)
and opens the file. Falls back to generating a diagrams.net URL if the app is unavailable.

Usage: python3 open_drawio.py diagram.drawio
       python3 open_drawio.py diagram.drawio --edit
       python3 open_drawio.py diagram.drawio --browser
"""
import argparse
import os
import platform
import subprocess
import sys
from pathlib import Path


def find_drawio_app():
    """Detect the draw.io desktop app path across platforms."""
    system = platform.system()

    if system == "Darwin":  # macOS
        app_path = Path("/Applications/draw.io.app/Contents/MacOS/draw.io")
        if app_path.exists():
            return str(app_path)
    elif system == "Windows":
        # Try default installation paths
        paths = [
            Path("C:/Program Files/draw.io/draw.io.exe"),
            Path("C:/Program Files (x86)/draw.io/draw.io.exe"),
        ]
        for p in paths:
            if p.exists():
                return str(p)
    elif system == "Linux":
        # Try common Linux paths and PATH
        if subprocess.run(["which", "drawio"], capture_output=True).returncode == 0:
            return "drawio"
        if subprocess.run(["which", "draw.io"], capture_output=True).returncode == 0:
            return "draw.io"

    return None


def open_with_desktop_app(file_path):
    """Open .drawio file in the native draw.io desktop app."""
    app = find_drawio_app()
    if not app:
        return False

    try:
        system = platform.system()
        if system == "Darwin":  # macOS
            subprocess.Popen(["open", "-a", "draw.io", file_path])
        elif system == "Windows":
            subprocess.Popen([app, file_path])
        else:  # Linux
            subprocess.Popen([app, file_path])
        return True
    except Exception as e:
        print(f"Failed to open with desktop app: {e}", file=sys.stderr)
        return False


def open_with_browser(file_path, edit_mode=False):
    """Generate a diagrams.net URL and open in browser."""
    try:
        # Use encode_drawio_url.py to generate the URL
        args = ["python3", "scripts/encode_drawio_url.py"]
        if edit_mode:
            args.append("--edit")
        args.append(file_path)

        result = subprocess.run(args, capture_output=True, text=True, timeout=15)
        if result.returncode != 0:
            print(f"Failed to generate URL: {result.stderr}", file=sys.stderr)
            return False

        url = result.stdout.strip()
        if not url:
            print("No URL generated", file=sys.stderr)
            return False

        # Open in default browser
        webbrowser_cmd = None
        system = platform.system()
        if system == "Darwin":  # macOS
            webbrowser_cmd = ["open", url]
        elif system == "Windows":
            webbrowser_cmd = ["cmd", "/c", f'start "" "{url}"']
        else:  # Linux
            webbrowser_cmd = ["xdg-open", url]

        if webbrowser_cmd:
            subprocess.Popen(webbrowser_cmd)
            print(f"Opened in browser: {url[:80]}...", file=sys.stderr)
            return True
    except Exception as e:
        print(f"Failed to open in browser: {e}", file=sys.stderr)
        return False

    return False


def main():
    ap = argparse.ArgumentParser(
        description="Open a .drawio file in draw.io (desktop or browser).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 open_drawio.py diagram.drawio          # Opens in desktop app (preferred)
  python3 open_drawio.py diagram.drawio --edit   # Opens in browser editor mode
  python3 open_drawio.py diagram.drawio --browser # Force browser (diagrams.net)
        """,
    )
    ap.add_argument("file", help=".drawio file path")
    ap.add_argument(
        "--edit",
        action="store_true",
        help="Open in edit mode (browser only)",
    )
    ap.add_argument(
        "--browser",
        action="store_true",
        help="Force opening in browser (skip desktop app)",
    )
    args = ap.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        sys.exit(f"error: file not found: {args.file}")

    if not args.browser:
        # Try desktop app first
        if open_with_desktop_app(str(file_path)):
            print(f"Opened in draw.io desktop app: {file_path}", file=sys.stderr)
            return

    # Fallback to browser
    if open_with_browser(str(file_path), edit_mode=args.edit):
        return

    sys.exit("error: could not open .drawio file (no draw.io app or browser available)")


if __name__ == "__main__":
    main()
