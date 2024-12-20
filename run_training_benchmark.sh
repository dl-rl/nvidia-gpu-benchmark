cd "$(dirname "$0")"
SCRIPT_DIR="$(pwd)"

rm -rf runs

env/bin/python3 prepare_yaml.py

################################################################################################################################
# For training, YOLO doesn't give a per-epoch timing in the results. One way to get this is to parse the terminals outputs.
# However, here I am running the training phases for two different epoch lengths, and then finding the difference.
# This removes the constant-time things like loading the model, preparing the data, etc.
# Then I'm taking the mean of the difference.
# Also, I had to run the training phases as separate python scripts because YOLO was taking a big pause while running 
# multiple training sessions within the same script.
################################################################################################################################
epochs_1=4
epochs_2=15
env/bin/python3 training_benchmark.py $epochs_1 $1
env/bin/python3 training_benchmark.py $epochs_2 $1
env/bin/python3 parse_training_times.py $epochs_1 $epochs_2
rm *_epochs___.txt
