# Smart Dress Code automated determination of dress code compliance
Documentation about YOLOv7 read on [official repository github](https://github.com/WongKinYiu/yolov7). 

This fork was create for project Smart dress code. 

## Project Assignment

This project aims to create a service that will automatically determine by photo/video whether a person's clothes comply with a given dress code. This service can be used by both individuals and companies to check employees for dress code compliance in the workplace. It can also be used at the entrance of various establishments such as restaurants, clubs and conference rooms to ensure that guests comply with the set dress code. This project can improve productivity and customer service in various industries where dress code is an important aspect.

It is planned to release a beta version in the form of a Telegram bot, which will allow a test mode to look at the principle of operation and functionality of the service. For this purpose, users will be able to send photos/videos. In the future, we plan to develop a full-fledged service that will have the function of recognizing images from a webcam in real time.

## Step by step start 

### In shell

Create clone this repository

```shell
git clone https://github.com/999rse/smart-dress-code
```

Install all requirements
```shell
pip install -r requirements.txt
```

----

If you have some zip-data-archives with different data, you can use this pipeline for aggregate and split all your data to train and valid part. Use file `aggregate_data.py`. It's python CLI with next options:
```shell
options:
  -h, --help            show this help message and exit
  -r RAW_FOLDER, --raw_folder RAW_FOLDER
                        Path to folder with raw data (exmp. datasets.zip)
  -i INTERNAL_FOLDER, --internal_folder INTERNAL_FOLDER
                        Path to folder where will be contains internal data
  -p PROCESSED_FOLDER, --processed_folder PROCESSED_FOLDER
                        Path to folder where will be contain final data (splitted on train & valid parts)
  -t TRAINP, --trainp TRAINP
                        Number from 0 to 1 represent the proportion of the dataset to include in the train split (default=0.8)
```
The request looks like this (example)
```shell
python3 aggregate_data.py -r datasets/raw -i datasets/internal -p datasets/processed
```

----

and __DON'T FORGET__ add data.yaml to final folder (for exmp upper is dir: datasets/processed)

----

Download the weight you need

[`yolov7_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7_training.pt) [`yolov7x_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7x_training.pt) [`yolov7-w6_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-w6_training.pt) [`yolov7-e6_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6_training.pt) [`yolov7-d6_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-d6_training.pt) [`yolov7-e6e_training.pt`](https://github.com/WongKinYiu/yolov7/releases/download/v0.1/yolov7-e6e_training.pt)

Train model (full description read on official github, but this run is no different than the original)
```shell
python3 train.py --workers 8  --epochs 10 --batch-size 16 --data datasets/precessed/data.yaml --img 640 640 --cfg cfg/training/yolov7.yaml --weights 'yolov7_training.pt' --name sdc --hyp data/hyp.scratch.p5.yaml
```

Run evaluation
```shell
python3 detect.py --weights runs/train/sdc/weights/best.pt --conf 0.1 --source datasets/eval/myphoto.png
```

### In playbook.ipynb
Create clone this repository

```shell
git clone https://github.com/999rse/smart-dress-code
```

Start play all cells in playbook.ipynb



## Citation

```
@article{wang2022yolov7,
  title={{YOLOv7}: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors},
  author={Wang, Chien-Yao and Bochkovskiy, Alexey and Liao, Hong-Yuan Mark},
  journal={arXiv preprint arXiv:2207.02696},
  year={2022}
}
```

```
@article{wang2022designing,
  title={Designing Network Design Strategies Through Gradient Path Analysis},
  author={Wang, Chien-Yao and Liao, Hong-Yuan Mark and Yeh, I-Hau},
  journal={arXiv preprint arXiv:2211.04800},
  year={2022}
}
```


## Acknowledgements

<details><summary> <b>Expand</b> </summary>

* [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
* [https://github.com/WongKinYiu/yolor](https://github.com/WongKinYiu/yolor)
* [https://github.com/WongKinYiu/PyTorch_YOLOv4](https://github.com/WongKinYiu/PyTorch_YOLOv4)
* [https://github.com/WongKinYiu/ScaledYOLOv4](https://github.com/WongKinYiu/ScaledYOLOv4)
* [https://github.com/Megvii-BaseDetection/YOLOX](https://github.com/Megvii-BaseDetection/YOLOX)
* [https://github.com/ultralytics/yolov3](https://github.com/ultralytics/yolov3)
* [https://github.com/ultralytics/yolov5](https://github.com/ultralytics/yolov5)
* [https://github.com/DingXiaoH/RepVGG](https://github.com/DingXiaoH/RepVGG)
* [https://github.com/JUGGHM/OREPA_CVPR2022](https://github.com/JUGGHM/OREPA_CVPR2022)
* [https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose](https://github.com/TexasInstruments/edgeai-yolov5/tree/yolo-pose)

</details>
