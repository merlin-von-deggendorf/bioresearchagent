from gwascat import Gwasapi

if __name__ == "__main__":
    api = Gwasapi()
    metadata = api.get_metadata()
    print(metadata)