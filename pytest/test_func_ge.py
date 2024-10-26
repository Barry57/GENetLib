from GENetLib.sim_data_func import sim_data_func
from GENetLib.func_ge import func_ge

def test_grid_func_ge():
  func_continuous = sim_data_func(n=10, m=30, ytype='Continuous', seed=123)
  func_ge_res = func_ge(func_continuous['y'], func_continuous['z'], func_continuous['location'], 
                        func_continuous['X'], 'Continuous', 'Bspline', num_hidden_layers=1, nodes_hidden_layer=[2], 
                        Learning_Rate2=0.035, L2=0.01, Learning_Rate1=0.02, L=0.01, Num_Epochs=1, 
                        nbasis1=5, params1=4, Bsplines=5, norder1=4, model=None, split_type=0, ratio=[7,3], plot_res=False)
  assert func_ge_res is not None
