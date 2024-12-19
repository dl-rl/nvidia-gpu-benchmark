# nvidia-gpu-benchmark

## Installation
Execute `./setup.sh`

## Inference Benchmark
Execute `./run_inference_benchmark.sh` (By default it'll try to run it on GPU 0)

To run it on a particular GPU, execute `./run_inference_benchmark.sh 1`, where 1 is the GPU index.

To run it on the CPU, execute `./run_inference_benchmark.sh cpu`

## Training Benchmark
Execute `./run_training_benchmark.sh` (By default it'll try to run it on GPU 0)

To run it on a particular GPU, execute `./run_training_benchmark.sh 1`, where 1 is the GPU index.

To run it across two GPUs, execute `./run_training_benchmark.sh multi`

To run it on the CPU, execute `./run_training_benchmark.sh cpu`