# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:hydrogen
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
from skimage import io
import numpy as np
import matplotlib.pyplot as plt

from poisson_blending_in_5lines import poisson_blend

# %%
src_img = io.imread("vinci_src.png",) / 255.0
target_img = io.imread("vinci_target.png",) / 255.0
mask_img = io.imread("vinci_mask.png") == 255

# %%
src_coords = np.argwhere(mask_img)
src_top, src_left = np.min(src_coords, axis=0) - 1
src_bottom, src_right = np.max(src_coords, axis=0) + 1
mask_patch = mask_img[src_top : src_bottom + 1, src_left : src_right + 1]
src_patch = src_img[src_top : src_bottom + 1, src_left : src_right + 1]

# %%
target_top, target_left = (src_top + target_img.shape[0] - src_img.shape[0], 30)
target_bottom, target_right = (
    target_top + mask_patch.shape[0],
    target_left + mask_patch.shape[1],
)
target_patch = target_img[target_top:target_bottom, target_left:target_right]
# %%
blend_patch = np.stack(
    [
        poisson_blend(target_patch[:, :, i], src_patch[:, :, i], mask_patch)
        for i in range(3)
    ],
    axis=2,
)

# %%
plt.figure(figsize=(64, 64))
plt.subplot(1, 4, 1)
io.imshow(src_patch)
plt.subplot(1, 4, 2)
plt.imshow(mask_patch)
plt.subplot(1, 4, 3)
io.imshow(target_patch)
plt.subplot(1, 4, 4)
io.imshow(blend_patch)
plt.show()
