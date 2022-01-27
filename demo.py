import numpy as np
from dipy.data import get_fnames
from dipy.io.image import load_nifti, save_nifti
import matplotlib.pyplot as plt
import nibabel as nib
from dipy.reconst.shore import ShoreModel
from dipy.viz import window, actor
from dipy.core.gradients import gradient_table
from dipy.data import get_fnames, get_sphere
from dipy.io.gradients import read_bvals_bvecs
from dipy.io.image import load_nifti, load_nifti_data

def read_dir(data):
    data_nums = data.split("  ")
    data_nums = [x.strip() for x in data_nums if x.strip() != " "]
    data_nums = [x.strip() for x in data_nums if x.strip() != ""]
    data_nums = map(float, data_nums)
    data_nums = list(data_nums)
    data_nums = np.mat(data_nums)
    return data_nums.getA()[0]

DATA = nib.load(r'D:\HCPData\shiyan\100206\T1w\Diffusion\data.nii.gz')
data = DATA.dataobj
data_small = data[50:70, 22, 50:70]

bvals = []
with open(r'D:\HCPData\shiyan\100206\T1w\Diffusion\bvals') as file_object:
    for line in file_object:
        bvals = line
bvals = bvals.split(" ")
bvals = np.array(list(map(float, bvals)))

b_vec_x, b_vec_y, b_vec_z, i = [], [], [], 0
with open(r'D:\HCPData\shiyan\100206\T1w\Diffusion\bvecs') as file_object:
    for line in file_object:
        if i == 0:
            b_vec_x = line
        if i == 1:
            b_vec_y = line
        if i == 2:
            b_vec_z = line
        i += 1
b_vec_x = read_dir(b_vec_x)
b_vec_y = read_dir(b_vec_y)
b_vec_z = read_dir(b_vec_z)
bvecs = np.concatenate([b_vec_x.reshape(1, -1), b_vec_y.reshape(1, -1), b_vec_z.reshape(1, -1)], axis=0)

gtab = gradient_table(bvals, bvecs)

radial_order = 6
zeta = 700
lambdaN = 1e-8
lambdaL = 1e-8
asm = ShoreModel(gtab, radial_order=radial_order,
                 zeta=zeta, lambdaN=lambdaN, lambdaL=lambdaL)
asmfit = asm.fit(data_small)
sphere = get_sphere('repulsion724')
odf = asmfit.odf(sphere)
interactive = False

scene = window.Scene()
sfu = actor.odf_slicer(odf[:, None, :], sphere=sphere, colormap='viridis', scale=0.5)# colormap='plasma'
sfu.RotateX(-90)
sfu.display(y=0)
scene.add(sfu)
window.record(scene, out_path='odfs.png', size=(1800, 1800))
if interactive:
    window.show(scene)