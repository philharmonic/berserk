The controllable benchmark program. Decide exactly how much memory, CPU, network
a benchmark program should consume to do your testing. Currently, CPU-bound
benchmarks are supported and the application is integrated with
[Philharmonic](http://github.com/kermit666/philharmonic) for sending
completion notifications.

Development installation
========================

- cd to the root of the project (e.g. `~/code/berserk/`)
- build the extensions

        python setup.py build

- make a symbolic link to the .so files

        ln -s build/lib.linux-x86_64-2.7/memory.so memory.so

Usage
=====
Edit the configuration file:

    $EDITOR conf.py

Run the program:

    $ python berserk.py
    We want to run a job for 0:00:04 (4 s).
    Looking for a 1 s task.
    Found 1st long-enough task (t = 1.386374) and it's for n = 31.
    [ 1.39240789  1.44514894  1.49032283  1.599298    1.51185799]
    1.39240789413
    #estimation 0:00:04.177224.
    We estimate that doing 3 tasks of size 31 will last 0:00:04.177224.
    ------------------
    BERSERK BENCHMARK
    ------------------
    #start 2015-01-30 16:34:43.678750
    Doing 3 runs of 31th Fibonacci number calculation
    #end 2015-01-30 16:34:48.313923
    #runtime 0:00:04.635173 (4 s)
    ------------------
