File-sorter-python-
Automated tool for organizing Downloads folder based on file extensions
---------------------------------------------------------------------

Python File Organizer

A lightweight, efficient automation script designed to keep your directories (like `Downloads`) perfectly organized.
It automatically moves files into categorized folders based on their extensions using a customizable JSON configuration.

Key Features;
Custom Logging: Includes a built-in logging system with timestamps `[HH:MM]` to track every file relocation.
JSON Configuration: Easily manage sorting rules via an external `config.json` file without modifying the Python code.
Robust Error Handling: Skips directories and handles system errors (like locked files) to ensure continuous operation.
One-Click Execution: Includes a Windows Batch script for easy manual or scheduled runs.

Tools:
Python 3.x
Libraries: "os", "shutil", "json", "datetime" (all standard libraries).

How to Setup
1. Download all files from this repository (`main.py`, `config.json`, `run_sorter.bat`) into one folder.
2. Edit "config.json" to define your own folder names and file extensions.
3. Run the script:
   - On Windows: Simply double-click "run_sorter.bat".
   - Via Terminal: Run "python main.py".
4. Check the "sort_log.txt" to see the results of the organization.

Note' this project was created for internship application during my first year of studies.
