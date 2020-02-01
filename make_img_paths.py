import os
filee = open('training_img_paths.txt','w')
given_dir = './coco/images/FLIR_Dataset/training/Data'
[filee.write(os.path.join(given_dir,i)+'\n') for i in os.listdir(given_dir)]
