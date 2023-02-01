import pickle

dumped_model = pickle.dump(model,open("pickle_file", "wb"))
loaded_model = pickle.load(open("pickle_file", "rb"))
