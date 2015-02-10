#!/bin/sh
#
# ~/.xinitrc
#
# Executed by startx (run your window manager from here)

if [ -d /etc/X11/xinit/xinitrc.d ]; then
  for f in /etc/X11/xinit/xinitrc.d/*; do
    [ -x "$f" ] && . "$f"
  done
  unset f
fi

pnmixer &

# Set Compositing
# -C -l -O -D1 
xcompmgr -n -C -l -O -D1 &

# Start Dropbox
#dropboxd &

# Set wallpaper
sh ~/.fehbg &

conky -c ~/.conkyrc_full/conkyXL | while true; read line; do wmfs -c status "bottom $line"; done &
conky -c ~/.conkyrc1/conky | while true; read line; do wmfs -c status "testbar $line"; done &
#conky -c ~/.conkyrc1/conkyRightTestSB | while true; read line; do wmfs -c status "testbar $line"; done &
exec wmfs

#conky -c ~/.config/wmfs/scripts/conkyrc_bottom | while true; read line; do wmfs -c status "bottom $line"; done &
#WMFS

#exec mate-session

#exec gnome-session

# exec startxfce4


