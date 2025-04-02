#!/bin/bash
#SBATCH -p mcml-hgx-a100-80x4-mig
#SBATCH --gres=gpu:1
#SBATCH --output=out.txt
#SBATCH --cpus-per-task=16
#SBATCH --time=2-00:00:00
#SBATCH --qos=mcml
#SBATCH --mem-per-cpu=0

srun python ape_service.py