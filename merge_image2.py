import cv2
import os



def concat_handler():
    for img_name in img_list:

        if not img_name.endswith("real.png"):
            continue

        real_name = os.path.join(input_path, img_name)

        name_pattern = img_name.split("_")
        name_pattern[-1] = "fake.png"
        fake_name = os.path.join(input_path, "_".join(name_pattern))

        name_pattern[-1] = "res.png"
        res_name = os.path.join(input_path, "_".join(name_pattern))

        if not os.path.exists(real_name):
            print(real_name)

            continue

        if not os.path.exists(fake_name):
            print(fake_name)

            continue

        if not os.path.exists(res_name):
            print(res_name)
            continue


        real_img = cv2.imread(real_name)
        fake_img = cv2.imread(fake_name)
        res_img = cv2.imread(res_name)


        if real_img is None:
            continue

        elif fake_img is None:
            continue

        elif res_img is None:
            continue


        # cv2.rectangle(real_img, (168, 232), (252, 248), (52, 163, 243), -1) # (29, 29, 253)
        # cv2.putText(real_img, "Real imageA", (170, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (152, 243, 248), 1)
        #
        # cv2.rectangle(basic_img, (188, 232), (252, 248), (70, 70, 205), -1) # (254, 19, 144)
        # cv2.putText(basic_img, f"CycleGan", (191, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 255, 255), 1)
        #
        # cv2.rectangle(shallow_img, (101, 232), (256, 248), (171, 108, 141), -1)
        # cv2.putText(shallow_img, f"CycleGan(self attentionA)", (102, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 255, 255), 1) #(152, 243, 248)

        # cv2.rectangle(deep_img, (101, 232), (256, 248),  (57, 198, 164),  -1)
        # cv2.putText(deep_img, f"CycleGan(self attentionB)", (102, 243), cv2.FONT_HERSHEY_COMPLEX, 0.35, (255, 255, 241), 1) # (34, 105, 241),

        # concat_res = cv2.hconcat([real_img, basic_img, shallow_img, deep_img])
        concat_res = cv2.hconcat([real_img, fake_img, res_img])
        # cv2.rectangle(concat_res, (2, 2), (72, 16), (61, 169, 61), -1) # (196, 61, 95)
        # cv2.putText(concat_res, f"Epoch {epoch_num}", (5, 12), cv2.FONT_HERSHEY_COMPLEX, 0.4, (255, 255, 255), 1)
        print(concat_res.shape, os.path.join(output_path, img_name))
        cv2.imwrite(os.path.join(output_path, img_name), concat_res)



if __name__ == "__main__":
    epoch_list = [20, 50, 80, 100]

    input_path = "/Users/Topaz/Downloads/sa/"
    output_path = "/Users/Topaz/Downloads/sa/res/"
    img_list = os.listdir(input_path)
    concat_handler()
