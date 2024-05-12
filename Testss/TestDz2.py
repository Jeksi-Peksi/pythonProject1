import subprocess

folder_in = "/home/evgeniy/tst"
folder_out = "/home/evgeniy/out"
folder_ext = "/home/evgeniy/folder1"

def checkout(cmd, text):
    res = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in res.stdout and res.returncode == 0:
        return True
    else:
        return False

def test_step1dz():
    # testdz1
    assert "7z l arx2.7z", "test FAIL"

def test_step2dz():
    # testdz2
    res = checkout("cd {}; 7z x arx2.7z -o{}/folder2".format(folder_out, folder_out), "Everything is Ok")
    assert res, "test2 FAIL"
