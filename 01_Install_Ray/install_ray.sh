#!/bin/bash

source ~/anaconda3/etc/profile.d/conda.sh
conda init bash

conda create -n "RayEnv" python=3.9
conda activate RayEnv

pip3 install ray[default]