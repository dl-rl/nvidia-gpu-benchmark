cd "$(dirname "$0")"
SCRIPT_DIR="$(pwd)"

rm -rf runs

env/bin/python3 prepare_yaml.py

env/bin/python3 training_benchmark.py $1
