from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="MLLMMU/MLLMU-Bench",
    repo_type="dataset",
    local_dir="data/MLLMU-Bench",
)


snapshot_download(
    repo_id="therem/CLEAR",
    repo_type="dataset",
    local_dir="data/CLEAR",
)