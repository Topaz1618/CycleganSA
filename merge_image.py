import cv2
import os

epoch_list = [20, 50, 80, 100]

img_list = os.listdir("output/mnist_cyclegan/20/images")
print(img_list)


def concat_handler(epoch_num):
    for img_name in img_list:

        if not img_name.endswith("fake.png"):
            continue

        name_pattern = img_name.split("_")
        name_pattern[-1] = "real.png"
        real_img_path = os.path.join(f"output/mnist_cyclegan/{epoch_num}/images", "_".join(name_pattern))
        basic_img_path = os.path.join(f"output/mnist_cyclegan/{epoch_num}/images", img_name)
        shallow_img_path = os.path.join(f"output/shallow_mnist_cyclegan/{epoch_num}/images", img_name)
        deep_img_path = os.path.join(f"output/deep_mnist_cyclegan/{epoch_num}/images", img_name)
        if not os.path.exists(real_img_path):
            continue

        if not os.path.exists(basic_img_path):
            continue

        if not os.path.exists(shallow_img_path):
            continue

        if not os.path.exists(deep_img_path):
            continue

        real_img = cv2.imread(real_img_path)
        basic_img = cv2.imread(basic_img_path)
        shallow_img = cv2.imread(shallow_img_path)
        # deep_img = cv2.imread(deep_img_path)


        if real_img is None:
            continue

        elif basic_img is None:
            continue

        elif shallow_img is None:
            continue
        #
        # elif deep_img is None:
        #     continue


        cv2.rectangle(real_img, (168, 232), (252, 248), (52, 163, 243), -1) # (29, 29, 253)
        cv2.putText(real_img, "Real imageA", (170, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (152, 243, 248), 1)

        cv2.rectangle(basic_img, (188, 232), (252, 248), (70, 70, 205), -1) # (254, 19, 144)
        cv2.putText(basic_img, f"CycleGan", (191, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 255, 255), 1)

        cv2.rectangle(shallow_img, (101, 232), (256, 248), (171, 108, 141), -1)
        cv2.putText(shallow_img, f"CycleGan(self attentionA)", (102, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 255, 255), 1) #(152, 243, 248)

        # cv2.rectangle(deep_img, (101, 232), (256, 248),  (57, 198, 164),  -1)
        # cv2.putText(deep_img, f"CycleGan(self attentionB)", (102, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 255, 241), 1) # (34, 105, 241),

        # concat_res = cv2.hconcat([real_img, basic_img, shallow_img, deep_img])
        concat_res = cv2.hconcat([real_img, basic_img, shallow_img])
        cv2.rectangle(concat_res, (2, 2), (72, 16), (61, 169, 61), -1) # (196, 61, 95)
        cv2.putText(concat_res, f"Epoch {epoch_num}", (5, 12), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255), 1)

        cv2.imwrite(f"output/mnist/{epoch_num}/{img_name}", concat_res)


for epoch_num in epoch_list:
    concat_handler(epoch_num)
