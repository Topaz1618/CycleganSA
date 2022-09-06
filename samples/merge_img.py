import cv2
import os


def concat_handler():
    data = []
    for idx, img_name in enumerate(sorted(img_list)):
        print(img_name)
        if img_name.endswith("png"):
            print(os.path.join(input_path, img_name))
            img = cv2.imread(os.path.join(input_path, img_name))
            # if idx == 2 or idx == 3:
            #     img = cv2.flip(img, 1)
            data.append(img)

    print(data)
    return data


if __name__ == "__main__":
    epoch_list = [20, 50, 80, 100]
    input_path = "data/ss"
    output_path = "data/ss"

    img_list = os.listdir(input_path)
    print(img_list)
    img_list = concat_handler()
    concat_res = cv2.vconcat(img_list)
    cv2.imwrite(os.path.join(output_path, "res.png"), concat_res)

