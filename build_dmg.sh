#!/bin/bash
set -e

# --- CONFIG ---
APP_NAME="record_meeting"
ICON_PNG="icon.png"
ICONSET_DIR="icon.iconset"
ICNS_FILE="icon.icns"
PYINSTALLER="/Users/nickd/anaconda3/bin/pyinstaller"

# --- CLEANUP ---
echo "[1/5] Cleaning old builds..."
rm -rf build/ dist/ *.spec $ICONSET_DIR $ICNS_FILE

# --- ICON CONVERSION ---
echo "[2/5] Converting $ICON_PNG to $ICNS_FILE..."
mkdir $ICONSET_DIR
sips -z 16 16     $ICON_PNG --out $ICONSET_DIR/icon_16x16.png
sips -z 32 32     $ICON_PNG --out $ICONSET_DIR/icon_16x16@2x.png
sips -z 32 32     $ICON_PNG --out $ICONSET_DIR/icon_32x32.png
sips -z 64 64     $ICON_PNG --out $ICONSET_DIR/icon_32x32@2x.png
sips -z 128 128   $ICON_PNG --out $ICONSET_DIR/icon_128x128.png
sips -z 256 256   $ICON_PNG --out $ICONSET_DIR/icon_128x128@2x.png
sips -z 256 256   $ICON_PNG --out $ICONSET_DIR/icon_256x256.png
sips -z 512 512   $ICON_PNG --out $ICONSET_DIR/icon_256x256@2x.png
sips -z 512 512   $ICON_PNG --out $ICONSET_DIR/icon_512x512.png
cp $ICON_PNG $ICONSET_DIR/icon_512x512@2x.png
iconutil -c icns $ICONSET_DIR

# --- BUILD APP ---
echo "[3/5] Building $APP_NAME.app with PyInstaller..."
$PYINSTALLER --windowed --onefile --name $APP_NAME --icon=$ICNS_FILE main.py

# --- CREATE DMG ---
echo "[4/5] Creating DMG..."
create-dmg dist/$APP_NAME.app

echo "[5/5] Done! Find your DMG and .app in the project directory." 