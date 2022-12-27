import os
import pickle

class ModelsManager:
    def init(self, models_folder):
        self.models_folder = models_folder
        if not os.path.exists(self.models_folder):
            os.makedirs(self.models_folder)
        self.models = {}
        
    def save(self, name, model):
        model_path = os.path.join(self.models_folder, f"{name}.pkl")
        with open(model_path, "wb") as f:
            pickle.dump(model, f)
        self.models[name] = {"model": model}
    
    def load(self, name):
        model_path = os.path.join(self.models_folder, f"{name}.pkl")
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    
    def load_all(self):
        for model_name in os.listdir(self.models_folder):
            model_name = model_name.split(".")[0]
            self.load(model_name)