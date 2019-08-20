
# conda-unowned-files

Find files on a conda prefix or env not owned by any package.

Ideally, all files in a conda env should by owned by a package installed in that env, but unonwed files can exist for many reasons, including:
  * Cache files, such as `.pyc` files from python
  * Data/config files created after installation
  * Files created manually by the user
  * Leftover files from old uninstalled packages

## Usage
```bash
# find unowned files on root prefix
$ ./conda-unowned-files.py

# find unowned files on a env
$ ./conda-unowned-files.py -n <env-name>
```
