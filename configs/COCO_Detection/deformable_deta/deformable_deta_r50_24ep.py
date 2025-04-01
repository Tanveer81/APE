from detrex.config import get_config

from .models.deformable_deta_r50 import model

dataloader = get_config("common/data/coco_detr.py").dataloader
lr_multiplier = get_config("common/coco_schedule.py").lr_multiplier_24ep
optimizer = get_config("common/optim.py").AdamW
train = get_config("common/train.py").train

train.init_checkpoint = "detectron2://ImageNetPretrained/torchvision/R-50.pkl"
train.init_checkpoint = "models/torchvision/R-50.pkl"
train.output_dir = "output/" + __file__[:-3]

train.max_iter = 180000

train.eval_period = 5000

train.log_period = 20

train.checkpointer.period = 5000
train.checkpointer.max_to_keep = 2

train.clip_grad.enabled = True
train.clip_grad.params.max_norm = 0.1
train.clip_grad.params.norm_type = 2

train.device = "cuda"

optimizer.lr = 2e-4
optimizer.betas = (0.9, 0.999)
optimizer.weight_decay = 1e-4
optimizer.params.lr_factor_func = (
    lambda module_name: 0.1
    if "backbone" in module_name
    or "reference_points" in module_name
    or "sampling_offsets" in module_name
    else 1
)
optimizer.params.weight_decay_norm = None

dataloader.train.num_workers = 16

dataloader.train.total_batch_size = 16


train.amp.enabled = False
train.ddp.fp16_compression = False
