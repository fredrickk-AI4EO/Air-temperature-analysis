import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

ds = xr.tutorial.open_dataset("air_temperature.nc")
data = ds["air"].isel(time=0)
output_dir = "xarray_analysis_outputs"
os.makedirs(output_dir, exist_ok=True)
# 1. Summary Statistics
mean_temp = data.mean().item()
std_temp = data.std().item()
min_temp = data.min().item()
max_temp = data.max().item()
with open(os.path.join(output_dir, "summary_statistics.txt"), "w") as f:
    f.write(f"Mean Temperature: {mean_temp:.2f} K\n")
    f.write(f"Standard Deviation: {std_temp:.2f} K\n")
    f.write(f"Minimum Temperature: {min_temp:.2f} K\n")
    f.write(f"Maximum Temperature: {max_temp:.2f} K\n") 
    


