# Copyright (c) 2024, DL-RL Inc.
# All rights reserved.

from ultralytics import YOLO
import torch
import sys
import time

batch = 32
epochs = int(sys.argv[1])
try:
  device = sys.argv[2]
  if device == "all_gpu":
    device = str(list(range(torch.cuda.device_count())))
except:
  device = 0

############# Training #############
model = YOLO("yolo11l.pt")
start_time = time.time()
results = model.train(data="data/custom.yaml", epochs=epochs, imgsz=640, batch=batch, val=False, save=False, patience=0, device=device)
stop_time = time.time()
training_time_in_seconds = stop_time - start_time

with open(f"___total_time_for_{epochs}_epochs___.txt", "w") as fobj:
  fobj.write(f"{training_time_in_seconds}")
  print(training_time_in_seconds)
