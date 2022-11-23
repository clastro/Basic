### np.newaxis 차원을 늘려 줌

X_train = X_train[:,:,np.newaxis]
train_dataset = TensorDataset(torch.from_numpy(X_train))
test_dataset = TensorDataset(torch.from_numpy(X_train))
