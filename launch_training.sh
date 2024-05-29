export MODEL_NAME="CompVis/stable-diffusion-v1-4"
# export MODEL_NAME="bguisard/stable-diffusion-nano-2-1"
export TRAIN_DIR="data/train"
export OUTPUT_DIR="outputs"

accelerate launch train_text_to_image.py \
  --pretrained_model_name_or_path=$MODEL_NAME \
  --train_data_dir=$TRAIN_DIR \
  --use_ema \
  --resolution=128 --center_crop --random_flip \
  --train_batch_size=2 \
  --gradient_accumulation_steps=4 \
  --gradient_checkpointing \
  --mixed_precision="fp16" \
  --max_train_steps=35000 \
  --learning_rate=2e-06 \
  --max_grad_norm=1 \
  --lr_scheduler="constant" --lr_warmup_steps=0 \
  --output_dir=${OUTPUT_DIR}