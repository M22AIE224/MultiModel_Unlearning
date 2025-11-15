from huggingface_hub import snapshot_download

from huggingface_hub import login


snapshot_download(
    repo_id="meta-llama/Llama-3.2-11B-Vision",
    local_dir="./vanilla_llama",
    local_dir_use_symlinks=False,
    resume_download=True,
)

