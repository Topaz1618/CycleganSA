import os
import pandas as pd
import csv
# import scipy.misc as sm


def create_csv():
    name = os.listdir('testA')
    with open('test.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['data', 'label'])
        for img_name in names:
            print("img_name", img_name)
            if fname.endswith(".jpg"):
                writer.writerow(['./dataset/'+str(dirname) +'/'+ str(n), './dataset/' + str(dirname) + 'label/' + str(n[:-4] + '.png')])


# csv = pd.read_csv("AgeDataset-V1.csv", header=0)
# # print("csv", csv)
#
# img_paths=[]
# file_folder = ""
# for index in csv.index:
#     image = str(csv.loc[index].values[0])
#     # image_name = os.path.join(file_folder, image)
#     image_name = image
#     print(index, image_name)
#     img_path.append(image_name)
#     # labels.append(label)
#
# print(img_paths)


create_csv()