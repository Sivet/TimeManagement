#!/bin/bash
if(($EUID != 0)); then
	echo "Please run as sudo"
	exit
fi
u="$SUDO_USER"
cp -r TimeManagement/ /usr/local/bin/ &&
chown -R $u:$u /usr/local/bin/TimeManagement &&
cp worktimer.service /etc/systemd/user/ &&
systemctl --user daemon-reload &&
systemctl start --user worktimer &&
systemctl enable --user worktimer
