<div align="center">

# ComfyUI-AuK (English Edition)

**Native ComfyUI integration for AuK / AuK-Flash Speech Generation & Audio Editing**

Based on [T8mars/Comfyui-Auk-T8](https://github.com/T8mars/Comfyui-Auk-T8) and Tencent's [AuK](https://github.com/Tencent-Hunyuan/AuK)

[Model repository (Hugging Face)](https://huggingface.co/t8star/Auk-Comfy) · [Official AuK Repository](https://github.com/Tencent-Hunyuan/AuK)

</div>

---

A standalone, native ComfyUI V3 custom node package for **AuK**, **AuK-Flash**, and **Qwen2.5-Omni-3B**. All inference executes directly within the ComfyUI process with native ComfyUI memory management and stage-based VRAM offloading.

### Features in this English Edition:
- **Full English UI:** Node titles, input/output socket names, tooltips, and floating task guide boxes are in English.
- **17 English Task Types:** Fully translated task options covering text-to-speech, voice cloning, audio editing, enhancement, and voice separation.
- **Bilingual Backwards Compatibility:** Preserves legacy alias mappings so workflows created with Chinese labels load and execute without validation errors.
- **Native ComfyUI Model Paths:** Seamlessly checks `models/auk` and standard ComfyUI model directories.

---

## Nodes

### 1. AuK Model Loader
Loads AuK models directly into ComfyUI with stage-based CPU offloading.
- **Model:** Choose between **AuK Base** (high quality, CFG & step controls) and **AuK-Flash** (fast 4-step distilled generation).
- **Device:** `auto`, `cuda:N`, or `cpu`.
- **Precision:** `auto`, `bf16`, `fp16`, or `fp32`.

### 2. AuK Generate / Edit
Executes the full suite of AuK speech generation and audio editing tasks:
- **Task:** Select from 17 supported tasks.
- **Primary Content:** Spoken text, replacement text, semitones, decibels, speed multiplier, or sound event instruction.
- **Voice Description / Context (optional):** Voice prompt for Instruct TTS, or transcript context for duration estimation.
- **Target Duration (Seconds):** Target output length in seconds (0.2s – 30s).
- **Seed:** Randomize or set fixed seed.
- **Input / Ref Audio:** Source audio for cloning, editing, enhancement, or separation.
- **NFE Steps & CFG Strength:** Sampling steps and guidance scale (AuK Base).
- **Duration Mode:** `Auto Estimate (TTS Recommended)` or `Manual Duration`.

---

## Supported Tasks

| Category | Task | Description |
| :--- | :--- | :--- |
| **Speech Generation** | **Instruct TTS (Description)** | Generate speech from text with natural language voice description (no audio input needed). |
| | **Zero-Shot TTS (Voice Clone)** | Speak new target text cloned from reference audio. |
| **Audio Editing** | **Speech Content Editing** | Insert, delete, or replace words in speech recordings. |
| | **Lyric Editing** | Edit lyrics in isolated vocal/a cappella recordings while preserving melody. |
| | **Pitch Editing** | Adjust vocal pitch by semitones (±1, ±2, ±3). |
| | **Speed Editing** | Adjust tempo/speed (0.5x, 0.75x, 1.25x, 1.5x, 2.0x). Duration scales automatically. |
| | **Volume Editing** | Adjust volume levels by decibels (±5, ±10, ±15 dB). |
| | **Emotion Editing** | Modify vocal emotion (happy, sad, angry, fearful, surprised, disgusted, calm, excited). |
| | **Timbre Editing** | Transform vocal timbre using descriptive prompts. |
| | **De-accent** | Remove regional accents or dialects into standard speech. |
| | **Nonverbal Sound Editing** | Add or remove nonverbal sounds (laughter, sigh, cough, breath). |
| | **Whisper Conversion** | Convert speech between whispering and normal voice. |
| **Restoration & Separation** | **Speech Enhancement** | Denoise, remove hum, and dereverberate room acoustics. |
| | **Audio Quality Restoration** | Restore high frequencies, expand bandwidth, and remove muffled/telephone artifacts. |
| | **Speaker Separation** | Separate and isolate speakers based on speaking order. |
| | **Music Vocal Separation** | Extract singing vocals from music mix or remove instruments. |
| | **Target Speaker Extraction** | Isolate a specific speaker matching a spoken anchor phrase. |

---

## Installation

Clone this repository into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/hellonearthis/Comfyui-Auk-T8
cd Comfyui-Auk-T8
pip install -r requirements.txt
```

---

## Model Setup

Place the model checkpoints under `ComfyUI/models/auk/`:

```text
ComfyUI/models/auk/
├── AuK/
│   ├── auk_base.safetensors
│   ├── vae.safetensors
│   └── config.yaml
├── AuK-Flash/           (optional for fast 4-step)
│   ├── auk_flash.safetensors
│   ├── vae.safetensors
│   └── config.yaml
└── Qwen2.5-Omni-3B/
    ├── config.json
    ├── generation_config.json
    ├── model-00001-of-00003.safetensors
    ├── model-00002-of-00003.safetensors
    ├── model-00003-of-00003.safetensors
    └── (tokenizer and config files)
```

Weights can be downloaded from:
- [t8star/Auk-Comfy](https://huggingface.co/t8star/Auk-Comfy) (bundled checkpoints)
- [tencent/AuK](https://huggingface.co/tencent/AuK) & [Qwen/Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B)

Alternatively, run the downloader:
```bash
python download_models.py --variant base
```

---

## Example Workflows

Pre-configured, drag-and-drop workflows in English for all 17 tasks are located in the [`example_workflows/`](example_workflows/) directory:
- `AuK-01-描述生成语音.json` (Instruct TTS)
- `AuK-02-参考声音克隆.json` (Zero-shot Voice Clone)
- `AuK-03` through `AuK-17` covering all editing, enhancement, and separation modes.

---

## Credits & Acknowledgements

- **Tencent Hunyuan Team:** For open-sourcing the [AuK](https://github.com/Tencent-Hunyuan/AuK) foundation model.
- **T8star / T8mars:** For the original [Comfyui-Auk-T8](https://github.com/T8mars/Comfyui-Auk-T8) node implementation and runtime architecture.
- **Qwen Team:** For [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B).

## License

Code is licensed under the [MIT License](LICENSE). Models retain the licenses and terms provided by their respective authors.
