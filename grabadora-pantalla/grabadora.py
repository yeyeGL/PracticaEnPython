import cv2
import numpy as np
import pyautogui
import sounddevice as sd
import wavio
import threading
import time
from moviepy.editor import VideoFileClip, AudioFileClip

# Variables globales
recording = False
audio_recording = []

# Configuración de velocidad
SCREEN_CAPTURE_INTERVAL = 0.01
AUDIO_SAMPLERATE = 44100  


def record_audio():
    global audio_recording
    audio_recording = []
    
    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_recording.append(indata.copy())
    
    with sd.InputStream(callback=callback, channels=1, samplerate=AUDIO_SAMPLERATE):
        while recording:
            sd.sleep(100)  


def record_screen():
    global recording
    screen_size = pyautogui.size()  
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("output.avi", fourcc, 20.0, screen_size)

    while recording:
        img = pyautogui.screenshot()  
        frame = np.array(img)  
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  
        out.write(frame)  

        time.sleep(SCREEN_CAPTURE_INTERVAL)  

    out.release()


def combine_audio_video():
    global audio_recording

    
    audio_data = np.concatenate(audio_recording, axis=0)
    wavio.write("audio_output.wav", audio_data, AUDIO_SAMPLERATE, sampwidth=2)
    video_clip = VideoFileClip("output.avi")
    audio_clip = AudioFileClip("audio_output.wav")
    
    if audio_clip.duration > video_clip.duration:
        audio_clip = audio_clip.subclip(0, video_clip.duration) 
    
    
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile("final_output.mp4", codec="libx264", audio_codec="aac")


def start_recording():
    global recording
    recording = True
    audio_thread = threading.Thread(target=record_audio)
    audio_thread.start()
    print("grabacion iniciada")
    threading.Thread(target=record_screen).start()


def stop_recording():
    global recording
    recording = False

    
    time.sleep(1)

   
    combine_audio_video()
    print("grabacion detenida y archivos guardados")


def menu():
    global recording
    while True:
        print("\nOpciones:")
        print("1. Iniciar grabacion")
        print("2. Detener grabacion")
        print("3. Salir")
        choice = input("Seleccione una opcion: ")

        if choice == '1':
            if not recording:
                start_recording()
            else:
                print("La grabacion ya esta en curso")
        elif choice == '2':
            if recording:
                stop_recording()
            else:
                print("No hay grabacion en curso")
        elif choice == '3':
            if recording:
                stop_recording()
            print("Saliendo")
            break
        else:
            print("Opcion no valida")

# Ejecutar el menu
if __name__ == "__main__":
    menu()
