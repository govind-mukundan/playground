#!/usr/bin/env bash
# Tells the shell/loader to look in the environment $PATH for the "bash" program
# Quick reference - https://ss64.com/bash/test.html

# Bash has a large number of "builtin" commands lile echo, if etc - https://www.tldp.org/LDP/abs/html/internal.html#SETREF
# set builtin can set bash internal flags
set -ex   # Exit in first error, Print commands (with a +) as you execute them

# Arguments to the script
# The $N syntax helps you extract arguments. $0 is the name of the script, $* is all the arguments, $# is the number of params
# Another more powerful option is to use the GETOPTS builtin
echo $@
echo "$*"  # Quotes the arguments
echo $*
set +x  # Disable the verbose option set earlier

# CONDITIONALS
# Testing conditions is done using the "test" program aka [ or [[
# Both versions expect a closing ] or ]] argument. [[ is the newer version
# In addition to numerical values, various FILE and STRING tests are available

if [[ $# -lt 3 ]]; then
  printf "We don't have enough arguments, I want at least 3\n"
  exit -1
fi

# printf is another builtin that can do more than echo
# Note the quote for the last args
printf "All Args = %s\n" "$*"
printf "Args (0,1,2 ..) = %s %s %s\n" $0 $1 $2

case "$1" in
    'start')
            start
            ;;
    'wake' | 'hello')  # You can have multiple cases
            printf "hello world\n"
            ;;
    'sleep')
            echo "Sleeping..."; sleep 1 ;
            ;;
    *)
            printf "Try a \"hello\"\n"
            ;;
esac

printf "Testing functions ... \n"

# The same $N scheme works with functions defined within a script
my_function() {
printf "My Function arguments = {%s}\n" "$*"

}

my_function 'Govind' 'mukundan'

echo "Some AWK to print the PID of the bash shells running"
ps -ef | grep -v grep | grep bash | awk '{print $1, $2}'
# grep -v grep removes the grep process searching for bash from the initial grep output

exit 0