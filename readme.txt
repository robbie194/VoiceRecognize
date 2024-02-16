
直接运行ui_main.py即可
送一个语音互动播报功能


需要按安装的包
speech_recognition
vosk
pyttsx3


需要去 https://alphacephei.com/vosk/models 下载英语和汉语离线包
我现在demo使用的是最小的模型，所以识别效果有限
下载好之后，在ui_main.py中，更改成你本地路径：
cn_model_path
en_model_path
模型的名字不要随便修改，因为通过名字中是否包含 “cn” 和 “en” 来区分中英文模型

录音文件格式有要求，最好是wav文件（已验证，稳定），其他格式文件可以先转化成该格式
录音文件命名的时候，也要包含 “cn” 和 “en” 来区分调用中英文哪个模型

