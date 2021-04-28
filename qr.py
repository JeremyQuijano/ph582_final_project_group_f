import numpy as np
import matplotlib.pyplot as plt
import cv2
import PIL
#%%
im_low = cv2.imread('low.png')
im_low = np.asarray(im_low)

#%%
im_wb_low = im_low[:, :, 2].copy()
# im_wb[im_wb < 190] = 0
#%%
plt.figure()
# plt.imshow(im_wb[-125:, 76:1330], cmap='gray')
# plt.imshow(im_wb_low[:742, 52:1340], cmap='gray')
plt.imshow(im_low, cmap='gray')
plt.show()
plt.close()

#%%
im_wb_low.shape

#%%
qr_code = np.zeros((72, 72))
im_wb_low_cut = im_wb_low[:742, 52:1340]
# print(im_wb_low_cut.shape)

step = 17.9
i = 0
k = 71
m = 0
j = im_wb_low_cut.shape[0]-step/2
print(j)
colors = []
while j > 0:
    i = 0
    m = 0
    while i*step < im_wb_low_cut.shape[1]:
        # print(int(step*i), int(step*j))
        if k == 69:
            print(k, m, step*i+step/2, im_wb_low_cut[int(j), int(step*i+step/2)])
        colors.append(np.average(im_wb_low_cut[int(j)-9:int(j)+9, int(step*i+step/2)-9:int(step*i+step/2)+9]))
        qr_code[k, m] = int((im_wb_low_cut[int(j), int(step*i+step/2)] > 128)*2 - 1)
        m += 1
        i += 1
    j = j - step
    k -= 1
    # j -= 1

#%%
im_wb_low_cut[:742, 52:1340][0]
int(step*j)
#%%
plt.figure()
plt.imshow(qr_code)
plt.savefig('qr_low.png', dpi=320)
plt.show()
plt.close()

#%%
plt.hist(np.array(colors), bins=30)
plt.show()
