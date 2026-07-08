import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 1. 보컬 파일 로드 (sr=None으로 설정하여 원본 음질 유지)
audio_path = r'vocal-pitch-matcher\music\FightingGoldVocal.mp3'  # 파일 경로 입력
y, sr = librosa.load(audio_path, sr=None)

# 2. 크로마 특징량 추출 (기본 CQT 방식이 음정 분석에 가장 정확합니다)
chroma = librosa.feature.chroma_cqt(y=y, sr=sr)

# 3. 시각화 그래프 그리기
plt.figure(figsize=(12, 4))
# x축은 시간(time), y축은 12개 음명(chroma)
librosa.display.specshow(chroma, y_axis='chroma', x_axis='time', cmap='coolwarm')

plt.colorbar(label='Intensity')
plt.title('Vocal Pitch Analysis (Chroma Cens)')
plt.tight_layout()
plt.show()