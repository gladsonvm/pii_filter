# PII Detection and Masking tool
 This is a tool to monitor new files dropped in a specified directory and to remove/mask **pii information** in the files if any.
 
Following are the components of the program

1. main.py
    - entry point of the program

    
2. config.py
    - config file where running configurations are written. A config entry typically contains following
        - watch directory
        - setup action (optional)
        - response actions

    
3. config_vars
    - contains constant values

    
4. response_actions.py
    - This file has all response actions as functions

    
5. watcher.py
    - contains function watchman() which listens for new files in a given folder

    
6. setup_action
    - task to execute before watchman is triggered. As per the use case setup action is to create a directory named **todecode** if same already exists, then deletes all files in the directory
    - only one setup action is allowed for one watchman instance
    

7. pii_regex.py
    - contains compiled regular expressions to detect pii information
    - only the regex in pii_regex_list is used to detect pii info
    - to add a new regex, add a compiled regex to the file using re.compile() and add it to the pii_regex_list also.
    

## Workflow Diagram


![workflow](./workflow.png?raw=true "workflow")

- Abbreviations used:
   - WdT: Watch Directory Thread
   - CdT: Compressed Directory Thread
   

### Start Service

 - First create a virtualenv and run 
   - `pip install -r requirements.txt`
   
`pyminizip` needs to be installed and same is used to set password to zip files.

**cd to pii_filter** directory once this repo is cloned successfully

```
$python3 main.py 
watchman running for /path/to/pii_filter/watch_dir
watchman running for /path/to/pii_filter/todecode
```

### Run tests

```
$python3 -m unittest tests/test_*.py
test_compress_files
.test_extract_all
.test_setup_action_delete_if_exists
.test_setup_action_directory_does_not_exist
.test_setup_action_no_delete
.
----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```