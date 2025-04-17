# mosec_emb

Embedding service with mosec that is compatible with OpenAI embedding API.

## Usage

```bash
EMB_MODEL=thenlper/gte-base python main.py
```

You can find more embedding models from the [HuggingFace Embedding LeaderBoard](https://huggingface.co/spaces/mteb/leaderboard).

## Dev

```bash
envd up
```

## Images

You can use the prebuilt image from `ghcr`: [kemingy/mosec_emb](https://github.com/kemingy/mosec_emb/pkgs/container/mosec_emb).

```bash
docker run --rm -p 8000:8000 ghcr.io/kemingy/mosec_emb:latest
```

Or build your own image:

```bash
# docker
docker build .
# envd
envd build :serving
```

## Test

```bash
python client.py
```
