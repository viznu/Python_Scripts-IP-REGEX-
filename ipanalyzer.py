import re
import socket

def main():
	
	list_of_paths = [ 'IP/dir1/file1.txt' , 
			'IP/dir1/file2.txt' , 
			'IP/dir2/file3.txt' ,
			'IP/dir2/file4.txt' ,
			'IP/f.inp' ]
	
	allmatches = []	
	ips = []
	ip_expression  = re.compile(r"((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.)(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.)(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])(\.)(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]))") 
	
	for file_path in list_of_paths:
		with open(file_path,"r") as current_file:
			file_data = current_file.readlines()
		for line in file_data:
			match  = ip_expression.findall(line)
			if match is not None:
				allmatches.append(match)	
	for match in allmatches:
		for ip in match:
			ips.append(ip[0])
	ips = sorted(ips)	
	print '\n'.join(str(x) for x in ips)

if __name__=="__main__":
	main()
