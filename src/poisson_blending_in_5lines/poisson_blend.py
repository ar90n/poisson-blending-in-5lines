from scipy.ndimage import laplace
def poisson_blend(target_img, src_img, mask_img, iter: int = 1024):
    for _ in range(iter):
        target_img = target_img + 0.25 * mask_img * laplace(target_img - src_img)
    return target_img.clip(0, 1)
