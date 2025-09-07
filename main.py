from gwascat import Gwasapi

if __name__ == "__main__":
    api = Gwasapi()
    study = api.get_study('GCST000854')
    print(study)