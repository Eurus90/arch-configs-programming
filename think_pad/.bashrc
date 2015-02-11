#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='\[\033[1;34m\]\u@\h \[\033[1;36m\]\W \$ \[\033[0;37m\]'
