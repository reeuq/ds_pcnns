import matplotlib.pyplot as plt

x = []
y = []
with open('./e_13_s_False_u_230_27_b_50_w_3_c_tanh_d_50_i_gap_40_len_80_n_0/test_pr_12.txt', 'r') as f:
    lines = f.readlines()
    for temp in lines:
        temp_x, temp_y = temp.split()
        x.append(float(temp_x))
        y.append(float(temp_y))

plt.plot(y, x)
plt.show()
