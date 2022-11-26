# Datasets
    - Mnist
    - h2z

# Environment
    Python3
    Pytorch
    Ubuntu16.04/macOS



# Results
    Add self-attention mechanism and semantic segmentation

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


# References
  - [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
