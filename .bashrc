. ~/.profile

######################
# Want to customize! (also other rc files, VIM, etc...)
#
# Need to check out Theano paths and version and whatnot...
#
# Can clean up a bit, also need to figure out once and for all: which direction is the path read in (I think it's top down?)
#
# Is there something I'm doing that makes my paths get copied? I don't know what that would be...
#
#######################


# for newer version of Mayavi/Python (seems to break matplotlib, tho!)
#comment out first two lines and 'el' BEFORE LOGOUT!
#if [ -e "/opt/lisa/os_v2/.local.bashrc" ];then
#   source /opt/lisa/os_v2/.local.bashrc
#el

#if [ -e "/opt/lisa/os/.local.bashrc" ];then
#    source /opt/lisa/os/.local.bashrc
#elif [ -e /data/lisa/data/local_export/.local.bashrc ];then
#    source /data/lisa/data/local_export/.local.bashrc
#fi


if [ -e "/opt/lisa/os_v3/.local.bashrc" ];then
    source /opt/lisa/os_v3/.local.bashrc
elif [ -e "/opt/lisa/os/.local.bashrc" ];then
    source /opt/lisa/os/.local.bashrc
elif [ -e /data/lisa/data/local_export/.local.bashrc ];then
    source /data/lisa/data/local_export/.local.bashrc
fi

#if [ -e "/opt/lisa/os/.local.bashrc" ];then source /opt/lisa/os/.local.bashrc; else source /data/lisa/data/local_export/.local.bashrc; fi

function nviz()
{
    while true; do 
    nvidia-smi;
    sleep $1;
    done
}

function swap()         
{
    local TMPFILE=tmp.$$
    mv "$1" $TMPFILE
    mv "$2" "$1"
    mv $TMPFILE "$2"
}


function cph()
{
    cp $1 /home/www-etud/kruegerd/public_html/
    chmod 755 /home/www-etud/kruegerd/public_html/$1
}

function lss()
{
    ls *$1*
}



cc() {
        cd $1
            ls
}

export EDITOR=vim

export HISTSIZE=100000

# set pylearn viewer
export PYLEARN2_VIEWER_COMMAND="eog --new-instance"


export PATH=$PATH:/u/kruegerd/repo/pylearn2/pylearn2/scripts/
export PATH=/u/kruegerd/dk_utils/:${PATH}
export PATH=$PATH:/opt/cuda-5.5.22/bin/

export PYTHONPATH=$PYTHONPATH:/u/kruegerd/repo/pylearn2/pylearn2/scripts/
# this was commented out, not sure why...
export PYTHONPATH=~/.local/lib/python2.7/site-packages:${PYTHONPATH}
#export PYTHONPATH=/data/lisa_ubi/kruegerd/speechgeneration/3rdparty/hgae_code:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/synergistic:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/IFT6085/mcd-0.2:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/synergistic/sae_on_norb:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/Theano:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/ubi_faces:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/lisa_emotiw:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/utilities:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/TTS_current:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/ift6266project:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/TTS_current/IFT6266_Project_Vincent:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/pylearn2/pylearn2:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/pylearn2/pylearn2/scripts:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/TTS_current/sheldon:${PYTHONPATH}
export PYTHONPATH=/data/lisa_ubi/speech/onomatopoeia/dataset/loud_silence_free:${PYTHONPATH}
export PYTHONPATH=/data/lisa_ubi/speech/onomatopoeia/dataset:${PYTHONPATH}
export PYTHONPATH=/data/lisa_ubi/kruegerd:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/TTS_current:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/TTS_current/speechgeneration:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/TTS_current/speechgeneration/pgp_scan:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/rondoudou:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/pylearn2:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/Sum-of-Functions-Optimizer:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/repo/Whetlab-Python-Client:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/dk_utils:${PYTHONPATH}
export PYTHONPATH=/u/kruegerd/local_installs/lib/python2.7/site-packages:${PYTHONPATH}

#export PATH=${PATH/\/opt\/diro\/bin/}

export MATLABPATH=$MATLABPATH:/u/kruegerd/TTS_current/
export MATLABPATH=$MATLABPATH:/u/kruegerd/repo/face-release1.0-basic/
export MATLABPATH=$MATLABPATH:/u/kruegerd/repo/lisa_emotiw/emotiw/raymonjp/face-release1.0-basic/:/data/lisa/exp/raymonjp/Ramanan/face-release1.0-basic/
export MATLABPATH=$MATLABPATH:/data/lisa_ubi/speech/STRAIGHTV40pcode/
export MATLABPATH=$MATLABPATH:/data/lisa_ubi/speech/

export HDF5_DISABLE_VERSION_CHECK=1

umask 027

export PYLEARN2_PICKLE_PROTOCOL=pickle.HIGHEST_PROTOCOL

export PYLEARN2_DATA_PATH=/data/lisa/data/
export MUMBLER_DATA_PATH=/data/lisa/data/timit/
export EXP_PATH=/data/lisa/exp/kruegerd/
export TMP_EXP_PATH=/data/lisa/exp/kruegerd/tmp/

[ -r ~/.git-bash-completion.sh ]  && . ~/.git-bash-completion.sh


# ALIASES
# for git
alias gba='git branch -a'
alias gs='git status'
alias ga='git add'
alias gap='git add -p'
alias gau='git add -u'
alias gbv='git branch -vv'
alias gd='git diff'
alias vigi='vi .gitignore'
alias grm='git rm'
alias gc='git commit -m'

# cd
alias ,.='cd -'
alias ..='cd ..'
alias pylearn='cd ~/repo/pylearn2/pylearn2'
alias mod='cd ~/repo/pylearn2/pylearn2/models'
alias ut='cd ~/dk_utils'
alias articles='cd ~/repo/articles/'
alias Texp='cd /Tmp/kruegerd/exp'
alias amod='cd ~/TTS_current/egg/alex_graves_reproduce/pylearn2/models'
alias k='cd /data/lisa_ubi/kruegerd/'
alias scripts='cd ~/repo/pylearn2/pylearn2/scripts'
alias exp='cd /data/lisa/exp/kruegerd'
alias lisatmp='cd /data/lisatmp/kruegerd'
alias lisatmp2='cd /data/lisatmp2/kruegerd'
alias lisatmp3='cd /data/lisatmp3/kruegerd'
alias utils='cd ~/dk_utils'
alias repo='cd ~/repo'

# cd (PROJECTS)
alias timit='cd /data/lisa/data/timit/readable/ubi'
alias rol='cd ~/rondoudou/exp'
alias Nice='cd /data/lisa/exp/kruegerd/NICE/'
alias rv='cd /data/lisa/exp/kruegerd/rnn-vae/'
alias ex='cd /u/kruegerd/TTS_current/egg/exp/egg/'
alias egg='cd /u/kruegerd/TTS_current/egg/'
alias aex='cd /u/kruegerd/TTS_current/egg/exp/alex_exp/'
alias rvae='cd /data/lisatmp3/kruegerd/rnn-vae_10_07/'
alias vae='cd /u/kruegerd/TTS_current/sheldon'
alias TTS='cd ~/TTS_current'
alias ubi='cd /data/lisa_ubi/speech/onomatopoeia/dataset'
alias sg='cd /u/kruegerd/TTS_current/speechgeneration'
alias sgp='cd /u/kruegerd/TTS_current/speechgeneration/pgp_scan'
alias develop='cd /u/kruegerd/develop'


alias bup='bash /u/kruegerd/dk_utils/update_htmls.sh'
alias vup='vi /u/kruegerd/dk_utils/update_htmls.sh'
alias vip='vi ~/planner.txt'
alias vipi='vi ~/project_ideas.txt'
alias vut='vi ~/dk_utils/utils.py'
alias psk='ps aux | grep kruegerd'
alias lr='ll -rt'

alias killme='pkill -u kruegerd'
alias gr='grep -rn'
alias gri='grep -rnI'
alias vbash='vim ~/.bashrc'
alias sbash='source ~/.bashrc'
alias lbash='less ~/.bashrc'
alias psp='ps aux | grep python' 
alias psk='ps aux | grep kruegerd'
alias p='python'
alias ip='ipython --pylab -i ~/dk_utils/utils.py'
alias pk='pkscreen -h 100000' # this only works for the 1st screen opened (others have the normal scrollback length (*short))
alias sr='screen -r'
alias sl='screen -ls'
alias sx='screen -x'
alias S='ssh -X'

# managing directories:
alias cpdir='cp -avr'
alias rmdr='rm -rf'
alias cput='cp ~/dk_utils/utils.py ./'

alias train='/u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py'
alias plot_monitor='/u/kruegerd/repo/pylearn2/pylearn2/scripts/plot_monitor.py'

alias nvi='nvidia-smi'
alias nvis='while true; do nvidia-smi; sleep .1; done'

alias lbs='du -sk * | sort -n'


# THEANO FLAGS
alias TFc='THEANO_FLAGS=device=gpu,floatX=float32,optimizer_including=conv_gemm /u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py'
alias TFd='THEANO_FLAGS=optimizer=None,exception_verbosity=high,compute_test_value=raise,mode=FAST_COMPILE,device=gpu,floatX=float32 ipdb /u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py' 
alias TFdd='THEANO_FLAGS=exception_verbosity=high,compute_test_value=raise,device=gpu,floatX=float32 ipdb /u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py' 
alias TFdddd='THEANO_FLAGS=optimizer=fast_compile,exception_verbosity=high,compute_test_value=raise,device=gpu,floatX=float32 ipdb /u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py' 
alias TFdl='THEANO_FLAGS=exception_verbosity=high,compute_test_value=raise,device=gpu,floatX=float32 /u/kruegerd/rondoudou/pylearn2/scripts/train.py' 
alias TFdldb='THEANO_FLAGS=exception_verbosity=high,compute_test_value=raise,device=gpu,floatX=float32 ipdb /u/kruegerd/rondoudou/pylearn2/scripts/train.py' 
alias TF64='THEANO_FLAGS=device=gpu,floatX=float64 /u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py'

alias TFC='THEANO_FLAGS=device=cpu,floatX=float32'
alias TFE='THEANO_FLAGS=device=gpu,floatX=float32,exception_verbosity=high'
alias TFde='THEANO_FLAGS=device=gpu,floatX=float32,exception_verbosity=high,compute_test_value=raise ipdb' 
alias TFt='THEANO_FLAGS=device=gpu,floatX=float32 /u/kruegerd/repo/pylearn2/pylearn2/scripts/train.py'
alias TF='THEANO_FLAGS=device=gpu,floatX=float32'
alias TF0='THEANO_FLAGS=device=gpu0,floatX=float32'
alias TF1='THEANO_FLAGS=device=gpu1,floatX=float32'
alias TF2='THEANO_FLAGS=device=gpu2,floatX=float32'

alias T='THEANO_FLAGS=device=gpu,floatX=float32 ipython --pylab -i ~/dk_utils/utils.py'
alias T0='THEANO_FLAGS=device=gpu0,floatX=float32 ipython --pylab -i ~/dk_utils/utils.py'
alias T1='THEANO_FLAGS=device=gpu1,floatX=float32 ipython --pylab -i ~/dk_utils/utils.py'
alias TT='THEANO_FLAGS=device=gpu,floatX=float32,exception_verbosity=high ipython --pylab -i ~/dk_utils/utils.py'
alias TTT='THEANO_FLAGS=device=gpu,floatX=float32,exception_verbosity=high,optimizer=fast_compile ipython --pylab -i ~/dk_utils/utils.py'

