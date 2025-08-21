# compose
❯ ./compose.py --help
usage: compose.py [-h] [-u URL] [-r RPMSJSON] [-l [LIST_COMPOSES]] [-d TWO_COMPOSES]

compose rpm change log

options:
  -h, --help            show this help message and exit
  -u, --url URL         URL of fedora compose
  -r, --rpmsjson RPMSJSON
                        care about the rpms.json file
  -l, --list [LIST_COMPOSES]
                        Outputs a list of Rawhide composes built in the past X days ; sorted as the first = the oldest
  -d, --diff TWO_COMPOSES
                        specify TWO composes: -d one -d two for.ex. --diff Fedora-Rawhide-20250807.n.1 --diff Fedora-Rawhide-20250814.n.0"


# is options used correctly?
--list
should be used separately

--diff one_compose --diff second_compose
there are 2x --diff with checking real composes from (--list)

# wrong combination of options

❯ ./compose.py -l ahoj
usage: compose.py [-h] [-u URL] [-r RPMSJSON] [-l [LIST_COMPOSES]] [-d TWO_COMPOSES]
compose.py: error: argument -l/--list: invalid int value: 'ahoj'
❯ ./compose.py -l -d
usage: compose.py [-h] [-u URL] [-r RPMSJSON] [-l [LIST_COMPOSES]] [-d TWO_COMPOSES]
compose.py: error: argument -d/--diff: expected one argument
❯ ./compose.py -d Fedora-Rawhide-20250821.n.0 -d Fedora-Rawhide-20
composes DOES not match --list
❯ ./compose.py -d Fedora-Rawhide-20250821.n.0 -d rockylinux-1
composes DOES not match --list


# GOOD USAGE
## --list 
### list all
❯ ./compose.py -l
Fedora-Rawhide-20250807.n.0
Fedora-Rawhide-20250807.n.1
Fedora-Rawhide-20250808.n.0
Fedora-Rawhide-20250809.n.0
Fedora-Rawhide-20250810.n.0
Fedora-Rawhide-20250811.n.0
Fedora-Rawhide-20250812.n.0
Fedora-Rawhide-20250812.n.1
Fedora-Rawhide-20250813.n.0
Fedora-Rawhide-20250813.n.1
Fedora-Rawhide-20250814.n.0
Fedora-Rawhide-20250814.n.1
Fedora-Rawhide-20250815.n.0
Fedora-Rawhide-20250816.n.0
Fedora-Rawhide-20250817.n.0
Fedora-Rawhide-20250818.n.0
Fedora-Rawhide-20250819.n.0
Fedora-Rawhide-20250820.n.0
Fedora-Rawhide-20250821.n.0

### list only 2 oldest avaiable composes, sort by the oldest
❯ ./compose.py -l 2
Fedora-Rawhide-20250807.n.0
Fedora-Rawhide-20250807.n.1

## --diff , compare two composes
Firstly it checks wheter composes really exist. It checks wheter user added two composes.

❯ ./compose.py -d Fedora-Rawhide-20250821.n.0 -d Fedora-Rawhide-20250820.n.0
old compose  : Fedora-Rawhide-20250820.n.0
new compose  : Fedora-Rawhide-20250821.n.0
temp dir:      /tmp/tmp_2g8lsxc
Downloaded to: /tmp/tmp_2g8lsxc/Fedora-Rawhide-20250820.n.0-rpms.json
Downloaded to: /tmp/tmp_2g8lsxc/Fedora-Rawhide-20250821.n.0-rpms.json
golang-github-azure-sdk-resourcemanager-resourcegraph-armresourcegraph REMOVED golang-github-azure-sdk-resourcemanager-resourcegraph-armresourcegraph0:0.9.0-3
greenboot REMOVED greenboot0:0.15.8-2
greenboot-rs ADDED greenboot-rs0:0.16.0-3
jfrog-cli ADDED jfrog-cli0:2.78.3-1
mingw-appstream ADDED mingw-appstream0:1.0.6-1
pgbouncer ADDED pgbouncer0:1.24.1-5
0xFFFF CHANGED 0:0.10-14 -> 0:0.10-16
389-ds-base CHANGED 0:3.1.3-8 -> 0:3.1.3-9
aide CHANGED 0:0.19.1-2 -> 0:0.19.2-1
anaconda CHANGED 0:43.35-2 -> 0:43.36-1
ansible-collection-community-general CHANGED 0:11.1.1-1 -> 0:11.2.1-1
asahi-scripts CHANGED 0:20250713-3 -> 0:20250713-5
cockpit-image-builder CHANGED 0:73-1 -> 0:74-1
cosmic-bg CHANGED 0:1.0.0~alpha.7-2 -> 0:1.0.0~alpha.7-3
cosmic-settings CHANGED 0:1.0.0~alpha.7-2 -> 0:1.0.0~alpha.7-3
ed CHANGED 0:1.22.1-1 -> 0:1.22.2-1
fail2ban CHANGED 0:1.1.0-10 -> 0:1.1.0-11
ffmpeg CHANGED 0:7.1.1-7 -> 0:7.1.1-8
fping CHANGED 0:5.3-4 -> 0:5.4-1
ghc9.2 CHANGED 0:9.2.8-28 -> 0:9.2.8-30
git CHANGED 0:2.50.1-2 -> 0:2.51.0-1
gram_grep CHANGED 0:0.9.9-2 -> 0:0.9.9-3
gtkwave CHANGED 0:3.3.124-2 -> 0:3.3.125-1
kernel CHANGED 0:6.17.0-0.rc2.24 -> 0:6.17.0-0.rc2.250820gb19a97d57c15.26
lexertl17 CHANGED 1:1.2.4-1 -> 1:1.2.5-1
libaec CHANGED 0:1.1.4-2 -> 0:1.1.4-3
libcpuid CHANGED 0:0.8.0-5 -> 0:0.8.1-1
magic CHANGED 0:8.3.538-1 -> 0:8.3.543-1
mcomix3 CHANGED 0:0-0.40.D20211016git483f4b3 -> 0:0-0.41.D20211016git483f4b3
mdadm CHANGED 0:4.3-8 -> 0:4.3-9
mingw-filesystem CHANGED 0:150-2 -> 0:150-3
mingw-gtk4 CHANGED 0:4.14.4-3 -> 0:4.19.2-1
mpibash CHANGED 0:1.4-2 -> 0:1.4-7
nbdkit CHANGED 0:1.45.4-1 -> 0:1.45.5-1
nfs-utils CHANGED 1:2.8.3-2.rc3.fc43 -> 1:2.8.3-3.rc3
nodejs-packaging CHANGED 0:2023.10-9 -> 0:2023.10-10
nudoku CHANGED 0:5.0.0-3 -> 0:6.0.0-1
opensips CHANGED 0:3.6.0-3 -> 0:3.6.1-1
perl-Class-Autouse CHANGED 0:2.01-42 -> 0:2.02-1
perl-Prima CHANGED 0:1.76-3 -> 0:1.77-1
plexus-velocity CHANGED 0:2.0-9 -> 0:2.2.1-2
poedit CHANGED 0:3.6.3-3 -> 0:3.7-1
python-Mastodon CHANGED 0:2.1.1-1 -> 0:2.1.2-1
python-atlassian-python-api CHANGED 0:4.0.4-4 -> 0:4.0.5-1
python-boto3 CHANGED 0:1.40.11-1 -> 0:1.40.14-1
python-botocore CHANGED 0:1.40.11-1 -> 0:1.40.14-1
python-dasbus CHANGED 0:1.7-11 -> 0:1.7-12
python-distlib CHANGED 0:0.3.9-3 -> 0:0.4.0-1
python-ogr CHANGED 0:0.55.0-4 -> 0:0.56.0-1
python-peewee CHANGED 0:3.18.2-2 -> 0:3.18.2-4
python-rpds-py CHANGED 0:0.26.0-2 -> 0:0.27.0-1
python-sgp4 CHANGED 0:2.24-4 -> 0:2.25-1
python-ufo2ft CHANGED 0:3.6.0-1 -> 0:3.6.0-3
python-uharfbuzz CHANGED 0:0.51.1-2 -> 0:0.51.2-1
python-websockets CHANGED 0:15.0.1-7 -> 0:15.0.1-8
qmmp-plugin-pack CHANGED 0:2.2.2-2 -> 0:2.2.2-3
qutebrowser CHANGED 0:3.5.0-3 -> 0:3.5.1-3
ruby CHANGED 0:3.4.4-26 -> 0:3.4.5-27
rubygem-rabbit CHANGED 0:3.0.5-2 -> 0:4.0.1-1
rubygem-tins CHANGED 0:1.39.1-1 -> 0:1.42.0-1
rust-astral-tokio-tar CHANGED 0:0.5.2-3 -> 0:0.5.3-1
rust-async-broadcast CHANGED 0:0.7.2-3 -> 0:0.7.2-4
rust-sspi CHANGED 0:0.16.0-1 -> 0:0.16.1-1
sirikali CHANGED 0:1.8.2-3 -> 0:1.8.3-1
sssd CHANGED 0:2.11.1-1 -> 0:2.11.1-2
unzip CHANGED 0:6.0-67 -> 0:6.0-68
wesnoth CHANGED 0:1.19.14-3 -> 0:1.19.15-1
wine CHANGED 0:10.12-4 -> 0:10.13-1
yasm CHANGED 0:1.3.0^20250625git121ab15-1 -> 0:1.3.0^20250625git121ab15-3
zswap-cli CHANGED 0:1.0.0-4 -> 0:1.1.0-1




