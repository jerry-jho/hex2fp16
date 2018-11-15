import numpy as np
import sys

def halfbits_to_floatbits(i):
    n = np.frombuffer(bytearray([i & 0xFF,(i>>8) & 0xFF]),dtype=np.float16)
    return n[0]

if __name__ == '__main__':
    if len(sys.argv) == 2:
        intput_value_1 = int(sys.argv[1],base=16)
        print("intput hex 0x%x" % intput_value_1)
        tmp_f_1 = halfbits_to_floatbits(intput_value_1)
        print("out helf-float %f" % tmp_f_1);
    elif len(sys.argv) == 3:
        intput_value_1 = int(sys.argv[1],base=16)
        intput_value_2 = int(sys.argv[2],base=16)


        print("intput hex value_1 : 0x%x" % intput_value_1)
        print("intput hex value_2 : 0x%x" % intput_value_1)


        tmp_f_1 = halfbits_to_floatbits(intput_value_1)
        tmp_f_2 = halfbits_to_floatbits(intput_value_2)

        print("out helf-float value_1 : %f" % tmp_f_1)
        print("out helf-float value_2 : %f" % tmp_f_2)

        add_result_f = tmp_f_1  + tmp_f_2
        sub_result_f = tmp_f_1  - tmp_f_2
        mul_result_f = tmp_f_1  * tmp_f_2
        div_result_f = tmp_f_1  / tmp_f_2


        print("Addition result float: %f" % add_result_f)
        print("Subtraction result float : %f " % sub_result_f)
        print("Multiplication result float : %f " % mul_result_f)
        print("Division result float : %f " % div_result_f)