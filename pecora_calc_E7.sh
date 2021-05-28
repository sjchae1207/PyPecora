#!/usr/bin/sh
#SBATCH -c 12 
#SBATCH -p HQ2comp

module load python/3.7.2
module load anaconda3/2020.11

python3 hk_pecora_calc_olaf.py
