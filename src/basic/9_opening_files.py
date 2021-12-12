# ident your Python code to put into and e-mail
import glob
# globl suport Unix style pathame extention
python_files = glob.glob('./src/*.py')
for file_name in sorted(python_files):
    print ('---------------' + file_name)

    with open(file_name) as f:
        for line in f:
            print ('    ' + line.rstrip())
    
    print()