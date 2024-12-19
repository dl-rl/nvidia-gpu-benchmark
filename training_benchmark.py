from ultralytics import YOLO
import sys
import time

batch = 0.9 # 90% vram
try:
  device = sys.argv[1]
  if device == "multi":
    device = [0, 1]
    batch = 32 # need to set fixed batch size for multi-gpu
except:
  device = 0

# Load a model
model = YOLO("yolo11l.pt")  # pretrained YOLO11n model

############# Training #############
epochs = 20
start_time = time.time()
results = model.train(data="data/custom.yaml", epochs=epochs, imgsz=640, batch=batch, val=False, save=False, amp=False, device=device)
stop_time = time.time()
average_training_time_per_epoch = round((stop_time - start_time) / epochs, 4)


print(f"\nAverage Training Time Per Epoch = {average_training_time_per_epoch} seconds")

# print(results.mean_results)