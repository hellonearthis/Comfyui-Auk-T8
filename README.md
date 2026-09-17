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
- **Natural English & Bilingual Prompts:** Directly accepts natural English phrases across all tasks with robust parsing and case-insensitivity—no Chinese characters required.
- **Bilingual Backwards Compatibility:** Preserves legacy alias mappings so workflows created with Chinese labels load and execute without validation errors.
- **Native ComfyUI Model Paths:** Seamlessly checks `models/auk`, `models/LLM`, and standard ComfyUI model directories.

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

## Supported Tasks & Prompt Guide

| Task | Primary Content Examples | Description & Notes |
| :--- | :--- | :--- |
| **Instruct TTS (Description)** | `Welcome back, you did a great job today.` | Generates speech from text. In **Secondary Content**, describe the voice (e.g. *Young female voice, gentle, warm*). |
| **Zero-Shot TTS (Voice Clone)** | `Ladies and gentlemen, thank you for coming.` | Clones the reference audio speaker's voice to speak new text. |
| **Speech Content Editing** | `Replace 'bad' with 'good'`<br>`Add 'again' after 'welcome'`<br>`Remove 'um'` | Edits spoken words while maintaining original speaker voice and tempo. Quotes can be single, double, or Chinese. |
| **Lyric Editing** | `Change 'rear view' to 'like you'` | Edits lyrics in isolated vocal/a cappella recordings while preserving singing melody and pitch. |
| **Pitch Editing** | `+2 semitones`, `-1 semitone`, `+3`, `-2` | Shifts vocal pitch up or down by 1, 2, or 3 semitones. |
| **Speed Editing** | `1.5x`, `0.75x`, `2.0x`, `0.5` | Adjusts speech tempo (0.5x, 0.75x, 1.25x, 1.5x, 2.0x). Audio duration scales automatically. |
| **Volume Editing** | `+10 dB`, `-5 dB`, `+15`, `-10` | Boosts or attenuates vocal loudness by ±5, ±10, or ±15 dB. |
| **Emotion Editing** | `Happy`, `Sad` (or `Sadness`), `Angry`, `Fearful` (or `Afraid`), `Surprised`, `Disgusted`, `Calm`, `Excited` | Adjusts vocal emotion while preserving words and speaker identity. |
| **Timbre Editing** | `Deep, resonant young male voice` | Transforms vocal timbre using natural language descriptions. |
| **De-accent** | `Remove regional accent, convert to standard pronunciation` | Removes regional dialect or non-native accents toward standard neutral pronunciation. *(Note: standardizes accents; not for cross-accent conversion like US to UK).* |
| **Nonverbal Sound Editing** | `Add laughter after 'welcome back'`<br>`Add sigh at the beginning`<br>`Remove all breath sounds` | Inserts or removes nonverbal acoustic events (laughter, breath, cough, sigh). Supports `after`, `before`, `beginning`, `end`. |
| **Whisper Conversion** | `Convert to whisper`<br>`Convert to normal speech` | Converts between standard phonation and whispering. |
| **Speech Enhancement** | `Denoise and remove room reverberation`<br>`Remove background noise` | Cleans noisy speech, removes background hum, and strips room reverb. |
| **Audio Quality Restoration** | `Boost high frequencies and enhance clarity`<br>`Remove telephone effect`<br>*(or leave blank)* | High-frequency bandwidth expansion and defect restoration. Supports `telephone`, `megaphone`, `underwater` (muffled), `clipping`, `dropout`, `dc offset`. |
| **Speaker Separation** | `First speaker`, `The first person to speak`, `Speaker #2`<br>*(or leave blank for 1st speaker)* | Isolates a specific speaker in a multi-speaker recording based on the order they start speaking. |
| **Music Vocal Separation** | `Keep vocals only`<br>`Keep all human voices, remove instruments` | Isolates singing vocals from accompaniment or extracts all human vocal tracks. |
| **Target Speaker Extraction** | `Welcome everyone to today's show` | Extracts a specific speaker from a multi-speaker audio by matching a phrase spoken by that target. |

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

AuK requires two sets of model files:
1. **AuK Diffusion Checkpoint** (`AuK` or `AuK-Flash`)
2. **Multimodal Language Model / Audio Encoder** (`Qwen2.5-Omni-3B`)

### 1. Download AuK Checkpoint

Choose between **AuK Base** (standard, high fidelity, 32-step CFG guidance) and/or **AuK-Flash** (fast, 4-step distilled generation):

#### Option A: AuK Base (Standard / High Fidelity)
- **Hugging Face Repository:** [tencent/AuK](https://huggingface.co/tencent/AuK/tree/main)
- **Directory:** `ComfyUI/models/auk/AuK/` (or `ComfyUI/models/checkpoints/AuK/`)
- **Required Files:** `auk_base.safetensors`, `vae.safetensors`, `config.yaml`

```bash
# Using Hugging Face CLI:
hf download tencent/AuK auk_base.safetensors vae.safetensors config.yaml --local-dir ComfyUI/models/auk/AuK
```

#### Option B: AuK-Flash (Fast 4-Step Distilled)
- **Hugging Face Repository:** [tencent/AuK-Flash](https://huggingface.co/tencent/AuK-Flash/tree/main)
- **Directory:** `ComfyUI/models/auk/AuK-Flash/` (or `ComfyUI/models/checkpoints/AuK-Flash/`)
- **Required Files:** `auk_flash.safetensors`, `vae.safetensors`, `config.yaml`

```bash
# Using Hugging Face CLI:
hf download tencent/AuK-Flash auk_flash.safetensors vae.safetensors config.yaml --local-dir ComfyUI/models/auk/AuK-Flash
```

> **Tip:** The `vae.safetensors` file (637 MB) is identical between AuK Base and AuK-Flash. If you already downloaded AuK Base, you can simply copy `vae.safetensors` into `AuK-Flash/` to save bandwidth:
> ```cmd
> copy "C:\cui\models\auk\AuK\vae.safetensors" "C:\cui\models\auk\AuK-Flash\vae.safetensors"
> ```

### 2. Download Qwen2.5-Omni-3B
Download from the official Qwen repository:
- **Model:** [Qwen/Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B)

Place the downloaded files in `ComfyUI/models/LLM/Qwen2.5-Omni-3B/` (or `ComfyUI/models/auk/Qwen2.5-Omni-3B/`):

```bash
# Using Hugging Face CLI:
hf download Qwen/Qwen2.5-Omni-3B --local-dir ComfyUI/models/LLM/Qwen2.5-Omni-3B
```

The node automatically searches for `Qwen2.5-Omni-3B` in:
- `ComfyUI/models/LLM/Qwen2.5-Omni-3B`
- `ComfyUI/models/auk/Qwen2.5-Omni-3B`
- `ComfyUI/models/text_encoders/Qwen2.5-Omni-3B`

> **Tip (Windows Junction / Symlink):** If you store LLMs on another drive or in `models/LLM`, you can also create a directory junction without duplicating 11 GB:
> ```cmd
> mklink /J "C:\cui\models\auk\Qwen2.5-Omni-3B" "C:\cui\models\LLM\Qwen2.5-Omni-3B"
> ```

---

### Complete Folder Layout

```text
ComfyUI/models/
├── auk/
│   ├── AuK/                                 <-- From https://huggingface.co/tencent/AuK/tree/main
│   │   ├── auk_base.safetensors
│   │   ├── vae.safetensors
│   │   └── config.yaml
│   └── AuK-Flash/                           <-- (Optional) From https://huggingface.co/tencent/AuK-Flash/tree/main
│       ├── auk_flash.safetensors
│       ├── vae.safetensors
│       └── config.yaml
└── LLM/                                     (or inside models/auk/ or models/text_encoders/)
    └── Qwen2.5-Omni-3B/                     <-- From https://huggingface.co/Qwen/Qwen2.5-Omni-3B
        ├── config.json
        ├── generation_config.json
        ├── preprocessor_config.json
        ├── chat_template.json
        ├── model.safetensors.index.json
        ├── model-00001-of-00003.safetensors
        ├── model-00002-of-00003.safetensors
        ├── model-00003-of-00003.safetensors
        ├── tokenizer.json
        ├── tokenizer_config.json
        ├── spk_dict.pt
        └── (remaining config/tokenizer files)
```

### Alternative: Bundled Downloader
To download all models bundled into `models/auk/` from [t8star/Auk-Comfy](https://huggingface.co/t8star/Auk-Comfy):
```bash
python download_models.py --variant base
# or for fast 4-step:
python download_models.py --variant flash
```

---

## Example Workflows

Pre-configured, drag-and-drop workflows in English for all 17 tasks are located in the [`example_workflows/`](example_workflows/) directory:
1. `AuK-01-Instruct-TTS.json` — Instruct TTS (from natural language voice description)
2. `AuK-02-Voice-Clone.json` — Zero-Shot Voice Clone (from reference audio)
3. `AuK-03-Speech-Content-Editing.json` — Speech Content Editing (word replacement, insertion, deletion)
4. `AuK-04-Lyric-Editing.json` — Lyric Editing (in singing vocals)
5. `AuK-05-Pitch-Editing.json` — Pitch Editing (semitones: ±1, ±2, ±3)
6. `AuK-06-Speed-Editing.json` — Speed Editing (0.5x, 0.75x, 1.25x, 1.5x, 2.0x)
7. `AuK-07-Volume-Editing.json` — Volume Editing (decibels: ±5, ±10, ±15 dB)
8. `AuK-08-Emotion-Editing.json` — Emotion Editing (happy, sad, angry, surprised, calm, etc.)
9. `AuK-09-Timbre-Editing.json` — Timbre Editing (transform vocal timbre via descriptions)
10. `AuK-10-De-accent.json` — De-accent (convert regional accents to standard speech)
11. `AuK-11-Nonverbal-Sound-Editing.json` — Nonverbal Sound Editing (add/remove laughter, sigh, breath)
12. `AuK-12-Whisper-Conversion.json` — Whisper Conversion (whisper <-> normal speech)
13. `AuK-13-Speech-Enhancement.json` — Speech Enhancement (denoise and dereverberate)
14. `AuK-14-Audio-Quality-Restoration.json` — Audio Quality Restoration (bandwidth restoration & clarity)
15. `AuK-15-Speaker-Separation.json` — Speaker Separation (isolate speakers by speaking order)
16. `AuK-16-Music-Vocal-Separation.json` — Music Vocal Separation (extract singing vocals from music)
17. `AuK-17-Target-Speaker-Extraction.json` — Target Speaker Extraction (extract speaker matching anchor phrase)

---

## Credits & Acknowledgements

- **Tencent Hunyuan Team:** For open-sourcing the [AuK](https://github.com/Tencent-Hunyuan/AuK) foundation model.
- **T8star / T8mars:** For the original [Comfyui-Auk-T8](https://github.com/T8mars/Comfyui-Auk-T8) node implementation and runtime architecture.
- **Qwen Team:** For [Qwen2.5-Omni-3B](https://huggingface.co/Qwen/Qwen2.5-Omni-3B).

## License

Code is licensed under the [MIT License](LICENSE). Models retain the licenses and terms provided by their respective authors.
