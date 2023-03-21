params=$1
. models/crowsonkb/crowsonkb_env/bin/activate
cd models/crowsonkb
style_transfer ../../images/content_image.jpg ../../images/style_image.jpg  -ms 512 -s 512  -o ../../images/output.jpg --save-every 5 $params
cd ..
cd ..
deactivate
