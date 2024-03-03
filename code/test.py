import torch











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