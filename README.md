
# About

> ibook


owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git pull origin master --allow-unrelated-histories
From github.com:zhbi98/ibook
 * branch            master     -> FETCH_HEAD
error: Your local changes to the following files would be overwritten by merge:
        ibook.py
Please commit your changes or stash them before you merge.
Aborting

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git add ibook.py

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git add .

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git commit -m "Add README.md"
[master 800ee24] Add README.md
 4 files changed, 711 insertions(+), 712 deletions(-)
 create mode 100644 __pycache__/message.cpython-37.pyc
 create mode 100644 __pycache__/power.cpython-37.pyc
 create mode 100644 __pycache__/updata.cpython-37.pyc
 rewrite ibook.py (94%)

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git push origin master
To github.com:zhbi98/ibook.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'git@github.com:zhbi98/ibook.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git pull origin master --allow-unrelated-histories
From github.com:zhbi98/ibook
 * branch            master     -> FETCH_HEAD
CONFLICT (add/add): Merge conflict in updata.py
Auto-merging updata.py
CONFLICT (add/add): Merge conflict in power.py
Auto-merging power.py
CONFLICT (add/add): Merge conflict in message.py
Auto-merging message.py
CONFLICT (add/add): Merge conflict in ibook.py
Auto-merging ibook.py
Automatic merge failed; fix conflicts and then commit the result.

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master|MERGING)
$ git add .
warning: LF will be replaced by CRLF in ibook.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in message.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in power.py.
The file will have its original line endings in your working directory
warning: LF will be replaced by CRLF in updata.py.
The file will have its original line endings in your working directory

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master|MERGING)
$ git commit -m "Add README.md"
[master f0e4f47] Add README.md

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$ git push origin master
Enumerating objects: 30, done.
Counting objects: 100% (30/30), done.
Delta compression using up to 4 threads
Compressing objects: 100% (24/24), done.
Writing objects: 100% (25/25), 14.53 KiB | 1.61 MiB/s, done.
Total 25 (delta 9), reused 0 (delta 0)
remote: Resolving deltas: 100% (9/9), completed with 1 local object.
To github.com:zhbi98/ibook.git
   5fe0f23..f0e4f47  master -> master

owon@mark MINGW64 /g/Others/python/src/pysource/ibook (master)
$
