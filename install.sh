#!/bin/bash -e
if(($EUID == 0)); then
	echo "Do not run as sudo"
	exit
fi
u="$USER"
sudo cp -r TimeManagement/ /usr/local/bin/
sudo chown -R $u:$u /usr/local/bin/TimeManagement
sudo cp worktimer.service /etc/systemd/user/
systemctl --user daemon-reload
systemctl start --user worktimer
systemctl enable --user worktimer
