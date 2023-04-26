. models/zhanghang/zhanghang_env/bin/activate
python3.6 models/zhanghang/experiments/main.py eval --content-image images/content_image.jpg --style-image images/style_image.jpg --output-image images/output.jpg  --model models/zhanghang/experiments/models/21styles.model --cuda=0
deactivate
