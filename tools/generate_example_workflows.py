from __future__ import annotations

import copy
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / "example_workflows"

TASKS = (
    ("01", "Instruct TTS (Description)", "Instruct-TTS", False, "你好，欢迎使用 AuK ComfyUI 原生节点。", "自然、清晰、温暖的年轻女性声音", "instruct_tts"),
    ("02", "Zero-Shot TTS (Voice Clone)", "Voice-Clone", True, "你好，这是使用参考声音生成的测试音频。", "", "voice_clone"),
    ("03", "Speech Content Editing", "Speech-Content-Editing", True, "把“今天下午开会”改成“明天上午开会”", "今天下午开会，请大家准时参加。", "speech_content_edit"),
    ("04", "Lyric Editing", "Lyric-Editing", True, "把歌词“明天你好”改成“未来你好”", "明天你好，声音多渺小。", "lyric_edit"),
    ("05", "Pitch Editing", "Pitch-Editing", True, "+1", "", "pitch_edit"),
    ("06", "Speed Editing", "Speed-Editing", True, "1.25", "", "speed_edit"),
    ("07", "Volume Editing", "Volume-Editing", True, "+5", "", "volume_edit"),
    ("08", "Emotion Editing", "Emotion-Editing", True, "悲伤", "", "emotion_edit"),
    ("09", "Timbre Editing", "Timbre-Editing", True, "低沉磁性的年轻男声", "", "timbre_edit"),
    ("10", "De-accent", "De-accent", True, "去掉方言口音，转换成标准普通话", "", "deaccent"),
    ("11", "Nonverbal Sound Editing", "Nonverbal-Sound-Editing", True, "在“欢迎回来”后增加笑声", "", "nonverbal_sound_edit"),
    ("12", "Whisper Conversion", "Whisper-Conversion", True, "转换成耳语", "", "whisper_conversion"),
    ("13", "Speech Enhancement", "Speech-Enhancement", True, "去噪并去除房间混响", "", "speech_enhancement"),
    ("14", "Audio Quality Restoration", "Audio-Quality-Restoration", True, "补充高频并提升清晰度", "", "audio_quality_restoration"),
    ("15", "Speaker Separation", "Speaker-Separation", True, "第一个开始说话的人", "", "speaker_separation"),
    ("16", "Music Vocal Separation", "Music-Vocal-Separation", True, "只保留歌声，去掉说话和伴奏", "", "music_vocal_separation"),
    ("17", "Target Speaker Extraction", "Target-Speaker-Extraction", True, "欢迎大家来到今天的节目", "", "target_speaker_extraction"),
)


def main() -> None:
    no_audio = json.loads((WORKFLOW_DIR / "AuK-01-Instruct-TTS.json").read_text(encoding="utf-8"))
    with_audio = json.loads((WORKFLOW_DIR / "AuK-03-Speech-Content-Editing.json").read_text(encoding="utf-8"))
    for path in WORKFLOW_DIR.glob("AuK-*.json"):
        path.unlink()
    for number, label, file_slug, needs_audio, primary, secondary, save_name in TASKS:
        workflow = copy.deepcopy(with_audio if needs_audio else no_audio)
        loader = next(node for node in workflow["nodes"] if node["type"] == "AuKModelLoader")
        generator = next(node for node in workflow["nodes"] if node["type"] == "AuKGenerateEdit")
        saver = next(node for node in workflow["nodes"] if node["type"] == "SaveAudio")
        loader["widgets_values"] = ["AuK Base", "auto", "auto"]
        generator["widgets_values"] = [
            label,
            primary,
            secondary,
            3.0,
            42,
            "randomize",
            32,
            2.0,
            -1.0,
            "Auto Estimate (TTS Recommended)",
        ]
        saver["widgets_values"] = [f"auk/{save_name}"]
        if needs_audio:
            audio_loader = next(node for node in workflow["nodes"] if node["type"] == "LoadAudio")
            audio_loader["widgets_values"] = ["auk_input.wav"]
        path = WORKFLOW_DIR / f"AuK-{number}-{file_slug}.json"
        path.write_text(json.dumps(workflow, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
