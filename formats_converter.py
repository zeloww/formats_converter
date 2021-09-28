import os
from io import FileIO

try:
    import convertapi

except:
    os.system("pip install convertapi")
    import convertapi

zelow = """
███████╗ ██████╗ ██████╗ ███╗   ███╗ █████╗ ████████╗███████╗     ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗███████╗██████╗ 
██╔════╝██╔═══██╗██╔══██╗████╗ ████║██╔══██╗╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
█████╗  ██║   ██║██████╔╝██╔████╔██║███████║   ██║   ███████╗    ██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   █████╗  ██████╔╝
██╔══╝  ██║   ██║██╔══██╗██║╚██╔╝██║██╔══██║   ██║   ╚════██║    ██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   ██╔══╝  ██╔══██╗
██║     ╚██████╔╝██║  ██║██║ ╚═╝ ██║██║  ██║   ██║   ███████║    ╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   ███████╗██║  ██║
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                               
                                                                                                                                    by github.com/zeloww
"""

def convert():
	options = {
		"Files": []
	}

	convertapi.api_secret = input("Enter your ConvertAPI Key >>> ")
	to_format = input("Enter the format conversion do you want >>> ")
	file = input("Enter the file directory to convert or 'stop' for break >>> ")

	while file not in ["stop", "break", "s", "b"]:
		options["Files"].append(file)
		file = input("Enter the file directory to convert or 'stop' for break >>> ")

	for file in options["Files"]:
		try:
			FileIO(file)

		except FileNotFoundError as e:
			print(e)
			options["Files"].remove(file)
 
	if not options["Files"]:
		exit("no valid file!")

	for file in options["Files"]:
		os.makedirs("formats_converted/", exist_ok=True)

		result = convertapi.convert(to_format=to_format, params={"File": file})
		result.save_files("formats_converted/")

	print("Conversion Successfully Completed!")

def main():
    os.system("color d")

    while True:
        os.system("cls")
        print(zelow)
        convert()

        choice = input("restart? [y/n] >>> ")

        if choice not in ["y", "yes"]:
            print("bye :D")
            break

if __name__ == "__main__":
	main()
	input()
