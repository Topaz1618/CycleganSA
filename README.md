# CycleGAN with Self-Attention and Semantic Segmentation



## Introduction
This repository contains the implementation of a CycleGAN model enhanced with self-attention mechanism and semantic segmentation for improved style transfer results. It includes experiments on the MNIST and horse2zebra (h2z) datasets. The enhancements lead to faster generation times and address the issue of blurred backgrounds in the transformed images.






## Results

### CycleGAN with Self-Attention & Semantic Segmentation
After adding self-attention and semantic segmentation, the generation speed and quality have significantly improved.


## CycleGAN with self-attention
It can be seen that the generation is faster than CycleGAN.

<img src='images/1.png' width='600' title=''>

(Original image -> CycleGAN output, CycleSA output)


## CycleGAN with Semantic Segmentation

  CycleGAN has an issue with blurred background after style transformation.
  <img src='images/horse2zebra.gif' width='600' title=''>

  The background issue has been solved after added semantic segmentation.
 <img src='images/n02381460_1920_real.png' width='600' title=''>

 (Original image -> CycleGAN output, CycleSA output)

## Environment
    - Python3
    - Pytorch
    - Ubuntu16.04/macOS

## Usage

### Training
To train with a shallow self-attention mechanism:

```bash
python train_sa.py --model_type shallow --dataroot datasets/horse2zebra/ --name h2z_sa_shallow

python train_sa.py --model_type shallow --dataroot datasets/mnist/ --name mnist_sa_shallow
```

To train with a deep self-attention mechanism:
```bash
python train_sa.py --model_type deep --dataroot datasets/horse2zebra/ --name h2z_sa_deep --gpu 0

python train_sa.py --model_type deep --dataroot datasets/mnist/ --name h2z_sa_deep
```

To train without self-attention mechanism:
```bash
python train_sa.py --dataroot datasets/horse2zebra/ --name h2z_sa_shallow

python train_sa.py--dataroot datasets/mnist/ --name mnist_sa_shallow
```

### Training Parameters
- `--dataroot`: Path to the dataset
- `--name`: Specific checkpoint location. (will be saved in checkpoint/{name})
- `--results_dir`: Directory to save the results
- `--gpu-ids`: IDs of GPUs to use, default is 0 for GPU, -1 for CPU
- `--model_type`:
-     shallow: Use self-attention in shallow CycleGAN
-     deep: Use self-attention in deep CycleGAN
-     default: Use the original CycleGAN


### Testing
```bash
 python test.py --gpu_ids -1
 python test.py --dataroot datasets/mnist/testA --name mnist_sa_deep --results_dir output/mnist/sa_shallow --direction AtoB
```

### Testing Parameters
- `--dataroot`: Path to the test images, ensure to select images from domain A or B
- `--name`: Specific checkpoint model location. (will be fetched from checkpoint/{name})
- `--results_dir`: Directory to save the results
- `--gpu-ids`: IDs of GPUs to use, default is 0 for GPU, -1 for CPU
- `--direction`: Specify the direction of the transformation, AtoB or BtoA


## Dataset
-- datasets
    └── dataset_name
        ├── domain_A
        └── domain_B


## Publication
My paper has been published by IEEE. You can access it here [A New CycleGAN-Based Style Transfer Method](https://ieeexplore.ieee.org/document/10361163).


# References
  - [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)





