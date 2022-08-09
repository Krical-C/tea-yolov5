rgb图片和标签
链接：https://pan.baidu.com/s/1RAg1IojMv3HFOl1NIFrtng 
提取码：oq2i

label-new解压后放到data/Annotations
image-new解压后放到data/src_images
先运行split_train_val.py进行数据及划分
然后运行text_to_yolo.py进行数据集格式转化(这个文件下的路径需要更改)


可使用命令行运行
训练
python train.py --weights weights/yolov5s.pt  --cfg models/yolov5s.yaml  --data data/myvoc.yaml --epoch 900 --batch-size 1 --img 1600   --device 0
测试
python detect.py --weights runs/train/exp3/weights/best.pt --source ./data/test/xxx.JPG

目前我留了四个训练集运行结果在run/train下

exp40 exp41是57张rgb标签训练结果 
测试结果在run/detect

exp42 exp43是5张图相同标签个数下真彩和伪彩的训练结果,因为训练效果都不好所以没进行测试
