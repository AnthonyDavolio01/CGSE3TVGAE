


import mdtraj as md
import sys
sys.path.append('DeepLearningExamples/DGLPyTorch/DrugDiscovery/SE3Transformer/')

from typing import Tuple

import dgl
import pathlib
import torch
from dgl.data import QM9EdgeDataset
from dgl import DGLGraph
from torch import Tensor
from torch.utils.data import random_split, DataLoader, Dataset
from tqdm import tqdm

from se3_transformer.data_loading.data_module import DataModule
from se3_transformer.model.basis import get_basis
from se3_transformer.runtime.utils import get_local_rank, str2bool, using_tensor_cores

from se3_transformer.data_loading import QM9DataModule
from se3_transformer.runtime.arguments import PARSER


from se3_transformer.data_loading import DCDDataModule


#qm9_kwargs = dict(label_keys=['homo'], verbose=False, raw_dir='./data')
#full_dataset = QM9EdgeDataset(**qm9_kwargs)
#print(full_dataset)



#exit()
args = PARSER.parse_args()
fUCK = DCDDataModule(**vars(args))

print(fUCK)
exit()
args = PARSER.parse_args()
qm9=QM9DataModule(**vars(args))

c=qm9._collate

print(c)


exit()
from dig.threedgraph.dataset import QM93D
from dig.threedgraph.dataset import MD17
from dig.threedgraph.method import SphereNet #SchNet, DimeNetPP, ComENet
from dig.threedgraph.method import run # main function
from dig.threedgraph.evaluation import ThreeDEvaluator # MAE for QM9 and MD17

device = torch.device('cuda:0') if torch.cuda.is_available() else torch.device("cpu")
print(device)

dataset = QM93D(root='dataset/')
print(dataset)