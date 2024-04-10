import requests
import sys

sub_list = open("subdomains.txt").read()
directories = sub_list.splitlines()
count = 0
for dir in directories:
	length = len(directories)
	dir_enum = f"http://{sys.argv[1]}/{dir}.html"
	r = requests.get(dir_enum)
	if r.status_code==404:
		count += 1
		print(f"\r{str(round((count/length)*100, 2))}% of list scanned", end='', flush=True)
		continue
	else:
		print("\nValid Directory: ", dir_enum)
