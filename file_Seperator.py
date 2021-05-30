import os
from shutil import copyfile

train_images_file = open('val.txt')
line = train_images_file.readline()
while line:
    line = train_images_file.readline().split('\n')[0]
    print(line)
    copyfile('annotations_trainval/'+line+'.png', 'val_anno/'+line+'.png')
