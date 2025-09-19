import numpy as np
import matplotlib.pyplot as plt

try:
    img1 = np.asarray(plt.imread('assets/img1.jpg'), dtype=np.float64) / 255.0
    img2 = np.asarray(plt.imread('assets/img2.jpg'), dtype=np.float64) / 255.0
    img3 = np.asarray(plt.imread('assets/img3.jpg'), dtype=np.float64) / 255.0
    img4 = np.asarray(plt.imread('assets/img4.jpg'), dtype=np.float64) / 255.0
    logo = plt.imread('assets/logo.png')
    all_images = [img1, img2, img3, img4]
except FileNotFoundError:
    print("Error: No images detected")
    exit()

fig, axs = plt.subplots(2, 2, figsize=(7, 6),
                        gridspec_kw={'wspace': 0.1, 'hspace': 0.1})
fig.patch.set_facecolor('gray')

xin, xfin = 20, 200
yin, yfin = 20, 200
for ax, img in zip(axs.flat, all_images):
    ax.imshow(img[yin:yfin, xin:xfin])
    ax.axis('off')

logo_h, logo_w, _ = logo.shape
fig_w, fig_h = fig.get_size_inches() * fig.dpi

logo_display_w = fig_w * 0.25
scale = logo_display_w / logo_w
logo_display_h = logo_h * scale

left = (fig_w - logo_display_w) / 2 / fig_w
bottom = (fig_h - logo_display_h) / 2 / fig_h
width = logo_display_w / fig_w
height = logo_display_h / fig_h

ax_logo = fig.add_axes([left, bottom, width, height])

ax_logo.imshow(logo, interpolation='antialiased')
ax_logo.axis('off')

plt.savefig('output.jpg', facecolor=fig.get_facecolor(), dpi=150)
plt.show()