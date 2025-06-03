# FILE-INTEGRITY-CHECKER
*COMPANY*: CODTECH IT SOLUTIONS
*NAME*:NITHA ZACHARIAH
*INTERN ID*: CT04DF211
*DOMAIN*: CYBER SECURITY AND ETHICAL HACKING
*DURATION*: 4 WEEKS
*MENTOR*: NEELA SANTOSH
*DESCRIPTION*:???? File Integrity Checker in Python
I created a basic File Integrity Monitoring Tool during my internship. Its function is to scan for modifications done on certain files based on comparing their hash values with time.
???? How It Works:
The tool operates in two fundamental steps:
Baseline Creation – Upon initial execution of the script, it prompts the user to input file names to be watched (e.g., test1.txt, test2.txt). It computes a SHA-256 hash for every file via Python's hashlib library and writes the outputs into a file named hashes.json.
Change Detection – Afterwards, when the script is executed again, it re-computes the hash values of the said files and cross-checks them against the stored ones. When any file's content is modified, the script gives a warning message. If a file is deleted or missing, it also informs the user.

???? What I Did:
Created two sample text files: test1.txt and test2.txt, filled with support ticket details.
Wrote a Python program (file_monitor.py) in Visual Studio Code.
Utilized the hashlib library to compute SHA-256 hashes.
Utilized json to store and read hash values into/from a file.
Tested the program by modifying one of the files and seeing if the tool identified the change.
???? What I Learned:
How hashing catches file modification.
How even the slightest change in file content yields an entirely different hash.
How to read file input/output and JSON data in Python
The real-world significance of file integrity in systems such as support logs, configuration files, and reports.
Result:
The script was able to:
Create a baseline of file hashes.
Identify changes to monitored files.
Report missing files correctly.
This tool can be extended to monitor more files or entire directories. It offers a basic but effective way to ensure that important files remain unchanged, making it useful in security-sensitive environments.
