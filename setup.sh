cd "$(dirname "$0")"
SCRIPT_DIR="$(pwd)"

if [ ! -d "env" ]; then
  echo "Creating env..."
  python3 -m venv env
fi

echo "Installing dependencies..."
env/bin/pip3 install -r requirements.txt