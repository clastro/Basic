# LIST EXTEND 처럼 사용할 때

rfe_X_train = np.concatenate((X_train.values[:1000],X_train.values[-100000:-99000],X_train.values[-1000:]), axis = 0)
rfe_y_train = np.concatenate((y_train.values[:1000],y_train.values[-100000:-99000],y_train.values[-1000:]), axis = 0)

