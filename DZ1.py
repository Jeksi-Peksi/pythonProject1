import subprocess


def function(command, text):
    result = subprocess.run(command, text, stdout=subprocess.PIPE, shell=True, encoding='utf-8')
    if result.returncode == 0:
        print("SUCCESS")
    else:
        print("FAIL")
