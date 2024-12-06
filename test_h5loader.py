from dataloader.h5 import H5Loader

config = {
    "data": {
        "path": "../../../../../../media/doha/SSK Drive/dataset/MVSEC/",
    },
    "loader": {
        "batch_size": 1,
    },
}

try:
    loader = H5Loader(config, num_bins=10)
    print("H5Loader initialized successfully.")
    loader.close_files()
except Exception as e:
    print(f"Error: {e}")
