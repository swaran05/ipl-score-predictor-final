@echo off
python train_model.py
if exist model.pkl (
  echo Model trained.
) else (
  echo Training failed.
)
