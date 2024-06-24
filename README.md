# TimeManagement
Simple time management for keeping track of hours spent.

Normal use is to set the startup part to be run on either boot or login, and the shutdown part to be run on either shutdown or logoff.
The Break script is meant to be used manually by running it when starting a break.
Adding an alias to .bashrc when runs the script is an easy solution

## Ubuntu
The install.sh script is created for installation on ubuntu installations and simply sets up a systemd service on user level.
Adding the Break feature is not handled by the install.sh.

## Windows
For windows build the startup, shutdown and break scripts separately with pyinstaller, if needed as exe files.
