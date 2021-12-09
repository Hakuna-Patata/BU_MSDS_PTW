# Author: Patrick Weatherford

# Branch Statuses
###################

#  Unstaged: *
#  Staged: +
#  Stashed: $
#  Untracked: %
#  Behind Upstream: <
#  Ahead of Upstream: >
#  Diverged: <>
#  No differences: =

###################


export GIT_PS1_SHOWDIRTYSTATE='y'
export GIT_PS1_SHOWSTASHSTATE='y'
export GIT_PS1_SHOWUNTRACKEDFILES='y'
export GIT_PS1_DESCRIBE_STYLE='contains'
export GIT_PS1_SHOWUPSTREAM='auto' 

PS1='\[\033]0;\W\007\]'; # window header is base working directory
PS1+='\n\n\[\e[0;38;5;246m\]-------------------------------------------------------\n';  # separator for each command/output
PS1+='\[\e[0;4;38;5;147m\]Git Bash';  # Start of prompt - light purple
PS1+='\[\e[0;38;5;252m\] ─>';  # arrow pointing to branch - light grey
PS1+='\[\e[0;1;38;5;190m\]';  # highlighter green/yellow - bold
if [ -z $(__git_ps1) ];  # if no found branches output 'No branches' else output the current working branch 
	then PS1+=' (No branches!)'
	else PS1+='`__git_ps1`'
fi
PS1+='${git_branch}';
PS1+='\[\e[0;38;5;147m\]'; # light purple
PS1+='\n';  # new line
PS1+='|\n'; # '|' connecting arrow which points to beggining of input start - light purple
PS1+='└─> ';  # elbow arrow pointing to beggining of input start - light purple 
PS1+='\[\e[0m\]';  # reset color settings


export PS1