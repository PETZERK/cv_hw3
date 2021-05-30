## cv_hw3 semantic segmentation

models.py:存放训练使用模型

train.py:训练代码，自行修改内部路径

file_Seperator:将VOC训练集格式分割为train，val，test三个文件夹，自行修改格式

inference:预测代码，自行修改路径，预测结果放在test_result或val_result

eval.py:计算mean IOU，自行修改路径,使用annotation_trainval和val_result

annotation_trainval:存放训练集与验证集标注文件

images:存放所有原始图片

