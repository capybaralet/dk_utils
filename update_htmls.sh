#!/bin/sh
# This is a comment
#echo "List of files in lisa/exp/*/tmp:"
#ls /data/lisa/exp/kruegerd/tmp/*.png
#cp /data/lisa/exp/kruegerd/tmp/*.png /home/www-etud/kruegerd/public_html/
#cp /data/lisa/exp/kruegerd/tmp/*.html /home/www-etud/kruegerd/public_html/


#echo "List of files in rondoudou/exp:"
#ls /u/kruegerd/rondoudou/exp/*.png
#cp /u/kruegerd/rondoudou/exp/*.png /home/www-etud/kruegerd/public_html/
#cp /u/kruegerd/rondoudou/exp/*.html /home/www-etud/kruegerd/public_html/


#echo "List of files in /exp/NICE:"
#ls /data/lisa/exp/kruegerd/NICE/*.png
#cp /data/lisa/exp/kruegerd/NICE/*.png /home/www-etud/kruegerd/public_html/
#cp /data/lisa/exp/kruegerd/NICE/*.html /home/www-etud/kruegerd/public_html/


#echo "List of files in lisa/exp/:"
#ls /data/lisa/exp/kruegerd/*.png
#cp /data/lisa/exp/kruegerd/*.png /home/www-etud/kruegerd/public_html/
#cp /data/lisa/exp/kruegerd/*.html /home/www-etud/kruegerd/public_html/


#echo "List of files in lisa/exp/rnn-vae:"
#ls /data/lisa/exp/kruegerd/rnn-vae/*.png

#cp /data/lisa/exp/kruegerd/rnn-vae/*.png /home/www-etud/kruegerd/public_html/
#cp /data/lisa/exp/kruegerd/rnn-vae/*.html /home/www-etud/kruegerd/public_html/


echo "List of files in lisa/exp/kruegerd/layer_wise_training/:"

ls /data/lisa/exp/kruegerd/layer_wise_training/*.png
cp /data/lisa/exp/kruegerd/layer_wise_training/*.png /home/www-etud/kruegerd/public_html/
cp /data/lisa/exp/kruegerd/layer_wise_training/*.html /home/www-etud/kruegerd/public_html/

chmod 755 /home/www-etud/kruegerd/public_html/*.png
chmod 755 /home/www-etud/kruegerd/public_html/*.html
