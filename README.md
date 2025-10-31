# log_classification 

## The content of this repo

This is a python package that takes a log file and classify it

based on 5 LOG levels: (**DEBUG** / **INFO** / **WARNING** / **ERROR** / **CRITICAL**)

and you can choose the level that you want to classify based on

and when you choose the level a file will be created in the path that you specify,ex:

``` powershell
debug.log | info.log | warning.log | error.log | critical.log
```

and this classification is based on a certain regex , ex:

``` powershell
[2025-10-15 09:00:01] DEBUG    Starting system diagnostics for user: dev_admin

[2025-10-15 09:00:09] INFO     Application startup complete

[2025-10-15 09:00:16] WARNING  Slow response from API endpoint /fetch-data (2.4s)

[2025-10-15 09:00:22] ERROR    Database connection lost: db-prod-02

[2025-10-15 09:00:29] CRITICAL System instability detected — entering safe mode
```

## the setup

so when you clone this repo to your device,in the terminal navigate to it and make sure that

**pyproject.toml** exist, ex:

``` powershell
C:\Users\Ghost\Desktop\Classify [master] > ls


    Directory: C:\Users\Ghost\Desktop\Classify


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----        10/28/2025   1:22 AM                .pytest_cache
d-----        10/31/2025   4:32 AM                classification
d-----        10/28/2025  11:16 PM                classification.egg-info
d-----        10/28/2025  11:07 PM                tests
-a----        10/28/2025  11:41 PM            247 .gitignore
-a----        10/28/2025  11:15 PM            419 pyproject.toml
```

Then write this command:

``` powershell
pip install .
```

## the main action

After installing this package , you must know that  **act** is the command for this package

and after **act**. First, specify the path to the log file you want to analyze.
Next, provide the path to the output location where the classification result file will be created.
Finally, choose the type of classification you want to perform:

- ``` --de ``` for DEBUG

- ``` --inf ``` for INFO

- ``` --war ``` for WARNING

- ``` --err ``` for ERROR

- ``` --cri ``` for CRITICAL

Examples:

``` powershell
C:\Users\Ghost\Desktop\Classify [master] > act 'C:\Users\Ghost\Desktop\example.log' 'C:\Users\Ghost\Desktop' --de
the debug.log has been created and filled with the debug data
```

``` powershell
C:\Users\Ghost\Desktop > act 'C:\Users\Ghost\Desktop\example.log' 'C:\Users\Ghost\Desktop' --inf
the info.log has been created and filled with the info data
```

```powershell
C:\Users\Ghost\Desktop > act 'C:\Users\Ghost\Desktop\example.log' 'C:\Users\Ghost\Desktop' --war
the warning.log has been created and filled with the warning data
```

```powershell
C:\Users\Ghost\Desktop > act 'C:\Users\Ghost\Desktop\example.log' 'C:\Users\Ghost\Desktop' --err
the error.log has been created and filled with the error data
```

```powershell
C:\Users\Ghost\Desktop > act 'C:\Users\Ghost\Desktop\example.log' 'C:\Users\Ghost\Desktop' --cri
the critical.log has been created and filled with the critical data
```




  
