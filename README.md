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
   From left to right are the results of original image, CycleGAN, CycleSA. It can be seen that the generation is faster than CycleGAN.

<img src='images/1.png' width='600' title=''>

## CycleGAN with semantic segmentation

  CycleGAN has an issue with blurred background after style transformation.
  <img src='images/horse2zebra.gif' width='600' title=''>

  It can be seen that the background blur problem has been solved. From left to right is the original image, CycleGAN, CycleSA.
 <img src='images/n02381460_1920_real.png' width='600' title=''>


# References
  - [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)
