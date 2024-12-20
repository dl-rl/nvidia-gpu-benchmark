import sys

epochs_1 = int(sys.argv[1])
epochs_2 = int(sys.argv[2])

with open(f"___total_time_for_{epochs_1}_epochs___.txt", "r") as fobj:
  time_1_in_seconds = float(fobj.read())

with open(f"___total_time_for_{epochs_2}_epochs___.txt", "r") as fobj:
  time_2_in_seconds = float(fobj.read())

print(f"\n\nAverage Training Time Per Epoch = {round((time_2_in_seconds - time_1_in_seconds)/(epochs_2 - epochs_1), 4)} seconds")