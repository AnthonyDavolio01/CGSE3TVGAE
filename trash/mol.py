### Tools to convert between molecular representations
### This is from when I was trying to use distance to represent the adjacency matrix


import mdtraj as md
import numpy as np
import scipy

### All atomistic (without hydrogen)

def topology_to_features(dcd,psf):
    mol = md.load(dcd,top=psf)
    atomTypes=[]
    pruneH=[]
    for atom in mol.topology.atoms:
        atomType=atom.element.symbol
        if atomType=='H':
            pruneH.append(atom.index)
        elif atomType not in atomTypes:
            atomTypes.append(atomType)
    atomFeature={}
    for type in range(len(atomTypes)):
        atomFeature[atomTypes[type]]=np.zeros(len(atomTypes)).astype(int)
        atomFeature[atomTypes[type]][type]=1

    n_nodes=mol.xyz.shape[1]-len(pruneH)        # Each non-H atom is a node
    n_features=len(atomFeature)
    X=np.zeros(shape=(n_nodes,n_features))
    counter=0
    for atom in mol.topology.atoms:
        if atom.element.symbol!='H':
            X[counter]=atomFeature[atom.element.symbol]
            counter+=1
    return X, pruneH




def cartesian_from_dcdNpsf(dcd, psf, pruneH):
    # Convert .dcd and .psf files to cartesian coordinates (prune H atoms)
    mol = md.load(dcd,top=psf)
    full = mol.xyz
    prunedCart = np.delete(full, pruneH, axis=1)
    return prunedCart


def molgraph_from_cartesian(cartesian):
    # Convert cartesian coordinates to molecular graph
    n_nodes=cartesian.shape[0]        # Each atom in the cartesian matrix is a node
    A=np.zeros(shape=(n_nodes,n_nodes))

#    distance=np.linalg.norm(cartesian[:,np.newaxis]-cartesian,axis=2)
#    print(distance)
#    print(distance.shape)
    print('begin')
    distance=scipy.spatial.distance_matrix(cartesian,cartesian)
    print(distance)
    print(distance.shape)
    exit()
    return








### All atomistic results in an adjacency matrix with 11.1 GiB of memory
'''
def molgraph_from_cartesian_allAtomistic(cartesian):
    # Convert cartesian coordinates to molecular graph, all atomistic
    n_nodes=cartesian.shape[0]        # Each atom is a node
    A=np.zeros(shape=(n_nodes,n_nodes))
    for i in range(n_nodes):
        for j in range(n_nodes):
            A[i,j]=np.linalg.norm(cartesian[i]-cartesian[j])
    return A

def atomFeaturize(dcd, psf):
    # Get the number of unique atoms in the system
    mol = md.load(dcd,top=psf)
    atomTypes=[]
    for atom in mol.topology.atoms:
        atomType=atom.element.symbol
        if atomType not in atomTypes:
            atomTypes.append(atomType)
    atomFeature={}
    for type in range(len(atomTypes)):
        atomFeature[atomTypes[type]]=np.zeros(len(atomTypes)).astype(int)
        atomFeature[atomTypes[type]][type]=1
    return atomFeature

def features_from_dcdNpsf_allAtomistic(dcd, psf):
    # Convert .dcd and .psf files to features
    # Features won't change from frame to frame (for now)
    mol = md.load(dcd,top=psf)
    #n_frames=mol.xyz.shape[0]
    n_nodes=mol.xyz.shape[1]        # Each atom is a node
    featureDic=atomFeaturize(dcd,psf)
    n_features=len(featureDic)
    X=np.zeros(shape=(n_nodes,n_features))
    counter=0
    for atom in mol.topology.atoms:
        X[counter]=featureDic[atom.element.symbol]
        counter+=1
    X=np.array(X,dtype="int")
    return X
    
def cartesian_from_dcdNpsf(dcd, psf):
    # Convert .dcd and .psf files to cartesian coordinates
    mol = md.load(dcd,top=psf)
    return mol.xyz
'''