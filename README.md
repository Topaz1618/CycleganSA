# 200 epoch
python train.py --dataroot ./datasets/maps --name maps_cyclegan --model cycle_gan --gpu_ids -1

#
python test.py --dataroot datasets/horse2zebra/lit --name horse2zebra_pretrained --model test --no_dropout --results_dir ~/Desktop/images

scp -ri ../my_gpu.pem ubuntu@3.140.208.99:/home/ubuntu/pytorch-CycleGAN-and-pix2pix/results/horse2zebra_pretrained/test_latest/images .


# dataset: https://www.kaggle.com/datasets/allexmendes/synthetic-gaze-and-face-segmentation?rvi=1

# test
python test.py --dataroot datasets/horse2zebra/testA --name horse2zebra_pretrained --model test --no_dropout --results_dir ~/Desktop/images

----------------- Options ---------------
             aspect_ratio: 1.0
               batch_size: 1
          checkpoints_dir: ./checkpoints
                crop_size: 256
                 dataroot: datasets/horse2zebra/testA
             dataset_mode: single
                direction: AtoB
          display_winsize: 256
                    epoch: latest
                     eval: False
                  gpu_ids: -1
                init_gain: 0.02
                init_type: normal
                 input_nc: 3
                  isTrain: False                         	[default: None]
                load_iter: 0                             	[default: 0]
                load_size: 256
         max_dataset_size: inf
                    model: test
             model_suffix:
               n_layers_D: 3
                     name: horse2zebra_pretrained
                      ndf: 64
                     netD: basic
                     netG: resnet_9blocks
                      ngf: 64
               no_dropout: False
                  no_flip: False
                     norm: instance
                 num_test: 50
              num_threads: 4
                output_nc: 3
                    phase: test
               preprocess: resize_and_crop
              results_dir: ~/Desktop/images
           serial_batches: False
                   suffix:
                use_wandb: False
                  verbose: False
----------------- End -------------------



