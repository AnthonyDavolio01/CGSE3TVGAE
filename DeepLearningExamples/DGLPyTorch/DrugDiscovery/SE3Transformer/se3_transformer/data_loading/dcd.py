
import torch.distributed as dist
from abc import ABC
from torch.utils.data import DataLoader, DistributedSampler, Dataset

from se3_transformer.runtime.utils import get_local_rank

from se3_transformer.data_loading.data_module import DataModule

import mdtraj as md
import sys
sys.path.append('../../../')


class DCDDataModule(DataModule):
    def __init__(self,
                  batch_size: int = 1,
                  num_workers: int = 1,
                  **kwargs):
        super().__init__(batch_size=batch_size, num_workers=num_workers, collate_fn=self._collate)
        full_dataset = DCDDataset()
        print(full_dataset.__getitem__(0))

    def prepare_data(self):
        pass

    def _collate(self, samples):
        batched_graph, node_feats, edge_feats, targets = 0 #Placeholder
        return batched_graph, node_feats, edge_feats, targets

    #def __repr__(self):
    #    return f'DCDDataModule(dcd={self.dcd}, psf={self.psf}, traj={self.traj})'



from dgl.data.dgl_dataset import DGLDataset
from dgl.convert import graph as dgl_graph
import numpy as np

class DCDDataset(DGLDataset):
    def __init__(self,
                 dcd: str='data/monte_carlo/0lig.dcd',
                 psf: str='data/monte_carlo/0lig.psf',
                 **kwargs
                 ):
        self.dcd = dcd
        self.psf = psf

    def load(self):
        self.traj = md.load(self.dcd, top=self.psf)

    def __getitem__(self, idx):
        src=0
        dst=0
        g=dgl_graph(src,dst)
        return g,'fuck'
    
    def __len__(self):
        return 1 #Placeholder
    
    def has_cache(self):
        return True
    