# poisson-blending-in-5lines
This project is a simple implementation of Poisson Blending algorithm whose code size is 5 lines.
It uses scipy and contain only esssential logics. i.e. input validations are missing and single data type and channel are support.


The contants of [poisson_blend.py](https://github.com/ar90n/poisson-blending-in-5lines/blob/master/src/poisson_blending_in_5lines/poisson_blend.py) are following.
You can see that there are only 5 lines. They are all of out Poisson Blending algorithm. 
In fact, They are optimized for code size.  It means that there are some redundant computations.

```python
from scipy.ndimage import laplace
def poisson_blend(target_img, src_img, mask_img, iter: int = 1024):
    for _ in range(iter):
        target_img = target_img + 0.25 * mask_img * laplace(target_img - src_img)
    return target_img.clip(0, 1)
```

Above codes generate the folloing right image  with three left images as its input.
These input images area  source image, mask image and target image from left to right.

![output of poisson blending](https://raw.githubusercontent.com/ar90n/poisson-blending-in-5lines/assets/image/output.jpg)

## Feature
* Only importing gradients method support
* Mixigin gradients methods is **not support**
* Convergence checking of [jacobi method](https://en.wikipedia.org/wiki/Jacobi_method) is **not suuport**

## Launch example notebook
```bash
$ git clone https://github.com/ar90n/poisson-blending-in-5lines.git
$ cd poisson-blending-in-5lines
$ poetry install
$ poetry run jupytext --to notebook ./notebook/example.py ./notebook/example.ipynb
$ poetry run jupyter notebook ./notebook/example.ipynb
```

## References
* [Poisson Blending](http://opencv.jp/opencv2-x-samples/poisson-blending)
* [Erkaman / poisson_blend](https://github.com/Erkaman/poisson_blend)
* [Poisson Image Editing](https://dl.acm.org/doi/pdf/10.1145/1201775.882269)

## License
This software is released under the Apache License, see [LICENSE](LICENSE).
