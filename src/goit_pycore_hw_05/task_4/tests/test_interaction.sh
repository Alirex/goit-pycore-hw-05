#!/usr/bin/env bash
# [bash_init]-[BEGIN]
# Exit whenever it encounters an error, also known as a non–zero exit code.
set -o errexit
# Return value of a pipeline is the value of the last (rightmost) command to exit with a non-zero status,
#   or zero if all commands in the pipeline exit successfully.
set -o pipefail
# Treat unset variables and parameters other than the special parameters ‘@’ or ‘*’ as an error when performing parameter expansion.
set -o nounset
# Print a trace of commands.
#set -o xtrace
# [bash_init]-[END]

cat <<EOF | uv run task_4
all
add x1 +380880000001
add x2 +380880000002
add x3 +380880000003
add x4 +380880000004
add x5 +380880000005
add x6 +380880000006
add x7 +380880000007
add x8 +380880000008
all
add Bob +380111234567
add Alice +380997654321
all
change Bob +380220000000
all
bla
add bla foo
add bla foo141234
exit
EOF

echo "----- Restarting -----"

cat <<EOF | uv run task_4
all
close
EOF
