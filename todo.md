#### Design

1. Merge into one script: cloning, etc.
2. Flip script: perform all steps for one submission + repeat for all submissions.
3. Command line arguments: 
  1. [optl] Asst name. _Default:_ `asst_yyyymmdd_hhmmss`, otherwise `asstname_yyyymmdd_hhmm`.
  2. [reqd] Asst repo name.
  3. [reqd] Filename for file with Github acct id-s **OR** a single id inline. _Note: All steps tied to Github acct id._
  4. [reqd] Filename for file with required files.
  5. [optl] Build directory (to copy files, build, and run the asst code).
  6. [optl] Filename for grading log file. _Default:_ `[asst-name]_grading.csv`.
4. Steps:
  1. Open log file and add a new line with the Github acct id. _Note: Format {id, num_passed, num_total, msg} (e.g. `ivogeorg, 147, 204, "Err msg or comment"`)._
  2. Clone repository. _Errors: exact spelling; **master** branch; no tags._ 
  3. Check for required files. _Errors: exact spelling; missing files._
  4. Copy files to build directory. _Note: Always clean up old files._
  5. Build with `cmake`. _Errors: missing files; compilation errors; linker errors._ _Note: this can be arbitrarily sophisticated with CMake._
  6. Run and `grep` the _"Passed 56/56 tests."_ line. _Errors: early termination (i.e. the program doesn't complete and the "Passed" line is not printed), in which case the number of "ok" lines have to counted._ _TODO: Can the `ErrorContext` be modified to be exception-safe (i.e. the destructor is called even upon early termination), or does this fall under the inevitable exceptions?_ 
  7. Parse the numbers for the _passed_ and _total_ tests. Alternatively, count the "ok" lines.
  8. Complete the entry in the log file: 
    * If asst code ran, add number of passed and total tests, and empty message.
    * If some other error, enter the "ok" count for passed tests, the number of total tests, and an error message.
5. Repeat for all Github acct id-s in the input file.
6. Environment assumptions:
  1. Git repository directory `$HOME/git-repos/submit-py` is root for the application.
  2. There is a Python virtual environment at `$HOME/PythonVirtualEnvs/submitpy`.
  3. The config files with the Github acct id-s and required files are in the `$SUBMITPY_ROOT/config`.
  4. A directory is created for the assignment `[asst-name]`.
  5. Subdirectories `build`, `repos`, `config`, and `log` are created in the asst dir.
  6. Config files are copied to `config`.
  7. Log file is created under `log`.

#### Todo

1. How is this a _submit_ script w/o a remote server? Currently, it is an autograde script only.
2. What might the Github API be useful for?
3. 

#### Some fresh ideas

1. Subcommands:

  1. check - give remote feedback on tests passing, syntax check, style check
  2. submit - record date, time and stats with authentication and feedback
  3. grade - grade a roster or a single student, multiple assignments or one, depending on cmd line args
  4. compare - check for possible plagiarism

2. Execution modes:

  1. Local (check, grade, compare)
  2. Server (all).

3. Encapsulate and abstract interaction with shell (command & feedback/result/return codes).

4. Modes of identification, isolation, security, and confidentiality (protect).

5. Encapsulate and abstract build tool for particular programming language (lang).

6. Encapsulate and abstract protocol for particular repository (fetch).


