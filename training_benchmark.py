from ultralytics import YOLO
import sys
import time


try:
  device = sys.argv[1]
  if device == "multi":
    device = [0, 1]
except:
  device = 0

# Load a model
model = YOLO("yolo11l.pt")  # pretrained YOLO11n model

############# Training #############
epochs = 20
start_time = time.time()
results = model.train(data="data/custom.yaml", epochs=epochs, imgsz=640, batch=0.9, val=False, save=False, amp=False, device=device) # batch=0.9 means it'll auto-determine the bbatch size to fill 90% of the vram.
stop_time = time.time()
average_training_time_per_epoch = round((stop_time - start_time) / epochs, 4)


print(f"\nAverage Training Time Per Epoch = {average_training_time_per_epoch} seconds")

# print(results.mean_results)