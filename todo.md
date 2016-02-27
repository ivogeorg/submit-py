#### TODO

1. Merge into one script: cloning, etc.
2. Flip script: perform all steps for one submission.
3. Input parameters: 
  1. Asst repo name.
  2. Filename for file with Github acct id-s. _Note: All steps tied to Github acct id._
  3. Filename for file with required files.
  4. Build directory (to copy files, build, and run the asst code).
  5. Filename for grading log file.
4. Steps:
  1. Open log file and add a new line with the Github acct id. _Note: {format id, num_passed, num_total, msg} (e.g. `ivogeorg, 147, 204, "Err msg or comment"`)._
  2. Clone repository. _Errors: exact spelling; **master** branch; no tags._ 
  3. Check for required files. _Errors: exact spelling; missing files._
  4. Copy files to build directory. _Note: Always clean up old files._
  5. Build with `cmake`. _Errors: missing files; compilation errors; linker errors._
  6. Run and `grep` the _"Passed 56/56 tests."_ line.
  7. Parse the numbers for the _passed_ and _total_ tests.
  8. Complete the entry in the log file: 
    * If asst code ran, add number of passed and total tests, and empty message.
    * If some other error, enter 0 for passed tests, the number of total tests, and an error message.
5. Repeat for all Github acct id-s in the input file.

