from __future__ import absolute_import
import time
from subprocess import call
import random

#@app.task

input_file = "/home/osboxes/Documents/Dorothea/Scripts/rockyou_160000.txt"  # Archivo de entrada
output_prefix = 'rockyou_160000'  # Prefijo para los archivos de salida
lines_per_file = 4000  # Número de líneas por archivo


with open(input_file, 'r') as file:
    data = file.readlines()

num_files = len(data) // lines_per_file + 1
 
for i in range(num_files):
    start = i * lines_per_file
    end = (i + 1) * lines_per_file
    lines = data[start:end]
        
    output_file = "/home/osboxes/Documents/Dorothea/Scripts/"f"{output_prefix}_{i+1}.txt"
    with open(output_file, 'w') as file:
        file.writelines(lines)