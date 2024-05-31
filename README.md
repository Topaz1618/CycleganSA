# CycleGAN with Self-Attention and Semantic Segmentation



## Introduction
This repository contains the implementation of a CycleGAN model enhanced with self-attention mechanism and semantic segmentation for improved style transfer results. It includes experiments on the MNIST and horse2zebra (h2z) datasets. The enhancements lead to faster generation times and address the issue of blurred backgrounds in the transformed images.






## Results

### CycleGAN with Self-Attention
The addition of the self-attention mechanism shows a significant improvement in generation speed compared to the original CycleGAN.


## CycleGAN with self-attention
   It can be seen that the generation is faster than CycleGAN.

<img src='images/1.png' width='600' title=''>

(Original image -> CycleGAN output, CycleSA output)


## Semantic segmentation

  CycleGAN has an issue with blurred background after style transformation.
  <img src='images/horse2zebra.gif' width='600' title=''>

  The background issue has been solved after added semantic segmentation.
 <img src='images/n02381460_1920_real.png' width='600' title=''>

 (Original image -> CycleGAN output, CycleSA output)

# Environment
    Python3
    Pytorch
    Ubuntu16.04/macOS



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

```
--dataroot: Path to the test images, ensure to select images from domain A or B.
--name: Checkpoint location => checkpoint/{mnist_sa_deep}
--results_dir: Directory to save the results.
--gpu-ids: Default is 0 for GPU, -1 for CPU.
--direction: Specify the direction of transformation, either AtoB or BtoA.
--model_type:
    shallow: Self-attention in shallow CycleGAN.
    deep: Self-attention in deep CycleGAN.
    default: Original CycleGAN.

```






# Results
    Add self-attention mechanism and semantic segmentation




 python test.py --gpu_ids -1
 python test.py --dataroot datasets/mnist/testA --name mnist_sa_deep --results_dir output/mnist/sa_shallow --direction AtoB
 --dataroot 测试图片路径，注意选择 A 域或者 B 域图片
 --name mnist_sa_deep  checkpoint位置 => checkpoint/{mnist_sa_deep}
 -- results_dir 结果保存位置
 --direction AtoB or BtoA



## Dataset
-- datasets
    dataset_name
        A 域
        B 域


## Publication
My paper has been published by IEEE. You can access it here [A New CycleGAN-Based Style Transfer Method](https://ieeexplore.ieee.org/document/10361163).


# References
  - [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)





