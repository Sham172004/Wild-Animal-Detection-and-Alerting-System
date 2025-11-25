# %%
"""
<a href="https://colab.research.google.com/github/ckteja/Animal-Intrusion-Detection/blob/main/AIDsys.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
"""

# %%
from google.colab import drive
drive.mount('/content/gdrive')

# %%
!unzip gdrive/My\Drive/AID/animal.zip

# %%
!pip install utils

# %%
!git clone https://github.com/ultralytics/yolov5  # clone
%cd yolov5
%pip install -qr requirements.txt  # install
import torch
import utils
display = utils.notebook_init()  # checks

# %%
# Train YOLOv5s
!python train.py --img 415 --batch 31 --epochs 101 --data coco128.yaml --weights yolov5s.pt --cache

# %%
!python detect.py --weights runs/train/exp3/weights/best.pt --img 196 --conf 0.25 --source ../testpic.jpg

# %%
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

image = cv2.imread("runs/detect/exp6/testpic.jpg")
height, width = image.shape[:2]
resized_image = cv2.resize(image,(3*width, 3*height), interpolation = cv2.INTER_CUBIC)

fig = plt.gcf()
fig.set_size_inches(18, 10)
plt.axis("off")
plt.imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
plt.show()