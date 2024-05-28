if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi
export ZSH="/home/developer/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(git)

source $ZSH/oh-my-zsh.sh
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(my_rosenv $POWERLEVEL9K_LEFT_PROMPT_ELEMENTS)
# cache credentials
git config --global credentials.helper cache --timeout=3h

# fix CTRL+left/right/backspace/delete
bindkey '^[[1;5D' backward-word
bindkey '^[[1;5C' forward-word
bindkey '^H' backward-kill-word
bindkey '5~' kill-word

source /opt/ros/noetic/setup.zsh

# add alias for common build instruction
rebuild-ws() {
  cd /home/developer/ros-playground/workspaces/hrwros_ws
  catkin build
  source devel/setup.zsh
  function prompt_my_rosenv() {
    p10k segment -f 208 -t '(hrwros_ws)'
  }
}