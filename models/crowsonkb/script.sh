. models/crowsonkb/crowsonkb_env/bin/activate
cd models/crowsonkb
style_transfer ../../images/content_image.jpg ../../images/style_image.jpg  -ms 512 -s 512  -ii 1000 -o ../../images/output.jpg
cd ..
cd ..
deactivate
