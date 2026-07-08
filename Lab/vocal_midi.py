import pretty_midi

# 1. 죠죠 노래 MIDI 파일 불러오기
midi_data = pretty_midi.PrettyMIDI(r'vocal-pitch-matcher\music\fightinggold1.mid')

# 2. 보컬(멜로디) 트랙 선택하기
# 여기서는 예시로 첫 번째 트랙(instruments[0])을 보컬 트랙이라고 가정합니다.
vocal_track = midi_data.instruments[5]

print(f"선택된 트랙 이름: {vocal_track.name}")

# 3. 정답 음정 데이터 추출해서 리스트에 담기
vocal_pitches = []

for note in vocal_track.notes:
    # note.pitch: MIDI 음정 번호 (예: 60, 62, 64...)
    # pretty_midi.note_number_to_hz: MIDI 번호를 주파수(Hz)로 변환
    pitch_hz = pretty_midi.note_number_to_hz(note.pitch)
    
    # (시작시간, 끝시간, 음정Hz) 형태로 저장
    vocal_pitches.append({
        "start": note.start,
        "end": note.end,
        "pitch_hz": pitch_hz
    })

# 4. 상위 5개 노지만 출력해서 확인해보기
for i, note_info in enumerate(vocal_pitches[:5]):
    print(f"[{i+1}번째 음] 시간: {note_info['start']:.2f}초 ~ {note_info['end']:.2f}초 | 음정: {note_info['pitch_hz']:.1f} Hz")