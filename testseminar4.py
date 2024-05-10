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
def test_step1():
    # test1
    res1 = checkout("cd {}; 7z a {}/arx2".format(folder_in, folder_out), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_out), "arx2.7z")
    assert res1 and res2, "test FAIL"
def test_step2():
    # test2
    res1 = checkout("cd {}; 7z e arx2.7z -o{} -y".format(folder_out, folder_ext), "Everything is Ok")
    res2 = checkout("ls {}".format(folder_ext), "test1")
    res3 = checkout("ls {}".format(folder_ext), "test2")
    assert res1 and res2 and res3, "test2 FAIL"
