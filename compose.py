#!/usr/bin/env python3

import argparse
import glob
import json
import os
import re
import requests
from typing import List
import requests, re
import tempfile



def download_path(url: str):
    """
    download all page in html
    create list by found 'href='
    go through list ^ and jump over 'start by ?' , some signs in the name
    """

    html = requests.get(url).text

    hrefs = re.findall(r'href="([^"]+)"', html)
    
    #print('DEBUG_START\n' + "\n".join(hrefs) + '\nDEBUG_END')
    
    subdirs = []
    for h in hrefs:
        if h.startswith("?"):
            continue
        if h in ("../", "/", "/compose/", "latest-Fedora-Rawhide/"):
            continue
        if h.endswith("/"):
            subdirs.append(h.strip("/"))

    return(subdirs)

def download_rpmsjson(url: str, compose_list: list, rpmsjson: str):
    temp_dir = tempfile.mkdtemp()
    print("temp dir:     ", temp_dir)

    file_paths = []

    for compose in compose_list:
        r = requests.get(url + compose + rpmsjson)
        r.raise_for_status()

        filepath = os.path.join(temp_dir, compose + '-rpms.json')
        with open(filepath, "wb") as f:
            f.write(r.content)
        print("Downloaded to:", filepath)

        file_paths.append(filepath)
    return(file_paths)

def parse_rpmsjson(two_files: list):
    with open(two_files[0]) as f1:
        d = json.load(f1)
        rpm_dict_f1=dict()
        for nevra in (d['payload']['rpms']['Everything']['x86_64']):
            name=nevra.rsplit("-", 2)[0]
            version='-'.join(nevra.rsplit('-', 2)[1:]).rsplit('.', 2)[0]
            rpm_dict_f1[name]=version
    with open(two_files[1]) as f2:
        d = json.load(f2)
        rpm_dict_f2=dict()
        for nevra in (d['payload']['rpms']['Everything']['x86_64']):
            name=nevra.rsplit("-", 2)[0]
            version='-'.join(nevra.rsplit('-', 2)[1:]).rsplit('.', 2)[0]
            rpm_dict_f2[name]=version


    #REMOVED
    for name, version in rpm_dict_f1.items():
        if name not in rpm_dict_f2.keys():
            print(name + " REMOVED " + name+version  )

    #ADDED
    for name, version in rpm_dict_f2.items():
        if name not in rpm_dict_f1.keys():
            print(name + " ADDED " + name+version)

    #CHANGED
    for name, version in rpm_dict_f2.items():
        try:
            if rpm_dict_f1[name] != rpm_dict_f2[name]:
                print(name + " CHANGED " + rpm_dict_f1[name] + " -> " + rpm_dict_f2[name])
        except KeyError as err:
            #print("XXXXXXXXXXXXXXXX" + name + " was ADDED, thus traceback; see ADDED section if true")
            continue







def main() -> None:
    """
    some options with default values
    :return: None
    """
    parser = argparse.ArgumentParser(description="compose rpm change log")

    parser.add_argument("-u", "--url", default="https://kojipkgs.fedoraproject.org/compose/rawhide/", dest="url",
                        help="URL of fedora compose")
    parser.add_argument("-r", "--rpmsjson", default="/compose/metadata/rpms.json", dest="rpmsjson",
                        help="care about the rpms.json file")
    parser.add_argument("-l", "--list", nargs="?", type=int, const=999, dest="list_composes",
                        help="Outputs a list of Rawhide composes built in the past X days ; sorted as the first = the oldest")
    parser.add_argument("-d", "--diff", action='append', dest="two_composes", help="specify TWO composes: -d one -d two for.ex. --diff Fedora-Rawhide-20250807.n.1 --diff Fedora-Rawhide-20250814.n.0\"")

    args = parser.parse_args()

    if args.list_composes and args.two_composes:
        print("USE: -l OR -d")
        print("HINT: list composes OR diff")
        print("--help")
        exit(1)

    wwwsubdirs_list=download_path(args.url)
    # 1. TASK = Use Python to create a CLI tool which ... 
    if args.list_composes is not None:
        wwwsubdirs_list=sorted(wwwsubdirs_list, reverse=False) # add True for order = 1. line as newest compose
        print("\n".join(wwwsubdirs_list[:args.list_composes]))

    # 2. TASK
    if args.two_composes:
        if len(args.two_composes) == 2:
            if args.two_composes[0] in wwwsubdirs_list and  args.two_composes[1] in wwwsubdirs_list:
                two_composes=sorted(args.two_composes)
                print("old compose  :", two_composes[0])
                print("new compose  :", two_composes[1])
                #compose_files=download_rpmsjson(args.url, two_composes, args.rpmsjson)
                compose_files=['/tmp/tmpyqg3625o/Fedora-Rawhide-20250820.n.0-rpms.json', '/tmp/tmpyqg3625o/Fedora-Rawhide-20250821.n.0-rpms.json']

                #print(compose_files)

                parse_rpmsjson(compose_files)
            else:
                print("composes DOES not match --list")
        else:
            print("USE: -d one -d two")
            print("HINT: two composes only")
            print("see --help")
            exit(1)
    #wwwsubdirs_list=download_path(args.url)
    #compose_files=download_rpmsjson(args.url, wwwsubdirs_list[:2], args.rpmsjson)
    #compose_files="/tmp/tmp0jiqkfrg"




if __name__ == "__main__":
    main()
