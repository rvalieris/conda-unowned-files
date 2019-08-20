#!/usr/bin/env python
import json
import os
import argparse
import subprocess
import conda.api

# check if dir is internal of conda
def is_internal_dir(prefix,path):
    for t in ['pkgs','conda-bld','conda-meta','locks','envs']:
        if path.startswith(os.path.join(prefix,t)): return True
    return False

def get_pkg_files(prefix):
    pkg_files = set()
    for p in conda.api.PrefixData(prefix).iter_records():
        for f in p['files']:
            pkg_files.add(f)
    return pkg_files

def get_prefix(env_name):
    _conda = os.environ.get('CONDA_EXE', 'conda')
    _info = json.loads(subprocess.check_output([_conda, 'info', '-e', '--json']))
    prefix = conda.base.context.locate_prefix_by_name(name=env_name, envs_dirs=_info['envs_dirs'])
    return prefix

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n','--name',default='base',help='conda env name')
    args = parser.parse_args()

    prefix = get_prefix(args.name)
    pkg_files = get_pkg_files(prefix)

    for root, dirs, files in os.walk(prefix):
        if is_internal_dir(prefix,root):
            continue

        for f in files:
            f0 = os.path.join(root,f)
            f1 = f0.replace(prefix,"").lstrip(os.sep)
            if f1 not in pkg_files:
                print(f0)

if __name__ == '__main__':
    main()

