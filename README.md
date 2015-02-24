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

I/O-intensive output:

    2015-02-25 00:27:41,720 Server: Berserk I/O-bound benchmark server
    2015-02-25 00:27:41,724  * Running on http://127.0.0.1:8089/
    ------------------
    BERSERK BENCHMARK
    ------------------

    2015-02-25 00:27:42,806 Client: #start 2015-02-25 00:27:42.806152
    2015-02-25 00:27:42,806 Client: Sending 1 remote tasks...
    2015-02-25 00:27:42,827 Starting new HTTP connection (1): localhost
    2015-02-25 00:27:42,828 Doing 1 runs of 30th Fibonacci num. calculation.
    2015-02-25 00:27:43,406 127.0.0.1 - "GET /?tasks=1&task_size=30 HTTP/1.1"
    2015-02-25 00:27:43,407 Client: ... Done.
    2015-02-25 00:27:43,408 Client: Doing 2 local tasks
    2015-02-25 00:27:43,408 Doing 2 runs of 30th Fibonacci num. calculation.
    2015-02-25 00:27:44,616 Client: Sending 1 remote tasks...
    2015-02-25 00:27:44,619 Starting new HTTP connection (1): localhost
    2015-02-25 00:27:44,621 Doing 1 runs of 30th Fibonacci num. calculation.
    2015-02-25 00:27:45,186 127.0.0.1 - "GET /?tasks=1&task_size=30 HTTP/1.1"
    2015-02-25 00:27:45,188 Client: ... Done.
    2015-02-25 00:27:45,188 Client: Doing 2 local tasks
    2015-02-25 00:27:45,188 Doing 2 runs of 30th Fibonacci num. calculation.
    2015-02-25 00:27:46,373 Client: #end 2015-02-25 00:27:46.373078
    2015-02-25 00:27:46,373 Client: #runtime 0:00:03.566926 (3 s)
    ------------------
