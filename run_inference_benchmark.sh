cd "$(dirname "$0")"
SCRIPT_DIR="$(pwd)"

env/bin/python3 inference_benchmark.py $1