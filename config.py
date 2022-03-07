# ------------------------ Paths ------------------------
# Additional files
SMPL_MODEL_DIR = 'additional/smpl'
SMPL_FACES_PATH = 'additional/smpl_faces.npy'
SMPL_MEAN_PARAMS_PATH = 'additional/neutral_smpl_mean_params_6dpose.npz'
J_REGRESSOR_EXTRA_PATH = 'additional/J_regressor_extra.npy'
COCOPLUS_REGRESSOR_PATH = 'additional/cocoplus_regressor.npy'
H36M_REGRESSOR_PATH = 'additional/J_regressor_h36m.npy'
VERTEX_TEXTURE_PATH = 'additional/vertex_texture.npy'
CUBE_PARTS_PATH = 'additional/cube_parts.npy'

# ------------------------ Constants ------------------------
FOCAL_LENGTH = 5000.
REGRESSOR_IMG_WH = 256

# ------------------------ Joint label conventions ------------------------
# The SMPL model (im smpl_official.py) returns a large superset of joints.
# Different subsets are used during training - e.g. H36M 3D joints convention and COCO 2D joints convention.
# You may wish to use different subsets in accordance with your training data/inference needs.

# The joints superset is broken down into: 45 SMPL joints (24 standard + additional fingers/toes/face),
# 9 extra joints, 19 cocoplus joints and 17 H36M joints.
# The 45 SMPL joints are converted to COCO joints with the map below.
# (Not really sure how coco and cocoplus are related.)

# Indices to get 17 COCO joints and 17 H36M joints from joints superset.
ALL_JOINTS_TO_COCO_MAP = [24, 26, 25, 28, 27, 16, 17, 18, 19, 20, 21, 1, 2, 4, 5, 7, 8]
ALL_JOINTS_TO_H36M_MAP = list(range(73, 90))

# Indices to get the 14 LSP joints from the 17 H36M joints
H36M_TO_J17 = [6, 5, 4, 1, 2, 3, 16, 15, 14, 11, 12, 13, 8, 10, 0, 7, 9]
H36M_TO_J14 = H36M_TO_J17[:14]


