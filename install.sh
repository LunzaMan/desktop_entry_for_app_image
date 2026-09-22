#!/bin/sh

set -e

REPO="LunzaMan/desktop_entry_for_app_image"
APP_NAME="imageToApp"
INSTALL_DIR="$HOME/.local/bin/"

ARCH="$(uname -m)"

case "$ARCH" in
x86_64)
  BINARY="imageToApp-linux-x86_64"
  ;;
*)
  echo "Unsupported architecture: $ARCH"
  exit 1
  ;;

esac

echo "Downloading $APP_NAME"

mkdir -p "$INSTALL_DIR"

curl -fL \
  "https://github.com/$REPO/releases/latest/download/$BINARY" \
  -o "$INSTALL_DIR/$APP_NAME"

chmod +x "$INSTALL_DIR/$APP_NAME"

echo ""
echo "$APP_NAME installed to $INSTALL_DIR"
echo ""

case ":$PATH:" in
*":$INSTALL_DIR:"*) ;;
*)
  echo "$INSTALL_DIR is not in your PATH"
  echo "Add it with:"
  echo ""
  echo 'export PATH="$HOME/.local/bin:$PATH"'
  ;;

esac
