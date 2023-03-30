package com.github.luleyleo.emotivate.state

import android.media.MediaRecorder
import android.util.Log
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.getValue
import androidx.compose.runtime.setValue
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.github.luleyleo.emotivate.api.Client
import com.github.luleyleo.emotivate.state.ActionSelector
import kotlinx.coroutines.launch
import java.io.File
import java.io.IOException
import com.github.luleyleo.emotivate.state.Emotion

class ConversationViewModel(initialState: ConversationUiState = ConversationUiState()) : ViewModel() {
    var uiState = initialState
        private set

    var isRecording by mutableStateOf(false)
        private set

    private var actionSelector = ActionSelector()

    private var client = Client()
    private var recorder: MediaRecorder? = null
    private var recorderFile: File? = null

    fun sendMessage(_transcript: String, audio: File) {
        uiState.addMessage(Message("me", "now", "<voice note>"))

        viewModelScope.launch {
            try {
                val transcript = client.getTranscript(audio)
                uiState.addMessage(Message("me", "now", transcript))
                //val diagram = client.getAffectArousalDiagram(transcript, audio)
                val emotion=client.getAffectArousal(transcript, audio)
                uiState.addMessage(Message("bot", "now", "Your emotions:", emotion = emotion))

                //TODO: get strings from server
                val action=actionSelector.selectAction(emotion.valence, emotion.arousal)
                uiState.addMessage(Message("bot", "now", action))

            } catch (e: Exception) {
                uiState.addMessage(Message("bot", "now", "Error:\n" + e.message))
            }
        }
    }

    fun startRecording(outFile: File): Boolean {
        recorder = MediaRecorder().apply {
            setAudioSource(MediaRecorder.AudioSource.MIC)
            setOutputFormat(MediaRecorder.OutputFormat.MPEG_4)
            setAudioEncoder(MediaRecorder.AudioEncoder.HE_AAC)
            setAudioChannels(2)
            setAudioSamplingRate(44100)
            setAudioEncodingBitRate(1411000)
            setOutputFile(outFile)
        }

        try {
            recorder?.prepare()
            recorder?.start()
            recorderFile = outFile
            isRecording = true

            return true
        } catch (e: IOException) {
            Log.e("Error", "MediaRecorder::prepare failed")
            recorder = null
        }

        return false
    }

    fun stopRecording(): File? {
        recorder?.stop()
        recorder?.release()
        recorder = null
        isRecording = false

        val recorderFile = recorderFile
        this.recorderFile = null
        return recorderFile
    }
}