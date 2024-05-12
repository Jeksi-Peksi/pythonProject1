from testnegative import checkout_negative

folder_in = "/home/evgeniy/tst"
folder_out = "/home/evgeniy/out"
folder_ext = "/home/evgeniy/folder1"


def test_nstep1():
    # test neg1
    assert checkout_negative("cd {}; 7z e arx3.7z -o{} -y".format(folder_out, folder_ext), "ERROR"), "test1 FAIL"


def test_nstep2():
    # test neg2
    assert checkout_negative("cd {}; 7z t arx3.7z".format(folder_out), "ERROR"), "test2 FAIL"
