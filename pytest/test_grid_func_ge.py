from GENetLib.sim_data_func import sim_data_func
from GENetLib.grid_func_ge import grid_func_ge
import matplotlib
matplotlib.use('Agg')

def test_func_ge():
  func_continuous = sim_data_func(n=500, m=30, ytype='Continuous', seed=123)
  func_ge_res = grid_func_ge(func_continuous['y'], func_continuous['z'], func_continuous['location'], func_continuous['X'], 
                             'Continuous', 'Bspline', num_hidden_layers=2, nodes_hidden_layer=[100,10], Learning_Rate2=[0.009, 0.01],
                             L2=[0.002, 0.003], Learning_Rate1=[0.02], L=[0.01], Num_Epochs=50, nbasis1=5, params1=4, Bsplines=5, norder1=4, 
                             model=None, split_type=1, ratio=[3, 1, 1], plot_res=False)
  assert func_ge_res is not None
