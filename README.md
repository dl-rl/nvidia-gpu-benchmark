# Training & Inference Benchmark
This benchmark uses [YOLO11](https://docs.ultralytics.com/models/yolo11) to evaluate the per-epoch training time and inference time of a system.

It uses the [coco128](https://docs.ultralytics.com/datasets/detect/coco128) dataset.

## Prerequisites
* Ubuntu 22.04+
* Python 3.10+

## Installation
Execute `./setup.sh`

## Inference Benchmark
Execute `./run_inference_benchmark.sh` (By default it'll try to run it on GPU 0)

To run it on a particular GPU, execute `./run_inference_benchmark.sh 1`, where 1 is the GPU index.

To run it on the CPU, execute `./run_inference_benchmark.sh cpu`

## Training Benchmark
Execute `./run_training_benchmark.sh` (By default it'll try to run it on GPU 0)

To run it on a particular GPU, execute `./run_training_benchmark.sh 1`, where 1 is the GPU index.

To run it across all GPUs (DDP), execute `./run_training_benchmark.sh all_gpu`

To run it across specific GPUs (DDP), execute `./run_training_benchmark.sh [0,2,3,5]`, where the list contains the specific GPU indices.

To run it on the CPU, execute `./run_training_benchmark.sh cpu`

<br/><br/><br/>
<hr/>
Copyright (c) 2024, DL-RL Inc.
All rights reserved.

