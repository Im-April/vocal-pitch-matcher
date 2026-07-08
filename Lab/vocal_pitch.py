import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

# 1. 보컬 음원 파일 불러오기
file_path = r'vocal-pitch-matcher\music\FightingGoldVocal.mp3'  # 파일 경로 입력
y, sr = librosa.load(file_path, sr=None)

# 2. 피치(주파수) 추출하기 (YIN 알고리즘 사용)
# fmin: 보컬 최저 주파수 한계(보통 65Hz), fmax: 최고 주파수 한계(보통 2093Hz)
pitches, magnitudes = librosa.piptrack(y=y, sr=sr, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

# 또는 더 직관적인 YIN 알고리즘 사용 (연속적인 피치 트래킹에 유리)
f0 = librosa.yin(y=y, sr=sr, fmin=librosa.note_to_hz('C2'), fmax=librosa.note_to_hz('C7'))

# 무음 구간(피치가 0에 가깝거나 무의미한 값) 처리 (NaN으로 변환하여 그래프에서 제외)
f0[f0 == librosa.note_to_hz('C2')] = np.nan 

# 3. 결과 확인 (시간별 주파수 Hz 배열)
print("시간대별 주파수(Hz) 배열:", f0)

# 4. 피치 변화 그래프 그리기
times = librosa.times_like(f0, sr=sr)
plt.figure(figsize=(12, 4))
plt.plot(times, f0, label='Pitch (F0)', color='blue', linewidth=2)
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.title('Vocal Pitch Tracking')
plt.grid(True)
plt.show()