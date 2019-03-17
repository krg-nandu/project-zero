import os

# this should ideally collect some data at this point
# lets figure this out later
# for now, just call in a simple voice activation
def main():
	os.system("espeak -ven+f5 -s170 'Hi There'")

if __name__ == '__main__':
	main()
