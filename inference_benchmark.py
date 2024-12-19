from ultralytics import YOLO
import sys

try:
  device = sys.argv[1]
except:
  device = 0

# Load a model
model = YOLO("yolo11l.pt")  # pretrained YOLO11n model

############# Inference #############
inference_n_passes = 50
inference_batch_size = 30

sum_average_inference_time = 0
for i in range(inference_n_passes):
  print(f"\n\nPass {i+1}:-")
  # Run batched inference
  input_list = ["sample_image.png"] * inference_batch_size
  results = model.predict(input_list, save=False, imgsz=640, device=device)
  average_inference_time = results[0].speed["inference"] # Since this is a batched run, all the entries have the average inference time. 
  sum_average_inference_time += average_inference_time

average_inference_time_per_image = round(sum_average_inference_time / inference_n_passes, 4)

print(f"\n\nAverage Inference Time Per Image = {average_inference_time_per_image} milliseconds")
